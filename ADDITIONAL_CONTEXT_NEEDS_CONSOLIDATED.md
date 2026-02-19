# Additional Context Needs - Consolidated Documentation Requirements

**Date:** February 19, 2026
**Status:** 15 placeholder pages remaining (13 IPR/TBD + 2 hidden admin pages)
**Purpose:** Single comprehensive list of all additional context needed to complete documentation

---

## Executive Summary

**Current State:**
- **Total documentation pages:** ~87 articles
- **Completed pages:** ~72 articles (83%)
- **Remaining placeholders:** 15 articles (17%)

**Context Required:**
- **Can complete without additional context:** 0 pages (all easy pages completed)
- **Need specific product knowledge:** 15 pages

**Breakdown by category:**
- Use Case Tutorials: 4 pages
- Scenarios (Advanced Features): 4 pages
- Assets: 2 pages
- Technical Documentation: 2 pages
- Admin: 2 pages
- Forecast: 1 page (removed from count - see note below)

---

## Category 1: Use Case Tutorials (4 pages)

High-value practical guides that require detailed product workflows.

### 1. Modeling Budget Cuts (`use-case-tutorials/modeling-budget-cuts.md`)

**Current status:** IPR placeholder
**Priority:** HIGH - Users actively need this for RIF planning

**What's needed:**

1. **Workflow for identifying positions to cut:**
   - Q: Do users typically filter by salary (highest paid first)?
   - Q: Filter by department (cut from specific areas)?
   - Q: Filter by performance metrics or other criteria?
   - Q: Is there a "target savings calculator" feature?

2. **Bulk operations for closing positions:**
   - Q: Can you bulk-select positions in Directory and close them all at once?
   - Q: How do you set effective dates for bulk closures?
   - Q: Does the system warn about broken hierarchies before closing?

3. **Comparing multiple RIF scenarios:**
   - Q: What's typical workflow? (Create "RIF Option A", "RIF Option B", "RIF Option C"?)
   - Q: Can you compare scenarios side-by-side in UI or only via exports?
   - Q: Is there a comparison view specifically for this?

4. **Sensitive data handling:**
   - Q: Best practices for limiting access to RIF scenarios?
   - Q: Should documentation address privacy concerns?

5. **Post-RIF optimization:**
   - Q: Do users need to reassign reports to new managers after cuts?
   - Q: Any specific tools for "healing" the org chart after cuts?

**Suggested delivery:** Loom walkthrough or step-by-step written example of RIF scenario

---

### 2. Compensation Planning (`use-case-tutorials/compensation-planning.md`)

**Current status:** IPR placeholder
**Priority:** HIGH - Core use case for many customers

**What's needed:**

1. **Annual compensation review workflow:**
   - Q: How do users model merit increases? (3% across board? Different % by performance?)
   - Q: Can you bulk-apply salary increases by percentage?
   - Q: Or edit each position individually?

2. **Rate cards and salary bands:**
   - Q: How do rate cards integrate with compensation planning?
   - Q: If promoted, change pay grade → rate card auto-populates salary?
   - Q: Can you model "bringing everyone to midpoint of their band"?

3. **Equity and total compensation:**
   - Q: Does Agentnoon support equity compensation fields (RSUs, options)?
   - Q: Can you model equity refreshes or new grants?
   - Q: Is there a "total compensation" calculator?

4. **Compression analysis:**
   - Q: Is there a built-in "compression analysis" tool?
   - Q: Or export to Excel for analysis?
   - Q: What does "compression" mean in Agentnoon? (ICs making more than managers?)

5. **Budget allocation by department:**
   - Q: If $2M compensation budget, can you allocate "$500K to Eng, $300K to Sales"?
   - Q: Or just set total and track?

**Suggested delivery:** Example workflow with screenshots or Loom; clarify equity support, bulk operations, compression analysis

---

### 3. Succession Planning (`use-case-tutorials/succession-planning.md`)

**Current status:** IPR placeholder
**Priority:** MEDIUM - Important for enterprise customers

**What's needed:**

1. **Identifying critical roles:**
   - Q: How do users flag positions as "critical" or "key"?
   - Q: Is there a field/tag for this?

2. **Identifying potential successors:**
   - Q: Is there a "talent assessment" or "performance rating" field?
   - Q: How do users track "ready now" vs "ready in 1-2 years"?

3. **Modeling succession transitions:**
   - Q: Create scenario showing Person A promoted to Role X, Person B backfills Role A?
   - Q: Use effective dates to model timing?

4. **Succession depth analysis:**
   - Q: Can you see "how many successors exist for each critical role"?
   - Q: Any built-in succession depth metrics?

**Suggested delivery:** Example succession planning workflow; clarify if there are succession-specific fields or features

---

### 4. Annual Hiring Plan (`use-case-tutorials/annual-hiring-plan.md`)

**Current status:** IPR placeholder
**Priority:** HIGH - Annual planning season use case

**What's needed:**

1. **Planning new positions across quarters:**
   - Q: Create positions with future hire dates (Q1, Q2, Q3, Q4)?
   - Q: Use effective dates for phased hiring?

2. **Using Forecast view:**
   - Q: Does Forecast view show planned hires by quarter?
   - Q: Can you set quarterly headcount targets?

3. **Budget tracking:**
   - Q: Does system calculate cumulative cost by quarter?
   - Q: Can you set quarterly budget limits?

4. **Comparing hiring scenarios:**
   - Q: Create "Conservative Growth" vs "Aggressive Growth" scenarios?
   - Q: How to compare headcount/cost projections?

**Suggested delivery:** Step-by-step annual hiring plan example with Forecast view screenshots

---

## Category 2: Scenarios - Advanced Features (4 pages)

These are advanced scenario capabilities that need feature-specific documentation.

### 5. Scenario Refresh (`scenarios/refresh.md`)

**Current status:** TBD placeholder
**Priority:** HIGH - Frequently requested feature

**What's needed:**

1. **Current status:**
   - Q: Is scenario refresh available now, in beta, or planned?
   - Q: Where in UI do you access it?

2. **How it works:**
   - Q: Click "Refresh Scenario" → preview of changes → confirm?
   - Q: What happens to scenario data?
   - Q: Are scenario changes (additions, closures, moves) preserved or lost?

3. **Conflict resolution:**
   - Q: If position in scenario but not Main Org (employee left), what happens?
   - Q: If position in Main Org but not scenario (new hire), added automatically?
   - Q: Can you selectively choose which Main Org changes to incorporate?

4. **Use cases:**
   - Q: When should users refresh a scenario?
   - Q: When should they NOT refresh (create new instead)?

5. **Limitations:**
   - Q: Known issues or limitations?
   - Q: Any data that doesn't sync correctly?

**Suggested delivery:** Step-by-step workflow with screenshots; confirm feature status

---

### 6. Scenario Merging (`scenarios/merging.md`)

**Current status:** TBD placeholder
**Priority:** MEDIUM

**What's needed:**

1. **Feature availability:**
   - Q: Is scenario merging available? (Merge Scenario A + Scenario B → New Scenario C?)

2. **How it works:**
   - Q: Step-by-step flow?
   - Q: What happens to conflicting changes?

3. **Use cases:**
   - Q: When would users merge scenarios?

**Suggested delivery:** Confirm if feature exists; if yes, provide workflow

---

### 7. Scenario to Main Org (`scenarios/scenario-to-main-org.md`)

**Current status:** TBD placeholder
**Priority:** HIGH - Critical implementation workflow

**What's needed:**

1. **Implementation workflow:**
   - Q: After scenario approved, how do you "push to Main Org"?
   - Q: Is there a button/action for this?
   - Q: Is it automatic or manual?

2. **What happens:**
   - Q: Do changes apply to Main Org immediately?
   - Q: Are effective dates respected when implementing?
   - Q: Can you roll back if issues?

3. **Prerequisites:**
   - Q: Must scenario be approved first?
   - Q: Any validation checks before implementation?

**Suggested delivery:** Clear step-by-step implementation guide

---

### 8. Project Creation (`scenarios/projects.md`)

**Current status:** TBD placeholder (duplicate file: `scenarios/project-creation.md`)
**Priority:** MEDIUM

**What's needed:**

1. **What is a Project?**
   - Q: How does a "Project" differ from a "Scenario"?
   - Q: Is it a container for multiple related scenarios?

2. **Creating projects:**
   - Q: Where do you create projects?
   - Q: What fields/settings?

3. **Use cases:**
   - Q: When should users create a project vs just a scenario?

**Suggested delivery:** Clarify project concept and workflow

**Note:** Two files exist: `scenarios/projects.md` and `scenarios/project-creation.md` - consolidate

---

## Category 3: Assets (2 pages)

Quick reference materials requiring specific information.

### 9. Keyboard Shortcuts (`assets/keyboard-shortcuts.md`)

**Current status:** IPR placeholder
**Priority:** MEDIUM - Nice-to-have for power users

**What's needed:**

1. **Complete list of shortcuts:**
   - Q: Navigation shortcuts (known: `/` for search, what else?)
   - Q: Scenario shortcuts (e.g., `Cmd+N` for new position?)
   - Q: Org chart shortcuts (arrow keys to navigate?)
   - Q: Save/Undo: `Cmd+S`, `Cmd+Z`, `Cmd+Shift+Z`?
   - Q: View switching: `3` for Org Chart, `5` for Directory (confirmed)?
   - Q: Any platform-specific (Mac vs Windows)?

2. **Configurable shortcuts:**
   - Q: Can users customize shortcuts?
   - Q: If yes, where (Settings)?

**Suggested delivery:** Complete list of all keyboard shortcuts organized by category

---

### 10. Video Tutorial Library (`assets/video-library.md`)

**Current status:** IPR placeholder
**Priority:** HIGH - Important learning resource

**What's needed:**

1. **Available videos:**
   - Need: List of all tutorial videos with:
     - Title
     - URL (YouTube/Loom/embedded?)
     - Duration
     - Brief description (1-2 sentences)
     - Topics covered

2. **Organization:**
   - Q: Organize by category (Getting Started, Scenarios, Forecast, Admin)?
   - Q: Or by skill level (Beginner, Intermediate, Advanced)?

**Suggested delivery:** Spreadsheet or list of all videos with metadata

---

## Category 4: Technical Documentation (2 pages)

Reference pages requiring architecture and compliance information.

### 11. Technical Overview (`technical-documentation/technical-overview.md`)

**Current status:** IPR placeholder
**Priority:** MEDIUM - Needed for technical buyers/IT teams

**What's needed:**

1. **Architecture:**
   - Q: Cloud platform (AWS, Azure, GCP)?
   - Q: Data residency options (US, EU, other)?
   - Q: Multi-tenant or single-tenant architecture?

2. **APIs:**
   - Q: REST API available?
   - Q: GraphQL?
   - Q: Webhooks or event streaming?
   - Q: API documentation location?

3. **Integration ecosystem:**
   - Q: Supported HRIS: Workday, BambooHR, ADP, others?
   - Q: SSO: Okta, Azure AD, Google (documented), others?
   - Q: BI tools: Tableau, Looker, Power BI?
   - Q: SFTP import (documented - already covered)?

4. **Performance and scalability:**
   - Q: Max organization size supported?
   - Q: Performance benchmarks?
   - Q: Uptime SLA?

5. **Deployment:**
   - Q: SaaS only or on-premise available?

**Suggested delivery:** 1-page technical overview covering architecture, APIs, integrations, scalability

---

### 12. Data Security & Privacy (`technical-documentation/data-security-privacy.md`)

**Current status:** IPR placeholder
**Priority:** HIGH - Critical for security/compliance reviews

**What's needed:**

1. **Certifications and compliance:**
   - Q: SOC 2 compliant?
   - Q: GDPR compliant?
   - Q: CCPA compliant?
   - Q: ISO 27001, HIPAA, or other certifications?

2. **Encryption:**
   - Q: Data at rest encrypted?
   - Q: Data in transit (TLS 1.2+)?
   - Q: Key management approach?

3. **Access controls:**
   - Q: RBAC (Role-Based Access Control)?
   - Q: Field-level permissions? (Already documented)
   - Q: Audit logging available?
   - Q: Session management?

4. **Data privacy:**
   - Q: Data retention policies?
   - Q: Right to deletion (GDPR)?
   - Q: Data export for compliance?
   - Q: Data anonymization features?

5. **Incident response:**
   - Q: Security incident response process?
   - Q: Breach notification policy?
   - Q: Vulnerability management?

**Suggested delivery:** List of certifications, encryption practices, retention policies, incident response overview (if publicly shareable)

---

## Category 5: Admin (2 pages)

Recently added admin pages needing platform-specific details.

### 13. Platform Notifications (`admin/notifications.md`)

**Current status:** Hidden placeholder (created Feb 19, 2026)
**Priority:** MEDIUM - Helpful for users managing notifications

**What's needed:**

1. **Complete notification inventory:**

   **Scenario-related:**
   - Q: Scenario shared with you
   - Q: Scenario approval request
   - Q: Scenario approved/rejected
   - Q: Scenario comment/mention
   - Q: Scenario changes by collaborator
   - Q: Scenario deadline approaching (if supported)

   **Data & System:**
   - Q: Data import completed
   - Q: Data import failed/errors
   - Q: Live data refresh completed
   - Q: System maintenance scheduled

   **Collaboration:**
   - Q: User invited to workspace
   - Q: Access level changed
   - Q: Comment replies
   - Q: @mentions in comments
   - Q: Position assignment notifications (if applicable)

   **Admin:**
   - Q: New user sign-up (pending approval)
   - Q: User access request
   - Q: Integration connection issues
   - Q: License/billing notifications

   **Approval Workflow:**
   - Q: Approval request received
   - Q: Approval decision made (upstream/downstream)
   - Q: Approval workflow completed
   - Q: Approval request canceled

2. **For each notification:**
   - What triggers it?
   - Who receives it (roles/permissions)?
   - Email vs in-app delivery?
   - Can it be configured/muted?

3. **Notification management:**
   - Q: How do users configure notification preferences?
   - Q: Notification frequency settings (instant, daily digest, etc.)?
   - Q: Can admins set org-wide notification defaults?

4. **Integration notifications:**
   - Q: Are there API webhooks for notifications?
   - Q: Slack/Teams integrations for notifications?

**Suggested delivery:** Complete list of all notification types with triggers, recipients, and configuration options

---

### 14. Access Groups Examples (`admin/access-groups-examples.md`)

**Current status:** Hidden placeholder with draft examples (created Feb 19, 2026)
**Priority:** MEDIUM - Helps users configure access control

**What's needed:**

1. **Validation of draft examples:**
   - I drafted 8 example scenarios (view budget without edit, department-specific, executive, HRBP, consultant, reviewer, read-only, recruiter)
   - Q: Are these examples accurate to how the product works?
   - Q: Are permission names correct ("View all," "Edit all," etc.)?

2. **Product-specific details:**
   - Q: Actual field names used in access group configuration?
   - Q: Can access groups combine multiple filters (Department + Location)?
   - Q: Are there row-level security features I missed?
   - Q: Time-based access control available?

3. **Real customer examples:**
   - Q: Can you provide 2-3 anonymized customer examples of access configurations?
   - Q: What are common mistakes users make?

4. **Compliance scenarios:**
   - Q: Should we include GDPR/SOX-specific examples?

5. **Screenshots:**
   - Q: Can you provide screenshots of access group configuration UI?

**Suggested delivery:** Review draft examples; provide corrections; add screenshots; share customer examples

---

## Category 6: Forecast (1 page - NOTE)

### 15. Diversity & Inclusion Analysis (`use-case-tutorials/diversity-inclusion-analysis.md`)

**REMOVED FROM REQUIREMENTS** - This is actually under Use Case Tutorials, counted in Category 1

**Note:** I originally counted this separately but it's already in the Use Case Tutorials section above. Keeping this note for clarity.

---

## Summary by Priority

### 🔴 HIGH Priority (8 pages)
Must-have for users actively working on these workflows:

1. Modeling Budget Cuts (use case)
2. Compensation Planning (use case)
3. Annual Hiring Plan (use case)
4. Scenario Refresh (advanced feature)
5. Scenario to Main Org (implementation workflow)
6. Video Tutorial Library (learning resource)
7. Data Security & Privacy (compliance reviews)

### 🟠 MEDIUM Priority (5 pages)
Important but less urgent:

8. Succession Planning (use case)
9. Keyboard Shortcuts (power user feature)
10. Technical Overview (technical buyers)
11. Platform Notifications (notification management)
12. Access Groups Examples (access control)

### 🟡 LOW Priority (2 pages)
Nice-to-have, can complete later:

13. Scenario Merging (advanced feature, unclear if exists)
14. Project Creation (unclear product concept)

---

## Recommended Approach

### Phase 1: Quick Wins (Answer these first)
Can be answered quickly and unblock multiple pages:

1. **Video Tutorial Library** - Provide list of videos → immediate completion
2. **Keyboard Shortcuts** - Provide complete list → immediate completion
3. **Scenario Refresh** - Confirm status and provide workflow → immediate completion

**Result:** 3 pages completed quickly

---

### Phase 2: High-Value Use Cases (Requires workflow examples)
Best as Loom walkthroughs or step-by-step written guides:

4. **Modeling Budget Cuts** - Loom or written workflow
5. **Compensation Planning** - Clarify features (equity, bulk %, compression) + workflow
6. **Annual Hiring Plan** - Step-by-step with Forecast view
7. **Succession Planning** - Example workflow

**Result:** 4 high-value tutorials completed

---

### Phase 3: Technical/Admin Pages (Requires documentation)
Provide existing docs or summaries:

8. **Data Security & Privacy** - Certifications, encryption, retention policies
9. **Technical Overview** - Architecture, APIs, integrations, scalability
10. **Platform Notifications** - Complete notification list with details
11. **Access Groups Examples** - Review draft, provide corrections + screenshots

**Result:** 4 technical/admin pages completed

---

### Phase 4: Advanced Features (Requires feature clarification)
Confirm status and capabilities:

12. **Scenario to Main Org** - Implementation workflow
13. **Scenario Merging** - Confirm if exists; provide workflow
14. **Project Creation** - Clarify concept

**Result:** 3 advanced feature pages completed

---

## How to Provide Context

For each page, please provide:

1. **Answers to specific questions** listed above
2. **Screenshots or Loom videos** of workflows
3. **Example data or scenarios** (anonymized)
4. **Internal documentation** if available
5. **Subject matter expert contact** if complex

---

## Files to Consolidate/Archive

**Duplicate files identified:**
- `scenarios/projects.md` and `scenarios/project-creation.md` (same topic, consolidate)

---

## Total Remaining Work

**15 placeholder pages to complete:**
- 🔴 HIGH: 7 pages
- 🟠 MEDIUM: 5 pages
- 🟡 LOW: 2 pages
- ✅ DUPLICATE: 1 page (consolidate)

**Estimated completion:** With context provided, all 15 pages can be written to production quality.

---

**Last updated:** February 19, 2026
**Maintained by:** Claude (Documentation Agent)
**Contact:** Provide context via this document or direct communication
