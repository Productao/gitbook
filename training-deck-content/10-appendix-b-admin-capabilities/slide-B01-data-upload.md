# Slide B1 — Data Upload & Management

## Title
Data Upload & Management

## Lead-line
Import and maintain your organizational data in Agentnoon — from initial setup to ongoing sync.

## What Is It?
Data Upload & Management is the admin process of getting organizational data into Agentnoon and keeping it current. This includes the initial import, ongoing refreshes, and automated sync options.

## How to Set It Up
**Required fields (minimum):**
- Position ID (unique identifier for each role)
- Manager's Position ID (who each role reports to)
- Job Title

**Recommended fields for greater functionality:**
- Department, Location, Employee Name, Employee ID, Start Date, Salary, Email

**Prepare your data:** CSV file with one row per position, clean headers, unique IDs, no circular reporting (A reports to B reports to A), YYYY-MM-DD date format, UTF-8 encoding.

## How to Use It
1. **Initial import:** Data Management → Upload → map CSV columns to Agentnoon fields → validate → import
2. **Full upload** replaces all Main Org data with the new file. Only data in the CSV will exist after upload.
3. **Partial upload** updates specific records — include Employee ID + only the changed columns. (See Appendix A8.)
4. **Automated sync options:**
   - **SFTP** — Schedule recurring file drops
   - **Workday API** — Direct integration with Workday
   - **REST API** — Custom integration with any HRIS
5. **Recommended refresh frequency:** Weekly (Sunday/Monday). Daily available for fast-moving orgs.
6. **Processing time:** 5–15 minutes for under 5,000 employees

## Screenshot / Visual
The data upload mapping interface showing CSV columns being matched to Agentnoon fields.

## Speaker Notes
Data quality is the foundation of everything in Agentnoon. Garbage in, garbage out. Before uploading, run through the Data Error Checklist in the Help Center — check for duplicate IDs, circular reporting chains, missing managers, and inconsistent formatting. The initial upload takes the most effort; after that, ongoing refreshes are usually automated. If you're using SFTP or API integrations, coordinate with your IT team on the connection setup.
