# Reading Guide: Module 12 — ERP Integration and Middleware

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Overview

This reading guide accompanies Module 12 of CIS-4320. By working through these materials you will build a solid conceptual foundation in enterprise integration, understand the specific technologies used in SAP and Salesforce environments, and develop the vocabulary needed for both certification exams. Plan approximately 90 minutes to complete all sections.

---

## Section 1: The Integration Imperative

### Why ERP Systems Cannot Stand Alone

No enterprise runs on a single software system. Even organizations that have standardized on SAP or Salesforce still operate dozens of adjacent applications: HR platforms, manufacturing execution systems, e-commerce storefronts, logistics portals, customer communication tools, and business intelligence warehouses. The question is never whether integration is needed — it is how to do it well.

Poor integration creates compounding business problems. When data must be manually transferred between systems, errors accumulate. A typo in a customer account number creates a billing mismatch. A missed field during export causes a downstream process to fail. Staff spend hours reconciling records that should be automatically synchronized.

Beyond error risk, manual integration creates latency. If sales order data moves from Salesforce to SAP once per night in a batch job, finance cannot see today's pipeline until tomorrow morning. For operational decisions, that delay is unacceptable.

### The Four Integration Patterns

Enterprise architects recognize four foundational integration patterns. Understanding these patterns helps you choose the right technology for a given business requirement.

**Point-to-Point Integration** connects two systems directly with a custom-built interface. Simple and fast to implement, but brittle at scale. When you have ten systems, point-to-point integration creates forty-five potential connection pairs. Change one system and you may break every interface connected to it. This is sometimes called the "spaghetti architecture" problem.

**Hub-and-Spoke Integration** routes all messages through a central hub. Each system only connects to the hub, not to each other. This reduces the number of connections and centralizes transformation and routing logic. The hub is the middleware. The downside is that the hub becomes a single point of failure.

**Event-Driven Architecture** decouples producers from consumers using an event bus or message broker. When something happens in System A, it publishes an event. Any number of systems can subscribe to that event and react independently. This scales well and is resilient — a subscriber being down does not block the producer.

**API-Led Connectivity** is MuleSoft's architectural pattern, which Salesforce has adopted as a best practice. It organizes APIs into three layers: System APIs that abstract backend systems, Process APIs that implement business logic, and Experience APIs that serve specific consumer needs (mobile, web, partner). This layering promotes reuse and reduces duplication.

---

## Section 2: SAP Integration Technologies

### IDocs in Depth

The Intermediate Document (IDoc) is the backbone of SAP's traditional integration architecture. An IDoc has three structural components.

The **Control Record** is the envelope — it identifies the message type, the sender, the receiver, the date, and the status of the IDoc. Every IDoc has exactly one control record.

**Data Records** carry the actual business content. Each data record consists of a segment type (analogous to a record type), a hierarchical level, and 1,000 characters of data in fixed-length fields. The segment structure defines what data is present and in what order.

**Status Records** track the lifecycle of the IDoc as it is processed. SAP updates status records as the IDoc moves through outbound creation, transfer, delivery confirmation, and inbound processing.

IDocs are defined by their **message type** (such as ORDERS for purchase orders, INVOIC for invoices, MATMAS for material master data) and their **basic type** (the specific IDoc segment structure). Understanding message types is important for integration design.

### BAPIs and the Business Object Repository

SAP's Business Object Repository (BOR) catalogs all business objects and their associated BAPIs. To find the right BAPI for a task, you search the BOR in SAP transaction BAPI. Each business object — such as `BUS2032` for Sales Order — exposes methods including Create, Change, GetDetail, and GetList.

BAPI standards impose important rules. BAPIs must not use dialog screens (they must be executable without user interaction). They must handle errors by returning structured return tables rather than raising exceptions. They must be transactionally safe.

### RFC Types and When to Use Each

Understanding RFC variants is important for integration architects and appears on SAP certification assessments.

**Synchronous RFC (sRFC)** executes immediately and the calling program waits for a result. Use sRFC when you need an immediate answer — for example, checking whether a customer exists before creating a sales order.

**Asynchronous RFC (aRFC)** starts the function module in a parallel work process and the caller continues without waiting. Use aRFC for tasks that take a long time and do not need to return a result to the caller.

**Transactional RFC (tRFC)** guarantees exactly-once execution. The system assigns each call a unique transaction ID (TID). If the call fails due to a network error, the system retries using the same TID, ensuring the function is not executed twice. Use tRFC for financial postings and any operation where duplicates would cause problems.

**Background RFC (bgRFC)** is the modern successor to tRFC, offering improved monitoring and queue management.

### SAP Integration Suite

SAP Integration Suite, formerly known as SAP Cloud Platform Integration (CPI), is SAP's cloud-native integration platform. Its main components are:

**Cloud Integration** provides a graphical integration flow (iFlow) designer. An iFlow defines the sequence of steps — receive message, transform, route, call adapter, send — that constitute an integration scenario. Pre-built integration packages are available in the SAP Integration Content Catalog.

**API Management** allows organizations to expose SAP APIs to internal and external consumers, apply rate limiting and security policies, and monitor API usage.

**Event Mesh** provides an event broker that supports the CloudEvents standard, enabling event-driven integration between SAP and non-SAP systems.

**Open Connectors** provides pre-built adapters to hundreds of third-party cloud applications.

### OData in SAP S/4HANA

OData (Open Data Protocol) is an OASIS standard that defines a RESTful approach to building and consuming APIs. SAP S/4HANA exposes more than 1,000 OData services. You access them via URLs following the pattern `/sap/opu/odata/sap/{SERVICE_NAME}/{ENTITY_SET}`.

OData services are documented in SAP's API Business Hub at `api.sap.com`. For any integration that reads or writes S/4HANA master or transactional data, check the API Business Hub first before resorting to BAPIs.

---

## Section 3: Salesforce API Architecture

### API Limits and Governance

Before choosing a Salesforce API, you must understand API limits. Salesforce enforces a daily API call limit that varies by edition and number of user licenses. Exceeding the limit results in API_CURRENTLY_DISABLED errors, which can halt integrations during peak periods.

Strategies for staying within limits include: using Bulk API instead of REST for large data volumes, caching data in an integration layer rather than querying Salesforce repeatedly, using Streaming API to receive changes rather than polling, and monitoring API usage in Setup > System Overview.

### REST API Deep Dive

The Salesforce REST API uses standard OAuth 2.0 for authentication. The most common OAuth flow for server-to-server integration is the JWT Bearer flow, which uses a certificate rather than a user password, making it suitable for automated processes running without user interaction.

Key REST API operations for the Salesforce Admin exam:

**SOQL via REST:** `GET /services/data/v62.0/query?q=SELECT+Id,Name+FROM+Account+LIMIT+10`

**Create a record:** `POST /services/data/v62.0/sobjects/Account/` with JSON body.

**Update a record:** `PATCH /services/data/v62.0/sobjects/Account/{Id}`

**Upsert (insert or update):** `PATCH /services/data/v62.0/sobjects/Account/{ExternalId__c}/{value}` — extremely useful for integration because it creates or updates based on an external ID field.

### Bulk API 2.0

Bulk API 2.0 simplified the original Bulk API. The workflow is: create a job, upload CSV data, close the job, poll for completion, retrieve results. Bulk API 2.0 supports Insert, Update, Upsert, Delete, and Hard Delete operations.

Bulk API 2.0 processes records in parallel and is optimized for governor limits. It is the correct choice when loading more than 2,000 records in a single operation.

### Platform Events and Change Data Capture

Platform Events are custom events defined in Salesforce Setup. They follow a publish-subscribe pattern. An Apex trigger, Flow, or external API call can publish a Platform Event. Subscribers receive the event via the Streaming API's CometD channel.

Change Data Capture (CDC) is a related feature that automatically publishes events whenever records of specified object types are created, updated, deleted, or undeleted. Unlike Platform Events — which you explicitly publish — CDC events are generated automatically by Salesforce. This makes CDC ideal for keeping external systems synchronized without modifying Salesforce logic.

### Connected Apps and OAuth

Any external system that calls the Salesforce API must authenticate as a Connected App. A Connected App is a configuration record in Salesforce Setup that defines the OAuth consumer key and secret, the permitted OAuth flows, the IP ranges allowed, and the scopes granted.

For server-to-server integration, create a Connected App with the JWT Bearer flow, upload the integration system's certificate, and pre-authorize the integration user. This eliminates the need for interactive OAuth consent.

---

## Section 4: Middleware Architecture

### ESB vs. iPaaS

The Enterprise Service Bus (ESB) was the dominant middleware pattern of the 2000s. An ESB is typically an on-premises software product that acts as the central hub for all enterprise integrations. Products like IBM WebSphere MQ, TIBCO EMS, and Oracle Service Bus were common ESBs.

iPaaS — Integration Platform as a Service — is the cloud-native evolution of the ESB. iPaaS platforms run in the cloud, offer subscription-based licensing, provide hundreds of pre-built connectors, and can be configured graphically rather than coded. MuleSoft Anypoint Platform, Dell Boomi, and SAP Integration Suite are all iPaaS platforms.

The key differences: ESBs require infrastructure management and deep technical expertise; iPaaS reduces infrastructure overhead and accelerates integration delivery through pre-built connectors and visual designers.

### Message Queue Concepts

Message queues are foundational to asynchronous integration. A queue holds messages until the consumer is ready to process them. This decouples the producer (the system sending the message) from the consumer (the system receiving it).

Key queue concepts include:

**Dead Letter Queue (DLQ):** where messages go when they cannot be processed after a set number of retries. Monitoring the DLQ is essential — messages accumulating there indicate a systematic processing failure.

**Message ordering:** standard queues typically provide best-effort ordering; some systems offer FIFO queues that guarantee order at the cost of lower throughput.

**Idempotency:** processing the same message multiple times should produce the same result. This is essential because at-least-once delivery guarantees mean duplicate messages are possible.

### Adapter and Connector Patterns

Integration platforms expose system-specific functionality through adapters or connectors. A Salesforce connector, for example, abstracts the REST API calls needed to create, read, update, and delete Salesforce records. The connector handles authentication refresh, pagination, error mapping, and retry logic so the integration developer does not need to implement those concerns manually.

---

## Section 5: Data Mapping and ETL

### Field Mapping Techniques

Field mapping can be simple or complex. Simple mapping is direct: Source field A = Target field B, same data type, no transformation. Complex mapping involves transformations such as:

**Concatenation:** combining First_Name and Last_Name into a single Full_Name field.

**Lookup/Reference:** translating a numeric code in the source to a text value in the target — for example, SAP plant code 1001 maps to Salesforce account "Dallas Facility."

**Default values:** if the source field is blank, populate the target with a default.

**Conditional logic:** if the source status is "C," set the target status to "Closed"; if "O," set to "Open."

**Type conversion:** converting SAP date format YYYYMMDD to ISO 8601 YYYY-MM-DD.

### ETL Tools and Approaches

ETL processes can be implemented using dedicated ETL tools, middleware platforms, or custom code. Common ETL tools in enterprise environments include Informatica PowerCenter, Talend, and SAP Data Services. Cloud-native alternatives include AWS Glue, Azure Data Factory, and Google Dataflow.

For Salesforce-specific data loading, the Salesforce Data Loader is a desktop tool that supports CSV-based insert, update, upsert, delete, and export operations. It uses the Bulk API under the hood and is sufficient for most administrative data loading tasks.

### Data Lineage and Governance

In complex integration landscapes, tracking where data originated and how it was transformed is called data lineage. Maintaining data lineage documentation is increasingly required for regulatory compliance — particularly under GDPR and CCPA, which require organizations to know where personal data is stored and how it flows.

---

## Section 6: Certification Exam Focus Areas

### Salesforce Administrator Exam

The Salesforce Administrator exam tests integration knowledge in the context of administrative decisions, not programming. Expect questions about:

- When to use REST API vs. Bulk API vs. Platform Events
- What a Connected App is and how OAuth is used
- The role of Named Credentials for storing API endpoint credentials securely
- Integration with external data using External Objects and Salesforce Connect
- The difference between inbound and outbound integration from Salesforce's perspective

### SAP S/4HANA Essentials Exam

SAP essentials certification expects conceptual knowledge of:

- What IDocs are and when they are used
- The purpose of BAPIs and the BOR
- The difference between sRFC, tRFC, and aRFC
- The role of SAP Integration Suite in modern SAP architecture
- What OData APIs are in the context of SAP Fiori

---

## Key Terms for Module 12

**IDoc (Intermediate Document):** SAP's proprietary format for asynchronous document exchange between systems.

**BAPI (Business Application Programming Interface):** A stable, published interface to an SAP business object, implemented as an RFC function module.

**RFC (Remote Function Call):** SAP's proprietary protocol for calling function modules across system boundaries.

**REST API:** An HTTP-based API style using standard verbs (GET, POST, PATCH, DELETE) and JSON payloads.

**SOAP API:** An XML-based web services protocol supported by both SAP and Salesforce.

**Bulk API:** Salesforce's asynchronous API for processing large volumes of records.

**Platform Events:** Salesforce's publish-subscribe event framework for near-real-time integration.

**Middleware / ESB / iPaaS:** Software that mediates between systems, handling transformation, routing, and error management.

**ETL:** Extract, Transform, Load — the three phases of data movement between systems.

**OData:** An OASIS standard for RESTful APIs, used extensively in SAP S/4HANA.

**Connected App:** A Salesforce configuration that defines OAuth credentials for external system access.

**Change Data Capture (CDC):** Automatic publication of Salesforce record change events for external system synchronization.

**API-Led Connectivity:** MuleSoft's architectural pattern organizing APIs into System, Process, and Experience layers.

**Dead Letter Queue (DLQ):** A holding queue for messages that have failed processing after maximum retries.

**Idempotency:** The property of an operation that produces the same result regardless of how many times it is executed.

---

## Study Questions

1. What is the primary advantage of asynchronous integration over synchronous integration, and in what scenarios would synchronous be the better choice?

2. Explain the difference between tRFC and aRFC in SAP. Why does tRFC guarantee exactly-once execution?

3. A business analyst asks why you would use the Salesforce Bulk API instead of the REST API for a data migration. How do you respond?

4. Describe the role of a Connected App in Salesforce integration. What security risk does it help manage?

5. A company is evaluating whether to use an IDoc or an OData API to send sales order data from SAP to an external logistics system. What factors should drive that decision?

6. What is Change Data Capture in Salesforce, and how does it differ from a Platform Event?

7. Define ETL and explain the purpose of the Transform phase with two concrete examples.

8. What is the dead letter queue, and why is monitoring it critical for integration operations?

9. Explain API-Led Connectivity's three-layer model and give one example of what belongs in each layer for a Salesforce-to-SAP scenario.

10. What is data lineage, and why is it increasingly required for regulatory compliance?

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
