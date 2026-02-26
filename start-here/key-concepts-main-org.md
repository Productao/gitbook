---
description: Essential concepts for working with Main Org
---

# Key Concepts for Main Org

The Main Org is your current-state organization as it exists today.

***

## What is the Main Org?

**Main Org** is your **source of truth** — the current state of your organization imported from your HRIS or data files.

**Key characteristics:**

* **Read-only**: Cannot be edited directly (view only)
* **Real-time**: Reflects your current org structure (only if live data integration is set up; otherwise updated via scheduled imports)
* **Data-driven**: Updated via imports and syncs
* **Baseline**: Reference point for all scenario planning

<figure><img src="../.gitbook/assets/Screenshot 2026-02-26 at 10.06.36 AM.png" alt=""><figcaption></figcaption></figure>

***

## Main Org Views

* **Org Chart** — Visual hierarchy showing reporting relationships
* **Directory** — Table view with sortable columns for bulk analysis
* **Forecast** — Time-based projections of current organization
* **Workforce Hub** — Analytics charts for structure analysis

<figure><img src="../.gitbook/assets/Screenshot 2026-02-26 at 10.08.06 AM.png" alt=""><figcaption></figcaption></figure>

***

## Data Sync & Refresh

**Initial Import:** Load from HRIS systems (Dayforce, Workday, BambooHR, SAP SuccessFactors), CSV/Excel files, or API integrations.

**Regular Sync:** Scheduled refreshes (daily/weekly), manual refreshes, or real-time sync with HRIS.

**Important:** The Main Org updates don't automatically flow into existing scenarios. Scenarios are snapshots taken at creation time.

***

## Read-Only — Why Can't I Edit the Main Org?

The Main Org is read-only to preserve data integrity from your HRIS and ensure a consistent source of truth. All planning happens in scenarios.

**To make changes:**

1. Create a scenario based on the Main Org
2. Model your changes in the scenario
3. Submit scenario for approval
4. Implement approved changes in your HRIS
5. Changes flow back into the Main Org via data sync

***

## Main Org as Baseline for Scenarios

Every scenario starts as a copy of the Main Org at the time of creation.

* Scenarios capture a snapshot of the Main Org
* Changes in the Main Org after scenario creation don't automatically update the scenario
* "Show Before" in a scenario always references the Main Org snapshot
* "Show After" reflects proposed changes
* Use Scenario Refresh to rebase on the current Main Org if needed

***

## Related

* [Key Concepts](concepts.md) — Core Agentnoon concepts (Spans, Layers, Permissions)
* [Key Concepts for Scenarios](key-concepts-scenarios.md) — Scenario-specific concepts
* [Main Org Navigation](../main-org/navigation.md) — How to navigate the Main Org
* [Main Org Exporting](../main-org/exporting.md) — Export formats and workflows
* [Org Metrics & Insights](../main-org/metrics-insights.md) — Headcount, cost, and structure metrics
