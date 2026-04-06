---
description: Data upload and management questions
---

# 📊 Data & Import FAQs

Common questions about uploading, managing, and troubleshooting data in Agentnoon. Learn how to prepare your data, handle import errors, and keep your org information up-to-date.

***

## Data Requirements & Preparation

### What data format is required to upload to Agentnoon?

**Answer:** Agentnoon accepts CSV files (.csv). Files must be UTF-8 encoded with a single header row, unique column names, and no blank columns.&#x20;

**Learn more:** [Data Requirements](../data-import/data-requirements.md)

### What are the minimum required fields for a data upload?

**Answer:** Three fields are required: Position ID (unique identifier for each position), Manager's Position ID (defines reporting relationships), and Job Title. All other fields like name, department, salary, and location are optional but recommended.

**Learn more:** [Data Requirements](../data-import/data-requirements.md)

### Can I import custom fields beyond the standard fields?

**Answer:** Yes! You can import unlimited custom fields such as pay grade, cost center, business unit, employee type, or any organizational attribute you track. Custom fields can be used for filtering, highlighting, and reporting.

**Learn more:** [Data Requirements](../data-import/data-requirements.md)

### How do I prepare my CSV file to avoid upload errors?

**Answer:** Follow the data error checklist: ensure unique employee IDs, valid manager IDs (no self-reporting or circular relationships), positive salary values, consistent date formats, no blank mandatory fields, and standardized text formatting without special characters.

**Learn more:** [Data Error Checklist](../data-import/data-error-checklist.md)

***

## Upload Methods & Data Refresh

### What's the difference between full data upload and partial data upload?

**Answer:** Full data upload replaces your entire Main Org dataset—anything not in the CSV is removed. Partial data upload updates specific fields for specific employees without replacing all data, useful for salary adjustments or department changes.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### How often should we refresh data?

**Answer:** It depends on your setup. Manual CSV uploads are typically done weekly (Monday mornings) or monthly. Automated integrations can sync daily (overnight) or weekly. Most organizations refresh weekly to balance freshness with stability.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### What happens to scenarios when Main Org data is refreshed?

**Answer:** Scenarios are NOT automatically updated when Main Org refreshes. They remain as snapshots from when they were created. This preserves your planned changes and prevents new hires from unexpectedly appearing in scenarios like RIF plans.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### Can I update scenarios with new Main Org data?

**Answer:** Yes, using scenario refresh. This updates your scenario with recent Main Org changes while preserving your scenario modifications. However, this feature is still in development—check with support for availability.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### How do I perform a partial data upload?

**Answer:** Create a CSV with only the fields you want to update, always include Employee ID or Position ID to match records, then upload via Data Management → Partial Upload. Only those fields for those employees will be updated—nothing else changes.

**Learn more:** [Partial Data Upload](../scenarios/advanced-actions/partial-data-upload-1.md)

***

## Live Data Integrations

### What's the difference between manual upload vs live integration?

**Answer:** Manual upload gives you full control—you upload CSV files when needed. Live integration automatically syncs data from your HRIS (via SFTP, Workday API, or REST API) on a schedule, eliminating manual work but requiring initial setup.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### How do I set up a live data integration?

**Answer:** Contact Agentnoon support for setting up a live integration

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

***

## Troubleshooting Upload Errors

### What are the most common data validation errors?

**Answer:** Missing required fields (Employee ID, Manager ID), invalid data types (text in numeric fields), broken reporting relationships (manager doesn't exist), duplicate Employee IDs, circular reporting (manager loops), and self-reporting (employee is their own manager).

**Learn more:** [Data Error Checklist](../data-import/data-error-checklist.md)

### How do I fix broken reporting relationships?

**Answer:** Ensure every Manager ID corresponds to an existing Employee ID. Check for orphan records (manager doesn't exist), circular reporting (manager reports back to employee), and self-reporting. Fix in your HRIS, then re-upload or manually correct in Agentnoon.

**Learn more:** [Data Error Checklist](../data-import/data-error-checklist.md)

### Why is my org chart broken after data upload?

**Answer:** Likely caused by invalid manager IDs or broken reporting relationships. Go to Main Org → Data Management (admin only), look for "Broken Hierarchy" indicator with orange link icon. Click to view positions with invalid managers, then fix in HRIS and re-upload.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### A new hire from yesterday isn't showing in Agentnoon. Why?

**Answer:** Check if your HRIS has exported the new hire yet, verify sync has run since the hire was added, confirm the new hire passed data validation (no missing required fields), and if using manual upload, ensure you've uploaded the latest CSV.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

***

## Data Security & Best Practices

### How secure is my data during upload?

**Answer:** Agentnoon uses encrypted connections (HTTPS for uploads, secure SFTP for integrations). Only admins can upload data. API keys should be rotated regularly. Use access groups to restrict sensitive field visibility. Never include credentials or .env files in uploads.

**Learn more:** [Admin Overview](../admin/overview.md)

### Who can upload or refresh data?

**Answer:** Only admins have data upload and refresh permissions. Regular users can view Main Org and create scenarios, but cannot modify the underlying data source. This ensures data integrity and single source of truth from your HRIS.

**Learn more:** [Admin Overview](../admin/overview.md)

***

## Next Steps

* [**Data Requirements**](../data-import/data-requirements.md) - Detailed field requirements
* [**Data Error Checklist**](../data-import/data-error-checklist.md) - Complete validation checklist
* [**Data Refresh & Sync**](../admin/data-refresh-sync.md) - Full data management guide
* [**Admin Overview**](../admin/overview.md) - Admin capabilities and responsibilities
* [**Scenarios FAQs**](scenarios.md) - Scenario planning questions
