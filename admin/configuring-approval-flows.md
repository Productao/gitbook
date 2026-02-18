---
description: Setting up and managing scenario approval workflows
icon: workflow
hidden: false
---

# Configuring Approval Flows

Approval flows ensure that workforce planning scenarios go through proper review before implementation. As an admin, you'll configure who approves scenarios and how the approval process works.

## What Are Approval Flows?

**Approval flows** are the multi-stage review processes that scenarios go through before being marked as approved and ready for implementation.

**Why use approval flows:**
- Ensure budget compliance before implementing changes
- Get stakeholder buy-in from Finance, HR, and leadership
- Create audit trail of who approved what
- Prevent unauthorized organizational changes
- Maintain data governance and accountability

---

## Understanding the 4-Level Approval System

Agentnoon uses a 4-level approval system (Levels 0-3):

### **Level 1 & Level 2: Global Approvers**
- Set in **Settings → General** by admins
- Apply to **all scenarios** organization-wide
- Level 1 approves first, then Level 2
- Can have multiple Level 1 approvers (any one can approve)
- Typical use: Level 1 = Department leaders, Level 2 = Finance/HR

### **Level 0 & Level 3: Scenario-Specific Approvers**
- Set **per scenario** when submitting for approval
- Level 0 = First approver for that specific scenario
- Level 3 = Final approver for that specific scenario
- Typical use: Level 0 = Scenario creator's manager, Level 3 = Executive sponsor

### **Approval Flow Order:**
```
Level 0 (scenario-specific)
    ↓
Level 1 (global)
    ↓
Level 2 (global)
    ↓
Level 3 (scenario-specific)
```

**You don't have to use all levels.** Many organizations only use Level 1 and Level 2 (global approvers).

---

## Configuring Global Approvers (Levels 1 & 2)

### Step 1: Access Approval Settings
1. Go to **Settings** (admin menu)
2. Click **General** tab
3. Scroll to "Approval Workflows" section

### Step 2: Add Level 1 Approvers
1. Click "Add Level 1 Approver"
2. Select user(s) from dropdown
3. Add multiple approvers if desired

**How Level 1 works with multiple approvers:**
- Any **one** Level 1 approver can approve
- Once one approves, it proceeds to Level 2
- If one rejects, the scenario is rejected (goes back to requester)

**Typical Level 1 approvers:**
- Department heads
- HR Business Partners
- Finance Business Partners
- Team leaders responsible for their areas

### Step 3: Add Level 2 Approvers
1. Click "Add Level 2 Approver"
2. Select user(s) from dropdown

**Typical Level 2 approvers:**
- CFO or Finance leadership
- CHRO or HR leadership
- COO or Operations leadership
- Whoever has final budget authority

### Step 4: Configure "Lock Scenarios Upon Submission"
**Critical setting:** Enable this checkbox to lock scenarios during the approval process.

**When enabled:**
- Scenarios cannot be edited once submitted
- Prevents changes while approvers are reviewing
- If rejected, scenario unlocks and returns to creator

**When disabled:**
- Scenarios remain editable during approval
- Risk: Changes could be made while approvers are reviewing old version
- Not recommended for most organizations

**Recommendation:** Enable this setting for approval integrity.

### Step 5: Save Settings
Click "Save" to apply global approval configuration.

---

## Setting Scenario-Specific Approvers (Levels 0 & 3)

Scenario-specific approvers are set when submitting a scenario, not in Settings.

### Step 1: Open Scenario
Open the scenario you want to submit for approval.

### Step 2: Configure Submission
1. Open the **OpEx Panel** (Scenario Impacts and Changes)
2. Scroll to bottom
3. Click **"Configure Submission"** button

### Step 3: Set Approvers (if needed)
- **Level 0 Approver:** Select first approver for this scenario
- **Level 3 Approver:** Select final approver for this scenario
- Leave blank if you don't need scenario-specific approvers

### Step 4: Provide Justification
- Explain the scenario purpose
- Highlight key impacts (headcount change, cost impact)
- Provide context for approvers

### Step 5: Submit for Approval
1. Review summary (shows approvers, impacts, changes)
2. Click **"Submit"**
3. Scenario is now locked (if that setting is enabled)
4. Approvers receive notification

---

## The Approval Process (Approver's Perspective)

### How Approvers Receive Scenarios
1. Notification sent (email or in-app depending on configuration)
2. Scenario appears in their approval queue
3. Scenario shows current approval level and pending action

### How Approvers Review Scenarios
1. Open the scenario
2. View the **OpEx Panel** (Scenario Impacts and Changes)
3. Review each change:
   - See position additions (green)
   - See position reductions (red)
   - See modifications (blue)
4. Check cost and headcount impact
5. Review justification provided by requester

### Approver Actions
For **each change**, approvers must:
- ✅ **Approve** (green checkmark) - Accept this change
- ❌ **Reject** (red X) - Reject this change with reason

**Critical rule:** Approvers must approve or reject **every change**. Partial approvals are not currently supported—if any change is rejected, the entire scenario is rejected.

### Approver's Final Step
After reviewing all changes:
1. Provide final comment (optional but recommended)
2. Click **"Send Decision"** or similar button
3. Scenario proceeds to next approval level OR returns to requester if rejected

---

## Approval States

### Scenario States
- **Draft:** Editable, not submitted
- **Pending Approval:** Submitted, locked, awaiting approver action
- **Approved:** All approvers approved, ready for implementation
- **Rejected:** At least one change rejected, returned to creator

### What Happens After Rejection
1. Scenario unlocks (becomes editable again)
2. Returns to creator
3. **Approval history preserved:** Logs show who rejected, when, and why
4. Creator makes changes to address rejection reasons
5. Creator resubmits

**Important:** Previously approved positions stay approved on resubmission (saves time for approvers).

---

## Approval History & Tracking

### Viewing Approval History
In any scenario:
1. Open OpEx Panel
2. Look for "Approval History" or "Activity" section
3. See timeline of:
   - When submitted
   - Who approved/rejected
   - What positions were approved/rejected
   - Comments from approvers
   - When returned to creator (if rejected)

### What's Tracked
- All approval/rejection actions
- Timestamps
- Approver names
- Reasons for rejection
- Changes made between resubmissions

---

## Common Approval Workflow Designs

### Simple: 2-Level Approval
**Setup:**
- Level 1: HR Business Partner
- Level 2: CFO or Finance Director
- No Level 0 or Level 3

**Use case:** Small to mid-size organizations with straightforward approval needs.

### Standard: 3-Level Approval
**Setup:**
- Level 1: Department leaders (multiple, any one can approve)
- Level 2: Finance leadership
- Level 3: CEO or executive sponsor (scenario-specific)

**Use case:** Most common setup, balances thoroughness with efficiency.

### Complex: 4-Level Approval
**Setup:**
- Level 0: Scenario creator's direct manager (scenario-specific)
- Level 1: Departmental VP
- Level 2: CFO
- Level 3: Board or executive committee (scenario-specific for major changes)

**Use case:** Large enterprises with strict governance requirements.

### Department-Specific Approvals
**Setup:**
- Level 1: Multiple department heads (Engineering VP, Sales VP, etc.)
- Whichever department's scenario it is, that VP approves
- Level 2: CFO (final approval for all)

**Use case:** Decentralized organizations where departments manage their own workforce planning.

---

## Best Practices

### Approval Flow Design
1. **Keep it as simple as possible:** More levels = slower approvals
2. **Use Level 1 for domain experts:** People who understand the work
3. **Use Level 2 for budget gatekeepers:** Finance, HR, executives
4. **Reserve Level 0 & 3 for exceptional cases:** Don't overcomplicate

### Approver Selection
- **Pick people who will respond quickly:** Slow approvers bottleneck the process
- **Delegate approval authority:** Empower VPs/Directors, don't route everything to CEO
- **Have backup approvers:** If someone's on vacation, approval shouldn't stall

### Scenario Submission
- **Provide context:** Explain the "why" in the justification
- **Highlight unusual items:** Call out anything non-standard
- **Quantify impact:** "$2M savings from 15 position closures"
- **Attach supporting docs if needed:** Business case, budget memo, etc. (outside Agentnoon, via email)

### Rejection Handling
- **Be specific about rejection reasons:** Don't just say "No", explain why
- **Suggest alternatives:** "Consider closing X positions instead of Y"
- **Approve what you can:** If possible (future enhancement: partial approvals)

---

## Troubleshooting Common Issues

**"Scenario is stuck in approval"**
- Check if approver has been notified
- Follow up with approver directly
- Check if approver is on vacation (delegate if needed)
- Admin can potentially re-assign approver (contact support if urgent)

**"I submitted but it's not locked"**
- Check if "Lock scenarios upon submission" is enabled in Settings
- This setting must be enabled for scenarios to lock

**"Approver can't find the scenario to approve"**
- Ensure approver has access to that part of the org (access group settings)
- Verify approver is assigned at the correct level
- Check that scenario was actually submitted (not still in Draft)

**"Partial approval not working"**
- Current limitation: All changes must be approved together
- Workaround: Split into multiple scenarios (one per change type)
- Future enhancement expected to support partial approvals

**"Previously approved items need re-approval"**
- This shouldn't happen—previously approved positions stay approved on resubmission
- If this occurs, contact Agentnoon support (may be a bug)

---

## Advanced: Approval Workflow Strategy

### When to Require Approvals
**Always require approval for:**
- Scenarios affecting >10% of workforce
- Budget impacts >$500K (or your threshold)
- Reorgs involving executive-level positions
- RIFs (layoffs)
- Major new hiring plans

**Consider optional approval for:**
- Minor team restructures (<10 people)
- Small budget adjustments
- Exploratory scenarios (not intended for implementation)

### Approval Tiering by Scenario Type
Configure different approval flows based on scenario impact:
- **Low impact:** Level 1 only
- **Medium impact:** Levels 1 & 2
- **High impact:** Levels 0, 1, 2, & 3

**Note:** Current Agentnoon doesn't automatically route based on impact—you'll set this manually when submitting.

---

## Next Steps

- **[Admin Overview](overview.md)** - Full admin responsibilities
- **[Data Refresh & Sync](data-refresh-sync.md)** - Keep data up to date
- **[Scenario Approvals](../scenarios/approvals.md)** - User guide to submitting scenarios for approval
- **[Access Control](../access-control/access-groups.md)** - Control who can create and approve scenarios
