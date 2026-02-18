---
description: Fixing data upload and sync problems
icon: database
hidden: false
---

# Data Issues

Common solutions for data upload errors, validation failures, broken hierarchies, missing data, and field mapping problems.

## Data Upload Errors

### CSV Upload Fails Completely

**Problem:** Data upload fails, shows error, or process doesn't start

**Cause:** File format issue, file too large, or encoding problem

**Solution:**
1. Verify file is saved as CSV format (not Excel .xlsx)
2. Open CSV in text editor to verify it's readable
3. Check file encoding is UTF-8:
   - In Excel: Save As → CSV UTF-8 (Comma delimited)
   - In Google Sheets: Download as → Comma-separated values (.csv)
4. Check file size (large files >50MB may timeout)
5. Remove empty columns and rows
6. Try uploading a smaller subset to test (first 100 rows)
7. Close and reopen file in Excel, save again as CSV
8. Try different browser if issue persists

**See also:** [Data Error Checklist](../data-import/data-error-checklist.md)

---

### "Missing Required Fields" Error

**Problem:** Upload fails with "Required field missing" error

**Cause:** CSV is missing Employee ID, Position ID, or Manager ID columns

**Solution:**
1. Check error message for which field is missing
2. Add missing column to CSV
3. Required fields:
   - **Position ID** (or Employee ID)
   - **Manager's Position ID** (or Manager ID)
   - **Job Title**
4. Ensure column headers match exactly (case-sensitive)
5. Verify every row has a value for required fields
6. Leave Manager ID blank only for top-level position (CEO)
7. Re-upload CSV

> **[Screenshot placeholder: Data upload error dialog showing "Missing required field: Manager ID" with red X icon and list of affected row numbers (rows 5, 12, 23)]**

**See also:** [Data Requirements](../data-import/data-requirements.md)

---

### "Duplicate Employee ID" Error

**Problem:** Upload fails with "Duplicate Employee ID found"

**Cause:** Same Employee ID appears multiple times in CSV

**Solution:**
1. Open CSV in Excel
2. Select Employee ID column
3. Use Data → Remove Duplicates to find duplicates
4. Investigate why duplicates exist:
   - Same person listed twice
   - Two people incorrectly assigned same ID
   - Rehire with duplicate ID
5. Correct IDs to make each unique
6. Re-upload CSV

---

### "Invalid Manager ID" Error

**Problem:** Upload shows "Manager ID not found" or "Invalid reporting relationship"

**Cause:** Manager ID in a row doesn't match any Employee ID in the dataset

**Solution:**
1. Check error report for specific rows with invalid Manager IDs
2. Verify each Manager ID exists as an Employee ID in the CSV
3. Common causes:
   - Typo in Manager ID (e.g., 12345 vs 12346)
   - Manager was terminated and removed from dataset
   - Manager ID format doesn't match Employee ID format
4. Correct Manager IDs to match existing Employee IDs
5. For top-level executives: Leave Manager ID blank or use special value
6. Re-upload CSV

> **[Screenshot placeholder: Validation error report showing "Invalid Manager ID '5678' for Employee 'John Smith' in row 47 - Manager ID does not match any Employee ID in file"]**

**See also:** [Data Error Checklist](../data-import/data-error-checklist.md)

---

### "Circular Reporting" Error

**Problem:** Upload fails with "Circular reporting relationship detected"

**Cause:** Employee reports to someone who reports back to them (reporting loop)

**Solution:**
1. Check error message for Employee IDs involved in loop
2. Example: Alice reports to Bob, Bob reports to Alice (circular)
3. Trace reporting chain to find where loop occurs
4. Correct Manager IDs to break the loop
5. Verify reporting structure follows top-down hierarchy
6. Re-upload CSV

**Common scenario:**
- Employee A → Manager B → Manager C → Manager A (loop back)
- Fix: Correct one of the Manager IDs to point to correct manager

---

### "Self-Reporting" Error

**Problem:** Upload shows "Employee cannot be their own manager"

**Cause:** Employee ID and Manager ID are the same for one or more rows

**Solution:**
1. Check error report for affected rows
2. Find rows where Employee ID = Manager ID
3. Correct Manager ID to point to actual manager
4. For CEO or top-level position: Leave Manager ID blank
5. Re-upload CSV

---

## Field Mapping Issues

### Wrong Fields Mapped

**Problem:** Data uploads but appears in wrong columns (e.g., names in salary field)

**Cause:** Field mapping is incorrect during upload

**Solution:**
1. Go to Data Management → Field Mapping (Admin only)
2. Review current mappings
3. Update mappings to match your CSV structure:
   - CSV column "Employee Name" → Agentnoon field "Name"
   - CSV column "Annual Salary" → Agentnoon field "Salary"
4. Save new mappings
5. Re-upload CSV (mappings will auto-apply)

**Alternative during upload:**
1. During CSV upload process, review field mapping screen
2. Use dropdowns to map each CSV column to correct Agentnoon field
3. Click "Skip" for columns you don't want to import
4. Complete upload with corrected mappings

---

### Custom Fields Not Appearing

**Problem:** Uploaded custom field data but fields don't show in Agentnoon

**Cause:** Custom fields not created or mapped

**Solution:**
1. Go to Data Management → Field Mapping (Admin only)
2. Look for your custom field CSV column
3. If not mapped: Click "Add Field Mapping"
4. Map CSV column to new or existing Agentnoon field
5. Choose field type (text, number, date, etc.)
6. Save mapping
7. Re-upload CSV or perform partial data upload to populate field

**See also:** [Partial Data Upload](../data-import/partial-data-upload.md)

---

### Date Format Errors

**Problem:** Dates not uploading correctly or showing as text

**Cause:** Date format doesn't match expected YYYY-MM-DD format

**Solution:**
1. Open CSV in Excel
2. Check date format in columns (Hire Date, Start Date, etc.)
3. Required format: **YYYY-MM-DD** (e.g., 2026-02-18)
4. In Excel:
   - Select date column
   - Format Cells → Custom
   - Enter: yyyy-mm-dd
   - Click OK
5. Save as CSV
6. Re-upload

**Incorrect formats:**
- ❌ 02/18/2026 (MM/DD/YYYY)
- ❌ 18-Feb-2026 (text format)
- ❌ 2026/02/18 (wrong separators)

**Correct format:**
- ✅ 2026-02-18

---

## Missing or Incorrect Data After Upload

### Missing Employees After Upload

**Problem:** Some employees don't appear in Agentnoon after data refresh

**Cause:** Employees filtered out, missing from CSV, or validation error

**Solution:**
1. Check upload report for validation errors
2. Verify employees exist in source CSV file
3. Check if employees failed validation (missing required fields)
4. Look for "orphan" records (manager doesn't exist)
5. Check if filter is hiding employees (clear all filters)
6. Verify employees are within your access scope
7. If using partial upload: Employees not in partial file won't appear
8. Use full upload to ensure all employees included

---

### Employee Data Incorrect After Upload

**Problem:** Data uploaded but values are wrong (wrong salary, title, etc.)

**Cause:** Source data incorrect, field mapping wrong, or cache issue

**Solution:**
1. Clear browser cache and refresh
2. Check source CSV to verify correct data
3. Review field mapping (Data Management → Field Mapping)
4. Check if partial upload overwrote data incorrectly
5. Perform new full upload with corrected CSV
6. If still incorrect after re-upload, contact support

---

### Reporting Relationships Broken

**Problem:** Org chart structure is incorrect, people reporting to wrong managers

**Cause:** Manager IDs don't match, or broken hierarchy in data

**Solution:**
1. Go to Main Org → Taskbar → Data Management (Admin only)
2. Look for "Broken Hierarchy" indicator (orange link icon)
3. Click to view list of positions with invalid managers
4. Options to fix:
   - **Option A:** Correct in source system (HRIS) and re-sync
   - **Option B:** Use partial upload to fix Manager IDs
   - **Option C:** Manually edit in Agentnoon (temporary fix)
5. For manual fix in Agentnoon:
   - Open position card
   - Edit → Change Manager
   - Select correct manager
   - Save
6. For permanent fix: Update source data and re-upload

> **[Screenshot placeholder: Broken hierarchy warning panel listing affected positions - "Sarah Chen reports to invalid manager ID 9999", "Mike Johnson reports to invalid manager ID 8888" with "Fix Now" buttons]**

**See also:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

---

### Department or Location Data Incorrect

**Problem:** Employees showing in wrong department or location

**Cause:** Source data incorrect or field mapping wrong

**Solution:**
1. Check source CSV for correct department/location values
2. Verify field mapping points to correct columns
3. Check for typos or inconsistent naming:
   - "Engineering" vs "engineering" (different values)
   - "San Francisco" vs "SF" (inconsistent)
4. Standardize values in source CSV
5. Re-upload with corrected data
6. Or use partial upload to fix specific records

---

### Salary or Compensation Incorrect

**Problem:** Salaries showing wrong amounts or not at all

**Cause:** Data format issue, field mapping incorrect, or currency problem

**Solution:**
1. Check CSV salary column:
   - Values must be numbers only (no $ or , symbols)
   - Use: 150000 (correct)
   - Not: $150,000 (incorrect)
2. Verify field mapping points to salary column
3. Check currency field (if separate):
   - Use standard codes: USD, EUR, GBP
4. Remove any text or special characters from salary values
5. Re-upload corrected CSV

**See also:** [Data Error Checklist](../data-import/data-error-checklist.md)

---

## Data Sync Issues (Live Integrations)

### Data Not Syncing from HRIS

**Problem:** Live integration not pulling latest data, data is stale

**Cause:** Sync failed, integration paused, or HRIS connection issue

**Solution:**
1. Go to Settings → Data Management → Integration Status (Admin only)
2. Check last sync time:
   - If recent: Data is up to date
   - If old: Sync has failed
3. Review sync logs for error messages
4. Common errors and fixes:
   - **Authentication failure:** Re-enter API credentials or SFTP password
   - **Connection timeout:** Check firewall rules, verify SFTP server accessible
   - **Data validation error:** Fix source data in HRIS, wait for next sync
   - **Field mapping issue:** Update field mappings in integration settings
5. Click "Test Connection" to verify integration
6. Manually trigger sync to confirm resolution
7. If errors persist, contact support with error logs

> **[Screenshot placeholder: Integration status dashboard showing last sync failed with red X, error message "Authentication failed: Invalid SFTP credentials", and "Retry Sync" button]**

**See also:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

---

### New Hire Not Appearing in Agentnoon

**Problem:** Employee added to HRIS yesterday but not in Agentnoon today

**Cause:** Sync hasn't run yet, new hire not in HRIS export, or validation error

**Solution:**
1. Check sync schedule (Settings → Data Management)
2. Verify sync has run since hire was added to HRIS
3. Check if new hire passed data validation:
   - Employee ID present
   - Manager ID valid
   - Required fields filled
4. Review sync logs for errors related to new hire
5. Verify new hire is included in HRIS export (not filtered out)
6. If using manual CSV upload: Re-upload with new hire included
7. Manually trigger sync if urgent

---

### Terminated Employee Still in Agentnoon

**Problem:** Employee terminated in HRIS but still appears in Agentnoon

**Cause:** Sync hasn't run yet, or terminated employee still in HRIS export

**Solution:**
1. Verify termination was processed in HRIS
2. Check HRIS export settings:
   - Does export include terminated employees?
   - Is there a status field (Active/Inactive)?
3. If terminated employees filtered out of export:
   - Wait for next sync (employee will disappear automatically)
4. If terminated employees included in export:
   - Check "Employment Status" or "Active" field
   - Update field mapping to handle terminated status
5. Manually trigger sync
6. If employee should be removed immediately: Manual CSV upload without that employee

---

### SFTP Connection Failing

**Problem:** Integration logs show SFTP connection errors

**Cause:** Credentials incorrect, firewall blocking, or SFTP server down

**Solution:**
1. Go to Settings → Data Management → SFTP Integration
2. Click "Test Connection"
3. If fails:
   - Verify username and password correct
   - Check SFTP host URL is correct
   - Verify port (usually 22 for SFTP)
   - Check firewall allows connection to SFTP server
4. Test SFTP connection using external tool (FileZilla, WinSCP):
   - Same credentials
   - Same host/port
   - If external tool works: Contact Agentnoon support
   - If external tool fails: Issue is with SFTP server or credentials
5. Contact IT to verify SFTP server is running
6. Re-enter credentials in Agentnoon and test again

**See also:** [Live Data Integration](../live-data-integration/what-is-a-live-data-integration.md)

---

## Data Refresh Issues

### Data Refresh Taking Too Long

**Problem:** Data refresh has been running for hours, not completing

**Cause:** Large dataset, complex validation, or system issue

**Solution:**
1. For organizations >10,000 employees: Refresh may take 30-60 minutes (normal)
2. For organizations <5,000 employees: Should complete in 5-15 minutes
3. If unusually slow:
   - Check browser isn't frozen (try refreshing page)
   - Verify internet connection is stable
   - Check for validation errors (may be processing slowly)
4. If refresh is stuck >2 hours: Contact support
5. Future prevention:
   - Schedule refreshes during off-hours
   - Reduce sync frequency if regular timeouts occur

---

### Data Refresh Failed / Rolled Back

**Problem:** Data refresh started but failed, reverted to previous data

**Cause:** Critical validation error or system error during processing

**Solution:**
1. Check email for error notification from Agentnoon
2. Review error message in Data Management → Upload History
3. Common causes:
   - Too many validation errors (>10% of records)
   - File encoding issue
   - System timeout
4. Fix validation errors in source CSV
5. Re-upload corrected file
6. If no clear error: Contact support with upload timestamp

---

### Can't Roll Back to Previous Data

**Problem:** Need to restore previous data version after bad upload

**Cause:** No automatic rollback feature (by design)

**Solution:**
1. Locate your previous CSV file or data export
2. If you have previous CSV:
   - Upload previous CSV as full data upload
   - Data will revert to previous state
3. If you don't have previous CSV:
   - Export from HRIS as of previous date (if supported)
   - Or contact Agentnoon support for backup restoration
4. **Prevention:**
   - Save dated copies of CSV files before each upload
   - Export Agentnoon data to CSV before major uploads (backup)
   - Test uploads on small sample first

---

## Validation and Data Quality

### Salary Outliers Detected

**Problem:** Upload shows warnings about salary outliers

**Cause:** Salaries significantly higher or lower than peers

**Solution:**
1. Review salary outlier report
2. Check if outliers are legitimate:
   - Executive salaries (expected to be high)
   - Interns or part-time (expected to be low)
   - Currency conversion errors (e.g., $150,000 vs ¥150,000)
3. Verify currency codes are correct (USD, EUR, etc.)
4. Check for data entry errors:
   - Extra zero: 1500000 instead of 150000
   - Missing zeros: 15000 instead of 150000
5. Correct errors in CSV and re-upload
6. If all outliers are legitimate: Proceed with upload (warning only)

---

### Inconsistent Naming / Data

**Problem:** Upload warnings about inconsistent department names, locations, etc.

**Cause:** Typos or variations in naming conventions

**Solution:**
1. Review consistency report
2. Standardize naming in CSV:
   - "Engineering" vs "engineering" → Choose one
   - "San Francisco" vs "SF" vs "San Francisco, CA" → Choose one format
3. Use find-and-replace in Excel to standardize
4. Create data dictionary with standard values
5. Re-upload standardized CSV
6. **Prevention:** Use dropdowns in source system to enforce consistency

---

### Missing Mandatory Fields

**Problem:** Upload shows some rows have missing required data

**Cause:** Source data incomplete

**Solution:**
1. Check error report for affected rows
2. Identify missing fields (Employee ID, Name, Manager, etc.)
3. Fill in missing data in source system or CSV
4. If data not available:
   - Use placeholder values (e.g., "TBD" for title)
   - Or remove incomplete rows from upload
5. Re-upload corrected CSV

---

## Partial Upload Issues

### Partial Upload Not Updating Records

**Problem:** Partial upload completed but changes not reflected

**Cause:** Matching field incorrect, or records not found

**Solution:**
1. Verify you selected correct unique identifier during upload:
   - Usually Employee ID or Position ID
2. Check IDs in partial CSV match IDs in Agentnoon exactly
3. Look for typos or extra spaces in IDs
4. Ensure ID format matches (e.g., "001" vs "1")
5. Re-upload with corrected IDs
6. Check for orange edit icon on cards (indicates update)

**See also:** [Partial Data Upload](../data-import/partial-data-upload.md)

---

### Partial Upload Created Duplicates

**Problem:** Partial upload created new positions instead of updating existing

**Cause:** Unique identifier didn't match, so system treated as new records

**Solution:**
1. This happens when Employee IDs in partial CSV don't match existing IDs
2. Immediate fix: Use full data upload to replace duplicates
3. Or manually delete duplicate positions (if few)
4. **Prevention:** Always verify IDs match exactly before partial upload

---

## When to Contact Support

**Contact support if:**
- Upload fails with unclear error message
- Data corruption occurred after upload
- Live integration stopped working completely
- Need to restore backup data
- Validation errors persist after fixes
- Data refresh stuck for >2 hours

**Include in support request:**
- Upload timestamp
- Error message (exact text)
- Sample CSV file (anonymized if needed)
- Screenshots of error
- Organization name

**Contact:** support@agentnoon.com

---

## Next Steps

- Return to [Troubleshooting Overview](overview.md)
- Review [Data Error Checklist](../data-import/data-error-checklist.md)
- See [Data Requirements](../data-import/data-requirements.md)
- Learn about [Data Refresh & Sync](../admin/data-refresh-sync.md)
- Try [Partial Data Upload](../data-import/partial-data-upload.md) for targeted fixes
