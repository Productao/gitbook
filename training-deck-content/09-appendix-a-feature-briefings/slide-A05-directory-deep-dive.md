# Slide A5 — Directory (Deep Dive)

## Title
Directory View

## Lead-line
Your organization as a spreadsheet — sort, filter, bulk edit, and export position data in table format.

## What Is It?
The Directory is a table/spreadsheet view of all positions and employees. It shows the same data as the org chart but in rows and columns — sortable, filterable, and exportable. In scenarios, it also supports bulk editing and color-coded change tracking.

## How to Set It Up
- Access from any module via the **view switcher** or press keyboard shortcut **2**
- Customize visible columns using the column configuration panel
- Apply filters to narrow the dataset

## How to Use It
- **Sort:** Click any column header to sort ascending/descending. Hold Shift+click for multi-column sorting.
- **Filter:** Apply attribute-based filters (Department = Engineering AND Location = US). Filters use AND logic.
- **Search:** Use Cmd/Ctrl+F to find specific records by name, title, or any attribute.
- **Customize columns:** Show/hide columns, drag to reorder, auto-fit or manually resize widths. Save custom views for recurring tasks.
- **In Scenarios:**
  - Color-coded rows: **Green** (additions), **Red** (reductions), **Blue** (modifications), **White** (unchanged)
  - Select rows with checkboxes for **bulk editing** (change department, salary, manager, etc. for all selected)
  - Use the header checkbox to select all filtered rows at once
- **Export:** CSV or Excel with visible columns and active filters only

## Common Workflows
- Find highest-paid positions: Sort Salary descending
- Export department roster: Filter by Department → customize columns → Export CSV
- Identify vacancies: Filter where Employee Name is empty
- Bulk update after a reorg: Filter to affected team → select all → bulk edit Department field

## Screenshot / Visual
Directory view showing filtered data with color-coded scenario changes, column headers, and the bulk edit panel.

## Speaker Notes
The Directory is where power users spend a lot of their time. If you're comfortable with Excel, the Directory will feel natural. The key advantage over a spreadsheet is that it's always in sync with the org chart — filter in Directory, switch to org chart, and you see the same filtered view. Bulk editing in Directory is the fastest way to make mass changes: filter down to the rows you need, select all, edit the attribute, done. Much faster than clicking cards one by one in the org chart.
