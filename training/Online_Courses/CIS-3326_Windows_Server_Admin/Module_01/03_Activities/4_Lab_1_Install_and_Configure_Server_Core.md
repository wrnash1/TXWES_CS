### 4. Lab 1: Install and Configure Server Core
**Objective:** Deploy Windows Server 2022 Core and configure its identity.
**Instructions:**
1. Deploy a new VM in VirtualBox using the Windows Server 2022 Evaluation ISO.
2. During setup, specifically select **Windows Server 2022 Standard (Server Core)** (Do NOT select Desktop Experience).
3. Once logged in (default Administrator password), type `sconfig` and press Enter.
4. Change the Computer Name to `SRV-CORE-01`. (It will require a reboot).
5. Open `sconfig` again. Go to Network Settings and assign a static IP of `192.168.10.10` with a `/24` subnet mask.
**Deliverable:** Take a screenshot of your `sconfig` screen showing the new Computer Name and Static IP address. Submit to Blackboard.

---
