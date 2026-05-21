# Reading Guide: Module 11 - Enterprise Application Integration (EAI)

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 11 - Enterprise Application Integration (EAI)**! No enterprise runs on a single system. A typical large organization has an ERP for back-office operations, a CRM for customer management, an HCM platform for HR, an e-commerce system, and dozens of specialized tools — all of which need to exchange data reliably. Enterprise Application Integration is the discipline of connecting these systems so data flows correctly between them without manual re-entry.

This module covers integration architecture patterns (point-to-point vs. hub-and-spoke), the API standards used (REST and SOAP), and the role of middleware platforms like MuleSoft in translating and routing data between disparate systems. These concepts appear on both the Salesforce and SAP certification paths.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **EAI principles**: The foundational design concepts for connecting enterprise applications — including loose coupling (systems should not depend directly on each other's internal implementation), data transformation (converting formats between systems), and reliable message delivery (ensuring no transaction is lost in transit).
* **REST/SOAP APIs**: The two dominant web service standards for system-to-system communication. REST (Representational State Transfer) uses HTTP verbs (GET, POST, PUT, DELETE) and JSON payloads; it is lightweight and widely used in modern cloud integrations. SOAP (Simple Object Access Protocol) uses XML envelopes and WSDL contracts; it is older, more formal, and still common in enterprise middleware and SAP integrations.
* **Middleware brokers (MuleSoft)**: Integration platforms that act as central message brokers, receiving data from one system, transforming it to the required format, and routing it to destination systems. MuleSoft Anypoint Platform is Salesforce's owned integration platform; SAP Integration Suite (formerly SAP Cloud Platform Integration) is SAP's equivalent.
* **Data transformation schemas**: Mapping definitions that specify how fields in a source system correspond to fields in a target system — including data type conversions, field renaming, and value lookups. Transformations are configured in the middleware layer so neither source nor target system requires modification.

---

### 2. Certification Exam Tips

* **Salesforce Certified Associate focus:** The exam tests your understanding of how Salesforce connects to external systems. Know that Salesforce exposes REST and SOAP APIs for external systems to call, and that Connected Apps and OAuth 2.0 are the authentication mechanism for API access. MuleSoft is Salesforce's recommended integration platform.
* **Integration patterns:** Know the difference between real-time (synchronous) integration — where the calling system waits for a response — and batch (asynchronous) integration — where records are collected and sent in bulk on a schedule. ERP-to-CRM nightly data syncs are typically batch; order placement confirmations are typically real-time.
* **SAP iDoc:** SAP uses Intermediate Documents (iDocs) as its legacy message format for system-to-system communication. iDocs are still widely used for EDI (Electronic Data Interchange) with trading partners. Modern SAP integrations increasingly use REST APIs through SAP Integration Suite.
* **Point-to-point vs. hub-and-spoke:** Point-to-point integration connects each pair of systems directly; n systems require n(n-1)/2 connections. Hub-and-spoke (middleware) centralizes all connections through one broker, reducing total connections to n. Exam scenarios testing scalability always favor hub-and-spoke.
* **Study Resource:** Complete the Salesforce Trailhead module [Integration Architecture](https://trailhead.salesforce.com/content/learn/modules/integration-architecture) — a free module covering REST, SOAP, and MuleSoft integration patterns applicable to the Associate and Administrator exam paths.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Complete the Salesforce Trailhead module [Integration Architecture](https://trailhead.salesforce.com/content/learn/modules/integration-architecture) — a free module explaining how Salesforce integrates with external systems using REST, SOAP, and platform events.
* **Required Video:** Watch the video lecture on **Enterprise Application Integration** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Map database values to JSON API formats**: Given a sample SAP vendor master record (with fields in SAP-format naming conventions), write a JSON payload that represents the same vendor data in a REST API format suitable for creating a Salesforce Account record.
* **Draft middleware broker mapping definitions**: Create a field mapping table showing how five fields from a Salesforce Opportunity record (Name, Amount, CloseDate, StageName, AccountId) map to the corresponding fields in a hypothetical ERP sales order record.
* **Trace REST integrations**: Document the full request-response cycle for a REST API call that retrieves a Salesforce Account record by ID — including the HTTP method, endpoint URL structure, authentication header, and expected JSON response format.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to explain the difference between REST and SOAP in one sentence each.
* [ ] Complete [Integration Architecture](https://trailhead.salesforce.com/content/learn/modules/integration-architecture) on Trailhead (earn the badge).
* [ ] Watch the video lecture on **Enterprise Application Integration** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab JSON mapping, field translation table, and REST call trace exercises.
* [ ] Proceed to the weekly quiz.
