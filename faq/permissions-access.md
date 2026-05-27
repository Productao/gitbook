---
description: User permissions and access control questions
---

# 🔑 Permissions & Access FAQs

Common questions about user roles, access groups, field-level permissions, and admin capabilities. Learn who can see what data and how access control works in Agentnoon.

## User Roles & Permissions

### What are the different permission levels in Agentnoon?

**Answer:** There are two main levels: Regular Users (can view Main Org, create scenarios, use Forecast and analytics) and Admins (can do everything regular users can, plus manage users, upload data, configure fields, set up integrations, and control system settings).

**Learn more:** [Admin Overview](../admin/overview.md)

### Who can create scenarios?

**Answer:** Regular users with edit access can create scenarios. View-only users cannot create or edit fields in scenarios. Admins can control who has scenario creation permissions through access group configurations.

**Learn more:** [Admin Overview](../admin/overview.md)

### Who can approve scenarios?

**Answer:** Approvers are configured by admins and typically include Level 1 and Level 2 approvers (global) plus Level 0 and Level 3 approvers (scenario-specific). Common approvers: department heads, finance leaders, HR leaders, or executives.

**Learn more:** [Admin Overview](../admin/overview.md)

### What's the difference between Viewer, Planner, and Approver roles?

**Answer:** Viewers can see Main Org and read-only data. Planners can create and edit scenarios. Approvers can review and approve submitted scenarios. The exact permissions for each role are configured by your admin and may vary by organization.

**Learn more:** [Admin Overview](../admin/overview.md)

## Access Groups

### What's an access group?

**Answer:** An access group controls what fields users can see and edit. Admins create access groups with scope (e.g., "Engineering department only" or "US locations only"), field-level permissions (view/edit/hidden), and feature access, then assign users to groups.

**Learn more:** [Access Groups](../access-control/access-groups.md)

### How do access groups restrict what I see?

**Answer:** Access groups use filters to limit visibility. For example, an "HRBP North America" access group might filter to only US and Canada employees, so users in that group only see those employees in Main Org, scenarios, and reports.

**Learn more:** [Access Groups](../access-control/access-groups.md)

### Can I see people outside my access group?

**Answer:** No. If your access group filters to your department, you cannot see employees in other departments. Contact your admin if you need broader access.

**Learn more:** [Access Groups](../access-control/access-groups.md)

### How do I know what I have permission to see?

**Answer:** Check with your admin for your access group assignment. Try filtering to "All" in Main Org—if certain departments don't appear, you likely have restricted access. Admins can show you exactly what filters apply to your access group.

**Learn more:** [Access Groups](../access-control/access-groups.md)

## Field-Level Permissions

### Can admins hide sensitive fields like salary from certain users?

**Answer:** Yes! Admins configure field-level permissions in access groups: View (users can see), Edit (users can modify in scenarios), or Hidden (users cannot see at all). Common use: hide compensation fields from non-HR users.

**Learn more:** [Access Groups](../access-control/access-groups.md)

### Why can't I see salary information?

**Answer:** Your access group likely has compensation fields set to Hidden. This is intentional for data privacy. Contact your admin if you need salary visibility for your role (e.g., you're an HRBP or finance lead).

**Learn more:** [Access Groups](../access-control/access-groups.md)

### Can I edit all fields I can see?

**Answer:** Not necessarily. Fields can have View access (you can see but not edit) or Edit access (you can modify in scenarios). Main Org is always view-only—you can only edit in scenarios, and only fields your access group permits.

**Learn more:** [Access Groups](../access-control/access-groups.md)

## Admin Permissions

### What can admins do that regular users can't?

**Answer:** Admins can invite and manage users, upload and refresh data, create and configure custom fields, set up live data integrations, create access groups, configure approval workflows, upload rate cards, and customize system settings like colors and default views.

**Learn more:** [Admin Overview](../admin/overview.md)

### How do I become an admin?

**Answer:** Existing admins grant admin privileges to other users. If you need admin access, ask your current admin or IT lead. Admins typically include HR systems managers, workforce planning leads, or IT administrators.

**Learn more:** [Admin Overview](../admin/overview.md)

### Can admins see all data regardless of access groups?

**Answer:** Yes. Admins usually have unrestricted access to see and manage all organizational data. This allows them to configure settings, troubleshoot issues, and manage the system effectively.

**Learn more:** [Admin Overview](../admin/overview.md)

### Who can upload or refresh data?

**Answer:** Only admins can upload CSV files, refresh Main Org data, or configure live integrations. Regular users cannot modify the underlying data source to ensure data integrity and single source of truth from your HRIS.

**Learn more:** [Admin Overview](../admin/overview.md)

## Sharing & Collaboration

### Do exports respect access group restrictions?

**Answer:** Yes. When you export data (CSV, org chart, reports), you can only export data your access group permits you to see. This ensures sensitive data doesn't leak through exports.

**Learn more:** [Admin Overview](../admin/overview.md)

### Can I see other users' scenarios?

**Answer:** Only if they explicitly share scenarios with you. By default, scenarios are private to their creator. Shared scenarios appear in your scenario list with a shared indicator.

**Learn more:** [Admin Overview](../admin/overview.md)

## Requesting Access Changes

### How do I request access to specific departments?

**Answer:** Contact your Agentnoon account admins. Explain what data you need access to and why (e.g., "I need to see Engineering for cross-functional planning"). Admins can add you to a different access group or create a custom one.

**Learn more:** [Access Groups](../access-control/access-groups.md)

### How do I request additional permissions?

**Answer:** Contact your admin and explain what permissions you need (scenario creation, approver role, field visibility, etc.) and why. Admins can modify your access group or assign you to a different one with appropriate permissions.

**Learn more:** [Admin Overview](../admin/overview.md)

### What if I need temporary access for a special project?

**Answer:** Ask your admin to temporarily add you to a broader access group or create a time-limited access group for the project. After the project, your admin can revert your access.

**Learn more:** [Access Groups](../access-control/access-groups.md)

## Security & Data Privacy

### How does Agentnoon protect sensitive employee data?

**Answer:** Agentnoon uses access groups to restrict field visibility, encrypted connections for data transfers, role-based permissions for system functions, and admin-only data upload permissions. Only users with appropriate access can see sensitive fields like salary or personal information.

**Learn more:** [Admin Overview](../admin/overview.md)

### Can I restrict access by location or country for compliance?

**Answer:** Yes! Admins create access groups filtered by location or country. For example, an "EMEA HRBP" access group can filter to only European employees, ensuring compliance with regional data privacy regulations.

**Learn more:** [Access Groups](../access-control/access-groups.md)

## Next Steps

* [Access Groups](../access-control/access-groups.md) - Complete access control guide
* [Admin Overview](../admin/overview.md) - Admin capabilities and responsibilities
* [Getting Started FAQs](getting-started.md) - New user questions
* [Data & Import FAQs](data-import.md) - Data management questions
* [Scenarios FAQs](scenarios.md) - Scenario planning questions
