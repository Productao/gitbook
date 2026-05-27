---
description: Resolve scenario planning problems
---

# 🎯 Scenario Issues

Common solutions for scenario save failures, approval problems, change tracking issues, and drag-and-drop issues.

## Save & Load Issues

**Can't make changes to a scenario**

* Check if the scenario is locked (submitted for approval) — cannot edit until returned or rejected
* Verify you have edit permissions (not view-only)
* Locked scenarios display a visual indicator that editing is disabled

**Changes keep reverting**

* Changes autosave as you make them — if changes appear to revert, check your internet connection
* Clear browser cache; if still reverting, try a different browser and contact suppo

**Scenario won't load / blank screen**

* Wait 30–60 seconds for large orgs to load
* Clear cache, refresh (Ctrl+R), or try incognito mode
* If only this scenario fails to load, the scenario may be corrupted — contact support with the scenario name

**Can't create new scenario**

* Verify the Main Org has data loaded (scenarios require a baseline)
* Check you have edit/admin permissions and that your plan's scenario limit has not been reached

## Position Editing Issues

**Can't add / edit positions**

* Confirm the scenario is not locked and you have edit permissions
* Right-click a manager card → "Add Direct Report"
* For field-level restrictions (e.g., salary hidden), contact your admin

**Drag-and-drop not working**

* Refresh, clear cache, or try Chrome (recommended)
* Disable browser extensions (especially ad blockers)
* Alternative: Right-click position → **Change Manager** → select from dropdown
* For bulk moves, use Bulk Operations instead

**Can't delete / close position**

* Reassign or close direct reports first, then close the parent
* Main Org positions can be "closed" in a scenario but not deleted — use the Reduction interaction

## OpEx Panel Issues

**OpEx Panel not updating**

* Click Save while making an edit, wait a few seconds, then refresh
* Open via the 👀 icon; if still not updating, close and reopen the scenario

**Wrong cost / headcount numbers**

* Check the formula dropdown (Salary vs. Total Comp vs. Custom)
* Verify effective dates — future-dated changes may not appear in the current period
* Ensure you're in "Show Changes" mode (not "Show After")

**Can't see individual change details**

* Expand the panel and click Additions / Reductions / Data Changes to expand each category

## Scenario Comparison Issues

**No differences showing**

* Confirm you're comparing two different scenarios
* Refresh and try the Comparisons tab: open Scenario A > Comparisons > select Scenario B

**Comparison option missing**

* You need 2 scenarios
* Contact admin to confirm access level

## Sharing & Collaboration Issues

**Can't share / team members can't access**

* Verify team members have Agentnoon accounts and their access scope includes the relevant data
* Share via Scenario menu → Share

**Conflicting edits from multiple users**

* Concurrent editing is limited — coordinate edit times or assign ownership
* If conflict occurs, refresh to see latest changes and re-apply yours carefully

## Approval Workflow Issues

**Can't submit for approval**

* Confirm the scenario has changes (check OpEx Panel)
* Ensure all changes are saved; verify you have submit permissions
* Contact admin if approval workflow needs configuration: [Configuring Approval Flows](../admin/configuring-approval-flows.md)

**Scenario stuck in approval**

* Check which approver level is pending; follow up with that approver directly
* Contact admin to reassign if the approver is unavailable

**Approval rejected — need to revise**

1. Open the (now unlocked) scenario and review rejection comments
2. Make requested changes and save
3. Resubmit via OpEx Panel → Submit for Approval

**Scenario locked — can't edit**

* Wait for approval/rejection, or withdraw the submission if that option is available
* Or duplicate the scenario (Scenario Management → Duplicate) and edit the copy

## Effective Date Issues

**Dates not applying correctly**

* In Forecast, confirm you're viewing the correct time period — changes appear in the month/quarter of their effective date
* Ensure Start Date vs. End Date fields are correctly used for additions vs. closures

## Bulk Operations Issues

**Bulk action failed**

* Reduce selection size (try 50–100 at a time instead of 500+)
* Verify all selected positions support the same action and are within your access scope
* Check failed positions individually; retry separately if needed

## When to Contact Support

Contact [SupportSWP@dayforce.com](mailto:SupportSWP@dayforce.com) if:

* Scenario is corrupted or won't load after trying the steps above
* Changes are saving but not appearing in OpEx Panel
* Bulk operations fail repeatedly
* Approval workflow is completely stuck

Include: scenario name, timestamp, steps to reproduce, screenshots, and what you've already tried.
