---
description: Essential concepts for working with Main Org
hidden: false
---

# Key Concepts for Main Org

The Main Org is your current-state organization as it exists today. Understanding these concepts will help you navigate, analyze, and export your current organizational data.

---

## What is Main Org?

**Main Org** is your **source of truth** - the current state of your organization imported from your HRIS or data files.

**Key characteristics:**
- **Read-only**: Cannot be edited directly (view only)
- **Real-time**: Reflects your current org structure
- **Data-driven**: Updated via imports and syncs
- **Baseline**: Reference point for all scenario planning

**Use Main Org to:**
- Understand current organizational structure
- Analyze existing metrics (span of control, headcount, cost)
- Export current state data
- Serve as baseline for scenarios

> **[Screenshot placeholder: Main Org view showing read-only current state with organization structure]**

---

## Main Org Views

Main Org can be viewed in multiple ways depending on what you need to analyze:

### Org Chart View
Visual, hierarchical tree showing reporting relationships.

**Best for:**
- Understanding reporting structure
- Visualizing management chains
- Presenting to stakeholders
- Seeing the "big picture"

### Directory View
Table/spreadsheet view of all positions with sortable columns.

**Best for:**
- Analyzing data in bulk
- Filtering and searching
- Exporting data
- Reviewing specific attributes

### Forecast View
Time-based projections of your current organization.

**Best for:**
- Extending current state into future periods
- Baseline budget projections
- Multi-year headcount planning

### Workforce Hub View
Analytics and visualizations for org structure analysis.

**Best for:**
- Span of control analysis
- Headcount distribution
- Identifying organizational imbalances

> **[Screenshot placeholder: View dropdown showing Org Chart, Directory, Forecast, and Workforce Hub options]**

---

## Data Sync & Refresh

### Initial Import
When you first set up Agentnoon, you load your current org data from:
- HRIS systems (Workday, BambooHR, SAP SuccessFactors, etc.)
- CSV/Excel files
- API integrations

### Regular Sync
Keep Main Org up-to-date with:
- **Scheduled refreshes**: Automatic updates on a cadence (daily, weekly)
- **Manual refreshes**: On-demand updates triggered by admins
- **Live integrations**: Real-time sync with HRIS

**Important:** Main Org updates don't automatically flow into existing scenarios. Scenarios are snapshots taken at creation time.

> **[Screenshot placeholder: Data refresh settings showing scheduled sync configuration]**

---

## Span of Control in Main Org

**Span of Control (SOC)** is the number of direct reports a manager has.

**Why it matters in Main Org:**
- Identify managers who are overloaded (too many direct reports)
- Find narrow spans that create unnecessary layers
- Baseline for reorganization planning

**Healthy ranges (industry standard):**
- Individual Contributors: 0 direct reports
- First-Line Managers: 5-10 direct reports
- Mid-Level Managers: 5-8 direct reports
- Executives: 5-10 direct reports

**How Agentnoon displays SOC:**
- Color-coded managers in org chart
- SOC metrics in Workforce Hub
- Flags for unhealthy spans

> **[Screenshot placeholder: Org chart with span of control color coding showing healthy and unhealthy spans]**

---

## Layers & Organizational Depth

**Layers** are the number of management levels between an employee and the CEO.

**Example:**
- CEO: Layer 0
- VP reporting to CEO: Layer 1
- Director reporting to VP: Layer 2
- Manager reporting to Director: Layer 3
- Individual Contributor: Layer 4

**Why it matters:**
- More layers = slower decision-making, less agility
- Fewer layers = flatter organization, faster communication
- Industry best practice: 4-7 layers for most companies

**Use Main Org to:**
- Understand current organizational depth
- Identify opportunities to flatten structure
- Baseline layers before reorganization

> **[Screenshot placeholder: Workforce Hub Layers & Spans chart showing distribution of employees across organizational layers]**

---

## Exporting Main Org Data

Export your current organizational data for analysis, reporting, or presentations.

**What you can export:**
- Full org structure (all positions and attributes)
- Filtered subsets (specific departments, locations)
- Workforce Hub charts and analytics
- Directory table views

**Export formats:**
- CSV/Excel for data analysis
- PDF for presentations
- Images for reports

**Common use cases:**
- Share current headcount with finance
- Analyze salary distribution in Excel
- Create org charts for presentations
- Backup organizational data

**Learn more:** [Main Org Exporting](../main-org/exporting.md)

---

## Org Metrics & Insights

Main Org provides built-in metrics and insights about your organization:

### Headcount Metrics
- Total headcount
- Headcount by department, location, job level
- Open positions vs filled positions
- Employee type distribution (FTE, contractor, etc.)

### Cost Metrics
- Total compensation cost
- Cost by department, location
- Average salary by level or department
- Salary range distributions

### Structure Metrics
- Span of control distribution
- Number of organizational layers
- Manager vs IC ratio
- Departmental size distribution

> **[Screenshot placeholder: Workforce Hub dashboard showing key metrics like total headcount, cost, average span, and layers]**

---

## Filtering & Searching Main Org

Find specific positions or segments of your organization:

**Filtering options:**
- Department, Location, Job Title
- Salary range, Employee type
- Manager, Layer, Span of control
- Custom attributes (Cost Center, Business Unit, etc.)

**Search capabilities:**
- Search by employee name
- Search by position title
- Search by manager name
- Combined filters for advanced queries

**Use filtering to:**
- Analyze specific segments (e.g., "Engineering department in San Francisco")
- Prepare targeted exports
- Understand subset headcount and cost

---

## Read-Only Nature of Main Org

**Important:** Main Org is read-only. You cannot make direct edits.

**Why is Main Org read-only?**
- Preserves data integrity from HRIS
- Prevents accidental changes to current reality
- Ensures consistent source of truth
- All planning happens in scenarios

**To make changes:**
1. Create a scenario based on Main Org
2. Model your changes in the scenario
3. Submit scenario for approval
4. Implement approved changes in your HRIS
5. Changes flow back into Main Org via data sync

This workflow ensures that Main Org always reflects reality, while scenarios are used for planning.

---

## Main Org as Baseline for Scenarios

Every scenario starts as a copy of Main Org at the time of creation.

**What this means:**
- Scenarios capture a snapshot of Main Org
- Changes in Main Org after scenario creation don't automatically update the scenario
- "Show Before" in a scenario always references the Main Org snapshot
- "Show After" reflects proposed changes

**Example:**
1. Main Org has 500 employees on Jan 1
2. You create "Q1 Hiring Plan" scenario on Jan 1 (baseline: 500)
3. Main Org grows to 520 employees by Feb 1 (new hires)
4. Your scenario's "Before" state still shows 500 (snapshot from Jan 1)
5. Use Scenario Refresh feature to rebase on current Main Org if needed

---

## Permissions in Main Org

Access to Main Org is controlled by access groups and permission levels:

### Access Groups
Define **what data** users can see.

**Examples:**
- "Engineering Leadership" sees only Engineering org
- "Finance Team" sees all departments
- "HRBP North America" sees only US/Canada positions

### Permission Levels in Main Org
- **Viewer:** Can see Main Org data within their access group
- **Planner:** Can see Main Org + create scenarios
- **Approver:** Can see Main Org + approve scenarios
- **Admin:** Full access to all Main Org data

**Learn more:** [Access Control](../admin/access-control/overview.md)

---

## Next Steps

Now that you understand Main Org concepts:

- **Explore your Main Org:** Navigate the org chart and directory
- **Analyze structure:** Use Workforce Hub to understand span of control
- **Export data:** Pull current state data for analysis
- **Create a scenario:** Start planning changes based on Main Org

**Related concepts:**
- [Key Concepts](concepts.md) - Core Agentnoon concepts
- [Key Concepts for Scenarios](key-concepts-scenarios.md) - Scenario-specific concepts
- [Main Org Navigation](../main-org/navigation.md) - How to navigate Main Org
