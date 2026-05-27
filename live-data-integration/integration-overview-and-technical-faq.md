---
icon: comments-question-check
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/FQHYLeH687WAkUobefnf/live-data-integration/integration-overview-and-technical-faq
---

# Integration Overview & Technical FAQ

### Overview

This article describes how Agentnoon integrates with enterprise HR systems (such as Workday) to support organizational design, workforce planning, and scenario modelling. It is intended for technical and HRIT audiences responsible for data integrations, security, and platform architecture.

#### 1. Integration Principles

**What is the purpose of the Agentnoon integration?**

Agentnoon consumes workforce and organizational data from a customer’s system of record to enable:

* Organizational design and scenario modelling
* Headcount, span-of-control, and layer analysis
* Cost and workforce planning projections

Agentnoon is **not a system of record**. It is a planning and analytics platform that reflects source-system data and allows controlled modeling without altering upstream systems.

**Is the integration read-only or bi-directional?**

Most customers begin with a **one-way (read-only) integration** from their HR system into Agentnoon.

* Initial implementations focus on ingestion and modeling
* Bi-directional integrations (writing changes back to the HR system) are typically introduced later
* Bi-directional workflows are process-driven and customer-specific

Only a minority of customers implement bi-directional integrations, and usually after governance and approval workflows are mature.

**Does Agentnoon update data in the HR system?**

No, not in the initial implementation.

Organizational changes are:

1. Modeled and evaluated in Agentnoon
2. Approved outside the platform
3. Executed in the HR system using existing processes

Future-state integrations may allow approved scenarios to generate draft changes (e.g., positions or requisitions), depending on customer requirements.

#### 2. Data Requirements & Structure

**What data is required at a minimum?**

The minimum data required to construct an organizational hierarchy is:

* **Employee ID**
* **Manager ID**

All additional data fields are optional and configurable.

**What types of data can be ingested?**

Agentnoon can ingest any data associated with **employees or positions**, including:

* Job codes, job families, and titles
* Supervisory organization or reporting structure
* Location attributes
* Compensation data (salary, rate cards, projections)
* Demographic attributes
* Custom or calculated fields from the source system

Any field provided can be used in org charts, filters, analytics, and reporting.

**Do employee and position data need to be sent separately?**

No.

Agentnoon supports a **single flat file** that combines employee and position attributes.\
During configuration, fields are designated as either employee-level or position-level data.

#### 3. Data Refresh & Change Management

**How often should data be refreshed?**

Refresh cadence is configurable and customer-defined.

Common patterns include:

* **Weekly refresh** (most common; balances freshness and stability)
* **Daily refresh** (used in high-volume or fast-changing environments)

**Should full files or incremental changes be sent?**

_**Full file refreshes are strongly recommended.**_

Benefits include:

* Cleaner and more predictable data state
* Easier recovery from upstream data issues
* Lower long-term maintenance complexity

Incremental (delta-only) feeds are generally discouraged for initial implementations.

**How are terminated employees handled?**

Terminated employees are supported.

Customers define a retention window, commonly:

* 3 months
* 6 months
* 12 months

Older termination data can be excluded to reduce data volume and improve performance.

#### 4. Effective-Dated & Future Data

**Does Agentnoon support future-dated records?**

Yes.

Agentnoon respects **effective dates**, including:

* Future hires
* Future promotions
* Future compensation changes

This enables accurate forecasting and scenario modeling.

**What happens if a future hire is rescinded?**

If a future hire is no longer present in the most recent data feed:

* The individual is removed or marked unoccupied
* The change is reflected automatically in the core dataset

Previously created scenarios remain unchanged until a user explicitly refreshes them.

#### 5. Integration Methods & Connectivity

**What integration methods are supported?**

Agentnoon supports multiple enterprise integration patterns:

* **SFTP file transfer**
* **HR system Report-as-a-Service (RaaS)**
* **API-based integrations**

The chosen method depends on customer architecture and existing integration standards.

**Are standard field specifications available?**

Yes.

Agentnoon provides:

* Sample file layouts
* Field mapping guidance
* Connectivity documentation for SFTP, RaaS, and APIs

Final field selection is driven by customer reporting and planning needs.

#### 6. Custom & Calculated Fields

**Can custom or calculated fields be ingested?**

Yes.

Agentnoon accepts:

* Customer-defined calculated fields
* Custom attributes not delivered by the HR system vendor

These fields can be fully leveraged in analytics and reporting.

**Can source data be overridden in Agentnoon?**

Yes, with caution.

* Source-system data is respected by default
* Overrides are supported for special cases
* Long-term corrections should be made upstream in the system of record

#### 7. Environments & Testing

**What environments are provided?**

Agentnoon provides three standard environments:

* **Development**
* **Staging**
* **Production**

**What data should be used in each environment?**

Recommended approach:

* **Development**: Sample or scrubbed data
* **Staging**: Near-production data with sensitive fields removed
* **Production**: Full production data

This allows functional testing, performance validation, and secure rollout.

#### 8. Security & Access Control

**Does Agentnoon support role-based access control?**

Yes.

Access control operates at two levels:

1. **Access Groups** – control which organizational segments a user can view
2. **Access Roles** – control which data fields a user can access

Examples:

* Restricting compensation visibility
* Limiting access to sensitive demographic attributes
* Constraining users to specific business units or teams

**Who defines access policies?**

Access policies are defined by the customer and enforced by Agentnoon.\
Typical stakeholders include HR leadership, IT, security, and compliance teams.

#### 9. Typical Implementation Path

A common customer implementation follows this sequence:

1. Initial pilot group onboarded
2. One-way ingestion from HR system
3. Org modeling and analytics adoption
4. Gradual expansion to additional users
5. Optional evaluation of bi-directional workflows

Most customers adopt a phased rollout to ensure data quality and governance.

#### 10. Common Design Decisions During Implementation

* Data refresh cadence
* Termination data retention window
* Required vs optional fields
* Access and security model
* Long-term bi-directional integration roadmap

### Summary

Agentnoon integrations are designed to be flexible, scalable, and aligned with enterprise HR architectures. Customers retain full control over data, governance, and process design while enabling advanced organizational modeling and workforce analytics.
