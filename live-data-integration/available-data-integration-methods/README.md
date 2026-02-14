---
---

# Available Data Integration Methods

### Overview

Agentnoon supports multiple data integration methods to accommodate different system architectures, security requirements, and operational preferences. Each method is designed to support scheduled data refreshes and secure ingestion. Detailed setup instructions are available in the corresponding subpages.

#### 1. Importing via SFTP

SFTP-based integration is suited for organizations that prefer file-based data transfers using secure, controlled network access.

Data is exported from source systems as CSV files and uploaded to an Agentnoon-managed SFTP server on a defined cadence. Access is secured through SSH key authentication and IP whitelisting. This method is commonly used for batch-based integrations and environments with strict network controls.

**Best for:** Scheduled batch uploads, enterprise security environments, file-based exports.

#### 2. Importing via REST API

The REST API integration enables programmatic data uploads directly into Agentnoon.

Data is submitted as CSV files via authenticated API requests, allowing customers to automate uploads as part of existing data pipelines or workflows. This method provides flexibility in how and when data is sent, while maintaining schema alignment and secure transfer.

**Best for:** Automated pipelines, developer-driven integrations, custom data workflows.

#### 3. Importing from Workday (Reporting as a Service)

Agentnoon supports direct integration with Workday using **Reporting as a Service (RaaS)**.

This approach leverages Workday reports exposed via secure endpoints, allowing Agentnoon to retrieve data on a scheduled basis without requiring intermediate file handling. Configuration includes report setup within Workday and authentication between systems. Due to the depth of configuration options, this integration is covered in a dedicated, detailed guide.

**Best for:** Workday customers seeking direct, report-driven data synchronization.

***

Each integration method supports secure data transfer and customer-defined refresh schedules. Select the method that best aligns with your source systems and operational requirements, then refer to the corresponding guide for detailed setup instructions.
