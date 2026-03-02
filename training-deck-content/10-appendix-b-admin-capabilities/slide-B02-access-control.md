# Slide B2 — Access Control & User Management

## Title
Access Control & User Management

## Lead-line
Control who sees what data and what they can do — the two dimensions of access in Agentnoon.

## What Is It?
Access Control in Agentnoon has two dimensions: **Access Groups** (what fields a user can see/edit) and **Scopes** (which records a user can see). Together, they ensure every user sees only the data relevant to their role.

## How to Set It Up
**Create Access Groups:**
1. Navigate to the **Access Control** panel
2. Create a new Access Group (e.g., "HR Business Partner," "Finance Viewer," "Department Lead")
3. Set **field-level permissions** for each group:
   - **View** — User can see the field (read-only)
   - **Edit** — User can modify the field in scenarios
   - **Hidden** — Field is not visible to the user
4. Configure **feature access** — lock or unlock exports, forecast, scenarios, etc.

**Invite Users:**
1. Click **Invite User** → enter name and email (bulk invite supported)
2. Assign an **Access Group** (field permissions)
3. Set a **Scope** (which records they see):
   - **Manager Scope** — User sees a specific manager and everyone below them
   - **Filter-based Scope** — User sees records matching specific criteria (department, location, etc.)
   - **Select All Data** — User sees the entire organization
4. Users receive an email invitation to set up their account

## Key Concepts
- **Access Groups = field permissions** (what fields can they see/edit?)
- **Scopes = data visibility** (which positions/people can they see?)
- **Quick setup:** Replicate access from an existing user for similar roles
- **Compliance:** Export access logs to track who has access to what

## Screenshot / Visual
The Access Group configuration panel showing field-level permission settings (View/Edit/Hidden) organized by field category.

## Speaker Notes
Access control is one of the most important admin responsibilities. A common setup: create an "HR Business Partner" group with View/Edit access to most fields, a "Finance Viewer" group with View-only access to compensation data, and a "Department Lead" group with Edit access scoped to their own department. The scope setting is particularly important — it ensures department leads only see their own teams, even though they have the same Access Group permissions as other leads. Always follow the principle of least privilege: give users the minimum access they need to do their job.
