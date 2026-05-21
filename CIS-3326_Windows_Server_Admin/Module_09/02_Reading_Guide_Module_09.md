# Reading Guide: Module 09 - Windows Server Networking - Routing and Remote Access

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 09 – Windows Server Networking: Routing and Remote Access**! This week's study material covers the Routing and Remote Access Service (RRAS), which allows Windows Server to function as a software-based router, a VPN server, and a dial-up access point. Understanding RRAS is essential for AZ-800 exam scenarios involving site-to-site VPNs, remote worker access, and network address translation (NAT).

As a student, you will learn how to configure VPN protocols, set up NAT for internet access sharing, and understand how DirectAccess and Always On VPN provide seamless remote connectivity for domain-joined clients. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Routing and Remote Access Service (RRAS)**: A Windows Server role that provides software-based routing (LAN-to-LAN and WAN), VPN server functionality, and Network Address Translation (NAT). It is configured through the Routing and Remote Access MMC console or PowerShell.
* **VPN Protocols — PPTP, L2TP/IPsec, SSTP, IKEv2**: Windows Server RRAS supports four VPN tunneling protocols. SSTP (uses HTTPS/port 443) is the most firewall-friendly. IKEv2 supports VPN Reconnect (automatically re-establishes connections after brief network interruptions). L2TP/IPsec provides strong encryption but requires pre-shared keys or certificates. PPTP is legacy and not recommended for new deployments.
* **Network Address Translation (NAT)**: A routing function that translates private IP addresses on an internal network to a single public IP address for internet access. RRAS can act as a NAT device, allowing internal clients to reach the internet without each needing a public IP.
* **DirectAccess**: A Windows feature (now superseded by Always On VPN) that provides transparent, always-on remote access for domain-joined Windows clients over IPv6 tunneled in HTTPS. No user intervention is required — the tunnel establishes automatically before logon.
* **Always On VPN**: The modern Microsoft replacement for DirectAccess. It supports non-domain-joined devices, works with Windows 10/11 and later, and provides device tunnels (pre-logon) and user tunnels. It uses IKEv2 or SSTP and integrates with Microsoft Intune.
* **RADIUS (Remote Authentication Dial-In User Service)**: An authentication, authorization, and accounting protocol. RRAS can act as a RADIUS client, forwarding authentication requests to a Network Policy Server (NPS) acting as the RADIUS server, centralizing access policy enforcement.

---

### 2. Certification Exam Tips

* **VPN protocol selection by scenario**: AZ-800 will give a scenario and ask which VPN protocol to use. If the client is behind a restrictive firewall that blocks everything except port 443, the answer is SSTP. If mobile reconnection after brief outages is the requirement, the answer is IKEv2 with VPN Reconnect.
* **Always On VPN vs. DirectAccess**: DirectAccess requires domain membership, Windows Enterprise edition, and an IPv6 infrastructure. Always On VPN works with any Windows 10/11 edition, non-domain devices, and pure IPv4 networks — making it the preferred answer for modern deployments.
* **NPS as RADIUS for centralized policy**: When RRAS is configured as a RADIUS client pointing to NPS, all VPN authentication decisions are made centrally by NPS using Network Policies. This allows multi-factor authentication (MFA) and conditional access to be enforced on VPN connections.
* **Microsoft Learn Reference**: Review RRAS and Always On VPN documentation at [Microsoft Learn – Routing and Remote Access Service](https://learn.microsoft.com/en-us/windows-server/remote/remote-access/ras/remote-access-service-ras) and [Microsoft Learn – Always On VPN](https://learn.microsoft.com/en-us/windows-server/remote/remote-access/vpn/always-on-vpn/always-on-vpn-overview).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the RRAS and Always On VPN documentation at [Microsoft Learn: Remote Access Service (RAS)](https://learn.microsoft.com/en-us/windows-server/remote/remote-access/ras/remote-access-service-ras). Focus on VPN protocol options, NAT configuration, and the comparison between DirectAccess and Always On VPN.
* **Required Video:** Watch the video lecture on **Windows Server Networking – Routing and Remote Access** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will install and configure RRAS as a VPN server using IKEv2, create a VPN client connection from a test workstation, and verify connectivity. You will also configure NAT to allow internal clients to access the internet through a simulated external interface.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the RRAS documentation at [Microsoft Learn: Remote Access Service (RAS)](https://learn.microsoft.com/en-us/windows-server/remote/remote-access/ras/remote-access-service-ras).
* [ ] Watch the video lecture on **Windows Server Networking – Routing and Remote Access** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
