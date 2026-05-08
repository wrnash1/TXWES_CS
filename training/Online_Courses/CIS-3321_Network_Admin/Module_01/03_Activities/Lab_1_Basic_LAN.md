# Lab 1: Building a Basic Virtual LAN
**Course:** CIS 3321 - Network Administration
**Format:** Local Virtualization

## Objective
To understand physical/logical topologies and IP addressing by creating an isolated internal network between two virtual machines using Oracle VirtualBox.

## Prerequisites
*   Oracle VirtualBox installed on your host machine.
*   Two lightweight Linux VMs (e.g., Ubuntu Server or Alpine Linux) imported into VirtualBox.

## Instructions

### Step 1: Configure the Virtual Switch
By default, VirtualBox puts VMs on a NAT network so they can reach the internet. We want to isolate them to simulate a private switch.
1. Open VirtualBox Manager.
2. Right-click **VM_1** and go to **Settings > Network**.
3. Change "Attached to:" from *NAT* to **Internal Network**.
4. Name the network `TxWes_LAN`. Click OK.
5. Repeat this exact process for **VM_2**, ensuring you select the same `TxWes_LAN`.
*Note: By putting both VMs on the same "Internal Network", you have effectively plugged them into the same virtual Star topology switch.*

### Step 2: Assign IP Addresses
Power on both VMs and log in.
1. On **VM_1**, assign an IP address:
   `sudo ip addr add 192.168.1.10/24 dev eth0`
2. On **VM_2**, assign an IP address on the same subnet:
   `sudo ip addr add 192.168.1.20/24 dev eth0`

### Step 3: Verify Connectivity
1. On **VM_1**, attempt to send ICMP Echo Requests to VM_2:
   `ping 192.168.1.20 -c 4`
2. If successful, you should see 4 packets transmitted and 4 received.

## Deliverable
Take a screenshot of the successful `ping` command from VM_1, ensuring the IP addresses of both machines are visible in your terminal window. Submit this screenshot to the Blackboard assignment drop-box.
