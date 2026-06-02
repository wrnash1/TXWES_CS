# Lab — Module 01

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: GCP Console Navigation, Project Configuration, and gcloud CLI Fundamentals

### Points: 100

---

## Lab Overview

In this lab you will navigate the Google Cloud Console, create a GCP Project, configure the gcloud CLI using Cloud Shell, and explore regions and zones. These tasks mirror the skills tested on the Google Cloud Associate Cloud Engineer exam and are prerequisites for every subsequent lab in this course.

You will use Cloud Shell exclusively — no local SDK installation is required. All commands are tested against the current version of the gcloud CLI.

Estimated completion time: 60–75 minutes.

---

## Prerequisites

- A Google account with access to Google Cloud (personal or provided by your instructor)
- A web browser (Chrome recommended for Cloud Shell compatibility)
- Access to console.cloud.google.com

---

## Part 1: Console Navigation (20 points)

### Task 1.1 — Log In and Identify the Project Selector (5 points)

1. Open a browser and navigate to console.cloud.google.com.
2. Sign in with your Google account if prompted.
3. Locate the project selector at the top of the page (the dropdown showing a project name or "Select a project").
4. Click the project selector to open the project chooser dialog.
5. Note the columns displayed: Name, ID, and Number.

Deliverable: Take a screenshot of the project chooser dialog showing at least one project listed. Label this screenshot "Task 1.1".

### Task 1.2 — Navigate Console Service Sections (10 points)

Using the Navigation Menu (hamburger icon, top-left), navigate to each of the following sections and take a screenshot of each landing page:

- Compute Engine > VM Instances
- Cloud Storage > Buckets
- IAM and Admin > IAM
- Billing
- APIs and Services > Dashboard

Deliverable: Five screenshots, one per section. Label each "Task 1.2a" through "Task 1.2e".

### Task 1.3 — Console Search (5 points)

1. Click the search bar at the top of the Console.
2. Type "Cloud Shell" and note the results.
3. Search for "us-central1" and note what results appear.

Deliverable: One screenshot of any search result. Label it "Task 1.3".

---

## Part 2: Create a Project (20 points)

### Task 2.1 — Create a New Project via Console (10 points)

1. Click the project selector.
2. Click "New Project" in the top right of the dialog.
3. Set the Project Name to: `txwes-gcp-lab-[your initials]` (example: `txwes-gcp-lab-wn`)
4. Leave the Organization and Location fields at their defaults.
5. Click Create.
6. Wait for the project to be created (watch the notifications bell for a success message).
7. Select your new project using the project selector.

Deliverable: Screenshot of the Console Home showing your new project name in the project selector. Label it "Task 2.1".

### Task 2.2 — Inspect Project Details (10 points)

1. With your new project selected, navigate to IAM and Admin > Settings.
2. Record the Project ID, Project Name, and Project Number.

Deliverable: Screenshot of the IAM and Admin > Settings page showing all three project identifiers. Label it "Task 2.2".

---

## Part 3: Cloud Shell and gcloud Configuration (30 points)

### Task 3.1 — Open Cloud Shell (5 points)

1. Click the Cloud Shell icon (terminal icon) in the top-right of the Console.
2. Wait for Cloud Shell to provision — this may take up to 60 seconds on first use.
3. When the terminal appears at the bottom of the browser, click the "Open in new window" button to expand it to a full tab.

Deliverable: Screenshot of the full Cloud Shell terminal window. Label it "Task 3.1".

### Task 3.2 — Verify Active Configuration (10 points)

Run the following command in Cloud Shell:

```bash
gcloud config list
```

Verify that the output shows:

- Your Google account email under `[core] account`
- Your new project ID under `[core] project`

If the project shown is not your new lab project, run:

```bash
gcloud config set project YOUR_PROJECT_ID
```

Replace `YOUR_PROJECT_ID` with the actual Project ID from Task 2.2.

Run `gcloud config list` again to confirm.

Deliverable: Screenshot of the `gcloud config list` output showing your account and your lab project ID. Label it "Task 3.2".

### Task 3.3 — Set Default Region and Zone (10 points)

Run the following commands to set your default compute region and zone:

```bash
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a
```

Confirm the settings by running:

```bash
gcloud config list
```

Verify that the output now includes:

```text
[compute]
region = us-central1
zone = us-central1-a
```

Deliverable: Screenshot showing the updated `gcloud config list` output with region and zone set. Label it "Task 3.3".

### Task 3.4 — List Projects (5 points)

Run:

```bash
gcloud projects list
```

Note how many projects appear and identify your new lab project in the list.

Deliverable: Screenshot of the `gcloud projects list` output. Label it "Task 3.4".

---

## Part 4: Exploring Regions and Zones (20 points)

### Task 4.1 — List All Regions (5 points)

Run:

```bash
gcloud compute regions list
```

Observe the output. It shows region names, their status (UP or DOWN), and the number of CPUs and disks available in each region under your current quota.

Deliverable: Screenshot of the first 20 lines of output. Label it "Task 4.1".

### Task 4.2 — List Zones in us-central1 (5 points)

Run:

```bash
gcloud compute zones list --filter="region:(us-central1)"
```

This returns only the zones within `us-central1`. Note how many zones exist in this region.

Deliverable: Screenshot of the output. Label it "Task 4.2".

### Task 4.3 — Describe Your Active Region (5 points)

Run:

```bash
gcloud compute regions describe us-central1
```

Review the output. Note the `status` field and the `zones` list embedded in the response.

Deliverable: Screenshot of the output. Label it "Task 4.3".

### Task 4.4 — Named Configuration (5 points)

Create a second named configuration called `lab-alt`:

```bash
gcloud config configurations create lab-alt
```

Set it to use `us-east1` as its region:

```bash
gcloud config set compute/region us-east1
gcloud config set compute/zone us-east1-b
```

List all configurations to confirm both exist:

```bash
gcloud config configurations list
```

Switch back to your default configuration:

```bash
gcloud config configurations activate default
```

Confirm the active configuration returned to `default` by running:

```bash
gcloud config list
```

Deliverable: Screenshot of `gcloud config configurations list` output showing both configurations, and a second screenshot of `gcloud config list` showing you are back on `default`. Label these "Task 4.4a" and "Task 4.4b".

---

## Part 5: Reflection Questions (10 points)

Answer the following questions in your lab submission document (2–4 sentences each):

1. What is the difference between a Project ID and a Project Number? When would you use each one?
2. A classmate says "I set a $50 budget alert on my GCP project, so I know my bill will never exceed $50." What is wrong with this statement?
3. If a folder-level IAM policy grants a user `roles/editor`, can a project administrator inside that folder remove that editor role from the user at the project level? Explain why or why not.
4. You have projects for development, staging, and production. Why would using named gcloud configurations be better than manually running `gcloud config set project` every time you switch contexts?

---

## Submission Instructions

Compile all screenshots and your reflection answers into a single PDF or Word document. Label every screenshot with its task number as specified. Submit via the course LMS by the due date listed in the syllabus.

---

## Grading Rubric

| Task | Points | Criteria |
|---|---|---|
| 1.1 Project selector screenshot | 5 | Screenshot present and shows project list dialog |
| 1.2 Five service section screenshots | 10 | All five sections shown, each labeled correctly |
| 1.3 Console search screenshot | 5 | Screenshot present |
| 2.1 New project created and selected | 10 | Correct project name pattern, shown in selector |
| 2.2 Project identifiers screenshot | 10 | All three identifiers (ID, Name, Number) visible |
| 3.1 Cloud Shell screenshot | 5 | Full Cloud Shell terminal visible |
| 3.2 gcloud config list with correct project | 10 | Account and lab project ID visible in output |
| 3.3 Region and zone configured | 10 | us-central1 and us-central1-a shown in config |
| 3.4 gcloud projects list | 5 | Output shown, lab project identifiable |
| 4.1 Regions list | 5 | Output screenshot present |
| 4.2 Zones filtered to us-central1 | 5 | Correct filter used, correct output shown |
| 4.3 Region describe output | 5 | Output screenshot present |
| 4.4 Named configuration created and restored | 5 | Both configurations visible; default restored |
| Reflection Q1 | 2.5 | Accurate distinction explained |
| Reflection Q2 | 2.5 | Correctly explains budget alerts do not stop resources |
| Reflection Q3 | 2.5 | Correctly explains additive IAM inheritance |
| Reflection Q4 | 2.5 | Explains safety and convenience of named configs |
| Total | 100 | |

---

End of Lab — Module 01

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
