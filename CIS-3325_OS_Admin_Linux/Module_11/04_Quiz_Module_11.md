# Quiz: Module 11 — Networking in Linux

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Instructions

Select the best answer for each question. Each question is worth 10 points.

---

### Questions

**Question 1**

A Linux administrator needs to assign the IP address `10.0.5.25/28` to the interface `ens3` temporarily (until the next reboot). Which command accomplishes this?

- A) `ifconfig ens3 10.0.5.25 netmask 255.255.255.240`
- B) `ip addr add 10.0.5.25/28 dev ens3`
- C) `nmcli connection modify ens3 ipv4.addresses 10.0.5.25/28`
- D) `ip link set ens3 addr 10.0.5.25/28`

**Correct Answer: B**

*Explanation: `ip addr add` assigns an address to an interface immediately but non-persistently. `nmcli connection modify` creates a persistent profile. Option A (ifconfig) is deprecated. Option D uses `link`, which manages interface state, not addresses.*

---

**Question 2**

After running `sudo firewall-cmd --zone=public --add-service=https --permanent`, the HTTPS service is not yet accessible. What is the most likely reason?

- A) The `--permanent` flag is not valid without specifying a port number
- B) The firewall must be reloaded with `firewall-cmd --reload` for permanent rules to take effect
- C) HTTPS requires a rich rule, not a service name
- D) The public zone does not support HTTPS by default

**Correct Answer: B**

*Explanation: Permanent rules are written to disk but not applied to the running firewall until a reload is performed. Always follow permanent rule changes with `firewall-cmd --reload`.*

---

**Question 3**

Which file controls the order in which hostname resolution methods are attempted on a Linux system?

- A) `/etc/hosts`
- B) `/etc/resolv.conf`
- C) `/etc/nsswitch.conf`
- D) `/etc/hostname`

**Correct Answer: C**

*Explanation: `/etc/nsswitch.conf` contains the `hosts:` directive that specifies the lookup order (e.g., `files dns myhostname`). `/etc/hosts` is one of the sources, and `/etc/resolv.conf` configures DNS servers.*

---

**Question 4**

A technician runs `ping 8.8.8.8` successfully but `ping google.com` fails with "Name or service not known." What is the most likely cause?

- A) The default gateway is unreachable
- B) Google's servers are blocking ICMP
- C) DNS resolution is failing
- D) The network interface is down

**Correct Answer: C**

*Explanation: Successful ping to a numeric IP confirms Layer 3 routing works. Failure on hostname resolution indicates DNS is the problem — the resolver in `/etc/resolv.conf` may be misconfigured or unreachable.*

---

**Question 5**

Which `nmcli` command displays only the currently active network connections?

- A) `nmcli connection show`
- B) `nmcli connection show --active`
- C) `nmcli device status --active`
- D) `nmcli general active`

**Correct Answer: B**

*Explanation: `nmcli connection show --active` filters the connection list to show only connections that are currently activated. Without `--active`, all configured profiles are listed.*

---

**Question 6**

An administrator wants to display all listening TCP sockets along with the owning process name and PID. Which command is correct?

- A) `netstat -tlnp`
- B) `ss -tlnp`
- C) `ss -tap`
- D) `lsof -i tcp`

**Correct Answer: B**

*Explanation: `ss -tlnp` shows TCP (`-t`), listening (`-l`), numeric (`-n`), with process info (`-p`). While `netstat` and `lsof` can accomplish similar tasks, `ss` is the modern replacement and is tested on Linux+.*

---

**Question 7**

Which iptables command correctly displays all rules in the INPUT chain with packet counts and numeric addresses?

- A) `iptables -L INPUT`
- B) `iptables -L INPUT -n`
- C) `iptables -L INPUT -n -v`
- D) `iptables --list INPUT --verbose`

**Correct Answer: C**

*Explanation: `-L INPUT` lists the INPUT chain, `-n` suppresses DNS resolution for numeric output, and `-v` adds verbose mode which shows packet and byte counters. Option D uses incorrect syntax.*

---

**Question 8**

A system administrator needs to capture only TCP traffic on port 443 from interface `eth0` and save it to a file. Which `tcpdump` command is correct?

- A) `tcpdump -i eth0 tcp port 443`
- B) `tcpdump -i eth0 tcp port 443 -w /tmp/cap.pcap`
- C) `tcpdump --interface eth0 --port 443 --output /tmp/cap.pcap`
- D) `tcpdump eth0 443 > /tmp/cap.pcap`

**Correct Answer: B**

*Explanation: `-i eth0` specifies the interface, `tcp port 443` is the BPF filter, and `-w /tmp/cap.pcap` writes raw packet data to a file in pcap format for later analysis in Wireshark.*

---

**Question 9**

Which directive in `~/.ssh/config` prevents SSH from trying any key other than the one explicitly specified for a host?

- A) `PasswordAuthentication no`
- B) `IdentitiesOnly yes`
- C) `PubkeyAuthentication yes`
- D) `PreferredAuthentications publickey`

**Correct Answer: B**

*Explanation: `IdentitiesOnly yes` instructs the SSH client to offer only the key specified in `IdentityFile`, ignoring any keys loaded in ssh-agent or keys at default paths. This is important for security in multi-key environments.*

---

**Question 10**

A Linux administrator is configuring a server and runs `hostnamectl set-hostname app01.prod.example.com`. Where is this hostname persistently stored?

- A) `/etc/network/hostname`
- B) `/etc/sysconfig/network`
- C) `/etc/hostname`
- D) `/proc/sys/kernel/hostname`

**Correct Answer: C**

*Explanation: `hostnamectl` writes the static hostname to `/etc/hostname`. `/proc/sys/kernel/hostname` reflects the runtime hostname but does not persist. `/etc/sysconfig/network` is used on older RHEL-based systems for additional network settings.*

---

**Question 11** (5 points)

An administrator wants to add a static route to reach the `192.168.100.0/24` network via gateway `10.0.0.1` on interface `ens3`, persistently using NetworkManager. Which command is correct?

- A) `ip route add 192.168.100.0/24 via 10.0.0.1 dev ens3`
- B) `nmcli connection modify ens3 +ipv4.routes "192.168.100.0/24 10.0.0.1"`
- C) `route add -net 192.168.100.0/24 gw 10.0.0.1 dev ens3`
- D) `ip route add 192.168.100.0/24 gw 10.0.0.1`

**Correct Answer: B**

*Explanation: `nmcli connection modify` with `+ipv4.routes` adds a persistent static route to the NetworkManager connection profile. After running this command, the connection must be reactivated with `nmcli connection up ens3`. Option A adds a route immediately but non-persistently. Option C uses the deprecated `route` command. Option D uses invalid `gw` syntax for `ip route`.*

---

**Question 12** (5 points)

Which command shows the current state of all network interfaces including their IP addresses, MAC addresses, and operational state using the modern iproute2 toolset?

- A) `ifconfig -a`
- B) `ip addr show`
- C) `ip link show`
- D) `nmcli device status`

**Correct Answer: B**

*Explanation: `ip addr show` (or `ip a`) displays all interfaces with their IP addresses, MAC addresses, and operational state. `ip link show` shows interface state and MAC addresses but NOT IP addresses. `nmcli device status` shows connection states but not IP address details. `ifconfig` is deprecated.*

---

**Question 13** (5 points)

A firewall administrator needs to allow SSH access only from the subnet `10.10.5.0/24` using firewalld rich rules. Which command is correct?

- A) `firewall-cmd --zone=public --add-service=ssh --source=10.10.5.0/24`
- B) `firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="10.10.5.0/24" service name="ssh" accept'`
- C) `firewall-cmd --zone=public --add-rich-rule='accept service ssh from 10.10.5.0/24'`
- D) `firewall-cmd --zone=public --add-source=10.10.5.0/24 --add-service=ssh`

**Correct Answer: B**

*Explanation: Source-restricted service rules require firewalld's rich rule syntax. The correct format specifies `family`, `source address`, `service name`, and the action. Option A's `--source` flag controls zone assignment, not per-rule source filtering. Option C uses invalid syntax. Option D combines source zone assignment with service allowance, which has different semantics (all traffic from that source gets the zone's policy).*

---

**Question 14** (5 points)

What does `dig +short google.com` return that `nslookup google.com` does not provide by default?

- A) The authoritative DNS server name
- B) Only the resolved IP addresses with no other output
- C) The full DNS query and response headers
- D) The TTL value for each record

**Correct Answer: B**

*Explanation: `dig +short` produces minimal output — just the answer records, one per line, with no headers, statistics, or metadata. This makes it useful in scripts. `nslookup` outputs server information, the queried name, and the address in a formatted display. `dig` without `+short` shows full query details including authority and additional sections.*

---

**Question 15** (5 points)

A sysadmin runs `ss -s` on a server experiencing network issues. What type of information does this command display?

- A) A list of all established connections with process names
- B) Summary statistics showing counts of connections in each state (ESTAB, TIME-WAIT, CLOSE-WAIT, etc.)
- C) The contents of the socket buffer for each active connection
- D) The routing table organized by socket

**Correct Answer: B**

*Explanation: `ss -s` (summary) displays aggregate statistics — total sockets, TCP connections by state (ESTAB, SYN-SENT, SYN-RECV, FIN-WAIT, TIME-WAIT, CLOSE-WAIT, etc.), and UDP/raw socket counts. This provides a quick health overview without listing individual connections. To list connections with processes, use `ss -tp` or `ss -tlnp`.*

---

**Question 16** (5 points)

An administrator sets `PermitRootLogin prohibit-password` in `/etc/ssh/sshd_config`. What does this setting allow?

- A) Root login is completely disabled.
- B) Root can log in with an SSH key but not with a password.
- C) Root can log in with a password but not an SSH key.
- D) Root login is allowed from localhost only.

**Correct Answer: B**

*Explanation: `prohibit-password` (also written as `without-password` in older versions) disables password and keyboard-interactive authentication for root while still allowing public key authentication. This is a common hardening practice that allows automated root access via keys while preventing brute-force password attacks against the root account.*

---

**Question 17** (5 points)

What is the purpose of the `~/.ssh/known_hosts` file?

- A) It stores the user's private SSH keys for automatic loading.
- B) It stores the public host keys of servers the user has connected to, enabling detection of changed or spoofed servers.
- C) It lists the IP addresses of hosts the user is authorized to connect to.
- D) It stores SSH session logs for auditing purposes.

**Correct Answer: B**

*Explanation: `known_hosts` stores the public key fingerprints of SSH servers the user has connected to. On the next connection, the client verifies that the server's host key matches the stored fingerprint — a mismatch triggers a "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED" error, alerting to a possible man-in-the-middle attack or server rebuild. It does not contain user keys (those are in `id_rsa`, `id_ed25519`, etc.).*

---

**Question 18** (5 points)

Which `/etc/hosts` entry format is correct for assigning two aliases to an IP address?

- A) `192.168.1.10 webserver alias1 alias2`
- B) `192.168.1.10 webserver; alias1; alias2`
- C) `192.168.1.10 webserver, alias1, alias2`
- D) `192.168.1.10 webserver` on one line and `192.168.1.10 alias1 alias2` on another

**Correct Answer: A**

*Explanation: `/etc/hosts` format is: `IP_ADDRESS canonical_name [alias1] [alias2] ...` — all on one line, separated by whitespace. Multiple aliases are space-separated. Semicolons and commas are not valid delimiters. While option D would also work (multiple entries for the same IP are allowed), option A is the canonical single-line format.*

---

**Question 19** (5 points)

A server has `NetworkManager` managing connections. An administrator directly edits `/etc/sysconfig/network-scripts/ifcfg-ens3` to add a DNS server. After saving, the change does not take effect. What is the most likely reason?

- A) DNS must be configured in `/etc/resolv.conf` directly.
- B) NetworkManager must be restarted or the connection reactivated to read the updated file.
- C) The `ifcfg` file format does not support DNS configuration.
- D) `/etc/sysconfig/` files are read-only when NetworkManager is active.

**Correct Answer: B**

*Explanation: NetworkManager reads connection profile files at startup or when a connection is activated, not continuously. Direct edits to profile files require either `nmcli connection reload` followed by `nmcli connection up ens3`, or a restart of NetworkManager itself. Simply editing the file does not cause NetworkManager to apply the changes immediately.*

---

**Question 20** (5 points)

An administrator uses `tcpdump -i ens3 -nn -c 50 'host 10.0.1.15 and tcp port 80'` to capture packets. What does the `-nn` flag do?

- A) Captures 50 packets twice for redundancy.
- B) Prevents tcpdump from resolving IP addresses to hostnames and port numbers to service names.
- C) Enables verbose output with two levels of detail.
- D) Suppresses all output and writes only to the capture file.

**Correct Answer: B**

*Explanation: In tcpdump, `-n` suppresses DNS hostname resolution and `-nn` additionally suppresses port-to-service-name resolution (so port 80 appears as `80` rather than `http`). Using `-nn` is a best practice in troubleshooting because name resolution can add significant delay to packet capture and can itself alter the network traffic being observed.*

---

### Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | B |
| 3 | C |
| 4 | C |
| 5 | B |
| 6 | B |
| 7 | C |
| 8 | B |
| 9 | B |
| 10 | C |
| 11 | B |
| 12 | B |
| 13 | B |
| 14 | B |
| 15 | B |
| 16 | B |
| 17 | B |
| 18 | A |
| 19 | B |
| 20 | B |
