---
description: Fixing data upload and sync problems
hidden: false
---

# Data Issues

Common solutions for data upload errors, validation failures, broken hierarchies, missing data, and field mapping problems.

## Data Upload Errors

**CSV upload fails completely**
- Ensure file is saved as CSV (not .xlsx); verify encoding is UTF-8 (Excel: Save As > CSV UTF-8)
- Check file size (<50MB); remove empty rows/columns
- Test with a small subset (100 rows) to isolate the issue; try a different browser

**"Missing required fields"**
- Add the missing column (Position ID, Manager ID, or Job Title)
- Headers are case-sensitive and must match exactly
- Leave Manager ID blank only for the top-level position (CEO)

**"Duplicate Employee ID"**
- In Excel: select Employee ID column > Data > Remove Duplicates
- Correct so every ID is unique, then re-upload

**"Invalid Manager ID"**
- Each Manager ID must match an existing Employee ID in the file
- Check for typos, format mismatches (e.g., "001" vs "1"), or managers removed from the dataset

**"Circular reporting" or "Self-reporting"**
- Trace the reporting chain to find the loop (e.g., A → B → C → A)
- Correct one Manager ID to break the loop; an employee cannot be their own manager

## Field Mapping Issues

**Wrong fields mapped (data in wrong columns)**
- Go to Data Management > Field Mapping (Admin) and update mappings
- During upload, use the field mapping screen to map each CSV column to the correct Agentnoon field

**Custom fields not appearing**
- In Data Management > Field Mapping, add a mapping for the custom CSV column
- Choose field type (text, number, date), save, then re-upload or use partial upload

**Date format errors**
- Required format: **YYYY-MM-DD** (e.g., 2026-02-18)
- In Excel: Format Cells > Custom > `yyyy-mm-dd`
- Incorrect formats: `02/18/2026`, `18-Feb-2026`, `2026/02/18`

## Missing or Incorrect Data After Upload

**Missing employees after upload**
- Check upload report for validation errors (missing required fields, invalid manager IDs)
- Clear all filters; verify employees are within your access scope
- Partial uploads only update records in the file — use a full upload to include all employees

**Employee data incorrect after upload**
- Verify source CSV has correct values; check field mapping
- Re-upload a corrected CSV; if still wrong after re-upload, contact support

**Reporting relationships broken**
- Look for the orange broken hierarchy indicator in the toolbar
- Fix options: correct in source HRIS and re-sync, use partial upload to fix Manager IDs, or manually edit the position (temporary)

**Department / location incorrect**
- Check for inconsistent naming ("Engineering" vs "engineering", "SF" vs "San Francisco")
- Standardize in source CSV using find-and-replace, then re-upload

**Salary showing wrong amount**
- Values must be plain numbers only: `150000` not `$150,000`
- Verify field mapping points to the salary column; check currency codes (USD, EUR, GBP)

## Data Sync Issues (Live Integrations)

**Data not syncing from HRIS**
1. Go to Settings > Data Management > Integration Status
2. Check last sync time and review logs for errors:
   - Authentication failure → re-enter API credentials or SFTP password
   - Connection timeout → check firewall rules
   - Data validation error → fix source data in HRIS
   - Field mapping issue → update field mappings
3. Click Test Connection; manually trigger sync to confirm

**New hire not appearing**
- Verify sync has run since the hire was added to HRIS
- Check new hire passed validation (Employee ID, valid Manager ID, required fields filled)
- Review sync logs for errors; manually trigger sync if urgent

**Terminated employee still appearing**
- Verify termination was processed in HRIS; check if terminated employees are still included in the export
- Wait for next sync (employee will disappear automatically when excluded from export)
- For immediate removal: upload a full CSV without the terminated employee

**SFTP connection failing**
- Settings > Data Management > SFTP Integration > Test Connection
- Verify username, password, host, and port (usually 22)
- Test with FileZilla/WinSCP: if external tool also fails, the issue is the SFTP server; if it works, contact support

## Data Refresh Issues

**Refresh taking too long**
- Normal: <5,000 employees = 5–15 min; >10,000 employees = 30–60 min
- If stuck >2 hours: contact support

**Data refresh failed / rolled back**
- Check email for error notification; review Data Management > Upload History
- Fix validation errors in source CSV and re-upload
- If >10% of records have errors, the upload rolls back automatically

**Need to restore previous data**
- Re-upload your previous CSV as a full data upload
- If unavailable, export from HRIS as of a prior date or contact support for backup restoration
- Prevention: save dated CSV copies before each upload

## Validation Warnings

**Salary outliers detected**
- Review if legitimate (executives, interns, currency conversion errors)
- Check for typos (1,500,000 vs 150,000); if all are valid, proceed — it's a warning, not a blocker

**Inconsistent naming**
- Standardize values in source CSV (one format per field); use find-and-replace in Excel

## Partial Upload Issues

**Partial upload not updating records**
- Verify the unique identifier (Employee ID or Position ID) in the partial CSV matches exactly — including format (e.g., "001" vs "1")

**Partial upload created duplicates**
- IDs didn't match, so the system created new records
- Fix: run a full upload to replace duplicates, or manually delete the extra positions

## When to Contact Support

Contact SupportSWP@dayforce.com if:
- Upload fails with unclear error after trying solutions
- Data corruption occurred after upload
- Live integration stopped working completely
- Validation errors persist after fixes
- Data refresh stuck >2 hours

Include: upload timestamp, exact error message, anonymized sample CSV, screenshots, and organization name.
