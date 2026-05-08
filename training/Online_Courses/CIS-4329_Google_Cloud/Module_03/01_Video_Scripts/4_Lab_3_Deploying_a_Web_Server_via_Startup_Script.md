### 4. Lab 3: Deploying a Web Server via Startup Script
**Objective:** Automate the provisioning of an Nginx web server using Compute Engine startup scripts.
**Instructions:**
1. Open Cloud Shell in your GCP project.
2. We will use the `gcloud` CLI to create a VM and pass it a script to install Nginx.
3. Run the following command:
   ```bash
   gcloud compute instances create www-server-1 \
   --zone=us-central1-a \
   --machine-type=e2-micro \
   --tags=http-server \
   --metadata=startup-script='#! /bin/bash
   apt-get update
   apt-get install -y nginx
   echo "Hello from Texas Wesleyan" > /var/www/html/index.html'
   ```
4. Now, create a firewall rule to allow HTTP traffic to VMs with the `http-server` tag:
   ```bash
   gcloud compute firewall-rules create allow-http \
   --direction=INGRESS --priority=1000 --network=default --action=ALLOW \
   --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server
   ```
5. Navigate to Compute Engine in the console, find your VM's External IP, and paste it into a web browser.
**Deliverable:** Take a screenshot of your web browser displaying the "Hello from Texas Wesleyan" page. Submit to Blackboard.

---
