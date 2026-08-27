# Quiz: Module 13 — Network Security Fundamentals

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points.

---

## Question 1

A network administrator needs to implement device administration AAA with command-level authorization on Cisco routers. Which protocol best meets this requirement?

A. RADIUS using UDP port 1812

B. TACACS+ using TCP port 49

C. RADIUS using TCP port 49

D. TACACS+ using UDP port 1813

Correct Answer: B — TACACS+ uses TCP port 49 and supports granular command-level authorization, making it the preferred choice for device administration. RADIUS combines authentication and authorization and does not support per-command authorization.

Distractor Analysis:

* A — RADIUS does use UDP 1812 for authentication, but it cannot authorize individual commands.
* C — RADIUS uses UDP, not TCP. This is a common exam trap.
* D — TACACS+ uses TCP, not UDP. Port 1813 belongs to RADIUS accounting.

---

## Question 2

Which statement correctly describes the encryption behavior of RADIUS compared to TACACS+?

A. RADIUS encrypts the entire packet; TACACS+ encrypts only the password.

B. RADIUS encrypts only the password field; TACACS+ encrypts the entire packet body.

C. Both protocols encrypt only the username and password.

D. Neither protocol uses encryption; both rely on TLS for security.

Correct Answer: B — RADIUS encrypts only the password in the Access-Request packet using MD5. The username and other attributes travel in cleartext. TACACS+ encrypts the entire packet payload, providing stronger confidentiality.

Distractor Analysis:

* A — This reverses the correct behavior of each protocol.
* C — RADIUS does not encrypt the username; only the password is protected.
* D — Both protocols have built-in encryption mechanisms; TACACS+ is the more comprehensive of the two.

---

## Question 3

A switch port is configured with `switchport port-security violation restrict`. What happens when a frame from an unknown MAC address arrives and the maximum MAC count has already been reached?

A. The port shuts down and enters err-disabled state.

B. The frame is forwarded and a log message is generated.

C. The frame is dropped and a syslog message is generated; the port remains up.

D. The frame is dropped silently with no log entry; the port remains up.

Correct Answer: C — In restrict mode, frames from violating MAC addresses are dropped, the violation counter increments, and a syslog message is sent. The port remains operational. This differentiates restrict from protect (silent drop, no log) and shutdown (port goes err-disabled).

Distractor Analysis:

* A — Describes the shutdown violation mode, not restrict.
* B — Frames are never forwarded during a violation; they are dropped in all three modes.
* D — Describes the protect violation mode, which drops silently without logging.

---

## Question 4

An administrator configures port security with `switchport port-security mac-address sticky`. Which of the following is true?

A. The switch learns MAC addresses dynamically and stores them only in RAM; they are lost on reboot.

B. The switch learns MAC addresses dynamically and saves them to the running-configuration.

C. The administrator must manually enter all allowed MAC addresses in the configuration.

D. The switch broadcasts a query to learn which MAC addresses are authorized.

Correct Answer: B — Sticky MAC learning is a hybrid approach: the switch learns MAC addresses dynamically from incoming frames and immediately writes them to the running-configuration as static entries. They persist through reboots only if the config is saved with `copy running-config startup-config`.

Distractor Analysis:

* A — Describes dynamic MAC learning without sticky. Dynamic entries are volatile.
* C — Describes static MAC address configuration, which requires manual entry.
* D — No such broadcast mechanism exists in port security.

---

## Question 5

DHCP snooping is enabled on a switch. A DHCP OFFER packet arrives on a port that has NOT been configured as a trusted port. What action does the switch take?

A. The switch forwards the OFFER to the requesting client.

B. The switch drops the OFFER packet and increments the snooping statistics counter.

C. The switch forwards the OFFER but generates a warning log message.

D. The switch places the port in err-disabled state.

Correct Answer: B — DHCP snooping drops DHCP server messages (OFFER, ACK, NAK) arriving on untrusted ports. This is the core mechanism that blocks rogue DHCP servers. The packet is dropped and the statistics counter increments. The port is not err-disabled.

Distractor Analysis:

* A — Forwarding the OFFER would defeat the purpose of DHCP snooping entirely.
* C — The packet is dropped, not forwarded with a warning.
* D — DHCP snooping does not place ports into err-disabled state; it only drops offending packets.

---

## Question 6

Which command enables DHCP snooping on VLAN 20 only?

A. `ip dhcp snooping vlan 20`

B. `ip dhcp snooping enable vlan 20`

C. `dhcp snooping vlan 20`

D. `ip dhcp snooping trusted vlan 20`

Correct Answer: A — The correct syntax is `ip dhcp snooping vlan 20`. DHCP snooping must also be enabled globally with `ip dhcp snooping` before the per-VLAN command takes effect. The other options use incorrect syntax that Cisco IOS does not recognize.

Distractor Analysis:

* B — `enable` is not part of the DHCP snooping command syntax.
* C — Missing the `ip` prefix; IOS will not accept this command.
* D — `trusted` is not a keyword here; trust is configured per interface with `ip dhcp snooping trust`.

---

## Question 7

Dynamic ARP Inspection (DAI) is configured on VLAN 30. A host with a statically assigned IP address sends an ARP request, but there is no entry in the DHCP snooping binding table for this host. What happens?

A. The ARP packet is forwarded because static hosts are always trusted.

B. The ARP packet is dropped because no binding table entry exists.

C. The ARP packet is forwarded only if an ARP ACL explicitly permits the IP-MAC binding.

D. The ARP packet triggers creation of a new DHCP binding table entry.

Correct Answer: C — DAI validates ARP packets against the DHCP snooping binding table. Hosts with static IPs have no DHCP binding. For these hosts, the administrator must create an ARP ACL that explicitly permits their IP-MAC binding and apply it to the VLAN with `ip arp inspection filter ACL-NAME vlan X`. Without the ACL, the ARP is dropped.

Distractor Analysis:

* A — DAI does not automatically trust static hosts; they must be explicitly permitted via ARP ACL.
* B — Technically correct that the ARP is dropped without a binding, but C is the more actionable and complete answer.
* D — DAI does not create DHCP bindings; those come from actual DHCP exchanges only.

---

## Question 8

In an 802.1X deployment, which device is responsible for relaying EAP messages between the supplicant and the authentication server?

A. The RADIUS server

B. The supplicant

C. The authenticator

D. The DHCP server

Correct Answer: C — The authenticator (typically a switch port or wireless access point) relays EAP messages transparently between the supplicant and the authentication server. It does not interpret the EAP payload — it encapsulates EAP frames in RADIUS packets and forwards them to the authentication server.

Distractor Analysis:

* A — The RADIUS server is the authentication server, not the relay; it terminates the EAP exchange.
* B — The supplicant is the end device requesting access; it initiates EAP but does not relay it.
* D — The DHCP server has no role in 802.1X authentication.

---

## Question 9

Which global command is required on a Cisco switch before per-interface 802.1X configuration will take effect?

A. `aaa new-model`

B. `dot1x system-auth-control`

C. `authentication port-control auto`

D. `radius-server host 10.0.0.50`

Correct Answer: B — `dot1x system-auth-control` is the global command that enables 802.1X authentication on the switch. Without it, per-interface 802.1X commands are accepted but have no effect. Note that `aaa new-model` is also a prerequisite, but the question asks specifically which command enables the 802.1X system globally.

Distractor Analysis:

* A — `aaa new-model` enables the AAA framework and is a prerequisite, but it does not specifically enable the 802.1X subsystem.
* C — `authentication port-control auto` is a per-interface command, not a global enabler.
* D — `radius-server host` is an older deprecated syntax and addresses server connectivity, not 802.1X enablement.

---

## Question 10

A switch port is in err-disabled state due to a port-security violation. The administrator wants the port to recover automatically after 5 minutes. Which configuration achieves this?

A. `switchport port-security violation recover 300`

B. `errdisable recovery cause psecure-violation` and `errdisable recovery interval 300`

C. `spanning-tree portfast` and `errdisable recovery interval 300`

D. `no switchport port-security violation shutdown`

Correct Answer: B — Automatic err-disable recovery requires two commands: `errdisable recovery cause psecure-violation` specifies that port-security violations are subject to automatic recovery, and `errdisable recovery interval 300` sets the recovery timer to 300 seconds (5 minutes). Both commands are required together.

Distractor Analysis:

* A — `switchport port-security violation recover` is not valid IOS syntax.
* C — PortFast is a spanning-tree feature unrelated to err-disable recovery from port-security violations.
* D — Changing the violation mode does not recover a port already in err-disabled state; it only affects future violations.

---

---

## Question 11

An engineer runs `show port-security interface GigabitEthernet0/3` and sees the violation count is 47, but the port is still operational. Which violation mode is configured?

A. Shutdown

B. Protect

C. Restrict

D. Err-disabled

Correct Answer: C — In restrict mode, the port remains operational, frames from unknown MACs are dropped, and the violation counter increments with each offending frame. A count of 47 confirms many violations have occurred while the port stayed up. In shutdown mode, the first violation drops the port to err-disabled. In protect mode, the port also stays up but the counter does not increment.

Distractor Analysis:

* A — Shutdown mode would have placed the port in err-disabled after the very first violation, so a count of 47 would never accumulate while the port remained up.
* B — Protect mode drops frames silently and does not increment the violation counter.
* D — Err-disabled is a port state, not a violation mode. It results from shutdown mode being triggered.

---

## Question 12

An organization wants to authenticate network users using their Active Directory credentials when they connect to the corporate wireless network. Which combination of technologies accomplishes this?

A. Port security with sticky MAC and TACACS+ for device administration

B. 802.1X with PEAP and a RADIUS server integrated with Active Directory

C. DHCP snooping with an ARP ACL mapped to Active Directory user objects

D. TACACS+ with command authorization applied to the wireless controller

Correct Answer: B — 802.1X is the IEEE standard for port-based (and wireless) network access control. PEAP (Protected EAP) allows users to authenticate with username/password credentials (Active Directory accounts) without requiring client-side certificates. A RADIUS server (such as Cisco ISE or Windows NPS) integrates with Active Directory to validate the credentials. This is the standard enterprise wireless authentication design.

Distractor Analysis:

* A — Port security with sticky MAC is a Layer 2 protection feature for switch ports. It does not authenticate users and has no integration with Active Directory.
* C — DHCP snooping and ARP ACLs protect against Layer 2 attacks but have no user identity or Active Directory integration capability.
* D — TACACS+ command authorization controls what IOS commands administrators can run on network devices. It is not used for end-user wireless authentication.

---

## Question 13

Which statement correctly describes the difference between the `protect` and `restrict` port-security violation modes?

A. Protect drops frames and sends a syslog message; restrict drops frames silently.

B. Restrict drops frames and sends a syslog message; protect drops frames silently without logging.

C. Both modes send syslog messages, but only restrict shuts down the port.

D. Protect increments the violation counter; restrict does not.

Correct Answer: B — Restrict mode drops violating frames, increments the violation counter, and generates a syslog message. Protect mode drops violating frames silently — no syslog message is generated and the violation counter does not increment. This makes protect the quieter of the two modes. Shutdown is the third mode and places the port in err-disabled state.

Distractor Analysis:

* A — This reverses the behaviors of protect and restrict.
* C — Protect mode does not send syslog messages, and neither mode shuts down the port. Shutdown is the mode that err-disables the port.
* D — It is restrict that increments the violation counter, not protect. Protect provides no counter feedback.

---

## Question 14

A network engineer configures `aaa authentication login default group tacacs+ local` on a Cisco router. The TACACS+ server is unreachable at login time. What happens when an administrator tries to log in?

A. Login is denied because TACACS+ is the only configured authentication method.

B. The router falls back to local username/password authentication.

C. The router prompts for the enable password instead of a username.

D. The router enters a lockout mode and must be recovered from the console.

Correct Answer: B — The AAA method list `group tacacs+ local` defines a fallback sequence. The router first attempts TACACS+ authentication. If the TACACS+ server is unreachable (not just returning a reject), the router falls back to the local username database. This ensures administrators can still log in during TACACS+ outages using locally defined credentials. Note: if the server returns an explicit reject, the local fallback is NOT used — fallback only triggers on server unreachability.

Distractor Analysis:

* A — Login would only be denied if TACACS+ were the sole method and no fallback were configured (e.g., `group tacacs+ none`).
* C — The enable password is not part of the AAA login authentication process. It applies to privilege escalation (level 15), not initial login.
* D — Cisco AAA does not enter a lockout mode due to TACACS+ unavailability. The fallback mechanism prevents this scenario.

---

## Question 15

Which port-security command causes the switch to store dynamically learned MAC addresses in the running-configuration so they survive a reboot if saved?

A. `switchport port-security mac-address sticky`

B. `switchport port-security mac-address dynamic`

C. `switchport port-security mac-address persistent`

D. `ip dhcp snooping binding sticky`

Correct Answer: A — The `switchport port-security mac-address sticky` command enables sticky learning. The switch dynamically learns MAC addresses from incoming frames and immediately writes them as static entries to the running-configuration. Issuing `copy running-config startup-config` saves them to NVRAM so they persist through reboots. Without this, dynamically learned MACs are lost when the switch reloads.

Distractor Analysis:

* B — `mac-address dynamic` is not a valid port-security keyword. Dynamic learning is the default when sticky is not configured, but there is no explicit `dynamic` keyword in this command.
* C — `mac-address persistent` is not a valid Cisco IOS command. Persistence is achieved through the sticky keyword combined with saving the configuration.
* D — `ip dhcp snooping binding sticky` is not a valid command. DHCP snooping has its own binding database separate from port-security MAC learning.

---

## Question 16

An attacker sends a flood of forged DHCP Discover packets to exhaust the DHCP server's address pool. What attack type is this, and which Cisco security feature mitigates it?

A. ARP poisoning; mitigated by Dynamic ARP Inspection

B. DHCP starvation attack; mitigated by DHCP snooping rate limiting

C. MAC flooding; mitigated by port security maximum MAC count

D. Rogue DHCP server attack; mitigated by DHCP snooping trust ports

Correct Answer: B — A DHCP starvation attack sends thousands of DHCP Discover packets with spoofed source MAC addresses, consuming all available addresses in the DHCP pool. Legitimate clients then receive no IP addresses. DHCP snooping with rate limiting (`ip dhcp snooping limit rate`) on untrusted ports restricts the number of DHCP packets per second from any single port, preventing a single attacker from flooding the server.

Distractor Analysis:

* A — ARP poisoning exploits the ARP protocol to redirect traffic, not to exhaust the DHCP pool. DAI protects against ARP attacks, not DHCP starvation.
* C — MAC flooding targets the switch's CAM table to cause it to broadcast traffic, not the DHCP server's address pool. Port security mitigates MAC flooding.
* D — A rogue DHCP server attack involves an unauthorized server handing out incorrect IP configuration. The scenario describes an address exhaustion attack, not a rogue server attack.

---

## Question 17

An organization deploys 802.1X on all switch access ports. A network printer does not support 802.1X. Which feature allows the printer to access the network without disabling 802.1X on its port?

A. VLAN hopping using double-tagging bypass

B. MAC Authentication Bypass (MAB)

C. Force-authorized mode on the printer port only

D. Sticky MAC learning with the printer's MAC pre-configured

Correct Answer: B — MAC Authentication Bypass (MAB) allows non-802.1X-capable devices (printers, IP phones, IoT devices) to authenticate using their MAC address. When the switch detects that a device is not responding to EAP identity requests, it falls back to MAB and sends the device's MAC address to the RADIUS server for validation. The RADIUS server can then permit or deny access based on the MAC, and optionally assign a VLAN.

Distractor Analysis:

* A — VLAN hopping is an attack technique, not a legitimate access method for non-802.1X devices.
* C — Setting a port to force-authorized bypasses 802.1X entirely, granting network access to any device connected to that port. This removes security rather than providing controlled access for the printer.
* D — Pre-configuring the sticky MAC address controls which MAC can connect but still blocks the printer if 802.1X is required before the port opens. Sticky MAC is a port security feature, not an 802.1X bypass mechanism.

---

## Question 18

A Cisco switch has `ip arp inspection vlan 10` configured. A host in VLAN 10 has a statically assigned IP of 10.10.10.100 and MAC address 0011.2233.4455. No DHCP binding exists for this host. An ARP request from this host is dropped by DAI. What is the correct fix?

A. Add `ip dhcp snooping trust` to the port the static host is connected to.

B. Create an ARP ACL permitting the host's IP-MAC binding and apply it to VLAN 10 with `ip arp inspection filter`.

C. Assign the static host a DHCP reservation so a binding table entry is created.

D. Disable DAI on VLAN 10 to allow static hosts to use ARP normally.

Correct Answer: B — For hosts with static IP addresses, no DHCP binding exists in the snooping database. DAI cannot validate their ARP packets against the binding table, so they are dropped. The correct solution is to create an explicit ARP ACL: `arp access-list STATIC_HOSTS` with `permit ip host 10.10.10.100 mac host 0011.2233.4455`, then apply it with `ip arp inspection filter STATIC_HOSTS vlan 10`. This tells DAI to use the ACL as the authoritative source for that host.

Distractor Analysis:

* A — Trusting the port would bypass DAI for all devices on that port — including potential attackers. The correct approach preserves DAI's protection while creating a specific exemption for the known static host.
* C — Adding a DHCP reservation would create a binding only when the host requests an address via DHCP. A host with a static IP never sends a DHCP Discover, so no binding is ever created.
* D — Disabling DAI on the VLAN removes ARP inspection protection for all hosts on the VLAN, not just the static host. This eliminates the security feature entirely.

---

## Question 19

After enabling DHCP snooping on a Cisco switch, DHCP clients on VLAN 20 start receiving DHCP Offers with Option 82 (relay agent information) that the DHCP server is rejecting. What is the most likely cause and fix?

A. The DHCP server does not support Option 82 — disable DHCP snooping on VLAN 20.

B. DHCP snooping is inserting Option 82 on a switch without a relay agent present — add `no ip dhcp snooping information option` to suppress Option 82 insertion.

C. The DHCP server is a rogue server that does not understand Option 82 — configure a trusted port toward the legitimate server.

D. Option 82 requires the switch to be the DHCP relay — configure `ip helper-address` on the SVI.

Correct Answer: B — When DHCP snooping is enabled, Cisco switches insert Option 82 (relay agent information) into all DHCP packets by default — even when the switch is not acting as a DHCP relay agent. Many DHCP servers are configured to reject packets with Option 82 if they did not expect a relay agent. The fix is `no ip dhcp snooping information option` in global configuration, which prevents the switch from inserting Option 82. This is a common "first day" issue when deploying DHCP snooping.

Distractor Analysis:

* A — Disabling snooping removes the entire security protection. The correct fix is suppressing Option 82 insertion while keeping snooping active.
* C — The presence of Option 82 is caused by the switch itself, not by a rogue server. The rogue server issue is a separate scenario solved by trust port configuration.
* D — Option 82 is automatically inserted by snooping regardless of whether a helper-address is configured. Adding `ip helper-address` would make the switch a relay agent but does not fix the Option 82 rejection issue.

---

## Question 20

A network administrator wants to verify that 802.1X authentication is actively enforcing access control on a specific switch port. Which command provides the current authentication state of the port including whether the client is authenticated?

A. `show interfaces GigabitEthernet0/5`

B. `show authentication sessions interface GigabitEthernet0/5 detail`

C. `show dot1x interface GigabitEthernet0/5`

D. `show port-security interface GigabitEthernet0/5`

Correct Answer: B — `show authentication sessions interface GigabitEthernet0/5 detail` provides a comprehensive view of the authentication state for a specific port including: the client MAC address, the assigned VLAN, the authentication method used (802.1X, MAB, or WebAuth), the current session status (Authz Success, Authz Failed), and the applied policies from the RADIUS server. This is the primary troubleshooting command for 802.1X issues.

Distractor Analysis:

* A — `show interfaces` displays physical layer statistics, speed, duplex, and error counters. It has no awareness of 802.1X authentication state.
* C — `show dot1x interface` shows 802.1X-specific information for the port, but `show authentication sessions` provides a more complete view that also covers MAB and other authentication methods.
* D — `show port-security interface` displays port-security MAC address information and violation counts. It is not related to 802.1X authentication state.

---

End of Quiz — Module 13
