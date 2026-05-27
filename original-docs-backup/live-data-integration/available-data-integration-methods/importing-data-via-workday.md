---
icon: server
---

# Importing Data via Workday

### Overview

This guide explains how to allow Agentnoon to securely access Workday via REST API in order to pull **all employee data**, including basic profile information, compensation details, and any custom fields. We outline the end-to-end process, from required setup in Workday to best practices for using the API. Workday’s REST APIs provide a flexible way to retrieve HR data (e.g., personal details, job info, pay data) in real-time. By following this guide, you can enable Agentnoon to integrate with Workday while maintaining security and proper governance of your data.

### Prerequisites

Before beginning, ensure the following prerequisites are met:

* **Workday Tenant and Admin Access:** You have access to a Workday tenant (Sandbox or Production) with administrative privileges to configure integrations. This is required to create integration users, security groups, and API clients.
* **Integration System User (ISU):** Create a dedicated Integration System User in Workday for the Agentnoon integration, if one does not already exist. Use the **Create Integration System User** task to create a new user with a username/password . Add this user to the “System Users” group so their password never expires. (Each integration should have a distinct ISU account for security and to allow fine-grained access control.)
* **Tenant OAuth2 Enabled:** Verify that OAuth 2.0 is enabled for your Workday tenant. An admin can check this by editing the Tenant Setup – Security and confirming that “OAuth 2.0 Clients Enabled” is checked. If not, enable this setting to allow API client registrations.
* **Workday API Access License:** Generally, Workday’s API is available to customers as part of the Workday system. Ensure your organization’s Workday contract or configuration permits API integrations (in most cases, it does by default). No special license is typically required for basic API usage, but confirm that the needed web services or API features (e.g., Workday Web Services for Human Resources) are not restricted in your tenant.
* **Workday Community Access (optional):** If you have a Workday Community account, you can refer to official Workday documentation for APIs and support articles. (This is not mandatory for configuration, but can be helpful for troubleshooting.)

### Setting Up API Client Credentials

Next, you will register the Agentnoon’s application in Workday and configure OAuth2 credentials (Client ID/Secret and scopes) for API access. This registration establishes the **client credentials** that the Agentnoon Data Foundry will use to authenticate to Workday’s REST API.

**1. Register the API Client in Workday:** In your Workday tenant, search for the task **“Register API Client for Integrations”** and launch it. (If the integration will use a user-based OAuth flow instead of an ISU, you would use **“Register API Client”** for regular users, but in this case, we assume an Integration System User.) On the **Register API** **Client for Integrations** form, fill in the following:

* **Client Name:** Enter a descriptive name for the vendor application (e.g., “Agentnoon Integration”).
* **Grant Type:** Select **Authorization Code Grant**. (Workday requires using an authorization code flow even for integrations; you will later generate a refresh token for the ISU instead of doing an interactive user authorization.)
* **Access Token Type:** Select **Bearer** (the standard token type).
* **Redirect URI:** This cannot be used for an integration client (since we won’t use an interactive browser OAuth flow). If the form requires it, you can supply a placeholder URI as app.agentnoon.com
* **Scopes (Functional Areas):** In the Scopes section, add all relevant functional areas that the Agentnoon needs to access. For pulling employee data, this typically includes **“Human Resources (Staffing)”** for worker data. Also include **Compensation** and any other domains that might contain employee info (e.g. ,if pulling organizational assignments, include “Organizations and Roles”). If custom fields are implemented via custom objects, also enable the **Custom Objects** scopes (both System and Integration). When in doubt, it is acceptable to select all scopes under the necessary categories to ensure coverage.
* **Include Workday-owned Scopes:** Check this option if available. This ensures that the client can access core Workday data within Workday’s global (tenant non-configurable) scope.
* **Refresh Token Configuration:** Select **Non-Expiring Refresh Token** (sometimes worded as “Refresh Token Expiry: Never”). This allows the client to use a refresh token that never expires, so the integration can continually fetch new access tokens without requiring manual re-authentication.

Submit the form (click **OK**) to register the client. Workday will save the client and display the details on a **View API Client** page.

**2. Note the Client Credentials and Endpoints:** After registration, record the **Client ID** and **Client Secret** generated by Workday. These are shown on the View API Client page. Also note the **OAuth2 Token Endpoint** and the **Base REST API Endpoint** for your tenant . On the View API Client page, Workday typically lists the base URLs. For example:

* **REST API Endpoint:** https://{host}.workday.com/ccx/api/v1/{tenant} – this is the base URL for calling Workday REST API (where {host} is your data center host and {tenant} is your tenant name).
* **Token Endpoint:** https://{host}.workday.com/ccx/oauth2/{tenant}/token – this is the endpoint to obtain OAuth tokens (it may be shown on the client details page or derived from your tenant host).
* **Authorization Endpoint:** (if needed, for interactive auth) likely https://{host}.workday.com/ccx/oauth2/{tenant}/authorize (not used in a direct ISU integration scenario).

Make sure to copy the Client ID and Client Secret securely; you will provide these to the Agentnoon’s Integration Team. Treat the Client Secret like a password (store it securely and do not expose it). Agentnoon recommends using a service such as [https://onetimesecret.com/](https://onetimesecret.com/) to share the credentials.

**3. Associate the API Client with the ISU (Generate Refresh Token):** Now, you need to connect the API client to the Integration System User and get a refresh token that the Agentnoon can use. On the **View API Client** for Integrations page of the client you just created, open the related actions menu (often an ellipsis “…” next to the client name). Choose **“API Client > Manage Refresh Tokens for Integrations”**. In the dialog, select the Integration System User account that will be used by this client (the ISU created in prerequisites) as the **Workday Account**, and confirm to generate a refresh token. Workday will display a **Refresh Token** value (a long string). Copy this token **once** and store it securely – this is essentially the offline credential Agentnoon will use to get API access tokens. (If you navigate away, you may not be able to view the same token again; you’d have to generate a new one if lost.) Ensure the refresh token is marked as non-expiring, since we set this in the client config. The ISU is now linked to the OAuth 2.0 client.

At this stage, you have the **client ID, client secret**, and a **refresh token** for the integration. These will be used by Agentnoon’s integration process to authenticate and retrieve data. Typically, the application will use the OAuth 2.0 “refresh token” grant to obtain an access token on a regular basis.

**4. Obtaining an Access Token (for testing):** To confirm everything is set up, you can perform a token request. For example, using cURL, you can make the following request to get an access token using the refresh token grant type :

```bash
curl --request POST "https://{host}.workday.com/ccx/oauth2/{tenant}/token" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "grant_type=refresh_token" \
  --data-urlencode "client_id={YOUR_CLIENT_ID}" \
  --data-urlencode "client_secret={YOUR_CLIENT_SECRET}" \
  --data-urlencode "refresh_token={YOUR_REFRESH_TOKEN}"
```

If all credentials are correct, Workday will respond with a JSON containing an **access\_token** (a JWT or opaque token string) along with other info like token\_type and expires\_in. The access\_token is what must be included in API requests to Workday (in the Authorization: Bearer \<token> header). Each access token will be valid for a limited time (e.g. 30 minutes or 1 hour), after which the Agentnoon application should use the refresh token to get a new access token. We will discuss token expiration in Best Practices.

> **Note:** The above steps (client registration and token generation) usually only need to be done once during setup. Afterward, the Agentnoon application can obtain new access tokens programmatically as needed, without further manual intervention.

### Security Groups and Permissions

With the OAuth client in place, the next crucial step is to ensure the integration user has permission to retrieve all the required data. Workday’s security model uses **Security** **Groups** and **Domain Security Policies** to control access to data via APIs. In this section, we will set up a security group for the integration and grant it the necessary permissions (domains) for employee profile, compensation, and custom fields data.

**1. Create an Integration Security Group:** In Workday, search for “**Create Security Group”** and choose **“Create Security Group – Integration System (Unconstrained)”** (or **User-Based Security Group**) to create a new security group dedicated to this integration. Give it a name (e.g. “API – Agentnoon Integration SG”). This group will hold the integration user and manage the permissions for API access.

* If using an **Unconstrained Integration System Security Group**, it means the group is not limited to specific workers – it can have access to data for all workers, which is what you likely want when pulling all employee data.

**2. Add the ISU to the Security Group:** After creating the security group, add your Integration System User account as a member. This associates the user (for which the API calls will run) with the security group that will carry the permissions. You can do this in the members section of the security group or via the “Assign User-Based Security Group” task. Ensure the ISU is the only member of this group, as it is meant for that integration’s access.

**3. Grant Domain Permissions:** Now, determine which **security domains** contain the necessary data (e.g., employee profile, compensation), and grant **access** to your new security group for each of those domains. This is done via the **Domain Security Policy** administration in Workday:

* Launch the **“Domain Security for Functional Area”** task and locate domains under relevant functional areas (like “Human Resource Management” or “Compensation”). For each domain that is required, add your integration security group with **'view' or 'get'** permissions. Some important domains to consider:
  * **Worker Data: Workers –** core worker objects (needed for basic employee info).
  * **Worker Data: Public Worker Reports –** basic public info about workers (Workday often uses this for minimal profile data; it’s generally the minimum needed domain for any worker API access ).
  * **Person Data: Name** and **Person Data: Personal Data –** to retrieve legal names, personal demographics, etc. .
  * **Work Contact Information –** for the addresses, phone, and email of the worker
  * **Worker Data: Current Staffing Information –** covers job details such as employment status and job titles.
  * **Worker Data: Compensation –** provides access to worker compensation data.
  * **Worker Data: Compensation by Organization –** if needed for compensation by organizational unit.
  * **Worker Data: Employment Data and Worker Data: Employment – All Jobs –** general employment info and history.
  * **Worker Data: Organization Information –** to get the worker’s supervisory org and other org assignments.
  * **Reports: Pay Calculation Results for Worker –** if payroll or pay results data is needed (this might be beyond “compensation” basics, but included for completeness).<br>

Essentially, you should grant **“Get” (view)** access on all domains that relate to the data you want the Agentnoon to see. For **basic profile data**, the person and worker data domains listed above are key. For **compensation**, ensure that all relevant compensation domains are included (current compensation, compensation history, etc., as applicable). For **custom fields**, see the notes below. If the custom fields are part of a custom object or custom integration, you may need to enable specific domains or security policies.

> _Tip:_ Workday security can be complex. If unsure, **Workday’s Security > Domain Security for Functional Area** interface allows you to search for keywords (e.g., “Compensation”) to find domains. You can also consult the Workday Community for a list of domains needed for common integrations. For example, Merge.dev’s guide provides a list of required domains for full access to HRIS data. It’s essential to select **the correct GET-only permissions** for all necessary domains so the integration can retrieve the data without encountering “access denied” errors on certain fields.

**4. (If Custom Fields via Custom Objects) Grant Custom Object Access:** If your employee data includes custom fields that are stored in Workday as part of a **Custom Object**, you must also assign security for those. When you created the custom object, Workday would have generated security domains for that object. Typically, you should grant your integration security group access to the custom object’s domains, such as the domain for that custom object’s data. Often, Workday requires enabling “Integration” access on custom objects. For example, ensure domains like **Custom Object Data: \[Your Object Name]** are accessible, or add the security group to any integration permissions on the custom object. (In some cases, Workday documentation suggests adding the security group to the domains **Integration Security** and **Integration System** for custom objects. This step ensures the API can read the custom object’s fields.)

**5. Activate Security Policy Changes:** After making all these domain permission changes, **Activate Pending Security Policy Changes** to apply them. Workday requires security changes to be activated (and sometimes approved) before they take effect. Go to the **Activate Pending Security Policy Changes** task, review the changes, and submit to finalize them. Skipping this step can result in your integration not having the intended access, even though you configured the domains.

Once these steps are complete, your integration user (via its security group) should have the needed permissions to retrieve **worker profiles, compensation data, and custom fields**. It’s a good idea to test by retrieving one worker’s data (see next section) to confirm that all expected fields are returned. If something is missing or returns null, it usually means that an additional security domain needs to be granted.

### API Endpoints and Example Calls

Now that authentication and permissions are set up, the Agentnoon can use Workday’s REST API endpoints to pull the data. This section lists relevant API endpoints for retrieving employee information and provides examples of how to call them, along with sample request/response structures.

Workday’s REST API base URL (as noted earlier) will look like:

```shellscript
https://{host}.workday.com/ccx/api/v1/{tenant}
```

All REST endpoints we call will be relative to this base URL. The Agentnoon’s HTTP requests must include a valid **access token** in the Authorization header. For example: Authorization: Bearer {access\_token}.

Below are key endpoints and examples:

* **Get All Workers (Employee Directory):**\
  \
  **Endpoint:** GET /workers (on the base API URL).\
  \
  Description: Retrieves a list of worker records (employees) in the tenant. This is analogous to the “Get Workers” operation in Workday and will return basic information for each worker that the API user has access to. By default, this may return a paginated list of workers. The response contains an array of workers, each with fields such as worker ID, worker name, business title, and other profile fields (subject to security). For example, a simple call in code might look like:

```shellscript
GET https://{host}/ccx/api/v1/{tenant}/workers 
Authorization: Bearer {access_token}
```

* This would return an XML or JSON (depending on headers) payload of workers. Workday’s API tends to default to XML responses, which include elements like \<wd:Worker> with sub-elements for ID, name, etc. (You can request JSON by adding an Accept: application/json header or by appending ?format=json in some cases.) Each worker entry typically includes fields such as: Worker ID, Descriptor (full name), Business Title, Primary Work Email, Primary Organization, etc. . For example, the output may include:

```html
<Workers>
<WorkerID>3001234</WorkerID>
    <WorkerName>John Doe</WorkerName>
    <BusinessTitle>Software Engineer</BusinessTitle>
    <PrimaryWorkEmail>[email protected]</PrimaryWorkEmail>
    <!-- other fields -->
  </Worker>
  <!-- more Worker entries... -->
</Workers>
```

* When calling this endpoint, be mindful of **pagination**. Workday uses offset-based pagination. The API may only return a certain number of workers per call (e.g., 100). You can use query parameters like limit and offset to page through results (for example, GET /workers?limit=100\&offset=100 for the next page). Continue incrementing the offset until you receive an empty page. Always retrieve all pages to ensure you have all employees.
* **Get a Single Worker (Detailed Profile):**\
  \
  **Endpoint:** GET /workers/{WorkerID}.\
  \
  **Description:** Retrieves detailed information for a specific worker. Use this to get an individual’s full profile if needed. The {WorkerID} in the URL is typically the Workday Worker Reference ID. For example:

```shellscript
GET https://{host}/ccx/api/v1/{tenant}/workers/3001234 
Authorization: Bearer {access_token}
```

* This returns the worker resource for the given ID, including personal data, contact info, job data, etc., that the integration user is authorized to see . It will often contain nested data structures (e.g., primary location object, manager information, organization assignments). Use this endpoint if the Agentnoon needs to pull an individual profile (or if the Agentnoon only pulls changed workers one by one, for example). It’s also useful to verify that custom fields are appearing for a given worker.
* **Compensation Data:**
  1. **Worker Resource Compensation Fields:** Check if the GET /workers/{ID} response includes compensation details (such as current salary, grade, compensation plans, etc.). Workday may include compensation as a sub-object in the worker data (for example, a list of compensation plans or pay rate details), but this is often only if specifically requested or if your scopes/security allow. In some cases, the default worker response might omit detailed comp info to reduce payload size.
  2. **Compensation API Endpoints:** Workday provides specific endpoints under the **Compensation** service. For example, you might see endpoints like GET /scorecardResults or GET /workers/{ID}/compensation in documentation . These could retrieve compensation-related records (scorecards might relate to comp reviews or plans). If Workday’s REST directory offers an endpoint for worker compensation, use it. For instance, an endpoint (hypothetical) GET /workers/{ID}/compensation might return the worker’s compensation components (base pay, allowances, etc.) if available. Ensure your OAuth scope includes “Compensation” so that these calls are authorized.
  3. **Report as a Service (Custom Report):** If the native REST endpoints don’t easily expose all needed comp data (which is a common challenge), a practical solution is to create a **Custom Report** in Workday that includes the desired compensation fields (e.g., base salary, bonus, currency, etc.) along with worker info, and then expose that report via Workday’s **Report-as-a-Service (RaaS)** feature. The RaaS can be accessed via a REST URL (which is essentially an HTTPS GET returning XML or JSON). This approach is often recommended by Workday for pulling combined or custom data. For example, a custom report could join worker and comp data and be fetched at a URL like GET /ccx/service/{tenant}/ReportService/{ReportName}?format=json. This is an advanced technique, but it can simplify data retrieval by providing all needed fields in one call. (If you go this route, make sure to grant your integration security group access to the custom report in Workday.)
* In summary, to get compensation info: first, check if GET /workers or GET /workers/{ID} already includes what you need (with the proper domain permissions, you might see fields like “CompensationPlan” or “AnnualizedSalary” in the response). If not, use either specific compensation endpoints or a RaaS report. Keep in mind the Agentnoon may need to call one endpoint for basic data and another for comp data if they are separate. It is crucial to ensure the integration user has the **Worker Data: Compensation** domains or relevant security; otherwise comp fields will be blank or omitted due to security .
* **Custom Fields Data:**\
  Custom fields (often suffixed with \_\_c in Workday API outputs) will be retrieved along with their related object if configured properly. For example, if you added a custom field on the Worker object (say “Work Eligibility Status”), the API should return it as part of the worker data once the field is exposed to the integration. Workday doesn’t have a generic “custom fields” endpoint; instead, the custom fields appear in the payload of the standard endpoints (like Get Workers) when the integration is set up to include them. See the next section on how to expose custom fields via field overrides. If the custom data is a separate custom object linked to workers, there may be a REST endpoint for that custom object (e.g., GET /customObjects/{CustomObjectName}/{ID}), but typically using a field override or report is simpler.

**Example API Call and Response:**

Below is a simplified example of using cURL to fetch workers, and a snippet of the kind of response you might expect:

```shellscript
# Example: Fetch first 100 workers
curl -X GET "https://{host}/ccx/api/v1/{tenant}/workers?limit=100" \
  -H "Authorization: Bearer {access_token}"
```

**Response (XML snippet):**

```xml
<Workers total="350" offset="0" limit="100">
  <Worker>
    <WorkerID>3001234</WorkerID>
    <Descriptor>John Doe</Descriptor>
    <ID type="Employee_ID">E12345</ID>
    <PrimaryWorkEmail>[email protected]</PrimaryWorkEmail>
    <BusinessTitle>Software Engineer</BusinessTitle>
    <PrimaryOrganization>
      <Descriptor>Engineering</Descriptor>
      <ID type="SupervisoryOrg">SUPERVISORY_ORG-45</ID>
    </PrimaryOrganization>
    <IsManager>false</IsManager>
    <Location>
      <Descriptor>New York Office</Descriptor>
      <ID type="Location_ID">LOC-001</ID>
    </Location>
    <!-- ... other fields ... -->
  </Worker>
  <!-- 99 more Worker entries ... -->
</Workers>

```

In this example, total="350" indicates there are 350 workers in total; the call returned the first 100 (limit="100") starting at offset="0". To get all workers, you would iterate: next call with offset=100, then 200, etc., until you retrieve all 350. The fields shown (WorkerID, Descriptor (name), email, title, org, etc.) are examples of profile data. If compensation or custom fields are configured, additional elements would appear (for instance, \<Compensation> or a custom field \<CustomFieldName\_\_c> might show up if available).

The **Agentnoon’s application** should parse these responses (XML or JSON) and extract the needed fields. Many developers use JSON for ease of parsing; you can obtain JSON by adding the appropriate header or using Workday’s JSON support if available. Otherwise, parsing XML as shown with libraries (e.g., using Nokogiri in Ruby as demonstrated in some guides ) is an option.

### Handling Custom Fields

Handling custom fields in Workday’s API requires additional configuration, as standard API calls are not included by default. Custom fields in Workday (often created via **Create Custom Object** or as **Custom Attributes** on existing objects) need to be exposed to integrations. Here are two primary methods to retrieve custom fields:

**1. Use an Integration Field Override Service:** Workday provides a feature called **Field Override** for integrations, which allows you to specify additional fields (including custom fields) that should be returned by certain API operations (like Get Workers). The general steps are:

* **Create a Field Override Service:** In Workday, search “Create Integration Field Override Service”. Create a new override, give it a name (e.g. ,“Custom Worker Fields Override”), and select the business object that you want to extend – in this case, **Worker**. In the service definition, add entries for each custom field you want the API to return. For example, if you have a custom field “Work Eligibility Status” on the worker, add that field in a new row. Do this for all relevant custom fields (you can select from any custom objects or calculated fields related to the Worker). Save the service.
* **Attach to an Integration System:** If you have an Integration System (which can just be a dummy integration object) for this purpose, you can attach the field override. Since we are using an OAuth API client and ISU, one approach is to create a no-code integration system as a container. Use the **Create Integration System** task to make a new integration system of type “Cloud Integration” (this can just serve as a host for the field override) . Then, on that integration system’s related actions, go to **Integration System > Configure Integration Services**, and add the Field Override Service you created to the **Custom Integration Services** section. This links the override definition to an integration system. Next, go to **Integration System > Configure Integration Field Overrides** for the same integration. For each field in the service, map it to the actual Workday field; often, it will auto-select if you have chosen the field in the service. Essentially, you’re confirming which fields will be overridden/included .
* **Use the Integration System ID in API requests:** When making the **Get Workers** call via SOAP, one would include a reference to this Integration System’s ID in the request payload (in the Provider\_Reference of the request criteria) . For the REST API, if you use the newer endpoint /workers, you might not have an obvious way to reference the integration system. In such cases, the Field Override might automatically apply to all Get\_Workers responses for that integration user. (Workday documentation implies that if an ISU is associated with an API client and that ISU has an integration system with a field override, the override fields may be included in responses for that ISU). If that’s not the case, the alternative is to use the SOAP-based endpoint with the field override reference.

Using a Field Override Service is the official way to include custom fields in the output of Workday web services. It may require a bit of Workday config (as above), but once set up, the Agentnoon will start seeing the custom fields in the data payload. Custom fields typically appear with a double underscore (\_ \_) \_\_c suffix in JSON or by their custom name in XML. For example, if you have a custom field “Work Eligibility Status”, the API might return an element like \<Work\_Eligibility\_Status\_\_c> in the XML or "workEligibilityStatus\_\_c": "Eligible" in JSON. Make sure the integration user’s security group has access to these custom fields (Workday often treats custom object data as separate domains). With the field override attached and security granted, the API calls we discussed (e.g., GET /workers) will include those fields in each worker’s data.

**2. Use a Custom Report (RaaS) to expose custom fields:** Another approach, if the above is too complex, is to create a custom **Advanced Report** that includes all the custom fields (and any standard fields) you need, then enable that report as a web service (RaaS). In the report definition, you can include fields from the worker and any related custom objects. Once the report is built and shared with the integration security group, the Agentnoon can call the report’s URL (with .json or .xml format) and get all the fields in one dataset. Many integrations choose this method because it gives full control over which fields are output (including calculated fields) without needing to manipulate the core API. The trade-off is that it’s less of a “real-time transaction” and more reporting-oriented, but if you schedule the Agentnoon to pull periodically, it works well. For custom fields, especially, this is often the quickest path recommended (as noted in community forums).

When using custom reports, you still use the same OAuth token for authentication, and the URL would be under /ccx/service/ rather than /ccx/api/. But since the question focuses on REST API, the primary method remains the Field Override if you want to stick to direct API calls.

> **Important:** No matter which method, ensure that the integration user has security access to the custom fields. This might involve granting access to the custom object’s domain or marking the fields as reportable. If you followed the field override approach, test by calling a single worker and verifying that the custom field values are present. If they are missing, double-check the field override configuration and security policy for those fields.

### Best Practices and Security Considerations

Enabling an Agentnoon to access sensitive employee data requires careful attention to security and adherence to best practices. Below are recommendations to ensure the integration is robust and secure:

* **Use a Dedicated Integration User:** We have done this by creating an ISU – continue to use that account exclusively for this integration. Do not share a single integration user across multiple vendors or systems. This way, access can be tightly controlled and audited for each integration. If the vendor integration should be discontinued, you can simply deactivate that one user and its API client without affecting others.
* **Principle of Least Privilege:** Grant only the minimum domains and permissions required for the vendor’s data needs. While we listed many domains for full profile and comp data, periodically review if all are necessary. For example, if the vendor doesn’t need home addresses, you could revoke the “Personal Data: Home Contact” domain. Fewer permissions reduce risk. Also, do not give any **Modify** permissions – the vendor in this scenario only needs read access (“Get”). Verify that the security group has only “Get” (view) access on domains, not “Put” or higher, to prevent any changes in Workday from the API.
* **Secure the Client Credentials:** The Client ID and Client Secret, as well as the Refresh Token, should be stored securely by the vendor. They should be treated like passwords. Ideally, the vendor uses a secure secrets storage or vault. Never hard-code secrets in code or config files that are publicly accessible. If you ever suspect a credential leak, you can revoke the refresh token (via Workday’s Manage Refresh Tokens screen), which will invalidate it and issue a new one as needed.
* **Access Token Usage:** Access tokens issued by Workday have an expiration, typically on the order of minutes or hours. The vendor integration should be built to handle this. Typically, use the access token for API calls; if a call returns a 401 Unauthorized and the token has likely expired, the integration should automatically use the refresh token to get a new access token, then retry the API call. It’s a good practice to proactively refresh the token before it expires (or catch the expiration and refresh). Because we set the refresh token as non-expiring, it can be reused indefinitely. However, the access token will need to be refreshed periodically. Do not wait until the token fully expires if you have continuous data pulls; refresh on a schedule (e.g., if the token life is 30 min, refresh every 25 min). This ensures seamless data retrieval.
* **Rotate Credentials if Needed:** While non-expiring refresh tokens and long-lived secrets are convenient, it’s wise to rotate them periodically for security (for example, generate a new client secret or refresh token annually and update the vendor’s config). Workday allows you to regenerate the client secret if needed. Coordinate rotation with the vendor to avoid downtime.
* **Audit and Monitoring:** Enable and monitor **integration event logs** in Workday. Workday logs API calls made by an integration user. Regularly review these logs to see which API calls are being made, where they are coming from, and how often. This can help identify any unusual activity. Also, consider creating an alert in Workday for failed login attempts or other security events on the integration user. Since this is an Agentnoon, you may also ask them to provide an audit log of their access for compliance purposes.
* **API Rate Limits and Efficiency:** Workday does have throttling mechanisms to protect performance, although exact rate limits are not publicly documented. Ensure the vendor’s integration is efficient in its API usage. For example, they should **batch or paginate** requests rather than calling one record at a time in a tight loop (which could be slow and load-intensive). If pulling all employees nightly, pulling 100 or 1000 at a time is better than pulling 1 at a time. If Workday returns a HTTP 429 (Too Many Requests) or similar, the integration should back off and retry after a delay. Generally, staying under a few calls per second is advisable unless otherwise informed. Also, avoid pulling the same data too frequently; if the vendor only needs a daily refresh, schedule the calls responsibly.
* **Use Caching for Static Data:** If certain data doesn’t change often (like organization structures or job profiles), the vendor should cache it on their side instead of calling Workday repeatedly for it. This reduces load on the Workday API.
* **Timeouts and Retries:** The vendor application should handle network issues gracefully. If the Workday API call times out or fails due to a transient error, the vendor can retry after a short wait. However, they should also implement a reasonable retry limit to avoid infinite loops. Workday’s uptime is high, but network hiccups can occur.
* **Protect Personal Data:** Even though the integration is authorized, remember that the data being transmitted is sensitive (PII like names, contact info, compensation). Ensure that data is transmitted over HTTPS (Workday API is always HTTPS) and that the vendor secures the data on their end. It’s good practice to have a data protection agreement in place with the vendor. All exports or logging of this data should be controlled.
* **Token Scope and Revocation:** We gave a non-expiring refresh token to the vendor. If at any point the vendor should no longer have access, you can **revoke the refresh token** in Workday (via the same Manage Refresh Tokens screen). This immediately prevents new access tokens from being obtained. Also consider limiting the scope of data by adjusting security rather than relying solely on the honor system. For example, if the vendor is only supposed to pull data for active employees, you might add a condition in a custom report or integration that filters out others, or provide them with an API filter (if available) to only get active workers.
* **Testing in Sandbox:** Always test the full integration in a non-production Workday environment if possible. Create some sample workers with test data and have the vendor run their API calls. This will validate that the OAuth flow, permissions, and data mapping all work before exposing real production data. It also helps fine-tune what domains or fields might be missing. Once confirmed, replicate the configuration in Production.
* **Keep Documentation Updated:** Provide the vendor with up-to-date API documentation (e.g., Workday’s official API docs for the version your tenant is on). The vendor should know what endpoints are available and the data structures. Workday’s API can change with new versions, so be mindful during Workday updates if any API changes could affect the integration. Having open communication with the vendor about Workday maintenance windows or updates is also a best practice.

By following these practices, you ensure that the Agentnoon’s integration runs smoothly, does not compromise security, and continues to function even as things change (like token expiration or new Workday releases). In summary, always prioritize data security and plan for error handling in the integration.

### Common Pitfalls and How to Avoid Them

Finally, here are some common pitfalls encountered in setting up Workday API integrations and tips on avoiding them:

* **Using the Wrong URL/Endpoint:** One frequent mistake is using an incorrect Workday host URL or service path. For example, using a sandbox (**-impl**) URL for production, or missing the “ccx” portion. Always use the **Public Web Services** report in Workday to find your correct base host. The URL should be in the format given earlier. Ensure that if you are connecting to production, your URL does **not** contain “-impl-” (which indicates a Workday implementation tenant). Additionally, make sure you are using the /ccx/api/v1/tenant endpoints for REST and /ccx/oauth2/tenant/token for token calls. Double-checking the endpoint against Workday documentation is critical – using the wrong endpoint (e.g., calling a non-existent resource or the wrong version) will lead to frustration.
* **OAuth Client Not Enabled or Misconfigured:** If your token request is failing, verify that OAuth is enabled in the tenant (see Prerequisites) and that the client’s scopes cover the needed areas. A missing scope can lead to HTTP 403 Forbidden for certain API calls, even if the token is valid. If you get an OAuth error like “invalid\_client” or “invalid\_request”, ensure the token URL and credentials are correct (Client ID/Secret exact, refresh token correct and not expired). Remember that Workday’s OAuth for integrations typically uses the refresh token grant – a direct client credentials grant will **not** work unless specifically enabled (Workday often expects an initial refresh token to be generated via the UI) . The example in the Stack Overflow case was resolved by using the refresh token grant instead of client\_credentials.
* **Security Policy Not Activated:** After changing domain security permissions, if the API still returns “permission denied” or doesn’t show a field, it might be that the security changes weren’t activated. Always run the **Activate Pending Security Changes** task and ensure it completes successfully. Until activated, your changes are not live.
* **Missing Permissions (Null or Missing Fields):** If certain fields like compensation or personal data come back as null or not present in the API response, it usually means the integration user lacks permission for those fields. Go back to Domain Security Policies and find which domain controls that field. For instance, pay rate or comp info missing -> check **Worker Data: Compensation** domains; personal email missing -> check **Public Work Email** domain, etc. Using Workday’s Security Diagnostic reports can help identify which domain a field belongs to. The Merge help article specifically notes that missing pay info means some domains for compensation aren’t enabled . The solution is to add the security group to those domains and activate changes.
* **Integration User Not Associated with Correct Security Group or Environment:** Make sure the ISU is in the right security group (or at all). Sometimes, one might create the group but forget to add the user to it. Also, if you have multiple Workday environments (Sandbox, Implementation, Production), ensure you set up the user, group, client, etc., in the correct one. The token and URL must all point to the same environment. A token from Sandbox won’t work on Production API endpoints, for example. Keep credentials separate for each environment.
* **Forgetting to Include Workday-Owned or Custom Object Scopes:** If you notice the API returns some data but certain sections are empty, you might have missed a scope during client registration. For instance, if custom fields aren’t coming through, did you include the Custom Objects scopes? If not, go back and update the API client (Workday allows editing scopes for an API client via the View API Client task) and then reauthorize/regenerate the token if needed.
* **Exceeding Page Size or Not Handling Pagination:** If the client only pulls the first page of /workers and stops, they’ll miss data. This is a logical pitfall. Always implement the loop to get all pages until none remain . Conversely, if the client tries to pull all workers in one huge request (if Workday were to allow a very high limit), the response could be extremely large and cause timeouts. It’s safer to page through.
* **Inefficient Pulls (impacting performance):** If a client tries to pull data too frequently (e.g. every minute pulling all employees), this could strain the system or get rate-limited. Ensure they align with an acceptable schedule, like incremental changes or a nightly full pull, depending on needs. Workday can handle frequent calls, but it’s best to be prudent.
* **Not Handling Terminated Workers or Future Hires:** “All employee data” might include active and terminated workers. By default, Get Workers could return both unless filtered. If the client only expects active employees, you may need to filter out terminated employees (perhaps by using a query parameter or a custom report). Alternatively, they should be prepared to receive terminated workers. Clarify this to avoid confusion about what “all employees” means. Similarly, future-dated hires might appear (depending on Workday settings). The integration should handle these scenarios (e.g., an employee with no active job yet, if a future hire).
* **Data Transformations:** Remember, Workday API might present data differently (IDs, reference links, etc.). A common pitfall is misunderstanding Workday IDs – for example, worker IDs vs. Workday’s UUIDs. The client should use the “Workday ID” provided in the API (which might be a GUID or numeric ID, not necessarily the employee’s employee number unless that’s configured as an ID). Ensure the client knows how to map these IDs to their system.
* **Testing with Small Data vs. Full Scale:** Sometimes an integration works on a small test set but fails with a larger volume (memory issues, etc.). Encourage the client to test with as much data as possible (perhaps using a sandbox with a sizable dataset or partial production data) to ensure their solution scales for all employees.

By anticipating these pitfalls, you can address them proactively. Double-check configuration steps if something isn’t working – it’s often one piece of the puzzle (security, URL, token) that was missed. Workday’s error messages can be a bit generic (e.g., “Unauthorized” for many issues), so systematically verifying each aspect is key. With careful setup and testing, the integration should reliably provide the Agentnoon application with the employee profile, compensation, and custom field data they need.
