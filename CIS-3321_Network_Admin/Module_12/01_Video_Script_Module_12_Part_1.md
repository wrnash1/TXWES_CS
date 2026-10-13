# Video Script: Module 12 — Network Virtualization and SDN (Part 1)

## Course: CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

Estimated Runtime: 12–14 minutes

---

### [INTRO]

Welcome to Module 12. This module covers network virtualization and Software-Defined Networking — technologies that have fundamentally changed how enterprise networks are designed, deployed, and managed. These concepts are increasingly prominent in the CompTIA Network+ exam and represent the direction the industry has been moving for the past decade.

By the end of these two videos, you will understand virtual networking components, how hypervisors create virtual machines, what virtual switches do, how network functions are virtualized, and how SDN separates the control plane from the data plane.

---

### [SECTION 1: WHY VIRTUALIZATION MATTERS]

[SHOW DIAGRAM: Traditional data center — one application per server — versus virtualized data center with multiple VMs per physical host]

For most of computing history, one application ran on one physical server. An email server was a box. A file server was a box. A database was a box. This was simple but wasteful. A typical server ran at 5–15% CPU utilization most of the time, but occupied the same rack space, power, and cooling as a fully utilized server.

Virtualization changes this. Virtualization allows multiple operating system instances — called virtual machines (VMs) — to run simultaneously on a single physical host. Each VM believes it has its own dedicated hardware. A single modern server can run 20, 50, or 100 VMs simultaneously, depending on workload.

The benefits:

- Server consolidation: fewer physical machines
- Rapid provisioning: new VMs can be deployed in minutes
- Isolation: VMs are logically isolated from each other even on the same host
- Portability: VMs can be moved between physical hosts (live migration)
- Disaster recovery: VM snapshots and replication enable fast recovery

---

### [SECTION 2: HYPERVISORS — TYPE 1 AND TYPE 2]

[SHOW DIAGRAM: Type 1 hypervisor running directly on hardware with VMs above it; Type 2 hypervisor running inside a host OS]

The software layer that creates and manages VMs is called a hypervisor — also called a Virtual Machine Monitor (VMM).

Type 1 Hypervisor (Bare-Metal Hypervisor) — Runs directly on the physical hardware. There is no host operating system — the hypervisor is the base layer. Examples: VMware ESXi, Microsoft Hyper-V (server version), Citrix Hypervisor (XenServer), KVM (Linux kernel-based). Used in enterprise data centers. Best performance because no intermediate OS overhead.

Type 2 Hypervisor (Hosted Hypervisor) — Runs as an application on top of a host operating system. The host OS runs first, then the hypervisor runs within it. Examples: VMware Workstation, Oracle VirtualBox, Parallels Desktop. Used for development, testing, and labs. Lower performance than Type 1 due to the host OS layer.

For the CompTIA Network+ exam: know the difference between Type 1 (bare-metal, direct hardware access) and Type 2 (hosted, runs on top of an OS), and examples of each.

---

### [SECTION 3: VIRTUAL MACHINES AND VIRTUAL HARDWARE]

[SHOW DIAGRAM: Inside a VM — virtual CPU, virtual RAM, virtual NIC, virtual disk all shown as software components]

Each virtual machine has virtualized versions of physical hardware components:

Virtual CPU (vCPU) — A logical processing unit allocated from the physical CPU. Multiple VMs share physical CPU cores through scheduling.

Virtual RAM — A portion of the physical host's memory allocated to a VM. VMs are isolated from each other's memory.

Virtual NIC (vNIC) — A software-defined network interface card. Each VM has one or more vNICs. The vNIC connects to a virtual switch on the hypervisor.

Virtual Disk (VMDK, VHD) — A file on the host's storage system that appears to the VM as a physical hard drive.

Virtual machine templates and snapshots: A template is a VM image used to rapidly deploy new VMs with a pre-configured OS. A snapshot captures the current state of a VM at a point in time — it can be used for quick rollback after a software change.

---

### [SECTION 4: VIRTUAL SWITCHES]

[SHOW DIAGRAM: Physical server with hypervisor — vSwitch connecting multiple VMs internally, and uplinks to physical network switches]

When VMs on the same host communicate with each other, they do not need to go through a physical switch. The hypervisor includes a virtual switch (vSwitch) that handles inter-VM traffic entirely in software.

A virtual switch operates like a physical switch: it learns MAC addresses and forwards frames only to the appropriate virtual port. This allows VMs to communicate at Layer 2 speeds without hitting the physical network.

Key virtual switch concepts:

vSwitch uplinks — Physical NICs on the host that connect the virtual switch to the physical network. External traffic from VMs flows through these uplinks.

Port groups — Named groups of virtual ports on a vSwitch, typically mapped to a specific VLAN. A VM connected to a port group labeled VLAN 20 will have its traffic tagged for VLAN 20 when it leaves through the physical uplink.

VMware vSphere uses the vSphere Standard Switch (VSS) and the more advanced vSphere Distributed Switch (VDS) that spans multiple hosts. Microsoft Hyper-V uses the Hyper-V Virtual Switch. Both support VLANs through 802.1Q tagging, just like physical switches.

---

### [SECTION 5: NETWORK FUNCTION VIRTUALIZATION (NFV)]

[SHOW DIAGRAM: Traditional hardware appliances — physical firewall, physical load balancer, physical IDS — versus NFV running the same functions as VMs]

Network Function Virtualization (NFV) takes physical network appliances — firewalls, routers, load balancers, IDS/IPS, WAN accelerators — and replaces them with software instances running on commodity hardware.

Instead of buying a dedicated firewall appliance for each branch office, you deploy a virtual firewall (vFirewall) as a VM in a data center or cloud. Instead of a physical load balancer, you run a virtual load balancer on the same hardware as your application servers.

NFV benefits:

- Hardware cost reduction: commodity x86 servers instead of purpose-built appliances
- Elastic scaling: spin up additional instances during high load, scale down during off-peak
- Faster deployment: a new virtual firewall takes minutes; a new physical appliance takes weeks
- Centralized management: all network functions managed from a single orchestration platform

NFV is deployed and managed using orchestration systems such as VMware NSX, OpenStack, or cloud-native platforms like AWS and Azure.

---

### [SECTION 6: CONTAINERS AND MICROSERVICES]

[SHOW DIAGRAM: VM stack (hypervisor → OS → app) versus container stack (OS → container runtime → multiple containers sharing the OS kernel)]

Containers are a lighter-weight form of virtualization compared to VMs. Where a VM includes a full OS installation plus the application, a container shares the host OS kernel and includes only the application and its dependencies.

Key differences from VMs:

- Containers start in seconds; VMs take minutes to boot
- Containers use far less memory and disk than VMs
- Multiple containers share one OS kernel
- Containers are more portable but provide less isolation than VMs

Docker is the most common container runtime. Kubernetes (K8s) is the orchestration platform for managing large numbers of containers across multiple hosts.

For the Network+ exam, understand that containers share the host OS kernel while VMs include their own OS. This is the key architectural difference.

---

### [SECTION 7: VIRTUAL NETWORKING COMPONENTS SUMMARY]

[SHOW DIAGRAM: Complete virtualized data center stack — physical servers at bottom, hypervisor, VMs, vSwitch, physical switches, and WAN connection]

Let's summarize the virtual networking components you need to know:

Hypervisor — Creates and manages VMs. Type 1 (bare-metal) or Type 2 (hosted).

Virtual Machine (VM) — A software instance of a complete computer. Has virtual CPU, RAM, NIC, and disk.

Virtual Switch (vSwitch) — A software switch on the hypervisor. Connects VMs to each other and to physical networks through uplinks.

Virtual NIC (vNIC) — The VM's network interface. Connects to a virtual switch port group.

Port Group — A named group of virtual ports associated with a VLAN.

NFV — Network functions (firewall, router, load balancer) implemented as software VMs instead of physical hardware.

Container — A lightweight, OS-level virtualization that packages an application and its dependencies. Shares the host OS kernel.

In Part 2, we cover Software-Defined Networking (SDN), the control plane vs. data plane separation, SDN controllers, overlay networks, and how these technologies apply to cloud networking.

---

### [SUMMARY — PART 1]

In Part 1 we covered:

- The business case for virtualization: server consolidation, rapid provisioning, isolation
- Type 1 vs. Type 2 hypervisors: bare-metal versus hosted
- Virtual hardware components: vCPU, vNIC, virtual disk, VM templates and snapshots
- Virtual switches: how VMs communicate internally and connect to physical networks
- NFV: replacing physical network appliances with software instances
- Containers vs. VMs: shared OS kernel versus full OS per instance

See you in Part 2.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
