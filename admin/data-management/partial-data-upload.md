---
description: >-
  Update specific fields or add new records without re-uploading your entire
  dataset.
---

# Partial Data Upload

## Overview

Partial Uploads allow you to update select records or append new ones to your Agentnoon org chart without needing to import your full data file.

**Common use cases:**
- Update specific employee information (titles, salaries, departments)
- Add new hires without re-uploading entire organization
- **Add an acquired company's org alongside existing org (M&A integration)**
- Bulk update specific attributes across multiple employees
- Add temporary or contractor positions
- Append new departments or business units

**Key benefits:**
- No need to re-upload entire dataset
- Faster than full data import
- Updates or adds only what you specify
- Existing data remains unchanged unless explicitly updated

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

---

## Use Case: M&A Integration

One of the most powerful applications of Partial Upload is adding an acquired company's organization alongside your existing org for M&A integration planning.

### How It Works for M&A

**Standard data import** replaces your entire Main Org. **Partial Upload** adds the acquired company's data without replacing your existing organization.

**Result:** Both organizations exist side-by-side in your Main Org, allowing you to model integration in scenarios.

### M&A Partial Upload Workflow

#### Step 1: Prepare Acquired Company Data

Export the acquired company's org structure:
- All employees and positions
- Manager relationships
- Departments and locations
- Titles and compensation
- Any custom attributes

**Critical: Add identifying attribute**
- Add a "Company" or "Original Organization" column
- Value: "Acquired Company Name"
- This allows you to filter and distinguish between organizations

> **[Screenshot placeholder: Excel file with acquired company data including "Company" column set to "Acquired Co"]**

#### Step 2: Perform Partial Upload

1. Navigate to **Data Management → Partial Upload**
2. Upload acquired company file
3. Map fields to Agentnoon attributes
4. **Important:** Ensure unique identifiers don't conflict with existing employees
5. Confirm and process upload

#### Step 3: Verify Both Orgs Exist

After upload:
1. Navigate to Main Org > Directory
2. Filter by "Company" attribute
3. Verify both organizations appear
4. Check total headcount includes both orgs

#### Step 4: Create Integration Scenario

1. Create new scenario for M&A integration
2. Both orgs are visible as starting state
3. Model consolidation, redundancy elimination, and combined structure
4. Use effective dates to phase integration

**Learn more:** [M&A Integration Tutorial](../../use-case-tutorials/ma-integration.md)

---

## Advanced Partial Upload Scenarios

### Adding New Business Unit

**Scenario:** Your company creates or acquires a new business unit that needs to be added to Agentnoon.

**Approach:**
1. Prepare file with new business unit's positions
2. Include reporting structure (who reports to whom within the unit)
3. Define entry point: Which existing leader the new unit reports to
4. Use Partial Upload to append the unit
5. Verify new unit appears in correct location in org chart

### Bulk Attribute Updates

**Scenario:** You need to update salaries, titles, or departments for a subset of employees.

**Approach:**
1. Export current data or create file with just employees to update
2. Include unique identifier (Employee ID, Position ID)
3. Include only fields that need updating
4. Other fields remain unchanged
5. Upload and map to update existing records

**Example:**
- Update 50 employees with new titles after reclassification
- Adjust salaries for entire department after market adjustment
- Move team from Department A to Department B

### Adding Seasonal or Contract Workers

**Scenario:** Add temporary workforce without disrupting permanent employee data.

**Approach:**
1. Prepare file with contractor/seasonal employee data
2. Include Employee Type attribute (e.g., "Contractor", "Seasonal")
3. Use Partial Upload to add these positions
4. Filter by Employee Type to view or hide temporary workforce

---

## Best Practices

### Unique Identifiers

**Always use unique identifiers:**
- Employee ID (for updating existing employees)
- Position ID (for updating positions)
- Email address (if guaranteed unique)

**Why:** Without unique identifiers, Agentnoon may create duplicate records instead of updating existing ones.

### Testing First

**For major partial uploads:**
1. Test with small subset first (5-10 records)
2. Verify upload behaves as expected
3. Check for duplicates or unexpected changes
4. Then upload full dataset

### Backup Before Upload

**Create backup scenario:**
1. Duplicate your Main Org as a scenario before major partial upload
2. If upload has issues, you have reference to original state
3. Allows rollback if needed

### Data Validation

**Before uploading:**
- Check for missing required fields
- Verify manager relationships are valid
- Ensure unique identifiers are correct
- Validate data types (numbers as numbers, dates as dates)
- Remove any test or dummy data

### Communication

**For major partial uploads affecting many users:**
- Notify stakeholders before upload
- Communicate what's changing and why
- Provide timeline for when changes will appear
- Offer support for questions after upload

---

## Common Issues and Solutions

### Issue: Duplicate Records Created

**Cause:** Unique identifier not mapped correctly, or identifiers don't match between files.

**Solution:**
- Delete duplicate records
- Re-upload with correct unique identifier mapping
- Ensure Employee ID/Position ID values match exactly between files

### Issue: New Records Don't Appear in Org Chart

**Cause:** Missing manager relationship or invalid Manager ID.

**Solution:**
- Check that Manager ID exists in your org
- Verify manager field is mapped correctly
- Update records to include valid manager relationships
- Detached records appear at top level until manager assigned

### Issue: Updates Don't Apply

**Cause:** Unique identifier not found in existing data.

**Solution:**
- Verify identifier values match exactly (no extra spaces, case-sensitive)
- Check that records you're trying to update actually exist
- If adding new records, don't expect updates to non-existent IDs

### Issue: Wrong Fields Updated

**Cause:** Field mapping incorrect during upload process.

**Solution:**
- Review field mapping carefully before confirming
- Cancel and restart upload if mapping looks wrong
- Partial uploads are additive - you may need to undo changes manually

### Issue: M&A Upload Replaces Existing Org

**Cause:** Used standard data import instead of Partial Upload.

**Solution:**
- Contact Agentnoon support to restore if recent
- Use Partial Upload feature specifically (not standard import)
- Verify you're in Partial Upload workflow before uploading

---

## Permissions

**Who can perform Partial Uploads:**
- Administrators
- Users with data management permissions

**If you need Partial Upload access:**
- Contact your Agentnoon administrator
- Request data management permissions
- Provide business justification for access

**Security considerations:**
- Partial uploads can modify org data
- Should be restricted to trusted users
- Consider approval workflow for major uploads
- Audit trail tracks who uploaded what and when

---

## When to Use Partial Upload vs Full Data Import

### Use Partial Upload When:

✅ Updating specific employee attributes
✅ Adding new hires or positions
✅ Adding acquired company for M&A integration
✅ Appending new business unit or department
✅ Bulk updating subset of employees
✅ Adding temporary or contractor workforce

### Use Full Data Import When:

✅ Initial setup of Agentnoon
✅ Major org restructuring affecting entire company
✅ Refreshing entire dataset from HRIS
✅ Correcting fundamental data issues across all employees
✅ Starting fresh after major changes

**General rule:** Use Partial Upload for targeted changes, Full Import for complete replacement.

---

## Related Articles

- [M&A Integration Tutorial](../../use-case-tutorials/ma-integration.md) - Complete M&A workflow using Partial Upload
- [Data Import](data-import.md) - Full data import process
- [Data Requirements](data-requirements.md) - Required fields and formatting
- [Data Error Checklist](data-error-checklist.md) - Troubleshooting data issues
