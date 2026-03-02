# Slide B5 — Configuring Approval Flows

## Title
Configuring Approval Flows

## Lead-line
Set up multi-level review and approval workflows to ensure scenarios go through the right checkpoints.

## What Is It?
Approval Flows define who reviews and approves scenarios before they can be implemented. Agentnoon supports a 4-level approval system with both global (org-wide) and scenario-specific approver assignments.

## How to Set It Up
**Global approvers (admin configured):**
1. Go to **Settings** → **General** → **Approval Workflows**
2. Assign **Level 1 approvers** — The first tier of reviewers (e.g., HRBPs, Department Heads). These apply to ALL scenarios in the organization.
3. Assign **Level 2 approvers** — The second tier of decision-makers (e.g., CFO, COO, CHRO). These also apply to ALL scenarios.

**Scenario-specific approvers (scenario creator sets these):**
- **Level 0** (optional) — Pre-check before global approvers (e.g., direct manager or team lead)
- **Level 3** (optional) — Final sign-off after global approvers (e.g., executive sponsor or board member)

## The 4-Level Flow
```
Level 0 (optional, per scenario) → Level 1 (global) → Level 2 (global) → Level 3 (optional, per scenario)
[Pre-check]                        [Checkers]          [Decision-makers]    [Final sign-off]
```

## Common Designs
- **Simple (2-level):** Level 1 (HRBP) → Level 2 (VP/CFO)
- **Standard (3-level):** Level 0 (Manager) → Level 1 (HRBP) → Level 2 (CFO)
- **Complex (4-level):** Level 0 (Manager) → Level 1 (HRBP) → Level 2 (CFO) → Level 3 (CEO)

## What Approvers Do
- Receive email notification when a scenario is submitted
- Review the scenario: org chart, OpEx Panel, Forecast, all changes
- **Approve** — advances the scenario to the next level (or locks it if final)
- **Reject** — returns the scenario with feedback; the scenario unlocks for revision

## Screenshot / Visual
The Approval Workflow configuration in Settings showing Level 1 and Level 2 global approver assignments, plus a flow diagram of the 4-level system.

## Speaker Notes
Start simple and add complexity only if needed. Most organizations do well with a 2-level flow: HRBP reviews for accuracy, then a senior leader approves for budget alignment. Only add Level 0 and Level 3 if your governance requires additional checkpoints. When a scenario is rejected, all the comments and rejection reasons are preserved, so the planner knows exactly what to fix. One important detail: approvers at each level must sign off before it advances — if Level 1 has 3 approvers, all 3 need to approve.
