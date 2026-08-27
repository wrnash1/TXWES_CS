# Reading Guide: Module 03 - ERP Selection and Vendor Landscape

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Introduction

Selecting an ERP system is one of the most consequential technology decisions an organization makes. The choice shapes workflows, data structures, integration architecture, and operating costs for a decade or more. This module equips you with the frameworks, vocabulary, and market knowledge needed to participate intelligently in vendor selection decisions — and to answer the selection-related questions on both the Salesforce Certified Associate and SAP Certified Associate exams.

---

## Section 1: High-Yield Glossary

**Total Cost of Ownership (TCO)**
The full financial cost of an ERP system over its useful life, including software licenses or subscriptions, implementation labor, hardware or cloud infrastructure, customization development, training, annual maintenance and support fees, and internal IT staffing. TCO is the correct basis for comparing deployment models and vendor options. The upfront license price is only one of many components.

**Request for Proposal (RFP)**
A formal procurement document issued to shortlisted vendors asking them to describe their solution, provide detailed pricing, outline their implementation approach, demonstrate functional coverage against the company's requirements, and supply reference customer contacts. RFP responses are scored against defined criteria to enable objective vendor comparison.

**Request for Information (RFI)**
A shorter, less detailed document sent to a broader vendor longlist to gather high-level capability and pricing information. RFI responses are used to narrow the longlist to a shortlist before investing in a full RFP process.

**Statement of Work (SOW)**
A contract document that defines the specific tasks, deliverables, timelines, and resource commitments for a project already awarded to a vendor. SOW is written after vendor selection is complete — it is not a selection document.

**Service Level Agreement (SLA)**
A contractual commitment from a vendor defining performance standards such as system uptime percentage, support response time, and disaster recovery objectives. SLAs are negotiated after vendor selection and are part of the vendor contract.

**Functional Fit**
The degree to which an ERP system's standard capabilities cover the organization's business process requirements without customization. High functional fit reduces implementation cost and upgrade risk. Low functional fit requires expensive customizations that may become unsupportable in future upgrades.

**Vendor Lock-In**
The degree to which an organization becomes dependent on a specific vendor's proprietary technology, making it difficult and expensive to switch to a different vendor in the future. On-premise ERP systems historically create higher lock-in than SaaS systems due to customization accumulation.

**Perpetual License**
A software licensing model where the customer pays a one-time fee to own the right to use the software indefinitely. On-premise ERP systems traditionally use perpetual licensing, with separate annual maintenance fees (typically 18-22% of license value) for support and minor updates.

**Subscription Licensing**
A software licensing model where the customer pays a recurring fee (typically annual or monthly, per user) for the right to use the software. SaaS platforms use subscription licensing. The subscription covers hosting, support, and updates — the customer owns no software assets.

**Multi-Tenancy**
A cloud architecture pattern where multiple customers (tenants) share the same application infrastructure, application code, and database platform, with strict logical isolation enforcing data privacy between tenants. Salesforce and SAP S/4HANA Cloud Public Edition use multi-tenant architecture. Multi-tenancy enables the vendor to deliver updates to all customers simultaneously.

**Single-Tenant (Dedicated)**
A cloud hosting model where each customer has their own dedicated application instance and database, even though the infrastructure may be vendor-managed. SAP S/4HANA Cloud Private Edition uses single-tenant hosting. Single-tenant provides more customization flexibility but costs more than multi-tenant.

**Software as a Service (SaaS)**
A cloud delivery model where the vendor hosts and manages the complete application stack and customers access it through a web browser, managing only data and configuration. Salesforce is the primary SaaS example in this course. Customers have no access to or responsibility for the underlying infrastructure.

**Platform as a Service (PaaS)**
A cloud model where the vendor provides a managed runtime platform on which customers build and deploy their own applications. Salesforce Platform (Force.com) and SAP Business Technology Platform (SAP BTP) are PaaS offerings on top of SaaS applications.

**Infrastructure as a Service (IaaS)**
A cloud model where customers rent compute, storage, and network resources from a cloud provider and manage their own operating system, middleware, and application software. AWS EC2, Azure VMs, and Google Compute Engine are IaaS examples.

---

## Section 2: ERP Vendor Comparison Table

| Vendor | Primary Product | Primary Market | Core Strength | Deployment Options | Primary Competitor |
|---|---|---|---|---|---|
| SAP SE | S/4HANA | Large Enterprise | Finance, Manufacturing, SCM, HCM | SaaS (Public/Private Cloud), On-Premise | Oracle |
| Oracle | Oracle Cloud ERP | Large Enterprise | Finance, HR, Supply Chain | SaaS, On-Premise | SAP |
| Microsoft | Dynamics 365 | Mid-Market to Enterprise | Combined ERP + CRM, Microsoft ecosystem | SaaS (Azure) | SAP, Salesforce |
| Salesforce | Sales/Service/Marketing Cloud | SMB to Enterprise | CRM, customer engagement | SaaS only | Microsoft, Oracle CX |
| NetSuite (Oracle) | NetSuite ERP | SMB to Mid-Market | Cloud-first ERP for growing companies | SaaS | Microsoft Business Central |
| Workday | Workday HCM / Financials | Enterprise | HCM and Financial Planning | SaaS | SAP SuccessFactors |
| SAP SuccessFactors | SuccessFactors | Enterprise | Cloud HCM suite | SaaS | Workday |
| Infor | Infor CloudSuite | Mid-Market / Industry | Industry-specific ERP | SaaS, On-Premise | SAP, Oracle |

---

## Section 3: TCO Component Analysis

### On-Premise vs. SaaS TCO Over 10 Years

The following illustrates the typical cost structure for each model. Actual amounts vary significantly by company size and complexity.

| Cost Category | On-Premise | SaaS |
|---|---|---|
| Year 1: Software license | High (one-time perpetual) | Moderate (annual subscription) |
| Year 1: Implementation labor | High | High (similar magnitude) |
| Year 1: Hardware/infrastructure | High | None (vendor-managed) |
| Years 2-10: Annual maintenance | 18-22% of license per year | Included in subscription |
| Years 2-10: Infrastructure ops | IT staffing, patching, DBA | None |
| Years 4-8: Major upgrade project | Very high (millions for large orgs) | None (automatic updates) |
| Customization maintenance | High (re-test every upgrade) | Lower (fewer customizations; upgrades are automatic) |
| 10-year cumulative TCO | Often higher than SaaS by year 7-8 | Often lower over full lifecycle |

Key exam insight: The SaaS subscription appears more expensive per year on a line-item basis, but the elimination of hardware, infrastructure staffing, and upgrade project costs typically results in lower 10-year TCO for most organizations.

### The Hidden Costs of On-Premise ERP

On-premise customers frequently underestimate these cost categories:

- Database administrator (DBA) annual salary: $90,000-$150,000
- Server hardware refresh every 5 years: $500,000-$2,000,000 for large orgs
- Major version upgrade project: $1,000,000-$10,000,000+ for large SAP implementations
- Data center power, cooling, and physical security: ongoing
- Business continuity and disaster recovery infrastructure: significant capital

---

## Section 4: The ERP Selection Process — Stage-by-Stage

### Stage 1: Requirements Definition

Before evaluating vendors, the organization must document its requirements. This involves:

- Listing all business processes that the ERP must support
- Identifying must-have capabilities versus nice-to-have capabilities
- Documenting current system integrations that must be maintained
- Establishing budget parameters and timeline constraints
- Defining success criteria

### Stage 2: Market Research and Vendor Longlist

Research sources for identifying candidate vendors:

- Gartner Magic Quadrant for ERP (annually published)
- Forrester Wave for CRM
- Industry analyst reports specific to the company's sector
- Peer organizations in the same industry (conference networking)
- Internal IT and finance team recommendations

### Stage 3: RFI and Shortlisting

The RFI narrows 8-12 longlisted vendors to 3-5 shortlisted vendors. The RFI typically asks for:

- High-level capability coverage against major requirement areas
- Reference customers in the same industry and size range
- Estimated pricing range
- Proposed implementation approach and timeline

### Stage 4: RFP, Demos, and Scoring

```text
[RFP Issued to 3-5 Vendors]
        |
[Vendors Respond in 3-6 Weeks]
        |
[Scoring Committee Evaluates Responses]
        |
[Vendor Demonstrations (Scripted Scenarios)]
        |
[Reference Customer Calls]
        |
[Final Scoring and Vendor Recommendation]
        |
[Contract Negotiation and Award]
```

A vendor scoring matrix assigns weights to each evaluation criterion and scores each vendor's response:

| Criterion | Weight | Vendor A Score | Vendor B Score | Vendor C Score |
|---|---|---|---|---|
| Functional fit — Finance | 20% | 85 | 90 | 75 |
| Functional fit — Supply Chain | 15% | 90 | 80 | 70 |
| Functional fit — HR | 10% | 75 | 85 | 80 |
| TCO (10-year) | 25% | 80 | 70 | 90 |
| Technical fit with existing systems | 15% | 70 | 85 | 80 |
| Vendor stability and roadmap | 10% | 95 | 90 | 75 |
| Reference customer satisfaction | 5% | 88 | 82 | 70 |
| **Weighted Total** | **100%** | **82.7** | **81.5** | **78.5** |

### Stage 5: Procurement Documents — Key Distinctions

| Document | Timing | Purpose |
|---|---|---|
| RFI (Request for Information) | Pre-shortlist | Gather high-level info to narrow vendors |
| RFP (Request for Proposal) | During selection | Solicit detailed solution proposals for scoring |
| SOW (Statement of Work) | Post-selection | Define project scope and deliverables |
| MSA (Master Service Agreement) | Post-selection | Establish legal and commercial terms |
| SLA (Service Level Agreement) | Post-selection | Define performance commitments |

---

## Section 5: Deployment Model Comparison

| Dimension | On-Premise | SaaS (Public Cloud) | Private Cloud (Managed) | Hybrid |
|---|---|---|---|---|
| Infrastructure ownership | Customer | Vendor | Vendor (dedicated) | Mixed |
| Upgrade management | Customer (major projects) | Vendor (automatic) | Vendor (semi-automatic) | Mixed |
| Customization flexibility | High | Low to Moderate | Moderate to High | Mixed |
| Data sovereignty control | High | Moderate | High | Mixed |
| Time to provision | Months | Days | Weeks | Mixed |
| Typical contract term | Perpetual license | 1-3 year subscription | 1-3 year contract | Mixed |
| Salesforce availability | No | Yes (only model) | No | N/A |
| SAP S/4HANA availability | Yes | Yes (Cloud Public Ed.) | Yes (Cloud Private Ed.) | Yes |

---

## Section 6: Salesforce-Specific Deployment Facts

The Salesforce Certified Associate exam tests several specific Salesforce platform facts:

- Salesforce is **SaaS only** — there is no on-premise version of Salesforce
- Salesforce uses **multi-tenant architecture** — all customers share the same infrastructure with logical isolation
- Salesforce delivers **three major releases per year**: Spring, Summer, and Winter
- All customers receive the **same release on the same schedule** — there is no option to defer
- Salesforce **sandboxes** are updated before production — giving administrators a preview testing window
- The Salesforce **AppExchange** is the marketplace for pre-built add-on applications and managed packages
- **Governor limits** apply to all Salesforce customizations because of multi-tenancy — these ensure no single tenant monopolizes shared resources

---

## Section 7: SAP-Specific Market Facts

The SAP Certified Associate exam expects knowledge of SAP's market position and product portfolio:

- SAP is the **largest ERP vendor by market share** among large enterprises globally
- SAP **S/4HANA** is the current strategic platform, built on SAP HANA in-memory database
- SAP **ECC 6.0** (the predecessor) reaches end of mainstream maintenance in **2027** (extended to 2030 for some customers), driving migration projects
- SAP's cloud HR product is **SuccessFactors**; its cloud CRM product is **SAP Sales Cloud**
- SAP's **Business Technology Platform (SAP BTP)** is the PaaS layer for integrations, extensions, and custom applications
- SAP's implementation methodology is **SAP Activate** (covered in Module 04)
- SAP's **AppStore** for add-ons is the **SAP Store** (formerly SAP App Center)

---

## Section 8: Certification Exam Tips

1. **TCO is the correct decision framework, not license cost alone.** When an exam question asks how to compare ERP vendor costs, always choose the answer that references Total Cost of Ownership over the system's useful life — not just the upfront price.

2. **Know the difference between RFP, RFI, SOW, and SLA.** These four procurement documents are frequently confused on exams. RFI = pre-selection information gathering; RFP = formal proposal solicitation; SOW = post-selection scope definition; SLA = performance commitment.

3. **Salesforce is SaaS-only — no on-premise option exists.** This is tested directly on the Salesforce Associate exam. If a question describes on-premise Salesforce deployment as an option, it is incorrect.

4. **Multi-tenancy explains Salesforce governor limits.** Because all customers share infrastructure, Salesforce enforces per-transaction resource limits (governor limits) to prevent one tenant from degrading performance for others. This is a foundational Salesforce architecture concept.

5. **SAP dominates large enterprise ERP.** When asked which vendor is the global leader in ERP for large corporations, the answer is SAP. Salesforce leads CRM — these are different categories.

6. **Functional fit is weighted highest in most selection decisions.** A system with poor functional fit for the company's core industry processes creates years of expensive customization. Selection criteria weight questions on exams typically show functional fit as the most important factor.

7. **SaaS advantages: no upgrade projects, lower infrastructure TCO, automatic updates.** SaaS disadvantages: less customization flexibility, vendor-controlled release cadence, dependency on internet connectivity.

8. **The Gartner Magic Quadrant is the standard market analysis tool.** When a question describes a company using an industry analyst report to identify ERP vendors, the answer is typically the Gartner Magic Quadrant.

---

## Section 9: Required Trailhead and Study Resources

Complete these before attempting the quiz:

- **Salesforce Trailhead — Salesforce Platform Basics**
  URL: trailhead.salesforce.com — search "Salesforce Platform Basics"
  Reviews the SaaS architecture and platform model that defines Salesforce's deployment characteristics.

- **Salesforce Trailhead — AppExchange Basics**
  URL: trailhead.salesforce.com — search "AppExchange Basics"
  Covers the Salesforce AppExchange — analogous to the add-on ecosystem in the broader ERP market.

---

## Section 10: Study Checklist

- Read all glossary terms in Section 1 and distinguish TCO from license cost in your own words.
- Study the vendor comparison table in Section 2. Know each vendor's market segment and primary strength.
- Review the TCO analysis in Section 3. Be able to explain why SaaS often wins on 10-year TCO.
- Trace the selection process stages in Section 4. Know which document belongs to which stage.
- Study the deployment model comparison in Section 5. Know what distinguishes SaaS, on-premise, and hybrid.
- Memorize the Salesforce-specific facts in Section 6. These are directly tested.
- Memorize the SAP market facts in Section 7.
- Complete the Salesforce Trailhead "Salesforce Platform Basics" and "AppExchange Basics" modules.
- Watch the Module 03 video lecture.
- Complete Lab 03.
- Post to Discussion Forum 03 by Wednesday at 11:59 PM.
- Complete Quiz 03 (10 questions).

---

## 9. Supplemental Resources

**1. Gartner Magic Quadrant for Cloud ERP for Product-Centric Enterprises**
<https://www.gartner.com/en/documents/magic-quadrant-cloud-erp>
The authoritative vendor landscape report evaluating SAP, Oracle, Microsoft, and others on Completeness of Vision and Ability to Execute. Understanding the Magic Quadrant framework is directly tested in ERP selection methodology questions.

**2. SAP — Why SAP S/4HANA: Business Case and Transition Guide**
<https://www.sap.com/products/erp/s4hana.html>
SAP's official S/4HANA product page with whitepapers on TCO, migration paths from ECC, and industry-specific capabilities. Useful for building the vendor comparison sections of Lab 03.

**3. Salesforce — AppExchange Overview and Ecosystem**
<https://appexchange.salesforce.com>
The live AppExchange marketplace. Browsing the ERP integration category demonstrates how Salesforce extends into back-office functions through partner applications — directly relevant to the deployment model comparison in this module.
