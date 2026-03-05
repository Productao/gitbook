---
description: Viewing forecast projections within scenarios
icon: chart-line
---

# 📊 Scenario Forecast

Scenario Forecast shows time-phased projections of your planned changes — when they take effect, headcount and cost over time, and before/after comparisons.

## Accessing

Open any scenario > click the view dropdown > select **Forecast**.

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

## Configuration

* **Row aggregator** — Department, Location, Country, Employee Type, Manager, Job Title, or any custom field
* **Metric** — Headcount (count of positions) or Cost (monetary projection)
* **Monetary fields (cost view)** — Select which compensation components to include: Salary, Bonuses, Allowances, Stock, Benefits, custom fields
* **Time period** — Monthly (detailed hiring plans), Quarterly (most common for planning and reporting), Yearly (multi-year strategy, shows up to 5 years)

**Before / After / Changes toggle:**

* **Show Before** — Main Org baseline extended over time

<figure><img src="../.gitbook/assets/Screenshot 2026-03-05 at 1.42.58 PM.png" alt=""><figcaption></figcaption></figure>

* **Show After** — All scenario changes applied; view full proposed state

<figure><img src="../.gitbook/assets/Screenshot 2026-03-05 at 1.43.18 PM.png" alt=""><figcaption></figcaption></figure>

* **Show Changes** — Delta only (+ and −); most useful for communicating impact

<figure><img src="../.gitbook/assets/Screenshot 2026-03-05 at 1.43.41 PM.png" alt=""><figcaption></figcaption></figure>

## How Effective Dates Work in Forecast

When you change a position's department with an effective date of July 1, 2026:

* **Through Q2** — the position appears in its original department
* **From Q3 onward** — the position appears in its new department

Without an effective date, changes are treated as immediate — the position appears in the new state for all time periods.

**Example (Show After, Quarterly):**

| Department      | Q1 | Q2 | Q3 | Q4 |
| --------------- | -- | -- | -- | -- |
| Network Ops     | 25 | 25 | 20 | 20 |
| Ops & Logistics | 30 | 30 | 35 | 35 |

5 positions moved in Q3.

## Common Use Cases

**Phased hiring plan** — Add positions with hire dates across Q1–Q4 > Monthly/Quarterly > Headcount > Show Changes → see exactly when each hire hits headcount and cost.

**Phased reorg** — Assign different effective dates to different teams > Quarterly > Show Changes → see the gradual transition by department.

**Budget impact** — Make changes (promotions, hires, closures) > Cost view > Salary + Bonus > Show Changes → quarterly cost delta per department.

**Scenario comparison** — View Scenario A in Forecast (note projections) > open Scenario B > compare timing and magnitude.

## FAQ

**Why do changes appear in all periods even with an effective date?**

You may be in the org chart/directory view (shows "after" state). Switch to Forecast view to see time-phased transitions.

**Can different positions in the same scenario have different effective dates?** Yes — each position can have its own effective date

**What's the difference between Hire dates vs. effective dates?**

Use hire dates for new positions being filled; use effective dates for changes to existing positions (reorganizations, transfers, attribute changes).

## Related Articles

* [Time-Based Planning](time-based-planning.md)
* [Forecast Overview](../forecast/overview.md)
* [Forecast Navigation](../forecast/navigation.md)
