# Quiz: Module 03 – IP Addressing: IPv4, Subnetting, CIDR
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

**Instructions:** Select the best answer for each question. Each question is worth 10 points (100 points total).

---

**Question 1**

A network technician is assigned the subnet 192.168.10.0/26. How many usable host addresses are available in this subnet?

A) 30

B) 62

C) 126

D) 254

- **Correct Answer:** B) 62
- **Distractor Analysis:**
  - *Why A is incorrect:* 30 usable hosts corresponds to a /27 subnet (32 total addresses minus 2 = 30 usable). A /26 is one step larger, with 64 total addresses.
  - *Why B is correct:* /26 has 6 host bits. 2^6 = 64 total addresses. 64 - 2 = 62 usable hosts.
  - *Why C is incorrect:* 126 usable hosts corresponds to a /25 subnet (128 total minus 2 = 126). A /25 borrows only 1 bit from a /24.
  - *Why D is incorrect:* 254 usable hosts corresponds to an unsubnetted /24 network (256 total minus 2 = 254). A /26 further subdivides the /24.

---

**Question 2**

Which of the following IPv4 addresses falls within a private address range defined by RFC 1918?

A) 172.32.10.5

B) 11.0.0.1

C) 10.200.15.33

D) 192.169.1.1

- **Correct Answer:** C) 10.200.15.33
- **Distractor Analysis:**
  - *Why A is incorrect:* The private Class B range is 172.16.0.0 through 172.31.255.255. The address 172.32.x.x falls outside this range and is a public address.
  - *Why B is incorrect:* The private Class A range is 10.0.0.0/8 only. The address 11.0.0.1 begins with 11, not 10, and is a public address.
  - *Why C is correct:* 10.200.15.33 begins with 10 and falls within the 10.0.0.0/8 private Class A range, which spans 10.0.0.0 through 10.255.255.255.
  - *Why D is incorrect:* The private Class C range is 192.168.0.0/16. The address 192.169.x.x is one octet beyond the private range and is a public address.

---

**Question 3**

A host is assigned the IP address 192.168.1.75 with a subnet mask of 255.255.255.224 (/27). What is the broadcast address of this host's subnet?

A) 192.168.1.63

B) 192.168.1.95

C) 192.168.1.127

D) 192.168.1.255

- **Correct Answer:** B) 192.168.1.95
- **Distractor Analysis:**
  - *Why A is incorrect:* 192.168.1.63 is the broadcast address of the /27 block 192.168.1.32–63. The host 192.168.1.75 falls in the next block (64–95).
  - *Why B is correct:* Block size = 256 - 224 = 32. Largest multiple of 32 not exceeding 75 is 64. Broadcast = 64 + 32 - 1 = 95. So the broadcast is 192.168.1.95.
  - *Why C is incorrect:* 192.168.1.127 is the broadcast of the third /27 block (96–127). The host 192.168.1.75 falls in the second block (64–95).
  - *Why D is incorrect:* 192.168.1.255 is the broadcast of the entire unsubnetted /24 network. This host is on a /27 subnet within that /24.

---

**Question 4**

A technician sees that a workstation has self-assigned the IP address 169.254.14.22 and cannot communicate with any network resources. What is the most likely root cause and correct remediation?

A) The default gateway is unreachable; configure a static gateway address on the workstation.

B) The DHCP server is unavailable or unreachable; restore the DHCP server or assign a static IP in the correct subnet.

C) The DNS server is offline; change the DNS server setting on the workstation to 8.8.8.8.

D) The subnet mask is misconfigured; correct it to match the rest of the network segment.

- **Correct Answer:** B) The DHCP server is unavailable or unreachable; restore the DHCP server or assign a static IP in the correct subnet.
- **Distractor Analysis:**
  - *Why A is incorrect:* A missing default gateway would still allow DHCP to assign a valid IP address. The 169.254.x.x range specifically signals DHCP failure before any gateway issue can be addressed.
  - *Why B is correct:* 169.254.x.x is the APIPA range, self-assigned by Windows when the DHCP DISCOVER process receives no response. The root cause is always DHCP server unavailability or a network path issue preventing the DISCOVER broadcast from reaching the server.
  - *Why C is incorrect:* A DNS failure results in a valid DHCP-assigned IP. The workstation would still have a proper address and could ping by IP. APIPA is not caused by DNS.
  - *Why D is incorrect:* A subnet mask misconfiguration assumes a valid IP address was already assigned. APIPA indicates no DHCP lease was obtained at all.

---

**Question 5**

A network design requires a subnet that connects exactly two routers on a point-to-point WAN link with minimal address waste. Which subnet mask is the most appropriate?

A) /24 — provides 254 usable host addresses

B) /28 — provides 14 usable host addresses

C) /30 — provides 2 usable host addresses

D) /32 — a host route representing a single device with no broadcast domain

- **Correct Answer:** C) /30 — provides 2 usable host addresses
- **Distractor Analysis:**
  - *Why A is incorrect:* A /24 wastes 252 addresses on a link that only needs 2. This violates the principle of minimal address waste for point-to-point links.
  - *Why B is incorrect:* A /28 provides 14 usable addresses, which is more than needed and wastes 12 addresses unnecessarily.
  - *Why C is correct:* A /30 has 4 total addresses: 1 network address, 2 usable host addresses (one for each router interface), and 1 broadcast address. This is the standard mask for point-to-point links.
  - *Why D is incorrect:* A /32 is a host route used in routing tables and loopback configurations. It has no broadcast domain and cannot be used to create a subnet connecting two devices.

---

**Question 6**

Which of the following statements about the 127.0.0.1 address is correct?

A) It is an RFC 1918 private address used for internal LAN communication.

B) It is the APIPA address assigned by Windows when DHCP fails.

C) It is the loopback address used to test the local host's TCP/IP stack without transmitting traffic.

D) It is the network address of the default Class C subnet 127.0.0.0/24.

- **Correct Answer:** C) It is the loopback address used to test the local host's TCP/IP stack without transmitting traffic.
- **Distractor Analysis:**
  - *Why A is incorrect:* 127.0.0.1 is not an RFC 1918 private address. The RFC 1918 private ranges are 10.x.x.x, 172.16-31.x.x, and 192.168.x.x. The loopback range (127.x.x.x) is a separate reserved category.
  - *Why B is incorrect:* APIPA addresses are in the 169.254.0.0/16 range, not 127.x.x.x.
  - *Why C is correct:* 127.0.0.1 is the standard loopback address. When you ping 127.0.0.1, the packet is processed by the local IP stack and returns without leaving the host. This confirms the NIC driver and TCP/IP stack are functional.
  - *Why D is incorrect:* While 127.0.0.0 might look like a network address, the entire 127.x.x.x range is reserved for loopback testing, not for host assignment as a /24 subnet.

---

**Question 7**

An administrator needs to create exactly 8 subnets from the 192.168.3.0/24 network block. What is the minimum number of bits that must be borrowed from the host portion?

A) 1 bit

B) 2 bits

C) 3 bits

D) 4 bits

- **Correct Answer:** C) 3 bits
- **Distractor Analysis:**
  - *Why A is incorrect:* Borrowing 1 bit creates 2^1 = 2 subnets, which is insufficient.
  - *Why B is incorrect:* Borrowing 2 bits creates 2^2 = 4 subnets, which is still insufficient for the requirement of 8.
  - *Why C is correct:* Borrowing 3 bits creates 2^3 = 8 subnets — exactly meeting the requirement. This extends the prefix from /24 to /27.
  - *Why D is incorrect:* Borrowing 4 bits creates 2^4 = 16 subnets, which exceeds the requirement. While it would technically work, it is not the minimum number of bits needed.

---

**Question 8**

Two hosts have the following configurations:

- Host A: IP 192.168.10.65, Mask 255.255.255.192
- Host B: IP 192.168.10.130, Mask 255.255.255.192

Can Host A communicate with Host B without a router?

A) Yes, because both hosts share the same /24 network address (192.168.10.0).

B) No, because Host A is on the 192.168.10.64/26 subnet and Host B is on the 192.168.10.128/26 subnet.

C) Yes, because both hosts have the same subnet mask (255.255.255.192).

D) No, because 192.168.10.65 is in the APIPA range and cannot communicate with RFC 1918 addresses.

- **Correct Answer:** B) No, because Host A is on the 192.168.10.64/26 subnet and Host B is on the 192.168.10.128/26 subnet.
- **Distractor Analysis:**
  - *Why A is incorrect:* Sharing the same /24 parent network does not mean they are on the same /26 subnet. The subnet mask is /26, not /24. Layer 3 routing is required to cross subnet boundaries.
  - *Why B is correct:* With a /26 mask (block size 64): Host A (65) falls in block 64–127 (network 192.168.10.64). Host B (130) falls in block 128–191 (network 192.168.10.128). These are different subnets — a router is required.
  - *Why C is incorrect:* Having the same subnet mask does not place hosts on the same subnet. The subnet depends on both the IP address and the mask.
  - *Why D is incorrect:* 192.168.10.65 is in the RFC 1918 private range (192.168.x.x), not APIPA. APIPA is 169.254.x.x.

---

**Question 9**

A network administrator is planning an address scheme for a new office with five departments. The largest department has 45 workstations and the smallest has 10. The administrator wants to use one contiguous block and minimize address waste. What is the smallest CIDR prefix that accommodates the largest department?

A) /26 — supports 62 usable hosts

B) /27 — supports 30 usable hosts

C) /28 — supports 14 usable hosts

D) /25 — supports 126 usable hosts

- **Correct Answer:** A) /26 — supports 62 usable hosts
- **Distractor Analysis:**
  - *Why A is correct:* The largest department has 45 workstations. A /26 provides 62 usable hosts, which accommodates 45 devices with room for 17 additional hosts (growth). This is the smallest prefix that supports 45 hosts.
  - *Why B is incorrect:* A /27 provides only 30 usable hosts, which is insufficient for a 45-workstation department.
  - *Why C is incorrect:* A /28 provides only 14 usable hosts, far too few for 45 workstations.
  - *Why D is incorrect:* A /25 provides 126 usable hosts, which accommodates the requirement, but it is larger than necessary and wastes more address space than the /26.

---

**Question 10**

What is the network address for the host 172.16.50.200 with a subnet mask of 255.255.255.248 (/29)?

A) 172.16.50.192

B) 172.16.50.200

C) 172.16.50.196

D) 172.16.50.248

- **Correct Answer:** A) 172.16.50.192
- **Distractor Analysis:**
  - *Why A is correct:* Block size = 256 - 248 = 8. Multiples of 8: 0, 8, 16, ..., 192, 200, 208. The largest multiple of 8 not exceeding 200 is 192. Network address = 172.16.50.192.
  - *Why B is incorrect:* 172.16.50.200 is the actual host address, not the network address. The network address has all host bits set to zero.
  - *Why C is incorrect:* 172.16.50.196 is not a multiple of 8 and is therefore not a valid network address for a /29 subnet. All /29 network addresses in a /24 are multiples of 8.
  - *Why D is incorrect:* 172.16.50.248 is the network address of the next /29 block beyond the one containing 200. The host falls in the 192–199 block, not the 248–255 block.

---

### Question 11

A host has the IP address 10.0.0.130 with a subnet mask of 255.255.255.128 (/25). What is the broadcast address for this subnet?

- A) 10.0.0.127
- B) 10.0.0.255
- C) 10.0.0.128
- D) 10.0.0.254

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* 10.0.0.127 is the broadcast address for the first /25 subnet (10.0.0.0–10.0.0.127). The host 10.0.0.130 falls in the second /25 subnet (10.0.0.128–10.0.0.255).
- *Why B is correct:* Block size = 256 – 128 = 128. Subnets: 10.0.0.0 (hosts .1–.126, broadcast .127) and 10.0.0.128 (hosts .129–.254, broadcast .255). The host .130 is in the second subnet; its broadcast address is 10.0.0.255.
- *Why C is incorrect:* 10.0.0.128 is the network address of the subnet, not the broadcast address.
- *Why D is incorrect:* 10.0.0.254 is the last valid host address in the second /25 subnet, not the broadcast address. The broadcast address is one higher, at .255.

---

### Question 12

How many usable host addresses are available in a /29 subnet?

- A) 8
- B) 4
- C) 6
- D) 14

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A /29 has 2^3 = 8 total addresses. Subtracting network and broadcast gives 6 usable hosts, not 8.
- *Why B is incorrect:* A /30 has 4 total addresses (2 usable). A /29 has 8 total addresses.
- *Why C is correct:* A /29 has 3 host bits (32 – 29 = 3). Total addresses = 2^3 = 8. Usable hosts = 8 – 2 = 6. This makes /29 useful for small multi-access links.
- *Why D is incorrect:* A /28 has 4 host bits, giving 16 total and 14 usable hosts. A /29 is one prefix longer (fewer hosts).

---

### Question 13

Which of the following IP addresses falls within the RFC 1918 private address space?

- A) 172.32.0.1
- B) 192.169.0.1
- C) 10.255.255.254
- D) 100.64.0.1

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* RFC 1918 Class B private range is 172.16.0.0–172.31.255.255. The address 172.32.0.1 is outside this range (begins at 172.32.x.x) and is therefore public.
- *Why B is incorrect:* RFC 1918 Class C private range is 192.168.0.0–192.168.255.255. The address 192.169.0.1 is one block above this range and is public.
- *Why C is correct:* The RFC 1918 Class A private range is 10.0.0.0–10.255.255.255. The address 10.255.255.254 falls within this range and is private.
- *Why D is incorrect:* 100.64.0.1 falls in the RFC 6598 Shared Address Space (100.64.0.0/10), used for carrier-grade NAT — it is not part of RFC 1918 private space.

---

### Question 14

A network is using VLSM to allocate subnets. A WAN point-to-point link between two routers requires only 2 usable host addresses. Which prefix length provides exactly 2 usable hosts with the least address waste?

- A) /28
- B) /29
- C) /30
- D) /31

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A /28 provides 14 usable hosts — far more than needed for a 2-host point-to-point link.
- *Why B is incorrect:* A /29 provides 6 usable hosts — still more than needed and wastes 4 addresses.
- *Why C is correct:* A /30 provides 4 total addresses: 1 network address, 2 usable hosts, and 1 broadcast address. This is the standard prefix for point-to-point WAN links and is the smallest subnet with 2 usable host addresses under traditional subnetting rules.
- *Why D is incorrect:* A /31 has 2 total addresses and no broadcast or network address under RFC 3021. While valid for point-to-point links in some implementations, the standard exam answer for 2 usable hosts on a WAN link is /30.

---

### Question 15

What is the CIDR notation for the subnet mask 255.255.248.0?

- A) /20
- B) /21
- C) /22
- D) /23

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* /20 = 255.255.240.0 (first 20 bits set). This corresponds to 11110000 in the third octet, not 11111000.
- *Why B is correct:* 255.255.248.0 in binary is 11111111.11111111.11111000.00000000. Count the consecutive 1s: 8+8+5 = 21. CIDR prefix = /21.
- *Why C is incorrect:* /22 = 255.255.252.0 (11111100 in the third octet, 22 ones total).
- *Why D is incorrect:* /23 = 255.255.254.0 (11111110 in the third octet, 23 ones total).

---

### Question 16

A host receives a 169.254.x.x IP address automatically. What does this indicate about the host's network configuration?

- A) The host has successfully obtained a valid IP address via DHCP.
- B) The host is configured with an RFC 1918 private address in the APIPA range.
- C) The host failed to contact a DHCP server and self-assigned an APIPA address.
- D) The host is using a static IP address reserved for network management.

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* APIPA addresses (169.254.x.x) are assigned when DHCP fails — the host has NOT successfully obtained a DHCP lease.
- *Why B is incorrect:* APIPA (169.254.0.0/16) is a separate range defined in RFC 3927. It is distinct from RFC 1918 private address space (10.x.x.x, 172.16–31.x.x, 192.168.x.x).
- *Why C is correct:* When a Windows host cannot reach a DHCP server, it self-assigns an APIPA address in the 169.254.0.0/16 range using zero-configuration networking. This address allows link-local communication but not internet access.
- *Why D is incorrect:* APIPA addresses are not statically configured management addresses. They are dynamically self-assigned as a fallback when DHCP is unavailable.

---

### Question 17

A company needs to create 14 subnets from the 192.168.10.0/24 network. What is the minimum number of bits that must be borrowed from the host portion to create at least 14 subnets?

- A) 3 bits
- B) 4 bits
- C) 5 bits
- D) 6 bits

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Borrowing 3 bits creates 2^3 = 8 subnets, which is fewer than the 14 required.
- *Why B is correct:* Borrowing 4 bits creates 2^4 = 16 subnets. This is the minimum number of borrowed bits that produces at least 14 subnets. The resulting prefix is /28 with 14 usable hosts per subnet.
- *Why C is incorrect:* Borrowing 5 bits creates 32 subnets — more than needed. While valid, it is not the minimum.
- *Why D is incorrect:* Borrowing 6 bits creates 64 subnets — far more than needed and provides only 2 usable hosts per subnet.

---

### Question 18

Which of the following is a valid host address within the 192.168.1.64/26 subnet?

- A) 192.168.1.63
- B) 192.168.1.64
- C) 192.168.1.100
- D) 192.168.1.128

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* 192.168.1.63 is the broadcast address of the previous subnet (192.168.1.0/26 with range .1–.62, broadcast .63). It is not a host in the .64/26 subnet.
- *Why B is incorrect:* 192.168.1.64 is the network address of this subnet — it cannot be assigned to a host.
- *Why C is correct:* Block size = 64. The 192.168.1.64/26 subnet covers .64–.127. Valid hosts are .65–.126. The address .100 falls within this range.
- *Why D is incorrect:* 192.168.1.128 is the network address of the next /26 subnet (.128–.191). It is in a different subnet than .64/26.

---

### Question 19

What is the primary purpose of NAT (Network Address Translation) in IPv4 networking?

- A) To convert IPv4 addresses to IPv6 addresses for dual-stack environments.
- B) To allow multiple devices using private RFC 1918 addresses to share a single public IPv4 address for internet access.
- C) To assign IP addresses automatically to clients on a local network.
- D) To encrypt IP packets as they cross the boundary between a private and public network.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* NAT does not convert between IPv4 and IPv6. That function is provided by translation technologies such as NAT64 or dual-stack configuration — standard NAT only operates within the IPv4 address space.
- *Why B is correct:* NAT (specifically PAT/overload) allows many private RFC 1918 addresses to appear as a single (or pool of) public IP address(es) on the internet by tracking connections using port numbers. This extends the life of IPv4 by reducing public address consumption.
- *Why C is incorrect:* DHCP assigns IP addresses automatically to clients. NAT translates addresses at a network boundary — these are separate functions.
- *Why D is incorrect:* NAT does not encrypt packets. IPsec and TLS provide encryption. NAT merely substitutes private source addresses with public addresses.

---

### Question 20

Given the IP address 172.16.100.200 with mask /22, what is the network address of this subnet?

- A) 172.16.100.0
- B) 172.16.99.0
- C) 172.16.100.128
- D) 172.16.96.0

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is incorrect (checking)... actually correct:* /22 means 22 bits of network, 10 bits of host. The subnet mask is 255.255.252.0. Block size in third octet = 256 – 252 = 4. Multiples of 4: 96, 100, 104... The address 172.16.100.200 falls in the 172.16.100.0 block (100 is a multiple of 4). Network address = 172.16.100.0.
- *Why A is correct:* 172.16.100.0 is correct — 100 is exactly divisible by 4 (block size), so the network address is 172.16.100.0.
- *Why B is incorrect:* 172.16.99.0 would be the network address of the 172.16.96.0/22 subnet's invalid subdivision — 99 is not a multiple of 4.
- *Why C is incorrect:* 172.16.100.128 is a host address within the subnet, not the network address. The network address has all host bits zeroed.
- *Why D is incorrect:* 172.16.96.0 is the network address of the previous /22 subnet (172.16.96.0–172.16.99.255). The host .100.200 is in the next block starting at 172.16.100.0.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
