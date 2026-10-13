# Video Script: CIS-4329 Google Cloud Infrastructure Architecture
## Module 03: Compute Engine Automation & Startup Script Architecture (Part 3)
### Recorded by Professor Nash | Texas Wesleyan University

**Runtime:** 21:15 minutes  
**Target Certification Domain:** Google Cloud Associate Cloud Engineer (ACE) — Section 2.1 (Configure Compute Engine instances) and Section 3.1 (Managing Compute Engine resources)

---

## [00:00 - 04:00] Part 1: Automated Instance Initialization Architecture

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / Andrew Brown &bull; Google Cloud Associate Cloud Engineer &bull; Module 03</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=UGRDM86MBIQ" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/UGRDM86MBIQ" title="freeCodeCamp / Andrew Brown &bull; Google Cloud Associate Cloud Engineer" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp / Andrew Brown &bull; Google Cloud Associate Cloud Engineer</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**[CAMERA: Cut to instructor workbench with Google Cloud Architecture diagram]**

"Welcome back to CIS-4329 Google Cloud. In Parts 1 and 2 of Module 03, we covered Google Kubernetes Engine (GKE), container orchestration, and cluster sizing. Now in Part 3, we address a foundational infrastructure pattern: automated compute provisioning and startup script lifecycle orchestration.

In modern cloud engineering, manual SSH access into individual virtual machines to install web servers, configure agents, or deploy code is an anti-pattern. VMs in cloud environments should be treated as cattle, not pets — they must be fully automated, ephemeral, and capable of bootstrapping themselves into a functional state upon launch.

Google Compute Engine provides this capability through **instance metadata** and **startup scripts**. Today, we will use the `gcloud` CLI in Cloud Shell to programmatically provision an automated Nginx web server, configure network tags, and establish least-privilege ingress firewall policies."

---

## [04:00 - 10:00] Part 2: Dissecting `gcloud compute instances create` and Metadata
**[SHOW SCREEN: Displaying the complete `gcloud compute instances create` syntax]**

"Let's break down the command we will execute in Google Cloud Shell:

```bash
gcloud compute instances create www-server-1 \
    --zone=us-central1-a \
    --machine-type=e2-micro \
    --tags=http-server \
    --metadata=startup-script='#! /bin/bash
    apt-get update
    apt-get install -y nginx
    echo "<h1>Texas Wesleyan University &bull; CIS-4329 Google Cloud</h1><p>Automated Nginx Deployment Verified via Compute Engine Startup Script.</p>" > /var/www/html/index.html'
```

Notice the critical architectural flags:
1. `--zone=us-central1-a`: Pins the VM to a specific zonal failure domain within the `us-central1` Iowa region.
2. `--machine-type=e2-micro`: Selects a cost-effective, shared-core cost tier suitable for testing without exhausting billing credits.
3. `--tags=http-server`: Attaches a network tag to the instance's virtual network interface (vNIC). In Google Cloud VPCs, firewall rules target network tags rather than IP addresses, allowing dynamic, decoupled security enforcement.
4. `--metadata=startup-script`: Injects an automated bash script into the instance metadata server (`http://metadata.google.internal/computeMetadata/v1/`). The Google guest environment daemon executes this script as `root` every time the instance boots."

---

## [10:00 - 15:30] Part 3: VPC Firewall Rules & Security Architecture
**[SHOW SCREEN: Creating the VPC Ingress Firewall Rule]**

"By default, Google Cloud VPC networks deny all unsolicited external ingress traffic. Even though Nginx is actively listening on port 80, external packets will be dropped at the VPC boundary until we explicitly define an ingress firewall rule.

Let's execute the firewall creation command:
```bash
gcloud compute firewall-rules create allow-http \
    --direction=INGRESS \
    --priority=1000 \
    --network=default \
    --action=ALLOW \
    --rules=tcp:80 \
    --source-ranges=0.0.0.0/0 \
    --target-tags=http-server
```

Why is `--target-tags=http-server` essential? If we omitted `--target-tags`, this firewall rule would open port 80 to *every* virtual machine on the default VPC network, violating the principle of least privilege. By binding the rule to the `http-server` tag, only instances carrying that tag allow port 80 ingress."

---

## [15:30 - 21:15] Part 4: Verification, Inspection, and Lab Deliverables
**[SHOW SCREEN: Inspecting the running instance and testing in web browser]**

"Let's retrieve our instance's public IP address via the CLI:
```bash
gcloud compute instances list --filter="name=www-server-1" --format="get(networkInterfaces[0].accessConfigs[0].natIP)"
```

Copy that public IP address, open a new browser tab, and paste it in using `http://<EXTERNAL_IP>`.

You will see:
`Texas Wesleyan University • CIS-4329 Google Cloud — Automated Nginx Deployment Verified.`

To inspect the execution logs of the startup script on the VM itself, you can view the serial console or run:
```bash
sudo journalctl -u google-startup-scripts.service
```

**Your Module 03 Deliverable:**
1. Execute the provisioning and firewall commands in your Cloud Shell terminal.
2. Verify the web page loads in your browser.
3. Take a screenshot showing both your terminal output and your browser displaying the Texas Wesleyan Nginx confirmation page.
4. Submit the screenshot and your instance verification log to Canvas.

In Module 04, we will take these single instances and scale them across multiple zones using Managed Instance Groups (MIGs) and Cloud Load Balancing. See you then!"
