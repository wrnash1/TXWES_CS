### 4. Lab 4: Configuring a Basic Host-Based Firewall
**Objective:** Use `ufw` (Uncomplicated Firewall) on Ubuntu to block and allow specific network traffic.
**Instructions:**
1. Boot your Ubuntu Server VM from previous labs.
2. Check the status of the firewall: `sudo ufw status` (It should be inactive).
3. Before enabling the firewall, you must ensure you don't lock yourself out. Allow SSH (Port 22): `sudo ufw allow ssh`
4. Now, enable the firewall: `sudo ufw enable` (Type 'y' to confirm).
5. Deny all incoming HTTP traffic (Port 80): `sudo ufw deny 80/tcp`
6. Check the status again to view the rules: `sudo ufw status verbose`
7. (Optional) From your host machine, attempt to connect to port 80 on the VM to verify it is blocked.
**Deliverable:** Take a screenshot of the output of `sudo ufw status verbose` showing the active rules for SSH (allowed) and Port 80 (denied). Submit to Blackboard.

---
