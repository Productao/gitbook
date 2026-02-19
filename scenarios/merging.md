---
description: Combine changes from multiple scenarios into one
hidden: false
---

# Scenario Merging

Scenario Merging enables users to merge one scenario into another, consolidating changes while preserving structure, tracking conflicts, and maintaining data integrity.

---

## Overview

**What is Scenario Merging?**

Scenario Merging allows you to bring selected records and fields from a **source scenario** into a **destination scenario**, combining the work of multiple planners into a single unified plan.

**When to use Scenario Merging:**
- Multiple teams are working on separate scenarios
- Independent organizational branches need to be combined
- One scenario should become the source of truth for another
- Consolidating planning efforts across different parts of the organization

**Key capabilities:**
- Merge entire scenarios or selected records
- Merge all fields or specific attributes
- Automatic destination backup before merge
- Clear conflict visibility and filtering
- Flexible source-of-truth control

---

## How Scenario Merging Works

### Basic Workflow

1. **Source scenario** - The scenario you're copying changes FROM
2. **Destination scenario** - The scenario you're merging changes INTO
3. **Select records** - Choose which positions to merge
4. **Select fields** - Choose which fields to merge
5. **Review summary** - See what will be merged
6. **Resolve conflicts** - Decide how to handle overlapping changes
7. **Automatic backup** - System creates backup of destination before merge
8. **Merge complete** - Source changes incorporated into destination

---

## Use Case 1: Merging Independent Teams (No Conflicts)

**Scenario:** Two planners working on completely separate parts of the organization with no overlap.

### Example Setup

In this example:
- **Main Org:** Teresa (CEO) → Betsy, Claudia, Sam (direct reports)
- **Scenario A:** "Betsy's Team" - Changes only to Betsy's organization
- **Scenario B:** "Sam's Team" - Changes only to Sam's organization

These teams operate under different branches of the organization and do not overlap, meaning **there are no structural conflicts**.

---

### How to Merge a Scenario

To merge Sam's team into Betsy's scenario:

#### Step 1: Navigate to Data Management

1. Open the **destination scenario** ("Betsy's Team")
2. Open taskbar → **Data Management**
3. Click **Merge Scenario**

#### Step 2: Select Source Scenario

1. Choose the source scenario (e.g., "Sam's Team") from the dropdown
2. Click **Next**

#### Step 3: Select Records

Choose the individuals you want to merge:
- **Select All** to merge the entire scenario
- Or use filters from the source board to bring a filtered subset
- Click **Next** to proceed

#### Step 4: Select Fields

You can control which fields are merged:
- **Select All Fields** to fully replicate the source scenario
- Or choose **specific fields** (e.g., salary, projects, role changes)
- Click **Next** to continue

#### Step 5: Review Summary

The system provides a summary including:
- **Source board:** "Sam's Team"
- **Destination board:** "Betsy's Team"
- **Selected records:** All positions from Sam's scenario listed
- **Selected fields:** Fields that will be merged
- **Automatic backup:** Created before merge

Click **Next** to proceed.

#### Step 6: Conflict Review

If conflicts exist, they are displayed on this screen.
- Use **"Show only conflicts"** filter to view only conflicting records
- In this use case: **No conflicts** appear because the teams are independent

To complete the process:
1. Select **"Merge All Fields to Destination"**
2. Click **Merge**

---

### Result

**What happens after merge:**
- Sam's entire team is now merged into Betsy's Team scenario
- Both teams exist as separate roots (since they don't report to each other)
- All changes made in Sam's original scenario were preserved
- No structural conflicts occurred

**Post-merge cleanup (if needed):**

If both merged teams appear as separate roots:
- Click on each team's top node
- Select **"Make Root"** to ensure both are roots of the organization
- Or reassign reporting structure if they should connect

---

## Use Case 2: Merging with Structural Changes & Conflicts

**Scenario:** Multiple structural changes were made across scenarios, creating conflicts.

### Example Setup

In this case:
- **Scenario A:** "Sam's Team" - Focused changes to Sam's organization
- **Scenario B:** "Full Org" - Company-wide changes including:
  - Moved positions from Betsy → Claudia
  - Moved positions from Sam → Claudia
  - Performed reductions in force (RIF)
  - Added new positions

**Result:** Both scenarios contain changes affecting overlapping data = conflicts to resolve

---

### Merge Process

The steps remain the same:

1. Open destination scenario ("Full Org")
2. **Data Management** → **Merge Scenario**
3. Choose source scenario ("Sam's Team")
4. **Select All** records
5. **Select All** fields
6. Click **Next** through summary

---

### Conflict Resolution

Because both scenarios contain changes affecting overlapping data, the system detects conflicts.

**What you can do:**
- Review all conflicts
- Filter to view only conflicting records
- Choose which version should take precedence

**If the source scenario is considered the source of truth:**
1. Select **"Merge All Fields to Destination"**
2. Click **Merge**

---

### Result

**What happens after merge:**
- Sam's scenario is fully integrated into the full organizational scenario
- Source changes override destination conflicts (if selected)
- The destination scenario is updated accordingly
- A backup of the original destination scenario is preserved

---

## Understanding Conflicts

### What Causes Conflicts?

Conflicts occur when **both scenarios modified the same position**:
- Same position moved to different managers
- Same position salary changed to different values
- Same position closed in one scenario, edited in another
- Reporting structure changed differently in both scenarios

---

### Current Conflict Resolution

**Today:** All-or-nothing approach
- **Merge All Fields to Destination** - Source wins for all conflicts
- **Cancel** - Keep destination as-is, don't merge

**Future capability:** Field-by-field conflict resolution UI (not currently available)

---

## Best Practices

### Before Merging

**Use independent scenarios to model separate team changes:**
- Assign non-overlapping parts of org to different planners
- Example: Planner A owns EMEA, Planner B owns Americas

**Use Partial Org scenarios:**
- Create scenarios focused on specific departments/regions
- Reduces chance of conflicts

**Communicate changes:**
- Let other planners know what you're changing
- Avoid working on same positions simultaneously

---

### During Merge

**Review conflicts carefully when merging overlapping structures:**
- Always check "Show only conflicts" view
- Understand what you're overwriting before proceeding

**Use full-field merge when the source scenario represents the latest approved version:**
- If source is the source of truth, use "Merge All Fields"
- Don't hesitate to choose destination if it's more accurate

**Test with small merges first:**
- Merge a subset to verify behavior
- Then merge full scenario once confident

**Leverage backups to safely experiment with structural changes:**
- System automatically creates backup before merge
- Can revert if merge doesn't work as expected

---

### After Merge

**Verify merged result:**
- Check that all expected changes appear
- Review conflict resolutions
- Test org chart structure integrity

**Communicate completion:**
- Let other planners know merge is complete
- Share combined scenario for review

---

## Limitations and Considerations

### Current Limitations

- **All-or-nothing conflict resolution** - Can't pick and choose which fields to use from source vs destination
- **No automatic conflict detection before starting** - Only see conflicts at final step
- **Manual root assignment** - Merged teams may need manual reconnection to hierarchy

---

### When NOT to Use Merge

- **Scenarios with significant overlap** - Better to coordinate in single scenario
- **Final approved scenarios** - Don't merge into approved scenarios (create new instead)
- **Scenarios with different baselines** - If scenarios started from different Main Org snapshots

---

### Alternative Approaches

Instead of merging, consider:
- **[Scenario Comparison](comparisons.md)** - Compare scenarios side-by-side without merging
- **Manual recreation** - Manually apply changes from one scenario to another
- **[Approval workflow](approvals.md)** - Route scenarios through approvals separately

---

## Troubleshooting

### Problem: Merge Created Duplicate Positions

**Cause:** Both scenarios created new positions with same attributes

**Solution:**
- Review merged scenario for duplicates
- Delete one of the duplicate positions
- In future, coordinate new position creation

---

### Problem: Hierarchy Broken After Merge

**Cause:** Merged scenarios had different reporting structures

**Solution:**
- Click broken hierarchy icon (orange link) in taskbar
- Review detached positions
- Reassign managers to reconnect hierarchy
- Or escalate to roots as needed

---

### Problem: Can't See Merged Changes

**Cause:** Filters or view settings hiding merged positions

**Solution:**
- Clear all filters
- Check "Show After" view (not "Show Before")
- Search for specific merged positions

---

### Problem: Merged Wrong Scenario

**Cause:** Selected wrong source scenario

**Solution:**
- Use automatic backup created before merge
- Restore from backup
- Re-do merge with correct source

---

## Related Features

- [Scenario Comparisons](comparisons.md) - Compare scenarios without merging
- [Scenario Collaboration](collaboration.md) - Share scenarios with team
- [Scenario Refresh](refresh.md) - Update scenario with Main Org changes
- [Bulk Operations](bulk-operations.md) - Select and modify many positions at once

---

## Future Enhancements

Features under consideration:
- Field-level conflict resolution UI
- Automatic conflict detection before merge starts
- Preview mode to see merge result before committing
- Partial field merge (merge only salary, not title, etc.)
- Merge conflict history and audit trail
