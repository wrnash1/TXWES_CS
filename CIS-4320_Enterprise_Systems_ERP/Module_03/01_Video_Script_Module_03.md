# Video Script: Module 03 - ERP Selection and Vendor Landscape

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 22-24 minutes

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### [00:00 - 01:30] Opening

Professor Nash on camera. Title card: "Module 03 - ERP Selection and Vendor Landscape."

"Welcome back to CIS-4320. In the first two modules we covered what enterprise systems are and how business processes are modeled. Now comes the question every organization faces before they can implement anything: which system do we buy?

ERP selection is one of the highest-stakes decisions an organization makes. A large enterprise might spend 50 to 150 million dollars over a multi-year implementation. A bad vendor selection decision cannot be easily undone. Companies have gone bankrupt from failed ERP implementations — and the root cause of many failures is traced back to selecting a system that was poorly matched to their actual needs.

Today we cover the vendor landscape, how organizations structure a selection process, how to evaluate Total Cost of Ownership, and how the Request for Proposal process works. These concepts are directly tested on both certification exams."

---

### [01:30 - 06:00] The ERP Vendor Landscape

Cut to slide: "Major ERP Vendors and Their Positioning."

"Let me walk you through the major players in the ERP and CRM market. This is the landscape you need to understand cold for both certification exams.

SAP SE is the dominant global ERP vendor. SAP's current flagship product is S/4HANA — the successor to the older SAP ECC 6.0 platform. SAP is used by the majority of Fortune 500 companies for core back-office operations: finance, procurement, manufacturing, logistics, and HR. SAP has over 440,000 customers across more than 180 countries. If you work in enterprise systems at a large company, you will almost certainly encounter SAP.

Oracle Corporation is SAP's closest competitor in large enterprise ERP. Oracle Cloud ERP, built on Oracle's Fusion Middleware, is the modern SaaS offering. Oracle also acquired NetSuite, which dominates the cloud ERP market for small-to-mid-size companies. Oracle has a particularly strong presence in financial services, healthcare, and the public sector.

Microsoft Dynamics 365 is a hybrid platform that combines ERP functionality — Finance, Supply Chain, Business Central — with CRM functionality — Sales, Customer Service, Marketing — in a single platform built on Microsoft Azure. For organizations already using Microsoft 365, Teams, and Azure, Dynamics 365 has significant integration advantages.

Salesforce is the global leader in CRM. Salesforce Sales Cloud, Service Cloud, and Marketing Cloud manage customer-facing processes for millions of organizations. Salesforce acquired Slack, MuleSoft, and Tableau, making it a broader platform play than pure CRM. Salesforce is not a full back-office ERP — it does not manage general ledger accounting or inventory management. Companies typically run Salesforce alongside an ERP.

Workday focuses on two domains: Human Capital Management and Financial Management. Workday is widely used in professional services, higher education, and healthcare for HR and FP&A.

SAP SuccessFactors is SAP's cloud HCM suite, competing directly with Workday for large-enterprise workforce management.

[SHOW DIAGRAM: A 2x2 matrix. X-axis: Company Size (SMB to Enterprise). Y-axis: Primary Function (Back-Office ERP to Front-Office CRM). SAP in Enterprise/ERP quadrant. Oracle Cloud ERP adjacent. NetSuite in SMB-Mid/ERP. Salesforce in Enterprise/CRM. Microsoft Dynamics 365 near center. Workday in Enterprise/HCM-Finance area.]

For this course and these certifications, our primary platforms are SAP S/4HANA for ERP and Salesforce for CRM."

---

### [06:00 - 10:30] ERP Selection Criteria

Cut to slide: "How Organizations Choose ERP."

"When a company needs to select an ERP system, they do not simply pick the brand they have heard of. A structured selection process evaluates vendors against a set of defined criteria. The most common criteria fall into five categories.

First: Functional fit. Does the system support the company's core business processes out of the box? A discrete manufacturer needs strong production planning and bill of materials management. A financial services firm needs robust multi-currency and multi-entity consolidation. A company that selects a system with weak support for its core industry will spend years customizing — which is expensive and risky.

Second: Total Cost of Ownership. What will this system actually cost over 10 years? Not just the license fee — but implementation labor, customization, training, annual maintenance, infrastructure, and internal IT staffing. We cover TCO in detail in a moment.

Third: Technical fit. How well does the system integrate with existing technology? A company on Microsoft Azure will have a lower integration cost with Dynamics 365 than with SAP. A company with Salesforce for CRM needs to evaluate how well a candidate ERP integrates with Salesforce.

Fourth: Vendor stability and roadmap. Will the vendor be around in 10 years? Is the product actively being developed? SAP's commitment to S/4HANA as the strategic product until at least 2040 is a strong stability signal. Smaller vendors carry more risk of acquisition or discontinuation.

Fifth: Reference customers. Has this vendor successfully implemented their system for companies similar to ours in size, industry, and complexity? Reference customer conversations are one of the most valuable steps in the selection process.

[SHOW DIAGRAM: A radar/spider chart with five axes: Functional Fit, TCO, Technical Fit, Vendor Stability, Reference Customers. Show three overlapping polygons representing scores for SAP, Oracle, and Microsoft Dynamics for a hypothetical mid-size manufacturer, illustrating a scoring approach.]"

---

### [10:30 - 14:00] Total Cost of Ownership

Cut to slide: "Understanding Total Cost of Ownership."

"Total Cost of Ownership — TCO — is one of the most tested concepts on both certification exams when the topic is vendor selection. Let me make sure you understand it precisely.

TCO is the full financial cost of an ERP system over its useful life. For most enterprises, we measure over 5 to 10 years. TCO includes:

Software licenses or subscription fees. For on-premise systems, this is typically a one-time perpetual license plus annual maintenance — usually 18 to 22% of license value per year. For SaaS systems, it is a recurring annual subscription per user.

Implementation labor. This is often the largest single cost component. A typical SAP S/4HANA implementation for a mid-size company costs 3 to 5 times the annual license fee in consulting and internal project labor.

Hardware and infrastructure. On-premise systems require servers, storage, network infrastructure, data center space, and power. SaaS systems eliminate this category — the vendor handles it.

Customization and development. Every deviation from standard that requires code costs money to build, test, and maintain across every future upgrade.

Training. Users and administrators must be trained. In large deployments, training costs are significant.

Annual maintenance and support. On-premise: 18-22% of license annually for vendor support. SaaS: included in the subscription.

Upgrade projects. On-premise ERP upgrades are major projects costing millions and requiring months of testing. SaaS vendors deliver updates automatically — the customer does not manage upgrade projects.

[SHOW DIAGRAM: A stacked bar chart comparing SaaS vs. On-Premise TCO over years 1 through 10. Year 1 shows high on-premise cost (hardware + license + implementation) vs. lower SaaS cost (subscription + implementation). Over years 2-10, SaaS annual costs are steady subscription fees. On-premise shows annual maintenance fees, and spikes in years 4 and 8 for upgrade projects. Total on-premise often exceeds SaaS by year 7-8.]

The key insight is this: the upfront license cost of an on-premise system often looks cheaper than a SaaS subscription, but when you add up infrastructure, upgrade projects, and DBA staffing over 10 years, SaaS frequently wins on TCO. That is why so many organizations are moving to cloud ERP."

---

### [14:00 - 17:30] The RFP Process

Cut to slide: "The Request for Proposal Process."

"Once a company has defined its requirements and selection criteria, it issues a formal procurement document to candidate vendors. This document is called a Request for Proposal, or RFP.

The RFP is the company's structured solicitation asking vendors to describe their solution, provide pricing, outline their implementation approach, list reference customers, and respond to specific functional requirements. Every vendor receives the same RFP and responds in a standardized format, allowing the company to compare responses objectively.

A typical ERP RFP process follows these steps:

Step one: Vendor longlist. The company identifies 6 to 10 potential vendors through market research, analyst reports like Gartner Magic Quadrant, and industry peer conversations.

Step two: Request for Information (RFI). A shorter, less detailed document sent to all longlisted vendors to narrow the field. The RFI response helps eliminate vendors that clearly do not fit before investing in a full RFP.

Step three: Shortlist selection. Based on RFI responses, the company selects 3 to 5 vendors to receive the full RFP.

Step four: RFP issuance and responses. The full RFP is issued. Vendors typically have 3 to 6 weeks to respond. Responses include pricing, functional coverage matrices, implementation timelines, and reference customer contacts.

Step five: Vendor demonstrations. Shortlisted vendors conduct scripted demos showing how their system handles the company's specific business scenarios.

Step six: Reference checks. The company contacts reference customers from the vendor's list and asks specific questions about implementation experience, support quality, and post-go-live performance.

Step seven: Contract negotiation and award.

[SHOW DIAGRAM: A horizontal timeline showing the RFP stages left to right: Market Research → RFI → Shortlist → RFP Issue → Vendor Demos → Reference Checks → Contract → Award. Estimated timeframes labeled above each stage. Total process: 4-6 months.]

Exam tip: Know the difference between an RFP (Request for Proposal — used for selection), a Statement of Work (SOW — used to define project scope after selection), and a Service Level Agreement (SLA — defines performance commitments in the contract)."

---

### [17:30 - 20:00] Deployment Models: SaaS vs. On-Premise vs. Hybrid

Cut to slide: "ERP Deployment Models."

"The three primary deployment models are: on-premise, SaaS (cloud), and hybrid.

On-premise: The company purchases software licenses, installs the ERP on its own servers, manages its own database, handles patching and upgrades, and controls all infrastructure. This model gives maximum control but requires significant IT resources and capital investment.

SaaS (Software as a Service): The vendor hosts everything. The company accesses the system through a web browser. The vendor manages all infrastructure, delivers updates automatically, and provides multi-tenant architecture where multiple customers share the same platform with logical data isolation. Salesforce is pure SaaS. SAP S/4HANA Cloud Public Edition is SAP's SaaS offering.

Hybrid: The company runs some workloads on-premise or in a private cloud and other workloads in the public cloud. For example, running core financials on SAP on-premise while using Salesforce in the cloud — connected by middleware. Most large enterprises today operate in a hybrid model during their transition to full cloud.

[SHOW DIAGRAM: Three-column comparison. Column 1 (On-Premise): Customer box at top, arrows pointing down through Application Server, Database Server, OS, Hardware, Data Center. Customer owns all layers. Column 2 (SaaS): Browser icon at top, cloud arrow pointing to Vendor-Managed stack. Customer box shows only Data and Configuration. Column 3 (Hybrid): Left side on-premise stack, right side cloud stack, connected by Integration Middleware in the middle.]

Exam tip for Salesforce: Salesforce has no on-premise deployment option. It is SaaS only. This is a frequently tested fact on the Salesforce Associate exam."

---

### [20:00 - 22:00] Module Summary and Exam Tips

Cut to slide: "Module 03 Key Takeaways."

"Key takeaways for Module 03:

One: Know the major vendors. SAP is the leader in large enterprise ERP. Salesforce leads CRM. Oracle competes with SAP in large enterprise ERP. Microsoft Dynamics 365 serves mid-market to enterprise with combined ERP and CRM. NetSuite serves SMB to mid-market.

Two: ERP selection is evaluated on five criteria — functional fit, TCO, technical fit, vendor stability, and reference customers.

Three: TCO includes much more than the license fee. Implementation, infrastructure, customization, training, maintenance, and upgrade projects all contribute. Over 10 years, SaaS often has lower TCO than on-premise.

Four: The RFP is the formal procurement document used for vendor selection. Know the difference between RFP, RFI, SOW, and SLA.

Five: Deployment models — SaaS, on-premise, and hybrid — have specific characteristics and tradeoffs. Salesforce is SaaS-only. SAP offers multiple models.

Complete the reading guide and lab. Your lab this week has you build a vendor selection matrix for a fictional company scenario — it is exactly the kind of structured analysis that both certifications test. I'll see you in Module 04."

---

### [End Card]

Text on screen:

- Complete Reading Guide 03
- Complete Lab 03 (Vendor Selection Matrix)
- Complete Quiz 03 (10 questions)
- Post to Discussion Forum 03 (due Wednesday)
- Peer responses due Sunday
- Trailhead: trailhead.salesforce.com — search "Salesforce Platform Basics"
