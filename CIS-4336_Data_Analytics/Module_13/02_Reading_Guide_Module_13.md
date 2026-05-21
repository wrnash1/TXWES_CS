# Reading Guide: Module 13 - Data Governance, Quality, and Privacy
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

### Introduction
Welcome to **Module 13 - Data Governance, Quality, and Privacy**! Data governance is the framework of policies, roles, and processes that ensures an organization's data is accurate, accessible to the right people, and protected from misuse. This module covers the governance and privacy concepts that appear throughout the **CompTIA Data+** exam: data privacy regulations (GDPR and CCPA), the definition and handling of personally identifiable information (PII), data masking and anonymization techniques, access control frameworks, and data stewardship roles.

As data analytics expands into every business function, the analyst's responsibility extends beyond computing correct answers. Analysts must understand what data they are permitted to access, how to protect sensitive information in their outputs, and what legal obligations govern the data they handle. These topics are heavily tested on the Data+ exam in scenario format.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Data privacy regulations (GDPR and CCPA)**: The General Data Protection Regulation (GDPR) is a European Union law that requires organizations to obtain explicit consent before collecting personal data, give individuals the right to access and delete their data, and report breaches within 72 hours. The California Consumer Privacy Act (CCPA) gives California residents similar rights — to know what data is collected, to opt out of its sale, and to request deletion. Both regulations impose significant fines for non-compliance.
*   **Personally identifiable information (PII)**: Any data that can be used, alone or in combination, to identify a specific individual. Direct PII includes name, Social Security number, email address, phone number, and date of birth. Indirect PII includes data that could identify someone when combined with other information — such as ZIP code, employer, and age together. Analysts must recognize PII in datasets and handle it according to organizational policy and applicable law.
*   **Data masking and anonymization**: Data masking replaces sensitive values with realistic but fictional substitutes — for example, replacing a real credit card number with `****-****-****-1234` in a test environment. Anonymization permanently removes or transforms identifiers so the data can no longer be linked to an individual. Pseudonymization replaces direct identifiers with a code, with the mapping stored separately — it is reversible, so pseudonymized data is still considered personal data under GDPR.
*   **Access control and the principle of least privilege**: Access control determines who can read, write, or delete data assets. Role-based access control (RBAC) assigns permissions to roles rather than individuals — users inherit permissions by being assigned to a role. The principle of least privilege dictates that users and systems should have only the minimum access required to perform their function — nothing more. This limits the damage from both insider threats and external breaches.
*   **Data stewardship and data catalog**: A data steward is a person responsible for the quality, governance, and appropriate use of a specific data domain (e.g., customer data, financial data). A data catalog is a searchable inventory of an organization's data assets — documenting what data exists, where it lives, who owns it, and what policies govern it. Data catalogs enable analysts to find trusted datasets and understand their lineage and sensitivity classification.

---

### 2. Certification Exam Tips
*   **Domain weight:** Data governance, quality, and privacy questions span Domain 1 (Data Concepts and Environments, ~15%) and Domain 2 (Data Collection and Management, ~25%) of the Data+ DA0-001 exam. Scenario questions frequently present a data handling situation and ask which governance control or privacy technique is most appropriate.
*   **Exam trap — anonymization vs. pseudonymization:** Anonymization is irreversible — the link to the individual is permanently destroyed. Pseudonymization is reversible — the key to re-identify the person is stored separately. GDPR treats pseudonymized data as still personal data. The exam may ask which technique produces data that is no longer subject to GDPR — the answer is anonymization, not pseudonymization.
*   **Exam trap — GDPR vs. CCPA scope:** GDPR applies to any organization processing data of EU residents, regardless of where the organization is based. CCPA applies to businesses meeting certain thresholds that collect personal information of California residents. An exam scenario involving a U.S. company with European customers falls under GDPR, not just domestic law.
*   **Exam trap — data masking in production vs. non-production:** Data masking is used to protect sensitive data in non-production environments (development, testing, analytics) where production-realistic data is needed but actual PII must not be exposed. Using real PII in a test environment is a governance violation.
*   **Study Resource:** The data ethics and governance chapters of [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/) address responsible data handling, bias, and privacy considerations in analytics. The [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238) demonstrates practical data handling techniques including column selection, filtering, and masking that relate directly to protecting sensitive data in analytical workflows.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the data ethics, privacy, and governance chapters in the OER Textbook: [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/). Focus on the sections covering responsible data use, privacy considerations in analysis, and the ethical obligations of data professionals.
*   **Required Video:** Watch the data handling and analysis sections of the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238), paying particular attention to column selection, data filtering, and transformation techniques that relate to managing sensitive data fields in analytical outputs.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Identify and classify PII columns in a customer dataset**: Review a dataset schema and label each column as PII, indirect PII, or non-sensitive, citing the specific attribute (name, email, SSN, ZIP code) that determines the classification.
*   **Apply data masking to sensitive columns**: Replace credit card numbers with masked values (retain last 4 digits only) and replace full names with initials, then verify the masked dataset cannot be used to re-identify individuals without external data.
*   **Document role-based access control assignments**: Define three roles (analyst, data engineer, executive) and specify which tables and columns each role can access based on the principle of least privilege, justifying each restriction.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the data ethics chapters in [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/).
- [ ] Watch the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238).
- [ ] Review the lab instructions and understand what each task requires.
- [ ] Proceed to the weekly hands-on lab activity.
