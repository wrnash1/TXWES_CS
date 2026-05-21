# Reading Guide: Module 03 - IP Addressing – IPv4, Subnetting, CIDR
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 03 – IP Addressing: IPv4, Subnetting, and CIDR**! IP addressing and subnetting are among the most heavily tested skills on the CompTIA Network+ N10-009 exam. You must be able to determine the network address, broadcast address, valid host range, and number of hosts for any given subnet — and do it under exam time pressure. This module covers binary-to-decimal conversion, classful addressing, private IP ranges, and CIDR notation. Practice the math until it is automatic.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **IPv4 Address**: A 32-bit logical address written in dotted-decimal notation (e.g., 192.168.1.10). Divided into a network portion (identified by the subnet mask) and a host portion. Every IPv4 address on a subnet shares the same network bits.
*   **Subnet Mask**: A 32-bit value that separates the network portion of an IP address from the host portion. Written in dotted-decimal (255.255.255.0) or CIDR slash notation (/24). Bits set to 1 = network; bits set to 0 = host.
*   **CIDR (Classless Inter-Domain Routing)**: A method of IP addressing that replaces the rigid classful system, expressing the subnet mask as a prefix length after a slash (e.g., 192.168.1.0/24). Allows flexible allocation of address space, reducing waste.
*   **Network Address**: The first address in a subnet where all host bits are 0. It is NOT assignable to a host. Example: 192.168.1.0 in the /24 subnet.
*   **Broadcast Address**: The last address in a subnet where all host bits are 1. It is NOT assignable to a host. Example: 192.168.1.255 in the /24 subnet.
*   **Usable Host Range**: All addresses between the network address and the broadcast address. Formula: 2^(host bits) − 2. A /24 subnet has 2^8 − 2 = 254 usable hosts.
*   **Classful Addressing**: The original IP address scheme dividing addresses into fixed classes based on the leading bits. Class A (/8, 1–126.x.x.x, ~16 million hosts per network), Class B (/16, 128–191.x.x.x, ~65,000 hosts), Class C (/24, 192–223.x.x.x, 254 hosts). Class D is multicast; Class E is experimental.
*   **Private IP Address Ranges (RFC 1918)**: Address ranges reserved for internal use that are not routed on the public internet. Must memorize all three: 10.0.0.0/8 (Class A private), 172.16.0.0–172.31.255.255 (/12, Class B private), 192.168.0.0/16 (Class C private).
*   **APIPA (Automatic Private IP Addressing)**: When a Windows device cannot reach a DHCP server, it self-assigns an address in the 169.254.0.0/16 range. An APIPA address means DHCP failed; the device can only communicate with other APIPA-addressed hosts on the same segment.
*   **Loopback Address**: 127.0.0.1 (IPv4). Used to test the TCP/IP stack on the local host without sending traffic to the network. Pinging 127.0.0.1 verifies the NIC driver and IP stack are functioning.
*   **VLSM (Variable Length Subnet Masking)**: The practice of using different subnet masks on different subnets within the same major network to allocate addresses efficiently. Requires a classless routing protocol (OSPF, EIGRP, RIPv2) to function.
*   **Subnetting the /24**: The most commonly tested subnet. Borrowing 1 bit from a /24 gives two /25 subnets (126 hosts each); borrowing 2 bits gives four /26 subnets (62 hosts each); borrowing 3 bits gives eight /27 subnets (30 hosts each). The pattern doubles the number of subnets and halves the hosts per subnet for each additional borrowed bit.
*   **Default Gateway**: The IP address of the router interface on the local subnet. Hosts send all traffic destined for remote networks to the default gateway. Misconfiguring the gateway breaks internet access but not local LAN communication.
*   **NAT (Network Address Translation)**: A router function that maps private internal IP addresses to one or more public IP addresses for internet access. PAT (Port Address Translation), also called NAT overload, maps many private IPs to a single public IP using unique port numbers.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** IP addressing falls under **Domain 1.0 – Networking Concepts (23%)**. Subnetting questions appear in scenario form — given an IP and mask, identify the subnet, broadcast, or valid range.
*   **The subnetting shortcut — "256 minus the interesting octet"**: For any subnet, find the block size by subtracting the subnet mask octet from 256. Example: /26 = mask 255.255.255.192. Block size = 256 − 192 = 64. Subnets start at 0, 64, 128, 192.
*   **Memorize the subnet mask to CIDR prefix table**: /24=255.255.255.0, /25=128, /26=192, /27=224, /28=240, /29=248, /30=252. The /30 gives exactly 2 usable hosts — used for point-to-point links.
*   **RFC 1918 trap question**: The exam frequently presents 172.32.x.x and asks if it is private. It is NOT — the private Class B range ends at 172.31.255.255. Similarly, 192.169.x.x is NOT private (private ends at 192.168.255.255).
*   **APIPA vs. no IP**: A 169.254.x.x address means DHCP failed but the NIC is functional. No IP at all (0.0.0.0) means a deeper configuration problem.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) has dedicated subnetting videos. Supplement with the free subnet calculator at [subnet-calculator.com](https://www.subnet-calculator.com/) to verify your practice answers.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters on **IPv4 Addressing and Subnetting** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Work through every subnetting example with pencil and paper.
*   **Required Video:** Watch Professor Messer's **IPv4 Addressing** and **Subnetting** videos from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/). These free videos walk through exam-style subnet calculations step by step.

---

### Lab & Command Integration
In this week's hands-on lab, you will configure static IP addresses on virtual machines, verify connectivity using `ping` and `ipconfig`/`ifconfig`, and practice subnet calculations by manually determining the correct address, mask, and gateway for each VM to communicate across simulated subnets.

---

### 3. Study Checklist
*   [ ] Memorize all three RFC 1918 private IP ranges and their CIDR prefixes.
*   [ ] Practice calculating network address, broadcast address, and usable host range for /24 through /30 subnets.
*   [ ] Know the APIPA range (169.254.0.0/16) and what it indicates.
*   [ ] Read the **IPv4 Addressing** chapter in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's subnetting videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
