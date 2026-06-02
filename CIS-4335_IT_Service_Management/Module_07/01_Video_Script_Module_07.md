# Video Script: Module 07 — Service Management Practices: Change Enablement

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 20–24 minutes
**Certification Alignment:** ITIL 4 Foundation

---

## Section 1: Introduction (approximately 2 minutes)

Welcome back to CIS-4335. I am Professor Nash, and this is Module 07: Change Enablement.

If you have ever seen an IT team bring down a production system on a Friday afternoon trying to apply a routine patch, you already understand why Change Enablement exists. Change is one of the most common sources of service disruption in IT — and it is also one of the most necessary activities. Systems need patches. Configurations need updating. New features need deploying. The question is never whether to change. The question is how to change safely.

This module covers one of the most heavily tested topics on the ITIL 4 Foundation exam. Change Enablement is almost certain to appear in multiple exam questions. By the end of this session, you will know the purpose of the practice, the three types of changes, the role of the Change Advisory Board, and how Change Enablement connects to Deployment Management and Release Management.

Let us get started.

---

## Section 2: What Is Change Enablement? (approximately 3 minutes)

ITIL 4 defines the purpose of Change Enablement as maximizing the number of successful IT and service changes by ensuring that risks are properly assessed, authorizing changes to proceed, and managing the change schedule.

There are three key ideas in that definition. First: maximize successful changes. Not minimize changes. Not eliminate risk. Maximize success. ITIL 4 is not trying to stop organizations from changing — it is trying to help them change safely and effectively.

Second: risks are properly assessed. Every change carries some risk. Even a simple password reset carries a small risk of error. Change Enablement requires that those risks be understood before the change is authorized. The level of risk determines what kind of assessment is needed.

Third: manage the change schedule. Not all changes can happen at the same time without conflict. A change schedule coordinates when changes will occur, who is responsible, and how they relate to other changes already planned.

[SHOW DIAGRAM]

Let me also address terminology. In ITIL v3, this practice was called Change Management. In ITIL 4, the name changed to Change Enablement. The shift in language is intentional — ITIL 4 frames the practice as enabling change rather than managing (or gatekeeping) it. The word "enablement" signals that the practice is designed to support successful change, not block it.

---

## Section 3: What Is a Change? (approximately 2 minutes)

Before we go further, let us be precise about what ITIL 4 means by a change.

A change is the addition, modification, or removal of anything that could have a direct or indirect effect on services.

Notice how broad that definition is. A change is not just a code deployment or a server upgrade. It includes changes to configurations, to network settings, to documentation, to processes — anything that could affect a service directly or indirectly.

This breadth matters because it means Change Enablement must be applied broadly. A configuration change to a firewall rule can take down a service just as effectively as a botched software deployment. Both require assessment before implementation.

---

## Section 4: The Three Types of Changes (approximately 5 minutes)

ITIL 4 identifies three types of changes. This is the most heavily tested area of Change Enablement on the exam, so pay close attention.

### Standard Changes

A standard change is a pre-authorized, low-risk, well-understood change that follows a documented procedure. Because the risk and the steps have already been assessed and formally approved, standard changes do not require individual authorization each time they are performed.

Examples of standard changes: adding a new user account, resetting a password, applying a tested security patch from a pre-approved patch list, upgrading a browser to the current supported version.

The key characteristic is pre-authorization. Someone — the appropriate change authority — has already reviewed the risk and the procedure and said: whenever this situation arises, you may proceed with this documented approach without coming back to us for individual approval. Standard changes are handled efficiently precisely because the hard work of assessment was done upfront, once, when the change type was established.

### Normal Changes

A normal change is any change that requires individual assessment and authorization before implementation. Normal changes have not been pre-authorized as a class. Each one must be reviewed on its own merits — scope, risk, timing, potential impact.

The appropriate change authority for a normal change depends on the level of risk and impact. A low-risk, low-impact normal change might be authorized by a single IT manager. A high-risk, high-impact change — such as upgrading a core banking system or migrating a hospital's electronic health record platform — might require review by the Change Advisory Board and authorization by senior IT leadership.

Normal changes are the largest category in most organizations. Not every change is low-risk enough to pre-authorize, and not every change is an emergency.

### Emergency Changes

An emergency change is a change that must be implemented as quickly as possible to resolve a major incident or prevent a critical service failure. The urgency is driven by a real and immediate risk to service continuity or security.

The classic examples: a zero-day vulnerability is actively being exploited; a production database is corrupted and a configuration rollback is needed immediately; a network outage requires an emergency routing change.

Emergency changes still require authorization. ITIL 4 is clear on this point. The process is expedited — often through an Emergency Change Advisory Board or a single senior authority with the power to authorize quickly — but authorization is not skipped. After implementation, the emergency change must be fully documented and reviewed.

[SHOW DIAGRAM]

Let me put these three types side by side so the distinctions are clear.

Standard changes: pre-authorized, low risk, well understood, documented procedure, no individual review required.

Normal changes: individual assessment required, authorization by appropriate authority, level of review depends on risk and impact.

Emergency changes: immediate need, expedited authorization, still authorized before or as close to implementation as possible, full documentation after.

The exam will test whether you can read a scenario and correctly identify which type applies. The signal words are: pre-authorized or routine for standard; requires individual assessment for normal; major incident or critical failure for emergency.

---

## Section 5: The Change Advisory Board (approximately 3 minutes)

The Change Advisory Board — commonly called the CAB — is a group that provides advisory support to the change authority by reviewing and making recommendations on high-risk or high-impact normal changes.

I want to underline the word advisory. The CAB does not authorize changes. It advises the change authority. The change authority is the individual or group with the actual power to approve or reject the change. The CAB brings expertise and perspective to help that authority make a well-informed decision.

This distinction shows up on the ITIL 4 Foundation exam with some regularity. If a question says the CAB authorizes changes, that answer is wrong. The CAB advises. The change authority authorizes.

Who sits on a CAB? Membership depends on the change being reviewed. For a major infrastructure change, the CAB might include IT infrastructure leads, security staff, the service owner, and a business representative. For a change to a customer-facing application, the CAB might include application owners, the service desk manager, and a customer relationship manager. The CAB is not a fixed standing committee with permanent membership — it is composed of whoever has relevant expertise for the change at hand.

For emergency changes, the regular CAB process is too slow. Many organizations maintain an Emergency CAB — a smaller, on-call group of senior decision-makers who can be convened quickly to authorize emergency changes.

---

## Section 6: The Change Schedule (approximately 2 minutes)

The change schedule is a document that lists all authorized changes and their planned implementation dates. Its purpose is to coordinate changes across the organization, minimize conflicts, and communicate to stakeholders when changes are coming.

Without a change schedule, two teams might independently schedule changes that affect the same system at the same time. Or a high-risk change might be scheduled during a peak business period with no awareness that the business unit has a major customer event that day.

The change schedule serves several purposes: it helps the CAB and change authority identify conflicts before they become incidents; it allows the service desk to anticipate upcoming changes and prepare for potential calls; it communicates planned maintenance to affected users; and it provides a record for post-change review.

In some organizations the change schedule is called the forward schedule of changes (FSC) — you may see this term, especially in contexts that reference ITIL v3.

---

## Section 7: Change Enablement and Other Practices (approximately 3 minutes)

Change Enablement does not operate in isolation. It connects directly to several other ITIL 4 practices, and the exam tests your ability to distinguish them.

### Change Enablement vs. Deployment Management

This is the most commonly tested relationship. Change Enablement assesses and authorizes the change. Deployment Management physically moves the change into the live environment.

Think of it this way: Change Enablement is the governance layer. Deployment Management is the execution layer. Change Enablement answers the question: should this change happen, and when? Deployment Management answers the question: how do we actually put it in place?

A change can be authorized by Change Enablement and then handed to Deployment Management for execution. These are two separate activities handled by two separate practices.

### Change Enablement vs. Release Management

Release Management plans and schedules the deployment of new or changed services. It groups changes into releases and manages the sequencing of what goes out when. Change Enablement authorizes the individual changes that make up those releases. They work together: Release Management structures the delivery; Change Enablement governs the risk.

### Change Enablement and Service Configuration Management

Change Enablement depends on knowing the current state of the environment when assessing risk. Service Configuration Management maintains a record of configuration items — the components that make up services — and their relationships. If the configuration data is accurate, Change Enablement can make better-informed risk assessments. If the data is stale or incomplete, risk assessments may miss important dependencies.

[SHOW DIAGRAM]

---

## Section 8: Applying Guiding Principles to Change Enablement (approximately 2 minutes)

Let us connect Change Enablement to the Guiding Principles.

Focus on Value: Every change should ultimately trace back to a business need or a service improvement. Change for the sake of change adds risk without benefit. The change authority should ask: what value does this change deliver?

Progress Iteratively with Feedback: Large, sweeping changes carry higher risk than incremental ones. Where possible, changes should be decomposed into smaller, lower-risk increments. Each increment can be assessed, implemented, and reviewed before the next proceeds.

Keep It Simple and Practical: Change Enablement processes should be proportionate to risk. A heavyweight approval process for a standard password reset adds bureaucracy without adding safety. A light-touch process for a major infrastructure change fails to manage real risk. Match the process to the level of risk.

Optimize and Automate: Many standard changes can be automated. Automated standard changes reduce the risk of human error, increase consistency, and free up human attention for higher-risk decisions.

---

## Section 9: Common Exam Scenarios (approximately 2 minutes)

Let me walk through the scenario patterns you will see on the exam.

Scenario pattern one: you are given a description of a change and asked to classify it as standard, normal, or emergency. Apply the criteria we covered. Pre-authorized routine activity equals standard. Requires individual risk assessment equals normal. Active incident or critical failure driving urgency equals emergency.

Scenario pattern two: you are given a situation involving the CAB and asked whether the CAB should approve or authorize. The CAB advises. It never authorizes. If the answer choice says the CAB approves the change, that answer is wrong.

Scenario pattern three: a scenario describes an activity — such as physically rolling out new software to desktops — and asks whether that is Change Enablement or Deployment Management. If the scenario is about authorizing or assessing, it is Change Enablement. If it is about executing the physical or technical move into production, it is Deployment Management.

Scenario pattern four: an emergency patch is needed immediately. The question asks what should happen. The answer is: classify as emergency change, obtain expedited authorization (ECAB or senior authority), implement, then document and review. You do not skip authorization. You do not wait for the regular CAB cycle. You do not implement first and document later without obtaining any authorization.

---

## Section 10: Module Summary (approximately 1 minute)

Let me summarize what we covered today.

Change Enablement's purpose is to maximize successful changes through risk assessment, authorization, and schedule management.

A change is the addition, modification, or removal of anything that could directly or indirectly affect services.

There are three types of changes: standard (pre-authorized, low-risk), normal (individual assessment required), and emergency (expedited authorization for critical situations).

The CAB is an advisory body — it provides recommendations to the change authority, which holds the actual authorization power.

The change schedule coordinates authorized changes to prevent conflicts and communicate to stakeholders.

Change Enablement authorizes; Deployment Management executes.

Complete the reading guide, then work through the lab. The lab will ask you to classify a set of proposed changes, draft a change record for a normal change, and analyze which scenarios require CAB involvement. These are exactly the kinds of analysis the ITIL 4 Foundation exam expects you to perform.

See you in the discussion forum.

---

End of Module 07 Video Script
