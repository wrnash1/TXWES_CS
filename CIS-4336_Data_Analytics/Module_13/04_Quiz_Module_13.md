# Quiz: Module 13 - Data Governance, Quality, and Privacy
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
A data analyst is preparing a customer dataset for a machine learning project. The dataset contains customer name, email address, home ZIP code, and purchase history. Which of the following columns contains direct Personally Identifiable Information (PII)?
*   A) Purchase history totals — aggregate spending amounts per customer.
*   B) Home ZIP code — a geographic area containing thousands of residents.
*   C) Email address — a unique identifier that directly links to a specific individual.
*   D) Product category — the type of item purchased, with no link to an individual.
*   **Correct Answer:** C) Email address — a unique identifier that directly links to a specific individual.
*   **Distractor Analysis:**
    *   *Why correct:* Direct PII uniquely identifies a specific individual without requiring combination with other data. An email address is assigned to one person and is therefore direct PII. Customer name is also direct PII and would be included in any complete PII inventory.
    *   A) Purchase totals are aggregate financial data — they do not identify an individual without being linked to an account. B) A ZIP code alone covers thousands of residents and is indirect PII — it can contribute to re-identification when combined with other attributes, but is not direct PII on its own. D) Product category is non-sensitive transactional metadata with no direct link to an individual identity.

---

**Question 2**
In data governance, which of the following most accurately defines **data masking**?
*   A) The permanent removal or transformation of all identifying attributes in a dataset so that no individual can be re-identified, even by combining the data with external sources.
*   B) The replacement of sensitive data values with realistic but fictional substitutes — such as replacing a real credit card number with a formatted placeholder — to protect PII in non-production environments while preserving data usability for development and testing.
*   C) A reversible technique that replaces direct identifiers with a code or token, storing the mapping in a separate secure location so the original values can be recovered by authorized parties.
*   D) An access control mechanism that restricts which columns of a database table are visible to a given user role, hiding sensitive fields from unauthorized queries.
*   **Correct Answer:** B) The replacement of sensitive data values with realistic but fictional substitutes — such as replacing a real credit card number with a formatted placeholder — to protect PII in non-production environments while preserving data usability for development and testing.
*   **Distractor Analysis:**
    *   *Why B is correct:* Data masking produces substitute values that look realistic (preserving format and data type) while containing no real personal information. It is the standard technique for creating safe copies of production data for development, testing, and analytics use cases.
    *   *Why A is incorrect:* Permanently removing or transforming all identifiers so re-identification is impossible describes anonymization, not masking. Anonymization is irreversible; masking may or may not be.
    *   *Why C is incorrect:* Replacing identifiers with tokens and storing a recoverable mapping describes pseudonymization. The key difference from masking is that pseudonymized data can be re-linked to the individual by an authorized party.
    *   *Why D is incorrect:* Restricting which table columns a user role can see describes column-level access control or column-level security — a permission management technique, not a data masking technique.

---

**Question 3**
A U.S.-based e-commerce company collects purchase data from customers in Germany, France, and Spain. The company's legal team asks whether GDPR applies. What is the correct answer?
*   A) No — GDPR only applies to companies incorporated in EU member states, not to U.S.-based companies.
*   B) No — the company is only subject to U.S. federal privacy law, regardless of where its customers are located.
*   C) Yes — GDPR applies to any organization that processes personal data of individuals located in the EU, regardless of where the organization itself is based.
*   D) Only partially — GDPR applies only to the company's EU-based servers and not to data processed on U.S. infrastructure.
*   **Correct Answer:** C) Yes — GDPR applies to any organization that processes personal data of individuals located in the EU, regardless of where the organization itself is based.
*   **Distractor Analysis:**
    *   *Why C is correct:* GDPR's scope is defined by the location of the data subjects (the individuals), not the location of the organization. Any company that collects, stores, or processes personal data of EU residents — even a company headquartered in Texas — must comply with GDPR when handling that data.
    *   *Why A is incorrect:* GDPR explicitly extends to non-EU organizations when they offer goods or services to EU residents or monitor their behavior. Country of incorporation is not the determining factor.
    *   *Why B is incorrect:* U.S. federal privacy law does not preempt international obligations. The company is subject to both U.S. applicable law and GDPR for its EU customer data.
    *   *Why D is incorrect:* GDPR compliance follows the data subject, not the server location. Processing EU resident data on U.S. infrastructure is still subject to GDPR and requires appropriate data transfer mechanisms (such as Standard Contractual Clauses).

---

**Question 4**
An organization follows the principle of least privilege for database access. An analyst in the marketing department needs to compute average order values by region for a campaign report. Which access configuration best follows this principle?
*   A) Grant the analyst full administrative access to the database so they can query any table they need without requesting help from IT.
*   B) Grant the analyst SELECT permission on the orders table and the regions lookup table only, scoped to the columns required for the report.
*   C) Create a shared "analytics" login used by all analysts in the department, giving it read access to all tables in the database.
*   D) Give the analyst a copy of the full production database exported to their laptop so they can work without requesting database access.
*   **Correct Answer:** B) Grant the analyst SELECT permission on the orders table and the regions lookup table only, scoped to the columns required for the report.
*   **Distractor Analysis:**
    *   *Why B is correct:* The principle of least privilege requires granting only the minimum permissions necessary to perform the specific task. This means read-only (SELECT) access, limited to the specific tables and columns needed — no more.
    *   *Why A is incorrect:* Full administrative access vastly exceeds what is needed for a read-only reporting task. Administrative privileges allow modifying or deleting production data, which creates unnecessary risk.
    *   *Why C is incorrect:* A shared login violates accountability — it cannot be audited to determine which individual ran a query or accessed sensitive data. It also provides broader access than any single analyst needs.
    *   *Why D is incorrect:* Exporting a full production database to a personal laptop introduces significant data governance and security risks — the data is outside organizational security controls, unencrypted, and could expose PII from unrelated business functions.

---

**Question 5**
A data engineer applies a transformation that replaces each customer's real name and email with a randomly generated code (e.g., Customer_A8F3), storing the mapping between the code and the real identity in a separate, encrypted key table accessible only to the data privacy officer. Which privacy technique is being used, and is this data still subject to GDPR?
*   A) Anonymization — the real identities are stored separately, so the dataset itself is no longer personal data and is exempt from GDPR.
*   B) Pseudonymization — the transformation is reversible using the key table, so the data is still considered personal data under GDPR and remains subject to its requirements.
*   C) Data masking — the values are replaced with formatted placeholders, which constitutes full anonymization under GDPR.
*   D) Encryption — the data is encoded and can only be read with the decryption key, which classifies it as anonymous under GDPR once the key is secured.
*   **Correct Answer:** B) Pseudonymization — the transformation is reversible using the key table, so the data is still considered personal data under GDPR and remains subject to its requirements.
*   **Distractor Analysis:**
    *   *Why B is correct:* Pseudonymization replaces identifiers with codes while storing the re-identification mapping separately. GDPR explicitly defines pseudonymized data as still personal data because re-identification is possible by anyone with access to the key. It is a useful risk-reduction measure but does not remove GDPR obligations.
    *   *Why A is incorrect:* The existence of the key table means re-identification is possible — therefore this is not anonymization. True anonymization requires that no party, including the organization, can re-identify the individual. The key table here preserves that possibility.
    *   *Why C is incorrect:* Data masking replaces values with non-recoverable fictional substitutes for use in non-production environments. The scenario describes a reversible transformation with a stored key — that is pseudonymization, not masking.
    *   *Why D is incorrect:* Encryption encodes data for confidentiality but the organization retains the decryption key. Encrypted personal data is still personal data under GDPR. Holding the key means the organization can still access the original values.
