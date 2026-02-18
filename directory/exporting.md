---
description: Exporting data from Directory to CSV
hidden: false
---

# Exporting from Directory

Export Directory data to CSV for offline analysis, reporting, and integration with other tools like Excel, Google Sheets, or BI platforms.

## CSV Export

**What is included:**
- All visible columns in current view
- Only filtered/visible rows (not hidden rows)
- Current sort order preserved
- Data formatted for spreadsheet applications

**What is NOT included:**
- Hidden columns
- Filtered-out rows
- Visual formatting (colors, symbols)
- Images or org chart graphics

---

## How to Export

### Basic Export

**Steps:**
1. Configure Directory view (columns, filters, sort)
2. Click **Export** button (usually in toolbar or menu)
3. Select **CSV** or **Excel** format
4. Choose file location
5. Click **Download** or **Export**
6. File downloads to your computer

**File naming:**
- Default: `Agentnoon_Directory_Export_[Date].csv`
- You may be able to customize filename

---

### Export Filtered Data

**Scenario:** Export only Engineering department roster

**Steps:**
1. Filter to Department = Engineering
2. Customize columns: Name, Title, Email, Manager, Location
3. Sort by Name (A→Z)
4. Click **Export**
5. Select **CSV**
6. Only Engineering positions exported (other departments excluded)

**Result:** CSV with only filtered Engineering positions

---

### Export Custom Column Sets

**Scenario:** Create contact list export

**Steps:**
1. Show only relevant columns: Name, Email, Phone, Manager, Department
2. Hide all other columns
3. Sort by Department, then by Name
4. Click **Export**
5. Only visible columns included in CSV

**Result:** Contact list with just the needed fields

---

## Export Templates

Some Agentnoon instances support export templates (admin-configured).

### Using Templates

**What are templates:**
- Pre-configured column sets
- Standardized export formats
- Consistent structure for recurring reports

**How to use:**
1. Click **Export**
2. Select **Template** option (if available)
3. Choose from template list (e.g., "Compensation Report", "Headcount Roster")
4. Export applies template column configuration automatically

**Benefits:**
- Consistency across exports
- No need to reconfigure columns each time
- Matches company reporting standards

---

## Export Use Cases

### Export Department Roster

**Purpose:** Share current department headcount with stakeholders

**Steps:**
1. Filter to Department = Sales
2. Show columns: Name, Title, Email, Manager, Location, Start Date
3. Sort by Name (A→Z)
4. Export to CSV
5. Share with department head

---

### Export Compensation Data for Analysis

**Purpose:** Analyze pay equity in Excel

**Steps:**
1. Filter to specific department or location (if needed)
2. Show columns: Name, Title, Department, Pay Grade, Salary, Location
3. Sort by Salary (high→low)
4. Export to CSV
5. Analyze in Excel (pivot tables, charts, etc.)

---

### Export Vacant Positions for Recruitment

**Purpose:** Send open position list to recruiting team

**Steps:**
1. Filter to Employee Name = (empty)
2. Show columns: Position Title, Department, Manager, Pay Grade, Location
3. Sort by Department
4. Export to CSV
5. Share with HR/recruiting

---

### Export Change Log from Scenario

**Purpose:** Document what changed in scenario for finance review

**Steps:**
1. Open scenario in Directory view
2. Apply no filters (export all changes)
3. Show columns: Name, Title, Change Type, Old Value, New Value, Department
4. Sort by Change Type
5. Export to CSV
6. Attach to scenario approval request

---

### Export Filtered List for Further Analysis

**Purpose:** Analyze span of control in Excel

**Steps:**
1. Filter to Layer = 3-5 (middle management)
2. Show columns: Name, Title, Department, Layer, Direct SOC, Total Org Size
3. Sort by Direct SOC (high→low)
4. Export to CSV
5. Create charts in Excel

---

## Working with Exported CSV Files

### Opening in Excel

**Steps:**
1. Open Excel
2. File → Open → select CSV file
3. Data imports automatically
4. Adjust column widths as needed

**Tips:**
- Format numbers (salary) as currency
- Apply filters for additional slicing
- Create pivot tables for summary views
- Build charts for visualization

---

### Opening in Google Sheets

**Steps:**
1. Go to Google Sheets
2. File → Import → Upload tab
3. Select CSV file
4. Choose import settings
5. Click "Import data"

**Tips:**
- Share sheet with collaborators
- Create filtered views
- Use formulas for additional calculations

---

## Export Best Practices

1. **Filter before exporting** - Don't export everything; narrow to what you need
2. **Customize columns** - Only export relevant attributes
3. **Sort for readability** - Organize data logically before export
4. **Name files descriptively** - Include date, department, or purpose in filename
5. **Check filters before exporting** - Ensure you're exporting intended subset
6. **Use export templates** - For recurring reports, use templates for consistency
7. **Document export criteria** - Note which filters/columns used for reproducibility

---

## Limitations

**Data freshness:**
- Export reflects data at time of export
- Not a live connection
- Re-export to get latest data

**No org chart visuals:**
- CSV contains data only, not visual hierarchy
- Use org chart export (PDF, PowerPoint) for visuals

**Calculated fields:**
- Some calculated fields may export as static values
- Formulas don't transfer to Excel
- Recalculate in Excel if needed

**Formatting:**
- Colors, symbols, and visual indicators don't export
- Plain text/numbers only

---

## Exporting from Different Directory Modes

### Main Org Directory

**What you can export:**
- Current org data
- All visible columns
- Filtered subsets
- Sorted lists

**Common exports:**
- Current headcount roster
- Department contact lists
- Compensation summaries

---

### Scenario Directory

**What you can export:**
- Scenario data (with changes)
- Change logs (before/after values)
- Modified positions
- Change type indicators

**Common exports:**
- Scenario change summaries
- Impact analysis reports
- "What-if" scenario data
- Approval documentation

---

### Forecast Directory

**What you can export:**
- Forecasted headcount
- Planned positions by quarter/year
- Future state projections

**Common exports:**
- Hiring plan summaries
- Budget projections
- Multi-year headcount forecasts

---

## Combining Exports for Analysis

### Compare Main Org vs Scenario

**Steps:**
1. Export Directory from Main Org
2. Export Directory from Scenario
3. Open both CSVs in Excel
4. Use VLOOKUP or compare side-by-side
5. Highlight differences

**Use case:** Validate scenario changes against current state

---

### Merge Multiple Scenario Exports

**Steps:**
1. Export Directory from Scenario A
2. Export Directory from Scenario B
3. Export Directory from Scenario C
4. Combine in Excel for comparison table
5. Analyze differences

**Use case:** Compare multiple scenario options

---

## Troubleshooting

**Problem:** Export includes too many columns.
- **Solution:** Hide unnecessary columns before exporting. Only visible columns are included.

**Problem:** Export missing expected positions.
- **Solution:** Check active filters. Clear filters to export all positions, or adjust filters to include desired subset.

**Problem:** Export file won't open in Excel.
- **Solution:** Ensure file format is CSV. Try opening Excel first, then use File → Open to import CSV.

**Problem:** Salary values formatted incorrectly in Excel.
- **Solution:** Select salary column, right-click, Format Cells → Currency. Excel may import as text.

**Problem:** Export doesn't reflect latest changes.
- **Solution:** Refresh Directory view, then re-export. Ensure scenario was saved before exporting.

---

## Next Steps

- Learn about [Filtering & Sorting](filtering-sorting.md) to narrow export targets
- Explore [Column Customization](columns-customization.md) to configure export fields
- Try [Scenario Tracking & Analysis](../scenarios/tracking-analysis.md) to export change logs
- Review [Exporting & Reporting](exporting-reporting.md) for comprehensive export options

## Visual Guide

> **[Screenshot placeholder: Export button in Directory toolbar]**

> **[Screenshot placeholder: CSV export with filtered data in Excel]**

> **[Screenshot placeholder: Export template selection menu]**
