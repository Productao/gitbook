# Agentnoon Help Center Refresh 2026 - Project Context

This document tracks our collaboration on refreshing the Agentnoon help center documentation.

## Project Overview

**Goal:** Comprehensive refresh of Agentnoon's help center documentation to provide clear, user-friendly guidance for all product features.

**Timeline:** Started February 2026

**Branch:** `docs/help-center-refresh-2026`

**Pull Request:** #2 on GitHub

---

## What We're Building

### Scope
- 30+ articles across 15 major sections
- Complete navigation restructure in SUMMARY.md
- New "Key Concepts" foundational page
- Comprehensive placeholder pages with outlines for incomplete content
- Screenshot placeholders strategically placed throughout
- Centralized screenshot inventory for team collaboration

### Target State Structure

**Core Sections:**
1. **Start Here** (7 articles) - Onboarding and fundamentals
2. **Main Org** (5 articles) - Current state visualization
3. **Scenarios** (14 articles) - Workforce planning and what-if modeling
4. **Directory** (3 articles) - Table view and data analysis
5. **Hub** (3 articles) - Workforce analytics
6. **Forecast** (7 articles) - Time-based projections and budgeting
7. **Use Case Tutorials** (7 articles) - Step-by-step guides
8. **FAQ** (6 articles) - Common questions
9. **Troubleshooting** (6 articles) - Problem resolution
10. **Admin Capabilities** (17 articles) - Administration and configuration
11. **Assets & Quick Guides** (4 articles) - Reference materials
12. **Best Practices** (2 articles) - Recommended approaches
13. **Technical Documentation** (13 articles) - SSO, integrations, security
14. **Org Chart (Legacy)** (3 articles) - Deprecated features
15. **Updates (Legacy)** (1 article) - Historical reference

---

## Work Completed

### Phase 1: Foundation & Structure
- ✅ Created comprehensive SUMMARY.md with proper hierarchy
- ✅ Added icons to all top-level articles (not nested children)
- ✅ Fixed GitBook sync issue (duplicate SUMMARY.md entries)
- ✅ Reordered sections to match target state plan
- ✅ Added "(Legacy)" markers to deprecated sections

### Phase 2: Core Content Creation
- ✅ **Welcome page** - Platform introduction
- ✅ **Quick Start Guide** - 30-minute onboarding
- ✅ **Key Concepts page** - Essential Agentnoon terminology (positions vs people, Main Org vs Scenarios, change types, SOC, layers, effective dates, etc.)
- ✅ **Main Org Navigation** - Comprehensive taskbar guide
- ✅ **Scenarios Overview** - What scenarios are and when to use them
- ✅ **Scenarios Directory** - Table view in scenarios
- ✅ **Scenarios Taskbar** - All scenario tools explained
- ✅ **Directory pages** - Overview and features
- ✅ **Hub pages** - Chart navigation and packs

### Phase 3: Placeholder Pages
- ✅ Created 33 placeholder pages with "IPR" prefix for easy identification
- ✅ Each placeholder includes:
  - Clear "under construction" notice
  - Comprehensive content outline (10-15 bullet points)
  - Support contact information
- ✅ All placeholders marked with `hidden: false` (visible in GitBook)

### Phase 4: Visual Planning
- ✅ Added 51 screenshot placeholders throughout documentation
- ✅ Created comprehensive SCREENSHOT_INVENTORY.md:
  - Complete checklist of all 51 needed screenshots
  - Technical requirements and data guidelines
  - Composition and naming guidelines
  - Priority tiers (P0, P1, P2)
  - Assignee tracking template
  - Storage location specified

### Phase 5: Forecast Section (COMPLETED ✅)
- ✅ **Forecast Overview** - Complete guide to Forecast module as visualization tool
- ✅ **Building Headcount Forecasts** - Comprehensive guide using hire dates, effective dates, and scenarios
- ✅ **Budget Planning & Tracking** - Scenario budgets and OpEx panel guide
- ✅ **Forecast Navigation** - Interface controls, filtering, exports, workflows
- ✅ **Forecast vs Scenarios** - When to use each, integrated workflow
- ✅ **Forecast Reports & Exports** - CSV/PowerPoint/Image exports, common reports
- ✅ **Multi-Year Planning** - 3-5 year workforce projections, strategic planning

### Phase 6: Admin Capabilities (Core Pages Complete ✅)
- ✅ **Admin Overview** - All admin responsibilities, 30-day checklist, maintenance schedules
- ✅ **Configuring Approval Flows** - Level 0-3 approval system configuration
- ✅ **Data Refresh & Sync** - Manual CSV uploads, live integrations, scenario refresh

### Phase 7: Best Practices (COMPLETED ✅)
- ✅ **Position vs Headcount Management** - Position-first philosophy, when to use each
- ✅ **Making Org Changes** - Planning, testing, communicating, implementing org changes

### Phase 8: Remaining Work (21 IPR Placeholders)
**Use Case Tutorials** (3 pages):
- 🔄 IPR Modeling Budget Cuts
- 🔄 IPR Compensation Planning
- 🔄 IPR Diversity & Inclusion Analysis

**FAQ Sections** (6 pages):
- 🔄 IPR FAQ Overview
- 🔄 IPR Getting Started FAQs
- 🔄 IPR Data & Import FAQs
- 🔄 IPR Scenarios FAQs
- 🔄 IPR Forecast FAQs
- 🔄 IPR Permissions & Access FAQs

**Troubleshooting** (6 pages):
- 🔄 IPR Troubleshooting Overview
- 🔄 IPR Login & Access Issues
- 🔄 IPR Data Issues
- 🔄 IPR Scenario Issues
- 🔄 IPR Performance Issues
- 🔄 IPR Export & Integration Issues

**Assets** (4 pages):
- 🔄 IPR Video Tutorial Library
- 🔄 IPR Quick Start Checklist
- 🔄 IPR Keyboard Shortcuts
- 🔄 IPR Glossary

**Technical Documentation** (2 pages):
- 🔄 IPR Technical Overview
- 🔄 IPR Data Security & Privacy

**Scenarios** (1 page):
- 🔄 IPR Scenario Refresh (feature in development)

---

## Key Technical Decisions

### Icon Strategy
- **Top-level articles only** have icons in SUMMARY.md
- **Nested child pages** do NOT have icons in SUMMARY.md
- **Individual markdown files:** Nested pages do not have `icon:` in frontmatter

### IPR Prefix Strategy
- "IPR" = "In Progress / Incomplete"
- Added to both:
  - Page titles in markdown files (`# IPR Page Title`)
  - SUMMARY.md navigation (`* [📊 IPR Page Title]`)
- Allows quick visual identification of incomplete pages in GitBook sidebar
- Remove IPR prefix when page is completed

### Placeholder Format
Every placeholder page includes:
```markdown
> **Note: This page is under construction. Content coming soon!**

## Planned Content Outline
- Bullet point 1
- Bullet point 2
...

---

For immediate assistance, please contact [support@agentnoon.com](...)
```

### Screenshot Placeholder Format
```markdown
> **[Screenshot placeholder: Description of what to capture]**
```

---

## Information Sources

### Primary Sources
1. **Training Transcript** (.resources/ folder) - Detailed product walkthrough
2. **Additional Context Provided** (.resources/additional-content-provided-v1.md) - 46-minute Loom transcript covering:
   - Forecast module deep dive
   - Admin capabilities and permissions
   - Approval workflows (Level 0-3 approvers)
   - Budget planning in scenarios
   - Position vs headcount philosophy
   - Effective dates and hire dates
   - Taskbar functionality
   - Directory view capabilities
3. **Existing Documentation** - Lift-and-shift content from original help center
4. **Excel Planning Document** (.resources/current-future-state-plan.xlsx) - Target state mapping

### Context Documents
- **REVIEW_GUIDE.md** - Comprehensive review of all 30 completed articles
- **additional-context-needs-v1-archived.md** - Original questions (now answered)
- **SCREENSHOT_INVENTORY.md** - Visual content tracking

---

## Git Workflow

### Branch Strategy
- Working branch: `docs/help-center-refresh-2026`
- Target branch: `main`
- All commits pushed to PR #2

### Commit Message Conventions
- `docs: <description>` for documentation changes
- Clear, descriptive messages
- Single-purpose commits when possible

### Recent Commits
1. `docs: fix icon placement - move icons from section headers to first-level articles`
2. `docs: remove icons from all nested child pages`
3. `docs: add Key Concepts page to Start Here section`
4. `docs: create comprehensive placeholders for all hidden pages`
5. `docs: unhide all pages and add IPR prefix to incomplete placeholder pages`
6. `docs: add screenshot placeholders throughout documentation`
7. `docs: add comprehensive screenshot inventory page for team reference`

---

## Key Product Concepts Documented

### Forecast Module
- **Not for data input** - Purely visualization
- **Pivot table paradigm** - Rows (aggregator) × Columns (time/fields) × Values (headcount/cost)
- **Three components:** Row aggregator, monetary fields, time period
- **Hire dates** control when headcount appears
- **Effective dates** control when changes take effect
- **Show Before** always references Main Org (not scenario start state)

### Scenarios
- **Sandbox environment** for workforce planning
- **Before and After** states tracked
- **Change Tracker** shows impact (headcount, cost)
- **Approval workflows:** Level 0-3 approvers
  - Level 1 & 2: Global approvers (set in settings)
  - Level 0 & 3: Scenario-specific approvers
- **OpEx Panel** (Scenario Impacts & Changes) shows budget progress

### Admin Capabilities
- **Access control** - Who can see what
- **Data management** - CSV uploads, integrations
- **Field configuration** - Custom fields, formulas, metrics
- **Rate cards** - Auto-populate salaries for new positions
- **Auto mapping** - Automatic field population based on rules
- **Approval configuration** - Set up Level 1 & 2 approvers

### Position vs Headcount Philosophy
- **Positions** = Roles (stable, used for planning)
- **Headcount** = People in roles (volatile, used for talent management)
- **Workforce planning** focuses on positions
- **Talent management** focuses on headcount
- Agentnoon is position-first

---

## File Organization

```
/Users/stephenjoly/Documents/Coding/gitbooks/
├── SUMMARY.md (navigation structure)
├── CONTEXT.md (this file)
├── SCREENSHOT_INVENTORY.md (visual assets tracking)
├── REVIEW_GUIDE.md (comprehensive article review)
├── start-here/
│   ├── welcome.md
│   ├── quick-start-guide.md
│   ├── concepts.md (NEW - key concepts page)
│   ├── agentnoon-101.md
│   └── ...
├── main-org/
├── scenarios/
├── forecast/ (7 pages - major expansion)
├── directory/
├── hub/
├── use-case-tutorials/
├── faq/ (6 placeholder pages)
├── troubleshooting/ (6 placeholder pages)
├── admin/
├── assets/ (4 placeholder pages)
├── best-practices/ (2 placeholder pages)
├── technical-documentation/
├── archive/ (archived/deprecated files)
└── .resources/ (source materials)
```

---

## Success Metrics

### Completion Status
- **Total Articles:** 87+
- **Completed:** ~47 (54%)
- **IPR Placeholders Remaining:** 21 (24%)
- **To Be Written:** ~19 (22%)

### Quality Indicators
- ✅ All pages have proper frontmatter
- ✅ All icons properly placed (top-level only)
- ✅ All placeholders have comprehensive outlines
- ✅ Screenshot locations identified and documented
- ✅ Navigation hierarchy matches target state
- ✅ No broken links in completed pages

---

## Next Steps

### Immediate Priorities
1. Complete remaining Forecast section pages (4 pages)
2. Write Admin Capabilities pages (3 pages)
3. Write Best Practices pages (2 pages)
4. Write Use Case Tutorial pages (3 pages)
5. Remove IPR prefixes from completed pages
6. Update SUMMARY.md to remove IPR from completed pages

### Future Phases
1. **Screenshot Capture:**
   - Assign screenshots from inventory
   - Capture P0 screenshots first
   - Insert into documentation

2. **Content Review:**
   - Technical accuracy review
   - User testing with sample audience
   - Feedback incorporation

3. **Go-Live:**
   - Remove all remaining IPR prefixes
   - Final SUMMARY.md cleanup
   - Merge PR #2 to main
   - Publish to production GitBook

---

## Team Collaboration

### Roles
- **Stephen (Product/Deployment Lead):** Context provider, reviewer, product expert
- **Claude (AI Assistant):** Content writer, documentation architect
- **Future Team Members:** Screenshot capture, technical review, user testing

### Communication
- **Primary:** This CONTEXT.md file
- **Secondary:** Git commit messages, PR comments
- **Reference:** SCREENSHOT_INVENTORY.md for visual assets

### How to Contribute
1. Read CONTEXT.md for project overview
2. Check SCREENSHOT_INVENTORY.md for screenshot assignments
3. Review REVIEW_GUIDE.md for completed content
4. Identify IPR pages in GitBook (they're prefixed)
5. Follow existing patterns for new content

---

## Lessons Learned

### What Worked Well
- Comprehensive placeholder strategy allowed rapid structure creation
- IPR prefix makes incomplete pages instantly identifiable
- Screenshot placeholders prevent "where should this go?" questions later
- Detailed content outlines in placeholders provide clear direction
- Icon-only-on-top-level strategy keeps sidebar clean

### Challenges Overcome
- **GitBook sync failure:** Resolved duplicate SUMMARY.md entry issue
- **Icon confusion:** Clarified icons belong on top-level articles only, not children
- **Hidden vs visible:** Decided to make all pages visible with IPR prefix instead of hiding
- **Placeholder format:** Standardized on clear, actionable placeholder structure

### Process Improvements
- Started with structure (SUMMARY.md) before content
- Created placeholders for everything to prevent "missing page" errors
- Used IPR prefix to track progress visibly
- Batched similar work (all placeholders at once, all icons together)

---

## Document Version History

- **v1.0** - February 18, 2026 - Initial CONTEXT.md creation

---

**Last Updated:** February 18, 2026

**Maintained By:** Stephen Joly & Claude (Documentation Team)

**Questions?** Contact [support@agentnoon.com](mailto:support@agentnoon.com)
