---
description: Analyzing scenario impact using Workforce Hub
hidden: false
---

# Scenario Analysis

Agentnoon provides several ways to analyze the impact of your scenario changes beyond the [OpEx Panel](opex-panel.md).

## Before-and-After Analysis in Workforce Hub

Open Workforce Hub inside a scenario (view dropdown > Workforce Hub) to compare baseline vs. scenario state:

- **Headcount comparison:** By department, location, or any attribute
- **Cost comparison:** Total compensation before and after, broken down by dimension
- **Span of Control comparison:** Average SOC and distribution of manager team sizes
- **Layers comparison:** Number of management levels before and after
- **Custom metrics:** Diversity metrics, cost per employee, manager-to-IC ratio (if configured)

Toggle between Before only, or After only views. Apply filters to drill into specific departments or locations.

## Activity Log

The Activity Log tracks every action taken in a scenario — who made what change and when. This provides a full audit trail of scenario modifications.

## Exporting Change Data

To download a record of all changes:
1. Click the **Export Data** button in the toolbar
2. Select **Comparisons Report** to download a before/after comparison of all positions

For more export options, see [Exporting Scenario Data](exporting.md).

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Unexpected cost impact | Review modifications in the [OpEx Panel](opex-panel.md) — a salary field may have changed unintentionally |
| Headcount doesn't match expected | Check closed vs. deleted — closed positions still count as reductions |
| Before/after charts look the same | Confirm you're in a scenario (not the Main Org); verify changes were made |
