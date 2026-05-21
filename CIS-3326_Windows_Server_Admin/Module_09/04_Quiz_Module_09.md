# Quiz: Module 09 - Windows Server Networking - Routing and Remote Access

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

A remote worker needs to connect to the corporate network from home. The home internet provider uses a firewall that blocks all ports except 80 and 443. Which VPN protocol supported by Windows Server RRAS can establish a VPN tunnel under these restrictive conditions?

A) L2TP/IPsec, because it is the most secure option and is supported by all RRAS deployments.
B) PPTP, because it uses port 1723 which is rarely blocked by consumer firewalls.
C) SSTP (Secure Socket Tunneling Protocol), because it tunnels VPN traffic inside HTTPS on port 443.
D) IKEv2, because it uses UDP port 500 which passes through NAT-traversal on most firewalls.

* **Correct Answer:** C) SSTP (Secure Socket Tunneling Protocol), because it tunnels VPN traffic inside HTTPS on port 443.
* **Distractor Analysis:**
  * *Why A is incorrect:* L2TP/IPsec uses UDP ports 500, 1701, and 4500 — all of which may be blocked by restrictive firewalls that only allow ports 80 and 443.
  * *Why B is incorrect:* PPTP uses TCP port 1723 and GRE protocol 47. Restrictive firewalls often block both, and PPTP is also considered cryptographically weak and is not recommended for new deployments.
  * *Why D is incorrect:* IKEv2 uses UDP ports 500 and 4500. While it supports NAT traversal, these ports would typically be blocked by a firewall that only allows ports 80 and 443.

---

### Question 2

A mobile workforce uses Windows 11 laptops that are Azure AD-joined (not domain-joined). The organization wants to provide always-on VPN connectivity that establishes a device tunnel before logon and a user tunnel after logon. Which remote access solution supports this configuration?

A) DirectAccess, which provides always-on transparent connectivity for domain-joined Windows Enterprise clients.
B) Always On VPN, which supports both device tunnels and user tunnels and works with Azure AD-joined non-domain devices.
C) SSTP VPN with pre-logon authentication configured through RRAS Connection Manager profiles.
D) Web Application Proxy (WAP) in pass-through mode, which provides pre-authentication for VPN clients.

* **Correct Answer:** B) Always On VPN, which supports both device tunnels and user tunnels and works with Azure AD-joined non-domain devices.
* **Distractor Analysis:**
  * *Why A is incorrect:* DirectAccess requires domain membership, Windows Enterprise edition, and an IPv6 infrastructure (or IPv6-over-IPv4 tunneling). It does not support Azure AD-joined or non-domain-joined devices.
  * *Why C is incorrect:* SSTP is a tunneling protocol, not an always-on solution with pre-logon device tunnel capability. Connection Manager profiles can configure SSTP but do not provide the device tunnel + user tunnel architecture of Always On VPN.
  * *Why D is incorrect:* Web Application Proxy is a reverse proxy for publishing internal web applications externally. It is not a VPN solution and does not establish a network-layer tunnel for device connectivity.

---

### Question 3

A Windows Server is configured as a NAT router using RRAS. Internal client computers use private IP addresses in the 10.0.0.0/8 range. An internal client initiates a web request to an external website. What does the NAT service do with the packet?

A) It encrypts the packet and forwards it to the external website using a VPN tunnel established by RRAS.
B) It replaces the internal source IP address with the server's public IP address and tracks the mapping so it can forward return packets back to the correct internal client.
C) It broadcasts the request to all internal clients and forwards whichever response arrives first to the requesting client.
D) It discards the packet because private IP addresses are not routable on the internet and cannot be translated by software.

* **Correct Answer:** B) It replaces the internal source IP address with the server's public IP address and tracks the mapping so it can forward return packets back to the correct internal client.
* **Distractor Analysis:**
  * *Why A is incorrect:* NAT and VPN are separate functions. RRAS can perform both, but NAT alone does not encrypt traffic — it only translates IP addresses. A VPN tunnel is a separate configuration from NAT.
  * *Why C is incorrect:* NAT maintains a state table mapping each internal client's IP:port pair to a unique external port on the NAT device's public IP. It does not broadcast requests — each connection is tracked individually and responses are forwarded to the originating internal client only.
  * *Why D is incorrect:* The entire purpose of NAT is to translate unroutable private IP addresses to a publicly routable address — this is precisely what NAT does and why it exists. Discarding the packet is the opposite of NAT's function.

---

### Question 4

An organization's RRAS VPN server is configured with Network Policy Server (NPS) as a RADIUS server for centralized authentication. A user reports being denied VPN access even though their AD account is active and their password is correct. Which component and tool should the administrator check first?

A) Check the VPN client's adapter settings on the user's laptop — the denial is likely caused by a misconfigured DNS suffix.
B) Check the NPS event logs on the Network Policy Server for a specific Event ID 6273 (Access-Reject) entry that includes the reason code for the denial.
C) Restart the RRAS service on the VPN server — authentication denials during peak hours are typically caused by service memory leaks.
D) Reset the user's dial-in permissions in Active Directory Users and Computers to "Allow access" to override all NPS policies.

* **Correct Answer:** B) Check the NPS event logs on the Network Policy Server for a specific Event ID 6273 (Access-Reject) entry that includes the reason code for the denial.
* **Distractor Analysis:**
  * *Why A is incorrect:* A DNS suffix misconfiguration on the client adapter would cause name resolution failures after a VPN connection is established — it would not prevent authentication and VPN connection establishment in the first place.
  * *Why C is incorrect:* Restarting services without evidence is an undirected troubleshooting approach that causes brief service disruption for all users. The NPS event log provides specific reason codes that pinpoint the exact policy condition causing the denial.
  * *Why D is incorrect:* Setting dial-in permission to "Allow access" overrides NPS Network Policy decisions for that user, which could bypass legitimate security controls such as MFA requirements or device compliance checks. This is a heavy-handed fix that should only be used after confirming NPS policies are correctly configured.

---

### Question 5

A site-to-site VPN is configured between two offices using RRAS on both ends. After a brief internet outage at one site, the VPN tunnel does not automatically re-establish, requiring the administrator to manually restart the RRAS service. Which VPN protocol should the administrator configure instead to enable automatic tunnel re-establishment after network interruptions?

A) PPTP, because its stateless design allows it to automatically reconnect after any network interruption.
B) L2TP/IPsec with pre-shared key authentication, because the pre-shared key eliminates certificate-dependent reconnection delays.
C) IKEv2 with the VPN Reconnect (MOBIKE) feature, which is specifically designed to re-establish VPN tunnels automatically after network interruptions.
D) SSTP, because its use of HTTPS makes it resilient to any network interruption and it reconnects transparently.

* **Correct Answer:** C) IKEv2 with the VPN Reconnect (MOBIKE) feature, which is specifically designed to re-establish VPN tunnels automatically after network interruptions.
* **Distractor Analysis:**
  * *Why A is incorrect:* PPTP has no built-in reconnection intelligence. After an internet outage, the PPTP session state is lost and the tunnel must be re-established from scratch — it does not reconnect automatically. Additionally, PPTP's weak encryption makes it unsuitable for production use.
  * *Why B is incorrect:* L2TP/IPsec also does not have automatic tunnel re-establishment built in. When the IPsec Security Associations expire or are disrupted, the tunnel requires re-negotiation, which in practice means manual intervention or a client-side reconnect trigger.
  * *Why D is incorrect:* SSTP uses HTTPS/port 443 to traverse firewalls and maintain connections through NAT, but it does not have a built-in reconnection mechanism equivalent to IKEv2's MOBIKE extension for surviving network interruptions without user or administrator action.
