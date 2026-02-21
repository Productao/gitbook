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
- **Real-time**: Reflects your current org structure (only if live data integration is set up; otherwise updated via scheduled imports)
- **Data-driven**: Updated via imports and syncs
- **Baseline**: Reference point for all scenario planning

**Use the Main Org to:**
- Understand current organizational structure
- Analyze existing metrics (span of control, headcount, cost)
- Export current state data
- Serve as baseline for scenarios

> **[Screenshot placeholder: Main Org view showing read-only current state with organization structure]**

---

## Main Org Views

- **Org Chart** — Visual hierarchy showing reporting relationships
- **Directory** — Table view with sortable columns for bulk analysis
- **Forecast** — Time-based projections of current organization
- **Workforce Hub** — Analytics charts for structure analysis

> **[Screenshot placeholder: View dropdown showing Org Chart, Directory, Forecast, and Workforce Hub options]**

---

## Data Sync & Refresh

**Initial Import:** Load from HRIS systems (Workday, BambooHR, SAP SuccessFactors), CSV/Excel files, or API integrations.

**Regular Sync:** Scheduled refreshes (daily/weekly), manual refreshes, or real-time sync with HRIS.

**Important:** The Main Org updates don't automatically flow into existing scenarios. Scenarios are snapshots taken at creation time.

---

## Span of Control

**Span of Control (SOC)** is the number of direct reports a manager has.

**Healthy ranges:** First-Line Managers: 5-10, Mid-Level: 5-8, Executives: 5-10

Agentnoon displays SOC via color-coded managers in org chart, SOC metrics in Workforce Hub, and flags for unhealthy spans.

> **[Screenshot placeholder: Org chart with span of control color coding showing healthy and unhealthy spans]**

---

## Layers

**Layers** are the number of management levels between an employee and the CEO.

**Example:** CEO (Layer 0) → VP (Layer 1) → Director (Layer 2) → Manager (Layer 3) → IC (Layer 4)

**Why it matters:** More layers = slower decisions; industry best practice: 4-7 layers

> **[Screenshot placeholder: Workforce Hub Layers & Spans chart showing distribution of employees across organizational layers]**

---

## Exporting Main Org Data

Export formats: CSV/Excel, PDF, images. Export full org structure, filtered subsets, Workforce Hub charts, or directory views.

**Learn more:** [Main Org Exporting](../main-org/exporting.md)

---

## Org Metrics

**Headcount:** Total headcount, by department/location/level, open vs filled positions, employee type distribution

**Cost:** Total compensation, cost by department/location, average salary, salary ranges

**Structure:** Span of control, layers, manager vs IC ratio, department sizes

> **[Screenshot placeholder: Workforce Hub dashboard showing key metrics like total headcount, cost, average span, and layers]**

---

## Filtering & Searching

**Filtering:** Department, Location, Job Title, Salary range, Employee type, Manager, Layer, Span of control, custom attributes

**Search:** Employee name, position title, manager name

Use filtering to analyze specific segments, prepare targeted exports, and understand subset headcount/cost.

---

## Read-Only Nature of Main Org

**Important:** The Main Org is read-only. You cannot make direct edits.

**Why is the Main Org read-only?**
- Preserves data integrity from HRIS
- Prevents accidental changes to current reality
- Ensures consistent source of truth
- All planning happens in scenarios

**To make changes:**
1. Create a scenario based on the Main Org
2. Model your changes in the scenario
3. Submit scenario for approval
4. Implement approved changes in your HRIS
5. Changes flow back into the Main Org via data sync

This workflow ensures that the Main Org always reflects reality, while scenarios are used for planning.

---

## Main Org as Baseline for Scenarios

Every scenario starts as a copy of the Main Org at the time of creation.

**What this means:**
- Scenarios capture a snapshot of the Main Org
- Changes in the Main Org after scenario creation don't automatically update the scenario
- "Show Before" in a scenario always references the Main Org snapshot
- "Show After" reflects proposed changes

**Example:**
1. The Main Org has 500 employees on Jan 1
2. You create "Q1 Hiring Plan" scenario on Jan 1 (baseline: 500)
3. The Main Org grows to 520 employees by Feb 1 (new hires)
4. Your scenario's "Before" state still shows 500 (snapshot from Jan 1)
5. Use Scenario Refresh feature to rebase on current Main Org if needed

---

## Permissions

**Access Groups** define what data users can see (e.g., "Engineering Leadership" sees only Engineering org).

**Permission Levels:**
- **Viewer:** Can see the Main Org data within their access group
- **Planner:** Can see the Main Org + create scenarios
- **Approver:** Can see the Main Org + approve scenarios
- **Admin:** Full access to all Main Org data

**Learn more:** [Access Control](../admin/access-control/overview.md)

---

## Next Steps

Now that you understand the Main Org concepts:

- **Explore your Main Org:** Navigate the org chart and directory
- **Analyze structure:** Use Workforce Hub to understand span of control
- **Export data:** Pull current state data for analysis
- **Create a scenario:** Start planning changes based on the Main Org

**Related concepts:**
- [Key Concepts](concepts.md) - Core Agentnoon concepts
- [Key Concepts for Scenarios](key-concepts-scenarios.md) - Scenario-specific concepts
- [Main Org Navigation](../main-org/navigation.md) - How to navigate Main Org
