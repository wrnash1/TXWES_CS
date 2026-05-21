# Reading Guide: Module 08 - Human Capital Management Modules

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 08 - Human Capital Management Modules**! Human Capital Management (HCM) is the ERP domain responsible for managing the organization's workforce — from recruiting and onboarding through payroll, performance management, and eventual offboarding. SAP SuccessFactors is the cloud-based HCM suite that has become SAP's primary HR platform, while SAP HCM (on-premise) remains widely deployed.

This module is particularly relevant to students targeting the SAP Certified Associate (Human Resources) path. It also provides important context for Salesforce students who will encounter HR data integration scenarios when connecting Salesforce with enterprise HR systems.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Human Capital Management (HCM)**: The integrated set of practices and software tools for managing the workforce across its full lifecycle — recruiting, hiring, onboarding, learning, performance management, compensation, payroll, and offboarding. SAP SuccessFactors is SAP's cloud HCM platform; SAP ECC/HCM is the on-premise equivalent.
* **Payroll processing**: The periodic calculation and disbursement of employee compensation, including base salary, overtime, bonuses, tax withholdings, and benefit deductions. ERP payroll modules automate the calculation engine, ensure legal compliance with tax rules, and post the resulting journal entries to the General Ledger.
* **Time tracking**: The ERP function that captures employee working hours — through time entry, absence management, and shift scheduling — and feeds the data to payroll for accurate compensation calculation and to project cost accounting for labor cost allocation.
* **Employee onboarding**: The structured process of integrating a new hire into the organization — provisioning system access, completing legal documentation, assigning training modules, and introducing them to their team. ERP onboarding workflows automate task assignment and track completion status.
* **Performance metrics**: Quantifiable measures used to evaluate employee contribution and development — including goal completion rates, 360-degree feedback scores, and learning completion data. These metrics feed into compensation planning and succession planning processes within the HCM suite.

---

### 2. Certification Exam Tips

* **SAP SuccessFactors modules:** Know the six core SuccessFactors module groups: Employee Central (core HR), Recruiting, Onboarding, Learning, Performance & Goals, and Compensation. Exam questions may ask which module handles a specific HR function.
* **Payroll integration:** SAP SuccessFactors Employee Central Payroll integrates cloud HR data with payroll processing. Know that SuccessFactors Employee Central is the system of record for employee master data, and changes replicate to payroll in real time.
* **Position management vs. job management:** SAP HCM uses Position Management (organizational plan with defined positions in the org chart) while simpler HCM systems use flat job codes. Position management enables headcount planning and org structure reporting.
* **Salesforce relevance:** Salesforce does not provide native payroll functionality, but the Employee Experience platform (Salesforce for HR) and integration patterns with SuccessFactors are common in enterprise architectures. Understanding HCM data structures helps you configure integrations correctly.
* **Study Resource:** Complete the free [openSAP SuccessFactors overview](https://open.sap.com) courses for an introduction to the full SuccessFactors suite and how each module connects to the employee lifecycle.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Review the [openSAP platform](https://open.sap.com) for free SAP SuccessFactors introductory course materials covering Employee Central, Recruiting, and Performance & Goals modules.
* **Required Video:** Watch the video lecture on **Human Capital Management Modules** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Review payroll transaction database tables**: Trace the data flow from an employee's approved timecard through the payroll calculation engine to the final journal entry posted in the General Ledger, identifying which fields change at each step.
* **Map employee onboarding workflows**: Design a 10-step onboarding task list for a new software engineer hire, assigning each task to the responsible team (HR, IT, Manager, Employee) and specifying the due date relative to the start date.
* **Verify timecard hours calculations**: Given a sample weekly timecard with regular hours, overtime, and one sick day, manually calculate the gross pay using a provided pay rate and overtime multiplier, then verify your answer matches the ERP's expected output.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to name three HCM functions that feed data to the payroll process.
* [ ] Review [openSAP](https://open.sap.com) for free SAP SuccessFactors introductory course content.
* [ ] Watch the video lecture on **Human Capital Management Modules** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab payroll trace, onboarding workflow design, and timecard calculation exercise.
* [ ] Proceed to the weekly quiz.
