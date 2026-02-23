---
description: Resolving login and authentication problems
---

# 🔑 Login & Access Issues

Common solutions for login failures, SSO problems, access denied errors, and authentication issues.

## Login Problems

**Incorrect password / forgot password**

* Check caps lock; verify you're using the correct email
* Click **Forgot Password** on the login page, enter your email, and follow the reset link (check spam if not received)
* Password requirements: 8+ characters, uppercase, lowercase, number

**Account locked**

* Too many failed attempts: wait 30 minutes for automatic unlock, or contact support to unlock immediately
* Account disabled by admin: contact your admin to reactivate in Settings > Users

**Wrong email / account not found**

* Verify the correct email with your admin
* If your org uses SSO, don't use email/password login — use the SSO button
* Request an invitation from your admin if no account exists

## SSO Issues

**SSO login fails or redirects back to login page**

1. Clear browser cache and cookies; log out of your SSO provider (Okta, Google, Azure AD)
2. Close all tabs, open a new window, and try again
3. If still failing: verify SSO is set up correctly with IT; check provider status page; try a different browser

**Wrong SSO provider selected**

* Return to the login page and select the correct provider; contact your admin if unsure which to use

**SSO redirect loop**

* Clear all cache and cookies; try incognito mode
* If it works in incognito: clear all browser data (not just cache); if it loops there too, contact support with a screenshot of the URL

**Switching SSO provider**

* Profile icon (top right) > **Update Authentication** > choose new method > verify by logging out and back in

## Access Denied / Missing Data

**"Access denied" after logging in**

* Verify you logged into the correct organization (profile menu > Switch Organization)
* Contact admin to confirm your access group and scope are configured correctly

**Can't see certain departments, people, or org units**

* Clear all filters first
* Your access scope may be restricted — contact admin to review Settings > Users > \[Your Name] > Scope

**Feature grayed out or missing**

* Your access group may not include that feature, or your license may not cover it
* Contact admin to verify role (Admin/Editor/Viewer) and access group permissions

## MFA Issues

**MFA code not working**

* Wait for a new code (codes expire every 30 seconds)
* Ensure phone clock is set to automatic time: Android — Authenticator > Settings > Time correction > Sync now; iPhone — Settings > General > Date & Time > Set Automatically

**Lost MFA device**

* Use backup recovery codes (if saved during setup)
* If no backup codes: contact SupportSWP@dayforce.com with your email, org name, last login date, and reason for reset

**Disabling MFA**

* Admins control MFA requirements org-wide; individuals cannot disable it if admin requires it
* If optional: Profile > Security Settings > Disable MFA

## Browser and Cookie Issues

**"Cookies required" error**

* Enable cookies for agentnoon.com in your browser's privacy/cookie settings

**Infinite login redirect**

* Clear cache and all cookies for agentnoon.com; close all tabs; restart browser
* Try incognito mode; if that works, disable extensions one by one (ad blockers and privacy extensions are common culprits)

**Session timeout / logged out unexpectedly**

* Sessions expire after inactivity — log back in
* If VPN changes your IP, it may force re-authentication; contact IT to extend session timeout or configure split-tunneling

## Network and Firewall Issues

**Can't reach agentnoon.com**

* Test other websites; try a different network (hotspot)
* If it works off your corporate network: ask IT to whitelist `*.agentnoon.com` on port 443 (HTTPS + WebSocket)
* Contact SupportSWP@dayforce.com for Agentnoon IP ranges if IT needs them for allowlisting

**VPN causing login issues**

* Try logging in without VPN; if that works, ask IT for split-tunneling or VPN bypass for agentnoon.com

## Account and Invitation Issues

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
