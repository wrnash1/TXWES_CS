# Lab — Module 03

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Compute Engine — VM Creation, Startup Scripts, Snapshots, and Custom Images

### Points: 100

---

## Lab Overview

In this lab you will create Compute Engine VM instances using both the Google Cloud Console and the gcloud CLI, deploy a web server using a startup script, take a persistent disk snapshot, and create a custom image. These skills are foundational for the ACE exam and for real-world GCP administration.

All tasks use Cloud Shell unless otherwise noted. Complete this lab in your `txwes-gcp-lab-[your initials]` project.

Estimated completion time: 75–90 minutes.

---

## Prerequisites

- Module 01 and 02 labs completed
- Compute Engine API enabled:

```bash
gcloud services enable compute.googleapis.com
```

- Default region and zone configured:

```bash
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a
```

---

## Part 1: Create a VM via Console (15 points)

### Task 1.1 — Create a VM Using the Console (15 points)

1. Navigate to Compute Engine > VM Instances in the Console.
2. Click Create Instance.
3. Set the following values:

   - Name: `console-vm-[your initials]`
   - Region: `us-central1`
   - Zone: `us-central1-a`
   - Machine family: General-purpose
   - Series: E2
   - Machine type: `e2-micro`
   - Boot disk: Debian GNU/Linux 11 (Bullseye), Standard persistent disk, 10 GB

4. Expand "Advanced options" > "Security" and verify a service account is listed.
5. Leave all other settings at default.
6. Click Create.

Wait for the VM to show status "Running" (green checkmark).

Deliverable: Screenshot of the VM Instances page showing `console-vm-[your initials]` with status RUNNING. Label it "Task 1.1".

---

## Part 2: Create a VM via gcloud CLI with Startup Script (25 points)

### Task 2.1 — Create a Web Server VM with Startup Script (15 points)

Open Cloud Shell and run the following command. This creates a VM and uses a startup script to install and configure Nginx:

```bash
gcloud compute instances create web-server-1 \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --tags=http-server \
  --metadata=startup-script='#!/bin/bash
apt-get update
apt-get install -y nginx
echo "Hello from Texas Wesleyan - $(hostname)" > /var/www/html/index.html
systemctl enable nginx
systemctl start nginx'
```

Wait about 60 seconds for the startup script to complete, then confirm the VM is running:

```bash
gcloud compute instances list
```

Deliverable: Screenshot of `gcloud compute instances list` showing `web-server-1` with status RUNNING. Label it "Task 2.1".

### Task 2.2 — Create a Firewall Rule and Test the Web Server (10 points)

Create a firewall rule to allow HTTP traffic to VMs tagged `http-server`:

```bash
gcloud compute firewall-rules create allow-http-lab \
  --direction=INGRESS \
  --priority=1000 \
  --network=default \
  --action=ALLOW \
  --rules=tcp:80 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=http-server
```

Get the external IP address of your web server:

```bash
gcloud compute instances describe web-server-1 \
  --zone=us-central1-a \
  --format="get(networkInterfaces[0].accessConfigs[0].natIP)"
```

Open a browser tab and navigate to `http://EXTERNAL_IP`. You should see the "Hello from Texas Wesleyan" message.

Deliverable: Screenshot of the browser showing the web server response. Label it "Task 2.2".

---

## Part 3: Manage Compute Engine Instances (15 points)

### Task 3.1 — List and Filter VMs (5 points)

List all VMs in your project:

```bash
gcloud compute instances list
```

List only running VMs:

```bash
gcloud compute instances list --filter="status=RUNNING"
```

List VMs in a specific zone:

```bash
gcloud compute instances list --filter="zone:(us-central1-a)"
```

Deliverable: Screenshot of the zone-filtered list output. Label it "Task 3.1".

### Task 3.2 — Stop and Start a VM (5 points)

Stop the `console-vm` you created in Task 1.1:

```bash
gcloud compute instances stop console-vm-[your initials] --zone=us-central1-a
```

Wait for the stop to complete, then list instances again to confirm it shows TERMINATED status:

```bash
gcloud compute instances list
```

Restart the VM:

```bash
gcloud compute instances start console-vm-[your initials] --zone=us-central1-a
```

Confirm it returns to RUNNING:

```bash
gcloud compute instances list
```

Deliverable: Screenshot showing the instance returning to RUNNING status. Label it "Task 3.2".

### Task 3.3 — SSH into a VM (5 points)

SSH into your `web-server-1` instance:

```bash
gcloud compute ssh web-server-1 --zone=us-central1-a
```

Once inside the VM, check that Nginx is running:

```bash
systemctl status nginx
```

Exit the SSH session:

```bash
exit
```

Deliverable: Screenshot of the `systemctl status nginx` output from inside the VM. Label it "Task 3.3".

---

## Part 4: Snapshots and Custom Images (30 points)

### Task 4.1 — Take a Snapshot of a Persistent Disk (15 points)

First, stop `web-server-1` to take a consistent snapshot:

```bash
gcloud compute instances stop web-server-1 --zone=us-central1-a
```

Create a snapshot of its boot disk. In GCP, a VM's boot disk has the same name as the VM by default:

```bash
gcloud compute disks snapshot web-server-1 \
  --snapshot-names=web-server-1-snap-$(date +%Y%m%d) \
  --zone=us-central1-a
```

List snapshots to confirm creation:

```bash
gcloud compute snapshots list
```

Restart the VM after snapshotting:

```bash
gcloud compute instances start web-server-1 --zone=us-central1-a
```

Deliverable: Screenshot of `gcloud compute snapshots list` showing your snapshot. Label it "Task 4.1".

### Task 4.2 — Create a Custom Image (15 points)

Stop `web-server-1` again so the disk is in a clean state for imaging:

```bash
gcloud compute instances stop web-server-1 --zone=us-central1-a
```

Create a custom image from the boot disk:

```bash
gcloud compute images create txwes-nginx-image \
  --source-disk=web-server-1 \
  --source-disk-zone=us-central1-a \
  --family=txwes-web \
  --description="Nginx web server image for Texas Wesleyan labs"
```

Verify the image was created:

```bash
gcloud compute images list --filter="family:txwes-web"
```

Restart the VM:

```bash
gcloud compute instances start web-server-1 --zone=us-central1-a
```

Deliverable: Screenshot of `gcloud compute images list` output showing your `txwes-nginx-image`. Label it "Task 4.2".

---

## Part 5: Deploy a VM from Custom Image (10 points)

### Task 5.1 — Create a New VM Using Your Custom Image (10 points)

Create a new VM using the custom image you built:

```bash
gcloud compute instances create web-server-2 \
  --zone=us-central1-b \
  --machine-type=e2-micro \
  --image=txwes-nginx-image \
  --image-project=$GOOGLE_CLOUD_PROJECT \
  --tags=http-server
```

Note: this VM is in zone `us-central1-b` — a different zone than the original. This demonstrates that custom images are portable across zones.

Get the external IP of the new VM:

```bash
gcloud compute instances describe web-server-2 \
  --zone=us-central1-b \
  --format="get(networkInterfaces[0].accessConfigs[0].natIP)"
```

Open a browser and navigate to `http://EXTERNAL_IP`. The page should load because Nginx was baked into the image — no startup script needed.

Deliverable: Screenshot of the browser showing the Nginx page from `web-server-2`. Label it "Task 5.1".

---

## Cleanup (5 points)

Delete all VMs created in this lab to stop charges:

```bash
gcloud compute instances delete web-server-1 --zone=us-central1-a --quiet
gcloud compute instances delete web-server-2 --zone=us-central1-b --quiet
gcloud compute instances delete console-vm-[your initials] --zone=us-central1-a --quiet
```

Delete the firewall rule:

```bash
gcloud compute firewall-rules delete allow-http-lab --quiet
```

Deliverable: Screenshot of `gcloud compute instances list` showing no instances. Label it "Cleanup".

Note: Keep the snapshot and custom image — they will be referenced in reflection questions.

---

## Reflection Questions

Answer in your submission document (2–4 sentences each):

1. In Task 4.2, you stopped the VM before creating a custom image. Why is it best practice to stop the VM before imaging?
2. In Task 5.1, the new VM from the custom image already had Nginx installed without running a startup script. Explain the advantage this provides over using a startup script for fleet deployments.
3. If you needed to run 20 identical copies of `web-server-2` and automatically replace any that became unhealthy, which GCP feature would you use and how does it use your custom image?

---

## Grading Rubric

| Task | Points | Criteria |
|---|---|---|
| 1.1 Console VM created and running | 15 | Screenshot shows VM with RUNNING status |
| 2.1 gcloud VM created with startup script | 15 | instances list shows web-server-1 RUNNING |
| 2.2 Firewall rule and browser test | 10 | Browser screenshot shows Hello from Texas Wesleyan |
| 3.1 List and filter VMs | 5 | Filtered list output shown |
| 3.2 Stop and start VM confirmed | 5 | RUNNING status confirmed after restart |
| 3.3 SSH and nginx status | 5 | systemctl status nginx output visible |
| 4.1 Snapshot created and listed | 15 | Snapshot in list with correct name |
| 4.2 Custom image created and listed | 15 | txwes-nginx-image in images list |
| 5.1 New VM from custom image works | 10 | Browser shows Nginx page from web-server-2 |
| Cleanup | 5 | Empty instances list shown |
| Total | 100 | |

---

End of Lab — Module 03

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
