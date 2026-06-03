# Lab: Module 01 — Cloud Computing Fundamentals and GCP Overview

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Lab Overview

In this lab you will create your first Google Cloud project, configure the
gcloud CLI, navigate the Cloud Console, and set up a billing budget alert. These
foundational skills are required for every subsequent lab in this course.

**Estimated Time:** 60 minutes

**Prerequisites:**

- A Google account (personal Gmail or institutional account)
- Access to Google Cloud Console at console.cloud.google.com
- No prior GCP experience required

**Learning Objectives:**

By the end of this lab you will be able to:

1. Create and configure a GCP project
2. Navigate the Google Cloud Console
3. Activate and use Cloud Shell
4. Run essential gcloud CLI commands
5. Configure a billing budget alert
6. Understand the GCP resource hierarchy in practice

---

## Part 1 — Create a GCP Project (15 minutes)

### Step 1.1 — Sign In to the Console

1. Open a browser and navigate to `console.cloud.google.com`.
2. Sign in with your Google account.
3. If prompted, accept the Terms of Service.

### Step 1.2 — Create a New Project

1. Click the project selector dropdown in the top navigation bar. It may show
   "Select a project" or an existing project name.
2. Click **New Project** in the top-right of the dialog.
3. Fill in the following fields:
   - **Project name**: `cis4329-lab01-yourname` (replace `yourname` with your
     last name, e.g., `cis4329-lab01-nash`)
   - **Project ID**: Note the auto-generated ID; you may customize it if desired.
     The Project ID must be globally unique.
   - **Organization**: Leave as-is (or select your institution if available).
   - **Location**: Leave as-is.
4. Click **Create**.
5. Wait for the project to be created (about 10–15 seconds).
6. Select the new project from the project selector dropdown.

### Step 1.3 — Record Project Identifiers

In the Cloud Console, navigate to **IAM & Admin > Settings**. Record the
following for your lab submission:

- Project Name: ______________________
- Project ID: ______________________
- Project Number: ______________________

**Question 1.3:** Which of the three project identifiers is globally unique AND
mutable after creation? (Answer in your lab report.)

---

## Part 2 — Explore the Cloud Console (10 minutes)

### Step 2.1 — Navigation Menu

1. Click the hamburger menu (three horizontal lines) in the top-left.
2. Browse the service categories:
   - Compute
   - Storage
   - Networking
   - Databases
   - Operations
   - IAM & Admin
3. Pin **Compute Engine** and **Cloud Storage** to the top of the navigation
   by clicking the pin icon next to each.

### Step 2.2 — APIs and Services

1. Navigate to **APIs & Services > Library**.
2. Search for "Compute Engine API".
3. Note its current status (enabled or disabled).
4. If disabled, click **Enable**. (You may be prompted to set up billing — do
   this in Part 3 if needed.)

### Step 2.3 — Dashboard Customization

1. Return to the main Dashboard by clicking the Google Cloud logo.
2. Click **Customize** on the Dashboard.
3. Add the **Billing** card if it is not already present.
4. Take note of the current estimated charges (should be $0.00 for a new project).

---

## Part 3 — Set Up Cloud Billing (10 minutes)

### Step 3.1 — Link a Billing Account

If your project does not already have a billing account linked:

1. Navigate to **Billing** in the navigation menu.
2. Click **Link a billing account**.
3. Select an existing billing account or create a new one with a credit card.

Note: GCP offers a free trial with $300 in credits for new accounts. You can
complete all labs in this course within the free tier or using the $300 credit.

### Step 3.2 — Create a Budget Alert

1. Navigate to **Billing > Budgets & alerts**.
2. Click **Create budget**.
3. Fill in:
   - **Name**: `lab01-budget`
   - **Projects**: Select your `cis4329-lab01-yourname` project
   - **Budget type**: Specified amount
   - **Target amount**: `$10`
4. Under **Actions**, set three alert thresholds:
   - 50% of budget ($5.00)
   - 90% of budget ($9.00)
   - 100% of budget ($10.00)
5. Ensure **Email alerts to billing admins and users** is checked.
6. Click **Finish**.

**Question 3.2:** What happens to your running resources when spending crosses
the 100% threshold? (Answer in your lab report.)

---

## Part 4 — Cloud Shell and gcloud CLI (20 minutes)

### Step 4.1 — Activate Cloud Shell

1. Click the **Cloud Shell** icon in the top-right of the Console toolbar
   (looks like `>_`).
2. A terminal panel opens at the bottom of the browser. Wait for it to
   initialize (up to 30 seconds on first use).
3. Confirm you see a prompt like `student@cloudshell:~ (your-project-id)$`.

### Step 4.2 — Verify Authentication and Configuration

Run these commands and record the output:

```bash
# Check your active account
gcloud auth list

# Check your current configuration
gcloud config list

# Verify the active project
gcloud config get-value project
```

### Step 4.3 — Set Default Region and Zone

```bash
# Set default region
gcloud config set compute/region us-central1

# Set default zone
gcloud config set compute/zone us-central1-a

# Confirm settings
gcloud config list
```

### Step 4.4 — Explore Projects

```bash
# List all projects your account can access
gcloud projects list

# Describe your current project
gcloud projects describe $(gcloud config get-value project)
```

Record the output of `gcloud projects describe`. Identify the `projectId`,
`projectNumber`, and `name` fields in the JSON output.

### Step 4.5 — List Available Regions and Zones

```bash
# List all GCP regions
gcloud compute regions list

# List zones in us-central1
gcloud compute zones list --filter="region:us-central1"

# Count total available regions
gcloud compute regions list --format="value(name)" | wc -l
```

**Question 4.5:** How many zones are in the `us-central1` region?

### Step 4.6 — Enable an API via CLI

```bash
# Enable the Cloud Resource Manager API
gcloud services enable cloudresourcemanager.googleapis.com

# List enabled APIs
gcloud services list --enabled --limit=10
```

### Step 4.7 — Explore gcloud Help

```bash
# View top-level help
gcloud help

# View help for the compute group
gcloud compute --help

# View help for a specific subcommand
gcloud compute instances --help
```

### Step 4.8 — Create a Named Configuration

```bash
# Create a new named configuration for this lab
gcloud config configurations create lab01

# Switch back to the default configuration
gcloud config configurations activate default

# List all configurations
gcloud config configurations list
```

---

## Part 5 — Organization Policy Exploration (5 minutes)

### Step 5.1 — View Organization Policies

1. In the Console, navigate to **IAM & Admin > Organization Policies**.
2. If you have an Organization node, browse the available constraints.
3. Search for `compute.requireOsLogin` and review its description.
4. Search for `gcp.resourceLocations` and note what it controls.

If you do not have an Organization node (common with personal accounts), you
can view the policy list via:

```bash
# List available organization policy constraints (requires org access)
gcloud org-policies list-custom-constraints \
  --organization=ORGANIZATION_ID
```

---

## Lab Deliverables

Submit a lab report (PDF or Word) containing:

1. Screenshot of your project Dashboard showing Project ID and Project Number.
2. Screenshot of your budget alert configuration.
3. Output of `gcloud config list` from Cloud Shell.
4. Output of `gcloud projects describe YOUR_PROJECT_ID` showing the full JSON.
5. Output of `gcloud compute zones list --filter="region:us-central1"`.
6. Answers to the following questions:

**Lab Questions:**

1. What is the difference between a Project ID, Project Number, and Project
   Name? Which is mutable after creation?
2. You set a budget alert at $10 with a 100% threshold. Your VM runs for longer
   than expected and you receive an alert email. What happens to your VM?
3. You run `gcloud config set compute/region us-east1`. Does this change affect
   your project's configuration or your local gcloud client configuration?
4. A colleague needs to access all projects in your organization. You want to
   grant the minimum permissions. At what hierarchy level should you grant the
   role, and which role?
5. What is the difference between a sustained use discount and a committed use
   discount?

---

## Cleanup

To avoid any unexpected charges, ensure no paid resources are running:

```bash
# Confirm no compute instances are running
gcloud compute instances list

# If you created any instances, delete them
# gcloud compute instances delete INSTANCE_NAME --zone=ZONE
```

The project itself can remain; the free tier and budget alert protect you.

---

End of Lab — Module 01

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash
