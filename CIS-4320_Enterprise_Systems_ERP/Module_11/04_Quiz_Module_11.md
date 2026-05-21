# Quiz: Module 11 - Enterprise Application Integration (EAI)

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

What role does middleware like MuleSoft play in enterprise system integration?

* A) It replaces the database engine in both the source and target systems
* B) It acts as a broker, translating and routing data payloads between disparate applications that use different formats and protocols
* C) It builds front-end user interface screens for web applications
* D) It hosts virtual machines for running ERP application servers

* **Correct Answer:** B) Middleware connects different system architectures (e.g., a cloud CRM to a legacy on-premise ERP) by translating data formats and routing messages on-the-fly.
* **Distractor Analysis:**
  * *Why B is correct:* MuleSoft Anypoint Platform sits between systems, receiving a message in the source format, applying a transformation map to convert it to the target format, and delivering it to the destination — without requiring either system to change.
  * *Why A is incorrect:* Middleware does not replace database engines; source and target systems keep their own databases, and middleware only handles the data exchange layer between them.
  * *Why C is incorrect:* Building UI screens is a front-end development task; middleware operates at the data integration layer and has no role in rendering user interfaces.
  * *Why D is incorrect:* Hosting virtual machines is an infrastructure/cloud operations function; middleware is an application-layer data routing and transformation tool.

---

### Question 2

Which of the following best describes the **EAI principle of loose coupling**?

* A) Each integrated system is directly dependent on the internal data structures and APIs of every other system it connects to
* B) Systems exchange data through a defined interface (API or message format) without knowing or depending on each other's internal implementation details
* C) All enterprise systems are consolidated into a single database to eliminate the need for any data exchange
* D) Integration connections are hard-coded in each application so that changes to one system automatically propagate to all connected systems

* **Correct Answer:** B) Loose coupling means systems interact through stable, well-defined interfaces while remaining internally independent — so a change to one system's internal structure does not break its integration partners.
* **Distractor Analysis:**
  * *Why B is correct:* Loose coupling is a foundational EAI principle. When Salesforce calls the SAP REST API for an order status, it only needs to know the API contract (endpoint, request format, response schema) — not how SAP stores the order internally.
  * *Why A is incorrect:* This describes tight coupling — the anti-pattern that makes systems brittle and expensive to change, exactly what EAI aims to avoid.
  * *Why C is incorrect:* Consolidating all systems into one database describes an ERP strategy, not an integration architecture principle; it is also impractical for the full enterprise technology landscape.
  * *Why D is incorrect:* Hard-coded direct dependencies between systems are the definition of point-to-point tight coupling, which creates a "spaghetti integration" architecture that is difficult to maintain.

---

### Question 3

A company has 8 enterprise systems that all need to share data with each other. An architect proposes deploying a central middleware platform as a hub. How many integration connections does hub-and-spoke require compared to point-to-point?

* A) Hub-and-spoke: 28 connections; Point-to-point: 8 connections — hub-and-spoke is more complex
* B) Hub-and-spoke: 8 connections (one per system to the hub); Point-to-point: 28 connections (one per unique system pair) — hub-and-spoke is simpler to maintain
* C) Both architectures require exactly 8 connections regardless of the number of systems
* D) Hub-and-spoke requires no connections because systems communicate through a shared database

* **Correct Answer:** B) With 8 systems, point-to-point requires n(n-1)/2 = 28 connections; hub-and-spoke requires only 8 connections (each system connects once to the hub), dramatically reducing integration maintenance complexity.
* **Distractor Analysis:**
  * *Why B is correct:* The hub-and-spoke model's scalability advantage is a core EAI concept. Adding a 9th system to hub-and-spoke requires 1 new connection; adding it to point-to-point requires 8 new connections.
  * *Why A is incorrect:* This reverses the connection counts; point-to-point has the exponentially growing connection count, not hub-and-spoke.
  * *Why C is incorrect:* Point-to-point connection count grows quadratically with the number of systems (n(n-1)/2), not linearly.
  * *Why D is incorrect:* Hub-and-spoke still requires each system to establish a connection to the middleware hub; it does not eliminate connections, it centralizes them.

---

### Question 4

A Salesforce developer needs to call an external ERP REST API from Salesforce to retrieve a customer's open order count. Which Salesforce feature is required to allow Salesforce code to make outbound HTTP calls to external systems?

* A) A Connected App OAuth configuration so the ERP can call Salesforce inbound
* B) A Remote Site Setting (or Named Credential) that whitelists the external ERP endpoint URL so Salesforce allows the outbound HTTP callout
* C) A Validation Rule on the Account object that triggers the API call when the record is saved
* D) A custom Apex Batch class scheduled to run nightly to collect all order counts

* **Correct Answer:** B) Salesforce requires all outbound HTTP callout destinations to be registered in Remote Site Settings (or as Named Credentials), which act as an allowlist of approved external endpoints for security purposes.
* **Distractor Analysis:**
  * *Why B is correct:* Before any Apex HTTP callout can succeed, the target URL must be registered. Named Credentials also store authentication details securely, so Apex code does not need to hard-code credentials.
  * *Why A is incorrect:* Connected Apps configure external systems calling *into* Salesforce via OAuth; they do not control outbound calls from Salesforce to external systems.
  * *Why C is incorrect:* Validation Rules evaluate field data for correctness before saves; they cannot make HTTP API calls to external systems.
  * *Why D is incorrect:* A Batch class addresses scheduling and volume, not the security allowlist requirement. Without a Remote Site Setting, even a Batch class callout would fail with a `CalloutException`.

---

### Question 5

When integrating Salesforce with an SAP system for a nightly customer account sync, which integration pattern is most appropriate?

* A) Real-time synchronous REST API call triggered every time a user views an Account record in Salesforce
* B) Scheduled batch integration that extracts updated Account records from SAP, transforms the data, and loads it into Salesforce once per night
* C) A SOAP web service call that blocks the SAP user's screen until Salesforce confirms receipt
* D) Direct database replication between the SAP HANA database and the Salesforce database

* **Correct Answer:** B) A scheduled nightly batch integration is the appropriate pattern for a bulk account sync — it processes high volumes efficiently, avoids real-time latency impacts on users, and aligns with how SAP data is typically extracted.
* **Distractor Analysis:**
  * *Why B is correct:* Batch/scheduled integration is the standard pattern for bulk master data synchronization between ERP and CRM. The ETL cycle (Extract from SAP, Transform field mappings, Load to Salesforce) runs at low-traffic hours to avoid impacting operational users.
  * *Why A is incorrect:* Triggering a live SAP API call every time a user opens an Account page would create excessive load on the SAP system and introduce latency into the Salesforce user experience for data that changes infrequently.
  * *Why C is incorrect:* A synchronous SOAP call that blocks a user's screen is appropriate only for real-time, user-driven transactions (like order placement confirmation) — not for bulk background data synchronization.
  * *Why D is incorrect:* Direct database replication between SAP HANA and Salesforce is technically impossible; Salesforce does not expose its underlying database for direct external replication. All Salesforce data access is through the API layer.
