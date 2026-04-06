---
description: Fix export and integration problems
---

# 📤 Export & Integration Issues

Common solutions for CSV export failures, PowerPoint export issues, SFTP connection errors, and integration sync issues.

## CSV Export Issues

**Export fails or downloads empty file**

* Clear all filters before exporting; verify data is visible on screen
* Check browser pop-up blocker — allow downloads from agentnoon.com
* Try incognito mode or a different browser
* If empty after filtering: verify your access scope includes the data

**Missing columns**

* Enable columns before exporting: click the column selector, check the boxes you need
* Fields hidden by your access group (e.g., salary) cannot be exported — contact your admin

**Missing rows**

* Clear all active filters; your access scope limits which rows you can export
* Very large exports may be capped — export in batches using filters

**CSV won't open in Excel / data appears corrupted**

* Import via Excel > Data > From Text/CSV, selecting UTF-8 encoding (do not double-click the file)
* Numbers as text: select column > Data > Text to Columns > Finish
* Dates export as YYYY-MM-DD; reformat in Excel if needed
* Salary values should be plain numbers (no $ or commas) — clear formatting if needed

## PowerPoint Export Issues

**Export fails or times out**

* Allow downloads from agentnoon.com in your browser pop-up settings
* Filter to a smaller scope (department or top 3 layers) before exporting
* Wait up to 2 minutes for large orgs; if it times out, export in sections

**Blurry or low quality**

* Show only 2–3 layers at a readable zoom level before exporting
* For better control: export as PNG, then insert into PowerPoint manually

**Wrong data in export**

* Verify you're viewing the correct scenario or Main Org, then refresh before exporting

## Image Export Issues

**Export is cut off / incomplete**

* Use "Fit to Screen" (zoom out) before exporting to capture the full visible area
* For large org charts, use PowerPoint export (captures entire org) instead of image export

## SFTP Integration Issues

**SFTP connection failing**

1. Go to Settings > Data Management > SFTP Integration
2. Verify host, port (usually 22), username, and password; click **Test Connection**
3. If test fails: test with FileZilla/WinSCP using the same credentials
   * External tool works → contact Agentnoon support
   * External tool also fails → issue is with the SFTP server or credentials
4. Check firewall allows Agentnoon IP addresses; verify key-based auth if applicable

**SFTP file not found**

* Connect via FileZilla and confirm the file exists at the configured path (case-sensitive)
* Verify filename matches exactly, including extension; check HRIS scheduled export is running
* Use a wildcard pattern (e.g., `employees-*.csv`) if the filename changes

**SFTP integration stopped working suddenly**

* Check if password, server, or certificate recently changed; re-enter credentials and test
* Review integration logs: Authentication errors → credentials; Timeout → firewall/network; File errors → HRIS export

## API Integration Issues

**API connection failing**

* Verify API key in Settings > API Keys and Documentation; regenerate if needed
* Check HTTP error codes: 401 = key issue, 403 = permissions, 429 = rate limit, 500 = Agentnoon issue
* Test with curl or Postman; if works externally, check your integration config

**Workday integration not syncing**

1. Re-verify Workday credentials and test connection in Settings > Data Management > Workday Integration
2. Confirm integration user has read access to employee data in Workday
3. Review integration logs; contact support for API version compatibility issues

## Scheduled Export Issues

**Scheduled exports not running**

* Verify schedule is Active in Settings > Scheduled Exports; check correct time and frequency
* Check spam folder for export emails; add noreply@agentnoon.com to safe senders
* Use "Run Now" to test manually; if that works but schedule doesn't, contact support

**Scheduled export has wrong data**

* Review filters and date range in the scheduled export configuration
* Verify data is up to date (check last sync time)

## Integration Sync Issues

**Sync timing out**

* Orgs >10,000 employees may take 30–60 minutes — this is normal
* Exclude terminated employees >12 months; schedule sync during off-peak hours

**Syncing wrong data**

* Verify the source data is correct in your HRIS
* Review field mapping in Settings > Data Management > Field Mapping and update if needed

**Webhook failing**

* Verify the webhook URL; test with curl/Postman to confirm endpoint responds
* Check Agentnoon webhook logs (Settings > Webhooks) for delivery status
* Ensure your firewall allows incoming requests from Agentnoon

## Export Permissions Issues

**"Export permission denied"**

* Contact admin to verify your access group includes export permissions
* Log out and back in after any permission change

**Can export some data but not all**

* Your access scope limits which departments/data you can export
* Contact admin to expand scope if needed

## When to Contact Support

Contact sSupportSWP@dayforce.com if:

* Exports consistently fail after trying solutions
* Integration connection fails with unclear error after credentials verified
* Data syncing but values are completely wrong
* Scheduled exports not running despite correct configuration

Include: export/integration name, exact error message, timestamp, screenshots, integration logs, and what you have already tried. For integration issues, add the integration type and connection details (no passwords).
