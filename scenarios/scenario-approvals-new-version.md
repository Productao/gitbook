---
description: Review and approve scenario changes before they are finalized.
icon: thumbs-up
---

# Scenario Approvals (New Version)

### Overview

Scenario approvals help teams review proposed org changes in a structured way. You can set approval levels, submit a scenario for review, and track whether it is pending, approved, or rejected.

Agentnoon supports both:

* Global approvers, which are set in the main board settings
* Scenario-specific approvers, which are set on an individual scenario

### Before you begin

Make sure:

* You already have a scenario to submit
* The right people already have Agentnoon accounts
* Global approvers are set in **Settings** if needed
* Scenario-specific approvers are set if needed
* Your scenario includes the changes you want reviewed

### Steps

### Set up global approvers&#x20;

{% hint style="info" %}
Note that if[ scenario specific approvers are configured](#user-content-fn-1)[^1], configuring global approvers is optional.
{% endhint %}

1. Open the main board.
2. Go to **Settings**.
3. In **Approval Configurations**, choose your:
   * **Level 1 approvers**
   * **Level 2 approvers**
4. If you want submitted scenarios to become read-only, enable **Lock Scenarios on submission (Recommended)**.
5. Click **Save**.

### Set up scenario-specific approvers

{% hint style="info" %}
Note that if[ global approvers are configured](#user-content-fn-1)[^1], configuring scenario-specific is optional.
{% endhint %}

1. Go to the scenario list.
2. Open the scenario menu.
3. Click **Configure approvers**.
4. Review the global approvers shown for:
   * **Level 1 approvers**
   * **Level 2 approvers**
5. Add scenario-specific approvers if needed:
   * **Level 0 approvers**
   * **Level 3 approvers**
6. Click **Save Changes**.

### Submit a scenario for review

1. Open the scenario.
2. Open **Scenario Impact and Changes**.
3. Click **Configure submission**.
4. Review the approver list.
5. Enter a justification in **Justification**.
6. Click **Submit scenario**.
7. Confirm the submission.

### Review a submitted scenario

When a reviewer opens a submitted scenario, they can review:

* **Cost**
* **Count**
* **Reviews**
* **Justification**
* **Reviewer Status**
* **Timeline**

In the **Reviews** tab, the reviewer can:

* Approve individual position changes
* Reject individual position changes
* Use **Approve all**
* Approve the full scenario
* Reject the full scenario

A reviewer must approve all changed positions before approving the scenario.

{% hint style="info" %}
Note that a review must be completed in one session. Leaving an approval session midway will not save changes.&#x20;
{% endhint %}

### Update and resubmit after rejection

If a scenario is rejected:

1. Open the scenario again.
2. Make the requested changes.
3. Return to **Scenario Impact and Changes**.
4. Click **Configure submission**.
5. Update the justification if needed.
6. Submit the scenario again.

### Expected result

After submission:

* The scenario moves into the approval flow
* Reviewers at the current level can review it
* The scenario can be locked from editing if locking is enabled

After approval:

* The scenario moves to the next level of approval, or is marked at "**Approved**" if fully approved

After rejection:

* The scenario returns to the submitted and the scenario is unlocked for editing

### Troubleshooting

| Problem                                                  | Solution                                                                                                                |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Cannot submit the scenario                               | Check whether any reviewers are configured. Agentnoon can block submission if no reviewers are assigned.                |
| Reviewer cannot edit the scenario                        | This is expected. Submitted scenarios are reviewed in read-only mode (unless otherwise configured in Settings>General). |
| Reviewer cannot approve the complete scenario            | Make sure all changed positions are approved in the **Reviews** tab first.                                              |
| Scenario became editable again after rejection           | This is expected. Rejected scenarios are unlocked for editing.                                                          |
| Some earlier approvals seem to remain after resubmission | This can happen if the underlying position change did not change.                                                       |

### Notes or limitations

* Global approvers are managed in **Settings**.
* Scenario-specific approvers are managed through **Configure approvers** on the scenario.
* Scenario-specific approvers use **Level 0** and **Level 3**.
* Global approvers use **Level 1** and **Level 2**.
* The approval flow starts at the lowest configured level.
* Submitted scenarios can be locked until an approver rejects them.
* Submission requires a justification.
* A scenario cannot be approved until all changed positions are approved.

[^1]: 
