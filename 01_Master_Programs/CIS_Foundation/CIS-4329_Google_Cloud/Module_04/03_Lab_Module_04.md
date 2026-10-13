# Lab: Module 04 — Cloud Storage

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Lab Overview

In this lab you will create and configure Cloud Storage buckets, upload and
manage objects, configure lifecycle policies, enable object versioning,
generate signed URLs, and set up Pub/Sub notifications for storage events.

**Estimated Time:** 75 minutes

**Prerequisites:**

- Active GCP project with billing enabled
- Cloud Shell access
- Cloud Storage API enabled (usually enabled by default)

**Learning Objectives:**

By the end of this lab you will be able to:

1. Create buckets with specific configurations
2. Upload, download, and manage objects via gcloud
3. Configure and test object lifecycle policies
4. Enable and use object versioning
5. Generate signed URLs for temporary access
6. Configure Pub/Sub notifications for storage events

---

## Part 1 — Create and Configure Buckets (15 minutes)

### Step 1.1 — Set Environment Variables

```bash
export PROJECT_ID=$(gcloud config get-value project)
export BUCKET_MAIN="cis4329-lab04-${PROJECT_ID}"
export BUCKET_ARCHIVE="cis4329-archive-${PROJECT_ID}"
echo "Main bucket: gs://$BUCKET_MAIN"
echo "Archive bucket: gs://$BUCKET_ARCHIVE"
```

### Step 1.2 — Create the Main Bucket (Standard, Regional)

```bash
gcloud storage buckets create gs://$BUCKET_MAIN \
  --location=us-central1 \
  --default-storage-class=STANDARD \
  --uniform-bucket-level-access

# Verify
gcloud storage buckets describe gs://$BUCKET_MAIN
```

### Step 1.3 — Create the Archive Bucket (Coldline, Regional)

```bash
gcloud storage buckets create gs://$BUCKET_ARCHIVE \
  --location=us-central1 \
  --default-storage-class=COLDLINE \
  --uniform-bucket-level-access

gcloud storage buckets list
```

### Step 1.4 — Upload Test Objects

```bash
# Create test files
for i in 1 2 3 4 5; do
  echo "This is test file number $i — created $(date)" > test-file-$i.txt
done

# Upload to the main bucket
gcloud storage cp test-file-*.txt gs://$BUCKET_MAIN/

# Upload a subdirectory
mkdir -p logs/app
echo "App log entry" > logs/app/app.log
echo "Error log entry" > logs/app/error.log
gcloud storage cp -r logs/ gs://$BUCKET_MAIN/

# List bucket contents
gcloud storage ls gs://$BUCKET_MAIN/
gcloud storage ls gs://$BUCKET_MAIN/logs/app/
```

### Step 1.5 — Download and Delete Objects

```bash
# Download a file
gcloud storage cp gs://$BUCKET_MAIN/test-file-1.txt ./downloaded-file-1.txt
cat downloaded-file-1.txt

# Delete an object
gcloud storage rm gs://$BUCKET_MAIN/test-file-5.txt

# Verify deletion
gcloud storage ls gs://$BUCKET_MAIN/
```

---

## Part 2 — Object Lifecycle Policy (20 minutes)

### Step 2.1 — Create a Lifecycle Policy File

```bash
cat > lifecycle.json << 'EOF'
{
  "lifecycle": {
    "rule": [
      {
        "action": {
          "type": "SetStorageClass",
          "storageClass": "NEARLINE"
        },
        "condition": {
          "age": 30,
          "matchesStorageClass": ["STANDARD"]
        }
      },
      {
        "action": {
          "type": "SetStorageClass",
          "storageClass": "COLDLINE"
        },
        "condition": {
          "age": 90,
          "matchesStorageClass": ["NEARLINE"]
        }
      },
      {
        "action": {
          "type": "Delete"
        },
        "condition": {
          "age": 365
        }
      }
    ]
  }
}
EOF
```

### Step 2.2 — Apply the Lifecycle Policy

```bash
gcloud storage buckets update gs://$BUCKET_MAIN \
  --lifecycle-file=lifecycle.json

# Verify the policy was applied
gcloud storage buckets describe gs://$BUCKET_MAIN \
  --format=json | python3 -c "
import sys, json
bucket = json.load(sys.stdin)
lifecycle = bucket.get('lifecycle', {})
rules = lifecycle.get('rule', [])
for i, rule in enumerate(rules):
    print(f'Rule {i+1}: {rule}')
"
```

### Step 2.3 — Manually Change an Object's Storage Class

```bash
# Move test-file-2.txt to Nearline immediately
gcloud storage objects update gs://$BUCKET_MAIN/test-file-2.txt \
  --storage-class=NEARLINE

# Verify the storage class changed
gcloud storage objects describe gs://$BUCKET_MAIN/test-file-2.txt \
  --format='value(storageClass)'
```

**Question 2.3:** If you delete `test-file-2.txt` tomorrow (it was just set to
Nearline storage class), how many days of storage will you be charged for?

---

## Part 3 — Object Versioning (15 minutes)

### Step 3.1 — Enable Versioning

```bash
gcloud storage buckets update gs://$BUCKET_MAIN \
  --versioning

# Verify
gcloud storage buckets describe gs://$BUCKET_MAIN \
  --format='value(versioning.enabled)'
```

### Step 3.2 — Create Multiple Versions of an Object

```bash
# Upload initial version
echo "Version 1 content" > versioned-file.txt
gcloud storage cp versioned-file.txt gs://$BUCKET_MAIN/versioned-file.txt

# Overwrite with version 2
echo "Version 2 content" > versioned-file.txt
gcloud storage cp versioned-file.txt gs://$BUCKET_MAIN/versioned-file.txt

# Overwrite with version 3
echo "Version 3 content" > versioned-file.txt
gcloud storage cp versioned-file.txt gs://$BUCKET_MAIN/versioned-file.txt
```

### Step 3.3 — List All Versions

```bash
# List all versions (including noncurrent)
gcloud storage ls -a gs://$BUCKET_MAIN/versioned-file.txt
```

Record all generation numbers from the output.

### Step 3.4 — Restore a Previous Version

```bash
# Get the generation number of version 1 (the oldest)
# Replace GENERATION_1 with the oldest generation number from Step 3.3

# Restore version 1 to a new name
gcloud storage cp \
  "gs://$BUCKET_MAIN/versioned-file.txt#GENERATION_1" \
  gs://$BUCKET_MAIN/versioned-file-restored.txt

# Verify contents
gcloud storage cp gs://$BUCKET_MAIN/versioned-file-restored.txt ./
cat versioned-file-restored.txt
```

---

## Part 4 — Signed URLs (10 minutes)

### Step 4.1 — Create a Service Account for Signing

```bash
# Create a dedicated service account for URL signing
gcloud iam service-accounts create storage-signer \
  --display-name="Storage URL Signer"

export SIGNER_SA="storage-signer@${PROJECT_ID}.iam.gserviceaccount.com"

# Grant storage viewer to the SA
gcloud storage buckets add-iam-policy-binding gs://$BUCKET_MAIN \
  --member="serviceAccount:$SIGNER_SA" \
  --role=roles/storage.objectViewer

# Grant your account permission to impersonate the SA
gcloud iam service-accounts add-iam-policy-binding $SIGNER_SA \
  --member="user:$(gcloud config get-value account)" \
  --role=roles/iam.serviceAccountTokenCreator
```

### Step 4.2 — Generate a Signed URL

```bash
# Generate a signed URL valid for 15 minutes
gcloud storage sign-url gs://$BUCKET_MAIN/test-file-1.txt \
  --duration=15m \
  --impersonate-service-account=$SIGNER_SA

# Test the URL with curl (replace URL below with output from command above)
# curl "https://storage.googleapis.com/..."
```

**Question 4.2:** After the signed URL expires, what happens if someone
tries to use it? Does this affect the object itself?

---

## Part 5 — Pub/Sub Notifications (15 minutes)

### Step 5.1 — Create a Pub/Sub Topic

```bash
gcloud pubsub topics create storage-events

# Create a subscription to receive messages
gcloud pubsub subscriptions create storage-events-sub \
  --topic=storage-events
```

### Step 5.2 — Grant Cloud Storage Permission to Publish

```bash
# Get the Cloud Storage service agent email
STORAGE_SA=$(gcloud storage service-agent --project=$PROJECT_ID)
echo "Storage Service Agent: $STORAGE_SA"

# Grant Pub/Sub publisher role
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$STORAGE_SA" \
  --role=roles/pubsub.publisher
```

### Step 5.3 — Create the Notification

```bash
gcloud storage buckets notifications create gs://$BUCKET_MAIN \
  --topic=storage-events \
  --event-types=OBJECT_FINALIZE,OBJECT_DELETE

# List notifications
gcloud storage buckets notifications list gs://$BUCKET_MAIN
```

### Step 5.4 — Test the Notification

```bash
# Upload a file to trigger a notification
echo "Notification test" > notification-test.txt
gcloud storage cp notification-test.txt gs://$BUCKET_MAIN/

# Pull messages from the subscription
gcloud pubsub subscriptions pull storage-events-sub \
  --limit=5 \
  --auto-ack \
  --format=json
```

---

## Lab Deliverables

Submit a lab report containing:

1. Output of `gcloud storage buckets list` showing both buckets.
2. Output of `gcloud storage ls gs://BUCKET_MAIN/` showing uploaded objects.
3. Screenshot of the lifecycle configuration applied to the main bucket.
4. Output of `gcloud storage ls -a gs://BUCKET_MAIN/versioned-file.txt`
   showing all generations.
5. The signed URL generated in Part 4 (redacted if concerned about security —
   it expires in 15 minutes regardless).
6. Output of the Pub/Sub pull command showing at least one notification event.
7. Answers to the lab questions.

**Lab Questions:**

1. You upload a 100 GB object to a Coldline bucket. After 45 days you decide
   you no longer need the file and delete it. How many days of Coldline storage
   are you billed for?
2. Explain the difference between uniform bucket-level access and fine-grained
   access control. For a new production bucket, which would you choose and why?
3. A user has `roles/storage.objectViewer` on a bucket. Can they list the
   contents of the bucket? Can they download objects? Can they delete objects?
4. A partner company needs to download a file from your private bucket without
   creating a Google account. What approach would you use and why?
5. What is the purpose of object versioning, and why should you configure a
   lifecycle policy alongside it?

---

## Cleanup

```bash
# Delete all objects and buckets
gcloud storage rm -r gs://$BUCKET_MAIN --quiet
gcloud storage rm -r gs://$BUCKET_ARCHIVE --quiet

# Delete Pub/Sub resources
gcloud pubsub subscriptions delete storage-events-sub
gcloud pubsub topics delete storage-events

# Delete service account
gcloud iam service-accounts delete $SIGNER_SA --quiet
```

---

## Part 9 — Challenge Exercise

### Challenge 1: Locked Retention Policy

Simulate a compliance retention scenario by applying and then locking a
retention policy on a test bucket.

1. Create a new bucket and set a 60-second retention policy (short duration for
   testing purposes):

```bash
export BUCKET_RETAIN="cis4329-retain-$(gcloud config get-value project)"
gcloud storage buckets create gs://$BUCKET_RETAIN \
  --location=us-central1 \
  --default-storage-class=STANDARD

gcloud storage buckets update gs://$BUCKET_RETAIN \
  --retention-period=60s
```

1. Upload a test object and attempt to delete it within 60 seconds — observe
   the error:

```bash
echo "compliance record" | gcloud storage cp - gs://$BUCKET_RETAIN/record.txt
gcloud storage rm gs://$BUCKET_RETAIN/record.txt
```

1. Wait 65 seconds, then delete successfully:

```bash
sleep 65
gcloud storage rm gs://$BUCKET_RETAIN/record.txt
echo "Deleted after retention period elapsed"
```

1. Clean up the test bucket:

```bash
gcloud storage rm -r gs://$BUCKET_RETAIN --quiet
```

### Challenge 2: Cross-Bucket Replication with Storage Transfer Service

Set up a one-time Storage Transfer Service job to copy all objects from your
main lab bucket to the archive bucket, preserving metadata.

1. In the Cloud Console, navigate to **Storage Transfer Service**.
1. Click **Create transfer job** and select **Cloud Storage** as both the source
   and destination.
1. Set the source bucket to `$BUCKET_MAIN` and the destination to
   `$BUCKET_ARCHIVE`.
1. Set the schedule to **Run once** and enable **Delete objects from destination
   if they don't exist in source** to observe the sync behavior.
1. Start the job and monitor its progress in the Transfer Jobs list. Record the
   number of objects transferred and total bytes copied.

### Reflection Questions

1. You attempted to delete an object inside its retention period and received an
   error. What would happen if you tried to lock the retention policy
   permanently? What is the key operational risk of locking a retention policy,
   and under what real-world scenario would locking be required?
2. The Storage Transfer Service job you created was configured to delete objects
   from the destination that do not exist in the source. How does this differ
   from a simple copy, and what use case does this deletion behavior serve?

---

End of Lab — Module 04

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash
