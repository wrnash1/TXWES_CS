# Video Script — Module 03, Part 2

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Compute Engine — Startup Scripts, Spot VMs, Managed Instance Groups, and gcloud CLI

### Estimated Duration: 11–13 minutes

---

## Introduction to Part 2

Welcome back to Module 03. In Part 1 we covered machine families, disk types, snapshots, and custom images. In Part 2 we go hands-on: startup scripts, pricing models including spot VMs, managed instance groups, and the gcloud compute commands you will use in the lab and on the ACE exam.

---

## Section 1: Startup Scripts

**[SHOW CONSOLE: Create VM instance page, Metadata section with startup-script key highlighted]**

A startup script is a shell script that runs automatically when a Compute Engine VM boots for the first time — or every time it boots, depending on how you configure it. You pass the script using the `metadata` key `startup-script` or by providing a script file stored in Cloud Storage via the `startup-script-url` key.

Startup scripts are useful for bootstrapping a VM — installing packages, configuring software, pulling application code from a repository, or registering the VM with a configuration management system.

Here is a simple startup script that installs Nginx and replaces the default page:

```bash
gcloud compute instances create web-server-1 \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --tags=http-server \
  --metadata=startup-script='#! /bin/bash
apt-get update
apt-get install -y nginx
echo "Hello from Texas Wesleyan" > /var/www/html/index.html
systemctl restart nginx'
```

**[SHOW CONSOLE: gcloud command running in Cloud Shell]**

Notice the `--tags=http-server` flag. Tags are arbitrary labels applied to VMs. Firewall rules can target VMs by their network tags, so this tag tells GCP that this VM should receive HTTP traffic. We will cover VPC firewall rules in Module 05.

A startup script that is too long to pass inline can be stored in Cloud Storage:

```bash
gcloud compute instances create web-server-2 \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --metadata=startup-script-url=gs://my-bucket/startup.sh
```

Startup scripts are powerful but have a limitation: they run every time the VM boots from scratch. If you need software to be available immediately without a boot delay, a custom image is more appropriate. For configuration that needs to be dynamic at boot time — like pulling the latest application code from Git — startup scripts are the right tool.

---

## Section 2: Pricing Models — On-Demand, Committed Use, Spot

**[SHOW SLIDE: Pricing model comparison table with cost and availability columns]**

Compute Engine VMs can be billed in several ways.

### On-Demand

The default billing model. You pay the standard per-second rate for the machine type. No commitment, no risk, full availability.

### Committed Use Discounts (CUDs)

If you know you will need a certain amount of compute capacity for one or three years, you can purchase a commitment and receive a significant discount — up to 57% off for three-year commitments, about 37% for one-year. There are two types:

Resource-based CUDs: you commit to a specific amount of vCPU and memory in a region. Any VM matching those resource specs gets the discount automatically, regardless of machine type.

Spend-based CUDs: you commit to a minimum spend level per hour. Applicable to certain services.

Use committed use discounts for production workloads that run continuously.

### Spot VMs (formerly Preemptible VMs)

**[SHOW SLIDE: Spot VM savings — up to 91% discount with preemption risk shown]**

Spot VMs are the lowest-cost option in Compute Engine. They can be up to 91% cheaper than equivalent on-demand VMs. In exchange, Google can preempt (shut down) your Spot VM at any time, with only a 30-second shutdown notice. Google preempts Spot VMs when it needs the capacity for other customers.

This makes Spot VMs ideal for fault-tolerant, retryable workloads:

- Batch processing jobs
- Video rendering and transcoding
- Machine learning training runs
- Any job that can checkpoint progress and restart from where it left off

Spot VMs are NOT appropriate for:

- Databases
- Web servers that must be continuously available
- Any stateful service where interruption causes data loss or user-facing downtime

**[PAUSE — Professor on camera]**

The ACE exam loves Spot VM questions. The signal in the question is always "fault-tolerant," "retryable," or "batch processing." If you see those words and cost optimization is the goal, the answer is Spot VMs. If the question describes a database, an API server, or anything that cannot be interrupted, Spot VMs are wrong.

---

## Section 3: Managed Instance Groups

**[SHOW SLIDE: MIG architecture — load balancer distributing traffic to multiple identical VMs, autoscaler adjusting count]**

A Managed Instance Group (MIG) is a collection of identical VMs that are managed as a single unit. You define an instance template — a blueprint for what each VM should look like: machine type, disk, image, startup script, network tags, service account. Then you create a MIG using that template.

MIGs give you four important capabilities:

**Autoscaling**: The MIG automatically adds or removes VMs based on CPU utilization, HTTP load balancing capacity, or custom Cloud Monitoring metrics. If traffic spikes at 3 AM, the MIG adds VMs. When traffic drops, it removes them.

**Autohealing**: You define a health check — for example, "is port 80 responding with HTTP 200?" If a VM fails the health check, the MIG automatically replaces it with a new healthy VM. This is self-healing infrastructure.

**Rolling updates**: When you update the instance template (for example, deploying a new application version), the MIG can roll out the update to VMs one batch at a time, keeping most of the fleet running during the update.

**Multi-zone support**: A regional MIG can span multiple zones within a region. If a zone goes down, the MIG automatically redistributes traffic to the surviving zones.

MIGs work together with Cloud Load Balancing — the load balancer distributes traffic to the healthy VMs in the MIG. This combination is the standard architecture for scalable, highly available web applications on GCP.

---

## Section 4: gcloud Compute Commands

**[SHOW CONSOLE: Cloud Shell with gcloud compute commands]**

Here are the gcloud compute commands you will use most in this course:

Create a VM:

```bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --image-family=debian-11 \
  --image-project=debian-cloud
```

List all VMs in the active project:

```bash
gcloud compute instances list
```

Start and stop a VM:

```bash
gcloud compute instances start my-vm --zone=us-central1-a
gcloud compute instances stop my-vm --zone=us-central1-a
```

Delete a VM:

```bash
gcloud compute instances delete my-vm --zone=us-central1-a
```

SSH into a VM:

```bash
gcloud compute ssh my-vm --zone=us-central1-a
```

Take a snapshot of a disk:

```bash
gcloud compute disks snapshot my-vm \
  --snapshot-names=my-vm-snap-$(date +%Y%m%d) \
  --zone=us-central1-a
```

Create a custom image from a disk:

```bash
gcloud compute images create my-golden-image \
  --source-disk=my-vm \
  --source-disk-zone=us-central1-a \
  --family=my-app-images
```

List available public images for Debian:

```bash
gcloud compute images list --filter="family:debian"
```

**[SHOW CONSOLE: Each command running in Cloud Shell with output]**

Pay attention to the `--zone` flag. Almost all `gcloud compute` commands require you to specify a zone. If you set `gcloud config set compute/zone us-central1-a`, that becomes the default and you can omit `--zone` from most commands. But in scripts and automation, always specify the zone explicitly to avoid errors.

---

## Module 03 Summary

**[SHOW SLIDE: Summary bullet list]**

Let's wrap up Module 03. Compute Engine is GCP's IaaS service. Machine families: E2 for general-purpose cost-sensitive workloads, N2 for high-performance general workloads, C2 for compute-intensive tasks, M2 for memory-intensive databases. Disk types: persistent disks survive VM stops; local SSDs are ephemeral. Snapshots are incremental backups for restore. Custom images create golden templates for fleet deployment.

Startup scripts automate VM configuration at boot. Spot VMs are up to 91% cheaper but can be preempted — ideal for fault-tolerant batch workloads. Committed use discounts save up to 57% for 1-3 year compute commitments. Managed Instance Groups provide autoscaling, autohealing, rolling updates, and multi-zone resilience.

Core gcloud commands: `gcloud compute instances create`, `list`, `stop`, `start`, `delete`, `ssh`, `gcloud compute disks snapshot`, `gcloud compute images create`.

Complete the lab, take the quiz, and post to the discussion. In Module 04 we move to Cloud Storage — buckets, storage classes, and lifecycle policies.

---

End of Part 2 — Module 03

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
