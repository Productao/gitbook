---
description: Diagnostic framework and general troubleshooting guide
hidden: false
---

# Troubleshooting Overview

This guide helps you diagnose and resolve common issues in Agentnoon. Use this framework to troubleshoot problems efficiently before contacting support.

## How to Use This Guide

**Step 1: Identify the Category**

Choose the category that best matches your issue:
- **[Login & Access Issues](login-access-issues.md)** - Can't log in, access denied, authentication problems
- **[Data Issues](data-issues.md)** - Upload errors, missing data, incorrect information
- **[Scenario Issues](scenario-issues.md)** - Can't save, approval stuck, changes not showing
- **[Performance Issues](performance-issues.md)** - Slow loading, timeouts, browser freezing
- **[Export & Integration Issues](export-integration-issues.md)** - Export failures, integration errors

**Step 2: Try Quick Fixes First**

Many issues resolve with these basic steps:
1. Clear browser cache and cookies
2. Refresh the page
3. Try a different browser (Chrome recommended)
4. Log out and log back in
5. Check your internet connection

**Step 3: Follow the Specific Troubleshooting Guide**

Each category page uses the format:
- **Problem:** What you're experiencing
- **Cause:** Why it's happening
- **Solution:** Step-by-step fix

---

## General Troubleshooting Steps

### Before You Start

1. **Check your browser:** Agentnoon works best on Chrome, Edge, or Firefox (latest versions)
2. **Verify internet connection:** Ensure stable connectivity
3. **Note what you were doing:** Document the steps that led to the issue
4. **Check for error messages:** Screenshot any error messages you see

### Clear Cache and Refresh

Many issues are caused by outdated cached data.

**Chrome:**
1. Press Ctrl+Shift+Delete (Windows) or Cmd+Shift+Delete (Mac)
2. Select "Cached images and files" and "Cookies and other site data"
3. Choose "Last hour" from time range
4. Click "Clear data"
5. Refresh Agentnoon

**Edge:**
1. Press Ctrl+Shift+Delete (Windows) or Cmd+Shift+Delete (Mac)
2. Check "Cached images and files" and "Cookies and other site data"
3. Click "Clear now"
4. Refresh Agentnoon

**Firefox:**
1. Press Ctrl+Shift+Delete (Windows) or Cmd+Shift+Delete (Mac)
2. Select "Cookies" and "Cache"
3. Click "Clear"
4. Refresh Agentnoon

### Check Browser Compatibility

**Supported browsers:**
- Chrome (version 90+)
- Microsoft Edge (version 90+)
- Firefox (version 88+)
- Safari (version 14+)

**Not supported:**
- Internet Explorer (any version)
- Older browser versions

### Verify Your Access Permissions

**Problem:** Feature is missing or grayed out
**Cause:** Your access group doesn't include that permission
**Solution:** Contact your Agentnoon admin to verify your access group settings

> **[Screenshot placeholder: Feature button grayed out with tooltip "This feature requires additional permissions. Contact your administrator."]**

---

## When to Check Troubleshooting vs FAQ

**Use Troubleshooting when:**
- Something isn't working as expected
- You're getting error messages
- Features are behaving incorrectly
- You need to fix a problem

**Use [FAQ](../faq/general.md) when:**
- You want to understand how a feature works
- You're looking for best practices
- You have questions about terminology
- You need guidance on workflows

---

## How to Take Screenshots for Support

If you need to contact support, screenshots help diagnose issues quickly.

**What to capture:**
1. The full browser window (including URL bar)
2. Any error messages (full text)
3. The context before the error occurred

> **[Screenshot placeholder: Example of good screenshot showing full browser window with URL bar, error message dialog, and surrounding context with user action that triggered the error]**

**How to take screenshots:**

**Windows:**
- Press Windows Key + Shift + S
- Select area to capture
- Image copies to clipboard
- Paste into email or document

**Mac:**
- Press Cmd + Shift + 4
- Click and drag to select area
- Image saves to desktop
- Attach to email

**Full page:**
- Press F12 to open Developer Tools
- Press Ctrl+Shift+P (Windows) or Cmd+Shift+P (Mac)
- Type "screenshot" and select "Capture full size screenshot"

---

## Troubleshooting by Symptom

### Nothing Loads / Blank Screen

**Try this:**
1. Clear browser cache
2. Disable browser extensions
3. Try incognito/private mode
4. Check browser console for errors (F12)
5. Try different browser

**Still not working?** See [Performance Issues](performance-issues.md)

### Changes Not Saving

**Try this:**
1. Check internet connection
2. Verify you have edit permissions
3. Check if scenario is locked (submitted for approval)
4. Refresh page and try again

**Still not working?** See [Scenario Issues](scenario-issues.md)

### Data Looks Wrong

**Try this:**
1. Check when data was last refreshed (Settings → Data Management)
2. Verify filters aren't hiding data
3. Check field mappings (Admin only)
4. Compare to source system (HRIS)

**Still not working?** See [Data Issues](data-issues.md)

### Can't Access Feature

**Try this:**
1. Verify you're logged into correct organization
2. Check your access group permissions
3. Confirm you have the correct license type
4. Ask admin to verify your settings

**Still not working?** See [Login & Access Issues](login-access-issues.md)

### Exports Failing

**Try this:**
1. Reduce data size (apply filters)
2. Try different export format
3. Check browser download settings
4. Disable pop-up blockers

**Still not working?** See [Export & Integration Issues](export-integration-issues.md)

---

## When to Contact Support

**Contact support immediately if:**
- Data loss occurred
- Security or access control is compromised
- Integration stopped working and blocking business
- Multiple users affected by same issue
- Issue persists after trying all troubleshooting steps

**Before contacting support, gather:**
1. Screenshots of the issue
2. Browser version and operating system
3. Steps to reproduce the problem
4. Error messages (exact text)
5. Time when issue occurred
6. What you've already tried

**How to contact support:**
- Email: [support@agentnoon.com](mailto:support@agentnoon.com)
- Include "URGENT" in subject line for critical issues
- See also: [Support & How to Self-Help](../start-here/support-self-help.md)

---

## Escalation for Critical Issues

**Critical issues include:**
- Production data corruption
- Security breach or unauthorized access
- Complete system outage
- Data sync failures preventing business operations

**For critical issues:**
1. Email support@agentnoon.com with "CRITICAL" in subject line
2. Include your organization name and contact info
3. Describe business impact
4. Note if other users are affected
5. List any recent changes (data uploads, config changes)

**Response times:**
- Critical issues: Within 2 hours
- High priority: Within 4 hours
- Standard issues: Within 24 hours

---

## Network and Connectivity Requirements

**Firewall requirements:**
- Allow outbound HTTPS (port 443) to *.agentnoon.com
- Allow WebSocket connections
- Enable JavaScript and cookies

**IP whitelisting:**
- Contact support for current IP ranges if your organization requires whitelisting

**Bandwidth recommendations:**
- Minimum: 5 Mbps download, 1 Mbps upload
- Recommended: 25 Mbps download, 5 Mbps upload
- For large orgs (10,000+ employees): 50 Mbps+ download

**Connection issues:**
**Problem:** "Connection lost" or "Unable to connect" errors
**Cause:** Network instability or firewall blocking connection
**Solution:**
1. Check internet connection stability
2. Verify firewall allows *.agentnoon.com
3. Disable VPN temporarily to test
4. Contact IT to check network restrictions
5. Try different network (mobile hotspot) to isolate issue

---

## Browser Requirements and Settings

**Required browser settings:**
- JavaScript enabled
- Cookies enabled (first-party and third-party)
- Pop-ups allowed for Agentnoon domain
- Local storage enabled

**To check browser settings:**

**Chrome:**
1. Go to Settings → Privacy and security
2. Click "Site settings"
3. Verify JavaScript, Cookies, and Pop-ups are allowed

**Edge:**
1. Go to Settings → Cookies and site permissions
2. Verify JavaScript and Cookies are allowed

**Firefox:**
1. Go to Settings → Privacy & Security
2. Verify cookies and JavaScript are not blocked

**Recommended browser extensions to disable:**
- Ad blockers (uBlock Origin, AdBlock)
- Script blockers (NoScript)
- Privacy extensions that block cookies
- VPN extensions (can interfere with authentication)

---

## Next Steps

- Browse category-specific troubleshooting guides (see links above)
- Check [FAQ](../faq/general.md) for how-to questions
- See [Support & How to Self-Help](../start-here/support-self-help.md) for additional resources
