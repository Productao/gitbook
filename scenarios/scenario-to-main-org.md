---
description: Implement approved scenarios to your Main Org
hidden: false
---

# Scenario to Main Org

After a scenario has been approved, you can merge it back into your Main Org, making the planned changes your organization's new reality.

---

## Overview

**What is Scenario to Main Org?**

This feature allows you to take an **approved scenario** and merge it into your **Main Org**, implementing your planned changes as the new baseline organizational structure.

**Key points:**
- Only **approved scenarios** can be merged to Main Org
- Only **admins** can perform this operation
- Changes are permanent once merged
- New positions created in scenarios can be included
- Conflicts are resolved before merge

---

## Prerequisites

Before you can merge a scenario to Main Org:

1. **Scenario must be approved** - Only approved scenarios appear in the merge list
2. **Admin permissions required** - This is an admin-only feature
3. **Review changes thoroughly** - Ensure scenario is ready for implementation

---

## When to Use Scenario to Main Org

Use this feature when:
- Scenario has gone through approval workflow and been approved
- You're ready to implement planned changes organization-wide
- The scenario represents the new organizational reality
- Changes should become the baseline for future scenarios

**Common use cases:**
- Implementing approved reorganization
- Finalizing annual hiring plan
- Applying approved headcount changes
- Making approved structural changes permanent

---

## Use Case 1: Merging Full Company Scenario

**Scenario:** You've modeled company-wide organizational changes and received approval. Now implement them.

### Example Setup

- **Main Org:** Current organizational structure with CEO at top
- **Scenario:** "Full Company Reorganization" (approved)
  - Moved positions reporting to different managers
  - Added new positions
  - Changed reporting structures

---

### How to Merge Full Company Scenario to Main Org

#### Step 1: Navigate to Main Org

1. Return to **Main Org** view
2. Open taskbar → **Data Management**
3. Click **Merge Approved Scenarios to Main**

#### Step 2: Select Approved Scenario

1. System shows only **approved scenarios**
2. Select "Full Company Reorganization" from the list
3. Click **Next**

#### Step 3: Select Fields to Merge

Choose which fields to bring from scenario into Main Org:

**Option A: Merge all fields** (most common)
- Click **Select All**
- All changes from scenario applied to Main Org
- Scenario becomes complete source of truth

**Option B: Selective field merge**
- Example: Only modeling department changes
- Select only **Department** field
- Other fields remain unchanged in Main Org

For this example: **Select All** to merge everything.

Click **Next** to continue.

#### Step 4: Review Confirmation Summary

The confirmation screen shows:
- **Source scenario:** "Full Company Reorganization"
- **Destination:** Main Organization
- **Fields selected:** All fields (e.g., 14 fields)
- **Include new positions checkbox:** Check this to bring new positions created in scenario

**Include New Positions:**
- ✅ **Checked:** New positions from scenario added to Main Org
- ❌ **Unchecked:** Only changes to existing positions applied

#### Step 5: Review Conflicts

The system shows all conflicts between scenario and Main Org.

**What are conflicts?**
Conflicts occur when:
- Scenario value differs from Main Org value
- Same position was edited in both places
- Reporting structure changed

**Resolving conflicts:**

**Option: Use scenario values for all conflicts**
- Click **"Use Scenario Values for All Conflicts"**
- Scenario becomes source of truth
- All scenario values override Main Org values

This is the recommended approach for approved scenarios.

#### Step 6: Merge to Main

1. Click **"Merge to Main"**
2. System processes the merge
3. Wait for confirmation

#### Step 7: Verify Changes

Once merge completes:
- Navigate through Main Org to see changes applied
- New positions appear (if checkbox was checked)
- Changed reporting structures visible
- All scenario edits now permanent in Main Org

---

### Example Changes Applied

In the example scenario, these changes were merged:
1. **Moved positions:** Dropped positions previously under different manager, moved one level up to report directly to CEO
2. **Reorganized reporting:** CHRO previously under CEO, moved to report under Sam Hart
3. **New position created:** Content Strategist created under Sam Hart

All these changes now appear in Main Org permanently.

---

## Use Case 2: Merging Partial Org Scenario

**Scenario:** You've created a scenario focused on one specific team/manager and received approval. Now implement those changes.

### Example Setup

- **Main Org:** Full organizational structure
- **Scenario:** "Sam's Team" (partial org, approved)
  - Changes only to Sam Hart's organization
  - Reporting structure modifications
  - Position changes within that team

---

### How to Merge Partial Org Scenario to Main Org

#### Step 1: Access Merge Function

1. Navigate to **Main Org**
2. **Data Management** → **Merge Approved Scenarios to Main**

#### Step 2: Select Partial Scenario

1. Select "Sam's Team" from approved scenarios list
2. Click **Next**

#### Step 3: Select All Fields

1. Click **Select All** (or choose specific fields)
2. Check **Include New Positions** if scenario created new roles
3. Click **Next**

#### Step 4: Resolve Conflicts

1. Review conflicts (if any)
2. Click **"Use Scenario Values for All Conflicts"**
3. Scenario becomes source of truth for Sam's team

#### Step 5: Merge to Main

1. Click **"Merge to Main"**
2. Wait for completion
3. Changes to Sam's team now live in Main Org

---

### Result

**What happens:**
- Sam's team structure updated in Main Org
- Only changes within Sam's organization applied
- Rest of Main Org unaffected
- New scenario's reporting structure becomes reality

---

## Understanding the Merge Process

### What Gets Merged

**Positions:**
- All position changes from scenario
- New positions (if checkbox checked)
- Closed positions (deletions)
- Moved positions (reporting changes)

**Fields:**
- Any fields selected during merge process
- Common: All fields (complete scenario implementation)
- Or selective: Only specific fields (e.g., just departments)

**Structure:**
- Reporting relationships updated
- Hierarchy changes applied
- Organizational structure modified

---

### What Doesn't Get Merged

- Changes from unapproved scenarios (not in the list)
- Fields not selected during merge
- New positions if checkbox unchecked

---

## Conflict Resolution

### Understanding Conflicts

**Conflicts happen when:**
- Main Org has changed since scenario was created
- Same position edited in both Main Org and scenario
- Position exists in scenario but deleted in Main Org
- Position deleted in scenario but edited in Main Org

### Resolving Conflicts

**Current approach:** Use scenario as source of truth
- Click **"Use Scenario Values for All Conflicts"**
- All scenario changes override Main Org
- Recommended for approved scenarios (they've been reviewed and approved)

**Why this works:**
- Scenario went through approval process
- Changes were intentional and authorized
- Approved scenarios should be trusted

---

## Best Practices

### Before Merging

1. **Verify scenario is approved**
   - Only approved scenarios can be merged
   - Ensure approval workflow completed

2. **Review scenario one more time**
   - Open scenario and verify all changes correct
   - Check Change Tracker for complete impact
   - Ensure nothing unexpected

3. **Communicate to stakeholders**
   - Notify affected teams that changes are being implemented
   - Set expectations for when changes go live

4. **Choose timing wisely**
   - Merge during low-activity periods if possible
   - Coordinate with team announcements

### During Merge

5. **Select fields carefully**
   - Usually "Select All" is correct
   - Only use selective fields if you have specific reason

6. **Check "Include New Positions" appropriately**
   - ✅ Check if scenario created new roles to implement
   - ❌ Uncheck if new positions were hypothetical only

7. **Use scenario values for conflicts**
   - Approved scenarios should override Main Org
   - They represent intended future state

### After Merge

8. **Verify implementation**
   - Browse Main Org to confirm changes applied
   - Check specific positions that were modified
   - Verify new positions appear (if included)

9. **Communicate completion**
   - Notify stakeholders that changes are live
   - Share updated org chart if needed

10. **Archive approved scenario**
    - Scenario can be archived or deleted after successful merge
    - Or keep for historical record

---

## Limitations and Important Notes

### Admin-Only Feature

- **Only admins** can merge scenarios to Main Org
- Regular users cannot access this functionality
- If you need access, request admin permissions

### Approved Scenarios Only

- **Only approved scenarios** appear in merge list
- Scenarios in draft or pending approval cannot be merged
- Complete approval workflow first

### Permanent Changes

- **Merge is permanent** - Changes become part of Main Org
- Cannot "undo" a merge (would need new scenario to reverse)
- Ensure scenario is correct before merging

### No Preview Mode

- Cannot preview merge before committing
- Review scenario thoroughly before initiating merge
- Use Change Tracker to understand impact

---

## Troubleshooting

### Problem: My Approved Scenario Doesn't Appear in List

**Cause:** Scenario may not be fully approved, or you're not an admin

**Solution:**
1. Verify scenario status shows "Approved"
2. Check that you have admin permissions
3. Refresh the page and try again

---

### Problem: New Positions Didn't Merge

**Cause:** "Include New Positions" checkbox was unchecked

**Solution:**
- The merge is already complete (permanent)
- Create new scenario with just the new positions
- Get it approved and merge again

---

### Problem: Some Changes Didn't Apply

**Cause:** Those fields weren't selected during merge, or conflicts weren't resolved

**Solution:**
- Review what fields were selected during merge
- Check if conflicts were resolved with scenario values
- If needed, create corrective scenario and merge again

---

### Problem: Merge Taking Long Time

**Cause:** Large organization with many changes

**Solution:**
- Wait for process to complete (don't refresh page)
- System is processing all changes
- Larger orgs and more changes = longer processing time

---

## Related Features

- [Scenario Approvals](approvals.md) - Approve scenarios before merging
- [Scenario Merging](merging.md) - Merge one scenario into another
- [Change Tracker](tracking-analysis.md) - Review impact before merging
- [Scenario Comparisons](comparisons.md) - Compare scenario to Main Org

---

## Future Enhancements

Features under consideration:
- Preview mode before merging to Main Org
- Selective conflict resolution (choose per-conflict)
- Scheduled merges (implement at specific date/time)
- Rollback capability (undo merge)
- Partial merge (only specific positions to Main Org)
