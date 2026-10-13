# Quiz 2: Network Implementations (Domain 2.0)
**Course:** CIS 3321 - Network Administration
**Format:** Question Bank with Distractor Analysis

---

**Question 1**
A network administrator needs to logically separate the Accounting department's network traffic from the Marketing department's traffic, even though both departments plug their computers into the exact same physical switch. Which technology should the administrator configure?
A) VPN
B) VLAN
C) NAT
D) ARP

*   **Correct Answer:** B) VLAN
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A Virtual Private Network (VPN) encrypts traffic over an untrusted network like the internet, it is not used to separate broadcast domains on a local switch.
    *   *Why C is incorrect:* Network Address Translation (NAT) translates private IP addresses to public IP addresses for internet access.
    *   *Why D is incorrect:* The Address Resolution Protocol (ARP) resolves IP addresses to MAC addresses; it does not separate traffic.

**Question 2**
Which of the following IPv4 addresses is considered a private IP address under RFC 1918 and cannot be routed across the public internet?
A) 8.8.8.8
B) 172.16.5.100
C) 192.169.1.50
D) 12.0.0.1

*   **Correct Answer:** B) 172.16.5.100
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 8.8.8.8 is a public IP address (famously owned by Google for DNS).
    *   *Why C is incorrect:* The private Class C range is 192.168.x.x. 192.*169*.x.x is a public IP address space.
    *   *Why D is incorrect:* The private Class A range is 10.x.x.x. 12.0.0.1 is a public IP address.

**Question 3**
What protocol is used to tag Ethernet frames with a VLAN ID as they pass across a trunk link between two switches?
A) 802.11ac
B) 802.3af
C) 802.1Q
D) IPv6

*   **Correct Answer:** C) 802.1Q
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 802.11ac is a Wireless networking standard (Wi-Fi 5).
    *   *Why B is incorrect:* 802.3af is the standard for Power over Ethernet (PoE).
    *   *Why D is incorrect:* IPv6 is a Layer 3 addressing protocol, not a Layer 2 VLAN tagging protocol.

**Question 4**
A computer on an IPv6 network automatically generates an address to communicate with other devices on its immediate local network segment, without needing a DHCP server. What type of IPv6 address does this begin with?
A) 192.168::
B) fe80::
C) 2001::
D) ::1

*   **Correct Answer:** B) fe80::
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 192.168 is an IPv4 convention, not an IPv6 prefix.
    *   *Why C is incorrect:* 2001:: is a Global Unicast address prefix, meaning it is routable on the public IPv6 internet.
    *   *Why D is incorrect:* ::1 is the IPv6 Loopback address (equivalent to 127.0.0.1 in IPv4), used to test the local NIC, not talk to other devices.
