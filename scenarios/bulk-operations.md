---
description: Editing multiple positions at once
hidden: false
---

# Bulk Operations

When you need to make the same change to many positions at once, bulk operations are your best friend. Instead of editing positions one-by-one, you can select multiple positions and update them all simultaneously.

## When to Use Bulk Operations

**Bulk operations are ideal for:**

- **Department reorganizations** - Move 20 positions to a new manager
- **Mass attribute updates** - Change department for an entire team
- **Budget cuts** - Close multiple positions in one action
- **Standardization** - Update job titles across similar roles
- **Location changes** - Move entire teams to new office
- **Scaling teams** - Add many similar positions quickly

**When NOT to use bulk operations:**

- Making unique changes to each position (edit individually instead)
- Complex restructuring requiring careful consideration of each role
- When you need to review each change individually

---

## Three Ways to Select Multiple Positions

### Method 1: Org Chart Selection (Best for Visual Work)

**Single selection:**
1. Click on a position card
2. Position highlights
3. Details panel opens

**Multi-selection:**
1. Hold **Cmd (Mac)** or **Ctrl (Windows)**
2. Click multiple position cards
3. All selected cards highlight
4. Bulk edit panel opens automatically

**Keyboard shortcut:**
- Press **X** key while hovering over cards to select
- **Cmd/Ctrl + K** for quick search and selection

**When to use:** When you can see all the positions on screen and want to cherry-pick specific ones.

---

### Method 2: Select Team (Best for Hierarchies)

**How to do it:**
1. Hover over the **manager's position** card
2. Click **⋮** (three dots) menu
3. Select **Select Team**
4. Manager + all direct reports are selected automatically
5. Bulk edit panel opens

**What gets selected:**
- The manager position
- All direct reports (one level down)
- Does NOT include indirect reports (grandchildren)

**When to use:** When you want to act on an entire team reporting to one manager.

**Pro tip:** For multi-level teams, select the top manager, then hold Cmd/Ctrl and add deeper positions manually.

---

### Method 3: Directory Selection (Best for Large-Scale)

**How to do it:**
1. Open **Directory** view (click Directory in taskbar)
2. Apply **filters** to narrow down positions
   - Filter by Department, Location, Job Title, etc.
   - Example: Department = "Engineering" AND Location = "San Francisco"
3. Review filtered results
4. Click **checkbox at the top** of the list
5. All filtered positions selected
6. Bulk edit panel opens

**What you can filter by:**
- Department
- Location (City, Country)
- Job Title
- Pay Grade
- Manager
- Employment Status
- Any custom fields

**When to use:** When you need to select many positions across different parts of the org, or when visual selection would be tedious (e.g., "all 50 positions in the Marketing department").

**Pro tip:** Always review the filtered list before bulk selecting to ensure you're selecting exactly what you intend.

---

## The Bulk Edit Panel

Once you've selected multiple positions (using any method above), the **Bulk Edit Panel** opens automatically on the right side.

**What you see:**
- Count of selected positions (e.g., "15 positions selected")
- List of all selected positions
- Available bulk actions
- Apply/Cancel buttons

**General workflow:**
1. Select positions (using one of the three methods)
2. Panel opens automatically
3. Choose your bulk action
4. Make changes
5. Click **Apply**
6. Changes apply to all selected positions instantly

---

## Bulk Edit Actions

### 1. Edit Attributes

**What it does:** Change field values for all selected positions at once.

**How to do it:**
1. Select multiple positions
2. In bulk edit panel, click **Edit Attributes**
3. Choose which field to update (Department, Location, Job Title, Pay Grade, etc.)
4. Enter new value
5. Click **Apply**

**What you can edit:**
- Department
- Location (Work City, Work Country)
- Job Function
- Pay Grade
- Job Family
- Any custom fields configured by your admin

**What you typically CANNOT bulk edit:**
- Employee name (use Assign/Detach instead)
- Salary (usually requires individual consideration)
- Manager (use Change Manager instead)

**Example use cases:**
- Update department for all positions from "Marketing" to "Growth"
- Change location for entire team from "New York" to "Remote"
- Standardize job titles across similar roles

**Pro tip:** Use filters in Directory to select positions, then bulk edit to ensure consistency across your org.

---

### 2. Change Manager

**What it does:** Reassigns multiple positions to report to a different manager.

**How to do it:**
1. Select multiple positions
2. In bulk edit panel, click **Change Manager**
3. Search for or select the new manager
4. Click **Apply**
5. All selected positions move to report to new manager

**What happens:**
- Reporting relationships update in org chart
- Positions move visually under new manager
- Team structure reorganizes
- Change Tracker logs the moves (neutral cost)

**Example use cases:**
- Consolidating two teams under one manager
- Reorganizing after a manager departure
- Redistributing direct reports to balance span of control

**Pro tip:** Use "Select Team" to quickly grab a manager's direct reports, then reassign them all to a new leader.

---

### 3. Close Positions (Bulk RIF)

**What it does:** Marks multiple positions as closed due to layoffs or exits.

**How to do it:**
1. Select multiple positions
2. In bulk edit panel, click **Close Positions**
3. Choose closure reason:
   - **Layoff (RIF)** - Position eliminated due to budget/restructuring
   - **Exit (Voluntary)** - Employee departing voluntarily
4. Click **Confirm**

**What happens:**
- All selected positions marked as closed
- Change Tracker shows cost savings
- Positions remain visible but marked (grayed out)
- Historical record preserved

**When to use:**
- Modeling budget cuts affecting many positions
- Mass downsizing scenarios
- Department closures

**Important:** Use Close (not Delete) to preserve tracking and historical record.

**Example:** Select 20 positions in a department being eliminated, bulk close as "Layoff (RIF)" to model the cost savings.

---

### 4. Detach Employees

**What it does:** Removes employees from multiple positions at once, leaving positions vacant.

**How to do it:**
1. Select multiple **filled positions** (positions with employees)
2. In bulk edit panel, click **Detach Employees**
3. Click **Confirm**

**What happens:**
- Employees removed from positions
- Positions become vacant
- Positions remain in org chart
- Employees moved to bench (available for reassignment)

**When to use:**
- Preparing for mass reassignments
- Modeling employee departures
- Restructuring with intent to backfill differently

**Example:** Detach 10 employees from current roles, then reassign them to new positions in a restructured org.

---

### 5. Move to Bench

**What it does:** Removes multiple employees from the org chart and places them on the bench.

**How to do it:**
1. Select multiple **filled positions**
2. In bulk edit panel, click **Move to Bench**
3. Click **Confirm**

**What happens:**
- Employees removed from positions
- Positions become vacant
- Employees placed on bench (not in org chart)
- Available for future assignment

**When to use:**
- Holding employees during large-scale restructuring
- Modeling transitions between roles
- Temporarily removing people while determining new structure

**Difference from Detach:**
- **Detach** - Employee removed from position, position stays, employee available for reassignment
- **Move to Bench** - Employee removed from org chart entirely, held on bench

**Learn more:** [Working with People - The Bench](working-with-people.md#the-bench)

---

### 6. Duplicate Positions

**What it does:** Creates multiple copies of selected positions.

**How to do it:**
1. Select **one position** (duplication works best with single selection)
2. Click **📋 Duplicate** button
3. Choose quantity:
   - 1x - One copy
   - 5x - Five copies
   - Custom - Enter number
4. Click **Duplicate**

**What happens:**
- Multiple identical positions created
- All have same title, salary, department, manager, etc.
- All vacant (no employees assigned)
- Appear under same manager as original

**When to use:**
- Scaling teams quickly (e.g., 10 new Software Engineers)
- Adding multiple similar roles
- Modeling uniform growth

**Pro tip:** Duplicate first, then select all copies and bulk edit to customize (e.g., change 5 "Software Engineer" positions to different specialties).

---

## Advanced Bulk Workflows

### Workflow 1: Reorganize Entire Department

**Goal:** Move 30 positions from Manager A to Manager B.

**Steps:**
1. Open **Directory** view
2. Filter: Manager = "Manager A"
3. Review list (30 positions)
4. Click **checkbox at top** to select all
5. In bulk edit panel, click **Change Manager**
6. Select "Manager B"
7. Click **Apply**
8. All 30 positions move to Manager B
9. Verify in org chart view

**Result:** Entire department reorganized in seconds.

---

### Workflow 2: Standardize Job Titles Across Team

**Goal:** Update 15 positions with inconsistent titles to standard title.

**Steps:**
1. In **org chart**, use Cmd/Ctrl + Click to select all 15 positions
2. In bulk edit panel, click **Edit Attributes**
3. Select field: **Job Title**
4. Enter new value: "Senior Software Engineer"
5. Click **Apply**
6. All 15 positions now have consistent title

**Result:** Standardized titles for cleaner org structure.

---

### Workflow 3: Model Budget Cut Across Multiple Teams

**Goal:** Close 25 positions across 3 different departments.

**Steps:**
1. Open **Directory** view
2. Filter: Department IN ("Sales", "Marketing", "Customer Success")
3. Manually deselect positions you want to keep (click checkboxes)
4. 25 positions remain selected
5. In bulk edit panel, click **Close Positions**
6. Select **Layoff (RIF)**
7. Click **Confirm**
8. Check Change Tracker for total savings

**Result:** Budget cut modeled with exact savings calculated.

---

### Workflow 4: Scale Team with Bulk Duplication and Editing

**Goal:** Add 10 new Software Engineers with slightly different attributes.

**Steps:**
1. Find existing "Software Engineer" position
2. Hover → Click **📋 Duplicate**
3. Select **10x**
4. Click **Duplicate** (creates 10 identical vacant positions)
5. Select all 10 new positions (Cmd/Ctrl + Click)
6. In bulk edit panel, **Edit Attributes**
7. Update Department, Location, or other fields as needed
8. Optionally: Edit individual positions for specialties (iOS, Android, Backend, etc.)

**Result:** 10 new positions created and customized quickly.

---

## Best Practices

1. **Filter before bulk selecting** - Use Directory filters to ensure you're selecting exactly what you intend
2. **Review selection before applying** - Check the count and list of positions in the bulk edit panel
3. **Use Change Tracker** - Verify cost/headcount impact immediately after bulk changes
4. **Save incrementally** - Make bulk changes in batches if reorganizing very large groups
5. **Comment on bulk changes** - Add a comment explaining why you made the change
6. **Test with small groups first** - Try bulk actions on 2-3 positions before applying to 50
7. **Use Directory for large-scale** - Org chart selection works well up to ~20 positions; beyond that, use Directory

---

## Common Mistakes to Avoid

❌ **Selecting the wrong positions** - Always review the list before applying changes

❌ **Bulk editing salary without consideration** - Salaries usually require individual review

❌ **Using bulk delete instead of bulk close** - Close preserves tracking for RIFs

❌ **Not checking Change Tracker after bulk actions** - Miss unintended cost impacts

❌ **Bulk changing manager without verifying new structure** - May create span of control issues

❌ **Forgetting employees when closing positions** - Detach or address employees before/after closing

---

## Keyboard Shortcuts for Bulk Operations

- **Cmd/Ctrl + Click** - Multi-select positions in org chart
- **X key** - Quick-select position while hovering (org chart)
- **Cmd/Ctrl + A** - Select all (in Directory view)
- **Cmd/Ctrl + K** - Quick search for positions to select
- **Esc** - Deselect all / close bulk edit panel

---

## Troubleshooting

**Problem:** I can't select multiple positions in org chart.
- **Solution:** Hold Cmd (Mac) or Ctrl (Windows) while clicking. Or use Directory view.

**Problem:** Bulk edit panel won't open.
- **Solution:** You may have only one position selected. Select at least 2 positions for bulk actions.

**Problem:** Some positions in my selection didn't change.
- **Solution:** Check if those positions had restrictions (e.g., can't change certain fields). Review Activity Log.

**Problem:** I bulk-edited the wrong positions.
- **Solution:** Use Undo (Cmd/Ctrl + Z) immediately, or check Activity Log to revert.

**Problem:** Directory filter selected too many positions.
- **Solution:** Refine filters, or manually deselect positions using checkboxes before applying bulk action.

**Problem:** I can't bulk edit a specific field.
- **Solution:** That field may not support bulk editing (e.g., salaries). Edit individually instead.

---

## Next Steps

Now that you understand bulk operations:
- Practice with small selections first (2-3 positions)
- Try all three selection methods to find your preferred workflow
- Use bulk operations for [Planning a Reorganization](../use-case-tutorials/planning-reorganization.md)
- Combine with [Time-Based Planning](time-based-planning.md) to schedule bulk changes
- Learn [Scenario Tracking & Analysis](tracking-analysis.md) to monitor bulk change impact



