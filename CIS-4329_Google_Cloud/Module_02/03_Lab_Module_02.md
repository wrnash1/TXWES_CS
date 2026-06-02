# Lab — Module 02

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: IAM Roles, Policy Bindings, and Service Accounts

### Points: 100

---

## Lab Overview

In this lab you will manage IAM policy bindings using both the Google Cloud Console and the gcloud CLI, create a custom IAM role, create a service account, and attach a service account to a Compute Engine VM. These tasks are core competencies for the Google Cloud Associate Cloud Engineer exam.

All tasks use Cloud Shell. No local SDK installation is required. Complete the lab in the GCP project you created in Module 01 (`txwes-gcp-lab-[your initials]`).

Estimated completion time: 60–75 minutes.

---

## Prerequisites

- Module 01 lab completed (project `txwes-gcp-lab-[your initials]` exists and is configured)
- Compute Engine API enabled in your project
- Cloud Shell accessible

Enable the Compute Engine API if not already done:

```bash
gcloud services enable compute.googleapis.com
```

---

## Part 1: Inspect the Current IAM Policy (15 points)

### Task 1.1 — View IAM Policy via Console (5 points)

1. Navigate to IAM and Admin > IAM in the Google Cloud Console.
2. Observe the list of principals and their assigned roles.
3. Identify any principal with a basic role (`roles/owner`, `roles/editor`, or `roles/viewer`).

Deliverable: Screenshot of the IAM page showing the current policy. Label it "Task 1.1".

### Task 1.2 — View IAM Policy via gcloud (10 points)

Open Cloud Shell and run:

```bash
gcloud projects get-iam-policy $GOOGLE_CLOUD_PROJECT
```

The `$GOOGLE_CLOUD_PROJECT` environment variable is automatically set in Cloud Shell to your active project ID. Review the JSON output. Identify the `bindings` array, the `role` fields, and the `members` fields.

Run the same command with JSON format and save it to a file:

```bash
gcloud projects get-iam-policy $GOOGLE_CLOUD_PROJECT \
  --format=json > current-policy.json
cat current-policy.json
```

Deliverable: Screenshot of the `gcloud projects get-iam-policy` output showing at least one binding. Label it "Task 1.2".

---

## Part 2: Add and Remove IAM Bindings (20 points)

### Task 2.1 — Grant a Role to Your Own Account at Viewer Level (10 points)

For this exercise, you will grant the `roles/storage.objectViewer` role to your own account on the project. In a real environment you would grant this to a different user, but for lab purposes using your own account demonstrates the mechanics.

First, retrieve your account email:

```bash
gcloud config get-value account
```

Now grant the role. Replace `YOUR_EMAIL` with your account email:

```bash
gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
  --member="user:YOUR_EMAIL" \
  --role="roles/storage.objectViewer"
```

Verify the binding was added:

```bash
gcloud projects get-iam-policy $GOOGLE_CLOUD_PROJECT \
  --flatten="bindings[].members" \
  --format="table(bindings.role,bindings.members)" \
  --filter="bindings.members:YOUR_EMAIL"
```

Deliverable: Screenshot showing the new `roles/storage.objectViewer` binding for your account. Label it "Task 2.1".

### Task 2.2 — Remove the Binding (10 points)

Remove the role you just added:

```bash
gcloud projects remove-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
  --member="user:YOUR_EMAIL" \
  --role="roles/storage.objectViewer"
```

Confirm the binding is gone:

```bash
gcloud projects get-iam-policy $GOOGLE_CLOUD_PROJECT \
  --flatten="bindings[].members" \
  --format="table(bindings.role,bindings.members)" \
  --filter="bindings.members:YOUR_EMAIL"
```

The output should show no `storage.objectViewer` binding for your account.

Deliverable: Screenshot showing the filter result with no `storage.objectViewer` binding. Label it "Task 2.2".

---

## Part 3: Explore Predefined Roles (15 points)

### Task 3.1 — List and Describe Roles (10 points)

List the predefined roles available for Cloud Storage:

```bash
gcloud iam roles list --filter="name:roles/storage"
```

Describe the `roles/storage.objectViewer` role to see its included permissions:

```bash
gcloud iam roles describe roles/storage.objectViewer
```

Note the list of included permissions in the output.

Describe the `roles/storage.objectAdmin` role:

```bash
gcloud iam roles describe roles/storage.objectAdmin
```

Compare the two permission lists.

Deliverable: Screenshot of the `roles/storage.objectViewer` describe output. Label it "Task 3.1".

### Task 3.2 — Identify a Compute Engine Role (5 points)

Describe the `roles/compute.instanceAdmin.v1` role:

```bash
gcloud iam roles describe roles/compute.instanceAdmin.v1
```

Review the list of permissions. Count how many `compute.instances.*` permissions are included.

Deliverable: Screenshot of the describe output. In your submission notes, write how many `compute.instances.*` permissions you counted. Label it "Task 3.2".

---

## Part 4: Create a Custom Role (20 points)

### Task 4.1 — Design a Minimal Monitoring Role (10 points)

You will create a custom role that allows a user to list Compute Engine VM instances and view their details, but grants nothing else. This simulates a read-only operations viewer role.

Create a YAML file defining the role:

```bash
cat > custom-viewer-role.yaml << 'EOF'
title: "VM Read Only Viewer"
description: "Can list and describe VM instances only. No write access."
stage: "GA"
includedPermissions:
  - compute.instances.list
  - compute.instances.get
  - compute.zones.list
  - compute.regions.list
EOF
```

Create the custom role in your project:

```bash
gcloud iam roles create vmReadOnlyViewer \
  --project=$GOOGLE_CLOUD_PROJECT \
  --file=custom-viewer-role.yaml
```

Deliverable: Screenshot of the successful role creation output. Label it "Task 4.1".

### Task 4.2 — Verify the Custom Role (10 points)

List custom roles in your project to confirm it was created:

```bash
gcloud iam roles list --project=$GOOGLE_CLOUD_PROJECT
```

Describe the custom role:

```bash
gcloud iam roles describe vmReadOnlyViewer \
  --project=$GOOGLE_CLOUD_PROJECT
```

Deliverable: Screenshot of the describe output showing your custom role's permissions. Label it "Task 4.2".

---

## Part 5: Create and Use a Service Account (25 points)

### Task 5.1 — Create a Service Account (10 points)

Create a service account named `lab-vm-sa`:

```bash
gcloud iam service-accounts create lab-vm-sa \
  --display-name="Lab VM Service Account" \
  --description="Service account for Module 02 lab VM"
```

List service accounts to confirm creation:

```bash
gcloud iam service-accounts list
```

Grant the service account `roles/storage.objectViewer` on the project:

```bash
gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
  --member="serviceAccount:lab-vm-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
```

Deliverable: Screenshot of the service account list showing your new `lab-vm-sa` account. Label it "Task 5.1".

### Task 5.2 — Create a VM with the Service Account (10 points)

Create a small Compute Engine VM attached to your service account:

```bash
gcloud compute instances create lab-iam-vm \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --service-account=lab-vm-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com \
  --scopes=cloud-platform \
  --no-address
```

The `--no-address` flag creates the VM without an external IP, which is a security best practice.

Confirm the VM was created:

```bash
gcloud compute instances list
```

Deliverable: Screenshot of the `gcloud compute instances list` output showing `lab-iam-vm` with status RUNNING. Label it "Task 5.2".

### Task 5.3 — Verify Service Account Attachment (5 points)

Describe the VM to confirm the service account is attached:

```bash
gcloud compute instances describe lab-iam-vm \
  --zone=us-central1-a \
  --format="yaml(serviceAccounts)"
```

The output should show the `lab-vm-sa` email in the `serviceAccounts` section.

Deliverable: Screenshot of the service account section from the describe output. Label it "Task 5.3".

---

## Part 6: Cleanup (5 points)

Delete the VM to avoid ongoing charges:

```bash
gcloud compute instances delete lab-iam-vm \
  --zone=us-central1-a \
  --quiet
```

Deliverable: Screenshot of the successful delete confirmation. Label it "Task 6".

Note: Leave the `lab-vm-sa` service account and `vmReadOnlyViewer` custom role in place — they will be referenced in future labs.

---

## Reflection Questions (bonus — included in rubric total)

Answer in your submission document (2–4 sentences each):

1. Why is it a security risk to grant `roles/editor` to a service account used by a web application?
2. You created a VM with `--scopes=cloud-platform`. What does this scope do, and what controls the actual permissions?
3. If you needed to grant a contractor temporary read-only access to your Cloud Storage bucket only during a specific project (ending in 30 days), how would you structure the IAM binding? What feature would you use?

---

## Grading Rubric

| Task | Points | Criteria |
|---|---|---|
| 1.1 IAM policy Console screenshot | 5 | Screenshot present showing at least one binding |
| 1.2 gcloud get-iam-policy output | 10 | JSON output shown with bindings visible |
| 2.1 Role granted and binding confirmed | 10 | objectViewer binding visible for account |
| 2.2 Role removed and confirmed absent | 10 | Filter output shows no objectViewer binding |
| 3.1 Role describe output for objectViewer | 10 | Permissions list visible in screenshot |
| 3.2 Compute instanceAdmin role described | 5 | Output shown; count in submission notes |
| 4.1 Custom role created | 10 | Success output with role name shown |
| 4.2 Custom role verified and described | 10 | Describe output showing four permissions |
| 5.1 Service account created and role granted | 10 | SA list shows lab-vm-sa |
| 5.2 VM created with SA attached | 10 | instances list shows lab-iam-vm RUNNING |
| 5.3 SA attachment verified | 5 | serviceAccounts section in describe output |
| 6 VM deleted | 5 | Delete success confirmation shown |
| Total | 100 | |

---

End of Lab — Module 02

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
