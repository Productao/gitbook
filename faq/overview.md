---
description: Frequently asked questions index
---

# ❓ FAQ Overview

Welcome to the Agentnoon FAQ section. Here you'll find answers to the most common questions users ask about workforce planning, scenarios, forecasting, and administration.

## How to Use This FAQ Section

### Browse by Category

FAQs are organized into topic-specific pages:

* [**Getting Started FAQs**](getting-started.md) - First-time user questions, onboarding, basic concepts
* [**Data & Import FAQs**](data-import.md) - CSV uploads, field mapping, data validation
* [**Scenarios FAQs**](scenarios.md) - Creating scenarios, making changes, submitting for approval
* [**Forecast FAQs**](forecast.md) - Time-based projections, hire dates, effective dates
* [**Permissions & Access FAQs**](permissions-access.md) - User roles, access groups, admin permissions

### Search for Answers

1. Use your browser's search function (Cmd/Ctrl + F) to find keywords
2. Check the relevant category page based on your question topic
3. Review the troubleshooting guides if you're experiencing an issue

### When FAQs Aren't Enough

* **Check Troubleshooting Guides:** [Troubleshooting Overview](../troubleshooting/overview.md)
* **Read Full Documentation:** Each FAQ links to detailed documentation pages
* **Contact Support:** [Support & How to Self-Help](../start-here/support-self-help.md)

***

## Top 10 Most Common Questions

### 1. What's the difference between Main Org and Scenarios?

**Answer:** Main Org is your current organizational structure (view-only). Scenarios are sandboxes where you model changes before implementing them.

**Learn more:** [Key Concepts](../start-here/concepts.md)

### 2. How do I add a new position to my organization?

**Answer:** Create a scenario, navigate to where you want to add the position, click "+ Add Position", fill in details, and save.

**Learn more:** [Making Position Changes](../scenarios/making-position-changes.md)

### 3. What are hire dates and how do they work in Forecast?

**Answer:** Hire dates control when future positions appear in Forecast projections. A position with a hire date of July 2026 will appear in your headcount starting July 2026.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

### 4. How do I submit a scenario for approval?

**Answer:** Open your scenario, go to the OpEx Panel (Scenario Impacts and Changes), click "Configure Submission", add justification, select approvers (if needed), and click Submit.

**Learn more:** [Scenario Approvals](../scenarios/approvals.md)

### 5. Can I edit a scenario after submitting it for approval?

**Answer:** Not if "Lock scenarios upon submission" is enabled (Settings → General). If locked, the scenario becomes read-only until approved or rejected.

**Learn more:** [Configuring Approval Flows](../admin/configuring-approval-flows.md)

### 6. Why isn't my CSV upload working?

**Answer:** Common issues: Missing required fields (Employee ID, Name, Manager), invalid data types (text in salary field), or broken reporting relationships (manager doesn't exist).

**Learn more:** [Data Error Checklist](../data-import/data-error-checklist.md)

### 7. What's the difference between Forecast and Scenarios?

**Answer:** Forecast is for visualization (showing data over time). Scenarios are for modeling (making changes to test "what-if" alternatives).

**Learn more:** [Forecast vs Scenarios](/broken/pages/MKRiiU8DK4L0RAbqG70N)

### 8. How do I give someone access to only their department?

**Answer:** As an admin, create an Access Group with a filter (Department = Engineering), then assign users to that group. They'll only see Engineering employees.

**Learn more:** [Access Groups](../access-control/access-groups.md)

### 9. What's span of control (SOC) and why does it matter?

**Answer:** SOC is the number of direct reports a manager has. Typical healthy range: 5-10 direct reports. Too high (>10) = overloaded manager. Too low (<3) = unnecessary management layer.

**Learn more:** [Key Concepts - Span of Control](../start-here/concepts.md)

### 10. How do I update my Main Org data?

**Answer:** Admins can upload a new CSV file (Main Org → Data Management → Upload) or set up a live integration (SFTP, Workday, API) for automatic syncing.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

***

## Quick Answers by Topic

### Getting Started

* **"How do I log in?"** → Use your company's SSO (Okta, Azure AD, Google) or email/password
* **"Where do I start?"** → [Quick Start Guide](../start-here/quick-start-guide.md)
* **"What's a scenario?"** → A sandbox for testing organizational changes

### Scenarios

* **"How do I create a scenario?"** → Click "Create Scenario", name it, choose type (Full/Partial/New Org)
* **"Can I delete a scenario?"** → Yes, scenarios are temporary and can be deleted anytime
* **"Do scenarios affect Main Org?"** → No, scenarios are sandboxes—they don't change Main Org until implemented in the real world

### Forecast

* **"Why is my headcount zero in future months?"** → Positions need hire dates to appear in future periods
* **"How do I see monthly projections?"** → Forecast → Select "Monthly" time period → Choose year
* **"What's 'Show Before' vs 'Show After'?"** → Before = Main Org (current state), After = Scenario final state

### Data & Import

* **"What format should my CSV be?"** → [Data Requirements](../data-import/data-requirements.md)
* **"How often should I refresh data?"** → Weekly or bi-weekly for most organizations
* **"Can I upload partial data?"** → Yes, partial uploads update specific fields without replacing all data

### Permissions

* **"Who can create scenarios?"** → Depends on your admin's access control settings—typically all users or specific user groups
* **"Who can see my scenario?"** → Users with access to the org areas included in your scenario
* **"How do I become an admin?"** → An existing admin must grant you admin privileges

***

## FAQ Categories

### [Getting Started FAQs](getting-started.md)

First-time user questions:

* Logging in and navigation
* Understanding basic concepts
* First 30 minutes in Agentnoon
* Common confusion for new users

### [Data & Import FAQs](data-import.md)

Data management questions:

* CSV format requirements
* Field mapping
* Validation errors
* Data refresh timing
* Live integrations

### [Scenarios FAQs](scenarios.md)

Scenario planning questions:

* Creating and editing scenarios
* Making position changes
* Submitting for approval
* Scenario management
* Best practices

### [Forecast FAQs](forecast.md)

Forecasting questions:

* Understanding time periods
* Hire dates and effective dates
* Headcount vs. cost views
* Exporting forecast data
* Multi-year planning

### [Permissions & Access FAQs](permissions-access.md)

Access control questions:

* User roles and permissions
* Access groups
* Admin capabilities
* Data visibility
* Security

***

## Tips for Finding Answers Quickly

### Use the Search Function

Press `Cmd + F` (Mac) or `Ctrl + F` (Windows) to search the current page for keywords.

**Example searches:**

* "hire date" → Find questions about hire dates
* "approval" → Find questions about scenario approvals
* "CSV" → Find questions about data uploads

### Start with the Category

Know the general topic? Go directly to the category page:

* New to Agentnoon? → [Getting Started FAQs](getting-started.md)
* Data issues? → [Data & Import FAQs](data-import.md)
* Planning changes? → [Scenarios FAQs](scenarios.md)

### Check Related Documentation

Each FAQ links to detailed documentation pages. If the short answer isn't enough, click through for the full guide.

***

## Still Need Help?

### Troubleshooting Guides

If you're experiencing a specific issue, check the troubleshooting guides:

* [Login & Access Issues](../troubleshooting/login-access-issues.md)
* [Data Issues](../troubleshooting/data-issues.md)
* [Scenario Issues](../troubleshooting/scenario-issues.md)
* [Performance Issues](../troubleshooting/performance-issues.md)
* [Export & Integration Issues](../troubleshooting/export-integration-issues.md)

### Contact Support

Can't find your answer? Reach out to Agentnoon support:

* **Email:** [SupportSWP@dayforce.com](mailto:SupportSWP@dayforce.com)
* **In-app chat:** Click the support icon in the bottom-right corner
* **Support hours:** Monday-Friday, 9am-5pm PT

**See:** [Support & How to Self-Help](../start-here/support-self-help.md)

***

## Contributing FAQ Suggestions

Have a question that's not answered here? Let us know!

* Email your question to [docs@agentnoon.com](mailto:docs@agentnoon.com)
* Suggest it to your Agentnoon customer success manager
* We regularly update FAQs based on user feedback

***

## Next Steps

* [**Getting Started FAQs**](getting-started.md) - New user questions
* [**Data & Import FAQs**](data-import.md) - Data management questions
* [**Scenarios FAQs**](scenarios.md) - Scenario planning questions
* [**Forecast FAQs**](forecast.md) - Forecasting questions
* [**Permissions & Access FAQs**](permissions-access.md) - Access control questions
