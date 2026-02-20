---
description: Practical examples of access group configurations
hidden: true
---

# TBD Access Groups Examples

> **Note: This page is in progress. Content coming soon!**

This page will provide practical, real-world examples of how to configure access groups for common organizational scenarios.

## Planned Content Outline

### View Budget Without Edit Access
**Use case:** Finance team needs to see compensation data for analysis but shouldn't be able to make changes.

**Configuration:**
- Access group: "Finance Analysts - View Only"
- Permissions: View all data including budget/compensation fields
- Restrictions: No edit access, no scenario creation
- Fields visible: All compensation, cost, budget fields
- Actions allowed: Export, filter, analyze
- Actions blocked: Edit positions, create scenarios, approve scenarios

### Department-Specific Access
**Use case:** Department heads should only see their own department's data.

**Configuration:**
- Access group: "Department Head - Engineering"
- Scope: Department filter = "Engineering"
- Permissions: Full edit access within Engineering only
- Can create scenarios affecting only Engineering
- Cannot see compensation data outside Engineering

### Executive View (All Data, No Restrictions)
**Use case:** C-suite needs full visibility across all data and scenarios.

**Configuration:**
- Access group: "Executives"
- Permissions: View all, edit all, approve all
- No department or field restrictions
- Can access all scenarios
- Can export all data

### HR Business Partner (Regional)
**Use case:** HRBP needs full access to specific geographic region.

**Configuration:**
- Access group: "HRBP - North America"
- Scope: Location filter = "USA, Canada, Mexico"
- Permissions: View and edit all positions in region
- Can create scenarios for region
- Can view compensation data
- Cannot approve scenarios

### External Consultant (Limited View)
**Use case:** Consultant needs to analyze org structure but shouldn't see names or compensation.

**Configuration:**
- Access group: "Consultant - Org Design"
- Permissions: View organizational structure
- Restrictions: Hide employee names, hide compensation fields
- Can view titles, departments, reporting structure
- Cannot create or edit scenarios
- Can export anonymized org charts

### Scenario Reviewer (Approval Role)
**Use case:** Manager needs to review and approve scenarios but not create them.

**Configuration:**
- Access group: "Scenario Approvers"
- Permissions: View all scenarios, approve/reject scenarios
- Can comment on scenarios
- Cannot create new scenarios
- Cannot edit positions in scenarios
- Can view change tracker and cost impact

### Read-Only Stakeholder
**Use case:** Board member needs periodic visibility without access to make changes.

**Configuration:**
- Access group: "Board - View Only"
- Permissions: View Main Org and approved scenarios
- Cannot see draft/in-progress scenarios
- Can view summary metrics and analytics
- Cannot export detailed data
- No edit or creation permissions

### Recruiter (Hiring Access)
**Use case:** Recruiting team needs to see open positions and create new positions.

**Configuration:**
- Access group: "Recruiting Team"
- Permissions: View all open/unfilled positions
- Can create new positions in scenarios
- Cannot close or modify existing filled positions
- Can see hiring budgets and compensation ranges
- Limited export permissions

---

## Additional Examples Needed

If you have specific access control scenarios that aren't covered above, we'd like to include them. Common scenarios we're still documenting:

- Multi-entity organizations (separate legal entities)
- Matrix organizations (dual reporting)
- Project-based access (temporary scenario access)
- Merger & acquisition access (acquired company limited access)
- Compliance/audit access (read-only with full historical data)

---

For immediate assistance with access control configuration, please contact [support@agentnoon.com](mailto:support@agentnoon.com) or refer to:
- [Access Control Overview](access-control/overview.md)
- [Access Groups](access-control/access-groups.md)
- [Support & How to Self-Help](../start-here/support-self-help.md)
