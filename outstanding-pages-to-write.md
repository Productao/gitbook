# Outstanding Pages to Write

This document tracks all documentation pages that are hidden, incomplete, or placeholder-only. Each entry includes the page's purpose and a content outline to guide writing.

**Total pages remaining:** 15

**Excluded from this list:**
- **Redirect/consolidated pages** (intentionally hidden, no content needed): `scenarios/comparison-exporting.md`, `scenarios/tracking-analysis.md`, `scenarios/change-tracker.md`, `main-org/taskbar.md`, `directory/exporting.md`, `start-here/calculated-agentnoon-attributes.md`, `forecast/budget-planning-tracking.md`
- **Duplicate/archive files** in `archive/`, `original-docs-backup/`, `org-chart/copy-of-span-of-control-metrics.md`, `settings/copy-of-fields.md`, `settings/metrics.md`, `admin/access-control/updating-login-method.md` (the live version at `access-control/updating-login-method.md` is complete and visible)
- **Internal docs** (not user-facing): `REVIEW_GUIDE.md`, `docs-mapping.md`, `CONTEXT.md`, `SESSION_SUMMARY_FEB18.md`, `SESSION_SUMMARY_FEB18_PART2.md`, `additional-context-needs-consolidated.md`
- **Draft that was superseded**: `approvals/approvals-draft.md` (the live version at `scenarios/approvals.md` is already in SUMMARY.md)

---

## Scenario Refresh

**File:** `scenarios/refresh.md`
**Status:** TBD (hidden)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Explains how to update an existing scenario with the latest Main Org data so that planners can keep scenarios current without recreating them from scratch. For scenario owners and workforce planners.

### Content Outline

1. **What scenario refresh does** — pulls updated Main Org data (new hires, terminations, re-orgs) into an existing scenario while preserving the planner's scenario-specific changes
2. **When to refresh vs. create a new scenario** — refresh when the scenario is still in progress and Main Org has changed; create new when starting over or when changes are too extensive
3. **Prerequisites before refreshing** — confirm Main Org data is up to date, communicate with collaborators, consider saving a duplicate as backup
4. **Step-by-step: performing a scenario refresh** — navigate to scenario settings or the refresh button, confirm the action, wait for processing
5. **How conflicts are handled** — what happens when a position was deleted in Main Org but modified in the scenario, or when an employee transferred departments
6. **Reviewing refresh impact** — reviewing the before/after comparison to ensure your scenario changes were preserved correctly
7. **What is preserved and what is overwritten** — scenario additions/deletions/edits stay; baseline data (titles, salaries, reporting lines from Main Org) updates
8. **Limitations and known issues** — scenarios with very large change sets may take longer; certain edge cases (e.g., merged positions) may need manual review
9. **Alternatives to refresh** — creating a new scenario from updated Main Org, duplicating and re-applying changes manually
10. **Best practices** — refresh before major planning sessions, refresh after quarterly data imports, always review the change summary

### Notes
- This is a feature that users frequently ask about. Needs input from the product team on exact conflict resolution behavior.
- Related to `admin/data-refresh-sync.md` (which covers the admin-side data refresh from HRIS).

---

## Projects

**File:** `scenarios/projects.md`
**Status:** TBD (not hidden, but title prefixed with TBD)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Explains how to use the Projects feature to split large org datasets into manageable segments for enterprise customers with 50,000+ records. For admins and enterprise workforce planners.

### Content Outline

1. **What Projects are and who needs them** — Projects create sub-instances of your Main Org, scoped to a business unit, region, or division; primarily for organizations with very large datasets
2. **When to use Projects vs. just using scenarios** — Projects for ongoing data segmentation and access control; scenarios for modeling changes within a dataset
3. **Creating a new Project** — navigate to Home Page > Create New Project, name it, select data scope (department, location, or custom filter), invite members
4. **Choosing which data to include** — filtering criteria for scoping the Project (by department hierarchy, location, cost center, etc.)
5. **Inviting members and setting access** — adding team members to a Project with appropriate permissions; members only see data within the Project scope
6. **Working within a Project** — the Project tile appears on the home page; scenarios created inside a Project use the Project org chart as baseline (non-editable)
7. **Projects vs. Main Org relationship** — Projects inherit from Main Org but do not push changes back; Main Org data refreshes flow into Projects
8. **Managing and editing Projects** — renaming, updating scope, adding/removing members, archiving Projects
9. **Limitations** — scenarios in a Project cannot span outside the Project scope; cross-project comparisons are not supported
10. **Best practices for enterprise use** — one Project per major business unit, align Projects to your HRBP assignments, review Project scopes quarterly

### Notes
- The existing page has substantial content with screenshots already. Primarily needs the TBD prefix removed, hidden flag added, and content polished/verified against current product behavior.
- User previously noted this is a "confusing concept" — the page should clearly distinguish Projects from scenarios and explain when each is appropriate.

---

## Project Creation

**File:** `scenarios/project-creation.md`
**Status:** TBD (title prefixed with TBD)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Step-by-step guide specifically for creating a new Project. Could potentially be merged into `scenarios/projects.md` rather than kept as a separate page. For admins setting up Projects for the first time.

### Content Outline

1. **Navigate to the Home Page** — locate the "Create New Project" button at the top right
2. **Name your Project** — choose a descriptive name (e.g., "North America Engineering")
3. **Choose data to include** — select the org data subset using department, location, or other filters
4. **Invite members** — add users who need access to this Project and assign roles
5. **Review and create** — confirm settings and create the Project
6. **Verify Project appears on Home Page** — the new Project tile should be visible
7. **Create your first scenario within the Project** — start planning using the Project baseline

### Notes
- This page has good existing content with screenshots. Consider merging into `scenarios/projects.md` as a "How to Create" section rather than maintaining as a separate page.
- Has screenshots that reference the current UI and should be verified for accuracy.

---

## Platform Notifications (Admin Reference)

**File:** `admin/notifications.md`
**Status:** TBD (hidden)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Comprehensive reference of all platform notifications — what triggers each one, who receives it, and delivery method. For admins who need to understand and explain the notification system to their organization. Distinct from `scenarios/collaboration/notifications.md` which is the end-user-facing page already written.

### Content Outline

1. **Notification delivery channels** — in-app (bell icon) vs. email; which events use which channel
2. **Approval workflow notifications** — request received, approved, rejected, workflow complete, request canceled; who gets each notification at each stage
3. **Scenario sharing & collaboration notifications** — shared with you, invitation accepted, new collaborator joined
4. **Data & system notifications** — data import complete/failed, live data refresh complete, system maintenance announcements
5. **Account & access notifications** — new user account created, access level changed, invitation sent/accepted
6. **What does NOT generate notifications** — scenario edits by collaborators, comments, presence changes (important to set expectations)
7. **Managing notification preferences** — where to find notification settings (if configurable), email opt-out options
8. **Notification frequency and timing** — real-time vs. batched, any digest options
9. **Admin controls over notifications** — can admins disable certain notifications org-wide, configure notification routing
10. **Troubleshooting notification delivery** — emails going to spam, delays, missing notifications

### Notes
- The existing planned content outline is thorough. Some of this content may overlap with `scenarios/collaboration/notifications.md` — consider whether this should be a separate admin-focused reference or merged.
- Needs product team input on the full notification catalog and whether notification preferences are configurable.

---

## Technical Overview

**File:** `technical-documentation/technical-overview.md`
**Status:** IPR (hidden)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Provides IT and security teams with an architectural overview of the Agentnoon platform for procurement, compliance, and integration decisions. For IT admins, security teams, and technical evaluators.

### Content Outline

1. **Platform architecture summary** — SaaS application, cloud-hosted, multi-tenant architecture with data isolation
2. **Cloud infrastructure and hosting** — cloud provider(s), hosting regions, data residency options
3. **Data storage and encryption** — encryption at rest and in transit, database architecture, backup and retention policies
4. **Security certifications and compliance** — SOC 2, GDPR, any other certifications; link to Data Security & Privacy page for full details
5. **Authentication and access control** — SSO/SAML, MFA, role-based access; link to Authentication & IAM section
6. **API and integration capabilities** — REST API, SFTP, Workday connector; rate limits, authentication methods; link to Live Data Refresh section
7. **Browser and device compatibility** — supported browsers (Chrome, Edge, Firefox, Safari), minimum versions, mobile support status
8. **Network requirements** — required domains/IPs to whitelist, bandwidth recommendations; link to Whitelisting page
9. **Scalability and performance** — supported org sizes (tested up to X employees), concurrent user limits, typical response times
10. **SLA, uptime, and disaster recovery** — uptime commitment, RTO/RPO targets, incident communication process

### Notes
- This page needs significant input from the Agentnoon DevOps/engineering team. Much of it overlaps with the Data Security & Privacy page which is already complete.
- Consider whether this should be a concise "Technical FAQ for IT Teams" or a full architecture document.

---

## Authentication Best Practices

**File:** `authentication-and-identity-security/best-practices.md`
**Status:** Hidden (empty stub)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Security best practices for configuring authentication in Agentnoon — helping IT admins choose and implement the right auth strategy. For IT admins and security teams.

### Content Outline

1. **Choose SSO over email/password** — why SSO (Okta, Azure AD, Google) is recommended for enterprise deployments; reduces credential sprawl
2. **Enable MFA for all users** — how to enable MFA org-wide, which MFA methods are supported (authenticator app, etc.)
3. **Configure role-based access from day one** — set up access groups before inviting users, principle of least privilege
4. **Regularly audit user access** — quarterly review of who has access, remove departed employees, review access levels
5. **Use dedicated service accounts for integrations** — separate accounts for SFTP/API integrations, not tied to individual users
6. **IP whitelisting for additional security** — restrict Agentnoon access to corporate network/VPN; link to Whitelisting page
7. **Password policies (for email/password auth)** — minimum complexity, rotation recommendations, what Agentnoon enforces
8. **Session management** — session timeout settings, forced re-authentication for sensitive actions
9. **Incident response** — what to do if credentials are compromised, how to force password resets, how to revoke access
10. **Compliance considerations** — GDPR data access requirements, SOC 2 alignment, audit logging

### Notes
- This page is currently a completely empty stub (just frontmatter and a title). All content needs to be written.
- Should reference and link to the existing SSO, MFA, and Whitelisting pages in the same section.

---

## Troubleshooting Authentication Issues

**File:** `authentication-and-identity-security/troubleshooting-authentication-issues.md`
**Status:** Hidden (empty stub)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Practical troubleshooting guide for common login and authentication problems. For end users and IT admins resolving access issues.

### Content Outline

1. **"I can't log in with SSO"** — verify SSO is configured for your org, check with IT admin, try incognito browser, clear cookies
2. **"I get a 'user not found' error"** — account may not be provisioned yet, email mismatch between SSO provider and Agentnoon, contact admin
3. **"MFA code is not working"** — time sync issues on authenticator app, use backup codes, request admin MFA reset
4. **"I'm locked out of my account"** — too many failed attempts, wait period, contact admin for unlock
5. **"I changed my email and can't log in"** — email changes require admin update in Agentnoon, steps to request re-linking
6. **"SSO login redirects but doesn't complete"** — browser popup blocked, third-party cookies disabled, firewall blocking redirect
7. **"I can log in but see no data"** — access group may not be assigned, admin needs to add you to appropriate access group
8. **"Session keeps expiring"** — expected behavior for security, check session timeout settings, VPN disconnection can cause re-auth
9. **Switching authentication methods** — link to Updating Login Method page for step-by-step instructions
10. **Escalation path** — when to contact Agentnoon support vs. your IT admin, what information to provide in a support ticket

### Notes
- This page is currently a completely empty stub. All content needs to be written.
- Consider consolidating some of this with `troubleshooting/login-access-issues.md` if that page has overlapping content. Check for duplication.

---

## Building an Annual Hiring Plan

**File:** `use-case-tutorials/annual-hiring-plan.md`
**Status:** IPR (hidden)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** End-to-end tutorial walking through how to use Agentnoon to build an annual hiring plan — from setting targets to getting approval. For HR leaders, workforce planners, and department heads doing annual planning.

### Content Outline

1. **Start with your hiring targets** — gather headcount requests from department heads, define budget constraints, establish timeline (Q1-Q4)
2. **Create a dedicated hiring plan scenario** — use Full Org Copy, name it descriptively (e.g., "FY2027 Hiring Plan - Draft 1")
3. **Add new positions by department** — use Add Position for each planned hire, set title, department, level, and target hire date
4. **Apply compensation using rate cards** — assign rate cards to new positions for consistent salary banding; use location-specific rates for distributed teams
5. **Set effective dates for phased hiring** — spread hire dates across quarters to model ramp-up; use Time-Based Planning view to verify timing
6. **Review budget impact in OpEx Panel** — check total cost impact, filter by department, compare current vs. planned headcount cost
7. **Use Forecast view for time-based projections** — switch to Forecast, set yearly aggregation, review headcount and cost curves over time
8. **Create alternative scenarios** — duplicate the scenario, create conservative/moderate/aggressive versions with different headcount numbers
9. **Compare scenarios side-by-side** — use Scenario Comparisons to present options to leadership with cost/headcount differences
10. **Submit for approval and export** — submit via approval workflow, export final plan as CSV/PowerPoint for implementation

### Notes
- The existing planned outline is solid. This tutorial should reference specific Agentnoon features (OpEx Panel, Forecast, rate cards) and link to their respective documentation pages.
- Consider including a "Prerequisites" section listing what data needs to be in place (rate cards configured, Main Org data current).

---

## Modeling Budget Cuts

**File:** `use-case-tutorials/modeling-budget-cuts.md`
**Status:** IPR (hidden)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Step-by-step tutorial for modeling workforce reductions and budget cuts using scenarios. For HR leaders and finance partners managing cost reduction initiatives.

### Content Outline

1. **Define the target** — determine the savings goal (e.g., reduce OpEx by $2M or reduce headcount by 15%), clarify timeline
2. **Create a budget reduction scenario** — duplicate from Main Org, name clearly (e.g., "Q3 2026 Cost Reduction - Option A")
3. **Identify high-cost positions using Directory** — sort by compensation, filter by department/level, export candidate lists for analysis
4. **Model position closures** — use Close Position (with or without RIF designation) for each reduction; set effective dates if phased
5. **Use bulk operations for larger reductions** — select multiple positions via Directory checkboxes, apply bulk close
6. **Review cost impact in OpEx Panel** — verify savings total matches target, review by department to ensure proportional distribution
7. **Evaluate org structure impact** — check span of control changes, identify teams that drop below critical mass, review layers impact
8. **Create multiple options** — duplicate scenario for Option B and C with different approaches (e.g., across-the-board vs. targeted by department)
9. **Compare options for leadership** — use Scenario Comparisons to show cost savings, headcount delta, and org structure differences across options
10. **Submit and export approved plan** — route through approval workflow, export final plan for HR implementation

### Notes
- Sensitive topic — the tone should be professional and neutral, avoiding casual language around layoffs/RIFs.
- Should link to: OpEx Panel, Bulk Operations, Scenario Comparisons, Exporting Scenario Data.

---

## Compensation Planning

**File:** `use-case-tutorials/compensation-planning.md`
**Status:** IPR (hidden)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Tutorial for using Agentnoon to model compensation changes across an organization — merit increases, promotions, and equity adjustments. For HR compensation teams and finance partners.

### Content Outline

1. **Gather compensation review inputs** — merit budget percentage, promotion pool, equity adjustment targets, market data
2. **Set up rate cards for salary bands** — configure rate cards with min/mid/max for each level/location; link to Rate Cards documentation
3. **Create a compensation planning scenario** — Full Org Copy, name it (e.g., "FY2027 Merit Cycle - Draft")
4. **Model merit increases** — edit salary fields on individual positions, or use bulk operations to apply percentage increases by department/level
5. **Model promotions and title changes** — change title and level fields, apply new salary band from rate card, set effective dates
6. **Identify and fix compression issues** — sort by salary within same level/department, find cases where new hires earn more than tenured employees, model adjustments
7. **Review total compensation impact** — use OpEx Panel to see aggregate cost change, filter by formula (Salary, Total Employer Cost) to see different views
8. **Compare conservative vs. generous scenarios** — create multiple versions with different merit percentages (e.g., 3% vs. 4% vs. 5%)
9. **Department-level budget allocation** — use Directory filtering to review comp changes by department, ensure each stays within allocated budget
10. **Submit for approval and export** — route through comp committee approval, export for payroll implementation

### Notes
- Depends on rate cards being configured. Should include a "Prerequisites" section.
- Link to: Rate Cards/Compensation Bands, Bulk Operations, OpEx Panel, Scenario Comparisons.

---

## Succession Planning

**File:** `use-case-tutorials/succession-planning.md`
**Status:** IPR (hidden)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Tutorial for using Agentnoon to model internal succession and leadership transition plans. For HR business partners and talent management teams.

### Content Outline

1. **Identify critical roles** — determine which positions need succession plans (C-suite, VP+, hard-to-fill roles, single points of failure)
2. **Create a succession planning scenario** — Full Org Copy, name it (e.g., "Succession Plan - CFO Transition")
3. **Model the departure** — close or vacate the departing leader's position, set an effective date for the transition
4. **Evaluate internal candidates** — review the org chart for potential successors, assess their current level, reporting line, and readiness
5. **Model the promotion path** — move the selected successor into the role, update title/level/compensation, set effective date
6. **Plan the backfill chain** — the successor's old position now needs filling; model whether to promote from within (creating another backfill) or hire externally
7. **Assess org structure impact** — review span of control changes, check whether the promotion creates reporting line issues, verify no team is left without leadership
8. **Compare multiple succession paths** — create scenario variants for different internal candidates and an external hire option
9. **Use Workforce Hub for talent analysis** — review demographic, tenure, and level distribution to identify bench strength
10. **Document and share the plan** — export the scenario as a PowerPoint for board/exec review, add comments to positions noting succession rationale

### Notes
- Agentnoon may not have dedicated "succession planning" features — this tutorial should show how to use existing scenario tools (position changes, effective dates, comparisons) to achieve succession planning outcomes.
- Link to: Making Position Changes, Working with People, Scenario Comparisons, Hub overview.

---

## Multi-Year Planning

**File:** `forecast/multi-year-planning.md`
**Status:** Hidden (has substantial content)
**Currently in SUMMARY.md sidebar:** Yes
**Purpose:** Guide to projecting workforce headcount and costs over 3-5 years using the Forecast module. For strategic workforce planners and finance partners doing long-range planning.

### Content Outline

1. **Setting up a multi-year scenario** — create a scenario with positions spread across future years using hire dates (content exists)
2. **Viewing multi-year projections in Forecast** — set Time Period to Yearly, choose aggregation dimension, toggle headcount vs. cost (content exists)
3. **Modeling uncertainty with multiple scenarios** — conservative/moderate/aggressive growth assumptions; compare side-by-side (content exists)
4. **Planning detail by time horizon** — Year 1 high detail, Year 2 moderate, Year 3+ directional only (content exists)
5. **Modeling salary inflation** — using effective dates to apply future raises; limitations of manual salary updates (content exists)
6. **Geographic cost planning** — location-specific rate cards for multi-region workforce expansion (content exists)
7. **Rolling forecast updates** — quarterly refresh process: update Main Org, create new scenario version, adjust projections (content exists)
8. **Presenting multi-year plans to leadership** — export strategies, what to include in executive presentations
9. **Common pitfalls** — over-precision in Year 3+ estimates, not accounting for attrition, ignoring contractor/contingent workforce
10. **Related resources and next steps** — links to Forecast Overview, Building Headcount Forecasts, Annual Hiring Plan tutorial

### Notes
- This page already has substantial, well-written content covering items 1-7 above. It mainly needs: the `hidden: true` flag removed, minor polish, and possibly items 8-9 added.
- Currently referenced in SUMMARY.md sidebar. If the content is accurate, this may just need review and unhiding rather than a full rewrite.

---

## Summary View

**File:** `summary-view.md`
**Status:** Hidden (has substantial content)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Explains the Summary View feature that provides a financial overview of scenario changes. This appears to be a legacy/deprecated feature or may have been folded into the OpEx Panel documentation.

### Content Outline

1. **Total financial overview** — Current Headcount Cost, Sum of Position Changes, Placeholder Adjustments, New Headcount Cost, Remaining Budget (content exists)
2. **Viewing changes by activity type** — Additions, RIF/Exits, Changes, Moved categories (content exists)
3. **Filtering impact by custom formula** — selecting different formulas (Salary, Total Employer Cost, Severance) from the dropdown (content exists)
4. **Using Summary View for budget tracking** — comparing planned vs. remaining budget at a glance
5. **Summary View vs. OpEx Panel** — clarify the relationship between these two views, whether Summary View is a subset of OpEx Panel or a separate feature

### Notes
- This page has real content with feature descriptions. It may have been superseded by or consolidated into the OpEx Panel (`scenarios/opex-panel.md`). Verify with the product team whether Summary View is still a distinct feature.
- If Summary View is the same as OpEx Panel, this page should be converted to a redirect rather than written as a standalone page.

---

## Access Groups Examples

**File:** `admin/access-groups-examples.md`
**Status:** TBD (hidden)
**Currently in SUMMARY.md sidebar:** Yes
**Purpose:** Real-world configuration examples for access groups covering common enterprise scenarios. For admins setting up role-based access for the first time or expanding access controls.

### Content Outline

1. **Finance Analyst (view-only with budget visibility)** — can see all compensation data, cannot edit, cannot create scenarios (content exists)
2. **Department Head (scoped to own department)** — full edit within department, cannot see other departments' compensation (content exists)
3. **Executive (unrestricted access)** — view all, edit all, approve all, no restrictions (content exists)
4. **HR Business Partner (regional scope)** — full access to specific geographic region, can create scenarios for region (content exists)
5. **External Consultant (anonymized view)** — org structure only, no names or compensation, cannot edit (content exists)
6. **Scenario Approver (review and approve only)** — can approve/reject, can comment, cannot create or edit (content exists)
7. **Board Member (read-only stakeholder)** — view Main Org and approved scenarios, no exports of detailed data (content exists)
8. **Recruiter (hiring-focused access)** — view open positions, create new positions in scenarios, limited export (content exists)
9. **Setting up your first access group** — step-by-step walkthrough linking to the Access Groups documentation page
10. **Common mistakes to avoid** — overly broad permissions, forgetting to restrict compensation fields, not testing access groups before rollout

### Notes
- This page already has substantial content with 8 detailed examples. It mainly needs: the TBD prefix removed, `hidden: true` removed, and verification that the configuration options described match current product capabilities.
- Currently in SUMMARY.md sidebar. May be close to publication-ready after product review.

---

## Approvals Draft

**File:** `approvals/approvals-draft.md`
**Status:** Hidden (has content with screenshots)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** Draft documentation for the approval workflow feature. This appears to be an earlier draft of the approvals content; verify whether `scenarios/approvals.md` (which IS in SUMMARY.md) has superseded this entirely.

### Content Outline

1. **Setting up approvals** — click Configure Approvals, assign two levels of approvers (content exists with screenshots)
2. **Two-level approval structure** — first-level and second-level approvers; scenario creator defines who approves (content exists)
3. **Locking a scenario after submission** — optional lock to prevent edits during review (content exists)
4. **Approving a scenario** — approvers review but cannot edit; both levels must approve (content exists)
5. **Approval notifications** — approvers receive email/in-app notifications when assigned
6. **Rejecting or requesting changes** — what happens when an approver rejects, how to resubmit
7. **Approval history and audit trail** — viewing who approved, when, and any comments
8. **Configuring approval flows (admin)** — link to admin configuration page

### Notes
- This draft has screenshots and real content but was likely superseded by `scenarios/approvals.md`. Check if `scenarios/approvals.md` is complete. If so, convert this to a redirect or delete it.
- The screenshots may be valuable to reuse in the live approvals page if they aren't already there.

---

## Scenario Project Creation (Duplicate Check)

**File:** `scenarios/project-creation.md`
**Status:** TBD (title prefixed, not marked hidden)
**Currently in SUMMARY.md sidebar:** No
**Purpose:** This appears to be a duplicate/alternate version of `scenarios/projects.md`. Both cover Project creation. Decision needed on whether to merge or keep separate.

### Notes
- See the entry for `scenarios/projects.md` above. These two files should likely be merged into a single comprehensive Projects page.
- `project-creation.md` has more step-by-step content with screenshots; `projects.md` is a shorter stub. Consider using `project-creation.md` as the base.

---

## Summary by Status

| Status | Count | Pages |
|--------|-------|-------|
| **TBD (placeholder only)** | 4 | Scenario Refresh, Platform Notifications, Projects, Access Groups Examples |
| **IPR (in progress)** | 5 | Technical Overview, Annual Hiring Plan, Modeling Budget Cuts, Compensation Planning, Succession Planning |
| **Hidden with content** | 4 | Multi-Year Planning, Summary View, Approvals Draft, Project Creation |
| **Hidden empty stub** | 2 | Authentication Best Practices, Troubleshooting Authentication Issues |
| **Total** | **15** | |

## Priority Recommendations

### Ready for review and unhiding (minimal work)
1. **Multi-Year Planning** — content is substantial and well-written; needs product review and `hidden: true` removed
2. **Access Groups Examples** — 8 detailed examples already written; needs product verification and TBD prefix removed

### Needs content written from outline (moderate work)
3. **Scenario Refresh** — clear outline exists, needs product input on conflict resolution behavior
4. **Platform Notifications** — detailed outline exists, needs product input on full notification catalog
5. **Building an Annual Hiring Plan** — outline exists, can be written using existing feature documentation as reference
6. **Modeling Budget Cuts** — outline exists, can be written using existing feature docs
7. **Compensation Planning** — outline exists, requires rate cards feature knowledge
8. **Succession Planning** — outline exists, can be written as a "how to use existing features" tutorial

### Needs significant input from engineering/product (heavy work)
9. **Technical Overview** — requires architecture details from engineering team
10. **Authentication Best Practices** — empty stub, needs security team input
11. **Troubleshooting Authentication Issues** — empty stub, needs support team input on common issues

### Needs decision (merge/archive)
12. **Summary View** — may be deprecated or consolidated into OpEx Panel; verify with product
13. **Approvals Draft** — may be superseded by `scenarios/approvals.md`; verify and merge or archive
14. **Projects** — merge with Project Creation into single page
15. **Project Creation** — merge into Projects page
