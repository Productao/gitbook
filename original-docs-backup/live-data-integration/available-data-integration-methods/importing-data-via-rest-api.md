---
description: >-
  Upload a CSV to Agentnoon's REST API using an API KEY. Ensure data matches the
  schema with your account manager. Customize the upload frequency as needed.
icon: cloud-arrow-up
---

# Importing Data via REST API

### Prerequisites

* Agentnoon account
* Valid API key for authentication. This can be requested from [support@agentnoon.com](mailto:support@agentnoon.com)
* CSV file to be uploaded.
* API endpoint URL for file upload.
* Whitelisted IP Address - Contact support@agentnoon.com to whitelist the IP address from which you will be uploading data.
* Schema Configuration - Work with your account manager to configure Agentnoon to align with the schema of the data being uploaded.
* Upload Cadence - Determine the appropriate upload frequency based on your business needs.

### Steps

1. Prepare the CSV File
2. Ensure the CSV file is properly formatted.
3. Verify that the data within the CSV file is accurate and complete.
4. Configure Agentnoon
5. Collaborate with your account manager to configure Agentnoon's schema to match the structure of the data within your CSV file.
6. Construct the API Request
7. Use an HTTP client or programming language capable of making POST requests.
8. Set the API endpoint URL as the destination for the request.
9. Include the CSV file in the request body.
10. Set the \`Content-Type\` header to \`multipart/form-data\`.
11. Include the bearer token in the \`API-KEY\` header as \`\<api-key>\`.
12. Request the Board ID to Agentnoon’s account manager
13. Send the API Request
14. Execute the constructed API request.
15. Upload API URI: https://api.agentnoon.co/v1/import-mapping/\<my\_board\_id>/import-csv-file
16. Handle the API Response
17. Check the HTTP status code of the response.
18. 200 OK indicates a successful upload.
19. Other status codes indicate errors.
20. Parse the response body for any additional information or error messages.

### Summary Checklist

1. Verify the API KEY
2. Prepare the CSV file.
3. Work with your account manager to configure the Agentnoon schema.
4. Contact support@agentnoon.com to whitelist your IP address.
5. Construct the API request.
6. Send the API request.
7. Handle the API response.

#### Example Request Headers

| Header       | Value                    |
| ------------ | ------------------------ |
| API-KEY      | \`an\_U8RgYNME5Hc88Knb\` |
| Content-Type | \`multipart/form-data\`  |

#### Example Request Body

The request body should be in \`multipart/form-data\` format, including the CSV file. The specific format will depend on the HTTP client or programming language used.

### Error Handling

| HTTP Status Code | Description                                                                                                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400              | Bad Request - The request could not be understood or contained invalid data.                                                                                                     |
| 401              | Unauthorized - Authentication failed due to an invalid or missing API Key.                                                                                                       |
| 403              | Forbidden - The request was valid, but the server is refusing to respond to it.  Contact support@agentnoon.com if you receive this error to ensure your IP has been whitelisted. |
| 415              | Unsupported Media Type - The server does not support the provided file type.                                                                                                     |
| 500              | Internal Server Error - An unexpected error occurred on the server.                                                                                                              |
