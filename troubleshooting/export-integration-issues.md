---
description: Fixing export and integration problems
hidden: false
---

# Export & Integration Issues

Common solutions for CSV export failures, PowerPoint export problems, SFTP connection errors, and integration sync issues.

## CSV Export Issues

### CSV Export Fails or Downloads Empty File

**Problem:** Export button doesn't work, or downloaded CSV file is empty

**Cause:** Filter hiding all data, permissions issue, or browser blocking download

**Solution:**
1. Clear all filters and try exporting again
2. Verify you're viewing data (not empty scenario or view)
3. Check browser download settings:
   - Allow downloads from agentnoon.com
   - Check if pop-up blocker is blocking download
4. Try different browser
5. Check browser's download folder (file may have downloaded)
6. If file downloads but is empty:
   - Apply filter to include data
   - Verify your access scope includes data
   - Try exporting smaller subset (apply filters)
7. Disable browser extensions (especially privacy extensions)
8. Try export in incognito/private mode

> **[Screenshot placeholder: Browser pop-up blocker notification showing "agentnoon.com was blocked from downloading a file" with "Always allow" option]**

---

### CSV Export Has Missing Columns

**Problem:** Downloaded CSV doesn't include expected columns

**Cause:** Columns not visible in current view, or field-level permissions

**Solution:**
1. Before exporting, verify columns are visible:
   - Click column selector (gear icon or column button)
   - Check boxes for columns you want to export
   - Apply changes
2. Scroll horizontally to confirm columns visible
3. Export again (only visible columns are exported)
4. Check field-level permissions:
   - Some fields (salary, etc.) may be hidden based on access group
   - Contact admin to verify permissions
5. If custom fields missing:
   - Verify custom fields are mapped and populated
   - Check Data Management → Field Mapping

> **[Screenshot placeholder: Column selector dialog showing checkboxes for Name (checked), Title (checked), Department (checked), Salary (unchecked/grayed out), with note "Hidden by access group"]**

---

### CSV Export Has Missing Rows

**Problem:** CSV has fewer rows than expected

**Cause:** Filters applied, access scope restriction, or export limit

**Solution:**
1. Clear all active filters before exporting
2. Check filter indicator (usually top of screen)
3. Click "Clear all filters" or reset filters
4. Verify export includes all data in view:
   - Count rows in Directory view
   - Compare to export row count
5. Check your access scope:
   - You can only export data you have permission to view
   - Contact admin if you need access to more data
6. For very large exports:
   - May be capped at 10,000 or 50,000 rows
   - Export in batches using filters
   - Contact support for bulk export assistance

---

### CSV File Won't Open in Excel

**Problem:** Excel shows error when opening CSV, or data appears corrupted

**Cause:** Encoding issue, special characters, or Excel compatibility

**Solution:**
1. Open CSV in text editor first to verify it's readable
2. Import CSV into Excel instead of opening directly:
   - Excel → Data → From Text/CSV
   - Select file
   - Choose UTF-8 encoding
   - Import
3. Try opening in Google Sheets first:
   - Upload to Google Drive
   - Open with Google Sheets
   - Download as Excel format
4. Check for special characters in data:
   - Commas in text fields (should be quoted)
   - Line breaks in cells
   - Emoji or foreign characters
5. If data looks corrupted:
   - Re-export from Agentnoon
   - Try different browser for export

---

### CSV Data Format Issues

**Problem:** Numbers showing as text, dates formatted incorrectly, or formulas appearing

**Cause:** Excel auto-formatting or CSV format interpretation

**Solution:**
1. For numbers showing as text:
   - Select column in Excel
   - Data → Text to Columns → Finish (converts to numbers)
2. For dates:
   - Dates exported as YYYY-MM-DD
   - Excel may auto-format to different format
   - Select column → Format Cells → Date → Choose format
3. For salary values:
   - Should export as plain numbers (no $ or commas)
   - If formatted: Select column → Clear formatting
4. For leading zeros (Employee IDs like 00123):
   - Format column as Text before importing
   - Or use Excel's Text to Columns → Text format
5. If formulas appear instead of values:
   - Re-export from Agentnoon (shouldn't contain formulas)
   - Or in Excel: Copy column → Paste Special → Values

---

## PowerPoint Export Issues

### PowerPoint Export Fails

**Problem:** PowerPoint export button doesn't work or download fails

**Cause:** Browser blocker, large org chart, or timeout

**Solution:**
1. Check browser pop-up blocker (allow for agentnoon.com)
2. Reduce scope before exporting:
   - Filter to specific department or layer
   - Collapse sections not needed
   - Export smaller subset
3. Try different browser (Chrome recommended)
4. Close other tabs to free memory
5. Wait longer for export (large orgs may take 1-2 minutes)
6. If times out:
   - Filter to smaller scope
   - Export in sections (department by department)
   - Combine slides manually in PowerPoint

**See also:** [Exporting & Reporting](../directory/exporting-reporting.md)

---

### PowerPoint Export Looks Blurry or Low Quality

**Problem:** Exported PowerPoint slides have poor image quality

**Cause:** Zoom level, too much data on screen, or export resolution

**Solution:**
1. Adjust org chart before exporting:
   - Zoom to appropriate level (not too far out)
   - Show 2-3 layers maximum per slide
   - Use readable font size
2. Reduce information on cards:
   - Show only essential fields
   - Remove unnecessary card content
3. Filter to smaller sections:
   - Export departments separately for better quality
4. Alternative: Use Image export (PNG) at higher resolution:
   - Export as PNG
   - Insert PNG into PowerPoint manually
   - Better control over quality
5. For presentations:
   - Focus on structure, not individual names
   - Use summary views instead of full org chart

---

### PowerPoint Export Has Wrong Data

**Problem:** PowerPoint shows outdated or incorrect information

**Cause:** Cache issue, or viewing wrong scenario

**Solution:**
1. Verify you're viewing correct scenario or Main Org
2. Refresh page before exporting
3. Clear browser cache
4. Check when data was last refreshed (Settings → Data Management)
5. Apply correct filters before exporting
6. Verify card content settings show correct fields
7. Re-export after verifying data on screen

---

## Image Export Issues

### Image Export Cut Off or Incomplete

**Problem:** Exported PNG/JPEG doesn't show full org chart

**Cause:** Export captures visible area only, or chart too large

**Solution:**
1. Use "Fit to Screen" before exporting:
   - Zoom out to fit desired area
   - Then export
2. Alternatively:
   - Export in sections
   - Combine images in photo editor
3. For very large org charts:
   - Use PowerPoint export (exports entire org, not just screen)
   - Or export to CSV and create diagram in external tool
4. Adjust browser window size before export:
   - Maximize window
   - Full screen mode (F11)
   - Then export

---

## SFTP Integration Issues

### SFTP Connection Failing

**Problem:** Integration logs show "SFTP connection failed" or "Authentication error"

**Cause:** Credentials incorrect, firewall blocking, or SFTP server down

**Solution:**
1. Go to Settings → Data Management → SFTP Integration (Admin only)
2. Verify connection details:
   - Host/URL correct
   - Port correct (usually 22)
   - Username correct
   - Password correct (re-enter to be sure)
3. Click "Test Connection"
4. If test fails:
   - Verify SFTP server is running (contact IT)
   - Check firewall allows Agentnoon IP addresses
   - Test SFTP connection externally (FileZilla, WinSCP):
     - Use same credentials
     - If external tool works: Contact Agentnoon support
     - If external tool fails: Issue with SFTP server
5. Check SFTP server logs for blocked connection attempts
6. If using key-based auth: Verify public key is installed correctly

> **[Screenshot placeholder: SFTP connection test results showing "Connection failed: Authentication error" with red X icon and fields for Host, Port, Username displaying configured values]**

**See also:** [Live Data Integration](../live-data-integration/what-is-a-live-data-integration.md)

---

### SFTP File Not Found

**Problem:** Integration shows "File not found" or "No file at specified path"

**Cause:** File path incorrect, file not uploaded, or filename wrong

**Solution:**
1. Verify file exists on SFTP server:
   - Connect via FileZilla or WinSCP
   - Navigate to configured path
   - Check if file exists
2. Check file path configuration:
   - Settings → Data Management → SFTP Integration
   - Verify path is correct (case-sensitive)
   - Include full path from root directory
3. Verify filename matches exactly:
   - Check for typos
   - Verify file extension (.csv)
   - Case-sensitive on some servers
4. Check if HRIS export is running:
   - Verify HRIS scheduled export is working
   - Check last export timestamp
   - Contact HRIS admin if export failing
5. Use wildcard if filename changes:
   - Configure to use latest file (e.g., *.csv)
   - Or use date pattern (employees-*.csv)

---

### SFTP Integration Stopped Working Suddenly

**Problem:** SFTP integration was working but now fails

**Cause:** Password changed, server moved, or certificate expired

**Solution:**
1. Check recent changes:
   - Did password change?
   - Did SFTP server migrate?
   - Was certificate renewed?
2. Re-enter SFTP credentials (password may have been reset)
3. Test connection to verify
4. Check SFTP server status (may be temporarily down)
5. Review integration logs for specific error:
   - Authentication errors → Credential issue
   - Timeout errors → Network/firewall issue
   - File errors → File path or HRIS export issue
6. Contact IT to verify no changes to SFTP server
7. If using key-based auth: Check if key expired

---

## API Integration Issues

### API Connection Failing

**Problem:** REST API integration shows connection errors

**Cause:** API key invalid, endpoint changed, or rate limiting

**Solution:**
1. Verify API key is correct:
   - Settings → API Keys and Documentation
   - Regenerate API key if needed
   - Update integration configuration with new key
2. Check API endpoint URL:
   - Verify URL hasn't changed
   - Check for typos in configuration
3. Review API error messages:
   - 401 Unauthorized → API key issue
   - 403 Forbidden → Permissions issue
   - 429 Too Many Requests → Rate limiting
   - 500 Internal Server Error → Agentnoon issue
4. Check API rate limits:
   - Reduce sync frequency if hitting limits
   - Contact support to increase limits
5. Test API connection using curl or Postman:
   - Verify API responds externally
   - If works externally: Check integration config
   - If fails externally: Contact support

> **[Screenshot placeholder: API error response showing "401 Unauthorized: Invalid API key" with request details and "Generate New API Key" button]**

**See also:** [Integration Overview & Technical FAQ](../live-data-integration/integration-overview-and-technical-faq.md)

---

### Workday Integration Not Syncing

**Problem:** Workday integration shows errors or data not updating

**Cause:** Workday credentials expired, permissions changed, or API version

**Solution:**
1. Verify Workday credentials:
   - Username and password still valid
   - Re-enter credentials if needed
2. Check Workday permissions:
   - Integration user must have read access to employee data
   - Contact Workday admin to verify permissions
3. Test Workday connection:
   - Settings → Data Management → Workday Integration
   - Click "Test Connection"
4. Review integration logs for specific errors
5. Check Workday API version compatibility:
   - Workday may have updated API version
   - Contact support if version mismatch
6. Verify Workday report is configured correctly:
   - Report must include all required fields
   - Report must be accessible to integration user

---

## Scheduled Export Issues

### Scheduled Exports Not Running

**Problem:** Configured scheduled export but not receiving files

**Cause:** Schedule disabled, email issue, or export failure

**Solution:**
1. Verify schedule is enabled:
   - Settings → Scheduled Exports (Admin only)
   - Check status is "Active"
   - Verify schedule settings (time, frequency)
2. Check email settings:
   - Verify email address is correct
   - Check spam folder for export emails
   - Add noreply@agentnoon.com to safe senders
3. Review export logs:
   - Check if exports are running but failing
   - Review error messages
4. Manually trigger export to test:
   - Click "Run Now" on scheduled export
   - Verify export succeeds
5. If export succeeds manually but not on schedule:
   - Contact support (possible scheduling issue)
6. Check export permissions:
   - Verify creator still has access to data

---

### Scheduled Export Has Wrong Data

**Problem:** Receive scheduled export but data is incorrect or outdated

**Cause:** Filters applied, data not refreshed, or wrong scope

**Solution:**
1. Review scheduled export configuration:
   - Check what filters are applied
   - Verify date range settings
   - Check data scope (Main Org vs specific scenario)
2. Verify data is up to date:
   - Check last data refresh time
   - Ensure integration is syncing regularly
3. Update export configuration:
   - Edit scheduled export settings
   - Adjust filters or scope
   - Save changes
4. Test export manually before next scheduled run
5. Verify export includes correct columns and sorting

---

## Integration Sync Issues

### Integration Sync Timing Out

**Problem:** Data sync starts but times out before completing

**Cause:** Large dataset, slow connection, or server issue

**Solution:**
1. For large organizations (>10,000 employees):
   - Sync may take 30-60 minutes (normal)
   - Wait for sync to complete
2. Check sync logs for timeout errors
3. Reduce data size if possible:
   - Exclude terminated employees >12 months
   - Remove unnecessary fields from export
4. Schedule sync during off-peak hours:
   - Late evening or early morning
   - Less network congestion
5. Check HRIS export performance:
   - Verify HRIS export completes in reasonable time
   - Large exports may need optimization
6. Contact support if timeouts persist:
   - May need to optimize integration

---

### Integration Syncing Wrong Data

**Problem:** Data syncs successfully but values are incorrect

**Cause:** Field mapping incorrect, transformation issue, or source data problem

**Solution:**
1. Verify source data in HRIS is correct:
   - Check if error exists in source system
   - Compare values in HRIS vs Agentnoon
2. Review field mapping:
   - Settings → Data Management → Field Mapping
   - Verify each field maps to correct column
   - Update mappings if incorrect
3. Check data transformations:
   - Some integrations transform data (e.g., currency conversion)
   - Verify transformations are correct
4. Test with small data sample:
   - Export small dataset from HRIS
   - Upload manually to verify mapping
5. Review integration logs for warnings
6. Contact support if mapping appears correct but data still wrong

---

### Sync Running Too Often

**Problem:** Data syncing more frequently than expected, causing disruption

**Cause:** Sync schedule misconfigured

**Solution:**
1. Review sync frequency:
   - Settings → Data Management → Integration Settings
   - Check schedule (hourly, daily, weekly)
2. Adjust sync frequency:
   - Weekly is standard for most organizations
   - Daily for fast-moving orgs
   - Hourly rarely necessary
3. Consider impact on users:
   - Frequent syncs may disrupt work
   - Coordinate schedule with team
4. Save changes and monitor next few syncs

---

### Webhook Integration Failing

**Problem:** Webhook notifications not being received

**Cause:** Webhook URL incorrect, endpoint down, or authentication issue

**Solution:**
1. Verify webhook URL is correct
2. Test webhook endpoint:
   - Use curl or Postman to send test request
   - Verify endpoint responds
3. Check webhook authentication:
   - Verify token or credentials are correct
4. Review webhook logs in Agentnoon:
   - Settings → Webhooks (Admin only)
   - Check delivery status
5. Check your server logs for incoming webhook requests
6. Verify firewall allows incoming requests from Agentnoon
7. Re-send webhook test from Agentnoon
8. Contact support if webhooks still not delivered

---

## Export Permissions Issues

### "Export Permission Denied" Error

**Problem:** Export button grayed out or shows permission error

**Cause:** User role doesn't include export permissions

**Solution:**
1. Verify your user role:
   - Contact admin to check your access group
2. Admin should check:
   - Settings → Users → [Your Name]
   - Verify access group includes export permissions
3. Admin can update your permissions:
   - Assign to different access group with export rights
   - Or modify current access group to allow exports
4. Log out and back in after permission change
5. If still can't export:
   - Verify you have access to data being exported
   - Check field-level permissions for sensitive data

---

### Can Export Some Data But Not All

**Problem:** Can export certain departments but not others

**Cause:** Access scope restriction

**Solution:**
1. Check your access scope:
   - You can only export data within your scope
   - Contact admin to review scope settings
2. Admin should verify:
   - Settings → Users → [Your Name] → Scope
   - Expand scope if you need access to more data
3. Alternative: Request admin to export restricted data
4. Or request broader access scope from admin

---

## When to Contact Support

**Contact support if:**
- Exports consistently fail after trying solutions
- Integration connection fails with unclear error
- SFTP/API credentials verified but still can't connect
- Data syncing but completely wrong values appearing
- Webhook integration not working after all checks
- Export contains corrupted or unreadable data
- Scheduled exports not running despite correct config

**Include in support request:**
- Export or integration name
- Error message (exact text)
- Timestamp of failure
- Screenshots of error
- Integration logs (if applicable)
- What you've already tried
- Organization name

**For integration issues, also include:**
- Integration type (SFTP, API, Workday)
- Connection details (sanitized - no passwords)
- Sample data file (anonymized)

**Contact:** support@agentnoon.com

---

## Next Steps

- Return to [Troubleshooting Overview](overview.md)
- Review [Exporting & Reporting](../directory/exporting-reporting.md)
- See [Forecast Reports & Exports](../forecast/reports-exports.md)
- Learn about [Live Data Integration](../live-data-integration/what-is-a-live-data-integration.md)
- Check [Data Refresh & Sync](../admin/data-refresh-sync.md)
