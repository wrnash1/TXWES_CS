# Quiz: Module 12 - Software Testing and Quality Assurance
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

**Question 1**
A development team has fixed a high-priority bug in the payment processing module. Before releasing the fix to production, the QA team re-runs all previously passing test cases across the entire application to ensure nothing was broken by the change. What type of testing is this?
*   A) User Acceptance Testing (UAT)
*   B) Unit Testing
*   C) Regression Testing
*   D) Integration Testing
*   **Correct Answer:** C) Regression Testing
*   **Distractor Analysis:**
    *   *Why A is incorrect:* UAT involves business users testing the system against real business scenarios to accept the release; it does not describe re-running a full existing test suite.
    *   *Why B is incorrect:* Unit testing tests individual components in isolation; re-running the full test suite across the application is not unit testing.
    *   *Why D is incorrect:* Integration testing verifies that components work correctly when combined; re-running previously passed tests after a change is specifically regression testing.
    *   *Why C is correct:* Regression testing is the practice of re-executing a previously validated test suite after any change to ensure that existing, working functionality has not been inadvertently broken by the modification.

---

**Question 2**
In the context of software testing, which of the following is the most accurate definition of **User Acceptance Testing (UAT)**?
*   A) Testing performed by individual developers to verify that each code module produces the correct output for a specific input
*   B) Automated testing that runs after every code commit to detect failures in any previously working functionality
*   C) Testing conducted by business users and stakeholders using realistic scenarios to verify the system meets requirements and is fit for their use before deployment
*   D) Testing of the data migration scripts to ensure legacy data is correctly transformed and loaded into the new system schema
*   **Correct Answer:** C) Testing conducted by business users and stakeholders using realistic scenarios to verify the system meets requirements and is fit for their use before deployment
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Developer testing of individual modules describes unit testing, not UAT.
    *   *Why B is incorrect:* Automated post-commit testing to catch broken functionality describes automated regression testing (e.g., CI/CD pipeline tests), not UAT.
    *   *Why D is incorrect:* Testing data migration scripts is a specific technical activity, not UAT; UAT focuses on business process validation, not data transformation verification.
    *   *Why C is correct:* UAT is the business-owned testing phase where actual users test the system using real business scenarios to confirm it meets their needs and the agreed requirements before formal sign-off and production deployment.

---

**Question 3**
During UAT for a new accounts payable system, a business user reports: "When I try to process an invoice over $50,000, the system shows an error and won't let me submit it." The requirements document specifies: "Invoices over $50,000 require dual approval before submission." The system is enforcing this rule and requesting a second approver. Is this a defect or a change request?
*   A) Defect — the system is preventing submission, which means it is broken
*   B) Change request — the user wants to bypass the dual approval rule, which is not in the current requirements
*   C) Defect — the error message should explain the dual approval requirement more clearly
*   D) Change request — dual approval is a new requirement that was not in the original requirements document
*   **Correct Answer:** B) Change request — the user wants to bypass the dual approval rule, which is not in the current requirements
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The system is working exactly as the requirements specify; there is no defect. The user's expectation conflicts with the documented requirement.
    *   *Why C is incorrect:* While improving the error message clarity may be a valid usability enhancement, the core issue is that the user wants to bypass a requirement — that is a change request, not a defect. Error message quality would be a separate, lower-priority item.
    *   *Why D is incorrect:* Dual approval for large invoices is in the requirements document as specified in the scenario; it is not a new requirement.
    *   *Why B is correct:* A defect is a variance between actual system behavior and documented requirements. Since the system is correctly implementing the dual approval requirement, the user's desire to process without dual approval is a new business request — a change request — not a system defect.

---

**Question 4**
A BA is writing acceptance test cases for the requirement: "The system shall send an email notification to the order owner within 5 minutes when an order status changes to Shipped." Which of the following test cases is most effective?
*   A) Verify that the Notifications module loads without errors when the system starts up
*   B) Given an order in "Processing" status, when the status is changed to "Shipped," then an email notification is sent to the order owner within 5 minutes
*   C) Confirm that the email server configuration is correct and all SMTP settings are properly configured
*   D) Verify that the order status dropdown includes "Shipped" as a valid option in the user interface
*   **Correct Answer:** B) Given an order in "Processing" status, when the status is changed to "Shipped," then an email notification is sent to the order owner within 5 minutes
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Testing that the Notifications module loads without errors verifies general system stability, not the specific requirement about shipped order notifications.
    *   *Why C is incorrect:* Verifying SMTP settings is a technical infrastructure test, not a business acceptance test case; it does not confirm the requirement from the user's perspective.
    *   *Why D is incorrect:* Confirming the dropdown includes "Shipped" tests a prerequisite UI element but does not test the actual requirement — the notification behavior triggered by the status change.
    *   *Why B is correct:* This test case directly tests the requirement using the Given/When/Then format with a specific, measurable expected result (notification sent within 5 minutes). It is traceable to the requirement and produces a clear pass/fail outcome.

---

**Question 5**
An organization is building a new ERP system. During which testing phase should the BA most actively participate to ensure the system meets business requirements before go-live?
*   A) Unit testing — to verify that each developer's code module performs its individual functions correctly
*   B) Performance testing — to confirm the system meets the required response time under maximum user load
*   C) User Acceptance Testing (UAT) — to facilitate business users testing real scenarios, manage defects, and obtain formal sign-off
*   D) Smoke testing — to confirm after each deployment that the basic system functions are operational
*   **Correct Answer:** C) User Acceptance Testing (UAT) — to facilitate business users testing real scenarios, manage defects, and obtain formal sign-off
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Unit testing is developer-owned; while BAs define what the code should do, they do not actively participate in running unit tests.
    *   *Why B is incorrect:* Performance testing is typically owned by the QA or performance engineering team; BAs define performance requirements but do not typically execute performance tests.
    *   *Why D is incorrect:* Smoke testing is a brief post-deployment sanity check that basic functions work; it is a technical QA activity, not a BA-led business validation phase.
    *   *Why C is correct:* BABOK® Guide v3 assigns UAT coordination as a BA responsibility. The BA facilitates business user test sessions, manages the defect vs. change request classification, and ensures formal acceptance sign-off is obtained before deployment — making UAT the testing phase where BA participation is most critical.
