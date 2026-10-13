# Video Script: Module 11 — DHCP and DNS Configuration

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Cisco CCNA 200-301

---

## Introduction (0:00–1:30)

Welcome back to CIS-3322 Advanced Networking. I'm Professor Nash. Module 11 covers two services that every IP network depends on: DHCP — the Dynamic Host Configuration Protocol — and DNS — the Domain Name System.

[SHOW SLIDE: "Module 11 — DHCP and DNS Configuration"]

DHCP automates IP address assignment so that administrators do not manually configure every device on the network. DNS translates human-readable hostnames into IP addresses so users can type names instead of memorizing numbers. These two services are so fundamental that a network without them is nearly unusable, regardless of how well-designed the routing and switching infrastructure might be.

By the end of this module you will be able to:

- Configure a Cisco IOS router as a DHCP server

- Configure a DHCP relay agent for multi-subnet environments

- Explain DHCP snooping and why it prevents rogue DHCP attacks

- Describe the DNS resolution process step by step

- Understand split-horizon DNS and when it is used

- Troubleshoot DHCP and DNS failures using IOS verification commands

[PAUSE — 3 seconds]

Let's start with DHCP.

---

## Section 1: DHCP Fundamentals (1:30–4:00)

[SHOW SLIDE: "DHCP — The DORA Process"]

DHCP uses a four-message exchange to assign an IP address to a client. The process is called DORA:

**Discover**: the client broadcasts to find a DHCP server. Source 0.0.0.0, destination 255.255.255.255.

**Offer**: the server responds with an available IP address and lease parameters.

**Request**: the client broadcasts to confirm it wants the offered address and to formally request it.

**Acknowledge**: the server confirms the assignment and provides the full configuration: IP address, subnet mask, default gateway, DNS server, and lease time.

[SHOW SLIDE: "DORA Packet Flow Diagram"]

Because DHCP Discover and Request are broadcasts, they do not cross router boundaries by default. This is why each subnet typically needs either a local DHCP server or a relay agent — also called a DHCP helper — to forward DHCP broadcasts to a centralized server.

[PAUSE — 3 seconds]

---

## Section 2: Cisco IOS DHCP Server Configuration (4:00–8:00)

[SHOW SLIDE: "Cisco DHCP Server — Pool Configuration"]

Cisco IOS routers can function as DHCP servers. The configuration centers on defining one or more DHCP pools, each representing a subnet's address allocation.

**Step 1: Exclude addresses that should not be assigned dynamically** (static devices, gateways, servers):

```text
Router(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.10
```

This reserves 192.168.1.1 through .10 from the pool — they will never be handed out dynamically.

**Step 2: Create a DHCP pool:**

```text
Router(config)# ip dhcp pool LAN_POOL
Router(dhcp-config)# network 192.168.1.0 255.255.255.0
Router(dhcp-config)# default-router 192.168.1.1
Router(dhcp-config)# dns-server 8.8.8.8 8.8.4.4
Router(dhcp-config)# domain-name txwes.edu
Router(dhcp-config)# lease 7
```

[SHOW SLIDE: "DHCP Pool Parameters Explained"]

The `network` command defines which subnet this pool serves. `default-router` is the gateway IP sent to clients. `dns-server` specifies one or more DNS server addresses. `domain-name` sets the DNS search domain appended to unqualified hostnames. `lease` sets the duration in days (default is 1 day).

Verification commands:

```text
Router# show ip dhcp pool
Router# show ip dhcp binding
Router# show ip dhcp conflict
```

`show ip dhcp binding` is the most useful — it lists every active lease with the MAC address of the client, the assigned IP, and the lease expiration time.

[PAUSE — 3 seconds]

---

## Section 3: DHCP Relay Agent (8:00–11:00)

[SHOW SLIDE: "DHCP Relay — ip helper-address"]

When a DHCP server serves multiple subnets, you need a relay agent on each subnet's gateway router to forward DHCP broadcasts to the server. The Cisco IOS command is `ip helper-address`.

[SHOW TOPOLOGY: Three subnets. Central DHCP server at 10.0.0.5. R1 Gi0/0 connected to 192.168.1.0/24. R1 Gi0/1 connected to 192.168.2.0/24. DHCP server on separate segment.]

On the interface facing the subnet that needs DHCP:

```text
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip helper-address 10.0.0.5
```

When a DHCP Discover broadcast arrives on Gi0/0, the router converts it from a broadcast to a unicast packet addressed to 10.0.0.5 and forwards it. The DHCP server sees the incoming interface IP address (10.0.0.5 would receive it with a giaddr field showing the relay interface IP) and knows which pool to use for that subnet.

The server responds directly to the relay agent, which then delivers the Offer back to the client subnet.

[SHOW SLIDE: "ip helper-address Details"]

`ip helper-address` by default forwards eight UDP broadcast services, not just DHCP. It also forwards DNS (53), TFTP (69), time (37), NetBIOS name service (137), NetBIOS datagram service (138), and a few others. If you want to restrict it to DHCP only, you can configure `no ip forward-protocol` for each unwanted service, but for most environments the default forwarding is acceptable.

---

## Section 4: DHCP Snooping (11:00–13:30)

[SHOW SLIDE: "DHCP Snooping — Preventing Rogue DHCP Servers"]

DHCP snooping is a Layer 2 security feature on Cisco switches that prevents rogue DHCP servers from handing out invalid IP configurations to clients. Without snooping, any device on the network could respond to DHCP Discover messages — sending clients incorrect gateways for man-in-the-middle attacks.

DHCP snooping works by classifying switch ports as trusted or untrusted:

- **Trusted ports**: ports connected to legitimate DHCP servers or uplinks to other switches. DHCP server responses are allowed through.
- **Untrusted ports**: ports connected to client devices. DHCP Offer and Acknowledge messages arriving on untrusted ports are dropped.

Configuration on a Cisco Catalyst switch:

```text
Switch(config)# ip dhcp snooping
Switch(config)# ip dhcp snooping vlan 10
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# ip dhcp snooping trust
```

All other ports default to untrusted after enabling snooping.

[SHOW SLIDE: "DHCP Snooping Binding Table"]

DHCP snooping builds a binding table mapping client MAC addresses to their assigned IP addresses and switch port. This table is used by downstream security features like Dynamic ARP Inspection (DAI) and IP Source Guard.

---

## Section 5: DNS Resolution Process (13:30–17:00)

[SHOW SLIDE: "DNS Resolution — Step by Step"]

The Domain Name System translates fully qualified domain names (FQDNs) into IP addresses. Here is the step-by-step resolution process for a client querying `www.example.com`:

**Step 1**: Client checks its local DNS cache. If a recent record exists, it uses it immediately with no network traffic.

**Step 2**: If not cached, the client sends a recursive query to its configured DNS resolver (usually the ISP's DNS server or an enterprise DNS server).

**Step 3**: The resolver checks its own cache. If cached, it returns the answer immediately.

**Step 4**: If not cached, the resolver sends an iterative query to a root name server. The root server responds with the address of the .com TLD (top-level domain) server.

**Step 5**: The resolver queries the .com TLD server. The TLD server responds with the address of the authoritative name server for example.com.

**Step 6**: The resolver queries the authoritative server for example.com. The authoritative server returns the A record (IPv4) or AAAA record (IPv6) for www.example.com.

**Step 7**: The resolver caches the result and returns it to the client. The client connects to the resolved IP address.

[SHOW SLIDE: "DNS Record Types"]

Common DNS record types tested on the CCNA:

| Record Type | Purpose                                           |
|-------------|---------------------------------------------------|
| A           | Maps hostname to IPv4 address                     |
| AAAA        | Maps hostname to IPv6 address                     |
| CNAME       | Alias — maps one hostname to another hostname     |
| MX          | Mail exchanger — identifies mail servers          |
| PTR         | Reverse lookup — maps IP address to hostname      |
| NS          | Name server record — identifies authoritative DNS |

---

## Section 6: Split-Horizon DNS (17:00–19:00)

[SHOW SLIDE: "Split-Horizon DNS — Two Views of the Same Name"]

Split-horizon DNS, also called split-brain DNS, provides different DNS responses to queries depending on the source of the query. Internal clients get the internal IP address of a resource. External clients get the public IP address.

Example: a company hosts `mail.company.com`. Internally, the mail server is at 10.1.5.20. Externally, the public IP is 203.0.113.20.

With split-horizon DNS:

- Internal clients querying `mail.company.com` receive 10.1.5.20 — they connect directly to the internal server without traversing NAT.
- External clients querying `mail.company.com` receive 203.0.113.20 — they connect to the public IP which NAT forwards to the internal server.

[SHOW SLIDE: "Why Split-Horizon DNS Matters"]

Without split-horizon DNS, internal clients querying a public DNS server would receive 203.0.113.20. Their traffic would exit to the router's outside interface, hit NAT, and either fail (if hairpin NAT is not configured) or take a suboptimal path back to the internal server. Split-horizon eliminates this by ensuring internal clients always get the optimal (internal) path.

---

## Section 7: DHCP and DNS Troubleshooting (19:00–21:30)

[SHOW SLIDE: "DHCP Troubleshooting Commands"]

Key DHCP troubleshooting commands on a Cisco IOS router:

```text
Router# show ip dhcp binding
Router# show ip dhcp pool
Router# show ip dhcp conflict
Router# debug ip dhcp server events
```

`show ip dhcp conflict` lists addresses the DHCP server found already in use via ping before assigning them. Conflicts indicate manually configured devices using addresses in the dynamic range.

`debug ip dhcp server events` shows the DISCOVER, OFFER, REQUEST, and ACK message exchange in real time. This is invaluable when a client claims it is not receiving an offer.

[SHOW SLIDE: "DNS Troubleshooting — nslookup and ping"]

Key DNS troubleshooting steps:

- `nslookup <hostname>` from a client — resolves a name and shows which DNS server answered
- `ping <hostname>` — confirms both DNS resolution and IP reachability
- Check `/etc/resolv.conf` (Linux) or ipconfig /all (Windows) to verify the DNS server address assigned by DHCP
- On the router: `ip name-server <dns-ip>` configures DNS for the router itself

[PAUSE — 3 seconds]

---

## Conclusion (21:30–23:00)

[SHOW SLIDE: "Module 11 Summary"]

Let's wrap up Module 11. Today you learned:

- DHCP uses the DORA exchange: Discover, Offer, Request, Acknowledge

- Cisco IOS DHCP server is configured with `ip dhcp pool` and `ip dhcp excluded-address`

- DHCP relay (`ip helper-address`) forwards broadcasts from clients to a centralized DHCP server

- DHCP snooping prevents rogue DHCP servers by classifying ports as trusted or untrusted

- DNS resolution involves local cache, recursive resolver, root, TLD, and authoritative servers

- Split-horizon DNS provides different responses to internal and external clients

- Troubleshoot with `show ip dhcp binding`, `debug ip dhcp server events`, and nslookup

[SHOW SLIDE: "CCNA Exam Focus Areas"]

For the exam: know the ip helper-address command, the DORA process, DHCP snooping trusted/untrusted port distinction, and the DNS resolution sequence. These all appear frequently in scenario-based questions.

See you in Module 12 where we cover WAN Technologies and Remote Access. Take care.

---

*End of Module 11 Video Script*
