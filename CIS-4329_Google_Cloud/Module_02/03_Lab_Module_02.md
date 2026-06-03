# Lab: Module 02 — IAM and Access Control in GCP

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Lab Overview

In this lab you will implement IAM access control in GCP. You will create
service accounts, assign predefined roles, test least-privilege access, create
a custom role, and enable Data Access audit logs. These skills directly map to
ACE exam scenarios.

**Estimated Time:** 75 minutes

**Prerequisites:**

- Completed Module 01 lab (GCP project created, Cloud Shell configured)
- An active GCP project with billing enabled
- Owner or Editor access to the project

**Learning Objectives:**

By the end of this lab you will be able to:

1. Assign predefined roles to users and service accounts
2. Create and configure a custom IAM role
3. Create service accounts and attach them to resources
4. Verify least-privilege access using the Policy Analyzer
5. Enable and query Cloud Audit Logs
6. Test Workload Identity concepts using service account impersonation

---

## Part 1 — Explore and Modify IAM Policies (15 minutes)

### Step 1.1 — View the Current IAM Policy

```bash
# Set your project (replace with your actual project ID)
export PROJECT_ID=$(gcloud config get-value project)

# View the current IAM policy
gcloud projects get-iam-policy $PROJECT_ID

# View in JSON format for inspection
gcloud projects get-iam-policy $PROJECT_ID --format=json
```

Record the number of bindings currently in the policy.

### Step 1.2 — Add a Role Binding

Add a viewer binding for your own account (simulating adding a new team member):

```bash
# Replace with your actual email address
export MY_EMAIL="your-email@example.com"

# Grant viewer role
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="user:$MY_EMAIL" \
  --role="roles/viewer"

# Verify the binding was added
gcloud projects get-iam-policy $PROJECT_ID \
  --flatten="bindings[].members" \
  --format="table(bindings.role,bindings.members)" \
  --filter="bindings.members:$MY_EMAIL"
```

### Step 1.3 — Remove a Role Binding

```bash
# Remove the viewer binding
gcloud projects remove-iam-policy-binding $PROJECT_ID \
  --member="user:$MY_EMAIL" \
  --role="roles/viewer"

# Confirm removal
gcloud projects get-iam-policy $PROJECT_ID \
  --flatten="bindings[].members" \
  --format="table(bindings.role,bindings.members)" \
  --filter="bindings.members:$MY_EMAIL"
```

---

## Part 2 — Create and Use Service Accounts (20 minutes)

### Step 2.1 — Create a Service Account

```bash
# Create a service account for a hypothetical app
gcloud iam service-accounts create lab02-app-runner \
  --display-name="Lab02 App Runner" \
  --description="Service account for Module 02 lab exercises"

# Verify creation
gcloud iam service-accounts list

# Store the service account email
export SA_EMAIL="lab02-app-runner@${PROJECT_ID}.iam.gserviceaccount.com"
echo "Service Account: $SA_EMAIL"
```

### Step 2.2 — Assign a Predefined Role to the Service Account

```bash
# Grant storage object viewer role to the service account
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/storage.objectViewer"

# Verify the binding
gcloud projects get-iam-policy $PROJECT_ID \
  --flatten="bindings[].members" \
  --format="table(bindings.role,bindings.members)" \
  --filter="bindings.members:$SA_EMAIL"
```

### Step 2.3 — Test Service Account Impersonation

```bash
# Describe the service account
gcloud iam service-accounts describe $SA_EMAIL

# Generate a short-lived access token for the service account
# (requires iam.serviceAccounts.getAccessToken permission on the SA)
gcloud auth print-access-token \
  --impersonate-service-account=$SA_EMAIL
```

### Step 2.4 — Examine Default Service Accounts

```bash
# List all service accounts including default ones
gcloud iam service-accounts list --format=json | \
  python3 -c "import sys,json; [print(sa['email']) for sa in json.load(sys.stdin)]"
```

Look for:

- The Compute Engine default service account:
  `PROJECT_NUMBER-compute@developer.gserviceaccount.com`
- The App Engine default service account:
  `PROJECT_ID@appspot.gserviceaccount.com`

**Question 2.4:** Why are default service accounts with broad permissions
considered a security risk?

---

## Part 3 — Create a Custom Role (15 minutes)

### Step 3.1 — Define a Custom Role in YAML

Create a YAML file defining a custom role:

```bash
cat > custom-role.yaml << 'EOF'
title: "Lab Custom Storage Reader"
description: "Read objects and list buckets only — no write, no delete"
stage: "GA"
includedPermissions:
  - storage.buckets.list
  - storage.buckets.get
  - storage.objects.get
  - storage.objects.list
EOF
```

### Step 3.2 — Create the Custom Role

```bash
# Create the custom role in your project
gcloud iam roles create labCustomStorageReader \
  --project=$PROJECT_ID \
  --file=custom-role.yaml

# Verify creation
gcloud iam roles describe labCustomStorageReader \
  --project=$PROJECT_ID
```

### Step 3.3 — Assign the Custom Role

```bash
# Grant the custom role to the service account
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="projects/$PROJECT_ID/roles/labCustomStorageReader"
```

### Step 3.4 — Compare Permissions

```bash
# Describe the custom role to see its permissions
gcloud iam roles describe labCustomStorageReader --project=$PROJECT_ID

# Describe a predefined role for comparison
gcloud iam roles describe roles/storage.objectViewer
```

**Question 3.4:** What permissions does `roles/storage.objectViewer` have that
your custom role does not? What does your custom role have that the predefined
role lacks?

---

## Part 4 — IAM Conditions (10 minutes)

### Step 4.1 — Add a Time-Bounded Binding

Add a role binding with an expiration condition. This simulates granting
temporary access to a contractor.

```bash
# Grant editor access that expires at the end of 2026
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/editor" \
  --condition='expression=request.time < timestamp("2026-12-31T23:59:59Z"),title=Expires-2026,description=Temporary access for lab'
```

### Step 4.2 — View the Conditional Binding

```bash
# View bindings for the service account
gcloud projects get-iam-policy $PROJECT_ID \
  --flatten="bindings[].members" \
  --format="table(bindings.role,bindings.condition,bindings.members)" \
  --filter="bindings.members:$SA_EMAIL"
```

### Step 4.3 — Remove the Conditional Binding

```bash
# Remove only the conditional editor binding (specify condition title)
gcloud projects remove-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/editor" \
  --condition='title=Expires-2026'
```

---

## Part 5 — Cloud Audit Logs (15 minutes)

### Step 5.1 — View Admin Activity Logs

```bash
# View the most recent admin activity log entries
gcloud logging read \
  "logName=\"projects/$PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity\"" \
  --limit=10 \
  --format="table(timestamp,protoPayload.authenticationInfo.principalEmail,protoPayload.methodName)"
```

### Step 5.2 — Filter for IAM Changes

```bash
# Find all IAM policy change events
gcloud logging read \
  "logName=\"projects/$PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity\"
   AND protoPayload.methodName=\"SetIamPolicy\"" \
  --limit=5 \
  --format=json
```

### Step 5.3 — Enable Data Access Logs

In the Cloud Console:

1. Navigate to **IAM & Admin > Audit Logs**.
2. Find **Cloud Storage** in the service list.
3. Enable **Data Read** and **Data Write** audit logs.
4. Click **Save**.

Verify via gcloud:

```bash
# View the current audit config in the IAM policy
gcloud projects get-iam-policy $PROJECT_ID --format=json | \
  python3 -c "import sys,json; p=json.load(sys.stdin); [print(ac) for ac in p.get('auditConfigs',[])]"
```

---

## Lab Deliverables

Submit a lab report (PDF or Word) containing:

1. Screenshot of the IAM page showing your project's policy bindings.
2. Output of `gcloud iam service-accounts list` showing your created SA.
3. Output of `gcloud iam roles describe labCustomStorageReader` showing the
   custom role definition.
4. Screenshot of the Audit Logs page showing Data Access logs enabled for
   Cloud Storage.
5. Output of the audit log query showing at least one `SetIamPolicy` event.
6. Answers to the lab questions.

**Lab Questions:**

1. You need to grant a developer read access to Cloud Storage objects but not
   the ability to list or modify buckets. Which predefined role best fits, and
   what permissions does it include?
2. Why is it risky to grant `roles/editor` at the project level to a service
   account used by a single microservice?
3. A service account key file was accidentally committed to a public GitHub
   repository. What are the immediate steps to mitigate the exposure?
4. What is the difference between Admin Activity logs and Data Access logs?
   Why are Data Access logs disabled by default?
5. Explain the etag field in an IAM policy and why it matters when updating
   policies programmatically.

---

## Cleanup

```bash
# Remove IAM bindings for the service account
gcloud projects remove-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/storage.objectViewer"

gcloud projects remove-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="projects/$PROJECT_ID/roles/labCustomStorageReader"

# Delete the custom role
gcloud iam roles delete labCustomStorageReader --project=$PROJECT_ID

# Delete the service account
gcloud iam service-accounts delete $SA_EMAIL
```

---

End of Lab — Module 02

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash
