# Reading Guide: Module 06 - DNS and DHCP Server Roles

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 06 – DNS and DHCP Server Roles**! This week's study material covers the two foundational network infrastructure services that every Windows Server environment depends on: Domain Name System (DNS) for name resolution and Dynamic Host Configuration Protocol (DHCP) for IP address assignment. Both services are heavily tested on the AZ-800 exam in the context of AD DS integration and enterprise network management.

As a student, you will learn how to configure DNS zones, understand the difference between AD-integrated and standard zones, and manage DHCP scopes, reservations, and failover. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **DNS Forward Lookup Zone**: A zone that resolves hostnames to IP addresses (A and AAAA records). Every AD DS domain must have a forward lookup zone matching the domain name (e.g., corp.local) so that DCs can register their SRV records and clients can locate services.
* **DNS Reverse Lookup Zone**: A zone that resolves IP addresses back to hostnames (PTR records). Required for certain applications and security tools that perform reverse lookups to verify client identity.
* **AD-Integrated DNS Zone**: A DNS zone stored directly in the AD DS database instead of a flat text file. AD-integrated zones replicate automatically with AD DS, support secure dynamic updates (only domain members can register records), and allow any DC running DNS to accept updates (multi-master).
* **DHCP Scope**: A defined range of IP addresses that the DHCP server can lease to clients on a specific subnet. A scope also distributes options such as the default gateway, DNS server addresses, and domain name.
* **DHCP Reservation**: A configuration within a scope that maps a specific MAC address to a specific IP address, ensuring a device always receives the same address via DHCP. Used for servers, printers, and other devices that need a predictable IP without static configuration.
* **DHCP Failover**: A Windows Server feature that allows two DHCP servers to share a scope's address pool, providing redundancy. Modes are Hot Standby (one server is passive) and Load Balance (both servers serve leases simultaneously).

---

### 2. Certification Exam Tips

* **DNS is a prerequisite for AD DS**: Every DC registers SRV records in DNS under _msdcs so that other DCs and clients can locate services. If DNS is broken, AD authentication fails. Know the `nslookup` and `dcdiag /test:dns` commands for diagnosing DNS issues.
* **AD-integrated zones vs. standard primary zones**: AZ-800 will present scenarios where you must choose between zone types. AD-integrated zones are almost always the correct answer for AD environments because of their automatic replication, secure dynamic updates, and no single-point-of-failure.
* **80/20 rule for DHCP**: A traditional best practice is to configure two DHCP servers where one serves 80% of a scope's addresses and the other serves the remaining 20%, providing redundancy. DHCP Failover in Load Balance mode automates this more cleanly.
* **Microsoft Learn Reference**: Review DNS and DHCP documentation at [Microsoft Learn – DNS Server](https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top) and [Microsoft Learn – DHCP](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top) for configuration walkthroughs and troubleshooting steps.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the DNS and DHCP server role documentation at [Microsoft Learn: DNS Server](https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top) and [Microsoft Learn: DHCP](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top). Focus on zone types, scope configuration, and DHCP failover.
* **Required Video:** Watch the video lecture on **DNS and DHCP Server Roles** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will create an AD-integrated DNS forward lookup zone, add an A record manually, and verify resolution with `nslookup`. You will also create a DHCP scope, configure a client exclusion range and a MAC-based reservation, and authorize the DHCP server in Active Directory.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the DNS documentation at [Microsoft Learn: DNS Server](https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top).
* [ ] Read the DHCP documentation at [Microsoft Learn: DHCP](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top).
* [ ] Watch the video lecture on **DNS and DHCP Server Roles** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
