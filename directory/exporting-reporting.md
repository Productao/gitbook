---
description: Getting data out and creating reports
hidden: false
---

# Exporting & Reporting

Agentnoon makes it easy to export organizational data for analysis, presentations, and reports. Learn how to get exactly the data you need in the format that works best for your workflow.

## Export Formats

Agentnoon supports multiple export formats depending on what you're exporting:

### CSV (Comma-Separated Values)

**Best for:**
- Excel or Google Sheets analysis
- Import into other systems
- Creating custom reports
- Data manipulation and calculations

**What gets exported:**
- All visible columns
- All rows matching current filters
- Raw data (no formatting or formulas)

**When to use:**
- Salary analysis in Excel
- Department rosters for distribution
- Position lists for recruitment
- Data for reporting tools (Tableau, Power BI, etc.)

---

### PowerPoint

**Best for:**
- Stakeholder presentations
- Executive briefings
- Leadership reviews
- Board presentations

**What gets exported:**
- One slide per manager
- Each slide shows manager + direct reports
- Org chart visualization
- Customizable templates

**When to use:**
- Presenting org structures
- Leadership team reviews
- Reorganization proposals
- Budget presentations

---

### JPEG / PNG

**Best for:**
- Email attachments
- Documents and reports
- Quick sharing
- Visual references

**What gets exported:**
- Screenshot of current org chart view
- Exactly what you see on screen
- Includes highlighting and filtering

**When to use:**
- Quick visual sharing
- Embedding in documents
- Status updates
- Email communications

---

## Exporting from Directory

Export filtered, sorted lists from Directory View.

### Basic CSV Export

**How to export from Directory:**
1. Go to Directory View
2. Apply filters to narrow data (optional)
3. Customize columns to show what you need
4. Sort data as desired
5. Click **Export** button
6. Choose **CSV**
7. Download the file

**What's included:**
- All visible columns (check column settings)
- All rows matching active filters
- Current sort order preserved

**Pro tip:** Filter and customize columns BEFORE exporting to get exactly the data you need.

---

### Custom Export Templates (Admin)

Admins can create standardized export templates:

**What admins can configure:**
- Which columns to include
- Column order
- Default column labels/headers
- Pre-applied filters or sorts

**Benefits:**
- Consistent reports across users
- One-click exports for common reports
- Standardized data formats for downstream systems

**To use a template:**
1. Click Export
2. Select template from dropdown (if configured)
3. Download

---

## Exporting from Org Chart

Export visual org charts and position data from org chart view.

### Org Chart as JPEG

**How to export:**
1. Go to Main Org or open a Scenario
2. Navigate to the view you want to capture
3. Apply filters, highlights, adjust layout
4. Click **Export** → **JPEG**
5. Download the image

**Tips for better exports:**
- Use "Fit to Screen" before exporting
- Adjust layout (vertical/horizontal/compact)
- Apply highlighting for visual clarity
- Zoom to appropriate level

---

### Org Chart as PowerPoint

**How to export:**
1. Configure your org chart view
2. Click **Export** → **PowerPoint**
3. Choose scope (full org or current view)
4. Download the .pptx file

**What you get:**
- One slide per manager in scope
- Each slide shows manager card + their direct reports
- Editable PowerPoint objects (not just images)
- Can customize colors, fonts, layout in PowerPoint

**Common use cases:**
- Executive presentations
- Department reviews
- Reorganization proposals
- Leadership offsites

---

### CSV from Org Chart

**How to export:**
1. Apply filters to show desired positions
2. Click **Export** → **CSV**
3. Download the file

**What's included:**
- All positions in current view (respects filters)
- All attributes for each position
- Reporting relationships (Manager field)

---

## Exporting from Workforce Hub

Export analytics charts and underlying data.

### Chart as PNG

**How to export:**
1. Go to Workforce Hub
2. Select a chart
3. Configure axes and filters
4. Click **Download** icon → **PNG**
5. Download the image

**Best for:**
- Including charts in reports
- Email communications
- Presentations (as backup slides)

---

### Chart as PowerPoint

**How to export:**
1. Configure chart as desired
2. Click **Download** icon → **PowerPoint**
3. Download the .pptx file

**What you get:**
- Editable chart object (not just image)
- Can modify colors, labels, formatting in PowerPoint
- Data included in chart (can view data table in PPT)

**Pro tip:** Export Hub charts as PowerPoint, not PNG, so you can customize them later.

---

### Chart Data as CSV

**How to export:**
1. Click **Show Table** to view chart data
2. Click **Download** icon → **CSV**
3. Download the file

**What's included:**
- The data behind the chart
- All visible breakdowns
- Current filter context

---

## Common Export Scenarios

### Export Department Roster

**Goal:** Create a list of everyone in Engineering with their titles, managers, and contact info.

**Steps:**
1. Go to Directory
2. Filter to Department = Engineering
3. Show columns: Name, Title, Manager, Email, Location
4. Sort by Manager, then by Name
5. Export to CSV
6. Open in Excel and distribute

---

### Export Org Chart for Executive Presentation

**Goal:** Create a PowerPoint deck showing the leadership team structure.

**Steps:**
1. Go to Main Org
2. Filter to Layer 1-3 (CEO and top leaders)
3. Apply highlighting by Department
4. Use vertical layout, expand to level 3
5. Export to PowerPoint
6. Download and customize slides in PowerPoint

---

### Export Compensation Data for Analysis

**Goal:** Analyze salary distribution by department and pay grade.

**Steps:**
1. Go to Directory
2. Show columns: Name, Department, Pay Grade, Salary, Title
3. Sort by Department, then Pay Grade, then Salary (high→low)
4. Export to CSV
5. Analyze in Excel (pivot tables, charts, etc.)

---

### Export Span of Control Analysis

**Goal:** Create a report showing managers with low span of control.

**Steps:**
1. Go to Directory
2. Filter to Direct SOC = 1-2
3. Filter to Pay Grade > 10 (senior managers only)
4. Show columns: Name, Title, Department, Direct SOC, Total Org Size, Pay Grade
5. Sort by Pay Grade (high→low)
6. Export to CSV
7. Share with leadership for review

---

### Export Vacancy Report

**Goal:** List all open positions for recruitment team.

**Steps:**
1. Go to Directory
2. Filter to Employee Name = (empty)
3. Show columns: Job Title, Department, Manager, Location, Pay Grade, Salary Range
4. Sort by Department, then Title
5. Export to CSV
6. Send to recruitment team

---

## Export Best Practices

### Before Exporting

1. **Apply filters** - Don't export everything; narrow to what you need
2. **Customize columns** - Show only relevant attributes
3. **Sort appropriately** - Organize data for your audience
4. **Check data freshness** - Ensure you're viewing latest sync
5. **Verify filters** - Confirm active filters are correct

### After Exporting

1. **Review the export** - Open file to verify it contains what you expected
2. **Document assumptions** - Note any filters or date ranges used
3. **Add context** - Include export date and source in your reports
4. **Secure sensitive data** - Follow data security policies for salary and personal info
5. **Version your exports** - Save with date in filename (e.g., "Engineering-Roster-2026-02-10.csv")

### Data Security

**Important reminders:**
- Exported files contain potentially sensitive data (salaries, personal info)
- Follow your organization's data handling policies
- Don't email unencrypted exports with compensation data
- Limit access to exported files based on need-to-know
- Delete old exports when no longer needed

---

## Export Limitations

**Main Org Directory:**
- Cannot export historical data (only current state)
- Export reflects your access scope (you only get data you can see)

**Scenarios:**
- Export shows scenario state at time of export
- Include scenario name and date in export filename

**Workforce Hub:**
- Chart exports are static (don't update automatically)
- CSV exports reflect current filter context

---

## Troubleshooting

**Problem:** Export is missing columns I expected.
- **Solution:** Check column settings. Ensure desired columns are visible before exporting.

**Problem:** Export has too much data.
- **Solution:** Apply filters before exporting to narrow the dataset.

**Problem:** Exported org chart looks different than my screen.
- **Solution:** Use "Fit to Screen" and adjust layout before exporting.

**Problem:** PowerPoint export has too many slides.
- **Solution:** Filter to a smaller scope before exporting (e.g., one department).

**Problem:** Export is missing some people.
- **Solution:** Check active filters. Clear filters and try again.

---

## Next Steps

- Learn more about [Directory Features](features.md) for filtering and sorting
- See [Directory Overview](overview.md) for when to use Directory vs Org Chart
- Try exporting from [Main Org Directory View](../main-org/directory-view.md)
- Explore [Workforce Hub charts](../hub/chart-navigation.md) for analytics exports
