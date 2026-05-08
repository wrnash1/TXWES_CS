### 1. Video Script 4.1: Managed Instance Groups and Autoscaling
**Estimated Duration:** 7 minutes
**Visual:** Instructor on camera.
**Audio:** "Welcome to Module 4. Cloud computing is powerful because it is elastic. You shouldn't pay for 10 web servers at 3:00 AM when nobody is visiting your site. You should pay for 2, and automatically scale up to 10 during the morning rush. In Compute Engine, we achieve this using Managed Instance Groups, or MIGs."
**Visual:** An animated diagram. A load balancer points to a group of 2 VMs. A 'High Traffic' icon appears. The group automatically spawns 3 more identical VMs. The load balancer distributes traffic to all 5.
**[Alt-text: Animation. A Load Balancer distributes traffic to a 'Managed Instance Group' containing 2 VMs. A CPU utilization gauge hits 80%. The group expands, adding 3 new VMs. The Load Balancer now points to all 5 VMs.]**
**Audio:** "A MIG uses an Instance Template—a blueprint of your VM—to automatically stamp out exact clones based on metrics you define, like CPU utilization. If the CPU crosses 80%, the MIG creates more VMs. If the CPU drops below 30%, it deletes them. The MIG also performs health checks; if an application crashes on a VM, the MIG deletes the broken VM and spins up a fresh one automatically. That is self-healing infrastructure."

---
