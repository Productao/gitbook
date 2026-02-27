---
description: Understanding the Main Organization view
icon: sitemap
---

# Main Org Overview

Main Org is your current-state organization as it exists today.

It provides a real-time, interactive view of your organizational structure and reflects the data imported from your HRIS or uploaded data source.

Main Org represents your live organizational data — not future plans or what-if scenarios.

**Key characteristics:**

* View-only — You cannot edit Main Org directly
* Synced from your data source — Data comes from your HRIS or imported files
* Single source of truth — All users with access see the same current state
* Baseline for planning — Scenarios are created from Main Org

<figure><img src="../.gitbook/assets/Screenshot 2026-02-26 at 10.06.36 AM.png" alt=""><figcaption></figcaption></figure>

***

## Main Org vs. Scenarios

| Main Org         | Scenarios              |
| ---------------- | ---------------------- |
| Current state    | Future state / what-if |
| View-only        | Fully editable         |
| One version      | Unlimited versions     |
| Synced from HRIS | Manually created       |
| Real-time data   | Point-in-time snapshot |

**When to use Main Org:** When you need to explore, search, analyze, or understand your current organization.

**When to use Scenarios:** When you need to model changes, plan reorganizations, or test different structures.

***

## Main Org as Baseline for Scenarios

Every Scenario begins as a copy of Main Org at the time it is created.

* Scenarios capture a point-in-time snapshot of Main Org.
* Changes made in Main Org after a Scenario is created do not automatically update that Scenario.
* In a Scenario, **Show Before** references the original Main Org snapshot.
* **Show After** reflects the proposed changes within the Scenario.

If Main Org has changed and you need to align your planning work, use **Scenario Refresh** to rebase the Scenario on the current Main Org.

## Main Org Views

* **Org Chart** — Visual hierarchy showing reporting relationships
* **Directory** — Table view with sortable columns for bulk analysis
* **Forecast** — Time-based projections of current organization
* **Workforce Hub** — Analytics charts for structure analysis

<figure><img src="../.gitbook/assets/Screenshot 2026-02-26 at 10.08.06 AM.png" alt=""><figcaption></figcaption></figure>

***

## What You Can Do in Main Org

Although Main Org is view-only, it supports exploration and analysis of your current organization.

#### Explore the Organization

* Navigate the hierarchy by expanding or collapsing reporting lines
* Zoom and pan across the org chart
* Switch between vertical, horizontal, or compact layouts
* Adjust display levels to show 1–3 levels at a time

#### Search and Filter

* Search by name or job title
* Filter by attributes such as department, location, or pay grade
* Use Manager Filtering to preserve reporting context
* Combine multiple filters to narrow your view

#### Highlight and Analyze

* Color-code positions by attributes such as department, location, or pay grade
* Use legends and outlines to add visual context or a second highlight dimension
* Customize color schemes (configured by administrators)
* Apply Spotlight rules to identify positions that meet specific criteria, including pre-built rules and custom attributes

#### Customize and Save Views

* Add, remove, or reorder fields displayed on position cards
* Include calculated fields such as Span of Control or Layer
* Save configured views for quick access later

#### Export and Switch Views

* Export the org chart as JPEG or PowerPoint
* Export filtered data as CSV
* Switch to Directory view for table-based analysis



***

## Common Workflows

#### Exploring the Organization

1. Open Main Org.
2. Navigate to the area of interest using search, filters, or hierarchy navigation.
3. Customize your view using highlights or card content as needed.
4. Save a view if you plan to revisit it.

#### Analyzing Span of Control

1. Open Main Org.
2. Apply Spotlight using span of control criteria.
3. Review highlighted positions.
4. Create a Scenario if structural changes are required.

#### Preparing for a Stakeholder Meeting

1. Filter to the relevant department or team.
2. Highlight by a key attribute (for example, location or pay grade).
3. Export the org chart or data for presentation.

***

## Data Source and Refresh

#### Initial Import

Data can be loaded to the Main Org from:&#x20;

* HRIS integrations (for example, Dayforce, Workday, BambooHR, ADP, Rippling, etc.)
* CSV or Excel files
* API integrations&#x20;

#### Ongoing Sync

Main Org may be refreshed through:

* Scheduled syncs (daily or weekly)
* Manual uploads
* Real-time integrations (if configured)

Refresh frequency depends on your organization’s integration setup.

**Important** — Updates to Main Org do **not** automatically flow into existing scenarios.

Each scenario captures a snapshot of Main Org at the time it is created.

To apply approved changes:

1. Model changes in a scenario.
2. Submit for approval.
3. Implement changes in your HRIS.
4. Refresh data so updates appear in Main Org.



***

## Access and Permissions

Your view of Main Org depends on your assigned Access Group.

Some users may see the entire organization, while others may only see specific departments or teams.

If you need access to additional areas, contact your administrator.



***

## Best Practices

* Start here first - Always explore Main Org before creating scenarios
* Use filters strategically - Manager filtering preserves hierarchy better than standard filtering
* Save useful presets - Create saved views for departments you analyze frequently
* Check your scope - Know what parts of the org you have access to
* Understand data freshness - Know when your data last synced from HRIS
* Don't forget to clear filters - Active filters carry over to other modules

***

## Limitations

Main Org is view-only, so you cannot:

* Add or delete positions
* Move people between positions
* Edit attributes (salary, title, department, etc.)
* Model future changes
* See historical views (Main Org always shows current state)

To make changes, create a Scenario.

***

## Next Steps

* Learn [how to navigate Main Org](navigation.md) in detail
* Understand the [Toolbar actions](taskbar.md) available
* Explore [Directory View](directory-view.md) for table-based analysis
* See [Org Metrics & Insights](metrics-insights.md) for calculated fields
* Create your first [Scenario](../scenarios/creating-scenarios.md) to model changes
