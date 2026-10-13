# Video Script: Module 09 - Networking Configuration (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 11 minutes
**Part:** 2 of 2 - Diagnostics and Troubleshooting

---

### Opening

Welcome back to Part 2 of Module 09. In Part 1 we covered ip addr, NetworkManager with nmcli,
routing, and DNS resolution. In Part 2 we cover network diagnostic tools: ping, traceroute,
ss, and tcpdump. We also cover hostname configuration, common failure scenarios, and basic
network troubleshooting methodology.

---

### Section 1: Connectivity Testing with ping

[SHOW TERMINAL]

```bash
ping -c 4 8.8.8.8
```

Sends 4 ICMP echo requests to 8.8.8.8 (Google's public DNS). The -c flag limits the count;
without it, ping runs until interrupted.

Interpreting output:
- Round-trip time (rtt) shows network latency
- Packet loss percentage shows reliability
- "Network unreachable" means no route to the destination
- "Request timeout" means the host may be up but not responding to ICMP, or is unreachable

```bash
ping -c 4 localhost
ping -c 4 192.168.1.1
ping -c 4 8.8.8.8
```

A systematic connectivity test:
1. Ping localhost — confirms TCP/IP stack is working
2. Ping the default gateway — confirms local network connectivity
3. Ping a public IP — confirms internet routing
4. Ping a hostname — confirms DNS resolution

If step 3 works but step 4 fails, the problem is DNS, not connectivity.

---

### Section 2: Path Tracing with traceroute

[SHOW TERMINAL]

```bash
traceroute 8.8.8.8
```

Shows each router hop between your system and the destination. Each line shows:
- Hop number
- Router IP address (or hostname if resolvable)
- Round-trip times for three probes

```bash
traceroute -n 8.8.8.8
```

-n suppresses DNS lookups on hop addresses. Faster output on networks with slow reverse DNS.

Interpreting traceroute output:
- * * * means the router does not respond to traceroute probes (ICMP TTL exceeded).
  This does not necessarily mean the path is broken — many routers silently drop these.
- If the path stops at a specific hop, that hop or the link after it may be the problem.

```bash
sudo apt install traceroute
```

traceroute may not be installed by default.

---

### Section 3: Port and Socket Information with ss

[SHOW TERMINAL]

```bash
ss -tuln
```

t=TCP, u=UDP, l=listening, n=numeric (no name resolution)

This shows all listening sockets. Essential for verifying that services are bound to the
expected ports and interfaces.

```bash
ss -tulnp
```

p=processes. Shows which process is listening on each port (requires root for processes
owned by other users).

```bash
sudo ss -tulnp
```

With sudo, shows the process name and PID for each listening socket.

```bash
ss -tan
```

Shows all TCP connections in all states (LISTEN, ESTABLISHED, TIME_WAIT, etc.).

Interpreting ss output columns:
- Netid: TCP or UDP
- State: LISTEN, ESTAB (established), etc.
- Local Address:Port: the interface and port on this system
- Peer Address:Port: the remote address (0.0.0.0:* for listeners)
- Process: the process listening (with -p)

```bash
ss -tulnp | grep :22
```

Verify that sshd is listening on port 22.

ss is the modern replacement for netstat. Both commands produce similar output; ss is
significantly faster on systems with many connections.

---

### Section 4: Packet Capture with tcpdump

[SHOW TERMINAL]

```bash
sudo tcpdump -i ens33 -n
```

Capture all packets on ens33. -n suppresses DNS lookup. Press Ctrl+C to stop.

```bash
sudo tcpdump -i ens33 -n port 80
```

Capture only traffic on port 80 (HTTP).

```bash
sudo tcpdump -i ens33 -n host 8.8.8.8
```

Capture only traffic to or from a specific host.

```bash
sudo tcpdump -i ens33 -n -c 20 -w /tmp/capture.pcap
```

Capture 20 packets and save to a file for analysis with Wireshark.

tcpdump output format: timestamp source_ip.port > dest_ip.port: protocol_info

tcpdump is a powerful diagnostic tool. For the exam, know how to specify an interface (-i),
suppress DNS (-n), filter by port (port N), filter by host (host IP), and save to a file (-w).

---

### Section 5: Hostname Configuration

[SHOW TERMINAL]

```bash
hostname
```

Shows the current hostname. This is the system's identity on the network.

```bash
cat /etc/hostname
```

The file where the persistent hostname is stored. Contains just the hostname, one line.

```bash
sudo hostnamectl set-hostname webserver01.example.com
```

Sets the hostname persistently using systemd's hostnamectl. This updates /etc/hostname
and informs the running system without a reboot.

```bash
hostnamectl
```

Shows the static hostname, transient hostname, and machine ID.

The hostname should also be in /etc/hosts:

```bash
cat /etc/hosts
```

The line 127.0.1.1 webserver01.example.com webserver01 is a convention on Ubuntu that
associates the hostname with the loopback interface. Some applications use this for
self-identification.

---

### Section 6: Troubleshooting Methodology

A systematic approach to network problems:

Layer by layer from bottom to top:

1. Physical: Is the cable connected? Does the interface show state UP in ip link show?

2. IP addressing: Does ip addr show show the correct IP and subnet?

3. Default route: Does ip route show have a default route? Can you ping the gateway?

4. DNS: Does /etc/resolv.conf have a nameserver? Does dig work with the IP address
   directly (@nameserver IP)?

5. Application: Is the service running? Does ss -tulnp show it listening on the expected port?

[SHOW TERMINAL]

Quick checklist:

```bash
ip addr show                    # verify IP is assigned
ip route show                   # verify default gateway exists
ping -c 2 $(ip route | awk '/default/ {print $3}')  # ping gateway
ping -c 2 8.8.8.8               # test internet routing
dig google.com                  # test DNS resolution
ss -tulnp | grep :SERVICE_PORT  # verify service is listening
```

This sequence isolates which layer has the problem.

---

### Section 7: Exam Tips for Module 09

ip addr show replaces ifconfig. ip route show replaces route -n. ss replaces netstat.
Know all six.

nmcli con mod makes persistent changes. ip addr add makes temporary changes. This
distinction is highly tested.

/etc/nsswitch.conf hosts: line controls resolution order. files before dns means
/etc/hosts is checked before DNS.

/etc/hosts maps hostnames to IPs. /etc/resolv.conf specifies DNS servers. These are
two different things.

ss -tuln shows listening ports. ss -tulnp adds the process name and PID.

dig @IP hostname queries a specific DNS server directly, bypassing /etc/resolv.conf.

traceroute shows path hops. ping tests end-to-end connectivity. ss shows local ports.
tcpdump captures actual packets.

---

### Summary

Module 09 covers the complete Linux networking stack: interface inspection with ip,
persistent configuration with nmcli, DNS resolution with /etc/hosts and /etc/resolv.conf,
and diagnostics with ping, traceroute, ss, dig, and tcpdump.

Module 10 covers SSH and remote access security: key-based authentication, SSH configuration
hardening, and tunneling.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
