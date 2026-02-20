---
description: Best practices for naming, versioning, and organizing scenarios
hidden: false
---

# Organizing Scenarios

Keep your scenario library navigable as it grows.

## Naming Convention

Use the format: **[Purpose] - [Scope] - [Version/Date]**

Examples:
- "Engineering Reorg - Flatten Structure - v2"
- "Q2 Hiring Plan - Commercial NA - 2026-02-15"
- "Budget Cut 10% - Option A"
- "VP Engineering Succession - Candidate A"

**Purpose** (required): What the scenario does — "Hiring Plan", "Budget Cut", "Reorganization", "Succession"

**Scope** (recommended): Which team, department, or geography is affected

**Version or date** (situational): Use v1/v2/v3 for iterations, Option A/B/C for alternatives, or a date for chronological tracking

Never leave a scenario named "Untitled Scenario" or "New Scenario".

## Versioning

Create a new version when: stakeholder feedback requires significant revisions, you're testing a completely different approach, or you want to preserve the previous version for reference.

For minor corrections (typos, small salary tweaks), just update the existing scenario.

**Version naming options:**
- Numbered: "Plan v1", "Plan v2"
- Lettered options: "Plan - Option A", "Plan - Option B"
- Descriptive: "Plan - Conservative", "Plan - Aggressive"
- Date-based: "Plan - Feb 15"
- Combined: "Plan v2 - Aggressive - Feb 15"

## Archive vs. Delete

**Archive** when: the scenario served an important decision, was approved/implemented, or has historical value.

**Delete** when: it was a test or mistake with no meaningful content.

When in doubt, archive — deletion is permanent.

**Cleanup cadence:**
- Weekly (5 min): Rename any "Untitled" scenarios; delete obvious test scenarios
- Monthly (30 min): Standardize names; archive completed work; export change logs before archiving
- Quarterly (2 hrs): Archive all prior quarter's scenarios; reorganize if needed

## Comparison Sets

When evaluating multiple approaches, create a named set:

1. Create base scenario: "Reorg - Base Analysis"
2. Duplicate and name: "Reorg - Option A - Flatten", "Reorg - Option B - Add Layer", "Reorg - Option C - Hybrid"
3. Tag all with a shared label (e.g., "Q2 Reorg Comparison")
4. Use Scenario Comparisons to evaluate side-by-side

## Ownership

Assign a clear owner to each scenario — they're responsible for naming, cleanup, and archiving. For shared scenarios, designate one "scenario lead" to coordinate edits and maintain consistency.

## Related Resources

- [Tags](tags.md)
- [Basic Actions](basic-actions.md)
- [Scenario Management Overview](../management.md)
