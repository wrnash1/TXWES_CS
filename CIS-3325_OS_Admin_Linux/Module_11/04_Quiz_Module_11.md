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
