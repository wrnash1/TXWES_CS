# Quiz: Module 03 - IP Addressing – IPv4, Subnetting, CIDR
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A network technician is assigned the subnet 192.168.10.0/26. How many usable host addresses are available in this subnet?
A) 30
B) 62
C) 126
D) 254
*   **Correct Answer:** B) 62
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 30 usable hosts corresponds to a /27 subnet (32 addresses − 2 = 30), which borrows 3 bits from a /24, not 2.
    *   *Why C is incorrect:* 126 usable hosts corresponds to a /25 subnet (128 addresses − 2 = 126), which borrows only 1 bit from a /24.
    *   *Why D is incorrect:* 254 usable hosts corresponds to an unsubnetted /24 network (256 − 2 = 254); a /26 borrows 2 bits and produces only 64 total addresses.

---

**Question 2**
Which of the following IPv4 addresses falls within a private address range defined by RFC 1918?
A) 172.32.10.5
B) 11.0.0.1
C) 10.200.15.33
D) 192.169.1.1
*   **Correct Answer:** C) 10.200.15.33
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The private Class B range is 172.16.0.0 to 172.31.255.255. The address 172.32.x.x falls outside this range and is a public address.
    *   *Why B is incorrect:* The private Class A range is 10.0.0.0/8 only. The address 11.0.0.1 begins with 11, not 10, and is therefore a public address.
    *   *Why D is incorrect:* The private Class C range is 192.168.0.0/16. The address 192.169.x.x is one octet beyond the private range and is a public address.

---

**Question 3**
A host is assigned the IP address 192.168.1.75 with a subnet mask of 255.255.255.224 (/27). What is the broadcast address of this host's subnet?
A) 192.168.1.63
B) 192.168.1.95
C) 192.168.1.127
D) 192.168.1.255
*   **Correct Answer:** B) 192.168.1.95
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 192.168.1.63 is the broadcast address of the first /27 block (192.168.1.32–63), not the block containing .75.
    *   *Why C is incorrect:* 192.168.1.127 is the broadcast address of the third /27 block (192.168.1.96–127); the host .75 falls in the second block (64–95).
    *   *Why D is incorrect:* 192.168.1.255 is the broadcast address of the entire /24 network, not of the /27 subnet containing this host.

---

**Question 4**
A technician sees that a workstation has self-assigned the IP address 169.254.14.22 and cannot communicate with any network resources. What is the most likely root cause and correct remediation?
A) The default gateway is unreachable; configure a static gateway address on the workstation.
B) The DHCP server is unavailable or unreachable; restore the DHCP server or assign a static IP in the correct subnet.
C) The DNS server is offline; change the DNS server setting on the workstation to 8.8.8.8.
D) The subnet mask is misconfigured; correct it to match the rest of the network segment.
*   **Correct Answer:** B) The DHCP server is unavailable or unreachable; restore the DHCP server or assign a static IP in the correct subnet.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A missing default gateway would still allow DHCP to assign a valid IP address; the 169.254.x.x range specifically signals DHCP failure before any gateway issue matters.
    *   *Why C is incorrect:* A DNS failure results in a valid IP being assigned; the workstation would still have a proper address and could ping by IP. APIPA (169.254.x.x) is not a DNS problem.
    *   *Why D is incorrect:* A subnet mask misconfiguration assumes a valid IP address was already assigned; APIPA addresses indicate no DHCP lease was obtained at all.

---

**Question 5**
A network design requires a subnet that connects exactly two routers on a point-to-point WAN link with minimal address waste. Which subnet mask is the most appropriate?
A) /24 — provides 254 usable host addresses
B) /28 — provides 14 usable host addresses
C) /30 — provides 2 usable host addresses
D) /32 — a host route representing a single device with no broadcast domain
*   **Correct Answer:** C) /30 — provides 2 usable host addresses
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A /24 wastes 252 addresses on a link that only needs 2; it violates the principle of minimal address waste for point-to-point links.
    *   *Why B is incorrect:* A /28 provides 14 usable addresses, which is more than needed for a two-endpoint link and still wastes 12 addresses.
    *   *Why D is incorrect:* A /32 is a host route (no subnet, no broadcast) used in routing tables and loopback configurations; it cannot be used to create a subnet connecting two devices.
