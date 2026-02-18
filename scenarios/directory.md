---
description: Table view in scenarios with change highlighting
hidden: false
---

# Scenario Directory

The Directory View in scenarios provides a spreadsheet-style table of all positions with powerful editing capabilities. Unlike Main Org Directory (which is view-only), Scenario Directory lets you select, edit, and export changed data.


> **[Screenshot placeholder: Scenario directory view showing spreadsheet-style table with positions]**
## What is Scenario Directory?

Directory View displays all positions in your scenario as a table, similar to Excel or Google Sheets. Each row represents a position, and each column represents an attribute (Name, Title, Department, Salary, Change Type, etc.).

**Key difference from Main Org Directory:**
- **Main Org Directory:** View-only, sort, filter, export
- **Scenario Directory:** All of the above PLUS bulk selection, bulk editing, change highlighting

---

## When to Use Scenario Directory

**Use Directory View when:**
- Selecting many positions for bulk actions
- Reviewing all changes in list format
- Filtering to specific change types (additions, closures, edits)
- Sorting by cost impact or effective date
- Exporting scenario data to Excel
- Comparing before/after values side-by-side

**Use Org Chart View when:**
- Visualizing reporting relationships
- Understanding org structure changes
- Presenting to stakeholders visually
- Dragging positions to new managers

**Best practice:** Use both views. Directory for analysis and bulk actions, Org Chart for structure and presentation.

---

## Accessing Scenario Directory

**From inside a scenario:**
1. Click the **Directory** icon in the taskbar (table/grid symbol)
2. Or click **Org Chart dropdown** → **Directory**
3. Or press keyboard shortcut **5**

**What you see:**
- Table of all positions in the scenario
- Standard columns (Name, Title, Department, Salary, Manager)
- Scenario-specific columns (Change Type, Effective Date, Cost Impact)
- Color-coded rows indicating changes

---

## Scenario Directory Interface

### Columns in Scenarios

**Standard columns** (same as Main Org):
- Name
- Job Title
- Department
- Manager
- Location
- Pay Grade
- Salary

**Scenario-specific columns:**
- **Change Type** - Addition, Reduction, Modification, or None
- **Effective Date** - When this change takes effect
- **Cost Impact** - Dollar impact of this change
- **Before Value** - Original value (for modifications)
- **After Value** - New value (for modifications)
- **Change Reason** - Why changed (RIF, Exit, Promotion, etc.)

**Custom columns:**
- Any fields your admin has configured
- Calculated fields (SOC, Total Org Size, Layer)

---

### Customizing Columns

**Add/remove columns:**
1. Click the column settings icon (gear or three dots)
2. Check/uncheck columns to show/hide
3. Scenario columns (Change Type, Effective Date) are especially useful
4. Changes apply immediately

**Reorder columns:**
- Drag column headers to rearrange

**Resize columns:**
- Drag the column border to adjust width

**Pro tip:** Show "Change Type" and "Cost Impact" columns to quickly see all modifications and their financial effect.

---

## Change Highlighting

Scenario Directory uses **color-coding** to indicate changes:

**Color scheme:**
- **Green row** - Newly added position
- **Red row** - Position closed/RIF'd
- **Blue row** - Position modified (edited attributes)
- **White/default row** - No change from Main Org

**Visual indicators:**
- Bold text for changed fields
- Strikethrough for closed positions
- Icons in Change Type column

**How to use:**
- Quickly scan for all green (additions)
- Review all red (reductions) before finalizing
- Check blue rows to see what was modified

---

## Sorting in Scenarios

Sort data by any column:

1. Click a column header to sort ascending
2. Click again to sort descending
3. Click a third time to remove sort

**Scenario-specific sorts:**
- **Change Type** - Group all additions, reductions, modifications
- **Effective Date** - See changes in chronological order
- **Cost Impact** - Sort by financial impact (highest to lowest)
- **Salary** - Find highest-cost positions

**Multi-column sorting:**
- Hold Shift and click multiple column headers
- Example: Sort by Change Type, then by Effective Date

---

## Filtering in Scenarios

Apply filters to show only specific rows:

1. Click the **Filter** icon
2. Select an attribute (Department, Location, Change Type, etc.)
3. Choose values to include
4. Click **Apply**

**Scenario-specific filters:**

**Filter by Change Type:**
- Show only **Additions** - See all new positions
- Show only **Reductions** - Review all RIFs/exits
- Show only **Modifications** - See what changed
- Show only **No Change** - See unmodified positions

**Filter by Effective Date:**
- Show positions effective in Q1
- Show positions effective in Q2
- Filter by date range

**Filter by Cost Impact:**
- Show positions with cost increase > $100K
- Show positions with cost decrease
- Show cost-neutral changes

**Common filter combinations:**
- **Department = "Engineering" AND Change Type = "Addition"** - All new Engineering hires
- **Change Type = "Reduction" AND Department IN ("Sales", "Marketing")** - All RIFs in go-to-market teams
- **Effective Date >= "2026-04-01" AND Effective Date <= "2026-06-30"** - All Q2 changes

---

## Bulk Selection in Scenarios

Scenario Directory supports powerful bulk selection for mass actions.

### Selecting Positions

**Select individual positions:**
- Click checkbox next to each row

**Select all visible positions:**
- Click checkbox in header row
- All filtered positions selected

**Select range:**
- Click first checkbox
- Hold Shift
- Click last checkbox
- All positions in range selected

**Deselect:**
- Click checkbox again to deselect
- Or click "Clear selection"

---

### Bulk Actions After Selection

Once you've selected multiple positions, bulk edit panel opens:

**Available bulk actions:**
1. **Edit Attributes** - Change department, location, title for all
2. **Change Manager** - Reassign to different manager
3. **Close Positions** - Mark as RIF or Exit
4. **Detach Employees** - Remove people from positions
5. **Move to Bench** - Place employees on bench
6. **Export Selection** - Export only selected rows

**Learn more:** [Bulk Operations](bulk-operations.md)

---

## Common Scenario Directory Workflows

### Workflow 1: Review All Additions Before Submitting

**Goal:** Verify all new positions are correct before approval.

**Steps:**
1. Open Scenario Directory
2. Click **Filter** → **Change Type** → **Addition**
3. Review list of all new positions
4. Sort by **Salary** to check compensation
5. Sort by **Effective Date** to verify timing
6. Export to PDF for documentation

**Result:** Confident all additions are accurate.

---

### Workflow 2: Select and Close 20 Positions for Budget Cut

**Goal:** Reduce cost by closing specific positions.

**Steps:**
1. Open Scenario Directory
2. Filter: **Department = "Sales" AND Pay Grade >= "Manager"**
3. Sort by **Salary** (high to low)
4. Review list
5. Click checkboxes for positions to close (select 20)
6. Bulk edit panel opens
7. Click **Close Positions** → **Layoff (RIF)**
8. Click **Confirm**
9. Check **Change Tracker** for total savings
10. If not enough savings, select more positions

**Result:** Budget cut achieved efficiently.

---

### Workflow 3: Export All Changes to Excel for Finance Review

**Goal:** Share detailed change log with finance team.

**Steps:**
1. Open Scenario Directory
2. Filter: **Change Type ≠ "No Change"** (show only changed positions)
3. Show columns: Change Type, Effective Date, Cost Impact, Before/After Salary
4. Sort by **Cost Impact** (highest to lowest)
5. Click **Export** → **CSV**
6. Open in Excel
7. Add pivot tables or charts as needed
8. Share with finance team

**Result:** Finance team has detailed scenario impact.

---

### Workflow 4: Verify Effective Dates Are Correct

**Goal:** Ensure all changes are scheduled for right quarter.

**Steps:**
1. Open Scenario Directory
2. Filter: **Change Type ≠ "No Change"**
3. Sort by **Effective Date**
4. Review dates column
5. Identify positions with wrong dates
6. Click each position to edit
7. Update Effective Date
8. Save changes

**Or bulk update:**
1. Select all positions with wrong date (Q1 instead of Q2)
2. Bulk edit → **Edit Attributes** → **Effective Date**
3. Set to correct date (e.g., 2026-04-01)
4. Apply

**Result:** All changes scheduled for correct timing.

---

### Workflow 5: Find All Positions Reporting to Specific Manager

**Goal:** See all direct reports in one view.

**Steps:**
1. Open Scenario Directory
2. Filter: **Manager = "Jane Smith"**
3. See all positions reporting to Jane
4. Review for span of control issues
5. Sort by **Change Type** to see which are new, closed, or modified

**Result:** Complete view of Jane's team with changes highlighted.

---

## Exporting from Scenario Directory

### Export Options

**What to export:**
- **All positions** - Full directory
- **Filtered positions** - Only visible rows
- **Selected positions** - Only checked rows
- **Change log** - Only changed positions

**Export formats:**
- **CSV** - For Excel analysis
- **Excel** - With formatting and multiple sheets
- **PDF** - For presentations

**What gets exported:**
- All visible columns
- Change indicators
- Before/After values for modifications
- Cost impact
- Effective dates

**How to export:**
1. Set up your view (columns, filters, sort)
2. Click **Export** button
3. Choose format
4. Choose what to export (all/filtered/selected)
5. Click **Export**
6. File downloads

---

## Before/After View in Directory

Some implementations support side-by-side before/after columns:

**Before columns:**
- Before Name
- Before Title
- Before Department
- Before Salary
- Before Manager

**After columns:**
- After Name
- After Title
- After Department
- After Salary
- After Manager

**Change columns:**
- Change indicator (what changed)
- Cost delta
- Change type

**When to use:** Compare old vs new values for all positions in one view.

---

## Scenario Directory vs Main Org Directory

| Feature | Main Org Directory | Scenario Directory |
|---------|-------------------|-------------------|
| View positions | ✅ All positions | ✅ All positions |
| Sort columns | ✅ Yes | ✅ Yes |
| Filter | ✅ Yes | ✅ Yes + Change Type |
| Export | ✅ CSV/Excel/PDF | ✅ CSV/Excel/PDF |
| Change highlighting | ❌ No | ✅ Color-coded rows |
| Change Type column | ❌ No | ✅ Yes |
| Effective Date column | ❌ No | ✅ Yes |
| Cost Impact column | ❌ No | ✅ Yes |
| Bulk selection | ❌ View only | ✅ Full bulk actions |
| Bulk editing | ❌ View only | ✅ Yes |
| Before/After columns | ❌ No | ✅ Yes (some implementations) |

**Key insight:** Scenario Directory is a powerful analysis and editing tool, not just a view.

---

## Best Practices

1. **Use Change Type filter** - Focus on additions, reductions, or modifications
2. **Export regularly** - Backup your scenario data
3. **Sort by Cost Impact** - Understand financial effect of changes
4. **Check Effective Dates** - Verify timing is correct
5. **Use bulk selection wisely** - Review before applying bulk actions
6. **Show scenario columns** - Change Type, Effective Date, Cost Impact
7. **Combine with org chart** - Directory for data, chart for structure

---

## Troubleshooting

**Problem:** Can't see Change Type column.
- **Solution:** Click column settings → Check "Change Type" → Apply.

**Problem:** Directory shows positions I didn't change.
- **Solution:** Filter by Change Type ≠ "No Change" to see only modifications.

**Problem:** Bulk selection not working.
- **Solution:** Ensure you're in a scenario (not Main Org). Main Org Directory is view-only.

**Problem:** Color-coding not showing.
- **Solution:** Refresh page. Or check view settings for change highlighting.

**Problem:** Export includes too many columns.
- **Solution:** Hide columns you don't need before exporting.

**Problem:** Can't edit positions in Directory.
- **Solution:** Use bulk edit panel after selecting, or click position to open edit panel.

---

## Next Steps

Now that you understand Scenario Directory:
- Practice filtering by Change Type to review your changes
- Try bulk selection + bulk editing for large-scale changes
- Export change log to share with stakeholders
- Use [Bulk Operations](bulk-operations.md) for mass edits
- Combine with [Scenario Tracking & Analysis](tracking-analysis.md) for complete picture
