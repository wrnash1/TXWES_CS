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

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
