---
description: >-
  Securely importing data via SFTP enables you to automate and manage
  large-scale data transfers directly into Agentnoon
---

# Importing Data via SFTP

### Prerequisites

To begin using Agentnoon’s SFTP data import service, the following setup is required:

#### 1. SSH Key and IP Whitelisting

You must provide:

* A valid **SSH public key**
* Your **corporate IP address range** to be whitelisted

Once received and configured by the Agentnoon team, you will be granted access to the appropriate regional SFTP server.

#### 2. SFTP Server Regions

SFTP endpoints based on the region where your data is hosted:

| Region             | SFTP Host Address             |
| ------------------ | ----------------------------- |
| United States (US) | `sftp-us.agentnoon.co`        |
| Europe (EU)        | `sftp-eu.agentnoon.co`        |
| Singapore          | `sftp-singapore.agentnoon.co` |
| Australia          | `sftp-australia.agentnoon.co` |
| Doha               | `sftp-doha.agentnoon.co`      |
| UAE                | `sftp-uae.agentnoon.co`       |

Please connect to the SFTP server corresponding to your data region.

#### 3. Connection Parameters

| Parameter       | Value                         |
| --------------- | ----------------------------- |
| **Protocol**    | SFTP                          |
| **Port**        | 22                            |
| **User**        | Your **Board ID** (see below) |
| **Auth**        | SSH key authentication        |
| **Upload path** | /upload                       |

#### 4. How to Find Your Board ID

The **Board ID** is a unique identifier for your organization on Agentnoon and serves as your SFTP username. To locate it:

1. Log in to the Agentnoon platform.
2.  If you're logged into Agentnoon, you can find your Board ID directly from the URL in your browser. It appears **after the last forward slash** in the URL. For example:

    > **URL:** `https://app.agentnoon.com/bd_xk2ENLcqdzZCZANji3YCBU`\
    > **Board ID:** `bd_xk2ENLcqdzZCZANji3YCBU`

Use this Board ID as the **username** when connecting to the SFTP server.

#### 5. IP Addresses for Whitelisting

Provide the following IPs to your network security team if needed:

| Region | IP Address Range |
| ------ | ---------------- |
| US     | `34.122.221.102` |
| UAE    | `4.161.49.183`   |

### Best Practices and Troubleshooting

**File Format Consistency:** Uploaded file must be a CSV and have the same columns as configured previously. For special format and processing requests, please contact support@agentnoon.com.

**Data Refresh:** After the data is processed:

* The connected organization’s data will refresh within **20 minutes**.
* Users may need to **refresh their browser 2–3 times** to clear cached data and view updated information.

**Timeout error:** This typically indicates your **IP is not yet whitelisted**. Contact your IT team to verify your public IP and share it with Agentnoon.

**File not processed:** Ensure the file structure matches the required format. Incorrect formats will not be imported.
