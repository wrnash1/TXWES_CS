# Lab — Module 04

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Storage — Buckets, Storage Classes, and Lifecycle Policies

### Points: 100

---

## Lab Overview

In this lab you will create Cloud Storage buckets with specific storage classes and location types, upload and manage objects, configure a lifecycle policy, enable object versioning, and test access with signed URLs and IAM bindings. These are core Cloud Storage skills for the Google Cloud ACE exam.

All tasks use Cloud Shell and the gcloud storage CLI. Complete this lab in your `txwes-gcp-lab-[your initials]` project.

Estimated completion time: 60–75 minutes.

---

## Prerequisites

- Modules 01, 02, and 03 labs completed
- Active project configured in Cloud Shell:

```bash
gcloud config list
```

Confirm project, region, and zone are set.

---

## Part 1: Create Buckets with Different Configurations (20 points)

### Task 1.1 — Create a Regional Standard Bucket (10 points)

Create a regional Standard bucket for active project assets:

```bash
gcloud storage buckets create gs://txwes-standard-[your-initials] \
  --location=us-central1 \
  --storage-class=STANDARD \
  --uniform-bucket-level-access
```

Replace `[your-initials]` with your initials (e.g., `wn`). Bucket names must be globally unique — if you get a name conflict, append a number.

Verify the bucket was created:

```bash
gcloud storage buckets describe gs://txwes-standard-[your-initials]
```

Note the `location`, `storageClass`, and `iamConfiguration.uniformBucketLevelAccess.enabled` fields in the output.

Deliverable: Screenshot of the `gcloud storage buckets describe` output for your Standard bucket. Label it "Task 1.1".

### Task 1.2 — Create a Nearline Bucket (10 points)

Create a second bucket with Nearline storage class for backup files:

```bash
gcloud storage buckets create gs://txwes-nearline-[your-initials] \
  --location=us-central1 \
  --storage-class=NEARLINE \
  --uniform-bucket-level-access
```

Verify:

```bash
gcloud storage buckets describe gs://txwes-nearline-[your-initials] \
  --format="value(storageClass, location)"
```

Deliverable: Screenshot confirming the Nearline storage class and location. Label it "Task 1.2".

---

## Part 2: Upload and Manage Objects (20 points)

### Task 2.1 — Create and Upload Sample Files (10 points)

Create several sample files to work with:

```bash
echo "This is a web asset - logo.png simulation" > logo.txt
echo "This is a monthly report for January" > report-jan.txt
echo "This is a quarterly compliance archive" > compliance-q1.txt
echo "This is an annual audit log for 2023" > audit-2023.txt
```

Upload all files to your Standard bucket:

```bash
gcloud storage cp logo.txt gs://txwes-standard-[your-initials]/assets/
gcloud storage cp report-jan.txt gs://txwes-standard-[your-initials]/reports/
gcloud storage cp compliance-q1.txt gs://txwes-standard-[your-initials]/compliance/
gcloud storage cp audit-2023.txt gs://txwes-standard-[your-initials]/archives/
```

List the contents of your bucket to confirm all files uploaded:

```bash
gcloud storage ls gs://txwes-standard-[your-initials]/
```

Deliverable: Screenshot of the `gcloud storage ls` output showing all four object paths. Label it "Task 2.1".

### Task 2.2 — Copy an Object Between Buckets (10 points)

Copy the audit log from the Standard bucket to the Nearline bucket (simulating moving archive data):

```bash
gcloud storage cp \
  gs://txwes-standard-[your-initials]/archives/audit-2023.txt \
  gs://txwes-nearline-[your-initials]/archives/audit-2023.txt
```

Verify the file exists in the Nearline bucket:

```bash
gcloud storage ls gs://txwes-nearline-[your-initials]/
```

Deliverable: Screenshot of the listing in the Nearline bucket. Label it "Task 2.2".

---

## Part 3: Lifecycle Policies (25 points)

### Task 3.1 — Write a Lifecycle Policy JSON (10 points)

Create a lifecycle policy file that implements the following rules:

1. Move objects to Nearline storage after 30 days
2. Move objects to Coldline storage after 90 days
3. Delete all objects after 365 days

Create the JSON file:

```bash
cat > lifecycle-policy.json << 'EOF'
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
        "condition": {
          "age": 30,
          "matchesStorageClass": ["STANDARD"]
        }
      },
      {
        "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
        "condition": {
          "age": 90,
          "matchesStorageClass": ["NEARLINE"]
        }
      },
      {
        "action": {"type": "Delete"},
        "condition": {"age": 365}
      }
    ]
  }
}
EOF
```

Display the file to confirm it is correct:

```bash
cat lifecycle-policy.json
```

Deliverable: Screenshot of the `cat lifecycle-policy.json` output showing all three rules. Label it "Task 3.1".

### Task 3.2 — Apply the Lifecycle Policy (10 points)

Apply the lifecycle policy to your Standard bucket:

```bash
gcloud storage buckets update gs://txwes-standard-[your-initials] \
  --lifecycle-file=lifecycle-policy.json
```

Verify the lifecycle configuration was applied:

```bash
gcloud storage buckets describe gs://txwes-standard-[your-initials] \
  --format="yaml(lifecycle)"
```

Deliverable: Screenshot of the lifecycle output from the describe command. Label it "Task 3.2".

### Task 3.3 — Add a Versioning Cleanup Rule (5 points)

Create a second lifecycle policy that also includes a rule to delete noncurrent object versions after 7 days. Update `lifecycle-policy.json` to add this fourth rule:

```bash
cat > lifecycle-policy-v2.json << 'EOF'
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
        "condition": {
          "age": 30,
          "matchesStorageClass": ["STANDARD"]
        }
      },
      {
        "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
        "condition": {
          "age": 90,
          "matchesStorageClass": ["NEARLINE"]
        }
      },
      {
        "action": {"type": "Delete"},
        "condition": {"age": 365}
      },
      {
        "action": {"type": "Delete"},
        "condition": {"isLive": false, "numNewerVersions": 1, "age": 7}
      }
    ]
  }
}
EOF
```

Deliverable: Screenshot of the v2 lifecycle JSON file showing all four rules. Label it "Task 3.3".

---

## Part 4: Object Versioning (15 points)

### Task 4.1 — Enable Versioning (5 points)

Enable object versioning on your Standard bucket:

```bash
gcloud storage buckets update gs://txwes-standard-[your-initials] --versioning
```

Confirm versioning is enabled:

```bash
gcloud storage buckets describe gs://txwes-standard-[your-initials] \
  --format="value(versioning.enabled)"
```

The output should show `True`.

Deliverable: Screenshot showing `True` in the output. Label it "Task 4.1".

### Task 4.2 — Overwrite a File and List Versions (10 points)

Overwrite the logo file to create a new version:

```bash
echo "This is the UPDATED logo.png simulation - version 2" > logo-v2.txt
gcloud storage cp logo-v2.txt gs://txwes-standard-[your-initials]/assets/logo.txt
```

List all versions of the object (including noncurrent):

```bash
gcloud storage ls -a gs://txwes-standard-[your-initials]/assets/
```

You should see two entries for `logo.txt` with different generation numbers — the original (noncurrent) and the new version (live).

Deliverable: Screenshot of the `-a` listing showing two versions of `logo.txt`. Label it "Task 4.2".

---

## Part 5: Cloud Storage IAM (15 points)

### Task 5.1 — Grant a Bucket-Level IAM Role (10 points)

First, get your own account email:

```bash
gcloud config get-value account
```

Grant yourself `roles/storage.objectViewer` on the Nearline bucket specifically (not at project level):

```bash
gcloud storage buckets add-iam-policy-binding \
  gs://txwes-nearline-[your-initials] \
  --member="user:YOUR_EMAIL" \
  --role="roles/storage.objectViewer"
```

View the bucket's IAM policy to confirm:

```bash
gcloud storage buckets get-iam-policy gs://txwes-nearline-[your-initials]
```

Deliverable: Screenshot of the IAM policy output showing the objectViewer binding for your account. Label it "Task 5.1".

### Task 5.2 — Uniform Access Verification (5 points)

Verify that uniform bucket-level access prevents object-level ACL changes. Try to set an ACL on an object in the Standard bucket (this should fail because uniform access is enabled):

```bash
gcloud storage objects update gs://txwes-standard-[your-initials]/assets/logo.txt \
  --predefined-acl=publicRead 2>&1
```

The command should return an error because uniform bucket-level access blocks object-level ACLs.

Deliverable: Screenshot of the error message. Label it "Task 5.2". In your submission notes, explain in one sentence why this error occurred.

---

## Cleanup (5 points)

Delete all objects in both buckets and then delete the buckets:

```bash
gcloud storage rm -r gs://txwes-standard-[your-initials]/
gcloud storage rm -r gs://txwes-nearline-[your-initials]/
gcloud storage buckets delete gs://txwes-standard-[your-initials]
gcloud storage buckets delete gs://txwes-nearline-[your-initials]
```

Deliverable: Screenshot of the successful bucket deletion messages. Label it "Cleanup".

---

## Reflection Questions

Answer in your submission document (2–4 sentences each):

1. You applied a lifecycle policy that moves objects to Nearline after 30 days. If an object is deleted before 30 days (for example, after only 5 days), what charges does Cloud Storage bill for, and why?
2. A team wants to enable versioning for recovery but is worried about storage cost growing unboundedly. What specific lifecycle rule would you add to prevent this?
3. An external auditor needs to download one specific compliance report from your private bucket. The auditor has no Google Account. What Cloud Storage feature would you use, and what is the maximum duration you can set?

---

## Grading Rubric

| Task | Points | Criteria |
|---|---|---|
| 1.1 Standard bucket created and described | 10 | Describe output shows STANDARD class, uniform access enabled |
| 1.2 Nearline bucket created and verified | 10 | Storage class NEARLINE confirmed |
| 2.1 Files uploaded and listed | 10 | All four object paths visible in listing |
| 2.2 Object copied to Nearline bucket | 10 | Nearline bucket listing shows audit file |
| 3.1 Lifecycle JSON created with three rules | 10 | All three rules visible in cat output |
| 3.2 Lifecycle policy applied and verified | 10 | Lifecycle config visible in describe output |
| 3.3 Fourth versioning cleanup rule added | 5 | v2 JSON shows all four rules |
| 4.1 Versioning enabled | 5 | Output shows True |
| 4.2 Two versions visible in listing | 10 | Both generation numbers visible for logo.txt |
| 5.1 Bucket IAM binding applied | 10 | IAM policy shows objectViewer for account |
| 5.2 Uniform access blocks ACL | 5 | Error message shown and explained |
| Cleanup | 5 | Both buckets deleted |
| Total | 100 | |

---

End of Lab — Module 04

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
