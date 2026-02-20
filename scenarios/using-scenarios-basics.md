---
description: Core scenario actions and workflows
hidden: false
---

# Using Scenarios - Basics

Scenarios let you model org changes before implementing them. The core cycle: make changes → review impact → refine → share → approve → implement.

## Core Actions

**Positions:** Add, Edit, Move (change manager), Close (RIF), Duplicate, Delete (cleanup only — use Close for real reductions). See [Making Position Changes](making-position-changes.md).

**People:** Assign employee to position, Detach (create vacancy), Move to Bench (hold during restructuring). See [Working with People](working-with-people.md).

**Bulk:** Select multiple positions, then bulk edit attributes, bulk change manager, or bulk close. See [Bulk Operations](bulk-operations.md).

## The Change Tracker

The Change Tracker panel shows real-time impact of every change:
- **Additions (+):** new positions, cost increases, headcount increases
- **Closures (−):** RIF'd positions, cost savings, headcount reductions
- **Modifications (~):** changed attributes (title, department, salary, manager)
- **Net:** total headcount change and total cost change

Check the Change Tracker after every edit to catch unintended impacts early.

## Time-Based Planning

Set **Effective Dates** on changes to schedule when they happen in Forecast. Model phased hiring (Q1: 5 hires, Q2: 3 hires), multi-quarter reorgs, and mid-year budget changes. See [Time-Based Planning](time-based-planning.md).

## Collaboration

**Comments:** Add notes to specific positions; @mention collaborators; track conversation history inline.

**Sharing:** Share scenarios with view or edit access; export for stakeholders without Agentnoon access.

**Approvals:** Submit through approval chains; track status; get sign-off before implementing. See [Scenario Approvals](approvals.md).

## Scenario States

**Draft** → **Submitted** (in approval workflow, limited editing) → **Approved** (locked, ready to implement) → **Implemented** (historical record, read-only)

## Comparing Scenarios

Create multiple versions (Option A, Option B, Option C) and use Scenario Comparisons to evaluate cost, headcount, and structural differences side-by-side. See [Scenario Comparisons](comparisons.md).

## Common Mistakes to Avoid

- **Delete instead of Close** — Close preserves the audit trail and cost tracking for real reductions; Delete removes all record
- **Ignoring the Change Tracker** — Unintended cost impacts are easy to miss
- **No effective dates** — Forecast shows changes as immediate rather than phased
- **No alternatives** — Model 2–3 options before choosing one
- **Too broad access** — Limit Edit access; use View access for stakeholders

## Related Articles

- [Making Position Changes](making-position-changes.md)
- [Bulk Operations](bulk-operations.md)
- [Time-Based Planning](time-based-planning.md)
- [Scenario Tracking & Analysis](tracking-analysis.md)
- [Scenario Protips](protips.md)
