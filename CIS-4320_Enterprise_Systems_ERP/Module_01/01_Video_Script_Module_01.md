# Video Script: Module 01 - Enterprise Systems Concepts

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 20-22 minutes

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### [00:00 - 01:30] Opening and Welcome

Professor Nash on camera. Title card: "Module 01 - Enterprise Systems Concepts."

"Welcome to CIS-4320 Enterprise Systems and ERP at Texas Wesleyan University. I'm Professor Nash, and this course is going to do something a little different from most technology courses: we're going to spend an entire semester understanding not just how enterprise software works, but why it exists, what business problems it solves, and how the two dominant platforms — SAP and Salesforce — have shaped the way large organizations run their operations.

By the end of this module you will understand what an enterprise system is, why businesses invest millions of dollars in ERP implementations, and what the foundational design principles are that make these systems work. These are also the concepts you will see first on both the Salesforce Certified Associate exam and the SAP Certified Associate exam.

Let's get started."

---

### [01:30 - 04:30] What Is an Enterprise System?

Cut to slide: "The Problem Enterprise Systems Solve."

"Before we define what an enterprise system is, let's talk about what happens when a company doesn't have one.

Imagine a manufacturing company with 500 employees. The finance department tracks all invoices in a custom spreadsheet. The warehouse team manages inventory in a database they built themselves. The HR department keeps employee records in a cloud folder. And the sales team logs customer orders in their own separate system.

Now imagine that a major customer places an order. The sales team logs it in their system. Great. But does the warehouse know the order exists? Not automatically. Someone has to email the warehouse. Does finance know to prepare the invoice? Not until someone tells them. Does HR know that a weekend shift is needed to fulfill the order? Not until a manager manually coordinates it.

This is called the functional silo problem. Every department has data and processes that are isolated from every other department. And when those silos exist, you get errors, delays, and decisions made on incomplete information.

[SHOW DIAGRAM: A series of isolated bubbles — Finance, Sales, Warehouse, HR, Purchasing — each with their own data store and no connections between them. Label the gaps between departments as 'Manual Handoffs.']

An enterprise system solves this by replacing those isolated tools with an integrated platform where every department shares a single database and a common process model. When the sales team creates that order, the warehouse sees it in real time. Finance is automatically notified. Inventory counts are updated. That is what integration means in the ERP context."

---

### [04:30 - 08:00] The Architecture of ERP: Modules and the Shared Database

Cut to slide: "Modular Architecture and the Shared Database."

"Enterprise systems are built on two foundational design principles: modular architecture and integrated data.

Let me start with modular architecture. An ERP system like SAP S/4HANA is not one single program. It is a collection of specialized modules — each one handling a distinct area of the business. You have the Financial Accounting module, abbreviated FI. You have Materials Management, MM. Sales and Distribution, SD. Human Capital Management, HCM. And so on.

[SHOW DIAGRAM: A large circle in the center labeled 'Shared Database.' Around it, connected by arrows: FI (Finance), MM (Materials Management), SD (Sales & Distribution), HCM (Human Resources), PP (Production Planning), CO (Controlling). All modules point inward to the central database.]

The critical design insight is that all of these modules share one common database. That sounds simple, but it has profound business consequences. When the Sales module records a customer order, the Inventory module sees that stock has been committed. When the Warehouse records a shipment, the Finance module automatically creates the invoice. Every module reads from and writes to the same central data store. There is no manual synchronization needed. There is no batch overnight update. The data is consistent in real time for every user in every department.

This is what we mean when we say ERP creates a single source of truth.

Now, the modular structure also means companies don't have to implement everything at once. A company might start with just Finance and HR, then add Supply Chain two years later. The modules are independently licensable and activatable — which is also why you see SAP quote license costs per module.

Salesforce follows the same principle with its cloud products. Sales Cloud handles the customer-facing sales pipeline. Service Cloud handles support cases. Marketing Cloud handles campaigns. Each is a separate product, but they all share the same underlying Salesforce platform and data model. When a salesperson closes a deal in Sales Cloud, the service team in Service Cloud can immediately see that this is now an active customer. That cross-product visibility is the CRM version of the same integration principle."

---

### [08:00 - 11:00] ERP vs. CRM: Understanding the Distinction

Cut to slide: "ERP vs. CRM — Where Each Platform Operates."

"One of the most important distinctions you need to carry through this entire course — and one that appears on both certification exams — is the difference between ERP and CRM.

ERP handles back-office operations. When we say back-office, we mean the internal operations of the company: accounting and financial reporting, procurement and supply chain, manufacturing and production planning, human resources and payroll. These are the processes that keep the business running internally. The people doing back-office work are largely invisible to customers.

CRM — Customer Relationship Management — handles customer-facing operations. Sales, marketing campaigns, customer service and support cases. These are the processes where the company interacts with its customers and prospects.

[SHOW DIAGRAM: Two columns side by side. Left column: 'ERP - Back Office' with examples: General Ledger, Purchase Orders, Inventory Management, Payroll, Production Planning. Right column: 'CRM - Front Office' with examples: Sales Pipeline, Leads and Opportunities, Customer Service Cases, Marketing Campaigns, Customer Accounts. An arrow labeled 'Integration Point' connects the two columns in the middle.]

SAP S/4HANA is primarily an ERP platform. Salesforce is primarily a CRM platform. Many large enterprises run both — an SAP system managing their finances and supply chain, and a Salesforce system managing their customer relationships — and they connect the two through integration middleware.

This is not a competition between the platforms. They are complementary. A sales rep using Salesforce might need to know a customer's payment status or their past order history — that data lives in SAP. An accounts receivable clerk in SAP needs to know when a customer signed a contract — that event originates in Salesforce. Good enterprise architecture brings those two worlds together.

Exam tip: If you see a question that describes a business process involving accounts payable, inventory, or payroll, you are in ERP territory. If the question describes sales pipeline management, customer service tickets, or marketing automation, you are in CRM territory."

---

### [11:00 - 14:30] Why Do Companies Invest in ERP?

Cut to slide: "The Business Case for ERP."

"If enterprise systems are so expensive — and they are, we are talking about implementations that can cost tens of millions of dollars for a large company — why do organizations make that investment?

The answer comes down to three core business drivers: data consistency, process efficiency, and regulatory compliance.

Data consistency means that every report, every dashboard, every decision in the company is based on the same numbers. When the CFO presents the quarterly earnings report, she is pulling from the same data that the VP of Operations used last week. There is no debate about which version of the spreadsheet is correct, because there is only one database.

Process efficiency comes from standardization. ERP systems encode best practices into their process flows. When you implement SAP's Accounts Payable module, you are not just buying software — you are adopting SAP's model of how the procure-to-pay process should work, a model that reflects decades of implementation experience across thousands of companies. That standard process is typically more efficient than whatever ad hoc process the company evolved on its own.

Regulatory compliance becomes manageable because ERP systems generate the audit trails that regulators require. Every financial transaction has a document number, a timestamp, a user ID, and a before/after change record. When the external auditor asks for evidence that internal controls are working, the ERP system can produce that evidence automatically.

[SHOW DIAGRAM: Three pillars supporting a platform labeled 'Enterprise Value.' The pillars are labeled: 'Data Consistency,' 'Process Efficiency,' and 'Regulatory Compliance.']

And the flip side is also true: companies that try to avoid ERP often pay the price in a different way — duplicate data entry, reporting that takes weeks instead of hours, and costly manual reconciliation at month-end close."

---

### [14:30 - 17:30] The ERP Market: SAP, Oracle, Salesforce, and Microsoft

Cut to slide: "The Enterprise Software Landscape."

"Let's briefly orient ourselves in the market, because the certification exams assume you know who the major players are and what they are known for.

SAP SE, based in Germany, is the global leader in ERP for large enterprises. SAP's flagship product is S/4HANA — the successor to the older SAP ECC platform. SAP is used by the majority of Fortune 500 companies for their core back-office operations. If you take an enterprise systems job at a large manufacturer, retailer, or financial services firm, there is a very high probability you will encounter SAP.

Oracle Corporation is SAP's primary competitor in the enterprise ERP space. Oracle Cloud ERP (formerly Oracle Fusion) is the modern cloud version of Oracle's application suite. Oracle also owns NetSuite, which is popular in the mid-market segment.

Salesforce is the global leader in CRM. Salesforce's platform — Sales Cloud, Service Cloud, and the broader Salesforce ecosystem — is used by millions of organizations to manage customer relationships. Salesforce is unique in that its entire platform is SaaS: there is no on-premise version.

Microsoft Dynamics 365 combines ERP functionality (Finance, Supply Chain) with CRM functionality (Sales, Customer Service) in a single platform built on Microsoft Azure. For companies already using Microsoft 365 and Azure, Dynamics 365 has a natural integration advantage.

[SHOW DIAGRAM: A 2x2 matrix. X-axis: 'SMB to Enterprise.' Y-axis: 'Back-Office ERP to Front-Office CRM.' Place SAP in the Enterprise/ERP quadrant. Oracle Cloud ERP slightly lower in Enterprise/ERP. Salesforce in the Enterprise/CRM quadrant. Microsoft Dynamics 365 in the middle. NetSuite in the SMB/ERP quadrant.]

For this course, we focus primarily on SAP S/4HANA for ERP concepts and Salesforce for CRM concepts. That dual focus also aligns with the two certification paths this course prepares you for."

---

### [17:30 - 19:30] Connecting the Concepts to Certification

Cut to slide: "What the Certifications Test."

"Let me connect what we covered today to the actual certification exams.

The Salesforce Certified Associate exam tests your understanding of the Salesforce platform and ecosystem at a foundational level. Today's concepts are directly tested: what is CRM, why do companies use it, what objects are at the core of the Salesforce data model — Accounts, Contacts, Leads, Opportunities — and how the platform supports different user roles. The exam guide lists 'Salesforce Ecosystem and Terminology' as one of the primary topic areas.

The SAP Certified Associate — SAP S/4HANA Cloud Essential exams test whether you can map business processes to SAP modules and understand the system's core architecture. Today's concepts — functional silos, integrated data, modular architecture — are the conceptual foundation for every SAP-specific process question you will face.

For both exams, the most important habit you can build starting today is to always think in terms of business processes. Do not just memorize software features. Ask yourself: what business problem does this feature solve? What would go wrong without it? That business-first thinking is exactly what both certification programs reward."

---

### [19:30 - 21:00] Module Summary and Exam Tips

Cut to slide: "Module 01 Key Takeaways."

"Let's wrap up Module 01 with the key takeaways.

First: enterprise systems exist to solve the functional silo problem — isolated departmental systems that cannot share data automatically.

Second: ERP uses modular architecture, where specialized modules all share one central database, creating a single source of truth across the entire organization.

Third: ERP handles back-office operations; CRM handles customer-facing operations. SAP is the leading ERP vendor; Salesforce is the leading CRM vendor. Many enterprises run both.

Fourth: the business case for ERP rests on data consistency, process efficiency, and regulatory compliance.

Two exam tips before you go: First, on both the Salesforce and SAP exams, when you see a scenario describing data inconsistency between two departments, the correct answer almost always involves the integrated ERP eliminating the problem through a shared database. Second, memorize the distinction between ERP and CRM — it is tested directly.

For your reading this week, complete the Salesforce Trailhead module 'Salesforce Platform Basics' at trailhead.salesforce.com — it is free, it is hands-on, and it will reinforce everything we covered today. Then complete the lab and the quiz before our next session.

I'll see you in Module 02, where we tackle Business Process Management and start learning how to diagram the workflows that ERP systems are designed to execute."

---

### [End Card]

Text on screen:

- Complete Reading Guide 01
- Complete Lab 01 (Business Process Mapping Exercise)
- Complete Quiz 01 (10 questions)
- Post to Discussion Forum 01 (due Wednesday)
- Peer responses due Sunday
- Trailhead: trailhead.salesforce.com — "Salesforce Platform Basics"
