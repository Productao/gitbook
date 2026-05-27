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

**Wrong data in export**

* Verify you're viewing the correct scenario or Main Org, then refresh before exporting

## Image Export Issues

**Export is cut off / incomplete**

* Use "Fit to Screen" (zoom out) before exporting to capture the full visible area
* For large org charts, use PowerPoint export (captures entire org) instead of image export

## Export Permissions Issues

**"Export permission denied"**

* Contact admin to verify your access group includes export permissions
* Log out and back in after any permission change

**Can export some data but not all**

* Your access scope limits which departments/data you can export
* Contact admin to expand scope if needed

## When to Contact Support

Contact [SupportSWP@dayforce.com](mailto:SupportSWP@dayforce.com) if:

* Exports consistently fail after trying solutions
* Integration connection fails with unclear error after credentials verified
* Data syncing but values are completely wrong

Include: export/integration name, exact error message, timestamp, screenshots, integration logs, and what you have already tried. For integration issues, add the integration type and connection details (no passwords).
