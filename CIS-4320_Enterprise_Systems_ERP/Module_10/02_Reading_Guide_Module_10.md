# Reading Guide: Module 10 - Customizing ERP Systems

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 10 - Customizing ERP Systems**! One of the most important skills in enterprise systems work is knowing *when* to use configuration versus custom code — and understanding the specific tools each platform provides. This module covers the spectrum from no-code configuration settings through low-code automation tools to custom programming in SAP ABAP and Salesforce Apex.

Customization decisions made during ERP implementation have long-term consequences: over-customization increases upgrade costs and introduces fragility. Both the SAP and Salesforce certification paths test your ability to distinguish standard configuration from custom development and choose the appropriate approach.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Low-code tools**: Platform-provided visual development environments that allow administrators and business analysts to build automation, forms, and integrations without writing traditional code. Salesforce Flow Builder and SAP BTP's low-code tools are the primary examples tested on their respective exams.
* **Proprietary scripting (Salesforce Apex, SAP ABAP)**: Platform-specific programming languages used for custom logic that cannot be achieved through configuration or low-code tools. Apex is a Java-like language for Salesforce server-side logic; ABAP (Advanced Business Application Programming) is SAP's proprietary language for reports, enhancements, and integrations.
* **Database triggers**: Code that executes automatically when a specific database event occurs (insert, update, delete). In Salesforce, Apex Triggers fire on DML operations on `sObject` records. In SAP ABAP, database triggers and Business Add-Ins (BAdIs) intercept standard transactions to inject custom logic.
* **Validation rules**: Logic expressions that enforce data quality by blocking record saves when conditions are violated. In Salesforce, validation rules use formula syntax to evaluate field values and display error messages. In SAP, field-level validations are configured in customizing and reinforced by user exits.

---

### 2. Certification Exam Tips

* **Salesforce configuration vs. code:** The Associate exam strongly emphasizes declarative (no-code/low-code) solutions. Before reaching for Apex, always consider whether a Flow, Validation Rule, Formula Field, or Process-level setting can solve the problem. The exam reward order is: Workflow/Approval → Flow → Apex.
* **Apex trigger best practices:** The Salesforce exam expects you to know the "one trigger per object" pattern and bulkification (handling collections of records, not single records, in trigger logic). Triggers that query inside loops cause governor limit violations.
* **SAP ABAP vs. configuration:** In SAP implementations, the distinction between IMG (Implementation Guide) configuration and custom ABAP development is critical. Modification of SAP standard code ("modifications") is strongly discouraged; "enhancements" using BAdIs and User Exits are the approved extension approach.
* **Upgrade impact of customization:** Every custom Apex class, ABAP program, or trigger must be retested after a platform upgrade. Heavy customization multiplies upgrade cost. The Salesforce exam emphasizes the advantage of Salesforce's upgrade-safe declarative tools.
* **Study Resource:** Complete the Salesforce Trailhead module [Apex Basics & Database](https://trailhead.salesforce.com/content/learn/modules/apex_database) — a free, no-cost introduction to Apex programming that provides the code literacy needed to understand customization concepts tested on the Associate exam.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Complete the Salesforce Trailhead module [Apex Basics & Database](https://trailhead.salesforce.com/content/learn/modules/apex_database) — a free introduction to Salesforce's proprietary server-side language, covering classes, triggers, and DML operations.
* **Required Video:** Watch the video lecture on **Customizing ERP Systems** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Write a mock validation rule**: In your Salesforce Developer org, create a validation rule on the Opportunity object that blocks saving if the Close Date is in the past and the Stage is not "Closed Won" or "Closed Lost," and test it with sample records.
* **Draft Apex trigger pseudo-code**: Write pseudo-code for an Apex trigger that fires after a Case is updated, checks if the Status field changed to "Closed," and sets a custom "Resolution Date" field to today's date. Identify the bulkification pattern required.
* **Test trigger conditions**: Document three test scenarios (a new Case being created, a Case status changing to Closed, and a Case description being updated) and predict which of your trigger scenarios would fire for each.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to give a real-world example of each customization type.
* [ ] Complete [Apex Basics & Database](https://trailhead.salesforce.com/content/learn/modules/apex_database) on Trailhead (earn the badge).
* [ ] Watch the video lecture on **Customizing ERP Systems** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab validation rule, Apex pseudo-code, and trigger test scenario exercises.
* [ ] Proceed to the weekly quiz.
