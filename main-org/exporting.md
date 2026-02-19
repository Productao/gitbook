---
description: Exporting data and visuals from Main Org
icon: download
---

# Main Org Exporting

Export your current organizational data and visuals for analysis, reporting, presentations, and integration with other systems. Agentnoon provides multiple export formats optimized for different use cases.

---

## Export Options Overview

Agentnoon offers several types of exports from Main Org:

**Visual Exports:**
- Org Chart as JPEG (screenshot)
- Org Chart as PowerPoint (hierarchical slides)

**Data Exports:**
- CSV (raw org data)
- Excel (formatted data)
- EIB File (for Workday integration)
- Custom Template Exports (admin-configured)

> **[Screenshot placeholder: Export menu showing all available export options]**

---

## Org Chart Visual Exports

### JPEG Export

Export a screenshot image of your org chart for presentations and documentation.

**How to export:**
1. Navigate to Main Org in Org Chart view
2. Zoom and pan to frame the area you want to export
3. Click "Export" button
4. Select "JPEG" format
5. Download image file

**Best for:**
- Quick screenshots for emails or Slack
- Informal documentation
- Capturing specific org segments

**Tips:**
- Frame your view before exporting (what you see is what you get)
- Use zoom controls to fit more or less detail
- Expand/collapse managers to control depth

> **[Screenshot placeholder: Org chart with Export button highlighted and JPEG option selected]**

### PowerPoint Export

Export your org chart as a structured PowerPoint presentation with customizable layout and content.

**How to export:**
1. Navigate to Main Org in Org Chart view
2. Click "Export" button
3. Select "PowerPoint" format
4. Configure export options (see below)
5. Click "Download"
6. Open PowerPoint file

**Configuration Options:**

#### Filters
Apply filters to export only specific segments:
- Export only Engineering department
- Export only specific locations
- Export specific business units

#### Hierarchy Depth
Select how many organizational layers to include:
- Full org (all layers)
- Top 3 layers only
- Top 5 layers only
- Custom depth selection

#### Layout Style
Choose how the org chart appears on slides:
- **Vertical**: Traditional top-down layout
- **Horizontal**: Left-to-right layout
- **Compact**: Dense layout fitting more on each slide

#### Slide Depth
Control how many layers appear per slide:
- 1-2 layers per slide (fewer, clearer slides)
- 3-4 layers per slide (balanced)
- 5+ layers per slide (more detail, denser)

**Prevents overcrowding** and ensures clear visuals for managers with large teams.

#### Card Content
Select level of detail for each position card:
- **Titles only**: Show just job titles
- **Full card content**: Include department, level, compensation, and other attributes

> **[Screenshot placeholder: PowerPoint export configuration dialog showing layout, depth, and content options]**

**Best for:**
- Board presentations
- Executive reviews
- Formal organizational documentation
- Stakeholder communication

**PowerPoint export features:**
- **One slide per manager**: Each manager with direct reports gets their own slide
- **Consistent formatting**: Professional appearance
- **Editable**: Customize in PowerPoint after export
- **Navigation**: Slide numbers and titles for easy reference

---

## Data Exports

### CSV Export

Export raw organizational data as comma-separated values for analysis in Excel, SQL databases, or BI tools.

**How to export:**
1. Navigate to Main Org (any view)
2. Apply filters if you want a subset (optional)
3. Click "Export" button
4. Select "CSV" format
5. Download CSV file

**What's included:**
- All position data
- All person data
- All standard attributes (name, title, department, salary, manager, etc.)
- All custom attributes configured for your organization
- One row per position

**Best for:**
- Data analysis in Excel
- Importing into BI tools (Tableau, Power BI, Looker)
- SQL database loading
- Custom reporting and analytics
- Sharing with teams who need raw data

> **[Screenshot placeholder: Export dialog with CSV option and filter options]**

**Tips:**
- Apply filters before exporting to get specific segments
- Use Directory view filters to export exactly what you need
- CSV respects your current filters and selections

### Excel Export

Export formatted organizational data as an Excel spreadsheet with headers and basic formatting.

**How to export:**
1. Navigate to Main Org (any view)
2. Apply filters if needed
3. Click "Export" button
4. Select "Excel" format
5. Download Excel file

**Differences from CSV:**
- Pre-formatted columns
- Headers with bold formatting
- Cell types set correctly (numbers as numbers, dates as dates)
- May include multiple sheets (depending on configuration)

**Best for:**
- Sharing with stakeholders who use Excel
- Quick analysis without formatting work
- Creating pivot tables and charts
- Formal reporting

### EIB File Export (Workday Integration)

Export organizational data in Workday's EIB (Enterprise Interface Builder) format for direct import into Workday.

**How to export:**
1. Navigate to Main Org
2. Click "Export" button
3. Select "EIB File" format
4. Download EIB file
5. Upload to Workday using standard EIB process

**Best for:**
- Workday administrators
- Synchronizing changes back to Workday
- Bulk updates in Workday
- Integration workflows

**Note:** EIB export is typically restricted to admins and HRIS teams.

### Template Builder Exports (Admin Feature)

Administrators can create custom export templates with specific columns, order, and formatting.

**How admins create templates:**
1. Navigate to Settings > Export Templates
2. Create new template
3. Select which attributes to include
4. Reorder columns
5. Set column headers
6. Save template with name

**How users use templates:**
1. Navigate to Main Org
2. Click "Export" button
3. Select "Template Export"
4. Choose saved template
5. Download file

**Template benefits:**
- Consistent exports across users
- Pre-configured for specific use cases (e.g., "Finance Headcount Report")
- Saves time vs manually configuring each export
- Ensures correct data for downstream systems

> **[Screenshot placeholder: Template selection dropdown showing saved export templates like "Finance Headcount Report", "HRIS Upload Format", "Executive Summary"]**

---

## Directory View Exports

When exporting from Directory view, you get additional flexibility:

### Exporting with Filters

**Workflow:**
1. Switch to Directory view
2. Apply filters (department, location, salary range, etc.)
3. Click "Export"
4. Only filtered positions are included in export

**Use cases:**
- Export only Engineering department
- Export only positions above $150K salary
- Export only open positions
- Export positions in specific locations

### Exporting with Column Customization

**Workflow:**
1. Switch to Directory view
2. Customize visible columns
3. Reorder columns by dragging
4. Click "Export"
5. Export includes only visible columns in displayed order

**Benefits:**
- Export only relevant attributes
- Control column order for downstream use
- Reduce file size for large orgs

> **[Screenshot placeholder: Directory view with filters and custom columns applied, Export button highlighted]**

---

## Forecast Exports

Export time-based projections from Forecast view:

**How to export:**
1. Navigate to Main Org
2. Switch to Forecast view
3. Configure time period (monthly, quarterly, yearly)
4. Set aggregation (department, location, etc.)
5. Choose metric (headcount or cost)
6. Click "Export"
7. Download file

**What's included:**
- Rows for each department/location/etc.
- Columns for each time period
- Headcount or cost values
- Summary totals

**Best for:**
- Budget planning
- Headcount forecasting
- Financial projections
- Trend analysis

**Learn more:** [Forecast Reports & Exports](../forecast/reports-exports.md)

---

## Workforce Hub Exports

Export analytics charts and data from Workforce Hub:

### Chart Image Exports

**How to export:**
1. Navigate to Main Org > Workforce Hub
2. Select and configure chart (Layers & Spans, Distribution, Heatmap)
3. Click "Export" on chart
4. Select "PNG" format
5. Download image

**Best for:**
- Presentations (board decks, executive reviews)
- Documentation
- Sharing insights without Agentnoon access

### Chart Data Exports

**How to export:**
1. Configure chart in Workforce Hub
2. Click "Export"
3. Select "CSV" or "Excel" format
4. Download data file

**What's included:**
- Underlying data points from chart
- Aggregated metrics
- Labels and dimensions

**Best for:**
- Further analysis in Excel or BI tools
- Creating custom visualizations
- Combining with other data sources

---

## Export Best Practices

### Choose the Right Format

**Use JPEG when:**
- You need a quick visual
- Informal communication
- Screenshots for documentation

**Use PowerPoint when:**
- Formal presentations
- Executive communication
- Need to edit after export

**Use CSV when:**
- Need raw data for analysis
- Loading into databases or BI tools
- Maximum flexibility

**Use Excel when:**
- Sharing with non-technical stakeholders
- Need formatted, ready-to-use file
- Creating pivot tables

**Use EIB when:**
- Integrating with Workday
- Bulk HRIS updates
- HRIS admin tasks

### Apply Filters Before Exporting

**Why filter first:**
- Reduce file size
- Focus on relevant data
- Protect sensitive data (don't export segments you shouldn't share)
- Faster downloads

**How to filter:**
- Use Directory view filters
- Apply before clicking Export
- Validate filtered results before exporting

### Use Template Exports for Consistency

**When to use templates:**
- Regular recurring exports (weekly headcount report)
- Standardized reporting
- Integration with downstream systems
- Team collaboration (everyone exports same format)

**Work with your admin:**
- Request templates for your common use cases
- Provide feedback on column selection and order
- Suggest new templates for team needs

### Document Export Purpose

**Keep track of:**
- Why you exported
- What filters/configuration you used
- Date of export
- Who received the export

**Create audit trail:**
- Main Org exports represent point-in-time snapshots
- Data changes over time as employees join/leave
- Document when exports were taken for accuracy

---

## Export Permissions and Access Control

Not all users can export all data:

**Viewer role:**
- Can export data within their access group
- Cannot export data outside their permissions
- May have export types restricted by admin

**Planner role:**
- Can export data within access group
- Can export their own scenarios
- Standard export formats available

**Admin role:**
- Can export all organizational data
- Can create and manage export templates
- Can configure export permissions
- Access to EIB and integration exports

**Access group restrictions apply:**
- If you can only see Engineering, you can only export Engineering
- Exports respect data access controls
- Sensitive attributes may be hidden in exports based on permissions

---

## Troubleshooting Exports

**Export button is grayed out:**
- You may not have export permissions
- Check with your admin
- Ensure you're in a view that supports exports

**Export file is empty:**
- Check if filters are too restrictive
- Validate you have data access to the segment you're trying to export
- Try removing filters and exporting again

**Export is taking a long time:**
- Large organizations may take time to export
- Try filtering to a smaller subset
- Consider exporting by department instead of full org

**Columns are missing in export:**
- Check column visibility in Directory view
- Some attributes may be hidden based on permissions
- Admins control which attributes are exportable

**Export format is wrong:**
- Ensure you selected correct format
- Try clearing browser cache and retrying
- Check if template export settings need updating

**Learn more:** [Export & Integration Issues](../troubleshooting/export-integration-issues.md)

---

## Related Articles

- [Directory Exporting & Reporting](../directory/exporting-reporting.md)
- [Forecast Reports & Exports](../forecast/reports-exports.md)
- [Main Org Navigation](navigation.md)
- [Scenario Exporting](../scenarios/exporting.md)
