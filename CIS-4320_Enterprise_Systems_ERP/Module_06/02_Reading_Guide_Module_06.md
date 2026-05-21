# Reading Guide: Module 06 - Supply Chain Management Integrations

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 06 - Supply Chain Management Integrations**! Supply chain management is one of the most operationally complex functions an ERP system supports. This module covers how SAP's Materials Management (MM) and Warehouse Management (WM) modules coordinate the procure-to-pay process — from identifying material needs through purchasing, receiving, storing, and paying vendors.

You will learn how Material Requirements Planning (MRP) automates procurement decisions, how inventory levels are tracked in real time, and how supplier master data ties every procurement transaction to a verified vendor record.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Supply Chain Management (SCM)**: The end-to-end coordination of the flow of goods, services, information, and finances from raw material suppliers through production and distribution to the end customer. ERP SCM modules automate procurement, inventory, and logistics to reduce cost and improve delivery reliability.
* **Inventory control**: The ERP function that tracks real-time stock levels across all warehouse locations, triggering replenishment when quantities fall below defined reorder points and preventing stock-outs or costly over-stocking.
* **Material Requirements Planning (MRP)**: An ERP planning algorithm that calculates what materials are needed, in what quantities, and by what dates — based on sales orders, bills of materials (BOMs), existing inventory levels, and production schedules. MRP generates automatic purchase requisitions and production orders to fulfill demand.
* **Logistics**: In ERP context, the coordination of goods movement — inbound from vendors (goods receipt), between warehouse locations (transfer orders), and outbound to customers (delivery and shipment). SAP's logistics execution modules track every physical movement with a system transaction.
* **Vendor records**: Master data records in SAP that store all information needed to do business with a supplier — name, address, bank account, payment terms, tax classification, and purchasing conditions. Vendor master records must be created and maintained before any purchasing transactions can be processed.

---

### 2. Certification Exam Tips

* **SAP MM procure-to-pay cycle:** Know the end-to-end process: Purchase Requisition → Purchase Order → Goods Receipt → Invoice Verification (three-way match) → Payment. Each step has a specific transaction code in SAP (ME51N, ME21N, MIGO, MIRO). Exam questions frequently test the correct sequence.
* **MRP planning run:** SAP MRP (transaction MD01/MD02) reads demand from sales orders and planned independent requirements, then nets against current stock and open orders to generate procurement proposals. Know the difference between a planned order (internal production) and a purchase requisition (external procurement).
* **Stock types:** SAP distinguishes between unrestricted stock (available for use), quality inspection stock (received but not yet released), and blocked stock (rejected). Exam questions may ask which stock type is consumed by a sales order (unrestricted only).
* **Salesforce relevance:** Salesforce Manufacturing Cloud and Salesforce Order Management integrate with back-end ERP supply chain modules. Understanding how ERP manages inventory and fulfillment helps you configure Salesforce order-to-cash processes correctly.
* **Study Resource:** Review the free [openSAP Materials Management](https://open.sap.com) course units for a walkthrough of the SAP MM procure-to-pay process with system screenshots.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Review the [openSAP platform](https://open.sap.com) for free SAP Materials Management course content covering purchase orders, goods receipts, and MRP planning runs.
* **Required Video:** Watch the video lecture on **Supply Chain Management Integrations** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Run a mock Material Requirements Planning (MRP) request**: Given a bill of materials, a sales order demand list, and current inventory levels, manually calculate the net requirements and identify which materials require a purchase requisition.
* **Track inventory levels and purchase triggers**: Map the reorder point logic for three materials with different lead times and minimum stock levels, showing at what stock level a purchase requisition should automatically fire.
* **Map supply chain links**: Draw a flow diagram tracing a single purchase order from vendor selection through goods receipt to the financial posting in Accounts Payable, labeling each module (MM, WM, FI-AP) responsible for each step.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to sequence the procure-to-pay steps in the correct order.
* [ ] Review [openSAP](https://open.sap.com) for free SAP Materials Management course content.
* [ ] Watch the video lecture on **Supply Chain Management Integrations** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab MRP calculation, reorder point mapping, and supply chain flow diagram.
* [ ] Proceed to the weekly quiz.
