# Video Script — Module 01, Part 2

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Console Navigation, Cloud Shell, and gcloud CLI

### Estimated Duration: 10–12 minutes

---

## Introduction to Part 2

Welcome back. In Part 1 we covered GCP's global infrastructure — regions, zones — and the four-level resource hierarchy: Organization, Folders, Projects, and Resources. Now in Part 2 we are going to make this hands-on. We will tour the Google Cloud Console, learn how Cloud Shell works, and execute our first gcloud CLI commands. Everything in this section maps directly to tasks you will perform in this week's lab.

---

## Section 1: Touring the Google Cloud Console

**[SHOW CONSOLE: Open console.cloud.google.com in a browser, logged in to a GCP account]**

This is the Google Cloud Console. It is the web-based graphical interface for managing every GCP service. Let me walk you through the key navigation elements.

At the very top left you see the hamburger menu — three horizontal lines. Click that and a left sidebar expands showing every major service category: Compute, Storage, Networking, Big Data, AI and Machine Learning, Security, and more. You will spend a lot of time in this menu.

Next to the hamburger menu is the project selector. It shows your currently active project. Click it and you get a dialog where you can switch between projects, search for a project by name or ID, or create a new project. Always check which project is selected before you create a resource — creating a VM in the wrong project is one of the most common beginner mistakes.

**[SHOW CONSOLE: Click the project selector, show the project list dialog]**

At the top right you have the Cloud Shell button — the small terminal icon that looks like `>_`. Next to that is the notifications bell, and then your user account avatar. The search bar at the top center lets you search for any service, resource, or documentation page across all of GCP.

On the main landing page — called the Console Home — you see a dashboard with widgets showing your recent projects, billing summary, and quick-access links to documentation. You can customize this dashboard by adding or removing cards.

**[SHOW CONSOLE: Navigate to Navigation Menu > Compute Engine > VM Instances]**

Let me show you how to navigate to a specific service. Click the hamburger menu, scroll to Compute, and click Compute Engine. The sub-menu expands to show VM Instances, Instance Templates, Instance Groups, Disks, Images, and more. This pattern is consistent across all services — click the parent category to expand its sub-services.

---

## Section 2: Cloud Shell

**[SHOW CONSOLE: Click the Cloud Shell button in the top-right corner of the Console]**

Cloud Shell is one of the most useful features of the Google Cloud Console, and it is completely free. When you click this button, GCP provisions a small Linux virtual machine — an `e2-micro` instance — running Debian. This VM comes pre-installed with the gcloud CLI, kubectl, Docker, Python, Node.js, Java, Go, and Terraform. It is automatically authenticated to your Google account, so you do not need to run `gcloud auth login` before using it.

**[SHOW CONSOLE: Cloud Shell terminal appears at the bottom of the browser]**

The Cloud Shell terminal opens at the bottom of your browser window. You can also pop it out into a full browser tab using the expand icon. Notice the toolbar at the top of the Cloud Shell pane — it has buttons to open a file editor, transfer files, and customize the terminal.

Here are the key facts about Cloud Shell for the ACE exam:

- Cloud Shell gives you a persistent 5 GB home directory stored in Cloud Storage. Your files there survive between sessions.
- The Cloud Shell VM itself is ephemeral — it is recycled after 20 minutes of inactivity. Any files outside your home directory are lost.
- Cloud Shell is automatically authorized to your account for the project selected in the Console.
- Cloud Shell has an integrated web preview feature on port 8080 that lets you test web applications running inside Cloud Shell.

---

## Section 3: The gcloud CLI — Core Commands

**[SHOW CONSOLE: Cloud Shell terminal with gcloud commands being typed]**

Now let's run some commands. The gcloud CLI is organized in a verb-noun pattern: `gcloud [service-group] [resource-type] [action] [flags]`. Let me demonstrate the most important commands for this module.

First, check your current configuration:

```bash
gcloud config list
```

This prints your active account, active project, default compute region, and default compute zone. You will use this constantly to verify you are working in the right context before creating resources.

List all projects your account can access:

```bash
gcloud projects list
```

This returns project IDs, project numbers, and project names. If you have many projects, add `--format="table(projectId,name,projectNumber)"` to get a clean table output.

Set your active project:

```bash
gcloud config set project YOUR_PROJECT_ID
```

Set your default compute zone:

```bash
gcloud config set compute/zone us-central1-a
```

Set your default compute region:

```bash
gcloud config set compute/region us-central1
```

List all GCP regions:

```bash
gcloud compute regions list
```

List all zones:

```bash
gcloud compute zones list
```

Filter to only zones in a specific region:

```bash
gcloud compute zones list --filter="region:(us-central1)"
```

**[SHOW CONSOLE: Each command being typed and its output shown]**

Notice the output format. By default gcloud returns human-readable table output. You can change this with `--format=json`, `--format=yaml`, or `--format=csv` flags. For scripting and automation, JSON output is most useful because it can be piped into tools like `jq`.

---

## Section 4: Named Configurations and Multiple Projects

**[SHOW SLIDE: Diagram showing three named gcloud configurations — dev, staging, prod — each with different project and zone settings]**

As you work with GCP professionally, you will often need to switch between multiple projects — development, staging, production. The gcloud CLI supports named configurations to make this easy.

Create a new named configuration:

```bash
gcloud config configurations create staging
```

Activate a named configuration:

```bash
gcloud config configurations activate staging
```

List all configurations:

```bash
gcloud config configurations list
```

Each named configuration can store its own account, project, region, and zone settings. When you run `gcloud config configurations activate prod`, all subsequent gcloud commands use the prod project and settings automatically. This is much safer than manually running `gcloud config set project` and risking working in the wrong project.

---

## Section 5: Getting Help

**[SHOW CONSOLE: Running gcloud help and gcloud compute instances --help]**

One final skill before the lab: getting help from within gcloud itself. Every gcloud command supports the `--help` flag:

```bash
gcloud compute instances create --help
```

This prints the full documentation for that command including all flags, their types, default values, and examples — all without leaving your terminal. You can also run:

```bash
gcloud help
```

for top-level help, or:

```bash
gcloud cheat-sheet
```

for a quick reference of the most commonly used commands. On the ACE exam you will not have access to these help commands, so practice the most important patterns until they are familiar.

---

## Module 01 Summary

**[SHOW SLIDE: Summary bullet list]**

Let's bring together everything from both parts of Module 01. GCP organizes its global infrastructure into Regions and Zones. The resource hierarchy flows from Organization down through Folders to Projects to Resources, with IAM policies inheriting additively downward. Billing Accounts attach at the Project level. Budget alerts are notifications only and do not stop resources. Organization Policies govern what actions are permitted regardless of IAM grants.

The Google Cloud Console provides a graphical interface for all services. Cloud Shell is a free, browser-based Linux VM pre-authenticated to your account with a persistent 5 GB home directory. The gcloud CLI uses a verb-noun command structure, supports named configurations for multi-project work, and every command has built-in help via `--help`.

Complete this week's lab to practice these commands hands-on. Then take the quiz and post to the discussion board. I will see you in Module 02, where we dive into Identity and Access Management in depth.

---

End of Part 2 — Module 01

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
