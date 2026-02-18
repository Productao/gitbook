---
description: Working with teammates in real-time
hidden: false
---

# Scenario Collaboration

Scenarios are built for teamwork. Agentnoon provides powerful collaboration features including real-time editing, comments, @mentions, and sharing controls to help teams plan together effectively.

## Why Collaborate in Scenarios

**Common collaboration needs:**

- **Get stakeholder input** - Share scenario with department heads for feedback
- **Discuss specific positions** - Comment on roles with questions or context
- **Coordinate with teammates** - Multiple planners working simultaneously
- **Present to leadership** - Share read-only access for review
- **Document decisions** - Leave comments explaining why changes were made
- **Track conversations** - Keep planning discussions in context

**Example:** You're planning a reorganization and need input from 3 VPs. Share the scenario, comment on specific positions with questions, and track their responses—all without leaving Agentnoon.

---

## Sharing Scenarios

### How to Share a Scenario

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

### Access Levels

When sharing a scenario, choose the appropriate access level:

#### View Only

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

#### Edit Access

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

#### Comment Only

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

### Managing Shared Access

**View who has access:**
1. Click **Share** button
2. See list of all users with access
3. See their access level

**Change access level:**
1. Click **Share** button
2. Find user in list
3. Change dropdown to new access level
4. Click **Update**

**Remove access:**
1. Click **Share** button
2. Find user in list
3. Click **Remove** or **X** icon
4. Confirm removal

**Only the scenario owner can manage access.**

---

### Access Control and Permissions

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

**Learn more:** [Access Control](../admin/access-control.md)

---

## Real-Time Collaboration

### See Who's Online

When multiple users work in the same scenario simultaneously, Agentnoon shows who's active.

**What you see:**
- **Profile icons** appear at top of scenario
- Each icon represents an active collaborator
- Hover over icon to see name
- See their cursor/activity in real-time (if enabled)

**Why this helps:**
- Avoid conflicting edits
- Coordinate who's working on what
- Know when to communicate before making big changes

---

### Collaborative Editing

**Multiple users can edit the same scenario simultaneously.**

**How it works:**
1. User A and User B both open the same scenario
2. User A adds a position in Engineering
3. User B sees the change appear immediately
4. User B closes a position in Marketing
5. User A sees the closure immediately
6. Changes sync in real-time

**Conflict prevention:**
- If two users edit the same position simultaneously, last save wins
- Best practice: Communicate before making big changes
- Use comments to coordinate who's working on what

---

## Using Comments

Comments are the primary way to discuss scenarios with teammates.

### Types of Comments

#### General Scenario Comments

**What they are:** Comments on the scenario as a whole (not tied to specific position).

**How to add:**
1. Click **Comments** icon in left panel
2. Type your comment
3. Optionally @mention users
4. Click **Post**

**When to use:**
- General questions about the scenario
- High-level feedback
- Announcements to all collaborators
- Summary of changes made

**Example:** "I've completed the Q2 hiring plan. @jsmith can you review the Engineering additions?"

---

#### Position-Specific Comments

**What they are:** Comments attached to a specific position.

**How to add:**
1. Hover over a position card
2. Click **⋮** (three dots) menu
3. Select **Comment**
4. Type your comment
5. Optionally @mention users
6. Click **Post**

**Visual indicator:** Position with comments shows a **comment icon** (💬) on card.

**When to use:**
- Questions about specific roles
- Documenting rationale for position changes
- Flagging issues with particular positions
- Discussing candidates for succession

**Example:** "This role reports to VP Product but should it report to VP Engineering instead? @jsmith thoughts?"

---

### @Mentions

**What they do:** Notify specific users about a comment.

**How to use:**
1. Type **@** in comment field
2. Start typing user's name
3. Select from dropdown
4. User receives notification

**When to use:**
- Direct questions to specific people
- Loop in stakeholders
- Request review from decision makers
- Assign action items

**Example:** "@jsmith can you verify this salary? @mdoe FYI this position will report to you"

**Notifications:**
- @mentioned users receive email notification
- Notification appears in Agentnoon inbox
- Clicking notification takes them to comment

---

### Commenting Best Practices

1. **Comment liberally** - Explain your reasoning
2. **Use @mentions** - Don't assume people will see comments
3. **Be specific** - "Should this role report to Engineering?" vs "Thoughts?"
4. **Respond timely** - Check comments regularly
5. **Mark resolved** - Close comment threads when addressed
6. **Use position comments** - Keep discussion in context

---

## Common Collaboration Workflows

### Workflow 1: Get Stakeholder Feedback

**Goal:** Share scenario with 3 department heads for input.

**Steps:**
1. Complete draft scenario
2. Click **Share**
3. Add 3 department heads with **Comment Only** access
4. Add message: "Please review and leave comments by Friday"
5. Click **Share**
6. Add general comment: "@head1 @head2 @head3 please review your respective areas"
7. Department heads review and comment
8. You address comments and make adjustments
9. Reply to each comment when addressed
10. Submit final scenario for approval

**Result:** Informed, collaborative scenario with stakeholder buy-in.

---

### Workflow 2: Collaborative Scenario Building

**Goal:** Two planners build scenario together.

**Steps:**
1. Planner A creates scenario
2. Planner A shares with Planner B (**Edit Access**)
3. Planner A works on Engineering section
4. Planner B works on Sales section simultaneously
5. Both see each other's icons at top
6. Planner A adds comment: "I'm working on Engineering, you do Sales"
7. Both work in parallel
8. Changes sync in real-time
9. When done, both review together
10. Submit for approval

**Result:** Faster scenario building through parallel work.

---

### Workflow 3: Review-Based Scenario Workflow

**Goal:** Build scenario, get VP approval, then share with leadership.

**Steps:**
1. Planner builds scenario
2. Share with VP (**Edit Access**)
3. VP reviews, makes adjustments, leaves comments
4. Planner addresses comments
5. VP approves
6. Share with leadership team (**View Only**)
7. Add general comment: "Final scenario for review. Implementation starts Q2."
8. Leadership reviews (read-only)
9. Leadership leaves comments with questions
10. Planner responds to comments
11. Submit through approval workflow

**Result:** Tiered review process with appropriate access levels.

---

### Workflow 4: Documenting Scenario Decisions

**Goal:** Use comments to explain every major decision for future reference.

**Steps:**
1. Build scenario, making changes
2. After each major change, add position comment:
   - "Closed this role due to budget constraints - $120K savings"
   - "Promoted Jane to VP because of strong performance and leadership pipeline"
   - "Created 5 new SDE roles to support AI initiative roadmap"
3. Add general comments for big-picture decisions
4. When scenario is approved, all comments serve as documentation
5. Export scenario with comments for historical record

**Result:** Well-documented scenario with clear rationale.

---

## Comment Management

### View All Comments

**How to view:**
1. Click **Comments** icon in left panel
2. See list of all comments (general + position-specific)
3. Sorted by most recent

**Filter comments:**
- Show only unresolved
- Show only @mentions
- Show only position comments
- Show only general comments

---

### Resolve Comments

**How to resolve:**
1. Open comment thread
2. Click **Resolve** button
3. Comment marked as resolved (but not deleted)

**When to resolve:**
- Question answered
- Issue addressed
- Change made as requested
- Comment no longer relevant

**Why resolve:**
- Keep comment list clean
- Focus on active discussions
- Track progress on feedback

---

### Delete Comments

**Who can delete:**
- Comment author can delete their own comments
- Scenario owner can delete any comment

**How to delete:**
1. Open comment
2. Click **⋮** (three dots)
3. Select **Delete**
4. Confirm

**When to delete:**
- Comment was mistake
- Duplicate comment
- Inappropriate content

**Note:** Resolved comments are preferred over deletion for historical record.

---

## Presenting Scenarios to Stakeholders

### Presentation Mode

**How to present:**
1. Share scenario with **View Only** access to stakeholders
2. Walk through scenario in meeting (screenshare)
3. Use **Org Chart** view to show structure
4. Use **Change Tracker** to show impact
5. Use **Workforce Hub** for analytics
6. Reference **comments** to explain decisions

**Best practices:**
- Present "After" view (final state) first
- Then show "Before and After" comparison
- Walk through Change Tracker by department
- Highlight key metrics (cost, headcount, span of control)
- Open floor for questions (add comments in real-time)

---

### Exporting for External Stakeholders

**For stakeholders outside Agentnoon:**
1. Export scenario to PDF
2. Include:
   - Org chart visual
   - Change Tracker summary
   - Before-and-after metrics
   - Comments (if relevant)
3. Share PDF via email

**When to use:**
- Board presentations
- External consultants
- Partners/investors
- Anyone without Agentnoon access

---

## Best Practices

1. **Share early** - Get feedback before finalizing
2. **Use right access level** - View Only for reviewers, Edit for co-planners
3. **Comment liberally** - Explain your reasoning
4. **@mention strategically** - Notify right people
5. **Respond to comments promptly** - Keep discussions moving
6. **Resolve when done** - Keep comment list manageable
7. **Coordinate parallel work** - Communicate who's working on what
8. **Document decisions** - Comments are historical record

---

## Troubleshooting

**Problem:** User can't see positions in shared scenario.
- **Solution:** Check their org-level permissions. Scenario sharing respects existing access controls.

**Problem:** User can't edit scenario even though I shared with Edit Access.
- **Solution:** Verify access level in Share dialog. They may have been given View Only or Comment Only.

**Problem:** Comments not showing up.
- **Solution:** Refresh page. Check if you're filtering comments.

**Problem:** @mention notification not received.
- **Solution:** Check user's notification settings. Verify email is correct.

**Problem:** Two users edited same position, now data is wrong.
- **Solution:** Last save wins. Undo and re-apply correct change. Use comments to coordinate before editing.

**Problem:** Can't see who else is online in scenario.
- **Solution:** Feature may be disabled by admin. Or users may not be actively in the scenario at that moment.

---

## Next Steps

Now that you understand collaboration:
- Share your next scenario with teammates for feedback
- Practice using position-specific comments to document decisions
- Try @mentions to loop in stakeholders
- Use real-time collaboration for faster scenario building
- Learn [Scenario Approvals](approvals.md) to formalize review workflows



