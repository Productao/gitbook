---
description: Navigating the Forecast interface and tools
icon: compass
hidden: false
---

# Forecast Navigation

Forecast provides a streamlined interface for viewing workforce projections over time. Understanding how to navigate the Forecast module will help you quickly access the insights you need for planning and reporting.

## Accessing Forecast

### From Main Org
1. Click the **"Open Org"** button from anywhere in Agentnoon
2. At the top of the screen, you'll see a dropdown showing "Directory" by default
3. Click the dropdown and select **"Forecast"**
4. You're now in Forecast mode viewing your Main Org data

### From a Scenario
1. Open any scenario
2. Look for the same dropdown at the top of the screen
3. Select **"Forecast"**
4. You'll now see the scenario's forecast (with Before/After/Changes options)

**Tip:** The Forecast module retains your configuration (aggregator, time period, etc.) when you switch between Main Org and scenarios, making it easy to compare different views.

---

## The Forecast Interface

### Top Bar Controls

The Forecast interface is designed around a single-line control panel at the top of the screen:

**Left Side:**
- **Row Aggregator dropdown** - How to group data (People, Department, Location, etc.)
- **Headcount/Cost toggle** - Switch between headcount and cost view
- **Monetary Fields** - Select which pay components to display (Salary, Bonus, Allowances)

**Center:**
- **Filter button** - Apply filters to narrow down data
- **Search button** - Find specific positions or employees

**Right Side:**
- **Time Period dropdown** - Monthly, Quarterly, or Yearly
- **Year selector** - Pick which year to view (when using Monthly or Quarterly)
- **Export button** - Export forecast data to CSV

### The Forecast Table

Below the control panel, you'll see your forecast data displayed as a pivot table:
- **Rows** - Determined by your Row Aggregator (e.g., one row per department)
- **Columns** - Time periods (months, quarters, or years) plus any additional pay components
- **Values** - Headcount or cost figures for each row/column intersection

---

## Configuring Your Forecast View

### Choosing a Row Aggregator

The row aggregator determines how your data is grouped:

**Common aggregators:**
- **People** - One row per employee (useful for individual-level analysis)
- **Department** - One row per department (best for org-wide budget planning)
- **Location** - One row per location/country (useful for geographic analysis)
- **Employee Type** - Group by Full-Time, Contractor, Part-Time, etc.
- **Pay Grade** - Group by compensation levels
- **Any custom field** - Group by business unit, cost center, or other custom attributes

**How to change:**
1. Click the leftmost dropdown in the top bar
2. Select your desired aggregator
3. The table instantly updates to show data grouped accordingly

**Example:** Selecting "Department" shows all Engineering positions aggregated into one row, all Sales positions in another row, etc.

### Switching Between Headcount and Cost

**Headcount view:**
- Shows number of positions/employees
- Useful for understanding team sizes
- Headcount doesn't divide by 12 (a 2026 position stays in 2027 unless terminated)

**Cost view:**
- Shows workforce cost (salary + configured pay components)
- Monthly view divides annual salary by 12
- Quarterly view shows cost for that quarter
- Yearly view shows full annual cost

**How to switch:**
- Click the **Headcount/Cost toggle** in the top bar
- Toggle back and forth to compare headcount vs. budget impact

### Selecting Time Periods

**Time granularity options:**
1. **Monthly** - Shows each month in the selected year
   - Best for: Detailed monthly projections, tracking when hires start
   - Note: Annual salaries are divided by 12 to show monthly cost

2. **Quarterly** - Shows Q1, Q2, Q3, Q4 of the selected year
   - Best for: Quarterly budget planning, board reporting
   - Shows cost for that entire quarter

3. **Yearly** - Shows up to 5 years in the future
   - Best for: Multi-year strategic planning, annual budgets
   - Shows full annual cost per year

**How to select:**
1. Click the **time period dropdown** (right side of top bar)
2. Choose Monthly, Quarterly, or Yearly
3. If Monthly or Quarterly, use the year selector to pick which year to view

**Example:**
- Select "Quarterly" + "2026" to see Q1-Q4 2026
- Select "Yearly" to see 2026, 2027, 2028, 2029, 2030 all at once

### Adding Monetary Fields

Beyond the base salary, you can display additional pay components as separate columns:

**Available monetary fields:**
- Salary (always available)
- Bonus
- Stock compensation
- Allowances
- Benefits (if configured)
- Any custom compensation field

**How to add:**
1. Click the **monetary fields dropdown** (next to Headcount/Cost toggle)
2. Select additional pay components
3. Each selected component appears as additional columns in the table
4. Total compensation is automatically calculated

**Example:** Selecting "Salary" + "Bonus" shows both columns, plus a "Total" column that sums them.

---

## Filtering and Searching

### Applying Filters

Filters narrow down which positions/employees are included in your forecast:

**How to filter:**
1. Click the **Filter button** (top bar)
2. Select filter categories (Department, Location, Employee Type, etc.)
3. Choose values within each category
4. Click "Apply"
5. Forecast table updates to show only filtered data

**Filter logic:**
- **AND** between different categories (e.g., Engineering AND San Francisco)
- **OR** within the same category (e.g., Engineering OR Sales shows both)

**Tip:** Filters persist across Directory, Org Chart, and Forecast views—apply once and your filter stays active across modules.

### Using Search

Search helps you find specific people or positions:

**How to search:**
1. Click the **Search button** (top bar)
2. Type employee name, position title, or employee ID
3. Results appear instantly
4. Click a result to highlight that row in the forecast table

**Use cases:**
- "Find Sarah Chen's salary projection"
- "Locate all 'Senior Engineer' positions"
- "Search for employee ID 12345"

---

## Before, After, and Changes Views (Scenarios Only)

When viewing a scenario in Forecast, you have three view options:

### Show Before
- Displays Main Org data (current state)
- **Important:** Always references Main Org, not the scenario's starting state
- Useful for: Seeing current baseline before scenario changes

### Show After
- Displays the final state of your scenario
- Reflects all changes you've made
- Useful for: Seeing the projected future state

### Show Changes
- Displays the **delta** between Before and After
- Shows additions (+), reductions (-), and net changes
- Cost and headcount deltas clearly visible
- Useful for: Understanding the impact of your scenario

**Example:**
You move 5 people from Network Ops to Operations & Logistics:
- **After view:** Shows all 5 in Operations & Logistics
- **Changes view:** Shows -5 in Network Ops, +5 in Operations & Logistics

**How to switch:**
1. Look for the **Before/After/Changes dropdown** (appears only in scenarios)
2. Select your desired view
3. Table updates immediately

---

## Exporting Forecast Data

Export your forecast projections for use in presentations, budget tools, or Excel analysis.

### Export to CSV

**How to export:**
1. Configure your forecast view (aggregator, time period, filters)
2. Click the **Export button** (right side of top bar)
3. Select **"Export to CSV"**
4. Choose file location
5. Open CSV in Excel or Google Sheets

**What's included in the export:**
- All visible rows and columns from your current view
- Respects your filters and aggregator selection
- Includes headcount or cost (depending on toggle state)
- All selected monetary fields

**Tip:** Export with "Show Changes" to create an impact report showing exactly what changed in your scenario.

---

## Keyboard Shortcuts

Speed up navigation with keyboard shortcuts:

- **`/` (forward slash)** - Focus search
- **`F` (filter)** - Open filter panel
- **`Esc`** - Close open panels
- **`Arrow keys`** - Navigate table cells
- **`Cmd/Ctrl + E`** - Export to CSV (if configured)

---

## Common Navigation Workflows

### Quarterly Department Budget Review
1. Select **Department** as row aggregator
2. Select **Quarterly** time period + current year
3. Toggle to **Cost** view
4. Add **Salary + Bonus** monetary fields
5. Review each department's quarterly cost
6. Export to CSV for budget meeting

### Tracking Hiring Plan Progress
1. Select **Department** as row aggregator
2. Select **Monthly** time period + year with planned hires
3. Toggle to **Headcount** view
4. Switch to **Show Changes** (if in a scenario)
5. See exactly which months headcount increases by department
6. Export for recruiting team

### Multi-Year Strategic Planning
1. Select **Department** as row aggregator
2. Select **Yearly** time period (shows 5 years)
3. Toggle to **Cost** view
4. Review long-term cost projections
5. Compare scenarios to evaluate different growth plans
6. Export for executive leadership

### Geographic Cost Analysis
1. Select **Location** as row aggregator
2. Select **Yearly** time period
3. Toggle to **Cost** view
4. See workforce cost by location/country
5. Apply filters to narrow to specific regions if needed
6. Export for finance team

---

## Tips for Effective Navigation

### Start with the Right Aggregator
- **Budget planning?** Use Department or Cost Center
- **Geographic analysis?** Use Location or Country
- **Compensation analysis?** Use Pay Grade or Employee Type
- **Individual review?** Use People

### Use Filters Strategically
- Apply broad filters first (e.g., select a division)
- Narrow down with additional filters (e.g., then select specific departments)
- Clear filters completely to return to full view

### Compare Time Periods
- Start with Yearly to see the big picture
- Drill into Quarterly to understand seasonal patterns
- Use Monthly for precise hire date and effective date tracking

### Leverage Before/After/Changes
- **Before** establishes your baseline
- **After** shows your planned future state
- **Changes** highlights the impact—use this for stakeholder presentations

---

## Troubleshooting Common Issues

**"My forecast shows zero headcount in future months"**
- Check if your positions have hire dates configured
- Positions without hire dates only appear in current/past periods
- In scenarios, add hire dates to show phased hiring

**"Costs don't match my calculations"**
- Verify you're viewing the correct time period (monthly divides by 12)
- Check if all relevant monetary fields are selected
- Ensure your data includes the compensation fields you expect

**"My filters aren't working"**
- Filters apply across all modules—check if a filter is already active
- Clear all filters and start fresh
- Verify the field you're filtering on has data populated

**"I can't see Before/After/Changes options"**
- This is only available in scenarios, not Main Org
- In Main Org, you only see current state (equivalent to "Before")

**"Export isn't including all data"**
- Export respects active filters—check if filters are hiding data
- Verify you're viewing the time period you want to export
- Try expanding time period (e.g., Yearly to see all years at once)

---

## Next Steps

- **[Forecast Overview](overview.md)** - Understand the Forecast module's purpose and concepts
- **[Building Headcount Forecasts](building-headcount-forecasts.md)** - Create workforce projections
- **[Budget Planning & Tracking](budget-planning-tracking.md)** - Align forecasts with budgets
- **[Forecast vs Scenarios](forecast-vs-scenarios.md)** - Understand when to use each module
- **[Forecast Reports & Exports](reports-exports.md)** - Advanced reporting and export options
