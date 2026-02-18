# Additional Context Needs for Documentation Refresh

This document outlines specific product knowledge questions needed to write accurate and effective articles for pages where current documentation and training transcripts don't provide sufficient detail.

---

## 🔴 CRITICAL PRIORITY (P0) - Needed for Core Functionality

### **Building Headcount Forecasts** (Target: FORECAST section)
**What I need to know:**
1. How does a user create a new headcount forecast from scratch?
2. What are the key inputs required (departments, timeframes, growth targets)?
3. How do users model hiring phased over time (Q1: 5 hires, Q2: 3 hires, etc.)?
4. How does forecast connect to scenarios? Can you create a forecast from a scenario?
5. What approval workflows exist for forecasts?
6. What visualizations/reports are available to show the headcount projection?
7. Can you compare multiple forecast versions?

---

### **Budget Planning & Tracking** (Target: FORECAST section)
**What I need to know:**
1. How does a user set budget constraints for headcount planning?
2. Where do users input their budget numbers (total budget, per-department, per-quarter)?
3. How does the system track actual spend vs. forecasted budget?
4. What variance analysis features exist?
5. How do compensation/rate cards integrate with budget planning?
6. Can users model "what-if" budget scenarios (e.g., 10% budget cut)?
7. What budget reports/exports are available?
8. How do budget alerts/warnings work when approaching limits?

---

### **Admin Overview** (Target: ADMIN CAPABILITIES section)
**What I need to know:**
1. What are the distinct admin responsibilities (vs. regular users)?
2. What permissions/roles exist for admins?
3. How does someone become an admin (is it assigned by Agentnoon or self-serve)?
4. What is the typical admin onboarding checklist (first 30 days)?
5. What ongoing maintenance tasks should admins perform (weekly, monthly, quarterly)?
6. Are there different types of admins (super admin, data admin, access admin)?

---

### **Configuring Approval Flows** (Target: ADMIN CAPABILITIES section)
**What I need to know:**
1. How does an admin set up approval workflows from scratch?
2. Can approval flows be customized per department or scenario type?
3. What are the approval routing options (linear, parallel, conditional)?
4. How do you configure multi-level approvals?
5. Can approvals be delegated? How?
6. What notifications are sent at each approval stage?
7. How do admins monitor approval workflow status?
8. Can approval flows be tested before going live?

---

## 🟠 HIGH PRIORITY (P1) - Important for User Success

### **Forecast Overview** (Target: FORECAST section)
**What I need to know:**
1. What is the primary purpose of the Forecast module (vs. Scenarios)?
2. When should a user use Forecast instead of Scenarios?
3. What are the key capabilities unique to Forecast?
4. What types of forecasts can be created (headcount, cost, both)?
5. How does Forecast handle historical data vs. future projections?
6. What is the relationship between Forecast and Main Org data?

---

### **Forecast vs Scenarios** (Target: FORECAST section)
**What I need to know:**
1. What are the key differences between Forecast and Scenarios?
2. When should you use Forecast? When should you use Scenarios?
3. Can you use both together? If so, how do they work together?
4. What data flows between Forecast and Scenarios?
5. Can you convert a Scenario into a Forecast or vice versa?

---

### **Forecast Reports & Exports** (Target: FORECAST section)
**What I need to know:**
1. What pre-built forecast reports are available?
2. Can users create custom forecast reports? How?
3. What export formats are supported (Excel, CSV, PowerPoint)?
4. What data is included in forecast exports?
5. How do users share forecasts with stakeholders who don't have Agentnoon access?

---

### **Position vs Headcount Management** (Target: BEST PRACTICES section)
**What I need to know:**
1. What is the difference between position-based and headcount-based planning?
2. What are the pros and cons of each approach?
3. When should an organization use position-based planning?
4. When should they use headcount-based planning?
5. Can organizations use a hybrid approach? How?
6. How does this fundamental choice affect the rest of the system?

---

### **Main Org Overview** (Target: MAIN ORG section)
**What I need to know:**
1. What does "Main Org" represent? (Is it the current org structure, a snapshot, or live data?)
2. How does Main Org sync with HRIS systems?
3. Can users edit Main Org directly, or is it read-only?
4. How often is Main Org data refreshed?
5. What is the difference between "Main Org" and "Scenarios"?
6. Can you have historical views of Main Org?

---

### **Taskbar (Main Org)** (Target: MAIN ORG section)
**What I need to know:**
1. What actions are available in the Main Org taskbar?
2. What actions are disabled in Main Org (vs. Scenarios)?
3. Why are certain actions restricted to Scenarios?
4. What can users do vs. what requires admin permissions?

---

### **Project Creation** (Target: SCENARIOS section - currently confusing)
**What I need to know:**
1. What exactly is a "Project" in Agentnoon?
2. How is a Project different from a Scenario?
3. How is a Project different from an Initiative?
4. When should users create a Project vs. just creating Scenarios?
5. Can a Project contain multiple Scenarios?
6. What are the key use cases for Projects?
7. Is this feature commonly used or is it enterprise-only?

---

## 🟡 MEDIUM PRIORITY (P2) - Nice to Have for Comprehensive Coverage

### **Multi-Year Planning** (Target: FORECAST section)
**What I need to know:**
1. How do users set up multi-year forecast views (2-3 years)?
2. What is a "rolling forecast" and how is it configured?
3. Can users do scenario-based multi-year forecasting?
4. How do long-term strategic plans integrate with annual planning?

---

### **Diversity & Inclusion Analysis** (Target: USE CASE TUTORIALS section)
**What I need to know:**
1. What D&I metrics are available in the Hub?
2. How do users track diversity progress over time?
3. Are there pre-built D&I reports or dashboards?
4. How do users set diversity goals and track against them?
5. What export formats work best for D&I reporting to leadership?

---

### **Compensation Planning** (Target: USE CASE TUTORIALS section)
**What I need to know:**
1. How do rate cards work in the annual comp cycle?
2. Can users model raises and promotions in scenarios?
3. How do users analyze pay equity across the organization?
4. What comp planning reports are available?
5. How does budget management integrate with comp planning?

---

### **Succession Planning** (Target: USE CASE TUTORIALS section)
**What I need to know:**
1. Beyond the shortlisting feature (already documented in talent-selection.md), what other succession planning capabilities exist?
2. Can you model "flight risk" or succession gaps?
3. How do you analyze bench strength?
4. Are there succession planning templates or workflows?

---

### **Data Refresh & Sync** (Target: ADMIN CAPABILITIES section)
**What I need to know:**
1. How do admins configure sync frequency (daily, weekly, monthly)?
2. What happens when there's a conflict between manual changes and synced data?
3. How do admins monitor integration health?
4. What audit logs are available for data changes?
5. Can admins pause or manually trigger a sync?

---

### **Scenario Refresh** (Target: SCENARIOS section)
**What I need to know:**
1. **Feature Status:** Is Scenario Refresh released yet? (Excel plan says "not released yet")
2. How does Scenario Refresh work once released?
3. What happens to manual changes in a scenario when you refresh with new Main Org data?
4. How do users handle conflicts between scenario changes and new data?
5. When should users refresh vs. create a new scenario?

---

## 📋 CLARIFICATIONS NEEDED

### **Directory View Capabilities**
**What I need to know:**
1. Is Directory view the same in Main Org, Scenarios, and Forecast, or are there differences?
2. What unique features exist in Scenario Directory vs. Main Org Directory?
3. Can users create custom directory views (saved column configurations)?

---

### **Taskbar Differences**
**What I need to know:**
1. Can you provide a comprehensive comparison table showing:
   - Main Org taskbar actions
   - Scenario taskbar actions
   - What's available where and why

---

### **Approval Flows Details**
**What I need to know:**
1. The current approvals.md mentions 4 levels (Level 0-3). Is this still accurate?
2. Can approval levels be customized or are they fixed?
3. What granular permissions exist for approvers (approve, reject, comment, delegate)?

---

## ✅ PAGES WHERE I HAVE SUFFICIENT CONTEXT

These pages can be written with existing documentation and training transcript:

### From Training Transcript:
- Welcome & Quick Overview
- Quick Start Guide
- Parts of the Application
- Cards
- Scenarios Fundamentals (basics)
- Orientation & Navigation (Main Org)
- Conducting Span of Control Analysis
- Planning a Reorganization (80% complete outline possible)
- Building an Annual Hiring Plan (80% complete outline possible)

### From Existing Documentation:
- All pages marked "ENHANCE", "CONSOLIDATE", "LIFT & SHIFT" in the target state mapping
- FAQ sections (can draft from existing content)
- Troubleshooting guides (can extract from error checklists and auth docs)
- All ADMIN pages that reorganize existing content (Access Control, Data Upload, Fields Management, Auto Mapping, User Management, Rate Card)
- All TECHNICAL pages that consolidate existing content (Authentication & IAM, Live Data Refresh)

---

## HOW TO USE THIS DOCUMENT

**For each question above:**
1. Provide a clear explanation addressing all sub-questions
2. Include screenshots or examples if helpful
3. Note any relevant UI locations or workflows
4. Flag any features that are enterprise-only or coming soon

**Priority order for providing context:**
1. 🔴 P0 - Critical (needed for core functionality)
2. 🟠 P1 - High (important for user success)
3. 🟡 P2 - Medium (nice to have for comprehensive coverage)

