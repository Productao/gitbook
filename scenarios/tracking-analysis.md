---
description: Monitoring scenario impact and changes
hidden: false
---

# Scenario Tracking & Analysis

Agentnoon automatically tracks every modification in a scenario and shows real-time cost and headcount impact.

## The Change Tracker

The Change Tracker (right panel, toggle with 👀 icon) shows three categories:

- **Additions (+):** New positions — title, department, salary, effective date, cost/headcount impact
- **Reductions (−):** Closed positions — closure reason, cost savings, effective date
- **Modifications (~):** Changed positions — before/after values for each field, cost impact

**Summary at bottom:** Net headcount change, net cost impact, total scenario cost, budget status (if set).

**Filtering and sorting:** Filter by change type (Additions / Reductions / Modifications); sort by cost impact, effective date, or department.

**Export:** Change Tracker > Export > CSV or PDF — includes all changes with cost/headcount detail and summary totals.

## Budget Tracking

Set a budget when creating the scenario, and the Change Tracker shows progress:
- Green = under budget
- Yellow = approaching budget
- Red = over budget

Adjust additions or reductions to stay within target before submitting for approval.

## Before-and-After Analysis in Workforce Hub

Open Workforce Hub inside a scenario (Org Chart dropdown > Workforce Hub) to compare baseline vs. scenario state:

- **Headcount comparison:** By department, location, or any attribute
- **Cost comparison:** Total compensation before and after, broken down by dimension
- **Span of Control comparison:** Average SOC and distribution of manager team sizes
- **Layers comparison:** Number of management levels before and after
- **Custom metrics:** Diversity metrics, cost per employee, manager-to-IC ratio (if configured)

Toggle between side-by-side, Before only, or After only views. Apply filters to drill into specific departments or locations.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Unexpected cost impact | Review Modifications — a salary field may have changed unintentionally |
| Headcount doesn't match expected | Check closed vs. deleted — closed positions still count as reductions |
| Can't find a specific change | Filter or sort; check whether it's a Modification vs. Addition/Reduction |
| Before/after charts look the same | Confirm you're in a scenario (not Main Org); verify changes were saved |
| Budget status not showing | Set a budget in scenario settings; edit scenario to add one |
| Can't export Change Tracker | Check permissions — export may be restricted by admin |
