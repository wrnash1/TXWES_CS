### 4. Lab 4: Configuring Autoscaling and Load Balancing
**Objective:** Create an Instance Template, deploy a Managed Instance Group, and trigger autoscaling.
**Instructions:**
1. In the GCP Console, go to **Compute Engine -> Instance templates**. Create a template named `web-template`. Under Advanced -> Management, add the Nginx startup script from Lab 3.
2. Go to **Instance groups**. Create a new Managed Instance Group named `web-mig`.
3. Select your `web-template`. Set the minimum instances to 1, and the maximum to 4.
4. Set the Autoscaling metric to `CPU utilization` at `60%`. Create the group.
5. SSH into your single running instance and install a stress testing tool: `sudo apt-get install stress`
6. Run the stress tool to max out the CPU: `stress --cpu 4 --timeout 300`
7. Navigate back to the Instance Groups page and watch as the MIG detects the CPU spike and automatically provisions new VMs to handle the load.
**Deliverable:** Take a screenshot of your Instance Group showing more than 1 instance running as a result of the autoscaling trigger. Submit to Blackboard.

---
