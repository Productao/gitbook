---
description: Resolving scenario planning problems
hidden: false
---

# Scenario Issues

Common solutions for scenario save failures, approval problems, change tracking issues, and drag-and-drop not working.

## Scenario Save and Load Issues

### Scenario Won't Save

**Problem:** Made changes but "Save" button grayed out or nothing happens when clicking Save

**Cause:** Scenario is locked, no changes made yet, or permission issue

**Solution:**
1. Check if scenario is locked (submitted for approval)
   - Look for lock icon or "Locked" badge
   - If locked: Cannot edit until returned or approved
2. Verify you made actual changes (Save only enables after edits)
3. Check internet connection (changes won't save offline)
4. Try these steps:
   - Refresh the page (changes may auto-save)
   - Clear browser cache
   - Try different browser
5. Check your permissions:
   - Verify you have edit access (not just view)
   - Contact admin if you need editor permissions
6. If scenario is shared: Check if someone else is editing (may conflict)

> **[Screenshot placeholder: Locked scenario banner showing lock icon with message "This scenario is locked pending approval. Changes cannot be saved until the scenario is returned or withdrawn."]**

---

### Changes Not Saving / Keep Reverting

**Problem:** Make changes but they disappear or revert when refreshing

**Cause:** Browser cache issue, auto-save failing, or connection problem

**Solution:**
1. Check internet connection stability
2. Watch for auto-save indicator (usually in top corner)
3. If auto-save fails:
   - Click manual Save button
   - Wait for confirmation "Changes saved"
4. Clear browser cache and reload scenario
5. Try these steps:
   - Make one change at a time
   - Wait for save confirmation before next change
6. If changes still revert:
   - Export scenario data before making changes (backup)
   - Try different browser
   - Contact support if persists

---

### Scenario Won't Load / Blank Screen

**Problem:** Click to open scenario but nothing loads, or blank screen appears

**Cause:** Browser cache issue, large scenario, or corrupted scenario

**Solution:**
1. Wait 30 seconds (large scenarios take time to load)
2. Clear browser cache completely
3. Refresh the page (Ctrl+R or Cmd+R)
4. Try opening in incognito/private mode
5. Try different browser
6. Check browser console for errors (F12 → Console tab)
7. If specific scenario won't load but others do:
   - Scenario may be corrupted
   - Contact support with scenario name and timestamp

> **[Screenshot placeholder: Blank screen with loading spinner and text "Loading scenario 'Q2 2026 Hiring Plan'... This may take up to 60 seconds for large organizations"]**

---

### Can't Create New Scenario

**Problem:** "Create Scenario" button missing or grayed out

**Cause:** Permission issue, license limit, or Main Org not loaded

**Solution:**
1. Verify you have edit or admin permissions
2. Check if Main Org is loaded (scenario needs baseline data)
3. Check license limits:
   - Some plans limit number of scenarios
   - Contact admin to verify license status
4. If Main Org has no data: Upload data first
5. Try creating from Main Org view:
   - Go to Main Org
   - Click "Create Scenario" in taskbar
6. If button still missing: Contact admin to verify permissions

---

## Position Editing Issues

### Can't Add New Position

**Problem:** "Add Position" option missing or doesn't work

**Cause:** Permission issue, scenario locked, or connection problem

**Solution:**
1. Verify scenario is not locked (check for lock icon)
2. Check you have edit permissions
3. Try these methods to add position:
   - Right-click on manager card → "Add Direct Report"
   - Use taskbar → Position Interactions → Add Position
   - Click "+" icon on manager card (if available)
4. Verify Main Org has data (can't add to empty scenario)
5. If option grayed out:
   - Check if you selected a position first
   - Try refreshing page
6. Clear browser cache and try again

---

### Can't Edit Position Details

**Problem:** Click on position but can't edit fields (name, title, salary)

**Cause:** Scenario locked, field-level permissions, or view-only access

**Solution:**
1. Check if scenario is locked (submitted for approval)
2. Verify you have edit permissions (not just view)
3. Check field-level permissions:
   - Admin may have restricted editing certain fields (e.g., salary)
   - Contact admin to verify your access group
4. Try clicking edit icon or pencil icon on position card
5. If position is from Main Org (not scenario change):
   - Some fields may be read-only from source data
   - Use Change Tracker to modify in scenario
6. Refresh page and try again

---

### Drag-and-Drop Not Working

**Problem:** Can't drag positions to new managers

**Cause:** Browser issue, scenario locked, or permission restriction

**Solution:**
1. Verify scenario is not locked
2. Check you have edit permissions
3. Browser troubleshooting:
   - Refresh page
   - Clear browser cache
   - Try different browser (Chrome recommended)
   - Disable browser extensions (especially ad blockers)
4. Drag-and-drop technique:
   - Click and hold on position card
   - Drag slowly to new manager
   - Release when you see drop zone highlight
5. Alternative method:
   - Right-click position → "Change Manager"
   - Select new manager from dropdown
   - Click Save
6. For bulk moves: Use Bulk Operations instead of drag-and-drop

---

### Can't Delete or Close Position

**Problem:** Delete option missing or doesn't work

**Cause:** Permission issue, position has dependencies, or scenario locked

**Solution:**
1. Check if scenario is locked
2. Verify you have edit permissions
3. Try these methods:
   - Right-click position → "Close Position" or "Mark as Reduction"
   - Select position → Use Reduction interaction
4. If position has direct reports:
   - Reassign or close direct reports first
   - Or use "Close position and reassign reports" option
5. Check if position is from Main Org:
   - Main Org positions can be "closed" in scenario but not deleted
   - Use reduction interaction instead
6. Refresh page and try again

---

## Change Tracker Issues

### Change Tracker Not Updating

**Problem:** Made changes but Change Tracker (OPEX panel) doesn't show them

**Cause:** Changes not saved yet, cache issue, or sync delay

**Solution:**
1. Click Save button to save changes
2. Wait a few seconds for Change Tracker to update
3. Refresh the page
4. Clear browser cache
5. Open Change Tracker panel (👀 icon in top right)
6. If still not showing:
   - Verify changes actually saved (check position cards)
   - Try closing and reopening scenario
   - Contact support if tracker still not updating

> **[Screenshot placeholder: Change Tracker panel showing "No changes detected" message with refresh icon, while org chart in background shows positions with green addition indicators]**

**See also:** [Change Tracker](../scenarios/change-tracker.md)

---

### Change Tracker Shows Wrong Numbers

**Problem:** Change Tracker cost or headcount numbers don't match expectations

**Cause:** Formula setting incorrect, effective dates, or calculation issue

**Solution:**
1. Check formula selection:
   - Click formula dropdown in Change Tracker
   - Switch between Salary, Total Comp, Custom Formula
   - Verify you're using correct formula
2. Check effective dates:
   - Changes with future effective dates may not count yet
   - Adjust date range in Change Tracker
3. Verify scenario comparison mode:
   - "Show Changes" displays deltas
   - "Show After" displays total
   - "Show Before" displays baseline
4. Recalculate metrics:
   - Save scenario
   - Close and reopen
   - Metrics should recalculate
5. If numbers still wrong: Contact support with screenshots

---

### Can't See Individual Change Details

**Problem:** Change Tracker shows totals but can't see specific changes

**Cause:** Panel collapsed, wrong view mode, or no changes made yet

**Solution:**
1. Expand Change Tracker panel (click 👀 icon)
2. Click on category to expand:
   - Additions (green)
   - Reductions (red)
   - Data Changes (blue)
3. Scroll through list to see individual positions
4. Click on specific position to see detailed changes
5. If list is empty:
   - Verify you made changes in scenario
   - Check if filter is hiding changes
   - Refresh page

---

## Scenario Comparison Issues

### Scenario Comparison Not Showing Differences

**Problem:** Comparing scenarios but no differences appear

**Cause:** Scenarios are identical, wrong comparison mode, or sync issue

**Solution:**
1. Verify you're comparing different scenarios (not same scenario)
2. Check comparison mode:
   - Select "Show Changes" or "Comparison" view
   - Not "Show After" (which shows final state only)
3. Ensure scenarios have actual differences
4. Refresh page
5. Try alternative comparison method:
   - Open Scenario A
   - Go to Comparisons tab
   - Select Scenario B to compare
   - View side-by-side or overlay mode
6. Clear cache and try again

---

### Can't Compare Scenarios

**Problem:** Comparison option missing or doesn't work

**Cause:** Need at least 2 scenarios, permission issue, or feature not available

**Solution:**
1. Verify you have at least 2 scenarios created
2. Check your license includes scenario comparison feature
3. Try these steps:
   - Open a scenario
   - Look for "Compare" or "Comparisons" button/tab
   - Select second scenario to compare
4. If option missing:
   - Contact admin to verify your access level
   - Check if license includes comparison feature
5. Alternative: Export both scenarios to CSV and compare in Excel

---

## Sharing and Collaboration Issues

### Can't Share Scenario with Team

**Problem:** Share option missing or team members can't access scenario

**Cause:** Permission issue, access scope restriction, or team member not invited

**Solution:**
1. Verify you have permission to share scenarios
2. Try sharing via:
   - Scenario menu → Share
   - Or copy scenario URL and send via email
3. For team members who can't access:
   - Verify they have Agentnoon account
   - Check their access scope includes data in scenario
   - Contact admin to adjust their permissions
4. Check if scenario is private (only you can see)
5. Make scenario shared or public (if option available)
6. If no share option: Contact admin for permissions

**See also:** [User Collaboration](../scenarios/user-collaboration.md)

---

### Multiple People Editing Same Scenario

**Problem:** Changes conflicting when multiple users edit simultaneously

**Cause:** Concurrent editing not fully supported

**Solution:**
1. Coordinate editing times with team
2. Use scenario locking when one person edits
3. Best practices:
   - Assign ownership of scenarios
   - Only one person edits at a time
   - Use comments to communicate changes
4. If conflict occurs:
   - Refresh page to see latest changes
   - Re-apply your changes carefully
   - Or create separate scenarios and merge later
5. For major edits: Lock scenario or notify team you're editing

---

## Approval Workflow Issues

### Can't Submit Scenario for Approval

**Problem:** Submit button missing or grayed out

**Cause:** No changes made, missing approvers, or permission issue

**Solution:**
1. Verify scenario has changes:
   - Open Change Tracker
   - Confirm additions, reductions, or modifications exist
2. Check if approval workflow is configured (Admin setting)
3. Try opening OpEx Panel or Change Tracker → Look for "Submit for Approval"
4. If button grayed out:
   - Ensure all changes are saved
   - Check if scenario already submitted
   - Verify you have permission to submit
5. Contact admin if approval workflow needs setup

**See also:** [Configuring Approval Flows](../admin/configuring-approval-flows.md)

---

### Scenario Stuck in Approval

**Problem:** Submitted scenario but approval not progressing

**Cause:** Approver not notified, approver unavailable, or approval process issue

**Solution:**
1. Check approval status in scenario
2. Identify current approver (which level: 0, 1, 2, or 3)
3. Follow up with approver:
   - Send reminder email
   - Verify they received notification
   - Check if they're on vacation or out of office
4. If approver unavailable:
   - Contact admin to reassign approver
   - Or request expedited approval process
5. If approver says they can't find scenario:
   - Verify their access scope includes scenario data
   - Check they're assigned as approver correctly
   - Resend link to scenario

> **[Screenshot placeholder: Approval workflow status showing "Waiting for Level 1 approval from Jane Smith (Finance)" with yellow pending clock icon and "Sent 3 days ago" timestamp]**

---

### Approval Rejected - Need to Revise

**Problem:** Scenario rejected, need to make changes and resubmit

**Cause:** Approver found issues and returned scenario

**Solution:**
1. Open scenario (should be unlocked after rejection)
2. Review rejection comments from approver
3. Make requested changes:
   - Modify specific positions
   - Adjust headcount or cost
   - Correct errors noted by approver
4. Save changes
5. Resubmit for approval:
   - Open OpEx Panel
   - Click "Submit for Approval"
   - Add note about changes made
6. Scenario goes back through approval levels
7. Previously approved items may stay approved (depends on configuration)

---

### Scenario Locked - Can't Edit

**Problem:** Scenario is locked and can't make any changes

**Cause:** Scenario submitted for approval and lock setting is enabled

**Cause:** Scenario submitted for approval, lock setting enabled, or admin locked it

**Solution:**
1. Check scenario status (should show "Pending Approval" or "Locked")
2. If submitted for approval:
   - Wait for approval/rejection
   - Or withdraw submission (if option available)
   - Contact approver to expedite or reject so you can edit
3. If admin locked scenario:
   - Contact admin to unlock
   - Or create copy of scenario to edit
4. To create editable copy:
   - Go to Scenario Management
   - Select scenario
   - Click "Duplicate"
   - Edit the copy instead

---

## Effective Date Issues

### Effective Dates Not Applying Correctly

**Problem:** Set effective dates but changes not showing at correct time

**Cause:** Date format issue, forecast not respecting dates, or calculation error

**Solution:**
1. Verify date format is correct (YYYY-MM-DD)
2. Check effective date is in the future (not past)
3. In Forecast view:
   - Ensure you're viewing correct time period
   - Changes should appear in month/quarter of effective date
4. For position additions:
   - Set Start Date or Hire Date
   - Verify date is saved correctly
5. For position closures:
   - Set End Date or Termination Date
   - Check date is in correct field
6. Refresh scenario and view in Forecast
7. If dates still not working: Contact support

**See also:** [Effective Date](../scenarios/effective-date.md)

---

## Bulk Operations Issues

### Bulk Action Failed

**Problem:** Selected multiple positions but bulk action failed

**Cause:** Too many positions, mixed position types, or permission issue

**Solution:**
1. Reduce selection size:
   - Select fewer positions (try 50-100 at a time instead of 500+)
2. Verify all selected positions can have same action:
   - All can be closed
   - All can have salary updated
   - All belong to accessible scope
3. Check you have edit permissions
4. Try bulk action via:
   - Select positions → Right-click → Bulk action
   - Or use Taskbar → Bulk Operations
5. If action partially failed:
   - Check which positions succeeded
   - Retry failed positions separately
6. For very large bulk operations: Contact support for assistance

**See also:** [Bulk Operations](../scenarios/bulk-operations.md)

---

## Scenario Refresh Issues

### Scenario Refresh Not Available

**Problem:** Can't find scenario refresh option

**Cause:** Feature not available in current version, or permission issue

**Solution:**
1. Scenario refresh may still be in development
2. Check with Agentnoon support for availability
3. Alternative approaches:
   - Create new scenario from refreshed Main Org
   - Manually update changed positions
   - Use partial upload to update scenario data
4. Contact support to request scenario refresh feature

**See also:** [Scenario Refresh](../scenarios/scenario-refresh.md)

---

### Scenario Refresh Conflicts

**Problem:** Refreshing scenario but conflicts between scenario changes and Main Org

**Cause:** Both scenario and Main Org changed the same positions

**Solution:**
1. During refresh, review conflict resolution screen
2. For each conflict, choose:
   - Keep scenario change (preserve your modifications)
   - Use Main Org data (accept source system updates)
3. Carefully review each conflict before selecting
4. Make decisions based on:
   - Which data is more current
   - Which change is more important
   - Business requirements
5. Complete refresh
6. Review scenario after refresh to verify correct data
7. If refresh creates unexpected results: Contact support

---

## Performance Issues with Scenarios

### Scenario Slow to Load or Navigate

**Problem:** Large scenario takes long time to load or navigate

**Cause:** Scenario has many positions (>5,000) or complex changes

**Solution:**
1. Wait for initial load (can take 30-60 seconds for large orgs)
2. Use filters to narrow view:
   - Filter to specific department
   - Filter to specific layer
   - View smaller subset at a time
3. Switch to Directory view instead of Org Chart view
4. Close other browser tabs to free memory
5. Use more powerful computer if available
6. For very large scenarios:
   - Work in sections (department by department)
   - Use search to find specific positions
7. Consider breaking into multiple smaller scenarios

**See also:** [Performance Issues](performance-issues.md)

---

## When to Contact Support

**Contact support if:**
- Scenario corrupted or won't load after trying solutions
- Changes saving but not appearing in Change Tracker
- Approval workflow completely stuck
- Bulk operations failing repeatedly
- Scenario refresh causing data loss
- Performance unusable even after optimization

**Include in support request:**
- Scenario name
- Timestamp of issue
- Steps to reproduce
- Screenshots of error
- Organization name
- What you've already tried

**Contact:** support@agentnoon.com

---

## Next Steps

- Return to [Troubleshooting Overview](overview.md)
- Learn about [Scenario Creation](../scenarios/creating-scenarios.md)
- Review [Change Tracker](../scenarios/change-tracker.md)
- See [Approval Flows](../admin/configuring-approval-flows.md)
- Try [Bulk Operations](../scenarios/bulk-operations.md)
