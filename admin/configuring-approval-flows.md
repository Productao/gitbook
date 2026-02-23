---
description: Setting up and managing scenario approval workflows
---

# ✅ Configuring Approval Flows

Approval flows route scenarios through multi-level review before implementation. As an admin, you configure global approvers in Settings and document how scenario-specific approvers work.

## The 4-Level Approval System

**Levels 1 & 2: Global Approvers** — Set in Settings > General > Approval Workflows; apply to all scenarios org-wide.

**Levels 0 & 3: Scenario-Specific Approvers** — Set per scenario when submitting; apply to that scenario only.

**Approval order:** Level 0 (scenario-specific, first) → Level 1 (global) → Level 2 (global) → Level 3 (scenario-specific, last)

You don't have to use all levels. Most organizations use only Levels 1 and 2.

## Configuring Global Approvers (Levels 1 & 2)

1. Settings > **General** > scroll to "Approval Workflows"
2. Click "Add Level 1 Approver" > select user(s)
3. Click "Add Level 2 Approver" > select user(s)
4. Enable **"Lock Scenarios Upon Submission"** (strongly recommended — prevents edits during review)
5. Save

**With multiple Level 1 approvers:** Any one approver can approve to advance; if any rejects, the scenario is rejected.

**Typical approvers:**

* Level 1: HR Business Partners, Department heads
* Level 2: CFO, CHRO, COO — whoever has final budget authority

## Setting Scenario-Specific Approvers (Levels 0 & 3)

Done by the scenario creator at submission time, not in Settings:

1. Open scenario > **OpEx Panel** > scroll to bottom > **Configure Submission**
2. Set Level 0 (first approver, e.g., direct manager) and/or Level 3 (final approver, e.g., executive sponsor) if needed
3. Add justification explaining the scenario purpose, headcount change, and cost impact
4. Click **Submit**

## The Approval Process (Approver's View)

1. Approver receives notification (email or in-app)
2. Opens scenario > views OpEx Panel
3. Reviews each change (green = add, red = reduce, blue = modify) and cost/headcount impact
4. Approves (✅) or Rejects (❌) each change with a reason
5. Clicks **Send Decision**

> Important: Currently all-or-nothing — if any change is rejected, the entire scenario is returned to the creator.

## After Rejection

Scenario unlocks and returns to the creator with approval history intact. The creator revises and resubmits. Previously approved positions stay approved on resubmission — approvers only need to review new or changed items.

## Common Approval Designs

**Simple (2-level):** Level 1 = HR Business Partner; Level 2 = Finance Director. For small/mid organizations.

**Standard (3-level):** Level 1 = Department heads (any one can approve); Level 2 = Finance; Level 3 (scenario-specific) = Executive sponsor for major changes.

**Complex (4-level):** Level 0 = Manager of scenario creator; Level 1 = VP; Level 2 = CFO; Level 3 = Executive committee. For large enterprises with strict governance.

## Troubleshooting

| Problem                                             | Solution                                                                          |
| --------------------------------------------------- | --------------------------------------------------------------------------------- |
| Scenario stuck in approval                          | Follow up with approver directly; admin can reassign if urgent                    |
| Scenario not locking after submission               | Enable "Lock Scenarios Upon Submission" in Settings > General                     |
| Approver can't find the scenario                    | Verify approver has access to that org scope and is assigned at the correct level |
| Need partial approval (approve some, reject others) | Not currently supported; workaround: split into multiple smaller scenarios        |

## Related Articles

* [Scenario Approvals (User Guide)](../scenarios/approvals.md)
* [Admin Overview](overview.md)
* [Access Groups](../access-control/access-groups.md)
