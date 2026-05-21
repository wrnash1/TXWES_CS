# Reading Guide: Module 02 – IAM: Roles, Policies, and Service Accounts
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 02 – IAM: Roles, Policies, and Service Accounts**! Identity and Access Management (IAM) is the single most tested domain on the Google Cloud ACE exam. This module teaches you how GCP controls *who* can do *what* on *which* resource. You will learn the difference between primitive, predefined, and custom roles; how policy bindings work; and how Service Accounts enable machine-to-machine authentication. Mastering IAM is prerequisite knowledge for every subsequent module.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Principal (Member)**: The identity to whom a role is granted. Principals include Google Accounts (users), Service Accounts, Google Groups, Google Workspace domains, and the special identifiers `allUsers` (public internet) and `allAuthenticatedUsers` (any Google-authenticated identity).

*   **Role**: A named collection of permissions. You never grant individual permissions directly — you grant roles. GCP has three role categories: **Primitive** (Owner/Editor/Viewer — overly broad, avoid in production), **Predefined** (curated per-service roles like `roles/storage.objectAdmin`), and **Custom** (user-defined combinations of granular permissions for least-privilege enforcement).

*   **IAM Policy**: A policy is a list of bindings that attaches one or more principals to a role on a specific resource. Policies are set on resources (projects, buckets, VMs) using `setIamPolicy`. IAM policies are additive — you can only grant access, not explicitly deny it (except via deny policies, a newer advanced feature).

*   **Service Account**: A special Google Account intended for use by applications and VMs rather than humans. A Compute Engine VM can be assigned a Service Account so that code running on the VM can call GCP APIs without embedding user credentials. Service Accounts are also principals — you can grant them roles just like users.

*   **Least Privilege**: The security principle that every principal should have only the minimum permissions required to perform their job function, and nothing more. The ACE exam consistently favors predefined roles over primitive roles, and custom roles when no predefined role is a precise fit.

*   **Policy Inheritance**: IAM policies set at the Organization or Folder level automatically apply to all child Folders, Projects, and resources. Effective permissions on a resource are the *union* of all policies from the resource up to the Organization root — you cannot subtract a permission granted at a higher level.

---

### 2. Certification Exam Tips

*   **Never use Owner or Editor in production**: The ACE exam treats primitive roles as incorrect answers when the question asks for *least privilege*. Always identify the most specific predefined role that grants only the needed permissions.

*   **Service Accounts for VMs, not user keys**: When a VM needs to call a GCP API, the correct answer is to assign a Service Account to the VM instance — not to generate and embed a user's API key. Embedded keys are a security anti-pattern that the exam specifically tests.

*   **`gcloud iam` command family**: Know `gcloud iam roles list`, `gcloud iam roles describe ROLE_ID`, `gcloud projects add-iam-policy-binding PROJECT --member=... --role=...`, and `gcloud projects get-iam-policy PROJECT`. The Console does the same things visually, but the CLI is often tested.

*   **Condition-based IAM (IAM Conditions)**: The ACE exam occasionally tests IAM Conditions, which allow you to grant a role only when specific attributes are true (e.g., only during business hours, only for resources with a specific tag). Know that conditions are added to policy bindings, not to roles themselves.

*   **Study Resource**: The freeCodeCamp ACE course covers IAM roles, policies, and service accounts with worked examples: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Supplement with the official IAM overview documentation for precise terminology.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Read the IAM overview documentation, which defines principals, roles, policies, and the policy hierarchy: [Google Cloud IAM Overview](https://cloud.google.com/iam/docs/overview). Pay close attention to the "Policy inheritance" section.
*   **Required Reading**: Review predefined roles and how to choose the right role for common scenarios: [Understanding IAM Roles](https://cloud.google.com/iam/docs/understanding-roles). The ACE exam draws heavily from the predefined roles table.
*   **Required Video**: Watch the IAM segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the IAM chapter using the video's table of contents.

---

### Lab & Command Integration
In this module's lab, you will create IAM bindings, inspect policies, and configure a Service Account on a Compute Engine VM. Key commands to practice:

*   `gcloud projects get-iam-policy PROJECT_ID` — retrieves the full IAM policy for a project
*   `gcloud projects add-iam-policy-binding PROJECT_ID --member=user:EMAIL --role=roles/viewer` — grants a role to a user
*   `gcloud iam service-accounts create SA_NAME --display-name "Description"` — creates a Service Account
*   `gcloud compute instances create VM_NAME --service-account=SA_EMAIL --scopes=cloud-platform` — attaches a Service Account to a new VM

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Google Cloud IAM Overview](https://cloud.google.com/iam/docs/overview) documentation page.
- [ ] Read the [Understanding IAM Roles](https://cloud.google.com/iam/docs/understanding-roles) documentation page.
- [ ] Watch the IAM segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create bindings, inspect policies, configure a Service Account on a VM.
- [ ] Proceed to the weekly quiz.
