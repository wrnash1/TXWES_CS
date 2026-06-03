# Video Script: Module 12 — ERP Integration and Middleware

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Production Notes

**Duration:** Approximately 25–30 minutes
**Format:** Lecture with slide transitions and screen demonstrations
**Segments:** 6 segments with natural pause points

---

## Segment 1: Introduction — Why Integration Matters (Lines 1–40)

[SLIDE: Title card — "Module 12: ERP Integration and Middleware"]

Welcome back, everyone. I'm Professor Nash, and today we're tackling one of the most practically important topics in enterprise systems: integration. By the end of this module you will understand why no ERP lives in isolation, what middleware actually does, and how both SAP and Salesforce approach the challenge of talking to the outside world.

[SLIDE: The integration problem — cartoon of siloed systems]

Let me start with a story. Imagine a telecom company — let's keep it generic — that has SAP handling finance and supply chain, Salesforce managing customers and sales opportunities, a legacy billing platform written in the 1990s, and a modern data warehouse on the cloud. Every day, sales reps close deals in Salesforce. Finance needs those deals in SAP to create billing records. The warehouse needs both to produce executive dashboards. Without integration, employees are copy-pasting between systems, introducing errors, and wasting hours every week.

[PAUSE — rhetorical question to students]

How many of you have manually exported a spreadsheet from one system and imported it into another? That manual step is exactly what enterprise integration is designed to eliminate.

[SLIDE: Integration continuum — manual to real-time]

Integration exists on a spectrum. At one end you have completely manual processes: exports, imports, rekeying. One step up is scheduled batch file transfers — think overnight CSV drops. Above that is message-based asynchronous integration where systems send events to a queue. At the top is real-time, event-driven API integration where a change in System A immediately triggers an update in System B.

Modern enterprise architecture targets the upper end of that spectrum wherever the business case justifies it. The key phrase is "where the business case justifies it" — real-time integration is more expensive to build and maintain, so you prioritize it for revenue-critical flows.

[SLIDE: Learning objectives]

Here are the four things we will cover today: SAP integration technologies including BAPIs, IDocs, and SAP Integration Suite; Salesforce API types including REST, SOAP, and Platform Events; middleware concepts and the role of an integration platform; and data mapping and ETL fundamentals.

---

## Segment 2: SAP Integration Technologies (Lines 41–80)

[SLIDE: SAP integration landscape]

SAP has been solving integration problems since the 1990s, so it has a rich and sometimes confusing set of tools. Let me walk you through the major ones chronologically, because understanding the history helps you understand why each tool exists.

[SLIDE: IDocs — Intermediate Documents]

The oldest integration mechanism in SAP is the IDoc, which stands for Intermediate Document. An IDoc is SAP's proprietary XML-like format for exchanging business documents. Think of it like an electronic version of a paper form — there is an IDoc type for a purchase order, a sales order, a goods receipt, and hundreds of other document types.

IDocs work asynchronously. SAP writes an IDoc to a port, and a receiving system picks it up and processes it. This decouples the sender from the receiver, which improves reliability. If the receiving system is temporarily down, the IDoc sits in the queue until the receiver is ready.

[SLIDE: BAPIs — Business Application Programming Interfaces]

BAPIs came next. A BAPI is a stable, published interface to a specific SAP business object — a customer, a material, a purchase order. BAPIs are implemented as Remote Function Calls, or RFCs, which means an external system can call them directly over the network.

The word "stable" is important here. SAP commits to not changing BAPI signatures across releases, which makes them safe to build integrations on. If you are writing code to create a sales order in SAP from an external system, you would typically call `BAPI_SALESORDER_CREATEFROMDAT2`.

[SLIDE: RFC — Remote Function Call]

RFC is the underlying transport mechanism that BAPIs run on. There are several RFC types: synchronous RFC waits for a response; asynchronous RFC fires and forgets; transactional RFC guarantees exactly-once delivery. Understanding which RFC type to use is a real architectural decision you will make in practice.

[SLIDE: SAP Integration Suite — the modern answer]

For modern SAP landscapes, SAP now offers the SAP Integration Suite, which runs on SAP Business Technology Platform, or BTP. Integration Suite provides a graphical integration flow designer, pre-built adapters for hundreds of systems, API management capabilities, and event mesh for event-driven architectures.

If you are implementing a new SAP S/4HANA integration today, Integration Suite is the preferred approach. The older IDoc and BAPI mechanisms still work, and you will see them in every production SAP system, but new development targets Integration Suite.

[SLIDE: OData APIs in SAP]

SAP S/4HANA also exposes a large catalog of OData APIs — these are RESTful APIs built on the OData standard. When you connect SAP Fiori apps to S/4HANA, those apps use OData. When you want to read or write SAP data from a modern web application, OData is usually the right choice.

[PAUSE — transition to Salesforce]

---

## Segment 3: Salesforce APIs (Lines 81–120)

[SLIDE: Salesforce API types]

Salesforce takes a very different approach to integration — it was cloud-native from day one, so APIs were baked in from the beginning rather than added later. Salesforce exposes multiple API types, and choosing the right one depends on your use case.

[SLIDE: REST API]

The Salesforce REST API is the most commonly used. It follows standard HTTP conventions: GET to retrieve records, POST to create, PATCH to update, DELETE to remove. Responses come back as JSON. The REST API is great for web applications, mobile apps, and lightweight integrations where you are working with individual records or small result sets.

For your Salesforce Admin exam, know the key REST API endpoints: `/services/data/vXX.0/sobjects/` for object metadata, `/services/data/vXX.0/query/` for SOQL queries, and `/services/data/vXX.0/composite/` for batching multiple operations.

[SLIDE: SOAP API]

The SOAP API predates the REST API and uses XML-based web service calls. It offers some capabilities the REST API does not, such as the ability to reset a user password or access certain metadata. Enterprise integration platforms often have mature SOAP connectors, so you still see the SOAP API in established integration patterns.

[SLIDE: Bulk API]

When you need to load or extract hundreds of thousands to millions of records, you use the Bulk API. The Bulk API processes data asynchronously in batches, which is much more efficient than making thousands of individual REST calls. It is the right tool for nightly data loads, migrations, and mass updates.

[SLIDE: Streaming API and Platform Events]

Platform Events are Salesforce's answer to event-driven integration. When something happens in Salesforce — a deal closes, a case is escalated — you can publish a Platform Event. External systems subscribe to the event channel using CometD, a streaming protocol. This enables near-real-time integration without polling.

Compare this to IDocs in SAP: both are asynchronous, message-based mechanisms. Platform Events are the Salesforce equivalent of an outbound IDoc.

[SLIDE: Apex REST and callouts]

You can also build custom REST endpoints in Salesforce using Apex REST classes. And Salesforce can call external systems using Apex HTTP callouts, which are essentially outbound REST or SOAP calls from within Salesforce logic.

[PAUSE]

---

## Segment 4: Middleware Concepts (Lines 121–160)

[SLIDE: What is middleware?]

Middleware sits between systems. Its job is to receive messages from one system, transform them if needed, route them to the right destination, and handle errors along the way. You might also hear the terms Enterprise Service Bus (ESB), Integration Platform as a Service (iPaaS), or API gateway — these are all flavors of middleware.

[SLIDE: Key middleware functions]

Good middleware handles five concerns. First, connectivity — it has adapters or connectors for dozens of protocols and systems. Second, transformation — it converts data from one format to another, such as SAP IDoc XML to Salesforce JSON. Third, routing — it directs messages based on content or rules. Fourth, error handling — it retries failed deliveries and alerts on unrecoverable failures. Fifth, monitoring — it gives integration teams visibility into message flows, latency, and error rates.

[SLIDE: Common middleware platforms]

You will encounter several middleware platforms in the enterprise world. MuleSoft Anypoint Platform is now a Salesforce product and is deeply integrated with the Salesforce ecosystem. SAP Integration Suite is SAP's cloud-native answer. Dell Boomi is popular in mid-market companies. IBM App Connect and Microsoft Azure Integration Services round out the major players.

For the Salesforce Admin exam, know that MuleSoft is a Salesforce company. Expect a scenario question about where you would use MuleSoft versus a native Salesforce flow.

[SLIDE: Message formats]

Middleware typically handles several message formats. JSON is dominant for modern REST integrations. XML is legacy-pervasive — SAP IDocs are XML, and many enterprise systems still produce XML. CSV remains common for bulk batch loads. EDIFACT and X12 are EDI standards used in supply chain and healthcare integrations.

[SLIDE: Synchronous vs. asynchronous integration]

This is a critical concept. Synchronous integration means the caller waits for a response. If the target system is slow or down, the caller is blocked. Asynchronous integration means the caller sends a message and moves on. A queue or message broker holds the message until the target is ready.

Synchronous: use it when the caller needs an immediate answer — such as a credit check during order entry.

Asynchronous: use it when immediate response is not required and reliability matters more than speed — such as sending a completed order to a fulfillment warehouse.

[PAUSE]

---

## Segment 5: Data Mapping and ETL (Lines 161–200)

[SLIDE: The data mapping challenge]

Every integration project runs headlong into a data mapping problem. System A calls a field "Customer Number." System B calls it "Account ID." System A stores phone numbers as ten digits with no formatting. System B stores them as (XXX) XXX-XXXX. Before you can move data, you must create a field-level mapping — a document or configuration that says "System A field X maps to System B field Y, with this transformation applied."

[SLIDE: ETL — Extract, Transform, Load]

ETL stands for Extract, Transform, Load. It describes the three phases of moving data between systems.

Extract: pull data from the source. This might be a SQL query, an API call, a file read, or a CDC (change data capture) stream.

Transform: apply business rules. Clean dirty data. Convert formats. Merge records. Apply lookups. Filter rows that do not meet criteria.

Load: write the transformed data to the target system. Handle conflicts — what do you do if the record already exists?

[SLIDE: ELT — the modern variant]

In modern cloud data warehouses, you often see ELT — Extract, Load, Transform — where you load raw data into the warehouse first and then apply transformations using SQL. This is common with Snowflake, BigQuery, and Databricks. The warehouse is powerful enough that transforming data after loading is fast and flexible.

[SLIDE: Data quality in integration]

Integration reveals data quality problems you did not know existed. When you try to move customer data from SAP to Salesforce, you discover duplicate accounts, missing phone numbers, invalid postal codes, and inconsistent state abbreviations. Part of every integration project is a data cleansing phase.

For the exam: Salesforce has native duplicate management rules. SAP has a Data Quality Management component in MDG (Master Data Governance). Both platforms emphasize data quality as a prerequisite to clean integration.

[SLIDE: API versioning and governance]

APIs change over time, which creates versioning challenges. The Salesforce API is versioned — you call `/services/data/v59.0/` or `/services/data/v62.0/`. When Salesforce retires an API version, integrations built on that version break. API governance means establishing policies for how APIs are versioned, documented, secured, and retired.

[PAUSE]

---

## Segment 6: Putting It All Together and Summary (Lines 201–240)

[SLIDE: Integration architecture example]

Let me walk through a complete integration scenario. A customer calls a service center. The service rep creates a case in Salesforce. That case needs to create a service ticket in SAP. Here is how that might flow using modern integration.

Step one: The service rep saves the case in Salesforce. A Process Builder flow publishes a Platform Event called "New_Case__e" with case details.

Step two: MuleSoft subscribes to that Platform Event channel. It receives the event message in near real time.

Step three: MuleSoft transforms the Salesforce case payload into the format required by SAP's OData API or a BAPI call.

Step four: MuleSoft calls the SAP API to create the service notification.

Step five: SAP returns a service notification number. MuleSoft writes that number back to the Salesforce case using the REST API.

The whole flow completes in seconds and is fully automated.

[SLIDE: Certification exam tips]

For the Salesforce Admin exam: know the four API types (REST, SOAP, Bulk, Streaming/Platform Events), know when to use each, know what MuleSoft does, and understand the concept of connected apps and OAuth for API authentication.

For SAP essentials: know what IDocs are, what BAPIs are, how RFC works, and the role of SAP Integration Suite. You do not need to write code — you need conceptual understanding.

[SLIDE: Key terms review]

Let us do a quick review of the key terms from today.

IDoc: SAP's proprietary format for asynchronous document exchange.

BAPI: a stable published interface to an SAP business object.

RFC: Remote Function Call, the transport layer for BAPIs.

REST API: HTTP-based, JSON, the primary Salesforce integration mechanism.

SOAP API: XML-based, legacy-compatible Salesforce API.

Bulk API: for high-volume asynchronous data operations in Salesforce.

Platform Events: Salesforce's publish-subscribe event framework.

Middleware/ESB: sits between systems, handles transformation, routing, and error management.

ETL: Extract, Transform, Load — the three phases of data movement.

OData: RESTful API standard used extensively in SAP S/4HANA.

[SLIDE: Coming up next]

In Module 13 we shift to security. We will cover Salesforce profiles and permission sets, SAP authorization objects and roles, Segregation of Duties, and audit trails. Security is a major topic on both certification exams, so come prepared.

[SLIDE: Assignment reminder]

Before the next class, complete the Module 12 Reading Guide, the Integration Architecture Lab, and post your response to the Discussion prompt. The quiz will be available on the LMS starting Monday.

Thank you for your attention today. I'll see you in Module 13.

[END OF VIDEO SCRIPT]

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
