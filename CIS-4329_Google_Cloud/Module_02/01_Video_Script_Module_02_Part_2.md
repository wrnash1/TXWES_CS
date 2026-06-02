# Video Script — Module 02, Part 2

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: IAM — Service Accounts, Conditions, and gcloud Commands

### Estimated Duration: 11–13 minutes

---

## Introduction to Part 2

Welcome back to Module 02. In Part 1 we covered the IAM model — principals, the three categories of roles, and the structure of IAM policies. In Part 2 we are going to focus on service accounts, which are one of the most important and most tested topics on the ACE exam. We will also cover IAM conditions, audit logging, and the gcloud commands you need for the lab.

---

## Section 1: Service Accounts in Depth

**[SHOW SLIDE: Service account lifecycle diagram — Create, Attach to VM, Use key or metadata server, Audit]**

A service account is a special Google identity intended to represent an application or workload, not a human user. When your code running on a Compute Engine VM needs to call the Cloud Storage API, it should not use a human user's credentials. It should authenticate as a service account.

Service accounts serve a dual role in GCP IAM:

- They are a principal — you can grant roles TO a service account, just like a user
- They are a resource — you can control WHO can use (impersonate) a service account

### Types of Service Accounts

**[SHOW SLIDE: Three columns — User-Managed, Default, Google-Managed]**

There are three types:

User-managed service accounts are ones you create explicitly. Their email format is `SA-NAME@PROJECT-ID.iam.gserviceaccount.com`. You have full control over their lifecycle, keys, and IAM bindings.

Default service accounts are created automatically when you enable certain APIs. The most important one is the Compute Engine default service account: `PROJECT-NUMBER-compute@developer.gserviceaccount.com`. By default, this service account is granted `roles/editor` on the project — which is overly broad and a security concern. Best practice is to disable the default service account and create purpose-built user-managed service accounts instead.

Google-managed service accounts are created by Google to run internal GCP infrastructure services. You generally do not interact with these directly.

### Attaching a Service Account to a VM

**[SHOW CONSOLE: Compute Engine > VM Instances > Create instance > Identity and API access section]**

When you create a Compute Engine VM, you can specify a service account in the "Identity and API access" section. The VM then automatically authenticates as that service account for all GCP API calls made from within the VM. Code running on the VM can retrieve credentials from the instance metadata server at the URL `http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token` without any hardcoded keys.

**[PAUSE — Professor on camera]**

This metadata-server-based authentication is the correct pattern. It is more secure than embedding a key file because there is no key to steal — the credentials are short-lived tokens that the metadata server rotates automatically. The ACE exam will test this pattern repeatedly: when a VM needs to call a GCP API, the answer is always "attach a service account to the VM," not "generate a service account key and put it on the VM."

### Service Account Keys

Service account keys are long-lived JSON credential files that you can download from the Console or generate via gcloud. They allow code anywhere — not just on GCP — to authenticate as a service account.

Keys are a necessary evil in some scenarios: code running outside of GCP (on-premises servers, third-party CI/CD pipelines) sometimes needs them. But they carry significant risk: if a key file is accidentally committed to a public Git repository or stolen from a server, an attacker gains persistent access to your GCP environment until the key is manually rotated.

Best practices for service account keys:

- Do not create keys unless you genuinely cannot use workload identity federation or VM-attached service accounts
- Rotate keys regularly (every 90 days maximum)
- Apply the Organization Policy constraint `constraints/iam.disableServiceAccountKeyCreation` to prevent key creation in projects that do not need it
- Use Secret Manager to store keys if they must exist

---

## Section 2: The serviceAccountUser Role

**[SHOW SLIDE: Diagram showing a developer with serviceAccountUser role being able to attach a service account to a VM]**

There are two important IAM roles related to service account usage:

`roles/iam.serviceAccountUser` — This role grants the ability to attach a service account to a resource (like a Compute Engine VM). If a developer needs to create a VM that runs as a specific service account, that developer must have `serviceAccountUser` on that service account. Without it, they cannot create the VM with that identity attached.

`roles/iam.serviceAccountTokenCreator` — This role grants the ability to generate OAuth tokens and sign blobs for a service account — essentially to impersonate it in API calls. This is a more powerful role and should be granted sparingly.

The ACE exam frequently tests: "A developer cannot create a VM using a specific service account even though they have `roles/compute.instanceAdmin`. Why?" The answer is that they are missing `roles/iam.serviceAccountUser` on the service account.

---

## Section 3: IAM Conditions

**[SHOW SLIDE: IAM policy binding JSON with a condition block highlighted]**

IAM Conditions allow you to grant a role only when certain attributes are true at the time of the request. Conditions are added directly to policy bindings. Common condition attributes include:

- `request.time` — restrict access to specific time windows (e.g., weekday business hours only)
- `resource.name` — restrict access to resources with specific names or name prefixes
- `resource.type` — restrict access to a specific GCP resource type
- `resource.service` — restrict access to a specific GCP service

Here is an example binding with a time-based condition:

```json
{
  "role": "roles/storage.objectAdmin",
  "members": ["user:contractor@example.com"],
  "condition": {
    "title": "Business hours only",
    "description": "Allow access only Mon-Fri 9am-5pm UTC",
    "expression": "request.time.getHours('America/Chicago') >= 9 && request.time.getHours('America/Chicago') < 17 && request.time.getDayOfWeek('America/Chicago') >= 1 && request.time.getDayOfWeek('America/Chicago') <= 5"
  }
}
```

For the ACE exam: IAM Conditions are the feature to use when a scenario requires time-based access, resource-name-based access, or temporary access. Organization Policies are for restricting what actions are allowed. VPC Service Controls are for network-level API perimeters. Know which feature answers which type of question.

---

## Section 4: gcloud IAM Commands

**[SHOW CONSOLE: Cloud Shell terminal with gcloud iam commands]**

Let's walk through the gcloud commands you will use in the lab and that appear on the ACE exam.

List all available roles:

```bash
gcloud iam roles list
```

Describe a specific predefined role to see its included permissions:

```bash
gcloud iam roles describe roles/storage.objectViewer
```

Get the current IAM policy for a project:

```bash
gcloud projects get-iam-policy PROJECT_ID
```

Grant a role to a user on a project:

```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:student@txwes.edu" \
  --role="roles/storage.objectViewer"
```

Remove a role from a user:

```bash
gcloud projects remove-iam-policy-binding PROJECT_ID \
  --member="user:student@txwes.edu" \
  --role="roles/storage.objectViewer"
```

Create a service account:

```bash
gcloud iam service-accounts create my-app-sa \
  --display-name="My Application Service Account"
```

Grant a role to a service account:

```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:my-app-sa@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectAdmin"
```

List service accounts in a project:

```bash
gcloud iam service-accounts list
```

**[SHOW CONSOLE: Run these commands live in Cloud Shell]**

Note the `--member` flag format. It always takes the form `TYPE:IDENTIFIER`, such as `user:email@domain.com`, `serviceAccount:sa@project.iam.gserviceaccount.com`, or `group:name@domain.com`. Getting this format wrong is a common mistake — remember the colon separator and the correct prefix word.

---

## Section 5: Audit Logging

**[SHOW SLIDE: Audit log types — Admin Activity, Data Access, System Event]**

Every IAM change in GCP is recorded in Cloud Audit Logs. There are three types of audit logs relevant to IAM:

Admin Activity logs record administrative actions: who modified IAM policies, who created or deleted resources, who enabled or disabled APIs. These logs are always enabled, cannot be turned off, and are free.

Data Access logs record who read data and who used the APIs to access resource metadata. These are disabled by default because they can generate large volumes of entries and incur storage costs. You must explicitly enable them for the services you want to audit.

System Event logs record GCP's internal system actions — for example, when GCP migrates your VM during maintenance.

For the ACE exam: when a question asks "how do you find out who changed an IAM policy last week?", the answer is Cloud Audit Logs — specifically Admin Activity logs. You view them in Cloud Logging under the Audit Logs section.

---

## Module 02 Summary

**[SHOW SLIDE: Summary bullet list]**

Let's bring together both parts of Module 02. IAM controls who can do what on which resource using bindings of principals, roles, and resources. Principals include Google Accounts, Service Accounts, Groups, and domain identifiers. Roles come in three categories: basic (avoid in production), predefined (service-specific, auto-updated), and custom (tailored, manually maintained).

Service accounts represent application identities. Attach them to VMs using the metadata server — never embed key files unless absolutely necessary. The `serviceAccountUser` role is required to attach a service account to a resource. IAM Conditions add attribute-based access control to policy bindings.

Key gcloud commands: `gcloud projects add-iam-policy-binding`, `gcloud projects get-iam-policy`, `gcloud iam service-accounts create`, and `gcloud iam roles describe`. All IAM changes are recorded in Cloud Audit Logs — Admin Activity logs are always on and free.

Complete the lab, take the quiz, and post to the discussion board. Module 03 covers Compute Engine — we will finally start spinning up virtual machines.

---

End of Part 2 — Module 02

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
