---
description: Common questions for new Agentnoon users
hidden: false
---

# Getting Started FAQs

New to Agentnoon? This page answers the most common questions from first-time users to help you get up and running quickly.

---

## Logging In & Access

### How do I log in to Agentnoon?
**Answer:** Agentnoon supports multiple login methods:
- **Single Sign-On (SSO):** If your company uses Okta, Azure AD, or Google Workspace, click "Sign in with SSO" and enter your company email
- **Email/Password:** If SSO isn't configured, use your email and password
- **First-time login:** Check your email for an invitation link from Agentnoon

> **[Screenshot placeholder: Login screen showing SSO button, email/password fields, and "Forgot Password" link]**

**Learn more:** [Authentication & IAM](../authentication-and-identity-security/README.md)

### I can't log in. What should I do?
**Common issues:**
- **Wrong email:** Use your company email, not personal email
- **SSO not configured:** Contact your IT admin to set up SSO
- **Account not created:** Ask your Agentnoon admin to invite you
- **Password reset:** Click "Forgot Password" on the login screen

**Learn more:** [Troubleshooting Login Issues](../troubleshooting/login-access-issues.md)

### Do I need to be invited to use Agentnoon?
**Answer:** Yes. An admin at your company must invite you. You'll receive an email invitation with a link to set up your account.

**If you haven't received an invitation:** Contact your HR team or the person who manages Agentnoon at your company.

---

## Understanding the Basics

### What is Agentnoon?
**Answer:** Agentnoon is a workforce planning and organizational design platform. It helps you:
- Visualize your current organizational structure
- Plan future changes (hiring, reorgs, budget cuts)
- Project workforce costs over time
- Get approvals before implementing changes

**Think of it as:** A combination of org chart software, workforce planning tool, and budget forecasting system.

**Learn more:** [Welcome to Agentnoon](../start-here/welcome.md)

### What's the difference between Main Org and Scenarios?
**Answer:**
- **Main Org:** Your current organizational structure (view-only, reflects real data)
- **Scenarios:** Sandboxes where you model "what-if" changes without affecting Main Org

**Analogy:** Main Org is like your company's actual org chart. Scenarios are like sketching different versions of that org chart on paper before deciding which to implement.

**Learn more:** [Key Concepts](../start-here/concepts.md)

### What are positions vs. people?
**Answer:**
- **Position:** A role in your organization (e.g., "Senior Engineer reporting to Engineering Manager A")
- **Person/Headcount:** The employee filling that position (e.g., "Sarah Chen")

**Why it matters:** Agentnoon is position-first. You plan by adding/closing/moving positions, not by managing individual people.

**Example:** You have 100 positions (roles with budget allocated). 85 are filled (people in those roles). 15 are vacant (open positions to recruit for).

**Learn more:** [Position vs Headcount Management](../best-practices/position-vs-headcount.md)

### Where do I start as a new user?
**Follow this path:**
1. Read the [Quick Start Guide](../start-here/quick-start-guide.md) (10 minutes)
2. Explore Main Org (your current organizational structure)
3. Create your first scenario (try adding a position or moving someone)
4. View your scenario in Forecast (see the impact over time)
5. Delete the practice scenario (it was just for learning!)

**Learn more:** [Quick Start Guide](../start-here/quick-start-guide.md)

---

## Navigating Agentnoon

### What's the main navigation?
**Answer:** Click "Open Org" to enter the organizational view. From there:
- **Directory** - Spreadsheet-style table view
- **Org Chart** - Visual hierarchy view
- **Forecast** - Time-based projections
- **Workforce Hub** - Analytics and charts

> **[Screenshot placeholder: Main navigation bar showing "Open Org" button and view dropdown menu with Directory, Org Chart, Forecast, and Workforce Hub options]**

**Learn more:** [Main Org Navigation](../main-org/navigation.md)

### What's the taskbar on the left side?
**Answer:** The taskbar provides tools for navigating and analyzing your org:
- **Search** - Find people or positions
- **Filter** - Narrow down data
- **Highlight** - Color-code by department, location, etc.
- **Card Content** - Customize what shows on position cards
- **Views** - Save and load custom views
- **Export** - Download data to CSV, PowerPoint, or images

> **[Screenshot placeholder: Left taskbar showing icons for Search, Filter, Highlight, Card Content, Views, and Export tools]**

**Learn more:** [Main Org Taskbar](../main-org/taskbar.md)

### How do I switch between org chart and table view?
**Answer:** Use the dropdown at the top of the screen:
- Select **"Directory"** for spreadsheet/table view
- Select **"Org Chart"** for visual hierarchy view (default)

Both views show the same data, just in different formats.

**Learn more:** [Directory Overview](../directory/overview.md)

### Can I customize what I see on position cards?
**Answer:** Yes! Click **Card Content** in the left taskbar. Select which fields you want to display (name, title, salary, department, etc.). You can also reorder fields by clicking the gear icon.

**Learn more:** [Main Org Taskbar - Card Content](../main-org/taskbar.md)

---

## Working with Data

### Where does the data come from?
**Answer:** Your admin imports data from your HRIS (Human Resources Information System) like Workday, BambooHR, or ADP. This can be:
- **Manual CSV upload:** Admin uploads a spreadsheet
- **Live integration:** Automatic sync from your HRIS

Main Org always reflects your current organizational data.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### Can I edit data in Main Org?
**Answer:** No. Main Org is view-only—it reflects your current org structure.

**To make changes:** Create a scenario. Scenarios are where you model changes before implementing them in the real world.

**Learn more:** [Scenarios Overview](../scenarios/overview.md)

### How often is data updated?
**Answer:** Depends on your organization's setup:
- **Manual uploads:** Updated when admin uploads new data (weekly/monthly typically)
- **Live integration:** Syncs automatically (daily/weekly depending on configuration)

Ask your admin how often data refreshes at your company.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### Why don't I see certain employees?
**Answer:** You might have limited access based on your role:
- **Access Groups:** Admins can restrict you to see only your department, location, or business unit
- **Filters:** You may have accidentally filtered out employees
- **Data not uploaded:** The employee might not be in the system yet

**To check:** Clear all filters (Filter button → Clear All). If you still don't see them, check with your admin about your access permissions.

**Learn more:** [Access Groups](../access-control/access-groups.md)

---

## First Scenario

### How do I create my first scenario?
**Step-by-step:**
1. Click **"Create Scenario"** button (top-right)
2. Name your scenario (e.g., "My First Test Scenario")
3. Choose scenario type:
   - **Full Org:** Copy your entire organization
   - **Partial Org:** Copy a specific department or location
   - **New Org:** Start from scratch
4. Click Create

> **[Screenshot placeholder: "Create Scenario" dialog showing name field, scenario type options (Full Org, Partial Org, New Org), and Create button]**

**Now what?** You can add positions, close positions, move people, change salaries—whatever you want to test!

**Learn more:** [Creating Scenarios](../scenarios/creating-scenarios.md)

### What's the difference between Full Org, Partial Org, and New Org scenarios?
**Answer:**
- **Full Org:** Copies your entire Main Org. Use for company-wide planning (reorgs, annual hiring plans, budget cuts)
- **Partial Org:** Copies only a specific part (e.g., just Engineering dept). Use for department-specific planning
- **New Org:** Starts blank. Use for modeling a brand-new team or business unit from scratch

**Most common:** Full Org (for comprehensive planning)

**Learn more:** [Creating Scenarios](../scenarios/creating-scenarios.md)

### Can I delete a scenario?
**Answer:** Yes! Scenarios are temporary workspaces. Delete them anytime:
1. Open the scenario
2. Click the **three-dot menu** (top-right)
3. Select **"Delete Scenario"**
4. Confirm deletion

**No risk:** Deleting a scenario doesn't affect Main Org or other scenarios.

**Learn more:** [Scenario Management](../scenarios/management.md)

### What if I make a mistake in a scenario?
**Answer:** No problem! Scenarios are sandboxes—mistakes don't affect Main Org. Options:
- **Undo changes:** If you just made the change, use your browser's undo (Cmd/Ctrl + Z)
- **Delete and start over:** Delete the scenario and create a new one
- **Revert individual changes:** Close positions you added, re-add positions you closed

**Learn more:** [Making Position Changes](../scenarios/making-position-changes.md)

---

## Common Confusion for New Users

### "I created a scenario but Main Org didn't change. Why?"
**Answer:** Scenarios don't automatically change Main Org. They're sandboxes for testing changes.

**To implement changes:** After your scenario is approved, you implement the changes in your real HRIS (Workday, BambooHR, etc.). Then your admin updates Main Org data, and the changes appear.

**Learn more:** [Scenarios Overview](../scenarios/overview.md)

### "I added a position in a scenario. When does it get hired?"
**Answer:** Adding a position in Agentnoon doesn't hire anyone. It models the impact of hiring that position.

**Real hiring happens outside Agentnoon:** After your scenario is approved, you recruit and hire someone into that role in your HRIS.

**To show when it will be hired:** Set a "hire date" on the position. This makes it appear in Forecast projections at that future date.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

### "What's span of control and why does it keep appearing?"
**Answer:** Span of Control (SOC) = number of direct reports a manager has.

**Why it matters:**
- Too high (>10 reports) = overloaded manager
- Too low (<3 reports) = unnecessary management layer
- Healthy range: 5-10 direct reports

Agentnoon highlights SOC to help you design balanced organizations.

**Learn more:** [Key Concepts - Span of Control](../start-here/concepts.md)

### "I see 'OpEx Panel' mentioned. What is that?"
**Answer:** OpEx Panel = "Operating Expense Panel" (also called "Scenario Impacts and Changes"). It shows:
- Net cost impact (+$500K, -$200K)
- Net headcount impact (+10, -5)
- List of all changes (additions, closures, moves)
- Submission button for approval

> **[Screenshot placeholder: OpEx Panel showing net headcount change (+15 positions), net cost impact (+$2.3M), and categorized list of additions (green) and closures (red)]**

**Where to find it:** In any scenario, look for a side panel on the right or click the "Scenario Impacts and Changes" button.

**Learn more:** [Budget Planning & Tracking](../forecast/budget-planning-tracking.md)

### "What are effective dates?"
**Answer:** Effective dates control when changes take effect in time-based projections.

**Example:** You move 5 people from Team A to Team B with effective date of January 2027. In Forecast, they appear in Team A through 2026, then move to Team B starting January 2027.

**Why useful:** Phase organizational changes over time (Q1: add managers, Q2: move teams, Q3: finalize structure).

**Learn more:** [Time-Based Planning](../scenarios/time-based-planning.md)

---

## Getting Help

### Where can I find video tutorials?
**Answer:** Video tutorials are available in:
- [Video Tutorials page](../start-here/video-tutorials.md) (curated list)
- Your admin may have company-specific training videos

**Learn more:** [Video Tutorials](../start-here/video-tutorials.md)

### Who do I ask if I have questions?
**Options:**
1. **This documentation:** Search for your question
2. **Your manager or HR team:** They may have used Agentnoon before
3. **Your company's Agentnoon admin:** For account/access questions
4. **Agentnoon support:** For product questions or issues

**Learn more:** [Support & How to Self-Help](../start-here/support-self-help.md)

### Can I practice without affecting anything?
**Answer:** Yes! Create a scenario and experiment. Scenarios are sandboxes—they don't affect Main Org or anyone else's work. Delete it when you're done practicing.

**Pro tip:** Name it "Practice Scenario - DELETE ME" so you remember to clean it up later.

---

## Next Steps

- **[Quick Start Guide](../start-here/quick-start-guide.md)** - 30-minute onboarding
- **[Key Concepts](../start-here/concepts.md)** - Essential terminology
- **[Creating Scenarios](../scenarios/creating-scenarios.md)** - Your first scenario
- **[Data & Import FAQs](data-import.md)** - Data management questions
- **[Scenarios FAQs](scenarios.md)** - Scenario planning questions
