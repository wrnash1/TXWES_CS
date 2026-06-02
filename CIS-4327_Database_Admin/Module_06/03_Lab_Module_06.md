# Lab Activity: Module 06 — Firestore and Datastore: Document Databases

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Total Points: 100

---

### Lab Overview

In this lab you will create a Firestore database in Native mode, write and read documents using the gcloud CLI and Firebase REST API, create a composite index, write security rules, and analyze the difference between a transaction and a batch write. These skills are directly tested in the Firestore domain of the GCP Database Engineer exam.

Estimated completion time: 60–75 minutes.

---

### Prerequisites

- Google Cloud student project with billing enabled
- Module 06 video scripts and reading guide reviewed
- Cloud Shell available in the Google Cloud Console

Cost note: Firestore charges per document read, write, and delete. This lab generates a small number of operations and costs less than $0.01.

---

### Part 1 — Create a Firestore Database (15 points)

#### Step 1 — Create the Database in Native Mode

```bash
# Create a Firestore database in Native mode
gcloud firestore databases create \
    --location=us-central \
    --type=firestore-native
```

If a Firestore database already exists in your project, use the existing one.

#### Step 2 — Verify Database Creation

```bash
# List Firestore databases
gcloud firestore databases list
```

**[SHOW CONSOLE: Firestore Console showing the (default) database in Native mode]**

**Deliverable 1 (10 points)**: Take a screenshot of either the gcloud output or the Firestore Console showing the database in Native mode. Save as `lab06_screenshot_01.png`.

**Deliverable 2 (5 points)**: In your lab report, explain in two sentences why you chose Native mode rather than Datastore mode for this lab, referencing at least one feature that Native mode provides.

---

### Part 2 — Write and Read Documents (25 points)

#### Step 3 — Create Documents

Use the Firestore REST API via curl to create documents. First, get an access token:

```bash
ACCESS_TOKEN=$(gcloud auth print-access-token)
PROJECT_ID=$(gcloud config get-value project)
```

Create a product document:

```bash
curl -X POST \
  "https://firestore.googleapis.com/v1/projects/${PROJECT_ID}/databases/(default)/documents/products" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "fields": {
      "productName": {"stringValue": "Wireless Keyboard"},
      "category": {"stringValue": "Electronics"},
      "price": {"doubleValue": 49.99},
      "inStock": {"booleanValue": true},
      "tags": {"arrayValue": {"values": [
        {"stringValue": "wireless"},
        {"stringValue": "bluetooth"}
      ]}}
    }
  }'
```

Create two more product documents (modify the values for variety):

```bash
curl -X POST \
  "https://firestore.googleapis.com/v1/projects/${PROJECT_ID}/databases/(default)/documents/products" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "fields": {
      "productName": {"stringValue": "USB-C Hub"},
      "category": {"stringValue": "Electronics"},
      "price": {"doubleValue": 34.99},
      "inStock": {"booleanValue": true},
      "tags": {"arrayValue": {"values": [
        {"stringValue": "usb"},
        {"stringValue": "connectivity"}
      ]}}
    }
  }'
```

```bash
curl -X POST \
  "https://firestore.googleapis.com/v1/projects/${PROJECT_ID}/databases/(default)/documents/products" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "fields": {
      "productName": {"stringValue": "Desk Lamp"},
      "category": {"stringValue": "Office"},
      "price": {"doubleValue": 24.99},
      "inStock": {"booleanValue": false},
      "tags": {"arrayValue": {"values": [
        {"stringValue": "led"},
        {"stringValue": "adjustable"}
      ]}}
    }
  }'
```

#### Step 4 — Read Documents

```bash
# List all documents in the products collection
curl \
  "https://firestore.googleapis.com/v1/projects/${PROJECT_ID}/databases/(default)/documents/products" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**[SHOW CONSOLE: Firestore Console — Data tab showing the products collection with three documents]**

**Deliverable 3 (15 points)**: Take a screenshot of the Firestore Console showing the products collection with at least three documents visible. Alternatively, show the curl output listing the documents. Save as `lab06_screenshot_02.png`.

In your lab report, answer these two questions about the documents you created.

First: each document has a system-generated ID. How does Firestore's auto-generated document ID differ from a relational database's AUTO_INCREMENT primary key in terms of what the value looks like and how it is generated?

Second: the `tags` field is an array. If you wanted to query all products that have the tag "wireless," what type of Firestore query operator would you use, and what type of index supports it?

**Deliverable 4 (10 points)**: Create a document in a sub-collection. Choose the first product document and add a review sub-collection entry.

```bash
# Get the document ID of the first product (from previous output)
# Replace PRODUCT_DOC_ID with the actual ID from Step 4
PRODUCT_DOC_ID="REPLACE_WITH_ACTUAL_ID"

curl -X POST \
  "https://firestore.googleapis.com/v1/projects/${PROJECT_ID}/databases/(default)/documents/products/${PRODUCT_DOC_ID}/reviews" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "fields": {
      "reviewer": {"stringValue": "Alice Johnson"},
      "rating": {"integerValue": 5},
      "comment": {"stringValue": "Excellent keyboard, very comfortable to type on."},
      "reviewDate": {"timestampValue": "2025-01-15T09:00:00Z"}
    }
  }'
```

Take a screenshot of the Firestore Console showing the product document with its reviews sub-collection. Save as `lab06_screenshot_03.png`.

---

### Part 3 — Composite Index (20 points)

#### Step 5 — Understand Index Requirements

A query filtering by both category and price requires a composite index. Attempt to run such a query through the Firestore Console or confirm the index requirement from the documentation.

**[SHOW CONSOLE: Firestore Console — Indexes tab]**

#### Step 6 — Create a Composite Index

```bash
# Create a composite index via gcloud
gcloud firestore indexes composite create \
    --collection-group=products \
    --field-config field-path=category,order=ASCENDING \
    --field-config field-path=price,order=ASCENDING
```

Wait 1–2 minutes for the index to finish building.

```bash
# List composite indexes
gcloud firestore indexes composite list
```

**Deliverable 5 (15 points)**: Take a screenshot of the gcloud output showing the composite index in READY state. Save as `lab06_screenshot_04.png`.

In your lab report, answer these two questions.

First: why does a query like `category == "Electronics" AND price < 50` require a composite index when single-field queries on category or price alone work without one?

Second: what would happen if you tried to run this multi-field query without the composite index existing? Describe the error behavior and explain how Firestore helps you resolve it.

**Deliverable 6 (5 points)**: In your lab report, explain what an Index Exemption is in Firestore and give one example of a field where you might want to disable automatic indexing.

---

### Part 4 — Security Rules Analysis (20 points)

#### Step 7 — Review and Write Security Rules

**Deliverable 7 (20 points)**: You do not need to deploy rules to your lab project for this deliverable (deploying requires the Firebase CLI). Instead, write the security rules in your lab report.

Write Firestore Security Rules that implement the following access policy for a user profile application.

Policy requirements:

- Unauthenticated users cannot read or write any document.
- An authenticated user can read and update only their own user profile document in the `users` collection, identified by matching `request.auth.uid` to the document ID.
- An authenticated user can create their own profile document if it does not yet exist.
- All authenticated users can read product documents in the `products` collection.
- No client can write to the products collection (write access reserved for server-side only).
- Reviews in a product's sub-collection can be created by any authenticated user.
- A review can only be updated or deleted by the user who created it (the `authorUid` field in the review matches `request.auth.uid`).

In addition to the rules code, write two to three sentences explaining why Security Rules are essential for mobile and web applications that connect directly to Firestore without a backend server layer.

---

### Part 5 — Transactions vs. Batch Writes (20 points)

#### Step 8 — Written Analysis

**Deliverable 8 (20 points)**: In your lab report, write a structured comparison of Firestore transactions and batch writes addressing the following four points.

First: describe the scenario where a transaction is required but a batch write is insufficient. Provide a concrete example using the products or reviews data from this lab.

Second: describe a scenario where a batch write is the correct choice and using a transaction would be unnecessarily complex. Provide a concrete example.

Third: both transactions and batch writes have a 500-document limit. Explain what you would do if your use case requires atomically writing more than 500 documents.

Fourth: explain what happens when two concurrent Firestore transactions attempt to modify the same document simultaneously. Describe Firestore's automatic behavior and what the application must do to handle this.

---

### Lab Submission Checklist

- Deliverable 1 (10 pts) — Native mode database screenshot
- Deliverable 2 (5 pts) — Written justification for Native mode selection
- Deliverable 3 (15 pts) — Products collection screenshot and two written questions answered
- Deliverable 4 (10 pts) — Sub-collection screenshot
- Deliverable 5 (15 pts) — Composite index READY screenshot and two written questions answered
- Deliverable 6 (5 pts) — Written explanation of Index Exemption
- Deliverable 7 (20 pts) — Written Security Rules code and explanation
- Deliverable 8 (20 pts) — Transaction vs. batch write analysis (four points)

---

### Grading Rubric — 100 Points Total

| Deliverable | Points | Criteria |
|---|---|---|
| 1 — Native mode screenshot | 10 | Database shown in Native mode |
| 2 — Mode justification | 5 | Accurate feature reference for Native mode |
| 3 — Products and questions | 15 | Collection screenshot shown; both questions answered accurately |
| 4 — Sub-collection screenshot | 10 | Review document in sub-collection visible |
| 5 — Composite index and questions | 15 | READY index shown; both questions answered accurately |
| 6 — Index Exemption explanation | 5 | Correct definition and valid example |
| 7 — Security Rules | 20 | Valid rules syntax; all policy requirements implemented; explanation accurate |
| 8 — Transaction vs. batch analysis | 20 | All four points addressed with accurate Firestore behavior descriptions |

---

Reference: cloud.google.com/learn
