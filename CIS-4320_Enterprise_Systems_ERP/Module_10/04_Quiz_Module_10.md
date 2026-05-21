# Quiz: Module 10 - Customizing ERP Systems

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

Which programming language is proprietary to SAP and used to develop custom reports, enhancements, and integrations within the SAP system?

* A) Python
* B) ABAP (Advanced Business Application Programming)
* C) Apex
* D) SQL Server T-SQL

* **Correct Answer:** B) ABAP is SAP's proprietary programming language, used for custom reports, BAdI implementations, RFC function modules, and data migration programs within the SAP landscape.
* **Distractor Analysis:**
  * *Why B is correct:* ABAP has been SAP's core development language since the 1980s. All SAP standard application code is written in ABAP, and it is the language used for customer extensions and enhancements in SAP ECC and S/4HANA.
  * *Why A is incorrect:* Python is a general-purpose scripting language used in data science and automation; it is not the native SAP development language, though it can be used in integration scenarios via APIs.
  * *Why C is incorrect:* Apex is Salesforce's proprietary server-side programming language for the Force.com platform, not for SAP.
  * *Why D is incorrect:* T-SQL is Microsoft SQL Server's dialect of SQL; while SAP can run on SQL Server as a database backend, T-SQL is not the SAP application development language.

---

### Question 2

Which of the following best describes **low-code tools** in the context of ERP and CRM platform customization?

* A) Stripped-down programming languages that require less syntax than full languages but still require writing code in a text editor
* B) Visual, drag-and-drop development environments that allow non-programmers to build automation, forms, and integrations without writing traditional code
* C) Compressed code libraries that reduce the file size of custom programs deployed to the ERP system
* D) Code review tools that automatically check custom programs for syntax errors before deployment

* **Correct Answer:** B) Low-code tools provide visual development interfaces — like Salesforce Flow Builder or SAP BTP's AppGyver — that enable administrators and business analysts to build functional automations without programming expertise.
* **Distractor Analysis:**
  * *Why B is correct:* Low-code platforms are a defining feature of modern cloud ERP and CRM. Salesforce Flow Builder, for example, allows complex multi-step automations to be built by drag-and-drop configuration, reducing dependence on developer resources.
  * *Why A is incorrect:* Low-code refers to minimal or no writing of traditional code, not to simplified programming syntax in a text editor.
  * *Why C is incorrect:* Code compression is a deployment optimization technique unrelated to the definition of low-code development tools.
  * *Why D is incorrect:* Syntax checking tools are part of development IDEs; they are not what "low-code" refers to.

---

### Question 3

A Salesforce administrator wants to prevent sales reps from saving an Opportunity record if the Amount field is blank and the Stage is "Proposal/Price Quote." Which Salesforce tool should the administrator use — without writing any Apex code?

* A) An Apex Trigger on the Opportunity object
* B) A Validation Rule using a formula expression to check the Amount and Stage field values
* C) A Flow that runs after the record is saved and deletes records missing the Amount field
* D) A custom Apex class called by a Lightning Web Component on the Opportunity page

* **Correct Answer:** B) A Validation Rule is the correct declarative tool — it uses a formula to evaluate field conditions and blocks the save with an error message, requiring no code.
* **Distractor Analysis:**
  * *Why B is correct:* Salesforce Validation Rules evaluate formula conditions before a record is saved. The formula `AND(ISPICKVAL(StageName, "Proposal/Price Quote"), ISBLANK(Amount))` would block the save and display an error to the user.
  * *Why A is incorrect:* An Apex Trigger could enforce this logic, but it requires code — the question specifically asks for a no-code solution, and the declarative Validation Rule is always preferred for this type of requirement.
  * *Why C is incorrect:* A Flow that runs after the save and then deletes the record would create a poor user experience (the record briefly exists before deletion) and is far more complex than needed.
  * *Why D is incorrect:* A custom Apex class and Lightning Web Component is the most complex and maintenance-heavy approach for a simple field validation requirement.

---

### Question 4

In SAP, a customer wants to add custom business logic that fires every time a vendor is saved in transaction XK01/XK02, without modifying SAP standard code. Which SAP extension approach is recommended?

* A) Direct modification of the SAP standard SAPMF02K function group source code
* B) Implementing a Business Add-In (BAdI) provided by SAP at the relevant extension point in the vendor master save process
* C) Creating a new ABAP program that replaces the standard XK01 transaction entirely
* D) Modifying the database table USR02 directly to add the custom validation logic

* **Correct Answer:** B) SAP Business Add-Ins (BAdIs) are the recommended, upgrade-safe extension mechanism — they inject custom logic at predefined extension points without touching SAP standard code.
* **Distractor Analysis:**
  * *Why B is correct:* BAdIs (and the older User Exit/Customer Exit pattern) are SAP's official approach for adding customer-specific logic. The custom implementation is stored separately from standard code, so SAP upgrades do not overwrite it.
  * *Why A is incorrect:* Modifying SAP standard source code ("modifications") is strongly discouraged because upgrades overwrite the changes, creating maintenance nightmares and voiding support agreements.
  * *Why C is incorrect:* Replacing a standard transaction with a custom program eliminates all future standard enhancements SAP delivers and creates a major upgrade liability.
  * *Why D is incorrect:* Modifying security table USR02 directly is dangerous, unsupported, and would have no effect on vendor master save logic; it would corrupt the user authentication system.

---

### Question 5

A Salesforce developer writes an Apex trigger on the Contact object that queries a related object inside a for loop processing 200 Contact records. Which problem does this code pattern cause?

* A) The trigger will fail to compile because Apex does not support for loops on `sObject` collections
* B) The trigger will violate Salesforce governor limits by executing up to 200 SOQL queries in a single transaction, exceeding the 100-query limit
* C) The trigger will run correctly but log a warning in the developer console about loop performance
* D) The trigger will automatically optimize itself to batch the queries through Salesforce's query optimizer

* **Correct Answer:** B) Querying inside a for loop (one query per record) is the classic Apex anti-pattern — processing 200 records would execute 200 SOQL queries, exceeding the per-transaction governor limit of 100 SOQL queries and throwing a LimitException.
* **Distractor Analysis:**
  * *Why B is correct:* Salesforce enforces strict per-transaction limits (governor limits) to ensure fair resource sharing across the multi-tenant platform. The correct pattern is to collect all record IDs first, then execute one query outside the loop to retrieve all related records at once (bulkification).
  * *Why A is incorrect:* Apex fully supports for loops on `List<sObject>` collections; the syntax is valid and will compile without errors.
  * *Why C is incorrect:* Salesforce does not merely log warnings for governor limit approaches; it throws a hard LimitException that rolls back the entire transaction when limits are exceeded.
  * *Why D is incorrect:* Salesforce does not automatically rewrite or optimize Apex code. The developer is responsible for writing bulkified code that handles collections rather than individual records.
