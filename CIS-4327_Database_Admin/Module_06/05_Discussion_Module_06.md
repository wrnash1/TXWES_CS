# Discussion Forum: Module 06 — Firestore and Datastore: Document Databases

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

---

### Overview

This discussion connects Firestore's document model, security configuration, and service selection criteria to real-world design decisions. Read all three scenarios and post your initial response to the one that best matches your background. Reply to at least two classmates.

---

### Scenario A — Ride-Share App Backend Design

A new ride-share startup is designing their application backend. The engineering team has sketched a data model with three main entities: drivers (with profile, vehicle info, ratings), riders (with profile, payment methods, ride history), and trips (with route, fare, timestamps, driver and rider references). A junior engineer proposes Cloud SQL for PostgreSQL because the relationships between entities feel relational. The senior engineer argues that Firestore would be more appropriate given the client platforms (iOS, Android, web dashboard) and the requirement that riders see live trip status updates.

For your initial post, address all of the following.

Evaluate the junior engineer's relational argument: which aspects of the ride-share data model actually benefit from relational design, and which aspects are better served by a document model? Explain which Firestore Native mode feature directly addresses the live trip status requirement and how it works architecturally. Design the top-level Firestore collection structure for this application — list at least four collections and explain what documents each contains. Identify one operational challenge the team would face if they chose Firestore and later needed to run complex analytics across all trips. Your post should be 175–225 words using correct Firestore terminology.

---

### Scenario B — Security Rules for a Healthcare Platform

A healthcare startup stores patient health records in Firestore. Each patient document contains personal health information (PHI) protected by HIPAA regulations. The application has three user roles: patients (who can read only their own record), care providers (who can read and update records for patients in their assigned panel), and administrators (who can read all records but cannot modify clinical data fields).

For your initial post, address all of the following.

Explain why Firestore Security Rules — rather than application-layer authorization — are the appropriate access control mechanism for a direct-client-to-Firestore architecture. Describe how the Security Rules would use `request.auth` fields to distinguish between the three user roles (assume the role is stored as a custom claim in the Firebase Authentication token). Identify one limitation of Firestore Security Rules that is particularly relevant for a healthcare compliance context (e.g., audit logging, complex role hierarchies) and describe how it would be addressed. Describe what `request.resource.data` is used for in Security Rules and give a concrete example of a clinical data field that administrators should not be able to modify. Your post should be 175–225 words using correct Firestore Security Rules terminology.

---

### Scenario C — Migrating from Cloud Datastore to Firestore

A government agency runs a case management system on Cloud Datastore that has been in production for seven years. The system has 40 million entities across 15 kinds. The IT director wants to migrate to Firestore Native mode to use real-time updates for a new field agent mobile app. A consultant warns that the migration is irreversible and requires careful planning.

For your initial post, address all of the following.

Explain why the migration from Datastore mode to Firestore Native mode is irreversible — what happens to the database after the migration that cannot be undone? Describe two specific risks the agency must evaluate before executing the migration, focusing on Datastore features or behaviors that may not have exact equivalents in Native mode. Identify which entity group consistency patterns in Datastore would need to be redesigned as Firestore Native mode transactions, and explain the structural difference. Recommend a testing strategy the agency should follow before migrating production data, describing at least one validation step. Your post should be 175–225 words using correct terminology from Module 06.

---

### Peer Response Guidelines

Reply to at least two classmates across any scenario. Each reply must be at least 50 words and add technical value — a design alternative, a security consideration they missed, a specific Firestore behavior relevant to their scenario, or a substantive follow-up question.

---

### Discussion Rubric — 10 Points Total

Initial post — 6 points.

- 5 to 6 points: Addresses all required elements with technical accuracy, correct Firestore terminology, and clear reasoning. Meets the 175–225 word count.
- 3 to 4 points: Addresses most elements but omits one required item or uses imprecise terminology.
- 0 to 2 points: Initial post is missing, substantially incomplete, or contains significant factual errors.

Peer responses — 4 points.

- 4 points: Two substantive replies of at least 50 words each that contribute technical content.
- 2 points: Only one qualifying reply, or both replies are superficial.
- 0 points: No peer responses by the deadline.

---

### Due Dates

Initial post: Wednesday at 11:59 PM

Peer responses: Sunday at 11:59 PM

Professor Nash reads every post. Posts that apply Security Rules concepts from the lab to the discussion scenarios will be recognized in class.

---

Reference: cloud.google.com/learn
