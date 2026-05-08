# Lab 2: Configuring VLANs in a Virtual Environment
**Course:** CIS 3321 - Network Administration
**Format:** Local Virtualization

## Objective
To understand 802.1Q tagging by configuring virtual LANs (VLANs) on a Linux virtual machine acting as a router/switch.

## Prerequisites
*   Oracle VirtualBox installed.
*   A Linux VM (Ubuntu Server) from Lab 1.

## Instructions

### Step 1: Install VLAN Packages
Log into your Ubuntu VM. You need to install the software required to understand 802.1Q tags.
1. Run: `sudo apt-get update`
2. Run: `sudo apt-get install vlan -y`
3. Load the 802.1Q kernel module: `sudo modprobe 8021q`

### Step 2: Create a VLAN Interface
Assume your primary network interface is `eth0`. We will create a virtual sub-interface that only listens for traffic tagged with VLAN ID 10.
1. Create the VLAN 10 interface:
   `sudo vconfig add eth0 10`
   *(You should see a message confirming the creation of `eth0.10`)*

### Step 3: Assign an IP Address to the VLAN
Now, we must assign an IP address to this specific VLAN interface.
1. Assign IP: `sudo ip addr add 10.0.10.1/24 dev eth0.10`
2. Bring the interface up: `sudo ip link set up eth0.10`

### Step 4: Verification
1. Run the command: `ip addr show`
2. You should see your standard `eth0` interface, AND your new `eth0.10` interface with the `10.0.10.1` IP address assigned to it.
3. This VM is now capable of receiving tagged traffic from a switch trunk port for VLAN 10.

## Deliverable
Take a screenshot of the output of the `ip addr show` command, clearly highlighting the `eth0.10` interface. Submit this screenshot to the Blackboard assignment drop-box.
