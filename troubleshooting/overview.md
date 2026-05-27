---
description: A diagnostic framework and general troubleshooting guide
---

# 🛠️ Troubleshooting Overview

## Step 1: Identify the Category

* [Login & Access Issues](login-access-issues.md) — Unable to log in, SSO failures, MFA issues, or access denied
* [Data Issues](data-issues.md) — Upload errors, missing data, broken hierarchies, or sync failures
* [Scenario Issues](scenario-issues.md) — Save failures, stuck approvals, or drag-and-drop not working
* [Performance Issues](performance-issues.md) — Slow loading, timeouts, or browser freezing
* [Export & Integration Issues](export-integration-issues.md) — Export failures, SFTP errors, or API issues

## Step 2: Quick Fixes First

Before diving into specific guides, try the following:&#x20;

1. Clear your browser cache\
   (Ctrl/Cmd+Shift+Delete > Cached images and cookies)
2. Refresh the page
3. Use Google Chrome (recommended browser)
4. Log out and log back in
5. Try incognito/private browsing mode

**Supported browsers:** Chrome 90+, Edge 90+, Firefox 88+, Safari 14+. Internet Explorer is not supported.

## Step 3: Check the Data

Many issues that appear to be system bugs are actually caused by data inconsistencies:

* **Missing positions** — Check active filters (clear all filters to confirm)
* **Wrong numbers** — Verify effective dates, access scope, and data sync timing
* **Broken org chart** — Look for the orange broken hierarchy indicator in the toolbar
* **Stale scenario** — Scenarios do not auto-update with Main Org changes; check when the scenario was created

## Troubleshoot by Symptom

| Symptom                      | Try first                                             | Guide                                                       |
| ---------------------------- | ----------------------------------------------------- | ----------------------------------------------------------- |
| Blank screen / nothing loads | Clear cache, disable extensions, incognito mode       | [Performance Issues](performance-issues.md)                 |
| Changes not saving           | Check permissions, verify scenario not locked         | [Scenario Issues](scenario-issues.md)                       |
| Wrong or missing data        | Clear filters, check data sync, verify field mappings | [Data Issues](data-issues.md)                               |
| Can't access feature         | Verify access group permissions with admin            | [Login & Access Issues](login-access-issues.md)             |
| Export failing               | Apply filters to reduce size, allow pop-ups           | [Export & Integration Issues](export-integration-issues.md) |

## Network Requirements

* Allow HTTPS (port 443) and WebSockets to `*.agentnoon.com`
* Minimum bandwidth: 5/1 Mbps
* Recommended bandwith: 25/5 Mbps
* Contact support for Agentnoon IP ranges if your firewall requires allowlisting

## When to Contact Support

Contact [SupportSWP@dayforce.com](mailto:SupportSWP@dayforce.com) if:

* The issue persists after completing all troubleshooting steps
* There is a data loss or security concern
* Multiple users are affected
* An integration issue is blocking business operations

When submitting a request, include:&#x20;

* Screenshots (with full browser window and URL bar visible)
* Browser version and Operating System
* Exact error message text
* Steps to reproduce the issue
* What you've already tried
* Time the issue occurred.&#x20;

For urgent or blocking issues, include "URGENT" or "CRITICAL" in the subject line.&#x20;

**Response times:**&#x20;

* Critical = 2 hrs
* High Priority = 4 hrs
* Standard = 24 hrs
