# Quiz: Module 10 - User Interface and UX Design Principles
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

**Question 1**
A user is uploading a large file to a web application. After clicking "Upload," the page appears frozen with no feedback for 45 seconds. The user cannot tell if the upload is processing, has failed, or is waiting for input. Which of Nielsen's 10 usability heuristics does this violate?
*   A) Error prevention — the system should prevent users from uploading files that are too large
*   B) Visibility of system status — the system should keep users informed of what it is doing through appropriate feedback
*   C) User control and freedom — the system should provide an undo option to cancel the upload
*   D) Consistency and standards — the system should follow platform conventions for upload interactions
*   **Correct Answer:** B) Visibility of system status — the system should keep users informed of what it is doing through appropriate feedback
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Error prevention addresses designing to prevent mistakes before they happen; the issue here is lack of feedback during a valid in-progress operation.
    *   *Why C is incorrect:* User control and freedom addresses the ability to undo or exit; the problem is not a lack of cancel option but a lack of any progress indication.
    *   *Why D is incorrect:* Consistency and standards concerns using recognized UI conventions; the problem here is specifically the absence of status feedback, not a convention violation.
    *   *Why B is correct:* "Visibility of system status" requires the system to always keep users informed about what is happening with appropriate feedback within reasonable time. A frozen page with no progress indicator during a 45-second operation is a direct violation of this heuristic.

---

**Question 2**
In the context of UI/UX design, which of the following is the most accurate definition of a **wireframe**?
*   A) A fully interactive, high-fidelity simulation of the final interface with real data, production styling, and clickable navigation flows
*   B) A low-fidelity structural diagram showing the layout and placement of UI components without color, graphics, or final styling
*   C) A written document listing all the screens in a system with their intended functions and the user tasks they support
*   D) A formal specification of all API endpoints and data contracts between the front-end interface and the back-end services
*   **Correct Answer:** B) A low-fidelity structural diagram showing the layout and placement of UI components without color, graphics, or final styling
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a high-fidelity prototype, not a wireframe. Wireframes are deliberately stripped of final styling to focus communication on structure and layout.
    *   *Why C is incorrect:* A written list of screens with descriptions is a screen inventory or navigation map, not a wireframe.
    *   *Why D is incorrect:* API endpoint specifications are technical interface design documents; they have nothing to do with visual wireframes.
    *   *Why B is correct:* A wireframe is a low-fidelity, grayscale or sketch-level representation that communicates page structure, element placement, and content hierarchy without the distraction of colors or branding — ideal for early stakeholder feedback.

---

**Question 3**
A government agency is building a new citizen-facing web portal. Their legal team confirms the portal must comply with WCAG 2.1 AA accessibility standards. The development team asks the BA what "AA compliance" means in practical terms. Which answer is most accurate?
*   A) The portal must have a contrast ratio of at least 4.5:1 for normal text, keyboard navigability for all functionality, and properly labeled form fields, among other criteria
*   B) The portal must be compatible with all major browsers (Chrome, Firefox, Safari, Edge) and mobile devices
*   C) The portal must load in under 2 seconds on a 4G mobile connection and pass Google's Core Web Vitals performance benchmarks
*   D) The portal must be available 99.9% of the time and have a documented disaster recovery plan tested annually
*   **Correct Answer:** A) The portal must have a contrast ratio of at least 4.5:1 for normal text, keyboard navigability for all functionality, and properly labeled form fields, among other criteria
*   **Distractor Analysis:**
    *   *Why B is incorrect:* Browser and device compatibility is cross-browser testing, not an accessibility standard. WCAG does not specify browser compatibility.
    *   *Why C is incorrect:* Load time and Core Web Vitals are performance (non-functional) requirements, not WCAG accessibility requirements.
    *   *Why D is incorrect:* Availability and disaster recovery are reliability/availability non-functional requirements, not accessibility standards.
    *   *Why A is correct:* WCAG 2.1 AA includes specific criteria such as minimum contrast ratios (4.5:1 for body text), full keyboard operability, text alternatives for non-text content, and accessible form labels — these are the practical implementation requirements of the "Perceivable" and "Operable" POUR principles at AA level.

---

**Question 4**
A BA is working with the UX team on a new customer portal. The UX designer has created a clickable mockup with final branding, real representative data, and working navigation between screens. A group of representative customers will test it before development begins. What type of design artifact is the UX designer using?
*   A) Wireframe — because it represents the interface before the final system is built
*   B) Context diagram — because it shows all the actors who interact with the portal system
*   C) High-fidelity prototype — because it closely resembles the final product and supports realistic user interaction
*   D) System architecture diagram — because it shows the complete structure of the portal from the user's perspective
*   **Correct Answer:** C) High-fidelity prototype — because it closely resembles the final product and supports realistic user interaction
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A wireframe is low-fidelity and lacks final branding, colors, and real data. The artifact described has all of these, making it a prototype, not a wireframe.
    *   *Why B is incorrect:* A context diagram is a DFD artifact showing the system boundary and external entities; it is not a UI design tool.
    *   *Why D is incorrect:* A system architecture diagram shows technical components and their interactions; it is not a UI design artifact for user testing.
    *   *Why C is correct:* A high-fidelity prototype closely replicates the final product's appearance and interaction patterns, enabling realistic usability testing with representative users — exactly what is described.

---

**Question 5**
During a usability review of a new inventory management system, a BA observes that experienced warehouse workers must memorize a 12-character item code to look up any product — the system provides no search or autocomplete feature. Which Nielsen usability heuristic does this violate?
*   A) Aesthetic and minimalist design — unnecessary data fields should be removed from the interface
*   B) Help users recognize, diagnose, and recover from errors — error messages should describe the mistake clearly
*   C) Recognition rather than recall — users should not have to memorize information; it should be made visible or easily retrievable
*   D) Flexibility and efficiency of use — accelerators should allow expert users to complete tasks more quickly
*   **Correct Answer:** C) Recognition rather than recall — users should not have to memorize information; it should be made visible or easily retrievable
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Aesthetic and minimalist design concerns removing irrelevant information from the interface; the problem here is the burden of memorization, not excessive screen clutter.
    *   *Why B is incorrect:* This heuristic addresses how the system communicates after an error occurs; the problem here is a design burden before any error, not error message quality.
    *   *Why D is incorrect:* Flexibility and efficiency of use concerns providing shortcuts for expert users; the issue here is the fundamental UX problem of requiring users to carry information in working memory rather than providing recognition-based lookup.
    *   *Why C is correct:* "Recognition rather than recall" directly addresses the design principle that systems should present available options and information rather than requiring users to memorize codes, commands, or sequences. An item search/autocomplete feature would correct this violation.
