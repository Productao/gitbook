---
description: Selecting multiple positions and performing bulk edits in Scenario Directory
hidden: false
---

# Bulk Operations

Bulk operations allow you to select multiple positions and apply changes simultaneously in Scenario Directory. This feature is only available in editable scenarios, not in Main Org Directory.

## Availability

**Where bulk operations work:**
- ✅ Scenario Directory (editable scenarios)
- ❌ Main Org Directory (view-only)
- ❌ Forecast Directory (aggregate planning)

**To use bulk operations:** Create or open a scenario, then switch to Directory view.

---

## Selecting Positions

### Single Selection

**How to select:**
- Click a row to highlight it
- Selected row changes color
- Click again to deselect

> **[Screenshot placeholder: Single row highlighted in Scenario Directory showing selected state with color change]**

**Use case:** Quick single-position edits

---

### Multiple Selection

**How to select:**
- Check checkboxes in the first column
- Select multiple positions at once
- Checkboxes appear only in Scenario Directory

> **[Screenshot placeholder: Multiple rows selected with checkboxes checked in first column of Scenario Directory]**

**Use case:** Bulk edits on specific positions

---

### Select All

**How to select:**
- Check the header checkbox (top of first column)
- Selects all rows matching current filters
- Does NOT select hidden/filtered-out rows

> **[Screenshot placeholder: Header checkbox in first column checked with all visible filtered rows selected below, showing "Department = Engineering" filter active]**

**Use case:** Bulk edits on entire filtered subset

**Example:**
- Filter to Department = Engineering
- Check "Select All" checkbox
- Only Engineering positions selected (other departments remain unselected)

---

### Selection Tips

1. **Filter before selecting all** - Narrow to relevant subset first
2. **Use Shift + Click** - Select range of positions (if supported)
3. **Deselect by unchecking** - Uncheck checkbox to remove from selection
4. **Clear selection** - Uncheck header checkbox to deselect all
5. **Visual feedback** - Selected rows highlight in blue/gray

---

## Bulk Edit Actions

Once positions are selected, you can apply bulk changes:

### Common Bulk Edits

**Update attribute for all selected positions:**
- Department
- Location
- Pay Grade
- Manager
- Custom fields

**Apply changes to selection:**
- Salary adjustments (% increase or flat amount)
- Bonus changes
- Start date updates
- Location transfers
- Department moves

---

### How to Bulk Edit

**Steps:**
1. Select multiple positions (checkboxes)
2. Click **Bulk Edit** button (appears when positions selected)
3. Choose attribute to change
4. Enter new value or adjustment
5. Click **Apply**
6. Changes apply to all selected positions

> **[Screenshot placeholder: Bulk Edit button appearing after position selection, with dialog showing attribute dropdown (Department, Location, Pay Grade, etc.) and new value field]**

**Confirmation:**
- Preview shows which positions will change
- Confirm before applying
- Changes tracked in scenario

> **[Screenshot placeholder: Bulk edit confirmation preview showing list of positions that will be changed with old and new values]**

---

## Bulk Edit Use Cases

### Update Department for Multiple Positions

**Scenario:** Move 15 positions from Marketing to Growth team

**Steps:**
1. Filter to Department = Marketing
2. Select the 15 positions (checkboxes)
3. Click **Bulk Edit**
4. Select **Department** attribute
5. Choose **Growth** as new value
6. Click **Apply**
7. All 15 positions updated

> **[Screenshot placeholder: Bulk edit in progress showing 15 selected Marketing positions with Department being changed to "Growth" in bulk edit dialog]**

---

### Apply Salary Increase to Filtered Subset

**Scenario:** Give 5% raise to all Software Engineers

**Steps:**
1. Filter to Job Title = "Software Engineer"
2. Click **Select All** checkbox
3. Click **Bulk Edit**
4. Select **Salary** attribute
5. Choose **Percentage increase** = 5%
6. Click **Apply**
7. All matching positions updated

> **[Screenshot placeholder: Bulk salary adjustment dialog showing "Percentage increase" option with 5% entered, applying to all selected Software Engineer positions]**

---

### Change Manager for Transitioning Team

**Scenario:** Reassign 20 positions to new manager after reorg

**Steps:**
1. Filter to current Manager = "Jane Smith"
2. Click **Select All**
3. Click **Bulk Edit**
4. Select **Manager** attribute
5. Choose new manager: "John Doe"
6. Click **Apply**
7. All positions now report to John Doe

---

### Move Positions to New Location

**Scenario:** Relocate 10 remote positions to San Francisco office

**Steps:**
1. Filter to Location = "Remote"
2. Select 10 specific positions
3. Click **Bulk Edit**
4. Select **Location** attribute
5. Choose **San Francisco**
6. Click **Apply**
7. Positions updated

---

## Bulk Deletion/Closure

Close multiple positions at once:

### Bulk Close Positions

**Steps:**
1. Select positions to close
2. Click **Bulk Actions** or **Close** button
3. Choose closure reason (RIF, Elimination, etc.)
4. Confirm bulk closure
5. Positions marked as closed in scenario

**Use case:**
- Modeling layoffs
- Eliminating redundant roles
- Restructuring departments

---

## Bulk Add/Copy

Create multiple new positions based on existing ones:

### Duplicate Position Multiple Times

**Steps:**
1. Select a position
2. Click **Duplicate** or **Copy**
3. Choose number of copies to create
4. Specify variations (e.g., different start dates)
5. Click **Create**
6. Multiple new positions added

**Use case:**
- Adding multiple similar roles
- Planning hiring pipeline
- Creating position templates

---

## Change Tracking

All bulk changes are tracked in scenarios:

**What gets tracked:**
- Which positions changed
- What attributes changed
- Old values and new values
- When changes were made
- Change symbols appear on position cards

**View changes:**
- Open **Change Tracker** panel
- See list of all changes
- Filter by change type
- Export change log

> **[Screenshot placeholder: Change Tracker panel showing list of bulk-edited positions with change symbols, old values, new values, and timestamp]**

---

## Best Practices

1. **Filter first, then select** - Narrow data before bulk selecting
2. **Preview before applying** - Review which positions will change
3. **Use Select All strategically** - Combine with filters for precise bulk edits
4. **Test on small subset first** - Try bulk edit on 2-3 positions before applying to hundreds
5. **Check change tracker after** - Verify changes applied correctly
6. **Create scenario copy** - Duplicate scenario before major bulk edits (backup in case of mistakes)
7. **Clear selection between operations** - Deselect all before starting new bulk edit

---

## Limitations

**Main Org Directory:**
- No bulk operations available
- View-only mode
- Cannot select or edit positions

**Forecast Directory:**
- No bulk operations
- Aggregate planning only
- Cannot edit individual positions

**Scenario Directory:**
- Bulk operations available
- Full editing capabilities
- Change tracking enabled

---

## Common Workflows

### Model Departmental Reorganization

**Steps:**
1. Filter to Department = Sales
2. Select all positions in "West Coast" region (filter + select)
3. Bulk edit Manager to new regional VP
4. Filter to "East Coast" region
5. Select all positions
6. Bulk edit Manager to different regional VP
7. Review changes in Change Tracker

---

### Apply Merit Increases by Pay Grade

**Steps:**
1. Filter to Pay Grade = 10
2. Select all
3. Bulk edit Salary: +3% increase
4. Clear filters
5. Filter to Pay Grade = 11
6. Select all
7. Bulk edit Salary: +4% increase
8. Repeat for other pay grades

---

### Relocate Remote Team to Office

**Steps:**
1. Filter to Department = Engineering
2. Filter to Location = Remote
3. Select all
4. Bulk edit Location to "Austin, TX"
5. Export updated roster

---

### Prepare for Layoffs (RIF Modeling)

**Steps:**
1. Filter to Department + criteria (e.g., low performers, redundant roles)
2. Select positions to eliminate
3. Bulk close positions with "RIF" reason
4. Review cost impact in Change Tracker
5. Export change log for finance review

---

## Troubleshooting

**Problem:** Bulk Edit button doesn't appear.
- **Solution:** Ensure you're in Scenario Directory (not Main Org). Check that at least one position is selected via checkbox.

**Problem:** Select All doesn't select all positions in org.
- **Solution:** Select All only selects visible/filtered rows. Clear filters to see all positions, or filter to intended subset first.

**Problem:** Bulk edit applied incorrect changes.
- **Solution:** Use scenario undo (if available) or revert scenario to previous state. Always preview before applying bulk edits.

**Problem:** Can't select positions (no checkboxes).
- **Solution:** Checkboxes only appear in Scenario Directory. Switch from Main Org to a scenario to enable bulk operations.

**Problem:** Changes don't appear in Change Tracker.
- **Solution:** Refresh the tracker panel. Ensure scenario is saved. Check that changes were actually applied (review positions individually).

---

## Next Steps

- Learn about [Scenario Directory](../scenarios/directory.md) for full editing capabilities
- Explore [Filtering & Sorting](filtering-sorting.md) to narrow bulk edit targets
- Try [Scenario Tracking & Analysis](../scenarios/tracking-analysis.md) to review bulk changes
- Master [Exporting](exporting.md) to create change logs

