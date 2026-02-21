---
description: >-
  Agentnoon supports Single Sign-On (SSO) via Microsoft Azure Active Directory
  using the SAML 2.0 protocol, allowing users to securely access the platform
---

# Microsoft SSO Integration (Azure AD)

#### 1. Consent Link for Microsoft SSO Integration

1. Shared a link for the Customer integration with Microsoft SSO.
2. Customer’s IT Admin will need to approve the app via the consent link below
   1. Consent link: please email us at [SupportSWP@dayforce.com](mailto:SupportSWP@dayforce.com) and we will send over the consent link for SSO for admins
3. Other parameters the IT admin will need.
   1. Redirect URI: [https://auth.agentnoon.com/\_\_/auth/handler](https://auth.agentnoon.com/__/auth/handler)
   2. Logout URL: [https://app.agentnoon.com/logout](https://app.agentnoon.com/logout)

#### 2. Documentation Reference

1. Reference to Microsoft Learn documentation for granting tenant-wide admin consent.
2. **Link:** [Microsoft Learn - Grant tenant-wide admin consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivot=portal)

#### 3. Testing Account

1. We will request a test account to validate the integration setup.

#### 4.  Post-Approval Actions

1. No further actions are required after the admin approval, as the configuration supports all organizational users by default.

**Action Items:**

1. Ensure the Customer’s IT Admin approves the consent link.
2. Confirm that the integration functions correctly using the provided test account.
