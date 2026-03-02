# Agentnoon Training Deck — Slide-by-Slide Outline

> **Target audience:** All Agentnoon users (Viewers, Planners, Approvers, Admins)
> **Target length:** ~50 core slides + ~15 appendix slides ≈ 65 slides total (max 120)
> **Slide format standard:** Title | Lead-line sentence | Bulleted key details (left) | Screenshot placeholder (right)
> **Purpose:** A self-serve user guide — go slide by slide, and by the end you're ready to use Agentnoon confidently.

---

## Document Structure

| Section | Slides | Purpose |
|---|---|---|
| **Part 1 — Welcome & Orientation** | 1–6 | Set context, introduce the platform |
| **Part 2 — Key Concepts** | 7–13 | Build foundational vocabulary |
| **Part 3 — Navigating Main Org** | 14–20 | Hands-on orientation to the live org |
| **Part 4 — Your First Scenario** | 21–32 | Core use case walkthrough end-to-end |
| **Part 5 — Reviewing Impact** | 33–38 | OpEx Panel, Forecast, Workforce Hub |
| **Part 6 — Collaboration & Approvals** | 39–43 | Sharing, commenting, approval workflow |
| **Part 7 — Exporting & Communicating** | 44–47 | Getting data and visuals out |
| **Part 8 — Wrap-Up** | 48–50 | Summary, next steps, support |
| **Appendix A — Feature Briefings** | A1–A10 | Reference pages for advanced features |
| **Appendix B — Admin Capabilities** | B1–B5 | Admin-specific configuration guides |
| **Appendix C — Quick Reference** | C1–C3 | Shortcuts, glossary, support info |

---

## PART 1 — WELCOME & ORIENTATION (Slides 1–6)

### Slide 1 — Title Slide
- **Purpose:** Branded cover page
- **Content:** "Agentnoon Training Deck" / subtitle: "Your complete guide to workforce planning with Agentnoon" / company logo / date
- **Screenshot:** None (branded design)

### Slide 2 — How to Use This Deck
- **Purpose:** Set expectations for the reader
- **Content:**
  - This deck is a self-serve training guide — go slide by slide at your own pace
  - The Core Narrative (slides 1–50) covers everything you need to get started
  - The Appendix contains reference material for advanced features and admin tasks
  - Each slide follows the same format: title, lead-line, key details, and a screenshot
- **Screenshot:** Table of contents / section overview graphic

### Slide 3 — What is Agentnoon?
- **Purpose:** One-sentence positioning
- **Content:**
  - Agentnoon turns workforce data into clear insights so you can forecast costs, model changes, and respond quickly as business needs evolve
  - Real-time dashboards and planning tools in one view
  - Run "what-if" scenarios, align plans to key goals, make decisions faster
  - No changes to live data until you're ready
- **Screenshot:** Homepage / high-level platform view

### Slide 4 — The Five Core Modules
- **Purpose:** Mental model for the whole platform
- **Content:**
  - **Main Org** — Your current, live organizational structure (view-only)
  - **Scenarios** — Editable copies where you model future changes
  - **Forecast** — Headcount and cost projections over time
  - **Workforce Hub** — Pre-built analytics charts
  - **Directory** — Table/spreadsheet view of your data
- **Screenshot:** Homepage showing module entry points or a diagram of the 5 modules

### Slide 5 — How the Modules Work Together
- **Purpose:** Show the typical workflow across modules
- **Content:**
  - **Step 1:** Main Org → Understand your current state
  - **Step 2:** Workforce Hub → Analyze structure, find opportunities
  - **Step 3:** Scenarios → Model proposed changes
  - **Step 4:** Forecast → Project headcount and cost over time
  - **Step 5:** Directory → Export detailed data for reporting
  - All modules work from the same underlying data
- **Screenshot:** Workflow diagram (Main Org → Hub → Scenarios → Forecast → Directory)

### Slide 6 — Logging In & the Homepage
- **Purpose:** Orient the user to what they see first
- **Content:**
  - Go to app.agentnoon.com and log in with your credentials
  - Homepage shows: instance name, list of scenarios (may be empty initially), quick links
  - Click "Open Org Chart" to enter Main Org
  - Scenario list is your home base for planning work
- **Screenshot:** Homepage with callouts to key areas

---

## PART 2 — KEY CONCEPTS (Slides 7–13)

### Slide 7 — Positions vs People
- **Purpose:** Establish the most fundamental concept
- **Content:**
  - **Position** = a job role (filled or open) with attributes like title, department, salary
  - **People (Employee)** = the individual assigned to a position
  - Agentnoon is position-based: you plan by creating/modifying positions first, then assigning people
  - Vacant positions appear in the org chart — you can plan for unfilled roles
- **Screenshot:** Card showing a filled position vs. a vacant position

### Slide 8 — Main Org vs Scenarios
- **Purpose:** Clarify the read-only vs editable distinction
- **Content:**
  - **Main Org** = current state, view-only, synced from your HRIS/data source
  - **Scenarios** = editable copies for modeling future changes
  - Scenarios are isolated — nothing you do in a scenario affects Main Org
  - Changes only become real when implemented externally and data is refreshed
- **Screenshot:** Side-by-side of Main Org (read-only badge) and a Scenario (editable)

### Slide 9 — Cards & the Org Chart
- **Purpose:** Explain the visual building block
- **Content:**
  - Each position appears as a card in the org chart
  - Default display: name and job title
  - Customize what's shown via Card Content (department, salary, location, etc.)
  - Hover to see quick info; click to open detail panel
  - Cards with FX fields show auto-calculated metrics (Span of Control, Layer, etc.)
- **Screenshot:** Annotated card with key fields labeled

### Slide 10 — Fields & Attributes
- **Purpose:** Understand the data behind every card
- **Content:**
  - **Attributes** = data points about positions or people (Department, Salary, Location, Title)
  - **Fields** = how attributes are organized and displayed
  - **Position fields** persist even when vacant (title, department, pay grade)
  - **People fields** are tied to individuals (name, email, start date)
  - **FX fields** = auto-calculated by Agentnoon (Span of Control, Layer, Total Org Size)
- **Screenshot:** Edit panel showing position fields and people fields in groups

### Slide 11 — Spans & Layers
- **Purpose:** Introduce the two key structural metrics
- **Content:**
  - **Span of Control (SOC)** = number of direct reports for a given position
  - Healthy range: 5–10 for most roles; <3 suggests compression; >15 suggests overload
  - **Layers** = number of management levels between a position and the CEO
  - Industry best practice: 4–7 layers depending on org size
  - Both are calculated automatically and update as you make changes
- **Screenshot:** Org chart with SOC and Layer values visible on cards

### Slide 12 — Views: Org Chart vs Directory
- **Purpose:** Two ways to see the same data
- **Content:**
  - **Org Chart** = visual, hierarchical — best for structure, reporting lines, drag-and-drop
  - **Directory** = table/spreadsheet — best for bulk analysis, sorting, filtering, exporting
  - Switch between them anytime (keyboard shortcut: 1 for Org Chart, 2 for Directory)
  - Filters persist when switching views
- **Screenshot:** Split view showing org chart on left, directory on right

### Slide 13 — Permissions & Access
- **Purpose:** Brief overview of who can do what
- **Content:**
  - **Viewer** — Can see data, cannot edit
  - **Planner** — Can create and edit scenarios
  - **Approver** — Can approve scenario changes
  - **Admin** — Full system access and configuration
  - Access Groups control which data you can see (scoped by department, location, etc.)
  - Your admin configures your access level
- **Screenshot:** Simplified permissions matrix or Access Control panel

---

## PART 3 — NAVIGATING MAIN ORG (Slides 14–20)

### Slide 14 — Entering Main Org
- **Purpose:** Get the user into the live org chart
- **Content:**
  - Click "Open Org Chart" from the homepage
  - Main Org is view-only — you cannot add, edit, or delete positions here
  - This is your current-state baseline, reflecting data from your HRIS or import
  - Use Main Org to explore, understand, and analyze before planning changes
- **Screenshot:** Main Org view with the view-only indicator highlighted

### Slide 15 — Navigating the Org Chart
- **Purpose:** Teach basic movement and exploration
- **Content:**
  - Scroll and zoom to explore different areas
  - Click expand/collapse arrows to show or hide reporting lines
  - Hover over a card for quick details
  - Use the layout options: Vertical, Horizontal, Compact
  - Set expansion levels (1–3) to control how much of the org is visible
- **Screenshot:** Org chart with expand/collapse and layout controls annotated

### Slide 16 — Searching for People & Positions
- **Purpose:** Find anyone or any role quickly
- **Content:**
  - Use the search bar (shortcut: Cmd/Ctrl+K or /)
  - Search by name, job title, employee ID, or position ID
  - Results appear as you type — click a result to navigate directly to that card
  - Works across your entire accessible scope
- **Screenshot:** Search bar with results dropdown

### Slide 17 — Filtering & Highlighting
- **Purpose:** Focus on specific parts of the org
- **Content:**
  - **Filter:** Click Filter in toolbar → select criteria (department, location, etc.) → Apply
    - Option: "Preserve manager relationships" maintains reporting context
  - **Highlight:** Click Highlight → choose an attribute → cards color-code automatically
    - Fill Color for background, Outline Color for borders
  - Combine filters and highlights to surface specific patterns
- **Screenshot:** Filtered + highlighted org chart with legend visible

### Slide 18 — Customizing Card Content
- **Purpose:** Control what information is visible at a glance
- **Content:**
  - Click "Card Content" in the toolbar
  - Check/uncheck fields to add or remove them from cards (salary, department, location, etc.)
  - Include FX fields like Span of Control or Total Org Size for added insight
  - Use the gear button to rearrange field display order
  - Changes apply immediately to all visible cards
- **Screenshot:** Card Content panel with a few fields selected, showing updated cards

### Slide 19 — Spotlight & Saved Views
- **Purpose:** Identify patterns and save configurations for reuse
- **Content:**
  - **Spotlight:** Dims non-matching positions to highlight specific rules (e.g., SOC > 15, specific pay grades)
  - **Saved Views:** After configuring filters, highlights, and card content → click Views → Save Current View
  - Name your views clearly (e.g., "Engineering Team," "US Employees," "SOC Analysis")
  - Saved views appear in the Views dropdown for quick access later
- **Screenshot:** Spotlight active with matching positions highlighted; Views dropdown

### Slide 20 — Main Org: Key Takeaways
- **Purpose:** Summarize before moving to Scenarios
- **Content:**
  - Main Org is your read-only baseline — explore, don't edit
  - Use Search, Filter, Highlight, and Spotlight to find patterns
  - Customize Card Content to see the data that matters to you
  - Save Views to quickly return to useful configurations
  - You're now ready to start modeling changes in a Scenario
- **Screenshot:** None (summary slide with key icons/bullets)

---

## PART 4 — YOUR FIRST SCENARIO (Slides 21–32)

### Slide 21 — What is a Scenario?
- **Purpose:** Transition from viewing to planning
- **Content:**
  - A scenario is an editable copy of your org where you model changes without affecting live data
  - Think of it as a "sandbox" — experiment freely, nothing is permanent until implemented
  - Use scenarios to plan reorganizations, model hiring, test budget cuts, explore alternatives
  - You can create unlimited scenarios and compare them
- **Screenshot:** Scenario list on homepage showing a few example scenarios

### Slide 22 — Creating a Scenario
- **Purpose:** Step-by-step creation walkthrough
- **Content:**
  - Return to the Homepage → click "+ Create Scenario"
  - Choose a type:
    - **Full Org** — Copy of your entire organization (company-wide planning)
    - **Partial Org** — Copy of a specific department or team (most common)
    - **New Org** — Blank canvas (building a new team from scratch)
  - Name it clearly: [Area] [Purpose] [Time Period] (e.g., "Engineering Q2 Reorg")
  - Optional: set a budget target, effective date, and description
- **Screenshot:** Scenario creation dialog with type selection and naming

### Slide 23 — Scenario Interface Orientation
- **Purpose:** Orient the user to the scenario workspace
- **Content:**
  - The scenario interface looks like Main Org but is fully editable
  - Key differences: scenario name in top bar, editing tools active, OpEx Panel available
  - Module switcher (top): Org Chart, Directory, Forecast, Workforce Hub
  - Toolbar (top): Search, Filter, Highlight, Card Content, Spotlight, Views
  - Side tools: Activity Log, Share, Export, Comments
  - Before/After/Changes toggle lets you compare your changes against the baseline
- **Screenshot:** Annotated scenario interface with key elements labeled

### Slide 24 — Adding a Position
- **Purpose:** First hands-on action
- **Content:**
  - Hover over a card in the org chart → click the **+** button
  - A new position is created as a direct report to the selected card
  - Fill in details: job title, department, salary, location, hire date, etc.
  - The new position appears in green (indicating an addition)
  - Set a hire date if this is a planned future hire
- **Screenshot:** Adding a position — hover state showing + button, then the new card in green

### Slide 25 — Editing a Position
- **Purpose:** Modify existing role details
- **Content:**
  - Click on any card to open the detail panel
  - Modify fields: title, department, salary, location, pay grade, etc.
  - Save changes — the card updates immediately
  - Edited positions appear with a blue indicator (modification)
  - All changes are tracked in the OpEx Panel
- **Screenshot:** Edit panel open with fields being modified

### Slide 26 — Moving a Position (Drag & Drop)
- **Purpose:** Restructure reporting lines
- **Content:**
  - **Move an individual:** Drag a card and drop it on a new manager
  - **Move a team:** Select the manager's card → click "Change Manager" → choose the new manager → the entire team moves together
  - Moved positions appear with a purple indicator
  - This is the core mechanic for reorganizations
- **Screenshot:** Drag-and-drop in action; team move via Change Manager

### Slide 27 — Closing a Position
- **Purpose:** Model reductions and exits
- **Content:**
  - Click on a card → select "Close Position" from the menu
  - Choose a reason: **RIF** (reduction in force / layoff) or **Exit** (voluntary departure)
  - Optionally set a termination date for time-phased planning
  - Closed positions appear in red (reduction)
  - The cost savings immediately reflect in the OpEx Panel
- **Screenshot:** Close position menu with RIF/Exit options; red card

### Slide 28 — Working with People (Assign, Detach, Bench)
- **Purpose:** Manage the people-to-position relationship
- **Content:**
  - **Assign:** Click a vacant position → Assign Employee → select from the employee list
  - **Detach:** Remove an employee from a position (position stays, person goes to the Bench)
  - **Bench:** A holding area for unassigned employees during restructuring
  - Common use: detach someone from their old role, assign them to a new one (internal transfer)
  - Employee salary follows them when moved between positions
- **Screenshot:** Assign/Detach flow; Bench panel

### Slide 29 — Bulk Operations
- **Purpose:** Make changes at scale
- **Content:**
  - Select multiple positions: Cmd/Ctrl+click in org chart, or use "Select Team," or checkboxes in Directory
  - Bulk actions: Edit Attributes, Change Manager, Close Positions, Detach Employees, Duplicate
  - Example: select 10 positions → Edit → change Department to "Product" → Save
  - Ideal for reorganizations affecting many roles at once
  - All bulk changes are tracked individually in the OpEx Panel
- **Screenshot:** Multi-select in org chart with bulk action menu

### Slide 30 — Understanding Change Indicators
- **Purpose:** Decode the visual language of scenarios
- **Content:**
  - **Green** = Addition (new position)
  - **Red** = Reduction (RIF or Exit)
  - **Blue** = Modification (data change)
  - **Purple** = Move (new manager/department)
  - **White/No color** = Unchanged
  - Use the Before/After/Changes toggle to isolate what you've changed
  - "Show Changes" filters the view to only modified positions
- **Screenshot:** Org chart showing all change types color-coded

### Slide 31 — Setting Effective Dates
- **Purpose:** Phase changes over time
- **Content:**
  - Assign an effective date to any change to control when it takes effect
  - **Hire Date** — When a new position becomes active
  - **Termination Date** — When a closed position is eliminated
  - **Effective Date** — When a modification (move, title change, salary change) takes effect
  - Effective dates feed directly into Forecast, showing phased impact by month/quarter
  - Example: 5 hires in Q1, 3 in Q2 — each appears in Forecast at the right time
- **Screenshot:** Effective date being set on a position; Forecast showing phased impact

### Slide 32 — Scenario Walkthrough: Recap
- **Purpose:** Summarize the scenario workflow before moving to impact analysis
- **Content:**
  - You've learned to: create a scenario, add positions, edit details, move roles, close positions, assign people, use bulk operations, and set effective dates
  - Every change is tracked with color-coded indicators
  - Nothing affects your live data — this is all in the sandbox
  - Next: let's see the impact of your changes
- **Screenshot:** None (summary slide with workflow icons)

---

## PART 5 — REVIEWING IMPACT (Slides 33–38)

### Slide 33 — The OpEx Panel
- **Purpose:** Introduce the primary impact-tracking tool
- **Content:**
  - The OpEx Panel is your real-time dashboard for every change in a scenario
  - Shows: total additions, reductions, modifications, and net headcount/cost impact
  - Groups changes by type: Additions, Reductions, Data Changes
  - Click any change to navigate directly to that position in the org chart
  - Check the OpEx Panel frequently to track progress against your goals
- **Screenshot:** OpEx Panel with additions, reductions, and net impact visible

### Slide 34 — OpEx Panel: Effective Date View
- **Purpose:** See changes organized by when they take effect
- **Content:**
  - Toggle to the "Effective Date" view to see changes grouped by their effective date
  - Useful for phased rollouts: see exactly what happens each month or quarter
  - Combine with budget targets to ensure you're pacing changes correctly
  - Download change data via the Activity Log for offline review
- **Screenshot:** OpEx Panel in Effective Date view showing changes by quarter

### Slide 35 — Viewing Impact in Forecast
- **Purpose:** See the time-phased projection
- **Content:**
  - Switch to Forecast via the view switcher (or keyboard shortcut: 3)
  - The timeline shows projected headcount or cost by month/quarter/year
  - Toggle between Headcount and Cost metrics
  - Use Before/After/Changes to compare baseline vs. planned state
  - Hover over any point for a detailed breakdown
  - Changes appear based on their effective/hire/termination dates
- **Screenshot:** Forecast view showing headcount over time with Before/After comparison

### Slide 36 — Configuring Forecast
- **Purpose:** Customize the Forecast view for your needs
- **Content:**
  - **Row Aggregator:** Group by Department, Location, Pay Grade, People, or any custom field
  - **Time Period:** Monthly (precise), Quarterly (standard for budget reviews), Yearly (strategic/5-year)
  - **Metric:** Headcount (position count) or Cost (salary-based, with individual compensation components available)
  - **Before/After/Changes:** Show baseline, final state, or delta only
  - Export to CSV for offline analysis or stakeholder reporting
- **Screenshot:** Forecast configuration options (aggregator, time period, metric toggles)

### Slide 37 — Validating with Workforce Hub
- **Purpose:** Use analytics to sanity-check your changes
- **Content:**
  - Switch to Workforce Hub via the view switcher (or keyboard shortcut: 4)
  - Inside a scenario, charts show the impact of your proposed changes
  - Toggle Before/After to compare org structure metrics
  - Key charts to check:
    - **Layers & Spans of Control** — Is your reorg creating compression or overload?
    - **Headcount Distribution** — Is the org shape healthy (pyramid vs. diamond)?
  - Export charts for stakeholder presentations
- **Screenshot:** Workforce Hub chart with Before/After toggle in a scenario

### Slide 38 — Impact Review: Key Takeaways
- **Purpose:** Summarize impact review tools
- **Content:**
  - **OpEx Panel** — Real-time change tracker (cost + headcount impact)
  - **Forecast** — Time-phased projections (monthly, quarterly, yearly)
  - **Workforce Hub** — Structural validation (SOC, layers, distribution)
  - Always review all three before submitting a scenario for approval
  - Together they give you a complete picture: what changed, how much it costs, and what it means structurally
- **Screenshot:** None (summary slide with three tool icons)

---

## PART 6 — COLLABORATION & APPROVALS (Slides 39–43)

### Slide 39 — Sharing a Scenario
- **Purpose:** Get the right people involved
- **Content:**
  - Click the Share button in the left panel → enter emails → choose access level
  - **View Only** — Can see the scenario but not edit (for leadership review)
  - **Comment Only** — Can view and leave feedback (for reviewers)
  - **Edit Access** — Can make changes (for collaborative planning)
  - Sharing respects existing access group permissions (users can only see data in their scope)
- **Screenshot:** Share dialog with access level options

### Slide 40 — Commenting
- **Purpose:** Document decisions and gather feedback
- **Content:**
  - Open the Comments panel from the side toolbar
  - Add scenario-level comments for general feedback, questions, or decision documentation
  - Comments can also be added on individual positions for targeted feedback
  - Resolve comments when addressed (keeps a record but removes from active view)
  - Use comments to build an audit trail of planning decisions
- **Screenshot:** Comments panel with a few example comments

### Slide 41 — Real-Time Collaboration
- **Purpose:** Work together simultaneously
- **Content:**
  - Profile icons at the top show who currently has the scenario open
  - Best practice: announce which section you're working on to avoid conflicts
  - Divide work by department or team to minimize overlap
  - Limit concurrent editors to 2–3 for best results
  - Review together before submitting for approval
- **Screenshot:** Presence indicators showing multiple collaborators

### Slide 42 — Submitting for Approval
- **Purpose:** Walk through the approval submission process
- **Content:**
  - When your scenario is ready, go to the OpEx Panel → click "Submit"
  - Add a justification explaining the changes and rationale
  - The scenario enters the approval workflow:
    - **Level 0** (optional) → **Level 1** → **Level 2** → **Level 3** (optional)
  - Approvers receive a notification and review the scenario
  - Once approved, the scenario locks to prevent further edits
- **Screenshot:** Submission dialog with justification field; approval flow diagram

### Slide 43 — The Approval Lifecycle
- **Purpose:** Understand what happens after submission
- **Content:**
  - **Draft** → scenario is being built (editable)
  - **Submitted** → waiting for approval (locked for editing)
  - **Approved** → all approvers have signed off (locked)
  - **Rejected** → returned for revisions (unlocked, editable again)
  - If rejected: make changes, then resubmit with updated justification
  - Admin can "un-submit" a scenario if changes are needed before approval completes
- **Screenshot:** Approval status badges / lifecycle diagram

---

## PART 7 — EXPORTING & COMMUNICATING (Slides 44–47)

### Slide 44 — Exporting from the Org Chart
- **Purpose:** Get visuals out for presentations
- **Content:**
  - Click Export in the toolbar
  - **JPEG** — Quick screenshot of the current org chart view
  - **PowerPoint** — Structured export with configurable depth, layout, and card content
  - PowerPoint options: filter scope, set hierarchy depth, choose slide layout, select which fields appear on cards
  - Exports respect your current filters and highlighting
- **Screenshot:** Export dialog with PowerPoint configuration options

### Slide 45 — Exporting Data from Directory & Forecast
- **Purpose:** Get structured data for analysis
- **Content:**
  - **Directory:** Click Export → CSV or Excel → includes visible columns and active filters only
  - **Forecast:** Export projection tables as CSV with your selected aggregator, time period, and metric
  - **Change Summary:** Download from OpEx Panel — lists all changes with cost/headcount impact
  - Tip: apply filters before exporting to get targeted, relevant data
- **Screenshot:** Directory export and Forecast export examples

### Slide 46 — Exporting Charts from Workforce Hub
- **Purpose:** Create presentation-ready analytics
- **Content:**
  - Open any chart in Workforce Hub → click Export
  - **PNG** — Static image for documents
  - **PowerPoint** — Editable chart object for presentations
  - **CSV** — Raw data for custom analysis
  - **Slide Packs** — Multi-chart presentations with customizable slides (see Appendix A6)
  - Charts export with your current filters and configuration applied
- **Screenshot:** Chart export options; example exported PowerPoint slide

### Slide 47 — Scenario Comparisons Export
- **Purpose:** Present multiple options to decision-makers
- **Content:**
  - From the homepage, select two scenarios → click Compare
  - View side-by-side: cost, headcount, org chart, pyramid chart, key metrics
  - Export the comparison as Excel (multi-sheet), CSV, or PowerPoint
  - Ideal for presenting Option A vs. Option B to leadership
  - Can also compare a scenario against Main Org (current state vs. proposed)
- **Screenshot:** Scenario comparison view with export options

---

## PART 8 — WRAP-UP (Slides 48–50)

### Slide 48 — The Agentnoon Workflow (Recap)
- **Purpose:** Reinforce the end-to-end workflow
- **Content:**
  - **1. Explore** — Navigate Main Org to understand your current state
  - **2. Analyze** — Use Workforce Hub to identify opportunities and issues
  - **3. Plan** — Create scenarios to model proposed changes
  - **4. Review** — Check impact via OpEx Panel, Forecast, and Workforce Hub
  - **5. Collaborate** — Share, comment, and refine with your team
  - **6. Approve** — Submit for approval through the defined workflow
  - **7. Communicate** — Export data, charts, and comparisons for stakeholders
- **Screenshot:** Workflow diagram (circular or linear) showing all 7 steps

### Slide 49 — You're Ready!
- **Purpose:** Confidence-building summary
- **Content:**
  - If you can navigate Main Org, create a scenario, make changes, review impact, and export insights — you're ready to plan with confidence
  - Start small: create a Partial Org scenario for your team and try adding, editing, and moving a few positions
  - Review the OpEx Panel and Forecast to see how your changes play out
  - Use the Appendix for reference on advanced features as you need them
- **Screenshot:** None (motivational summary slide)

### Slide 50 — Getting Help & Next Steps
- **Purpose:** Point to resources and support
- **Content:**
  - **Help Center:** Your first stop for documentation and guides
  - **Video Tutorials:** ~30-minute learning path for new users
  - **Support Email:** SupportSWP@dayforce.com
  - **Quick fixes:** Refresh page, clear cache, try Chrome, log out/in
  - **When contacting support:** Include your org name, what happened, screenshots, and browser/OS
  - See Appendix C for keyboard shortcuts, glossary, and self-help guide
- **Screenshot:** Help Center homepage / support contact card

---

## APPENDIX A — FEATURE BRIEFINGS (Slides A1–A10)

> Each appendix slide follows the format: What is it? | How to set it up | How to use it once set up

### Slide A1 — Scenario Comparisons (Deep Dive)
- **What:** Compare two scenarios side-by-side on cost, headcount, org structure, and key metrics
- **Setup:** Create 2+ scenarios with different approaches (e.g., Option A vs. Option B)
- **Usage:** Homepage → select two scenarios → Compare → review Cost, Headcount, Org Chart, Pyramid Chart, Key Metrics → export as Excel/CSV/PowerPoint
- **Screenshot:** Comparison view with side-by-side metrics

### Slide A2 — Scenario Merging
- **What:** Consolidate changes from one scenario (source) into another (destination)
- **Setup:** Best when independent teams work on non-overlapping parts of the org; create separate scenarios for each team
- **Usage:** Open destination scenario → Data Management → Merge Scenario → select source → choose records/fields → review conflicts → merge. An automatic backup is created before merging. Conflicts resolved on an all-or-nothing basis (source wins)
- **Screenshot:** Merge scenario dialog

### Slide A3 — Scenario to Main Org
- **What:** Apply an approved scenario's changes to the live Main Org
- **Setup:** Scenario must be fully approved; admin-only operation; permanent action
- **Usage:** Main Org → Data Management → Merge Approved Scenarios → select scenario → choose fields → Include New Positions checkbox → review conflicts → merge → verify in Main Org → notify stakeholders → archive scenario
- **Screenshot:** Merge to Main Org dialog

### Slide A4 — Time-Based Planning (Deep Dive)
- **What:** Phase changes over time using hire dates, termination dates, and effective dates
- **Setup:** Make changes in a scenario and assign dates to each change
- **Usage:** Hire Date = when a new position becomes active; Termination Date = when a position is eliminated; Effective Date = when a modification takes effect. View in Forecast to see the phased timeline. Forecast extends 5 years from today. Example: stagger 10 hires across Q1–Q3 for a realistic rollout
- **Screenshot:** Forecast showing phased hiring over multiple quarters

### Slide A5 — Directory (Deep Dive)
- **What:** Table/spreadsheet view of all positions and employees with sortable, filterable columns
- **Setup:** Access from any module via view switcher (shortcut: 2)
- **Usage:** Sort single or multiple columns; filter by any attribute (AND logic); customize visible columns; search by name/title. In scenarios: select rows for bulk edits, view color-coded changes (green/red/blue). Export CSV/Excel with visible columns and active filters
- **Screenshot:** Directory view with filters and color-coded scenario changes

### Slide A6 — Workforce Hub: Slide Packs
- **What:** Multi-chart presentations built from Workforce Hub analytics
- **Setup:** Workforce Hub → Go to Slide Pack → create blank pack or use a template
- **Usage:** Add slides → assign chart type to each → configure filters and axes → title each slide. Filters are memorized across sessions. Lock slides to prevent editing during collaboration. Export as PowerPoint (.pptx). Share with collaborators who have Hub access
- **Screenshot:** Slide Pack builder with multiple charts configured

### Slide A7 — Activity Analysis
- **What:** Map business activities and allocate effort (FTE %) across the organization
- **Setup:** Select a scenario → click Activity Analysis icon → add Level 1 processes (e.g., Sales, Finance) → add Level 2 activities under each
- **Usage:** Assign positions to activities with time percentage allocation; categorize as Value Add or Non-Value Add; analyze effort distribution in Workforce Hub using the Activity Split chart; view by FTE Count or Cost; filter by activity level
- **Screenshot:** Activity Analysis tree with assigned positions and percentages

### Slide A8 — Partial Data Upload
- **What:** Update specific records in Main Org or a scenario without replacing the entire dataset
- **Setup:** Prepare a CSV with: unique identifier (Employee ID or Position ID), Manager ID (for new positions), and only the fields you want to update
- **Usage:** Data Management → Partial Upload → choose file → upload → map fields → system matches by identifier → existing records update, new records are added → changed cards marked with orange edit icon
- **Screenshot:** Partial upload mapping dialog

### Slide A9 — Formulas (Custom Calculated Fields)
- **What:** Create custom calculated fields using natural language logic
- **Setup:** Navigate to Attributes & Formulas → select variables → write logic
- **Usage:** Supported functions: ifElse, in, min, max, arithmetic operations. Apply conditional rules based on position/employee attributes. Example: severance calculation based on RIF state, years of service, and employee level. Custom formulas appear alongside standard FX fields
- **Screenshot:** Formula builder with example severance formula

### Slide A10 — Forecast: Multi-Year Planning
- **What:** Project workforce costs and headcount up to 5 years into the future
- **Setup:** Create scenarios with hire dates spanning multiple years; set Forecast to Yearly time period
- **Usage:** Compare Conservative, Moderate, and Aggressive growth scenarios; toggle between Headcount and Cost; view by Department, Location, or any custom field. Plan in phases: Year 1 detailed, Year 2 moderate, Year 3+ directional. Present ranges rather than exact numbers for long-term plans
- **Screenshot:** 5-year Forecast view showing yearly headcount and cost projections

---

## APPENDIX B — ADMIN CAPABILITIES (Slides B1–B5)

### Slide B1 — Data Upload & Management
- **What:** Import and maintain organizational data in Agentnoon
- **Setup:** Prepare CSV with required fields: Position ID, Manager Position ID, Job Title (minimum). Recommended: Department, Location, Name, Employee ID, Start Date, Salary
- **Usage:** Data Management → Upload → map columns to Agentnoon fields → validate → import. Full upload replaces all Main Org data. Partial upload updates specific records. Automated sync available via SFTP, Workday API, or REST API. Recommended refresh: weekly (Sunday/Monday)
- **Screenshot:** Data upload mapping interface

### Slide B2 — Access Control & User Management
- **What:** Control who can see and do what in Agentnoon
- **Setup:** Create Access Groups → define field-level permissions (View, Edit, Hidden) → configure feature access (exports, forecast, scenarios) → invite users → assign Access Group and Scope
- **Usage:** Access Groups = what fields a user can see/edit. Scopes = which records (people/positions) a user can see (scoped by manager, department, etc.). Invite users individually or in bulk. Replicate access from an existing user for quick setup. Export access logs for compliance
- **Screenshot:** Access Group configuration panel with field permissions

### Slide B3 — Rate Cards (Compensation Bands)
- **What:** Auto-populate salary fields based on role attributes (like a VLOOKUP)
- **Setup:** Download the rate card CSV template → fill in compensation bands by Level, Location, Role Type, etc. → upload via Data Management → map the independent attributes (source) and the dependent field (salary)
- **Usage:** When a new position is created in a scenario with matching attributes, salary auto-populates. Enable Rate Card display in Card Content to show the suggested salary alongside actual salary. Group rate card fields for organization
- **Screenshot:** Rate card CSV example; auto-populated salary on a new position

### Slide B4 — Auto Mapping
- **What:** Automatically populate dependent fields when a source field changes
- **Setup:** Create a mapping rule → upload a CSV with the source attribute(s) and dependent attributes → select the independent attribute (e.g., National Department) → remaining columns become auto-populated fields
- **Usage:** When a user changes the source attribute on a position, all mapped dependent fields update automatically. Works on both existing and new records. Useful for standardizing regional terminology, populating cost centers, and maintaining consistency
- **Screenshot:** Auto Mapping rule creation with CSV example

### Slide B5 — Configuring Approval Flows
- **What:** Set up multi-level review and approval for scenario changes
- **Setup:** Settings → General → Approval Workflows → assign Level 1 approvers (e.g., HRBPs, department heads) and Level 2 approvers (e.g., CFO, COO). Level 0 and Level 3 are set per-scenario by the creator
- **Usage:** 4-level system: Level 0 (scenario-specific pre-check) → Level 1 (global checkers) → Level 2 (global decision-makers) → Level 3 (scenario-specific final). Approvers receive notifications → review OpEx Panel → approve or reject with reason. Rejected scenarios unlock for revision. Common designs: Simple (2-level), Standard (3-level), Complex (4-level)
- **Screenshot:** Approval workflow configuration in Settings; approval notification example

---

## APPENDIX C — QUICK REFERENCE (Slides C1–C3)

### Slide C1 — Keyboard Shortcuts
- **What:** Productivity shortcuts for power users
- **Content:**
  - **Module navigation:** 1 = Org Chart, 2 = Directory, 3 = Forecast, 4 = Workforce Hub, 5 = Activity Analysis
  - **Search:** Cmd/Ctrl+K or /
  - **Directory:** x = select row, j = next row, k = previous row, p = profile, o = org chart
  - **Scenario:** x = select card
  - **General:** Esc = close panel/deselect
- **Screenshot:** Keyboard shortcut reference card

### Slide C2 — Glossary of Key Terms
- **What:** Quick-reference definitions for Agentnoon terminology
- **Content (selected terms):**
  - **Position** — A job role in the org (filled or vacant)
  - **Main Org** — Current-state, view-only organization
  - **Scenario** — Editable copy for planning changes
  - **OpEx Panel** — Real-time cost and headcount impact tracker
  - **SOC** — Span of Control (number of direct reports)
  - **Layer** — Distance from CEO in the hierarchy
  - **RIF** — Reduction in Force (layoff)
  - **FX Field** — Auto-calculated field (Span of Control, Layer, etc.)
  - **Access Group** — Permission set controlling data visibility
  - **Rate Card** — Compensation band lookup table
  - (Full glossary available in Help Center)
- **Screenshot:** None (reference table)

### Slide C3 — Support & Self-Help
- **What:** How to get help when you're stuck
- **Content:**
  - **Quick fixes to try first:** Refresh page, clear cache, try Chrome, log out/in, try incognito mode
  - **Help Center:** Search the docs for guides, FAQs, and troubleshooting
  - **Video Tutorials:** ~30 minutes for new users, ~60 minutes for admins
  - **Support Email:** SupportSWP@dayforce.com
  - **Include in support requests:** Organization name, what happened, steps to reproduce, screenshots, browser/OS info
  - **Tip:** Contact your organizational admin first — they may be able to resolve access or data issues directly
- **Screenshot:** Help Center search bar; support email template

---

## APPENDIX — USE CASE QUICK REFERENCES (Optional Expansion)

> These slides could be added if the deck needs deeper use-case coverage. Each follows the pattern: Goal → Setup → Step-by-step → Key metrics to check → Export for stakeholders.

### Slide U1 — Use Case: Planning a Reorganization
- Goal: Model structural changes before implementing them
- Steps: Analyze current SOC → Define goals → Create Partial Org scenario → Move teams/positions → Check SOC and layers → Compare 2–3 options → Submit for approval
- Key metrics: Span of Control, Layers, Headcount by Department

### Slide U2 — Use Case: Span of Control Analysis
- Goal: Identify and address management compression or overload
- Steps: Open Workforce Hub → Layers & Spans chart → Identify 1-2 SOC managers and 15+ SOC managers → Use Spotlight on org chart → Create scenario to rebalance → Compare before/after
- Key metrics: SOC distribution, Manager-to-IC ratio, 1:1 Managers Ratio

### Slide U3 — Use Case: Building an Annual Hiring Plan
- Goal: Model phased headcount growth and budget impact
- Steps: Gather department inputs → Create 2-3 scenarios (Conservative, Target, Aggressive) → Add positions with hire dates → Use Rate Cards for salary → View Forecast quarterly → Compare scenarios → Submit for approval
- Key metrics: Headcount by quarter, Cost by quarter, Budget variance

### Slide U4 — Use Case: M&A Integration
- Goal: Plan post-acquisition organizational integration
- Steps: Create Full Org scenario → Upload acquired company via Partial Upload → Consolidate leadership → Integrate departments → Analyze cost synergies → Compare integration approaches (Fast/Moderate/Slow) → Export for executive review
- Key metrics: Total headcount, Cost savings, Redundancy count, SOC post-integration

---

## SLIDE COUNT SUMMARY

| Section | Slide Range | Count |
|---|---|---|
| Part 1 — Welcome & Orientation | 1–6 | 6 |
| Part 2 — Key Concepts | 7–13 | 7 |
| Part 3 — Navigating Main Org | 14–20 | 7 |
| Part 4 — Your First Scenario | 21–32 | 12 |
| Part 5 — Reviewing Impact | 33–38 | 6 |
| Part 6 — Collaboration & Approvals | 39–43 | 5 |
| Part 7 — Exporting & Communicating | 44–47 | 4 |
| Part 8 — Wrap-Up | 48–50 | 3 |
| **Core Total** | | **50** |
| Appendix A — Feature Briefings | A1–A10 | 10 |
| Appendix B — Admin Capabilities | B1–B5 | 5 |
| Appendix C — Quick Reference | C1–C3 | 3 |
| Appendix U — Use Case Quick Refs (optional) | U1–U4 | 4 |
| **Appendix Total** | | **18–22** |
| **Grand Total** | | **68–72** |

---

## NOTES FOR CONTENT CREATION PHASE

1. **Slide format standard:** Each slide should have:
   - **Title** (bold, top)
   - **Lead-line** (one sentence summarizing the slide's message)
   - **Key details** (bulleted list, left side — 3–5 bullets max)
   - **Screenshot placeholder** (right side — with description of what screenshot to use)

2. **Screenshot sources:** Most screenshots already exist in the documentation's `.gitbook/assets/` folder and can be referenced directly.

3. **Tone:** Instructional but approachable. Second person ("you"). Active voice. No jargon without definition.

4. **Progressive disclosure:** Core slides teach concepts in order of need. Appendix provides depth on demand. A user should never need the appendix to complete basic workflows.

5. **Optional expansion:** If the deck needs to grow toward the 120-slide maximum, the Use Case appendix (U1–U4) can each be expanded into 3–5 slide mini-tutorials following the existing use-case-tutorials documentation.
