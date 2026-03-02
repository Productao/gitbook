# Slide B4 — Auto Mapping

## Title
Auto Mapping

## Lead-line
Automatically populate dependent fields when a source field changes — keep data consistent without manual work.

## What Is It?
Auto Mapping creates rules that automatically fill in related fields based on a trigger field. When a user changes the trigger field on a position, all mapped dependent fields update automatically. Think of it as a cascade: change one value, and related values follow.

## How to Set It Up
1. Go to **Settings** → **Auto Mapping**
2. **Create a new rule** with a name and description (e.g., "Department → Cost Center Mapping")
3. **Upload a CSV** with the mapping logic:
   - Column 1: The independent (trigger) attribute (e.g., National Department)
   - Remaining columns: The dependent attributes that auto-fill (e.g., Cost Center, Business Unit, Region)
4. **Select the independent attribute** — this is the field that triggers the auto-fill when changed
5. The remaining columns become the dependent fields
6. **Save and activate** the rule

## How to Use It
- When a user changes "National Department" to "Engineering" on a position, the system automatically sets Cost Center to "ENG-001," Business Unit to "Technology," and Region to "Global"
- Works on both **existing records** (when the trigger field is edited) and **new records** (when the trigger field is first set)
- Useful for: standardizing regional terminology, populating cost centers, maintaining data consistency across multiple related fields

## Example Mapping CSV
| National Department | Cost Center | Business Unit | Region |
|---|---|---|---|
| Engineering | ENG-001 | Technology | Global |
| Sales | SAL-002 | Revenue | Americas |
| Marketing | MKT-003 | Revenue | Global |
| Finance | FIN-004 | Corporate | Global |

## Screenshot / Visual
The Auto Mapping rule creation interface with the CSV upload and field selection.

## Speaker Notes
Auto Mapping eliminates one of the biggest sources of data inconsistency in workforce planning — manually entering related fields. Without it, when someone creates a new Engineering position, they have to remember that the cost center is "ENG-001" and the business unit is "Technology." With Auto Mapping, they just set the department and everything else fills in. This is especially valuable for organizations with complex field relationships — multiple cost centers, business units, regions, and other categorizations that need to stay in sync.
