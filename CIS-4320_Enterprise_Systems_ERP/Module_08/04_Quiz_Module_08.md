# Quiz: Module 08 — Salesforce Service Cloud and Case Management

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Salesforce Administrator / SAP S/4HANA Essentials

---

### Question 1

A customer sends an email to a company's support address and a Case is automatically created in Salesforce. Which feature is responsible for this automatic Case creation, and what value will the Origin field contain on the resulting Case?

- A) Web-to-Case; Origin = Web
- B) Email-to-Case; Origin = Email
- C) Omni-Channel routing; Origin = Phone
- D) Case Assignment Rule; Origin = Internal

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Email-to-Case monitors a designated support mailbox and converts inbound emails into Case records automatically. The Origin field is set to Email by the feature. The email subject becomes the Case Subject and the email body becomes the Description.
- *Why A is incorrect:* Web-to-Case converts website form submissions into Cases, not emails. Web-to-Case sets Origin to Web, not Email.
- *Why C is incorrect:* Omni-Channel routes existing Cases to agents — it does not create Cases from incoming communications. Origin is set at case creation, not during routing.
- *Why D is incorrect:* Case Assignment Rules route Cases after they are created — they do not create Cases or set the Origin field.

---

### Question 2

A support manager wants Cases from customers labeled as "Enterprise" accounts to automatically route to the Enterprise Support Queue, while all other Cases go to the General Support Queue. Which Salesforce feature should the administrator configure?

- A) Escalation Rule — to move Cases to the Enterprise Queue after 1 hour if unresolved
- B) Case Assignment Rule — to route newly created Cases based on Account Type criteria
- C) Validation Rule — to require that Enterprise account Cases cannot be saved without queue assignment
- D) Flow Builder — to send a notification email to the Enterprise Queue manager when a Case is created

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Case Assignment Rules evaluate criteria on Cases at creation and assign them to the matching Queue or agent. Account Type = Enterprise is a valid criteria field. This is the purpose-built Salesforce feature for automatic routing at case creation.
- *Why A is incorrect:* Escalation Rules act on Cases that have been sitting open for too long — they are time-based, not criteria-based at creation. They reassign Cases that are already assigned, not fresh incoming Cases.
- *Why C is incorrect:* Validation Rules block saves when data is invalid — they enforce data quality, not record routing. A Validation Rule cannot route a Case to a Queue.
- *Why D is incorrect:* A Flow sending a notification email is a valid supplemental action but is not the mechanism for routing ownership. The Case Owner field (pointing to the Queue) must be set, which requires an Assignment Rule, not a Flow notification.

---

### Question 3

A Priority 1 Case has been open for 5 hours without resolution. The Entitlement attached to the customer's Account defines a Resolution Milestone of 4 hours. What Service Cloud feature is responsible for taking automated action when this Milestone deadline is missed?

- A) Case Assignment Rule — it reassigns the Case to a new Queue based on the elapsed time
- B) Knowledge Article — it surfaces a solution automatically when the timer expires
- C) Milestone Violation Action — it fires when the Milestone deadline is exceeded and executes configured automated actions such as reassignment and notification
- D) Omni-Channel routing — it re-queues the Case to a different agent based on capacity

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Milestone Violation Actions are configured within an Entitlement Process and fire automatically when a Milestone deadline is exceeded. They can reassign the Case, send email notifications, change the Priority, or trigger other automated steps — all without manual intervention.
- *Why A is incorrect:* Case Assignment Rules fire at Case creation based on field criteria, not on elapsed time. They cannot respond to a timer expiration.
- *Why B is incorrect:* Knowledge Articles are reference content for agents. They do not fire on timers or take actions when deadlines are missed.
- *Why D is incorrect:* Omni-Channel routes work items to available agents based on capacity. It does not respond to SLA Milestone violations or re-route Cases based on time elapsed.

---

### Question 4

Which of the following correctly describes the relationship between Entitlements, Entitlement Processes, and Milestones in Salesforce Service Cloud?

- A) An Entitlement Process contains multiple Entitlements; each Entitlement contains one Milestone
- B) A Milestone contains multiple Entitlement Processes; each Entitlement Process links to one Account
- C) An Entitlement is linked to an Account and references an Entitlement Process; the Entitlement Process defines the sequence of Milestones applied to Cases
- D) Milestones are independent of Entitlements and are manually added to each Case by the agent

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* This is the correct hierarchy. Account has an Entitlement. The Entitlement references an Entitlement Process. The Entitlement Process defines the Milestones (First Response, Resolution) and their time limits and actions. Cases created for customers with Entitlements inherit this chain automatically.
- *Why A is incorrect:* The hierarchy is reversed. An Entitlement Process defines Milestones; it is not contained within an Entitlement. Multiple Milestones are contained within one Entitlement Process.
- *Why B is incorrect:* This description inverts the entire hierarchy. Entitlement Processes are not contained within Milestones. Entitlement Processes are the parent objects that contain Milestone definitions.
- *Why D is incorrect:* Milestones are not manually added case by case. They are defined in the Entitlement Process and applied automatically to Cases when the associated Entitlement is triggered.

---

### Question 5

A Salesforce Knowledge Article is currently in "In Review" status. Which statement accurately describes who can see this article?

- A) All agents and all customers with portal access can see In Review articles
- B) Only Knowledge Managers can see In Review articles; they are not visible to agents or customers
- C) In Review articles are visible to all agents but hidden from customers until Published
- D) In Review articles are automatically promoted to Published status after 48 hours

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The "In Review" status means the article has been submitted for approval but not yet approved. Only Knowledge Managers and the article author (depending on permissions) can see it. It is not visible to agents or customers until it reaches Published status.
- *Why A is incorrect:* Customer portal access is limited to Published articles. In Review articles have not been approved and are not surfaced to agents or customers in search results.
- *Why C is incorrect:* Agents cannot see In Review articles through the standard Knowledge search — articles must be Published to appear in agent-facing search results and Knowledge Suggestions.
- *Why D is incorrect:* There is no automatic time-based promotion in the standard Knowledge lifecycle. Articles remain in In Review status until a Knowledge Manager manually approves and publishes them.

---

### Question 6

An administrator wants to configure Salesforce so that agents handling Live Chat sessions cannot simultaneously be assigned more than two Chat sessions at once, but can still receive Cases up to a capacity of three. Which Omni-Channel feature controls these per-channel capacity limits?

- A) Presence Status — agents set their own limits by choosing the appropriate availability status
- B) Service Channel and Routing Configuration — capacity weights and limits are set per channel in Routing Configuration
- C) Case Assignment Rule — the rule limits the number of Cases assigned to a single agent
- D) Escalation Rule — the rule reassigns work items when an agent's threshold is exceeded

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* In Omni-Channel, Routing Configurations define capacity limits per Service Channel. Each work type (Chat, Case) has its own Routing Configuration with a Units of Capacity setting. A Chat session might consume 2 units while a Case consumes 1. The agent's total capacity (set in Presence Configuration) limits how many units they can hold across all active channels simultaneously.
- *Why A is incorrect:* Presence Status controls whether an agent is available for routing at all — it does not set numeric capacity limits per channel. An agent in "Available for Chat" status still has their capacity controlled by the Routing Configuration, not the status itself.
- *Why C is incorrect:* Case Assignment Rules determine which agent or queue receives a Case. They do not enforce capacity limits or prevent overloading individual agents.
- *Why D is incorrect:* Escalation Rules act on Cases that have been sitting open too long without resolution. They are not a capacity management tool and do not reassign work based on agent workload thresholds.

---

### Question 7

A support agent is working in the Salesforce Service Console and opens a Case about a login error. Within seconds, a panel on the right side of the screen automatically displays three Knowledge Articles with titles related to login authentication issues. Which feature is providing these automatic article suggestions?

- A) Case Assignment Rule — it routes Cases to agents who have authored relevant articles
- B) Einstein Activity Capture — it syncs the agent's email history to surface related article conversations
- C) Knowledge Suggestions — it searches the Knowledge Base using the Case subject and description keywords and surfaces relevant Published articles automatically
- D) Omni-Channel routing — it attaches related Knowledge Articles to Cases before routing them to the agent

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Knowledge Suggestions is the Service Console feature that automatically searches the Knowledge Base using the Case Subject and Description as keyword inputs. Matching Published articles appear in the Knowledge sidebar panel without the agent performing a manual search.
- *Why A is incorrect:* Case Assignment Rules route Case ownership — they have no connection to Knowledge article authorship or suggestion surfacing.
- *Why B is incorrect:* Einstein Activity Capture syncs emails and calendar events to Salesforce records. It is a Sales Cloud productivity feature and does not surface Knowledge Articles in service cases.
- *Why D is incorrect:* Omni-Channel assigns Cases to agents based on availability and capacity. It does not attach or surface Knowledge Articles during the routing process.

---

### Question 8

A company's support team has three tiers: Tier 1 handles general questions, Tier 2 handles technical escalations, and a Senior Team handles critical incidents. A Case that was assigned to Tier 1 at 9:00 AM is still open and unupdated at 5:00 PM (8 hours later). The company's policy says all Cases must be updated within 4 hours or automatically reassigned to Tier 2. Which Salesforce feature enforces this policy?

- A) Case Assignment Rule with criteria: Hours Since Update greater than 4
- B) Escalation Rule with a time trigger: Case age 4 hours without update — reassign to Tier 2 queue
- C) Validation Rule that blocks closing a Case without a status update within 4 hours
- D) Flow Builder scheduled to run every hour and check all open Cases for update timestamps

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Escalation Rules are time-based rules that fire when a Case has been open (or unmodified) for a specified duration. The rule can be configured to fire after 4 hours of no update and automatically change the Case Owner to the Tier 2 queue. This is exactly the use case Escalation Rules are designed for.
- *Why A is incorrect:* Case Assignment Rules fire at Case creation based on field criteria. They do not monitor elapsed time or respond to inactivity. "Hours Since Update" is not a standard Assignment Rule criteria field.
- *Why C is incorrect:* Validation Rules block record saves based on field conditions. They enforce data quality at the point of saving — they cannot take proactive action on Cases that have not been touched for 4 hours.
- *Why D is incorrect:* A scheduled Flow checking all open Cases every hour would technically work, but it is an inefficient custom solution that partially duplicates the built-in Escalation Rule feature. When a native feature exists for a requirement, using it is the administrator best practice and the correct exam answer.

---

### Question 9

A service team manager reviews a report showing that 35% of Cases closed last month did not have a Knowledge Article attached. She wants to ensure agents always search the Knowledge Base before closing a Case. Which approach is most consistent with Salesforce administrator best practices?

- A) Enable Einstein Activity Capture on all Cases to automatically attach articles at closure
- B) Create a Validation Rule that prevents Case closure if no Knowledge Article is linked to the Case
- C) Configure an Escalation Rule that fires when a Case reaches Closed status without an article
- D) Create a Case Report filtered by Cases with no linked Knowledge Articles and email it to managers weekly

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A Validation Rule can check whether a related Knowledge Article exists (using a formula that checks the linked article count field) and block the save if none is attached when Status = Closed. This enforces the behavior at the point of action — when the agent tries to close the Case — using a standard no-code tool.
- *Why A is incorrect:* Einstein Activity Capture syncs emails and calendar events to records. It does not attach Knowledge Articles or respond to Case closure events.
- *Why C is incorrect:* Escalation Rules fire on time-based triggers for open Cases. They do not monitor Case closure or check for missing related records like Knowledge Articles.
- *Why D is incorrect:* Emailing a weekly report to managers is a monitoring approach, not an enforcement approach. It identifies the problem after the fact but does not prevent agents from closing Cases without articles. Validation Rules prevent the behavior at the source.

---

### Question 10

Which of the following best describes the primary purpose of the Salesforce Service Console compared to the standard Salesforce Lightning app?

- A) The Service Console is a mobile-only interface designed for field service agents working without internet access
- B) The Service Console is a multi-panel workspace optimized for agents handling multiple Cases simultaneously, with work items, active record details, and related information visible in a single screen layout
- C) The Service Console replaces all standard Salesforce objects with service-specific versions that cannot be used in the standard app
- D) The Service Console is available only to Salesforce administrators and is used exclusively for configuring queues and assignment rules

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The Service Console is a specialized app layout designed for high-volume support environments. Its multi-panel design — navigation list on the left, active record in the center, related tabs at the bottom — lets agents work multiple Cases simultaneously without navigating away and losing context. This is its defining characteristic.
- *Why A is incorrect:* The Service Console is a browser-based desktop interface, not a mobile-only tool. Salesforce has a separate mobile app. The Service Console requires a stable internet connection like any Salesforce browser-based experience.
- *Why C is incorrect:* The Service Console uses the same standard Salesforce objects (Cases, Accounts, Contacts, Knowledge) as the standard app. It is a different visual layout and app configuration, not a separate set of objects.
- *Why D is incorrect:* The Service Console is designed for support agents handling customer Cases — not for administrators configuring Salesforce. Admins configure queues and assignment rules in Setup, which is accessed through any Salesforce app or the gear icon, not through the Service Console.
