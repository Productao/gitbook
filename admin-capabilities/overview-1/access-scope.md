---
description: Assign access scopes to manage area of the organizations users have access to
icon: universal-access
---

# Access Scope

## **Understanding Access Scopes**

Access scopes control which people a user can access in Agentnoon.

If access groups define what someone can view or edit, access scopes define who those permissions apply to.

### **What access scopes are**

An access scope is a set of filters that narrows a user’s access to a specific part of the organization.

You can use access scopes to give someone access to:

* the entire company
* one or more departments
* one or more locations
* one or more manager hierarchies
* people who match selected custom field values (Business unit, Entity, etc)

This lets you give users the access they need without exposing the whole organization.

### **Why access scopes are useful**

Access scopes are helpful when a user should only work with a specific part of the business.

Common examples:

* an HR business partner who supports only Engineering
* a regional leader who should only see one office or country
* a people manager who should only access their reporting structure
* a specialist who works with a defined employee segment
* a user who should see a broad area, except for one excluded group

### **The main types of access scopes**

#### **Entire company**

If no filters are selected in a scope, that scope behaves like an entire-company scope.

Use this when the user’s permissions should apply across the whole board.

#### **Filtered scopes**

These are the most common scopes. They include people based on filters such as:

* Department
* Location
* Manager
* Custom fields
* Sensitive data

Manager-based scopes include the selected manager and their full reporting tree, so they work well when access should follow the org structure.

#### **Hidden scopes**

A hidden scope is used to exclude people.

This is not the same as hiding certain fields. A hidden scope removes matching people from the user’s accessible set entirely.

Use hidden scopes when someone should see a broad group, but one part of it must be excluded.

#### **Layered scopes**

A user can have more than one visible scope.

This is useful when access needs to come from more than one rule. For example, a user may need access to:

* everyone in Engineering
* plus everyone on Project Team Alpha

In that case, both visible scopes work together.

### **How filters work inside one scope**

Each scope can combine fields using AND or OR.

#### **Use AND for narrower access**

With AND, a person must match every populated field in the scope.

Example:

* Department = Sales
* Manager = VP West
* Combine fields with AND

This includes only people who are both:

* in Sales
* and in VP West’s reporting tree

#### **Use OR for broader access**

With OR, a person can match any populated field in the scope.

Example:

* Department = Sales
* Manager = VP West
* Combine fields with OR

This includes people who are:

* in Sales
* or in VP West’s reporting tree
* or both

That same pattern applies to:

* multiple departments
* multiple locations
* multiple managers
* multiple custom field values
* multiple sensitive data values

So the rule is:

* within one field, selected values behave like OR
* across different fields, the scope uses AND or OR depending on the setting

### **How multiple scopes work together**

When a user has multiple visible scopes, those scopes stack by adding access together.

That means if a person matches any visible scope, they are included.

Example:

* Scope 1: Department = Engineering
* Scope 2: Custom Field = Project Team Alpha

The user can access:

* everyone in Engineering
* plus everyone on Project Team Alpha

If a hidden scope also exists, it removes matching people from that result.

Example:

* Visible scope: Department = Sales
* Hidden scope: Manager = VP West

The user can access Sales, except for the VP West hierarchy.

### **What happens when scopes overlap**

Sometimes the same person is included by more than one visible scope.

When that happens, Agentnoon treats scopes lower in the list as more specific for that person’s field-level permissions.

In plain language:

* lower scopes in the UI take priority when the same person is covered by multiple visible scopes

This matters most when overlapping scopes use different field permissions.

### **Examples**

#### **Example 1: Department-based access**

An HRBP supports Engineering only.

Use:

* one visible scope for Department = Engineering

#### **Example 2: Multi-location access**

A leader should see London and Toronto.

Use:

* one visible scope for Location = London, Toronto

Because values in the same field behave like OR, this includes either location.

#### **Example 3: Narrow access with AND**

A user should only see Sales employees under VP West.

Use:

* Department = Sales
* Manager = VP West
* Combine fields with AND

#### **Example 4: Broader access from multiple rules**

A user should see:

* everyone in Engineering
* plus everyone on Project Team Alpha

Use:

* two visible scopes\
  or
* one broader scope using OR

#### **Example 5: Broad access with one exclusion**

A user should see all of Sales except one leader’s organization.

Use:

* visible scope: Department = Sales
* hidden scope: Manager = that leader

### **Good to know**

* Admins always have full board access, regardless of the scopes listed for them.
* Hidden scopes cannot be the only scopes a user has.
* In scenarios, newly added positions and certain related employees can appear even if they would normally sit outside a user’s main-board scope.
* If a project has its own filters, the user’s final access is the intersection of the project filter and their access scopes.

### **Summary**

Access scopes answer one question: which people should this user be able to access?

Use them to give access to:

* the whole company
* selected departments, locations, or manager hierarchies
* specific employee segments
* layered combinations of those rules

Visible scopes add access. Hidden scopes remove access. And when visible scopes overlap, lower scopes in the list are treated as more specific.
