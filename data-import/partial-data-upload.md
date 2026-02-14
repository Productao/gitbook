---
description: >-
  Update specific fields or add new records without re-uploading your entire
  dataset.
---

# Partial Data Upload

### Overview

Partial Uploads allow you to update select records or append new ones to your Agentnoon org chart without needing to import your full data file.&#x20;

### Prepare Your Partial Dataset

1. Create a spreadsheet with only the records you want to update or add.
2. Include only the fields that need to be updated (e.g. Name, Job Title).
3. Ensure each row includes a unique identifier (like Employee ID or Position ID).
4. For new positions/employees, include a Manager ID to correctly place them in the org chart.\
   &#xNAN;_**Note: Records without a manager may appear detached from the structure.**_

<div><figure><img src="../.gitbook/assets/Screenshot 2025-04-30 at 6.27.08 PM.png" alt=""><figcaption><p>Example: Original employee dataset</p></figcaption></figure> <figure><img src="../.gitbook/assets/Screenshot 2025-04-30 at 6.29.06 PM.png" alt=""><figcaption><p>Example: Edited partial upload dataset</p></figcaption></figure></div>

### Uploading the File

1. Navigate to **Data Management → Partial Upload**&#x20;
2. Choose your file type (**Google Sheets or CSV**).
3. If using Google Sheets, paste the link.
4. Click **Upload** to begin processing the file.

### Mapping Changes

Map records to update

1. **Select a unique identifier** (e.g., Employee ID or Position ID) so Agentnoon knows which existing records to update.
2. Agentnoon auto-detects the fields present in your partial file and pre-selects them for update. \
   &#xNAN;_**Note: You don’t need to re-map fields that haven’t changed.**_
3.  Review the selected fields and make adjustments if needed before continuing.<br>

    <figure><img src="../.gitbook/assets/Screenshot 2025-11-11 at 5.40.29 PM.png" alt="" width="563"><figcaption></figcaption></figure>

Once the upload completes, your data will be refreshed. Existing records will update, and any new records will appear in the org chart. You can identify which cards have changed by looking for the orange edit icon in the bottom-left corner.

<figure><img src="../.gitbook/assets/Screenshot 2025-11-11 at 5.41.33 PM.png" alt=""><figcaption><p>Updated Org Chart</p></figcaption></figure>

<br>
