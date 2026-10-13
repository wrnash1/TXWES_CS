# Video Script: Module 04 — Cloud Storage (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Recap and Agenda (1 minute)

Welcome back. In Part 1 we covered storage classes, bucket configuration,
lifecycle policies, and access control fundamentals. In Part 2 we cover:

- Signed URLs for time-limited access
- Object versioning
- Pub/Sub notifications for object events
- Data transfer options
- Console and gcloud CLI walkthrough
- ACE exam strategy

---

## Segment 2 — Signed URLs (3 minutes)

### What is a Signed URL?

A signed URL is a time-limited URL that grants access to a specific Cloud
Storage object without requiring the user to have a Google account or any
IAM permissions.

Use cases:

- Allow a customer to download a file for 15 minutes after purchase
- Allow a third-party service to upload a file to your bucket
- Grant temporary read access to a private object

### How Signed URLs Work

1. Your server (or Cloud Function) generates a signed URL using your service
   account's private key or via the IAM signing API.
2. The signed URL includes the object path, expiration time, and a cryptographic
   signature.
3. You give the signed URL to the client.
4. The client uses the URL to access the object directly. No GCP credentials
   required.
5. After the expiration time, the URL is invalid.

### Generating a Signed URL

```bash
# Sign a URL using the service account attached to your environment
gcloud storage sign-url gs://BUCKET_NAME/OBJECT_NAME \
  --duration=15m \
  --region=us-central1

# For a service account key file (legacy method)
gsutil signurl -d 15m -r us-central1 \
  key.json gs://BUCKET_NAME/OBJECT_NAME
```

**ACE Exam Tip:** Signed URLs are the correct answer when a question asks how
to grant temporary access to a single object for an unauthenticated user or
an external party. They are not a substitute for IAM when you need persistent
access control.

---

## Segment 3 — Object Versioning (2 minutes)

### Enabling Versioning

When versioning is enabled on a bucket, Cloud Storage retains previous
versions of objects when they are overwritten or deleted. Instead of being
permanently destroyed, the old version becomes a **noncurrent** version.

```bash
# Enable versioning on a bucket
gcloud storage buckets update gs://BUCKET_NAME \
  --versioning

# Check versioning status
gcloud storage buckets describe gs://BUCKET_NAME \
  --format='value(versioning)'

# List all versions of objects in a bucket
gcloud storage ls -a gs://BUCKET_NAME/

# Delete a specific version
gcloud storage rm gs://BUCKET_NAME/OBJECT_NAME#GENERATION_NUMBER
```

### Versioning and Lifecycle Policies

Versioning and lifecycle policies work together. A common pattern:

- Keep the 3 most recent versions of each object (condition: `numNewerVersions: 3`)
- Automatically delete noncurrent versions older than 30 days

This prevents unbounded storage cost growth from versioning.

---

## Segment 4 — Pub/Sub Notifications (2 minutes)

### Cloud Storage Pub/Sub Integration

Cloud Storage can publish notifications to a Pub/Sub topic when objects are
created, deleted, modified, or when their metadata changes. This enables
event-driven architectures.

```bash
# Grant Cloud Storage permission to publish to a Pub/Sub topic
BUCKET_SA=$(gcloud storage service-agent --project=$PROJECT_ID)
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$BUCKET_SA" \
  --role=roles/pubsub.publisher

# Create a Pub/Sub topic
gcloud pubsub topics create storage-events

# Create a notification on the bucket
gcloud storage buckets notifications create gs://BUCKET_NAME \
  --topic=storage-events \
  --event-types=OBJECT_FINALIZE,OBJECT_DELETE

# List notifications on a bucket
gcloud storage buckets notifications list gs://BUCKET_NAME
```

Event types:

- `OBJECT_FINALIZE` — Object created or overwritten
- `OBJECT_DELETE` — Object deleted
- `OBJECT_ARCHIVE` — Object archived (versioning)
- `OBJECT_METADATA_UPDATE` — Object metadata changed

**ACE Exam Tip:** When a question asks how to trigger a Cloud Function when a
file is uploaded to Cloud Storage, the answer uses either Pub/Sub notifications
or direct Cloud Storage triggers (Eventarc in newer Cloud Functions gen 2).

---

## Segment 5 — Data Transfer Options (2 minutes)

### gcloud storage / gsutil

For small volumes and scripting, use gcloud storage (preferred) or gsutil:

```bash
# Upload a file
gcloud storage cp local-file.txt gs://BUCKET_NAME/

# Upload a directory recursively
gcloud storage cp -r ./local-dir gs://BUCKET_NAME/dir/

# Download
gcloud storage cp gs://BUCKET_NAME/file.txt ./

# Sync a directory (upload new/changed files only)
gcloud storage rsync -r ./local-dir gs://BUCKET_NAME/dir/
```

### Storage Transfer Service

For large-scale transfers from other cloud providers, HTTP sources, or
on-premises systems, use Storage Transfer Service:

- Transfer from AWS S3, Azure Blob Storage, or HTTP URLs
- Schedule recurring transfers
- Supports petabyte-scale transfers
- Preserves metadata during transfer

### Transfer Appliance

For very large on-premises datasets where network transfer is impractical
(petabytes, months of network time), Google provides the Transfer Appliance:

- Physical rack-mounted appliance shipped to your data center
- Load data locally (up to 1 PB per appliance)
- Ship back to Google; Google uploads to Cloud Storage

**ACE Exam Tip:** Know which transfer option to recommend based on data volume
and source. Small data via gcloud storage. Large online transfer from another
cloud via Storage Transfer Service. Petabyte-scale on-premises via Transfer
Appliance.

---

## Segment 6 — Console and gcloud CLI Walkthrough (4 minutes)

### Creating a Bucket in the Console

1. Navigate to **Cloud Storage > Buckets**.
2. Click **Create**.
3. Configure:
   - **Name**: globally unique name (e.g., `cis4329-lab04-yourname`)
   - **Location type**: Regional
   - **Region**: `us-central1`
   - **Default storage class**: Standard
   - **Access control**: Uniform (recommended)
4. Click **Create**.

### Key gcloud Storage Commands

```bash
# Create a bucket
gcloud storage buckets create gs://BUCKET_NAME \
  --location=us-central1 \
  --default-storage-class=STANDARD \
  --uniform-bucket-level-access

# List buckets
gcloud storage buckets list

# Describe a bucket
gcloud storage buckets describe gs://BUCKET_NAME

# Upload an object
gcloud storage cp file.txt gs://BUCKET_NAME/

# List objects in a bucket
gcloud storage ls gs://BUCKET_NAME/

# Download an object
gcloud storage cp gs://BUCKET_NAME/file.txt ./

# Delete an object
gcloud storage rm gs://BUCKET_NAME/file.txt

# Delete a bucket and all its contents
gcloud storage rm -r gs://BUCKET_NAME

# Set a lifecycle policy from a JSON file
gcloud storage buckets update gs://BUCKET_NAME \
  --lifecycle-file=lifecycle.json

# Set the storage class of an existing object
gcloud storage objects update gs://BUCKET_NAME/file.txt \
  --storage-class=NEARLINE

# Grant IAM access on a bucket
gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
  --member=user:alice@example.com \
  --role=roles/storage.objectViewer
```

---

## Segment 7 — ACE Exam Tips for Cloud Storage (1 minute)

Key ACE exam patterns for Module 04:

- **Storage class selection**: Match access frequency to the correct class.
  Know minimum storage durations.
- **Lifecycle policies**: Know the conditions (age, storage class match) and
  actions (SetStorageClass, Delete). Use lifecycle for cost automation.
- **IAM vs. ACLs**: Uniform access (IAM only) is the modern, recommended
  approach. Fine-grained ACLs are legacy.
- **Signed URLs**: Temporary access for unauthenticated users or external
  parties accessing a specific object.
- **Public access**: `allUsers` + `roles/storage.objectViewer` on a bucket
  makes all objects publicly readable.
- **Data transfer**: Storage Transfer Service for large-scale online transfers;
  Transfer Appliance for petabyte-scale offline transfers.
- **Versioning + lifecycle**: Combine them to prevent unbounded storage costs.

---

## Summary — Module 04

Across both parts we covered:

- Cloud Storage fundamentals: buckets, objects, global naming
- Four storage classes and cost trade-offs
- Object lifecycle policies for automated tiering and deletion
- Uniform bucket-level access vs. ACLs
- Signed URLs for time-limited unauthenticated access
- Object versioning and integrating lifecycle policies
- Pub/Sub notifications for event-driven architectures
- Data transfer: gcloud storage, Storage Transfer Service, Transfer Appliance
- Console and gcloud CLI workflows

The lab will have you create buckets, configure lifecycle policies, generate
signed URLs, and set up Pub/Sub notifications.

---

End of Part 2 — Module 04

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/storage/docs
