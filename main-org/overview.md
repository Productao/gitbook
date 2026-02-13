---
description: Understanding the Main Organization view
icon: sitemap
hidden: false
---

# Main Org Overview

Main Org is your view into the current state of your organization. It's a real-time, interactive org chart that syncs with your HRIS system, providing a visual representation of who reports to whom and how your organization is structured.

## What is Main Org?

**Main Org** represents your organization's **current state** - not future plans or what-if scenarios. Think of it as a living snapshot of your org structure that updates as your HRIS data changes.

Key characteristics:

- **View-only** - You cannot edit Main Org directly
- **Synced from your HRIS** - Data comes from Workday, BambooHR, or your data source
- **Real-time** - Reflects your latest org data (refresh frequency depends on your integration settings)
- **Single version** - Everyone with access sees the same current state
- **Scoped to your access** - You only see parts of the org you have permission to view

## Main Org vs Scenarios

| Main Org | Scenarios |
|----------|-----------|
| Current state | Future state / what-if |
| View-only | Fully editable |
| One version | Unlimited versions |
| Synced from HRIS | Manually created |
| Real-time data | Point-in-time snapshot |

**When to use Main Org:** When you need to explore, search, analyze, or understand your current organization.

**When to use Scenarios:** When you need to model changes, plan reorganizations, or test different structures.

## What You Can Do in Main Org

Even though Main Org is view-only, it's incredibly powerful for analysis and exploration:

### 1. Explore the Organization

- **Navigate the hierarchy** - Click to expand/collapse teams
- **Zoom and pan** - Use trackpad gestures or mouse controls
- **Switch layout** - Toggle between vertical, horizontal, or compact views
- **Adjust display levels** - Show 1, 2, or 3 levels at once

### 2. Search and Find

- **Search by name** - Find any employee or position instantly
- **Search by job title** - Locate specific roles (e.g., "VP of Engineering")
- **Navigate directly** - Search results take you straight to that position in the org chart

### 3. Filter and Focus

- **Filter by attributes** - Show only specific departments, locations, or pay grades
- **Manager filtering** - Preserve hierarchy while filtering (recommended)
- **Multiple filters** - Combine filters to narrow your view
- **Clear filters** - Reset to see the full organization

### 4. Highlight and Visualize

- **Color-code by attribute** - Highlight by department, location, work country, pay grade, etc.
- **Add legends** - See what each color represents
- **Use outlines** - Add a second highlight dimension with card outlines
- **Customize colors** - Admins can configure color schemes

### 5. Spotlight Specific Positions

- **Apply rules** - Find positions matching criteria (e.g., "Span of Control 1-2")
- **Pre-built rules** - Use common span of control or layer-based rules
- **Custom fields** - Spotlight by any attribute in your org
- **Focus attention** - Spotlighted positions appear in blue, others grayed out

### 6. Customize Card Content

- **Add/remove fields** - Control what information appears on cards
- **Reorder fields** - Drag fields to change display order
- **Use calculated fields** - Include auto-calculated metrics like SOC, layers, total org size

### 7. Export and Share

- **JPEG export** - Screenshot of current org chart view
- **PowerPoint export** - One slide per manager
- **CSV export** - Raw data for Excel analysis
- **Custom templates** - Admins can configure export column structure

### 8. Save Views (Presets)

- **Save current settings** - Store filter, highlight, and display configurations
- **Quick switching** - Instantly switch between saved views
- **Share presets** - Other users can access your saved views

### 9. Switch to Directory View

- **Table format** - See org data in rows and columns
- **Sort and filter** - Analyze data in spreadsheet format
- **Export lists** - Download filtered lists to CSV

## Main Org Data Source

Main Org data comes from your HRIS integration:

**Common integrations:**
- Workday
- BambooHR
- ADP
- Rippling
- Manual CSV upload
- SFTP file sync
- REST API

**Refresh frequency depends on your setup:**
- **Live integrations** - Daily or real-time sync
- **Manual uploads** - Updated when admin uploads new data
- **Scheduled syncs** - Weekly or monthly (configurable)

**Important:** Changes made in your HRIS will appear in Main Org after the next sync. Changes made in Agentnoon Scenarios do NOT flow back to Main Org automatically.

## Access and Permissions

Not everyone sees the entire organization in Main Org:

- **Full access** - Some users see the entire company
- **Scoped access** - Others see only specific departments or divisions
- **Manager-based scoping** - Access determined by reporting relationships
- **Department-based scoping** - Access limited to specific org units

Your access is configured by your Agentnoon admin. If you need access to additional areas, contact your admin.

## Common Workflows

### Exploring the Organization

1. Log into Agentnoon
2. Click **Main Org** (or press keyboard shortcut **1**)
3. Navigate to area of interest (search, filter, or browse)
4. Customize view (highlight, card content, layout)
5. Export or save preset for future use

### Analyzing Span of Control

1. Go to Main Org
2. Apply Spotlight → "Average Immediate SOC" → "1-2"
3. Review highlighted positions
4. Note potential compression opportunities
5. Create Scenario to model reorganization

### Preparing for Stakeholder Meeting

1. Go to Main Org
2. Filter to specific department
3. Highlight by relevant attribute (location, pay grade, etc.)
4. Export to PowerPoint
5. Present to stakeholders

## Best Practices

1. **Start here first** - Always explore Main Org before creating scenarios
2. **Use filters strategically** - Manager filtering preserves hierarchy better than standard filtering
3. **Save useful presets** - Create saved views for departments you analyze frequently
4. **Check your scope** - Know what parts of the org you have access to
5. **Understand data freshness** - Know when your data last synced from HRIS
6. **Don't forget to clear filters** - Active filters carry over to other modules

## Limitations

Main Org is view-only, so you cannot:

- Add or delete positions
- Move people between positions
- Edit attributes (salary, title, department, etc.)
- Model future changes
- See historical views (Main Org always shows current state)

**To make changes:** Create a Scenario instead. Scenarios are editable copies where you can model any organizational changes you want to explore.

## Next Steps

- Learn [how to navigate Main Org](navigation.md) in detail
- Understand the [Taskbar actions](taskbar.md) available
- Explore [Directory View](directory-view.md) for table-based analysis
- See [Org Metrics & Insights](metrics-insights.md) for calculated fields
- Create your first [Scenario](../scenarios/creating-scenarios.md) to model changes
