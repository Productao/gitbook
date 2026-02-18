# Additional Context Needs for Documentation Refresh - Version 2

**Date:** February 18, 2026
**Status:** 22 IPR placeholder pages remaining
**Purpose:** Identify specific product knowledge and context needed to complete remaining documentation pages

---

## Summary of Remaining Work

**22 IPR Placeholder Pages Remaining:**
- Use Case Tutorials: 3 pages
- Scenarios: 1 page (Scenario Refresh)
- FAQ Sections: 6 pages
- Troubleshooting: 6 pages
- Assets: 4 pages
- Technical Documentation: 2 pages

**Context Assessment:**
- **Can write with existing context:** ~8-10 pages (FAQ, Troubleshooting - can leverage existing docs)
- **Need additional context:** ~12-14 pages (Use Cases, Technical, Assets, Scenario Refresh)

---

## Priority 1: Use Case Tutorials (3 pages)

These are high-value, practical guides that users need. They require detailed product workflows.

### 1. Modeling Budget Cuts (`use-case-tutorials/modeling-budget-cuts.md`)

**What I need to know:**
1. **Workflow for identifying positions to cut:**
   - Do users typically filter by salary (highest paid first)?
   - Filter by department (cut from specific areas)?
   - Filter by performance metrics or other criteria?
   - Is there a "target savings calculator" feature?

2. **Bulk operations for closing positions:**
   - Can you bulk-select positions in Directory and close them all at once?
   - How do you set effective dates for bulk closures?
   - Does the system warn you about broken hierarchies before closing?

3. **Comparing multiple RIF scenarios:**
   - What's the typical workflow? (Create "RIF Option A", "RIF Option B", "RIF Option C"?)
   - Can you compare scenarios side-by-side in the UI or only via exports?
   - Is there a "scenario comparison" view specifically for this?

4. **Sensitive data handling:**
   - Should documentation address privacy concerns (who sees RIF scenarios)?
   - Are there best practices for limiting access to RIF scenarios?

5. **Post-RIF optimization:**
   - After closing positions, do users typically need to reassign reports to new managers?
   - Any specific tools or features for "healing" the org chart after cuts?

**Can write from existing context:** Mostly yes, but need clarification on bulk operations and comparison tools.

---

### 2. Compensation Planning (`use-case-tutorials/compensation-planning.md`)

**What I need to know:**
1. **Annual compensation review workflow:**
   - How do users typically model merit increases? (3% across the board? Different % by performance tier?)
   - Can you bulk-apply salary increases by percentage?
   - Or do you have to edit each position individually?

2. **Rate cards and salary bands:**
   - How do rate cards integrate with compensation planning?
   - If someone is promoted, do you change their position's pay grade and rate card auto-populates?
   - Can you model "bringing everyone to midpoint of their band"?

3. **Equity and total compensation:**
   - Does Agentnoon support equity compensation fields (RSUs, options)?
   - Can you model equity refreshes or new grants?
   - Is there a "total compensation" calculator?

4. **Compression analysis:**
   - Is there a built-in "compression analysis" tool?
   - Or do users export to Excel and analyze there?
   - What does "compression" mean in Agentnoon's context? (ICs making more than managers?)

5. **Budget allocation by department:**
   - If you have a $2M compensation budget, can you allocate "$500K to Engineering, $300K to Sales"?
   - Or do you just set the total and hope it adds up?

**Can write from existing context:** Partially. Need details on bulk operations, compression analysis, equity support.

---

### 3. Diversity & Inclusion Analysis (`use-case-tutorials/diversity-inclusion-analysis.md`)

**What I need to know:**
1. **DEI fields in Agentnoon:**
   - What DEI fields are commonly tracked? (Gender, Ethnicity, LGBTQ+, Disability, Veteran status?)
   - Are these standard fields or custom fields users must create?

2. **Workforce Hub DEI analytics:**
   - Are there pre-built DEI charts in Workforce Hub?
   - Or do users have to create custom charts?
   - What kind of visualizations are possible? (Gender distribution by level, ethnicity by department, etc.)

3. **Filtering for DEI analysis:**
   - Can you filter by multiple DEI attributes at once? (e.g., "Women in Engineering at Senior+ levels")
   - Can you save DEI-specific views?

4. **Modeling DEI improvements in scenarios:**
   - Typical workflow: Add positions with target demographics to improve representation?
   - Can you set DEI targets/goals in Agentnoon?
   - How do you measure progress toward DEI goals?

5. **Privacy and compliance:**
   - Are there special access controls for DEI data?
   - Should documentation address privacy best practices?

**Can write from existing context:** Partially. The Loom transcript mentioned DEI fields, but need more detail on Workforce Hub analytics and goal-setting.

---

## Priority 2: Scenario Refresh (1 page)

This feature is still in development, but documentation is needed.

### 4. Scenario Refresh (`scenarios/refresh.md`)

**What I need to know:**
1. **Current status:**
   - Is scenario refresh available now, in beta, or still planned?
   - If available, where in the UI do you access it?

2. **How scenario refresh works:**
   - Step-by-step: Click "Refresh Scenario" → System shows preview of changes → Confirm?
   - What exactly happens to scenario data?
   - Are scenario changes (additions, closures, moves) preserved or lost?

3. **Conflict resolution:**
   - If a position exists in scenario but not Main Org (employee left), what happens?
   - If a position exists in Main Org but not scenario (new hire), is it added automatically?
   - Can you selectively choose which Main Org changes to incorporate?

4. **Use cases:**
   - When should users refresh a scenario?
   - When should they NOT refresh (create a new scenario instead)?

5. **Limitations:**
   - What are the known issues or limitations?
   - Any data that doesn't sync correctly?

**Can write from existing context:** No. This is a specific feature that wasn't covered in detail in the Loom transcript.

---

## Priority 3: FAQ Sections (6 pages)

These can mostly be written from existing content, but need confirmation on common questions.

### 5-10. FAQ Pages

**What I need to know:**
1. **Most common user questions:**
   - What do users ask support most often?
   - What questions come up in onboarding?
   - Any "gotchas" or confusing concepts?

2. **FAQ format preference:**
   - Should FAQs be Q&A style ("Q: How do I...? A: You do...")
   - Or topic-based ("Understanding Span of Control: SOC measures...")

3. **Specific FAQ topics needed:**
   - **Getting Started FAQs:** First 30 minutes questions?
   - **Data & Import FAQs:** CSV format, field mapping, validation errors?
   - **Scenarios FAQs:** Creating, editing, submitting for approval?
   - **Forecast FAQs:** Understanding time periods, hire dates, effective dates?
   - **Permissions & Access FAQs:** Who can see what, access groups, admin permissions?

**Can write from existing context:** Mostly yes. I can extract FAQs from existing documentation. Just need to know if there are specific support questions that should be included.

---

## Priority 4: Troubleshooting Guides (6 pages)

These can be written from existing docs + common error patterns.

### 11-16. Troubleshooting Pages

**What I need to know:**
1. **Most common user issues:**
   - What do users get stuck on most often?
   - What errors do they encounter?
   - What workflows fail or confuse them?

2. **Error messages:**
   - Are there specific error messages that should be documented?
   - Any cryptic errors that need translation?

3. **Troubleshooting format preference:**
   - Problem → Cause → Solution format?
   - Or step-by-step diagnostic flowchart?

**Specific topics:**
- **Login & Access Issues:** SSO failures, MFA problems, locked accounts?
- **Data Issues:** CSV validation errors, broken hierarchies, missing fields?
- **Scenario Issues:** Can't submit, approval stuck, changes not saving?
- **Performance Issues:** Slow loading, timeouts, large org charts?
- **Export & Integration Issues:** CSV export fails, SFTP connection errors?

**Can write from existing context:** Mostly yes. Existing docs have error handling info. Just need confirmation on most common issues.

---

## Priority 5: Assets (4 pages)

These are quick reference materials.

### 17. Keyboard Shortcuts (`assets/keyboard-shortcuts.md`)

**What I need to know:**
1. **Complete list of keyboard shortcuts:**
   - Navigation shortcuts (e.g., `/` for search, `Esc` to close panels)
   - Scenario shortcuts (e.g., `Cmd+N` for new position?)
   - Org chart shortcuts (e.g., arrow keys to navigate cards?)
   - Any platform-specific shortcuts (Mac vs Windows?)

2. **Configurable shortcuts:**
   - Can users customize keyboard shortcuts?
   - If yes, how? (Settings page?)

**Can write from existing context:** Partially. The Loom transcript mentioned `/` for search and filter, but need the full list.

---

### 18. Glossary (`assets/glossary.md`)

**What I need to know:**
1. **Agentnoon-specific terminology:**
   - Terms that are unique to Agentnoon or have special meaning
   - Examples: "Position", "Headcount", "SOC", "Main Org", "OpEx Panel"
   - Any acronyms used in the product?

2. **Glossary format preference:**
   - Alphabetical list with definitions?
   - Categorized by topic (Scenarios, Forecast, Admin)?

**Can write from existing context:** Yes! I can extract all key terms from existing documentation and create a glossary.

---

### 19. Video Tutorial Library (`assets/video-library.md`)

**What I need to know:**
1. **Available video tutorials:**
   - What videos exist? (Titles, topics, URLs)
   - Are they on YouTube, Loom, or hosted on Agentnoon's site?
   - Organized by topic or skill level?

2. **Video descriptions:**
   - Should each video have a description/summary?
   - Timestamps for key sections?

**Can write from existing context:** No. Need the actual list of videos.

---

### 20. Quick Start Checklist (`assets/quick-start-checklist.md`)

**What I need to know:**
1. **Format preference:**
   - Printable PDF checklist?
   - Or markdown checklist users can copy?

2. **Checklist scope:**
   - First 30 minutes? First day? First week?
   - For new users or new admins?

**Can write from existing context:** Yes! I can create a checklist based on the Quick Start Guide already written.

---

## Priority 6: Technical Documentation (2 pages)

These are more reference-style pages.

### 21. Technical Overview (`technical-documentation/technical-overview.md`)

**What I need to know:**
1. **Agentnoon's technical architecture:**
   - Cloud-based? (AWS, Azure, GCP?)
   - Data residency options? (US, EU, etc.)
   - APIs available? (REST, GraphQL?)
   - Webhooks or event streaming?

2. **Integration ecosystem:**
   - What systems does Agentnoon integrate with?
   - HRIS: Workday, BambooHR, ADP, etc.?
   - SSO: Okta, Azure AD, Google, etc.?
   - BI tools: Tableau, Looker, Power BI?

3. **Performance and scalability:**
   - Max organization size supported?
   - Performance benchmarks?
   - Uptime SLA?

**Can write from existing context:** Partially. Some integration info exists, but need architecture details.

---

### 22. Data Security & Privacy (`technical-documentation/data-security-privacy.md`)

**What I need to know:**
1. **Data security features:**
   - Encryption at rest and in transit?
   - SOC 2 compliant?
   - GDPR compliant?
   - CCPA compliant?
   - Other certifications?

2. **Access controls:**
   - Role-based access control (RBAC)?
   - Field-level permissions?
   - Audit logging?

3. **Data privacy:**
   - Data retention policies?
   - Right to deletion?
   - Data export for compliance?

4. **Incident response:**
   - Security incident response process?
   - Breach notification policy?

**Can write from existing context:** Partially. Some access control info exists, but need compliance/certification details.

---

## Summary: What Can Be Written Now vs. Needs Context

### ✅ Can Write Now (8-10 pages)
With existing documentation and general product knowledge, I can write:
1. **FAQ sections (6 pages)** - Extract from existing docs
2. **Troubleshooting guides (6 pages)** - Leverage existing error handling content
3. **Glossary** - Extract key terms from all completed pages
4. **Quick Start Checklist** - Based on Quick Start Guide

**Total: ~8 pages can be written immediately**

### ⚠️ Need Additional Context (12-14 pages)
These require specific product knowledge or assets:
1. **Use Case Tutorials (3 pages)** - Need workflow details
2. **Scenario Refresh (1 page)** - Feature details, current status
3. **Keyboard Shortcuts** - Full list needed
4. **Video Tutorial Library** - Need video list and URLs
5. **Technical Overview** - Architecture, integrations, scalability
6. **Data Security & Privacy** - Compliance certifications, security features

**Total: ~6 pages need context**

---

## Recommendation

**Option 1: Write what we can now**
I can immediately write 8-10 pages (FAQ, Troubleshooting, Glossary, Quick Start Checklist) using existing documentation. These would be production-ready and remove 8-10 IPR prefixes.

**Option 2: Provide context for high-priority pages**
You can provide context for the 6 pages that need specific product knowledge (Use Cases, Technical, Assets), and I'll write those as high-quality comprehensive guides.

**Option 3: Hybrid approach**
I write the 8-10 pages I can do now, and you provide context for the remaining 6 pages in a follow-up session.

---

## Questions for You

1. **Which approach do you prefer?** (Write what I can now, wait for context, or hybrid?)

2. **For Use Case Tutorials:** Can you provide:
   - Example workflows for budget cuts, compensation planning, DEI analysis?
   - Screenshots or Loom walkthrough of these workflows?

3. **For Scenario Refresh:** What's the current status of this feature?

4. **For Keyboard Shortcuts:** Can you provide the full list, or should I document only what's mentioned in existing docs?

5. **For Video Tutorial Library:** Do you have a list of videos with URLs?

6. **For Technical/Security pages:** Do you have internal docs on architecture, compliance, certifications?

---

**Next Steps:**
Let me know which pages you'd like me to write now with existing context, and which ones you'd like to provide additional context for. I'm ready to continue immediately!
