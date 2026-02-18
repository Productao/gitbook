---
description: Share scenarios with team members and control access levels
hidden: false
---

# Sharing Scenarios

Sharing scenarios allows you to collaborate with teammates, get stakeholder feedback, and present plans to leadership. Agentnoon provides flexible access controls to ensure the right people have the right level of access.

---

## How to Share a Scenario

**Steps:**
1. Open the scenario you want to share
2. Click **Share** button in the left panel (or top taskbar)
3. Share dialog opens
4. Enter email addresses or select users from list
5. Choose access level (see below)
6. Optionally add a message
7. Click **Share**

**What happens:**
- Selected users receive notification/email
- They can access the scenario from their homepage
- Access level determines what they can do

---

## Access Levels

When sharing a scenario, choose the appropriate access level:

### View Only

**What they can do:**
- See the scenario org chart
- View positions and employees
- Read comments
- View Change Tracker
- Export data (if permitted)

**What they CANNOT do:**
- Make changes to positions
- Add/edit/delete positions
- Move positions
- Leave comments
- Edit scenario settings

**When to use:**
- Presenting to leadership for review
- Sharing with stakeholders who don't need edit access
- Allowing observers to track progress

---

### Edit Access

**What they can do:**
- Everything in View Only, plus:
- Add, edit, delete positions
- Move positions to different managers
- Close positions
- Assign/detach employees
- Leave comments and @mention others
- Make any changes to the scenario

**What they CANNOT do:**
- Delete the scenario (only owner can)
- Change scenario owner
- Remove other users' access (only owner can)

**When to use:**
- Collaborating with co-planners
- Delegating scenario building to team members
- Distributed planning across departments

---

### Comment Only

**What they can do:**
- Everything in View Only, plus:
- Leave comments on scenario
- Comment on specific positions
- @mention other users
- Reply to existing comments

**What they CANNOT do:**
- Make changes to positions
- Edit scenario structure

**When to use:**
- Reviewers who provide feedback but don't edit
- Stakeholders who need to discuss but not change
- Department heads reviewing plans for their areas

---

## Managing Shared Access

### View Who Has Access

1. Click **Share** button
2. See list of all users with access
3. See their access level

### Change Access Level

1. Click **Share** button
2. Find user in list
3. Change dropdown to new access level
4. Click **Update**

### Remove Access

1. Click **Share** button
2. Find user in list
3. Click **Remove** or **X** icon
4. Confirm removal

**Only the scenario owner can manage access.**

---

## Access Control and Permissions

**Important:** Scenario sharing **respects existing user permissions**.

**Example:**
- User A has access only to Engineering org
- You share Full Org scenario with User A
- User A sees only Engineering positions in the scenario
- User A cannot see or edit positions outside Engineering

**This means:**
- Org-level permissions carry through to scenarios
- Scenario sharing doesn't override access controls
- Users see only what they're already allowed to see

**Learn more:** [Access Control](../../admin/access-control.md)

---

## Common Sharing Workflows

### Workflow 1: Share for Review

**Goal:** Get feedback from 3 department heads.

**Steps:**
1. Complete draft scenario
2. Click **Share**
3. Add 3 department heads
4. Select **Comment Only** access
5. Add message: "Please review your areas and leave comments by Friday"
6. Click **Share**
7. Department heads receive notification
8. They review and comment
9. You address feedback

**Result:** Structured feedback from stakeholders.

---

### Workflow 2: Collaborative Building

**Goal:** Build scenario with co-planner.

**Steps:**
1. Create scenario
2. Click **Share**
3. Add co-planner's email
4. Select **Edit Access**
5. Add message: "Let's build this together - I'll work on Engineering, you do Sales"
6. Click **Share**
7. Both work simultaneously
8. Changes sync in real-time

**Result:** Faster scenario building.

---

### Workflow 3: Present to Leadership

**Goal:** Share read-only with executive team.

**Steps:**
1. Finalize scenario
2. Click **Share**
3. Add executive team members
4. Select **View Only** access
5. Add message: "Final Q2 plan for your review"
6. Click **Share**
7. Present in meeting (they can follow along)
8. They review on their own time
9. They can see but not change

**Result:** Controlled presentation access.

---

### Workflow 4: Tiered Access

**Goal:** Different access levels for different stakeholders.

**Steps:**
1. Share with planning team: **Edit Access**
2. Share with department heads: **Comment Only**
3. Share with leadership: **View Only**
4. Each group has appropriate level of access
5. Collaboration flows smoothly

**Result:** Right access for right roles.

---

## Best Practices

1. **Choose access level carefully** - Don't give Edit Access when Comment Only is sufficient
2. **Add context in message** - Explain why you're sharing and what you need
3. **Review access regularly** - Remove access when no longer needed
4. **Remember org permissions** - Users can only see what they're already allowed to see
5. **Use Comment Only for reviewers** - Prevents accidental edits
6. **Use Edit Access sparingly** - Only for true co-planners
7. **Document who has access** - Keep track in comments or external doc

---

## Troubleshooting

**Problem:** User can't see positions in shared scenario.
- **Solution:** Check their org-level permissions. Scenario sharing respects existing access controls. They may only have access to specific departments.

**Problem:** User can't edit scenario even though I shared with Edit Access.
- **Solution:** Verify access level in Share dialog. Make sure you selected "Edit Access" not "Comment Only" or "View Only".

**Problem:** Can't remove user's access.
- **Solution:** Only scenario owner can manage access. If you're not the owner, ask the owner or admin.

**Problem:** User didn't receive share notification.
- **Solution:** Check that email address is correct. Check their spam folder. Verify notification settings in their Agentnoon account.

**Problem:** Want to change who owns the scenario.
- **Solution:** Contact admin. Scenario ownership transfer requires admin action.

---

## Next Steps

Now that you understand sharing:
- Learn [Commenting](commenting.md) to discuss scenarios with teammates
- Explore [Co-Editing](co-editing.md) for real-time collaboration
- Understand [Notifications](notifications.md) to stay updated
- Return to [Scenario Collaboration](../collaboration.md) overview
