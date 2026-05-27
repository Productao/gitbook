---
description: Common questions for new Agentnoon users
---

# 🚀 Getting Started FAQs

New to Agentnoon? This page answers the most common questions from first-time users to help you get up and running quickly.

## Logging In & Access

### How do I log in to Agentnoon?

Agentnoon supports SSO (Okta, Azure AD, Google Workspace), email/password, and first-time invitation links. Use whichever method your company has configured.

**Learn more:** [Authentication & IAM](../authentication-and-identity-security/)

### I can't log in. What should I do?

Check that you're using your company email, that SSO is configured by your IT admin, and that your account has been created. You can also try "Forgot Password" on the login screen.

**Learn more:** [Troubleshooting Login Issues](../troubleshooting/login-access-issues.md)

### Do I need to be invited to use Agentnoon?

Yes. An admin at your company must invite you. If you haven't received an invitation, contact your HR team or the person who manages Agentnoon at your company.

## Navigating Agentnoon

### What's the difference between Main Org and Scenarios?

**Main Org** is your current, view-only organizational structure reflecting real data. **Scenarios** are sandboxes where you model "what-if" changes without affecting Main Org.

**Learn more:** [Key Concepts](../start-here/concepts.md)

### What are positions vs. people?

A **position** is a role in your organization (e.g., "Senior Engineer"). A **person** is the employee filling that position. Agentnoon is position-first -- you plan by adding, closing, or moving positions.

**Learn more:** [Position vs Headcount Management](../best-practices/position-vs-headcount.md)

### Where do I start as a new user?

Start with the Quick Start Guide, explore Main Org, create a test scenario to try adding or moving a position, then view your changes in Forecast to see the projected impact.

**Learn more:** [Quick Start Guide](../start-here/quick-start-guide.md)

### What's the main navigation?

Click "Open Org" to enter the organizational view, then switch between **Directory** (table view), **Org Chart** (visual hierarchy), **Forecast** (time-based projections), and **Workforce Hub** (analytics).

**Learn more:** [Main Org Navigation](../main-org/navigation.md)

### What's the toolbar on the left side?

The left toolbar provides Search, Filter, Highlight, Card Content, Views, and Export tools for navigating and analyzing your org.

**Learn more:** [Main Org Toolbar](../main-org/navigation.md)

### How do I switch between org chart and Directory?

Use the dropdown at the top of the screen. Select **Directory** for spreadsheet/table view or **Org Chart** for visual hierarchy view. Both show the same data in different formats.

**Learn more:** [Directory Overview](../directory/overview.md)

### Can I customize what I see on position cards?

Yes. Click **Card Content** in the left toolbar to choose which fields display on position cards (name, title, salary, department, etc.).

**Learn more:** [Main Org Toolbar - Card Content](../start-here/cards.md)

## Working with Data

### Where does the data come from?

Your admin imports data from your HRIS (Workday, BambooHR, ADP, etc.) via manual CSV upload or live integration. Main Org always reflects your current organizational data.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### Can I edit data in Main Org?

No. Main Org is view-only. To model changes, create a scenario.

**Learn more:** [Scenarios Overview](../scenarios/overview.md)

### How often is data updated?

It depends on your setup -- manual uploads happen when your admin uploads new data, while live integrations sync automatically on a daily or weekly schedule. Ask your admin for details.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### Why don't I see certain employees?

Your admin may have restricted your access to specific departments or business units via Access Groups. You may also have active filters hiding results -- try clearing all filters first.

**Learn more:** [Access Groups](../access-control/access-groups.md)

## First Scenario

### How do I create my first scenario?

Click **Create Scenario**, name it, choose a type (Full Org, Partial Org, or New Org), and click Create. You can then add positions, close positions, move people, or adjust salaries.

**Learn more:** [Creating Scenarios](../scenarios/creating-scenarios.md)

### What's the difference between Full Org, Partial Org, and New Org scenarios?

**Full Org** copies your entire Main Org for company-wide planning. **Partial Org** copies a specific department or location. **New Org** starts blank for modeling a brand-new team. Full Org is most common.

**Learn more:** [Creating Scenarios](../scenarios/creating-scenarios.md)

### Can I delete a scenario?

Yes. Open the scenario, click the three-dot menu, and select **Delete Scenario**. Deleting a scenario never affects Main Org or other scenarios.

**Learn more:** [Scenario Management](../scenarios/management.md)

### What if I make a mistake in a scenario?

Scenarios are sandboxes -- mistakes don't affect Main Org. You can undo from the activity log, revert individual changes, or delete the scenario and start over.

**Learn more:** [Making Position Changes](../scenarios/making-position-changes.md)

### I created a scenario but Main Org didn't change. Why?

Scenarios don't automatically change Main Org. After a scenario is approved, you implement the changes in your real HRIS, and your admin refreshes the data in Agentnoon.

**Learn more:** [Scenarios Overview](../scenarios/overview.md)

### I added a position in a scenario. When does it get hired?

Adding a position in Agentnoon models the impact of hiring -- it doesn't hire anyone. Set a "hire date" on the position so it appears in Forecast projections at the right time.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

### What's span of control and why does it keep appearing?

Span of Control is the number of direct reports a manager has. Agentnoon highlights it to help you design balanced organizations (a healthy range is typically 5-10 direct reports).

**Learn more:** [Key Concepts - Span of Control](../start-here/concepts.md)

### What is the OpEx Panel?

The OpEx (Operating Expense) Panel shows the net cost and headcount impact of your scenario changes, a list of all additions and closures, and the submission button for approval.

**Learn more:** [OpEx Panel](../scenarios/opex-panel.md)

### What are effective dates?

Effective dates control when changes take effect in time-based projections, letting you phase organizational changes over multiple quarters.

**Learn more:** [Time-Based Planning](../scenarios/time-based-planning.md)

## Getting Help

### Where can I find video tutorials?

Video tutorials are available on the dedicated tutorials page. Your admin may also have company-specific training videos.

**Learn more:** [Video Tutorials](../start-here/video-tutorials/video-tutorials.md)

### Who do I ask if I have questions?

Search this documentation first, then try your manager or HR team, your company's Agentnoon admin (for account/access questions), or Agentnoon support (for product questions).

**Learn more:** [Support & How to Self-Help](../start-here/support-self-help.md)

### Can I practice without affecting anything?

Yes. Create a scenario and experiment freely -- scenarios are sandboxes that don't affect Main Org or anyone else's work. Delete it when you're done.

**Learn more:** [Creating Scenarios](../scenarios/creating-scenarios.md)
