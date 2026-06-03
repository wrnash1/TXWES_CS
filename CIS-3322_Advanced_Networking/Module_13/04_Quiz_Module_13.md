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

End of Quiz — Module 13
