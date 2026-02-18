---
description: Generating reports and exporting forecast data
hidden: false
---

# Forecast Reports & Exports

Forecast data is most valuable when shared with stakeholders. Agentnoon provides powerful export capabilities to help you generate reports for Finance, HR, leadership, and board presentations.

## Export Formats Available

Agentnoon supports three primary export formats from Forecast:

### CSV Export
- **Best for:** Excel analysis, budget tools, financial systems
- **Includes:** All visible rows and columns in your current Forecast view
- **Use when:** You need to manipulate data, create custom charts, or import into other systems

### PowerPoint Export
- **Best for:** Executive presentations, board decks, stakeholder meetings
- **Includes:** Visual snapshot of org chart view with Forecast data annotations
- **Use when:** You need presentation-ready visuals quickly

### Image Export
- **Best for:** Embedding in documents, sharing via email/Slack
- **Includes:** Static image of current Forecast table or org chart view
- **Use when:** You need a quick visual reference or screenshot

---

## Exporting to CSV

### Basic CSV Export

**Step 1: Configure Your Forecast View**
Before exporting, set up exactly what you want to export:
1. Select your row aggregator (Department, Location, Employee Type, etc.)
2. Choose time period (Monthly, Quarterly, Yearly)
3. Select year (if using Monthly or Quarterly)
4. Toggle Headcount or Cost
5. Add any additional monetary fields (Bonus, Stock, etc.)
6. Apply filters if you want to export a subset of data

**Step 2: Export**
1. Click the **Export button** (top-right corner of Forecast interface)
2. Select **"Export to CSV"**
3. Choose file save location
4. File downloads immediately

**What's included:**
- All rows visible in your current view
- All columns (time periods + monetary fields)
- Headers for each column
- Current data based on your Before/After/Changes selection (if in a scenario)

**Example CSV structure:**
```
Department, 2026, 2027, 2028, 2029, 2030
Engineering, 5000000, 5500000, 6000000, 6500000, 7000000
Sales, 3000000, 3300000, 3600000, 3900000, 4200000
Marketing, 1500000, 1650000, 1800000, 1950000, 2100000
```

### Advanced CSV Export Techniques

**Exporting scenario deltas:**
1. Open your scenario
2. Switch to Forecast view
3. Select **"Show Changes"** from the Before/After/Changes dropdown
4. Configure aggregator and time period
5. Export to CSV
6. Result: CSV shows +/- deltas for each department/location/etc.

**Use case:** Create an impact report showing how your scenario changes headcount and cost by department over time.

**Exporting multiple pay components:**
1. In Forecast, select Salary + Bonus + Stock from monetary fields
2. Export to CSV
3. Result: Separate columns for each pay component, plus total compensation

**Use case:** Finance needs to see base salary separate from variable compensation for budget planning.

**Exporting with filters for targeted reports:**
1. Apply filters (e.g., Department = Engineering, Location = San Francisco)
2. Configure Forecast view
3. Export to CSV
4. Result: CSV contains only Engineering positions in San Francisco

**Use case:** Create department-specific reports for distributed planning.

---

## Exporting to PowerPoint

PowerPoint export creates presentation-ready slides with organizational visualizations.

**How to export:**
1. Configure your Forecast view or org chart view
2. Click **Export button**
3. Select **"Export to PowerPoint"**
4. Choose file save location
5. PowerPoint file downloads with your org chart as a visual

**What's included:**
- Org chart visual with position cards
- Highlighting based on your current highlight settings
- Card content based on your configuration
- Scenario changes (if viewing a scenario in org chart view)

**Best practices:**
- Before exporting, configure card content to show only essential fields (name, title, salary)
- Use highlights to draw attention to key areas (e.g., highlight departments by color)
- Keep org chart zoomed to level 2 or 3 for readability in slides

**Note:** PowerPoint export is optimized for org chart view, not Forecast table view. For Forecast table exports, use CSV and create charts in PowerPoint manually.

---

## Exporting to Image

Image export creates a static PNG or JPEG of your current view.

**How to export:**
1. Configure your Forecast table or org chart view
2. Click **Export button**
3. Select **"Export to Image"**
4. Choose format (PNG recommended for clarity)
5. Choose file save location
6. Image downloads immediately

**Use cases:**
- Embed forecast table in a Word document or Google Doc
- Share quick snapshot via email or Slack
- Include in budget memo or planning document
- Create visual reference for discussions

**Tip:** Zoom out to show more data in the image, or zoom in to focus on specific area before exporting.

---

## Common Report Types

### Quarterly Headcount Report

**Purpose:** Show headcount growth by department over the next 4 quarters

**How to create:**
1. Row aggregator: **Department**
2. Time period: **Quarterly**
3. Year: Select current year
4. Toggle: **Headcount**
5. View: **Show After** (if in a scenario)
6. Export to CSV
7. Open in Excel, create bar chart showing Q1, Q2, Q3, Q4 by department

**Audience:** HR leadership, Recruiting team, Board of Directors

---

### Annual Budget Report

**Purpose:** Show workforce cost by department for next fiscal year

**How to create:**
1. Row aggregator: **Department**
2. Time period: **Yearly**
3. Toggle: **Cost**
4. Monetary fields: **Salary + Bonus** (or all pay components)
5. View: **Show After** (if in a scenario)
6. Export to CSV
7. Open in Excel, add column for budget targets, calculate variance

**Audience:** CFO, Finance team, Budget committee

---

### Geographic Cost Distribution Report

**Purpose:** Show workforce cost by location/country

**How to create:**
1. Row aggregator: **Location** or **Country**
2. Time period: **Yearly**
3. Toggle: **Cost**
4. View: **Show After** (if in a scenario)
5. Export to CSV
6. Open in Excel, create pie chart showing cost distribution by location

**Audience:** COO, Finance, HR leadership

---

### Scenario Impact Report

**Purpose:** Show the cost and headcount impact of a scenario compared to baseline

**How to create:**
1. Open your scenario
2. Switch to Forecast view
3. Row aggregator: **Department**
4. Time period: **Quarterly** or **Yearly**
5. Toggle: **Cost** (export once), then **Headcount** (export again)
6. View: **Show Changes** (critical!)
7. Export to CSV twice (once for cost deltas, once for headcount deltas)
8. Open in Excel, create side-by-side comparison showing +/- by department

**Audience:** Approvers, Executive team, Finance, Board

---

### Multi-Year Strategic Plan Report

**Purpose:** Show 5-year workforce cost projection by department

**How to create:**
1. Row aggregator: **Department**
2. Time period: **Yearly** (shows all 5 years)
3. Toggle: **Cost**
4. View: **Show After** (if in a scenario)
5. Export to CSV
6. Open in Excel, create line chart showing cost trajectory over 5 years

**Audience:** CEO, Strategic planning team, Board of Directors

---

### Hiring Plan Report

**Purpose:** Show when new positions start by department and month

**How to create:**
1. Open scenario with new positions (with hire dates)
2. Switch to Forecast view
3. Row aggregator: **Department**
4. Time period: **Monthly**
5. Toggle: **Headcount**
6. View: **Show Changes** (to highlight new hires)
7. Export to CSV
8. Open in Excel, filter to show only positive (+) headcount changes
9. Create timeline showing when each department hires by month

**Audience:** Recruiting team, HR, Department leaders

---

## Working with Exported CSV Data

### Excel Best Practices

Once you export to CSV, here's how to make the most of it in Excel:

**1. Create Pivot Tables**
- Import CSV into Excel
- Select all data → Insert → Pivot Table
- Drag departments to Rows, time periods to Columns, costs to Values
- Create custom aggregations and summaries

**2. Build Charts**
- Highlight data range
- Insert → Chart (Bar, Line, Pie, etc.)
- Customize colors to match your company branding
- Add data labels for clarity

**3. Add Budget Comparisons**
- Import forecast CSV
- Add a "Budget Target" column manually
- Create a "Variance" column: `=Forecast - Budget`
- Conditional formatting to highlight over/under budget

**4. Combine Multiple Scenarios**
- Export Scenario A forecast to CSV
- Export Scenario B forecast to CSV
- Export Scenario C forecast to CSV
- In Excel, place all three side-by-side
- Create comparison charts to evaluate options

---

## Best Practices for Reporting

### Report Cadence

**Monthly:**
- Headcount actuals vs. forecast by department
- New hires started vs. planned
- Attrition impact on workforce cost

**Quarterly:**
- Quarterly budget performance (forecast vs. actual spend)
- Headcount growth by department and location
- Scenario impact analysis for upcoming changes

**Annually:**
- Annual workforce budget for next fiscal year
- Multi-year strategic workforce plan
- Geographic cost distribution trends

**Ad-hoc:**
- Scenario comparison for reorgs or RIFs
- Board presentations on workforce strategy
- Budget cut impact analysis

---

### Naming Conventions

Use clear, descriptive file names for exported reports:

**Format:**
```
[Date]-[Scenario/Main Org]-[Report Type]-[Aggregator]-[Time Period].csv
```

**Examples:**
- `2026-02-18-Main-Org-Headcount-by-Department-Quarterly.csv`
- `2026-02-18-2026-Hiring-Plan-Cost-by-Location-Monthly.csv`
- `2026-02-18-Budget-Reduction-Scenario-Changes-by-Department-Yearly.csv`

**Why this matters:**
- Easy to find reports later
- Clear context for recipients
- Versions tracked by date

---

### Sharing with Stakeholders

**Internal stakeholders (Finance, HR, Ops):**
- Share CSV exports via email or shared drives
- Provide context: What's the scenario? What's the time period? What action is needed?
- Include a summary email explaining key takeaways

**Executive stakeholders (CEO, CFO, Board):**
- Convert CSV data into polished PowerPoint or Google Slides
- Focus on high-level insights (total cost, headcount growth, scenario impacts)
- Use charts and visuals, not raw data tables
- Provide recommendations based on forecast data

**External stakeholders (Investors, Auditors):**
- Ensure data is anonymized if needed (remove employee names, use generic titles)
- Export at appropriate aggregation level (department-level, not individual)
- Provide footnotes explaining assumptions (e.g., "assumes 3% attrition rate")

---

## Report Automation (Future Enhancement)

While Agentnoon doesn't currently support scheduled report generation, you can set up manual processes:

**Weekly/Monthly report process:**
1. Set a recurring calendar reminder
2. Open Agentnoon and navigate to Forecast
3. Use saved views to quickly configure your report layout
4. Export to CSV
5. Run your Excel template to generate charts
6. Email stakeholders with updated report

**Coming soon:**
- Scheduled exports (automatically email CSV every Monday at 9am)
- Custom report templates (save common report configurations)
- Dashboard widgets (embed forecast data in external dashboards via API)

---

## Troubleshooting Export Issues

**"CSV export is empty"**
- Check if filters are hiding all data
- Verify you're viewing the correct scenario or Main Org
- Ensure your time period includes data (future years may be empty without hire dates)

**"Export includes too much data"**
- Apply filters before exporting to narrow down data
- Use aggregators (Department, Location) instead of People for summary reports
- Export one year at a time instead of all 5 years if data is overwhelming

**"Excel can't open my CSV"**
- Verify file downloaded completely (check file size)
- Try opening in Google Sheets first, then save as Excel format
- Check if special characters in data are causing issues

**"PowerPoint export looks blurry"**
- Zoom org chart to appropriate level before exporting (level 2 or 3 recommended)
- Reduce card content to essential fields only for cleaner visuals
- Use Image export at higher resolution, then insert into PowerPoint manually

---

## Next Steps

- **[Forecast Overview](overview.md)** - Understand Forecast module fundamentals
- **[Forecast Navigation](navigation.md)** - Master Forecast interface and controls
- **[Building Headcount Forecasts](building-headcount-forecasts.md)** - Create workforce projections
- **[Budget Planning & Tracking](budget-planning-tracking.md)** - Align forecasts with budgets
- **[Multi-Year Planning](multi-year-planning.md)** - Long-term strategic workforce planning
