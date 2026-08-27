# Reading Guide: Module 04 – Enterprise Security & Infrastructure Hardening
## CSC-6361 Advanced Computer Networks | Graduate Level
## Week 4: November 9–15, 2026

---

## Learning Objectives
By completing this reading guide, you will be able to:
1. Configure AAA using TACACS+ and RADIUS with proper fallback to local authentication.
2. Design and implement named extended ACLs for traffic filtering, including `established` keyword and reflexive ACLs.
3. Apply Control Plane Policing (CoPP) to protect router CPU from denial-of-service.
4. Configure Layer 2 security features: DHCP Snooping, Dynamic ARP Inspection, IP Source Guard, Port Security, and 802.1X.
5. Harden BGP sessions with prefix filtering, max-prefix limits, and MD5 authentication.
6. Build a comprehensive management plane hardening baseline for Cisco IOS devices.

---

## Required Free Readings

### 1. NIST SP 800-41 Rev 1 — Guidelines on Firewalls and Firewall Policy (Free)
**URL:** https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final
**Focus:** Section 3 (Firewall technologies), Section 4 (Firewall policy design). Provides the policy framework that ACL design must support.

### 2. IETF RFC 8446 — Transport Layer Security (TLS) 1.3 (Free)
**URL:** https://datatracker.ietf.org/doc/html/rfc8446
**Focus:** Section 1 (Introduction), Section 2 (Protocol Overview). Understanding TLS 1.3 is essential for evaluating encrypted management traffic (HTTPS, SSH).

### 3. Cisco AAA Configuration Guide — IOS XE (Free)
**URL:** https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_aaa/configuration/xe-16/sec-usr-aaa-xe-16-book.html
**Focus:** TACACS+ vs. RADIUS configuration, aaa authentication/authorization/accounting commands, local fallback.

### 4. Cisco Layer 2 Security Guide — DHCP Snooping, DAI, IP Source Guard (Free)
**URL:** https://www.cisco.com/c/en/us/support/docs/lan-switching/ip-source-guard/116082-config-ip-source-guard-00.html
**Focus:** DHCP Snooping configuration, DAI validation, IP Source Guard — configuration and verification.

### 5. Cisco CIS Benchmark for IOS (Free Community Version)
**URL:** https://www.cisecurity.org/cis-benchmarks
Download the CIS Cisco IOS Benchmark (requires free registration). This is the industry-standard hardening checklist for Cisco IOS devices.
**Focus:** Review Level 1 (basic hardening) recommendations: management plane controls, SSH, service disabling.

### 6. Cisco BGP Security Best Practices (Free)
**URL:** https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/26634-bgp-best-practices.html
**Focus:** Prefix filtering, max-prefix, MD5 authentication, GTSM (TTL security).

---

## Key Security Hardening Baseline

### Device Hardening Checklist (Copy to Every IOS Device)
```
! Disable unnecessary services
no service tcp-small-servers
no service udp-small-servers
no ip finger
no ip http server
ip http secure-server
no ip bootp server
no cdp run                    ! Disable CDP on external-facing interfaces only

! SSH hardening
ip ssh version 2
ip ssh time-out 60
ip ssh authentication-retries 3
crypto key generate rsa modulus 2048

! Banner (legal warning — required for prosecution in many jurisdictions)
banner login ^
AUTHORIZED USERS ONLY. Unauthorized access is a federal crime under the
Computer Fraud and Abuse Act (18 U.S.C. 1030). All activity is logged.
^

! Disable EXEC sessions on console after inactivity
line console 0
 exec-timeout 5 0
 login authentication default

line vty 0 15
 transport input ssh
 exec-timeout 10 0
 login authentication default
 access-class MGMT-ACCESS in

! Logging
logging buffered 65536 informational
logging trap informational
service timestamps log datetime msec localtime show-timezone
service timestamps debug datetime msec localtime

! Password security
service password-encryption
security passwords min-length 12
enable secret 0 [use strong password]
```

### AAA Quick Reference
```
aaa new-model
tacacs server PRIMARY
 address ipv4 10.99.99.10
 key TacacsKey123
aaa group server tacacs+ ADMIN-GROUP
 server name PRIMARY
aaa authentication login default group ADMIN-GROUP local
aaa authorization exec default group ADMIN-GROUP local
aaa authorization commands 15 default group ADMIN-GROUP local
aaa accounting exec default start-stop group ADMIN-GROUP
aaa accounting commands 15 default start-stop group ADMIN-GROUP
```

### Layer 2 Security Quick Reference
```
! DHCP Snooping
ip dhcp snooping
ip dhcp snooping vlan 10,20,30
ip dhcp snooping database flash:dhcp-snooping.db
interface [uplink to DHCP server]
 ip dhcp snooping trust
interface range [access ports]
 ip dhcp snooping limit rate 15

! DAI (requires DHCP Snooping enabled first)
ip arp inspection vlan 10,20,30
interface [uplink]
 ip arp inspection trust

! IP Source Guard
interface [access port]
 ip verify source

! Port Security
interface [access port]
 switchport mode access
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation restrict
```

---

## Verification Commands Quick Reference
```
! AAA
show aaa sessions
show tacacs
debug aaa authentication

! ACLs
show ip access-lists                        ! View ACL hit counters
show ip access-lists ALLOW-WEB-ONLY        ! Specific ACL

! Layer 2 Security
show ip dhcp snooping binding               ! View binding table (MAC/IP/VLAN/Port)
show ip dhcp snooping statistics            ! Dropped packet counters
show ip arp inspection vlan 10              ! DAI statistics and forwarded/dropped counts
show port-security interface FastEth0/3    ! Port security status and MAC count
show dot1x interface FastEthernet0/5       ! 802.1X status

! BGP Security
show ip bgp neighbor 203.0.113.1           ! BGP session status, prefix counts
show ip bgp regexp _                        ! All BGP routes (debugging)
show ip prefix-list                         ! View configured prefix lists
```

---

## Graduate Discussion Prompt (Due Sunday, November 15, 2026, 11:59 PM CST)

**Scenario:** A small regional bank has experienced a security incident. A contractor connected an unauthorized laptop to a conference room Ethernet jack. The laptop was running a rogue DHCP server and an ARP spoofing tool. Within minutes, workstations throughout the building began sending traffic through the attacker's laptop instead of the legitimate default gateway — a classic man-in-the-middle attack that captured plaintext credentials for internal web applications.

**Write a graduate-level post (400+ words) addressing:**
1. **Attack Mechanics:** Explain precisely how the DHCP-based attack worked (rogue DHCP server) and how the ARP spoofing attack worked. What layer of the OSI model is each attack operating at, and why do traditional IP-based security tools (firewalls, IDS) fail to catch these attacks?
2. **Layer 2 Controls:** Which specific switch security features would have prevented each attack? For each control, explain exactly why it would have blocked the attack — not just that it would have.
3. **802.1X as a Systemic Solution:** The bank is considering deploying 802.1X with Cisco ISE to all wired access ports. What would have been different in this specific incident if 802.1X had been in place? What are the deployment challenges for 802.1X in a mixed environment (some devices cannot authenticate — printers, VoIP phones, IoT)?
4. **Defense-in-Depth Argument:** A bank executive argues that deploying 802.1X is expensive and complex, and that requiring VPN for all internal traffic would solve the same problem. Evaluate this argument — is it correct, and what are the trade-offs?

**Citation:** Cite NIST SP 800-41 (firewall/ACL policy), CIS Benchmarks for Cisco IOS, or a peer-reviewed paper on Layer 2 security attacks (available via IEEE Xplore through TXWES West Library).

---

## 9. Supplemental Resources

**1. Cisco Security Configuration Guide — AAA**
https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_aaa/configuration/xe-16/sec-usr-aaa-xe-16-book.html
Authoritative Cisco IOS-XE configuration reference for AAA, TACACS+, and RADIUS implementation.

**2. NIST SP 800-53 — Security and Privacy Controls**
https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
Federal standard for security controls applicable to enterprise network infrastructure hardening.

**3. IETF RFC 2865 — Remote Authentication Dial In User Service (RADIUS)**
https://datatracker.ietf.org/doc/html/rfc2865
The original RADIUS protocol specification — essential reading for understanding the authentication exchange.

**4. Cisco White Paper — Control Plane Policing**
https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/116664-technote-qos-00.html
Technical explanation of CoPP design principles, rate-limit categories, and configuration examples.
