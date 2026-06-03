# Video Script: Module 13 — Network Security Fundamentals

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Estimated Duration: 22 Minutes

---

## Segment 1: Introduction (0:00–1:30)

Welcome back to CIS-3322 Advanced Networking. I'm Professor Nash, and today we cover Module 13: Network Security Fundamentals. This module aligns directly with CCNA 200-301 exam domain 5.0 — Security Fundamentals — which accounts for approximately 15% of your exam score.

By the end of this session you will be able to:

- Describe the AAA security framework and explain the difference between RADIUS and TACACS+
- Configure port security on Cisco switches
- Enable and verify DHCP snooping and Dynamic ARP Inspection
- Understand the role of 802.1X in network access control

Let's get started.

---

## Segment 2: The AAA Security Framework (1:30–5:00)

AAA stands for Authentication, Authorization, and Accounting. These three concepts form the backbone of network access control. Think of it as a three-stage checkpoint system for anyone or any device trying to use your network.

Authentication answers the question: Who are you? The user provides credentials — a username and password, a digital certificate, or a biometric token — and the system verifies those credentials against a database.

Authorization answers the question: What are you allowed to do? Once authenticated, the system checks your permission level. Are you a read-only user? An administrator? Can you access the finance VLAN?

Accounting answers the question: What did you do, and when? Every command entered, every session opened, and every resource accessed gets logged. This is critical for compliance, auditing, and incident response.

Cisco devices implement AAA through a combination of local configuration and external servers. The two dominant AAA protocols you must know for the CCNA exam are RADIUS and TACACS+.

### RADIUS

RADIUS was developed originally for dial-up ISP authentication and is defined in RFC 2865. Key characteristics:

- Uses UDP — port 1812 for authentication/authorization combined, port 1813 for accounting
- Encrypts only the password in the Access-Request packet; the username travels in cleartext
- Combines authentication and authorization into a single process
- Widely supported — used by wireless 802.1X, VPNs, and ISP environments

### TACACS+

TACACS+ is a Cisco-developed protocol that extends the original TACACS standard. Key characteristics:

- Uses TCP port 49 — more reliable transport than UDP
- Encrypts the entire packet body — more secure than RADIUS
- Separates authentication, authorization, and accounting into independent transactions
- Better suited for device administration — supports granular command-level authorization

### RADIUS vs. TACACS+ Comparison

| Feature | RADIUS | TACACS+ |
|---|---|---|
| Transport | UDP 1812/1813 | TCP 49 |
| Encryption | Password only | Full packet |
| AAA model | Combined AuthN/AuthZ | Separate |
| Primary use | Network access | Device admin |
| Vendor | Open standard | Cisco-centric |

Now let's configure RADIUS on a Cisco router:

```ios
Router(config)# aaa new-model
Router(config)# radius server CORP-RADIUS
Router(config-radius-server)# address ipv4 192.168.10.50 auth-port 1812 acct-port 1813
Router(config-radius-server)# key C1sc0R@dius!
Router(config-radius-server)# exit
Router(config)# aaa authentication login default group radius local
Router(config)# aaa authorization exec default group radius local
Router(config)# aaa accounting exec default start-stop group radius
```

The `aaa new-model` command is the master switch — it enables the AAA framework globally. Without it, no other AAA commands take effect. The `local` fallback at the end of each method list means: if the RADIUS server is unreachable, fall back to locally configured usernames.

---

## Segment 3: Switch Port Security (5:00–9:00)

Port security is a Layer 2 feature on Cisco Catalyst switches that restricts which MAC addresses can communicate on a given port. This prevents MAC flooding attacks and unauthorized device connections.

### How Port Security Works

Each switch port can be configured with a maximum number of allowed MAC addresses. When a frame arrives from a MAC address that is not in the allowed list and the maximum has been reached, the switch takes a configured violation action.

The three violation modes are:

- **Protect** — Frames from unknown MACs are dropped silently. No log message, no SNMP trap, port stays up. Least disruptive, also least visible.
- **Restrict** — Frames are dropped AND the violation counter increments AND a syslog message is generated. Port stays up. Good balance of security and visibility.
- **Shutdown** — The port is placed into err-disabled state immediately. You must manually recover the port or configure err-disable recovery. This is the default mode and the most secure.

### MAC Address Learning Methods

- **Static** — You manually specify allowed MAC addresses in configuration
- **Dynamic** — Switch learns MACs as traffic arrives; entries are lost on reboot
- **Sticky** — Switch dynamically learns MACs AND saves them to running-config; best production choice

Let's configure sticky port security on a switch access port:

```ios
Switch(config)# interface gigabitethernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 2
Switch(config-if)# switchport port-security mac-address sticky
Switch(config-if)# switchport port-security violation restrict
Switch(config-if)# end
```

Verify your configuration:

```ios
Switch# show port-security interface gigabitethernet 0/1
Switch# show port-security address
Switch# show interfaces gigabitethernet 0/1 status
```

If a port enters err-disabled state due to a shutdown violation, recover it manually:

```ios
Switch(config)# interface gigabitethernet 0/1
Switch(config-if)# shutdown
Switch(config-if)# no shutdown
```

Or configure automatic recovery:

```ios
Switch(config)# errdisable recovery cause psecure-violation
Switch(config)# errdisable recovery interval 300
```

---

## Segment 4: DHCP Snooping (9:00–13:00)

DHCP snooping is a Layer 2 security feature that protects your network from rogue DHCP servers. The attack scenario is straightforward: an attacker connects an unauthorized DHCP server to your network and hands out IP addresses pointing to their own default gateway — a classic man-in-the-middle attack.

### DHCP Snooping Concepts

DHCP snooping classifies switch ports as either trusted or untrusted.

- Trusted ports connect to legitimate DHCP servers or uplinks to other switches. DHCP responses (OFFER, ACK) are forwarded normally.
- Untrusted ports connect to end-user devices. DHCP responses arriving on untrusted ports are dropped automatically.

The switch builds a DHCP snooping binding table that maps MAC addresses to IP addresses, VLANs, and ports. This binding table is the foundation for Dynamic ARP Inspection, which we cover in the next segment.

### DHCP Snooping Configuration

```ios
Switch(config)# ip dhcp snooping
Switch(config)# ip dhcp snooping vlan 10,20,30
Switch(config)# no ip dhcp snooping information option
Switch(config)# interface gigabitethernet 0/24
Switch(config-if)# ip dhcp snooping trust
Switch(config-if)# exit
Switch(config)# interface range gigabitethernet 0/1 - 23
Switch(config-if-range)# ip dhcp snooping limit rate 15
Switch(config-if-range)# end
```

The `no ip dhcp snooping information option` command disables Option 82 insertion on untrusted ports. This is often required when the DHCP server does not support or expect Option 82 data — otherwise clients may fail to receive addresses.

The `ip dhcp snooping limit rate 15` command rate-limits DHCP traffic to 15 packets per second on untrusted ports, protecting against DHCP starvation attacks where an attacker exhausts the address pool.

Verify DHCP snooping:

```ios
Switch# show ip dhcp snooping binding
Switch# show ip dhcp snooping statistics
Switch# show ip dhcp snooping
```

---

## Segment 5: Dynamic ARP Inspection (13:00–17:00)

Dynamic ARP Inspection, or DAI, operates at Layer 2 and validates ARP packets using the DHCP snooping binding table. ARP poisoning attacks work by sending gratuitous ARP replies that associate the attacker's MAC address with a legitimate host's IP address. DAI stops these attacks by verifying every ARP packet against the binding table.

### How DAI Works

When an ARP packet arrives on an untrusted port, the switch checks the sender's IP-to-MAC binding against the DHCP snooping binding table. If the binding matches, the ARP packet is forwarded. If not, it is dropped and logged.

Trusted ports bypass DAI validation — typically uplinks and trunk ports connecting to distribution-layer switches.

### DAI Configuration

```ios
Switch(config)# ip arp inspection vlan 10,20,30
Switch(config)# interface gigabitethernet 0/24
Switch(config-if)# ip arp inspection trust
Switch(config-if)# exit
Switch(config)# interface range gigabitethernet 0/1 - 23
Switch(config-if-range)# ip arp inspection limit rate 100
Switch(config-if-range)# end
```

For hosts with static IP addresses — where no DHCP binding exists — create ARP ACLs:

```ios
Switch(config)# arp access-list STATIC-HOSTS
Switch(config-arp-acl)# permit ip host 192.168.10.1 mac host 0050.56AA.BBCC
Switch(config-arp-acl)# exit
Switch(config)# ip arp inspection filter STATIC-HOSTS vlan 10
```

Verify DAI:

```ios
Switch# show ip arp inspection
Switch# show ip arp inspection vlan 10
Switch# show ip arp inspection statistics
```

---

## Segment 6: 802.1X Network Access Control (17:00–20:30)

IEEE 802.1X is a port-based Network Access Control standard that requires devices to authenticate before gaining network access. It is the gold standard for enterprise LAN and wireless access control.

### The Three 802.1X Actors

Three entities participate in every 802.1X authentication exchange:

- **Supplicant** — The end device (laptop, phone, printer) requesting network access. Must have 802.1X client software installed.
- **Authenticator** — The network device (switch port or wireless access point) that enforces access control. It relays EAP messages between the supplicant and the authentication server without interpreting them.
- **Authentication Server** — Typically a RADIUS server such as Cisco ISE or Microsoft NPS. Validates credentials and returns an Accept or Reject message.

### EAP Methods

802.1X uses the Extensible Authentication Protocol as its authentication framework. Common EAP methods:

- **EAP-TLS** — Certificate-based; both client and server present certificates. Most secure; requires PKI infrastructure.
- **PEAP** — Protected EAP; only the server presents a certificate; client uses username/password inside a TLS tunnel. Most common in enterprise environments.
- **EAP-FAST** — Cisco-developed; uses Protected Access Credentials instead of certificates. Good for environments where deploying certificates is difficult.

### 802.1X Switch Configuration

```ios
Switch(config)# aaa new-model
Switch(config)# radius server ISE-SERVER
Switch(config-radius-server)# address ipv4 192.168.10.100 auth-port 1812 acct-port 1813
Switch(config-radius-server)# key Str0ngK3y!
Switch(config-radius-server)# exit
Switch(config)# aaa authentication dot1x default group radius
Switch(config)# aaa authorization network default group radius
Switch(config)# dot1x system-auth-control
Switch(config)# interface gigabitethernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# authentication port-control auto
Switch(config-if)# dot1x pae authenticator
Switch(config-if)# end
```

The `dot1x system-auth-control` command globally enables 802.1X on the switch. The `authentication port-control auto` command sets the port to require authentication before allowing traffic. The `dot1x pae authenticator` command designates the port as an 802.1X authenticator.

Verify 802.1X:

```ios
Switch# show dot1x all
Switch# show dot1x interface gigabitethernet 0/1 detail
Switch# show authentication sessions
```

---

## Segment 7: Module Summary (20:30–22:00)

Let's bring everything together. This module covered five critical network security technologies that appear on the CCNA 200-301 exam.

AAA provides the framework — Authentication (who you are), Authorization (what you can do), Accounting (what you did). RADIUS uses UDP and combines AuthN/AuthZ; TACACS+ uses TCP, encrypts fully, and separates all three functions independently.

Port Security locks down Layer 2 by restricting which MAC addresses can use a switch port. Sticky learning is the most practical production setting. Violation modes range from silent drops (protect) to err-disabled shutdown.

DHCP Snooping prevents rogue DHCP servers by classifying ports as trusted or untrusted and rate-limiting DHCP traffic. It builds the binding table used by DAI.

Dynamic ARP Inspection uses the DHCP snooping binding table to validate ARP packets and prevent ARP poisoning attacks.

802.1X provides port-based access control using the EAP framework. Supplicants authenticate through the switch (authenticator) to a RADIUS server before gaining access.

For your lab this module, you will configure all five features in a single Packet Tracer topology. Your reading guide has full command reference tables. The quiz covers distinguishing characteristics between these protocols.

Next module we move to Wireless Networking — 802.11 standards, WPA3, and Cisco WLC configuration. See you there.

---

Script End — Module 13 | Approximate runtime: 22 minutes
