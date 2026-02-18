---
description: Resolving login and authentication problems
icon: key
hidden: false
---

# Login & Access Issues

Common solutions for login failures, SSO problems, access denied errors, and authentication issues.

## Login Problems

### Can't Log In - Incorrect Password

**Problem:** "Incorrect email or password" error when trying to log in

**Cause:** Password is incorrect, mistyped, or caps lock is enabled

**Solution:**
1. Check that caps lock is OFF
2. Verify you're using the correct email address
3. Try copying and pasting password from password manager (to avoid typos)
4. If still fails, use "Forgot Password" to reset
5. Check email for password reset link (including spam folder)
6. Create new password and try logging in again

---

### Forgot Password

**Problem:** Can't remember password and need to reset

**Cause:** Password forgotten or not recorded

**Solution:**
1. Click "Forgot Password" on login page
2. Enter your email address
3. Click "Send Reset Link"
4. Check email (including spam/junk folder)
5. Click reset link in email
6. Create new password (must meet requirements: 8+ characters, uppercase, lowercase, number)
7. Log in with new password
8. Save password in password manager for future use

**If reset email doesn't arrive:**
- Check spam/junk folder
- Verify you entered correct email address
- Wait 5 minutes and try again
- Contact support@agentnoon.com if still not received after 10 minutes

---

### Wrong Email Address

**Problem:** Account not found or email not recognized

**Cause:** Using wrong email address or account doesn't exist

**Solution:**
1. Verify you're using the correct email (check with admin)
2. Try alternative email addresses (work email vs personal email)
3. Check if your organization uses SSO (you shouldn't use email/password login)
4. Contact your Agentnoon admin to verify your account exists
5. If no account exists, request admin to send you an invitation

---

### Account Locked or Disabled

**Problem:** "Account locked" or "Account disabled" message appears

**Cause:** Too many failed login attempts, or account deactivated by admin

**Solution for locked account (too many attempts):**
1. Wait 30 minutes for automatic unlock
2. Clear browser cache and cookies
3. Try logging in again
4. If still locked, contact support to unlock immediately

**Solution for disabled account:**
1. Account was deactivated by admin (user left company or access revoked)
2. Contact your Agentnoon admin to reactivate
3. Admin must go to Settings → Users → Reactivate user
4. Once reactivated, you can log in

---

## SSO Issues

### SSO Login Not Working

**Problem:** SSO login fails, redirects back to login page, or shows error

**Cause:** SSO configuration issue, expired session, or identity provider problem

**Solution:**
1. Clear browser cache and cookies
2. Try logging out of your SSO provider (Google, Okta, Azure AD, etc.)
3. Close all browser tabs
4. Open new browser window
5. Go to Agentnoon login page
6. Click SSO button again
7. Log into SSO provider when prompted

**If still failing:**
1. Verify your organization uses SSO (check with IT or admin)
2. Check if SSO provider is experiencing outages (check status page)
3. Try different browser
4. Contact your IT department to verify your SSO account is active
5. Contact Agentnoon support if SSO configuration needs review

---

### Wrong SSO Provider Selected

**Problem:** Login with Google but organization uses Microsoft SSO (or vice versa)

**Cause:** Selected wrong authentication method

**Solution:**
1. Return to login page
2. Select correct SSO provider (Google, Microsoft, Okta, etc.)
3. Or use "Continue with Email" if you have password-based login
4. If unsure which method to use, contact your admin

---

### SSO Redirect Loop

**Problem:** Login keeps redirecting back to SSO provider in endless loop

**Cause:** Cookie or session issue, or SSO misconfiguration

**Solution:**
1. Clear browser cache and cookies completely
2. Close all browser windows
3. Open browser in incognito/private mode
4. Try logging in via incognito
5. If works in incognito: Clear all browser data (not just cache)
6. If still loops: Try different browser
7. If persists: Contact support with screenshot of URL during loop

---

### Need to Switch SSO Provider

**Problem:** Want to change from email/password to SSO, or change SSO method

**Cause:** Organization switched authentication methods

**Solution:**
1. Log in using your current method (email/password or existing SSO)
2. Click your profile icon (top right)
3. Select "Update Authentication"
4. Choose new authentication method from list
5. Follow prompts to link new provider
6. Log out and log back in using new method to verify

**See also:** [Updating Login Method](../access-control/updating-login-method.md)

---

## Access Denied Errors

### "Access Denied" After Logging In

**Problem:** Can log in but see "Access denied" or "You don't have permission" message

**Cause:** Your user account lacks necessary permissions or access scope

**Solution:**
1. Verify you logged into the correct organization (if you have multiple)
2. Contact your Agentnoon admin to verify your access group
3. Admin should check:
   - User is assigned to an access group
   - Access group has appropriate permissions
   - User's scope includes data they need to access
4. Admin may need to update your access group or scope
5. Log out and log back in after admin makes changes

**See also:** [Access Groups](../access-control/access-groups.md)

---

### Can't See Certain Data or People

**Problem:** Logged in but can't see expected departments, people, or org units

**Cause:** Access scope is restricted to specific parts of organization

**Solution:**
1. Check if filters are applied (clear all filters)
2. Verify you're viewing Main Org (not a scenario with limited data)
3. Contact admin to check your scope settings
4. Admin should review Settings → Users → [Your Name] → Scope
5. Scope may be restricted to specific departments, locations, or managers
6. Admin can expand scope if you need access to more data

**See also:** [User Invitations](../access-control/user-invitations.md)

---

### Feature Grayed Out or Missing

**Problem:** Can't access a feature (Scenarios, Forecast, Hub, etc.)

**Cause:** Access group doesn't include that feature, or license limitation

**Solution:**
1. Verify your license type supports the feature
2. Contact admin to check your access group permissions
3. Admin should verify:
   - Access group includes feature access
   - User has correct role (Admin, Editor, Viewer)
   - Organization license includes that feature
4. Admin may need to assign you to different access group
5. Log out and back in after changes

---

### Wrong Organization Displayed

**Problem:** Logged in but seeing wrong company's data

**Cause:** User has access to multiple organizations and selected wrong one

**Solution:**
1. Click profile icon (top right)
2. Click "Switch Organization" (if available)
3. Select correct organization from list
4. If organization isn't listed, your account may not have access
5. Contact admin of correct organization to verify access
6. They may need to send new invitation to your email

---

## MFA / 2FA Issues

### MFA Code Not Working

**Problem:** Multi-factor authentication code rejected or invalid

**Cause:** Code expired, time sync issue, or wrong code entered

**Solution:**
1. Wait for new code to generate (codes expire after 30 seconds)
2. Ensure clock on your phone is set to automatic time (not manual)
3. Try entering code immediately after it generates
4. Verify you're using correct authentication app (Google Authenticator, Duo, etc.)
5. Check if you have multiple accounts in app - use correct one
6. If using SMS: Request new code and try again

**Time sync issues (common problem):**
1. On Android: Open Authenticator app → Settings → Time correction → Sync now
2. On iPhone: Settings → General → Date & Time → Enable "Set Automatically"
3. Generate new code and try logging in

---

### Lost MFA Device

**Problem:** Can't access MFA codes because phone is lost, broken, or replaced

**Cause:** MFA device unavailable and no backup codes

**Solution:**
1. Use backup recovery codes (if you saved them during MFA setup)
2. If no backup codes, contact support@agentnoon.com
3. Provide:
   - Your email address
   - Organization name
   - Last successful login date
   - Reason for MFA reset request
4. Support will verify identity and reset MFA
5. Log in and set up MFA on new device

**Prevention:**
- Save backup codes when setting up MFA
- Register multiple devices if possible
- Store backup codes in password manager

---

### Need to Disable MFA

**Problem:** Want to turn off MFA requirement

**Cause:** Personal preference or organizational policy change

**Solution:**
1. Admins control MFA requirements at organization level
2. Individual users cannot disable MFA if admin requires it
3. Contact your admin to request MFA be made optional
4. Admin can disable MFA requirement in Settings → Security
5. If MFA is optional and you want to disable for your account:
   - Go to Profile → Security Settings
   - Click "Disable MFA"
   - Confirm with password

---

## Browser and Cookie Issues

### "Cookies Required" Error

**Problem:** Can't log in, see "Please enable cookies" message

**Cause:** Browser cookies are disabled or blocked

**Solution:**

**Chrome:**
1. Go to Settings → Privacy and security → Cookies and other site data
2. Select "Allow all cookies" or "Block third-party cookies"
3. Add agentnoon.com to allowed sites
4. Refresh login page and try again

**Edge:**
1. Settings → Cookies and site permissions → Manage and delete cookies
2. Enable "Allow sites to save and read cookie data"
3. Refresh and try logging in

**Firefox:**
1. Settings → Privacy & Security
2. Under "Cookies and Site Data," ensure cookies are not blocked
3. Add exception for agentnoon.com if needed

**Safari:**
1. Safari → Preferences → Privacy
2. Uncheck "Block all cookies"
3. Refresh login page

---

### Infinite Login Redirect / Loop

**Problem:** Login page keeps reloading or redirecting endlessly

**Cause:** Cookie or cache conflict, or browser extension interference

**Solution:**
1. Clear browser cache completely (see [Troubleshooting Overview](overview.md))
2. Clear all cookies for agentnoon.com
3. Close all browser tabs and windows
4. Restart browser
5. Try logging in again
6. If persists: Try incognito/private mode
7. If works in incognito: Disable browser extensions one by one to find conflict
8. Common culprits: Ad blockers, privacy extensions, VPN extensions

---

### Session Timeout / Logged Out Unexpectedly

**Problem:** Get logged out frequently or "Session expired" message appears

**Cause:** Session timeout, inactive for too long, or IP address changed

**Solution:**
1. Log in again (sessions expire after period of inactivity)
2. For longer sessions: Keep Agentnoon tab active (click around every 30 min)
3. If logging out constantly: Check if VPN is changing your IP address
4. Disable VPN and try again
5. If company policy requires VPN, contact admin to extend session timeout
6. Admin can adjust session timeout in Settings → Security

---

## Network and Firewall Issues

### Can't Access Agentnoon Domain

**Problem:** Agentnoon website won't load, "Cannot connect" or "Site unreachable"

**Cause:** Firewall blocking access, network issue, or DNS problem

**Solution:**
1. Check internet connection (try loading other websites)
2. Try different network (mobile hotspot, home WiFi, etc.)
3. If works on different network: Company firewall is blocking Agentnoon
4. Contact IT department to whitelist *.agentnoon.com
5. Provide IT with requirements:
   - Allow HTTPS (port 443) to *.agentnoon.com
   - Allow WebSocket connections
   - Enable JavaScript and cookies
6. If IT needs IP ranges for whitelisting, contact support@agentnoon.com

---

### VPN Causing Login Issues

**Problem:** Can't log in when connected to corporate VPN

**Cause:** VPN routing or IP restrictions

**Solution:**
1. Disconnect VPN temporarily and try logging in
2. If successful without VPN: VPN configuration is blocking access
3. Contact IT to configure VPN split-tunneling for Agentnoon
4. Or request Agentnoon be added to VPN bypass list
5. If company requires VPN for all access, IT must whitelist Agentnoon

---

## Account and Invitation Issues

### Invitation Email Not Received

**Problem:** Admin sent invitation but you didn't receive email

**Cause:** Email in spam folder, incorrect email address, or email filtering

**Solution:**
1. Check spam/junk folder
2. Search email for "Agentnoon" and "invitation"
3. Add noreply@agentnoon.com to safe sender list
4. Ask admin to verify email address they used
5. Ask admin to resend invitation
6. Wait 5-10 minutes for email to arrive
7. If still not received, contact support@agentnoon.com

---

### Invitation Link Expired

**Problem:** Clicked invitation link but says "Link expired" or "Invalid invitation"

**Cause:** Invitation links expire after 7 days

**Solution:**
1. Contact your admin to resend invitation
2. New invitation link will be sent to your email
3. Click new link within 7 days
4. Complete account setup process

---

### Already Have Account but Received New Invitation

**Problem:** Received invitation but already have Agentnoon account

**Cause:** Admin is adding you to new organization, or updating your access

**Solution:**
1. Click invitation link
2. Log in with existing credentials
3. You'll be added to new organization or access will be updated
4. You can now switch between organizations from profile menu

---

## When to Contact IT vs Support

**Contact your IT department for:**
- Network or firewall issues
- VPN problems
- SSO provider issues (Okta, Azure AD, Google Workspace)
- Corporate security policies
- Browser restrictions or policies

**Contact Agentnoon support for:**
- Account lockouts
- MFA resets
- Invitation issues
- Permission problems
- SSO configuration in Agentnoon
- Any issue persisting after trying solutions above

**Contact email:** support@agentnoon.com

---

## Next Steps

- Return to [Troubleshooting Overview](overview.md)
- See [Access Control](../access-control/access-groups.md) for permission details
- See [User Invitations](../access-control/user-invitations.md) for account setup
- Contact [Support](../start-here/support-self-help.md) if issues persist
