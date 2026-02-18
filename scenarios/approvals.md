---
description: Submitting scenarios for approval
hidden: false
---

# Scenario Approvals

Scenario approvals provide a structured workflow for reviewing and authorizing organizational changes before they're implemented. This feature ensures that all scenario modifications go through appropriate stakeholders for validation, creating accountability and governance around workforce planning decisions.

## Overview of the Approval Workflow

The approval workflow in Agent Noon uses a multi-level approval system that routes scenarios through designated approvers. Once a scenario is submitted, it moves through approval levels sequentially, with each approver reviewing changes and either approving or rejecting them before the scenario proceeds to the next level.

The approval process is designed to:
- Ensure organizational changes are reviewed by appropriate stakeholders
- Provide visibility into the impact of proposed changes
- Create an audit trail of who approved what and when
- Allow for feedback and iteration on proposed organizational structures

## Understanding Approval Levels

Agent Noon supports four levels of approvers, each serving a different purpose:

### Global Approvers (Levels 1 and 2)

**Level 1 Approvers** are the first reviewers who evaluate scenarios after submission. These are typically department heads, finance partners, or workforce planning leads who review the initial feasibility and alignment of proposed changes.

**Level 2 Approvers** provide a second layer of review after Level 1 approval. These are often senior leaders or executive stakeholders who provide final authorization before changes are implemented.

Both Level 1 and Level 2 approvers are configured globally in the Settings page and apply to all scenarios across the organization. A scenario must be approved by at least one Level 1 approver before it can proceed to Level 2.

### Scenario-Specific Approvers (Levels 0 and 3)

**Level 0 Approvers** are scenario-specific reviewers who evaluate changes before they reach the global approval chain. These are typically the direct stakeholders or budget owners for the specific organizational area being modified in the scenario.

**Level 3 Approvers** are the final scenario-specific reviewers who provide a last review after Level 2 approval. These might be specialized stakeholders who need to sign off on specific types of changes.

Level 0 and Level 3 approvers are configured individually for each scenario, allowing flexibility for different approval needs based on the scope and impact of changes.

## Setting Up Approvers

### Configuring Global Approvers (Admin Only)

Administrators configure global approvers in the Settings page under the General tab:

1. Navigate to Settings from the main navigation
2. Go to the General tab
3. Locate the approval settings section
4. Add Level 1 approvers by selecting users from your organization
5. Add Level 2 approvers in the same manner
6. You can add multiple approvers to each level - only one approver from each level needs to approve for the scenario to proceed

{% hint style="info" %}
**Screenshot Placeholder:** Settings > General tab showing Level 1 and Level 2 approver configuration fields with "Add Approver" buttons
{% endhint %}

### Configuring Scenario-Specific Approvers

When working within a scenario, you can configure Level 0 and Level 3 approvers:

1. Open the scenario you want to configure
2. Open the OpEx Panel (Scenario Impacts and Changes panel)
3. Click "Configure Submission" at the bottom of the panel
4. Add Level 0 approvers who should review before global approvers
5. Add Level 3 approvers who should provide final sign-off
6. These approvers only apply to this specific scenario

{% hint style="info" %}
**Screenshot Placeholder:** OpEx Panel with "Configure Submission" button highlighted, showing approval level configuration interface
{% endhint %}

## Submitting a Scenario for Approval

Once you've completed your scenario modeling and are ready to submit for review:

1. Open the scenario you want to submit
2. Open the OpEx Panel (Scenario Impacts and Changes panel) on the right side
3. Review the summary of changes and bottom-line impact
4. Click "Configure Submission" at the bottom of the panel
5. The submission interface will show:
   - Which approvers will review the scenario
   - The bottom-line impact (cost increase/decrease, headcount changes)
   - A field for justification text
6. Provide a clear justification explaining the rationale for your changes
7. Review all details carefully - this is your final chance before submission
8. Click "Submit" to send the scenario to the approval queue

{% hint style="info" %}
**Screenshot Placeholder:** Configure Submission modal showing approver list, bottom-line impact summary, justification text field, and Submit button
{% endhint %}

After submission, the scenario status will update to show it's in the approval process, and it will display which approval level it's currently at.

## The Approval Process

### For Approvers

When a scenario is submitted, approvers receive it in their scenario queue (the list of scenarios they have access to):

1. Open the submitted scenario from your scenario list
2. Open the OpEx Panel (Scenario Impacts and Changes panel)
3. Review the summary of all changes made in the scenario
4. For each change, you have two options:
   - **Green Checkmark**: Approve this change
   - **Red X**: Reject this change
5. If rejecting any changes, you must provide a reason for the rejection
6. After reviewing all changes, provide a final comment for the scenario creator
7. Submit your review

{% hint style="info" %}
**Screenshot Placeholder:** Approver view of OpEx Panel showing list of changes with green checkmarks and red X buttons next to each change, with comment field at bottom
{% endhint %}

{% hint style="warning" %}
**Important:** Currently, a scenario cannot proceed past an approver if any changes are rejected. The entire scenario must be approved together, or it returns to the creator for revisions.
{% endhint %}

### Approval Flow Sequence

The approval flow follows this sequence:

1. **Level 0** (if configured): Scenario-specific pre-approval
2. **Level 1**: First global approval level
3. **Level 2**: Second global approval level
4. **Level 3** (if configured): Scenario-specific final approval

A scenario must receive approval at each configured level before proceeding to the next. If a scenario is rejected at any level, it returns to the scenario creator for revisions.

## Approval History and Resubmission

### Viewing Approval History

Each scenario maintains a complete approval history log accessible in the OpEx Panel:

- When the scenario was submitted
- Who reviewed it at each level
- What changes were approved or rejected
- Reasons provided for any rejections
- When the scenario was approved or sent back

This creates a full audit trail of the decision-making process around organizational changes.

{% hint style="info" %}
**Screenshot Placeholder:** Approval History section in OpEx Panel showing timeline of submission, reviews, approvals, and rejections with timestamps and reviewer names
{% endhint %}

### Resubmitting After Rejection

When a scenario is rejected and returned to you:

1. Open the scenario to see which changes were rejected and why
2. Review the rejection reasons in the approval history
3. Make necessary revisions to address the concerns
4. Resubmit the scenario using the same process

{% hint style="success" %}
**Time-Saving Feature:** When you resubmit a scenario to an approver who previously reviewed it, any changes they already approved remain pre-approved. They only need to review the new or modified changes, significantly reducing review time.
{% endhint %}

## Lock Scenarios Upon Submission

Administrators can enable a setting called "Lock scenarios upon submission" in the General settings. When enabled:

- Scenarios cannot be edited once submitted for approval
- The scenario remains locked until an approver rejects it and sends it back
- This prevents changes from being made while a scenario is under review
- It ensures approvers are reviewing the exact changes that were submitted

When this setting is disabled, scenario creators can continue making edits even while the scenario is in the approval queue.

{% hint style="info" %}
**Screenshot Placeholder:** General Settings showing "Lock scenarios upon submission" checkbox
{% endhint %}

## Best Practices for Scenario Approvals

### For Scenario Creators

- **Provide Clear Justification**: Write detailed, specific reasons for your changes. Explain the business rationale and expected outcomes.
- **Review Before Submitting**: Use the Configure Submission preview to verify all changes are correct before submitting.
- **Document Context**: Include relevant context about why changes are needed, not just what the changes are.
- **Respond to Feedback**: When scenarios are rejected, carefully review the reasons and address all concerns in your revisions.

### For Approvers

- **Review Thoroughly**: Examine each change individually rather than approving everything at once.
- **Provide Specific Feedback**: When rejecting changes, explain clearly what needs to be addressed.
- **Check Bottom-Line Impact**: Ensure the cost and headcount impacts align with budget constraints and strategic goals.
- **Consider Dependencies**: Look for potential downstream impacts of proposed changes.

### For Administrators

- **Choose Approvers Carefully**: Select approvers who have the authority and context to make informed decisions.
- **Communicate the Process**: Ensure all users understand how the approval workflow functions.
- **Set Clear Guidelines**: Establish criteria for what types of changes need approval and what approvers should look for.
- **Review Lock Setting**: Decide whether locking scenarios upon submission makes sense for your organization's workflow.

## Common Questions

**Can I have different approvers for different types of scenarios?**

Yes, use Level 0 and Level 3 scenario-specific approvers for this purpose. Global Level 1 and 2 approvers will still review all scenarios, but you can add additional reviewers for specific cases.

**What happens if a Level 1 approver rejects a change?**

The entire scenario is sent back to the creator for revisions. The scenario cannot proceed to Level 2 until all Level 1 approvers approve.

**Can I remove a scenario from the approval queue?**

Contact your administrator or an approver to reject the scenario and send it back to you. You can then make any needed changes or cancel the scenario entirely.

**Do I need to set up all four approval levels?**

No. At minimum, you need at least one Level 1 approver. Level 0, Level 2, and Level 3 are optional and can be used based on your organization's governance needs.

---

## Related Articles

- [Creating and Managing Scenarios](creating-scenarios.md)
- [Scenario Impacts and Changes Panel](impacts-panel.md)
- [Admin Settings Overview](../admin-settings/overview.md)
