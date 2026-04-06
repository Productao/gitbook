---
description: Resolve login and authentication issues
---

# 🔑 Login & Access Issues

Use this guide to troubleshoot login failures, SSO issues, access denied errors, and other authentication issues.

## Login Issues

**Incorrect password / forgot password**

* Check Caps Lock and verify you're using the correct email
* Click **Forgot Password** on the login page, enter your email, and follow the reset link (check your spam folder if you don’t receive it)
* Password requirements: at least 8 characters, including uppercase, lowercase, and a number

**Account locked**

* Too many failed attempts: wait 30 minutes for automatic unlock, or contact support to unlock immediately
* Account disabled by admin: contact your admin to reactivate in Settings > Users

**Wrong email / account not found**

* Verify your email address with your adm
* If your organization uses SSO, do not use email/password login—use the SSO button instead
* If no account exists, request an invitation from your admin

## SSO Issues

**SSO login fails or redirects back to login page**

* Clear browser cache and cookies; log out of your SSO provider (Okta, Google, Azure AD)
* Close all tabs, open a new window, and try again
* If still failing: verify SSO is set up correctly with IT; check provider status page; try a different browser

**Wrong SSO provider selected**

* Return to the login page and select the correct provider; contact your admin if you are unsure which to use

**SSO redirect loop**

* Clear all cache and cookies, then try incognito mode
* If it works in incognito, clear all browser data (not just cache)
* If the issue persists, contact support with a screenshot of the URL

**Switching SSO provider**

* Go to Profile (top right) > Update Authentication
* Choose new method
* Verify by logging out and back in

## Access Denied & Missing Data

**Access denied**

* Verify you are logged into the correct organization (Profile menu > Switch Organization)
* Contact your admin to confirm your access group and scope are configured correctly

**Missing data visability**

* Clear all filters first
* Your access scope may be restricted — contact admin to review Settings > Users > \[Your Name] > Scope

**Feature missing / grayed out**

* Your access group may not include that feature, or your license may not cover it
* Contact your admin to verify your role (Admin/Editor/Viewer) and access group permissions

## MFA Issues

**MFA code not working**

* Wait for a new code (codes expire every 30 seconds)
* Ensure phone clock is set to automatic time:
  * Android — Authenticator > Settings > Time correction > Sync now
  * iPhone — Settings > General > Date & Time > Set Automatically

**Lost MFA device**

* Use backup recovery codes (if saved during setup)
* If no backup codes are available, contact SupportSWP@dayforce.com with your email, org name, last login date, and reason for reset

**Disabling MFA**

* Admins control MFA requirements org-wide; individuals cannot disable it if admin requires it
* If optional: Profile > Security Settings > Disable MFA

## Browser & Cookie Issues

**"Cookies required" error**

* Enable cookies for agentnoon.com in your browser's privacy/cookie settings

**Infinite login redirect**

* Clear cache and all cookies for agentnoon.com; close all tabs; restart browser
* Try incognito mode; if that works, disable extensions one by one (ad blockers and privacy extensions are common culprits)

**Session timeout / logged out unexpectedly**

* Sessions expire after inactivity — log back in
* If VPN changes your IP, it may force re-authentication
* Contact IT to extend session timeout or configure split-tunneling

## Network & Firewall Issues

**Can't reach agentnoon.com**

* Test other websites; try a different network (e.g., a hotspot)
* If it works off your corporate network: ask IT to whitelist `*.agentnoon.com` on port 443 (HTTPS + WebSocket)
* Contact SupportSWP@dayforce.com for Agentnoon IP ranges if IT needs them for allowlisting

**VPN causing login issues**

* Try logging in without VPN; if that works, ask IT for split-tunneling or VPN bypass for agentnoon.com

## Account & Invitation Issues

**Invitation email not received**

* Check spam/junk; search for "Agentnoon"; add noreply@agentnoon.com to safe senders
* Ask admin to verify the email address and resend

**Invitation link expired**

* Links expire after 7 days; ask admin to resend a new invitation

**Already have an account but received a new invitation**

* Click the link and log in with existing credentials — you'll be added to the new organization

## When to Contact IT vs. Support

**Contact IT for:** network/firewall issues, VPN, SSO provider (Okta/Azure/Google), browser restrictions

**Contact SupportSWP@dayforce.com for:** account lockouts, MFA resets, invitation issues, permission problems, or anything not resolved by the solutions above
