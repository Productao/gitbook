---
description: Diagnostic framework and general troubleshooting guide
hidden: false
---

# Troubleshooting Overview

## Step 1: Identify the Category

- **[Login & Access Issues](login-access-issues.md)** — Can't log in, SSO failure, MFA problems, access denied
- **[Data Issues](data-issues.md)** — Upload errors, missing data, broken hierarchies, sync failures
- **[Scenario Issues](scenario-issues.md)** — Save failures, approval stuck, drag-and-drop not working
- **[Performance Issues](performance-issues.md)** — Slow loading, timeouts, browser freezing
- **[Export & Integration Issues](export-integration-issues.md)** — Export failures, SFTP errors, API issues

## Step 2: Quick Fixes First

Try these before diving into specific guides:
1. Clear browser cache (Ctrl/Cmd+Shift+Delete > Cached images and cookies)
2. Refresh the page
3. Try Chrome (recommended browser)
4. Log out and back in
5. Try incognito mode

**Supported browsers:** Chrome 90+, Edge 90+, Firefox 88+, Safari 14+. Internet Explorer is not supported.

## Step 3: Check the Data

Many issues that look like system bugs are actually data issues:

- **Missing positions:** Check active filters (clear all filters to confirm)
- **Wrong numbers:** Check effective dates, access scope, and data sync time
- **Broken org chart:** Look for the orange broken hierarchy indicator in the toolbar
- **Stale scenario:** Scenarios don't auto-update with Main Org changes — check when the scenario was created

## Troubleshoot by Symptom

| Symptom | Try first | Guide |
|---------|-----------|-------|
| Blank screen / nothing loads | Clear cache, disable extensions, incognito mode | [Performance Issues](performance-issues.md) |
| Changes not saving | Check permissions, verify scenario not locked | [Scenario Issues](scenario-issues.md) |
| Wrong or missing data | Clear filters, check data sync, verify field mappings | [Data Issues](data-issues.md) |
| Can't access feature | Verify access group permissions with admin | [Login & Access Issues](login-access-issues.md) |
| Export failing | Apply filters to reduce size, allow pop-ups | [Export & Integration Issues](export-integration-issues.md) |

## Network Requirements

- Allow HTTPS (port 443) and WebSockets to `*.agentnoon.com`
- Minimum bandwidth: 5/1 Mbps; recommended: 25/5 Mbps
- Contact support for Agentnoon IP ranges if your firewall requires allowlisting

## When to Contact Support

Contact SupportSWP@dayforce.com if:
- Issue persists after trying all troubleshooting steps
- Data loss or security concern
- Multiple users affected
- Integration blocking business operations

**Include:** screenshots with full browser window and URL bar, browser version and OS, exact error text, steps to reproduce, what you've already tried, and time the issue occurred. Add "URGENT" or "CRITICAL" to the subject line for blocking issues.

**Response times:** Critical = 2 hrs, High Priority = 4 hrs, Standard = 24 hrs.
