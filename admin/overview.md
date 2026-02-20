---
description: Administrative capabilities and configuration overview
hidden: false
---

# Admin Overview

Admins in Agentnoon have elevated permissions to configure the platform, manage users, and maintain data integrity. This guide covers everything admins need to know to effectively manage their Agentnoon instance.

## What is an Admin?

**Admins** are power users with special permissions to configure and maintain Agentnoon for their organization. Unlike regular users who primarily view data and create scenarios, admins control the underlying system configuration.

**Who becomes an admin:**
- Initial admins are set up during customer onboarding
- Existing admins can grant admin privileges to other users
- Agentnoon (as the vendor) has super-admin access for support purposes (not documented for end users)

---

## Admin vs Regular User Permissions

### What Regular Users Can Do:
- View Main Org
- Create and edit scenarios (with appropriate permissions)
- View Workforce Hub analytics
- Use Forecast to analyze data
- Export data they have access to
- Submit scenarios for approval

### What Only Admins Can Do:
- **User management:** Invite users, manage permissions, configure access groups
- **Data management:** Upload CSV files, configure live integrations, manage data refreshes
- **Field configuration:** Create custom fields, configure formulas, define metrics
- **System settings:** Configure approval workflows, set default views, customize colors
- **Rate card management:** Upload and configure compensation rate cards
- **Auto mapping:** Configure automatic field population rules
- **Access control:** Define who can see what data based on field values

---

## Core Admin Responsibilities

### 1. User Management & Access Control

**Managing users:**
- Invite new users via email
- Assign admin privileges to power users
- Deactivate users who leave the organization
- Reset passwords if needed

**Access control:**
- Create access groups to limit data visibility
- Configure field-level permissions (who can see/edit which fields)
- Set department or location-based access restrictions
- Define which users can create scenarios vs. view-only access

**Example:** Create an "HRBP North America" access group that only sees US and Canada employees.

### 2. Data Upload & Management

**CSV uploads:**
- Upload full org data files (replaces Main Org)
- Upload partial data (updates specific fields)
- Validate data before upload
- Troubleshoot data errors

**Live integrations:**
- Configure SFTP, Workday, or API integrations
- Set sync frequency
- Monitor integration health
- Handle sync failures

**Data transformation hub:**
- Upload additional CSV files to enrich main data
- Perform joins between data sources
- Download merged data for upload

### 3. Field & Attribute Configuration

**Managing fields:**
- Mark fields as employee fields vs position fields
- Set fields as mandatory for new positions
- Configure field visibility (hide sensitive fields)
- Enable auto-duplication for scenario copying
- Create field groups for organized editing panels

**Creating custom fields:**
- Add new attributes to track (e.g., "Criticality", "Succession Ready")
- Define field types (text, number, dropdown, date)
- Set dropdown values if applicable

**Formulas:**
- Create calculated fields based on other fields
- Examples: Fully loaded cost, Pay ratio, Custom org levels

### 4. Rate Card Configuration

**What rate cards do:**
- Auto-populate salaries when creating new positions
- Based on criteria like pay grade, job family, location
- Ensure consistent, market-aligned compensation

**Setup:**
- Upload rate card CSV file
- Map columns to Agentnoon fields
- Select compensation-determining columns (checkboxes)
- Choose which column maps to salary (or other comp fields)

**Important:** All rate card columns must exist as fields in Agentnoon first.

### 5. Metrics Configuration

**System-calculated metrics:**
- Span of Control (SOC)
- Manager cost ratio
- IC count and cost
- Total org size
- Average manager salary

**Customizing metrics:**
- Disable metrics you don't want visible
- Create custom metrics (e.g., SOC excluding seasonal workers)
- Define calculation rules

### 6. Approval Workflow Configuration

**Setting up approvals:**
- Define Level 1 approvers (first approval stage)
- Define Level 2 approvers (second approval stage)
- Enable "Lock scenarios upon submission" to prevent edits during approval
- Multiple Level 1 approvers possible (any one can approve)
- Level 0 and Level 3 approvers are scenario-specific (set per scenario)

**Approval flow:**
Level 0 (scenario-specific) → Level 1 (global) → Level 2 (global) → Level 3 (scenario-specific)

### 7. Other Admin Settings

**Colors:**
- Customize highlight colors for departments, locations, etc.
- Ensure colors align with company branding

**Default views:**
- Save views (filters + highlights + card content) as defaults
- Assign default views to specific users or scenarios
- Helps onboard new users with pre-configured views

**Organization roots:**
- Typically one CEO as root
- Configure multiple roots if needed (e.g., multiple business units)

**General settings:**
- SSO configuration
- Data sync preferences
- UI customization options

---

## Admin Onboarding Checklist

### First 30 Days

**Week 1: Setup & Familiarization**
- [ ] Complete Agentnoon admin training
- [ ] Review current data structure and fields
- [ ] Understand existing access control setup
- [ ] Test data upload process with sample file
- [ ] Explore Settings pages to understand all options

**Week 2: User Management**
- [ ] Invite key users (HR, Finance, Ops leaders)
- [ ] Create access groups for departments or regions
- [ ] Set up admin accounts for other power users
- [ ] Configure default views for different user types

**Week 3: Data & Configuration**
- [ ] Set up regular data refresh schedule
- [ ] Configure rate cards (if applicable)
- [ ] Set up auto mapping rules
- [ ] Create custom fields specific to organization needs

**Week 4: Approval & Finalization**
- [ ] Configure approval workflows (Level 1 & 2 approvers)
- [ ] Test scenario approval process end-to-end
- [ ] Document admin procedures for future reference
- [ ] Train power users on creating scenarios

---

## Ongoing Admin Maintenance

### Weekly Tasks
- Monitor data sync status (if using live integration)
- Review user access requests
- Address data error reports from users

### Monthly Tasks
- Review active users and deactivate former employees
- Update rate cards if compensation bands change
- Audit access groups for accuracy
- Check for new feature releases from Agentnoon

### Quarterly Tasks
- Refresh training for new users
- Review and optimize access control rules
- Update custom fields as business needs evolve
- Conduct admin best practices review

### Annual Tasks
- Major data cleanup (archive old scenarios, remove outdated fields)
- Comprehensive access audit
- Review and update approval workflows
- Renew or expand Agentnoon licenses

---

## Common Admin Workflows

### Onboarding a New User
1. Go to Settings → Users (or Access Control section)
2. Click "Invite User"
3. Enter email address
4. Assign access group (determines what data they see)
5. Set permissions (Viewer, Planner, Approver)
6. Send invitation
7. User receives email to set up account

### Uploading New Data
1. Export latest data from HRIS
2. Format CSV according to Agentnoon requirements
3. Go to Data Management → Upload
4. Select file
5. Map columns to Agentnoon fields (if first time)
6. Review validation errors (if any)
7. Confirm upload
8. Verify data in Main Org

### Creating a Custom Field
1. Go to Settings → Fields and Attributes (or Data Management in Main Org toolbar)
2. Click "Add Field"
3. Name the field (must match CSV column if importing data)
4. Set field type (text, number, dropdown, date)
5. Configure visibility, mandatory status, auto-duplication
6. Save
7. Field now available in card content, filters, exports

### Configuring an Access Group
1. Go to Settings → Access Control → Access Groups
2. Click "Create Access Group"
3. Name the group (e.g., "Engineering Leadership")
4. Set filters:
   - Department = Engineering (users in this group only see Engineering)
   - Or Location = San Francisco (users only see SF employees)
5. Assign users to the group
6. Save
7. Users now have filtered view automatically

---

## Security & Data Governance

### Best Practices
- **Principle of least privilege:** Only grant admin access to those who need it
- **Regular audits:** Review user access quarterly
- **Data privacy:** Use access groups to protect sensitive information
- **Field visibility:** Hide fields like SSN, personal addresses from non-admins
- **Password policies:** Enforce strong passwords (configured in SSO if applicable)

### Sensitive Data Handling
- Never commit .env files or credentials to the Agentnoon system
- Use access groups to restrict salary visibility
- Be cautious with export permissions (exports respect access groups)

---

## Getting Help

### As an Admin, When to Contact Support
- Integration failures or data sync issues
- System errors or bugs
- Feature requests or configuration questions
- User access issues you can't resolve
- Data migration assistance

### Self-Service Resources
- [Support & How to Self-Help](../start-here/support-self-help.md)
- [Data Import Requirements](../data-import/data-requirements.md)
- [Access Control Guide](../access-control/access-groups.md)
- [Rate Cards Setup](../settings/compensation-cards.md)

---

## Next Steps

- **[Configuring Approval Flows](configuring-approval-flows.md)** - Set up scenario approvals
- **[Data Refresh & Sync](data-refresh-sync.md)** - Manage data updates
- **[Access Groups](../access-control/access-groups.md)** - Control who sees what
- **[Fields and Attributes Management](../settings/fields.md)** - Configure custom fields
- **[Rate Cards](../settings/compensation-cards.md)** - Set up compensation automation
