---
description: Combine changes from multiple scenarios into one
hidden: false
---

# Scenario Merging

Scenario Merging allows you to combine changes from one scenario into another, enabling collaborative planning where multiple people work on different parts of the organization simultaneously.

---

## Overview

**What is Scenario Merging?**

Merge functionality lets you take changes from a source scenario and bring them into a destination scenario, combining the work of multiple planners into a single unified plan.

**Common use cases:**
- Multiple teams working on different departments simultaneously
- Combining regional planning scenarios into a global scenario
- Merging approved changes from one scenario into your working scenario
- Consolidating parallel planning efforts before final review

---

## How Scenario Merging Works

### Basic Workflow

1. **Source scenario** - The scenario you're copying changes FROM
2. **Destination scenario** - The scenario you're merging changes INTO
3. **Selection** - Choose which positions and fields to merge
4. **Conflict resolution** - Decide how to handle overlapping changes
5. **Automatic backup** - System creates backup of destination before merge
6. **Merge complete** - Source changes incorporated into destination

---

## Use Case 1: Merging Non-Overlapping Scenarios

**Scenario:** Two planners working on completely separate parts of the org with no overlap.

### Example Setup
- **Main Org:** Teresa (CEO) → Betsy, Claudia, Sam (direct reports)
- **Scenario A:** "Betsy's Team" - Changes only to Betsy's organization
- **Scenario B:** "Sam's Team" - Changes only to Sam's organization

Since these are **separate organizational nodes** with no shared positions, merging is straightforward with no conflicts.

### Step-by-Step: Merging Sam's Team into Betsy's Team

1. **Open destination scenario**
   - Navigate to "Betsy's Team" scenario

2. **Access merge function**
   - Open taskbar → **Data Management**
   - Click **Merge Scenario** functionality

3. **Select source scenario**
   - Choose "Sam's Team" from the dropdown
   - Click **Next**

4. **Select positions to merge**
   - Click **Select All** to bring entire Sam's team
   - **Optional:** Use filters from source board to bring filtered subset
   - Click **Next**

5. **Select fields to merge**
   - **Select All** - Updates all fields from source scenario
   - **Or select specific fields** - Only merge salary, department, etc.
   - Click **Next**

6. **Review summary**
   - **Source board:** "Sam's Team"
   - **Destination board:** "Betsy's Team"
   - **Automatic backup:** Created before merge
   - **People included:** All positions from Sam's scenario listed
   - Click **Next**

7. **Check for conflicts**
   - Toggle **"Show only conflicts"** to filter view
   - In this case: **No conflicts** (separate organizational nodes)
   - Click **Merge All Fields to Destination**

8. **Merge complete**
   - Sam's entire team now appears in Betsy's Team scenario
   - Both teams exist as separate roots (since they don't report to each other)
   - All changes from Sam's scenario preserved

### Post-Merge Cleanup

If both merged teams appear as separate roots:
- Click on each team's top node
- Select **"Make Root"** to ensure both are roots of the organization
- Or reassign reporting structure if they should connect

---

## Use Case 2: Merging Overlapping Scenarios with Conflicts

**Scenario:** Two planners made changes to the same positions, creating conflicts.

### Example Setup
- **Scenario A:** "Sam's Team" - Focused changes to Sam's organization
- **Scenario B:** "Full Org" - Company-wide changes including:
  - Moved positions from Betsy → Claudia
  - Moved positions from Sam → Claudia
  - Performed RIF (closures)
  - Added new positions

**Result:** Overlapping changes to same positions = conflicts to resolve

### Step-by-Step: Merging with Conflict Resolution

1. **Open destination scenario**
   - Navigate to "Full Org" scenario

2. **Select source scenario**
   - Data Management → Merge Scenario
   - Select "Sam's Team"
   - Click **Next**

3. **Select all positions and fields**
   - Select All positions
   - Select All fields
   - Click **Next**

4. **Review conflicts**
   - System shows all positions with conflicting changes
   - **Toggle "Show only conflicts"** to focus on problem areas

5. **Resolve conflicts**

   **Option A: Trust source completely**
   - Click **"Merge All Fields to Destination"**
   - Sam's scenario becomes source of truth
   - All his changes overwrite conflicting changes in Full Org

   **Option B: Selective merge (future functionality)**
   - Review each conflict individually
   - Choose source or destination value for each field
   - Not currently available - today it's all-or-nothing

6. **Merge complete**
   - Source scenario changes incorporated
   - Conflicts resolved per your selection
   - Backup created automatically

---

## Conflict Resolution Rules

### What Causes Conflicts?

Conflicts occur when **both scenarios modified the same position**:
- Same position moved to different managers
- Same position salary changed to different values
- Same position closed in one scenario, edited in another

### Current Conflict Resolution

**Today:** All-or-nothing approach
- **Merge All to Destination** - Source wins for all conflicts
- **Cancel** - Keep destination, don't merge

**Future:** Field-by-field conflict resolution UI

---

## Best Practices

### Before Merging

1. **Coordinate planning boundaries**
   - Assign non-overlapping parts of org to different planners
   - Example: Planner A owns EMEA, Planner B owns Americas

2. **Use Partial Org scenarios**
   - Create scenarios focused on specific departments/regions
   - Reduces chance of conflicts

3. **Communicate changes**
   - Let other planners know what you're changing
   - Avoid working on same positions simultaneously

### During Merge

4. **Review carefully**
   - Always check "Show only conflicts" view
   - Understand what you're overwriting

5. **Test with small merges first**
   - Merge a subset to verify behavior
   - Then merge full scenario

6. **Leverage automatic backups**
   - System creates backup before merge
   - Can revert if merge doesn't work as expected

### After Merge

7. **Verify merged result**
   - Check that all expected changes appear
   - Review conflict resolutions
   - Test org chart structure integrity

8. **Communicate completion**
   - Let other planners know merge is complete
   - Share combined scenario for review

---

## Limitations and Considerations

### Current Limitations

- **All-or-nothing conflict resolution** - Can't pick and choose which fields to use from source vs destination
- **No automatic conflict detection** before starting - Only see conflicts at final step
- **Manual root assignment** - Merged teams may need manual reconnection to hierarchy

### When NOT to Use Merge

- **Scenarios with significant overlap** - Better to coordinate in single scenario
- **Final approved scenarios** - Don't merge into approved scenarios (create new instead)
- **Scenarios with different baselines** - If scenarios started from different Main Org snapshots

### Alternative Approaches

Instead of merging, consider:
- **Scenario Comparison** - Compare scenarios side-by-side without merging
- **Manual recreation** - Manually apply changes from one scenario to another
- **Approval workflow** - Route scenarios through approvals separately

---

## Troubleshooting

### Problem: Merge Created Duplicate Positions

**Cause:** Both scenarios created new positions with same attributes

**Solution:**
- Review merged scenario for duplicates
- Delete one of the duplicate positions
- In future, coordinate new position creation

### Problem: Hierarchy Broken After Merge

**Cause:** Merged scenarios had different reporting structures

**Solution:**
- Click broken hierarchy icon (orange link) in taskbar
- Review detached positions
- Reassign managers to reconnect hierarchy
- Or escalate to roots as needed

### Problem: Can't See Merged Changes

**Cause:** Filters or view settings hiding merged positions

**Solution:**
- Clear all filters
- Check "Show After" view (not "Show Before")
- Search for specific merged positions

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
