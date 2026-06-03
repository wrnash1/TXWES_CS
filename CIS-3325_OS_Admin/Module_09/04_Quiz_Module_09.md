# Quiz: Module 09 - Networking Configuration

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

**Question 1**

An administrator needs to display the IP address and subnet mask currently assigned to all
network interfaces on a Linux server. Which command is correct?

- A) ifconfig -a
- B) ip addr show
- C) nmcli dev status
- D) netstat -i

Correct Answer: B) ip addr show

Distractor Analysis:

- Why A is incorrect: ifconfig -a works on older systems but is deprecated and not installed by default on RHEL 8+ or Ubuntu 20.04+. The exam-current answer for interface information is the ip command.
- Why C is incorrect: nmcli dev status shows interface connection state (connected/disconnected) and the NetworkManager connection profile name, but does not display assigned IP addresses or subnet masks.
- Why D is incorrect: netstat -i shows interface statistics such as packet counts and errors, not assigned IP addresses or subnet masks.

---

**Question 2**

A Linux administrator wants to add a persistent static IP address to the ens33 interface using
NetworkManager so the configuration survives a reboot. Which command achieves this?

- A) ip addr add 10.0.0.5/24 dev ens33
- B) echo "IPADDR=10.0.0.5" >> /etc/network/interfaces
- C) nmcli con mod ens33 ipv4.addresses 10.0.0.5/24 ipv4.method manual
- D) ifconfig ens33 10.0.0.5 netmask 255.255.255.0

Correct Answer: C) nmcli con mod ens33 ipv4.addresses 10.0.0.5/24 ipv4.method manual

Distractor Analysis:

- Why A is incorrect: ip addr add makes a temporary, runtime-only change. The configuration is lost when the system reboots or when NetworkManager resets the interface.
- Why B is incorrect: /etc/network/interfaces is the Debian/Ubuntu legacy network configuration file, not used on systems managed by NetworkManager. It is not the correct method for NetworkManager-based persistence.
- Why D is incorrect: ifconfig is deprecated and its changes are not persistent. Like ip addr add, any address set with ifconfig is lost at reboot.

---

**Question 3**

A server administrator needs to verify which TCP ports are currently listening on a Linux system
without performing DNS lookups on the addresses. Which command is most appropriate?

- A) netstat -rn
- B) ss -tuln
- C) ip route show
- D) lsof -i tcp

Correct Answer: B) ss -tuln

Distractor Analysis:

- Why A is incorrect: netstat -rn displays the kernel routing table with numeric addresses — it shows routes, not listening ports.
- Why C is incorrect: ip route show displays the routing table entries. It does not list open sockets or listening ports.
- Why D is incorrect: lsof -i tcp lists open TCP connections and sockets but includes all connections (established, listening, closing) and performs name resolution by default. ss -tuln is the standard, faster, modern tool for listing listeners.

---

**Question 4**

An administrator edits /etc/hosts on a workstation to add the line 10.10.1.20  appserver.
After saving, a ping appserver command still fails to resolve the name. Which file controls
the order in which /etc/hosts and DNS are queried, and what should the administrator check?

- A) /etc/resolv.conf - verify the nameserver line points to the correct DNS server.
- B) /etc/nsswitch.conf - verify the hosts: line includes files before dns.
- C) /etc/hostname - verify the system's own hostname matches appserver.
- D) /etc/NetworkManager/NetworkManager.conf - verify dns=none is set so NetworkManager does not overwrite the hosts file.

Correct Answer: B) /etc/nsswitch.conf - verify the hosts: line includes files before dns.

Distractor Analysis:

- Why A is incorrect: /etc/resolv.conf configures which DNS servers to query. It does not control whether /etc/hosts is consulted at all or what priority it receives relative to DNS.
- Why C is incorrect: /etc/hostname sets the system's own hostname, not the resolution of arbitrary hostnames. Editing it would not affect how appserver resolves.
- Why D is incorrect: dns=none in NetworkManager.conf tells NetworkManager not to manage /etc/resolv.conf, but it has no bearing on whether the resolver reads /etc/hosts. The resolution order is governed by nsswitch.conf.

---

**Question 5**

An administrator uses dig appserver.example.com and gets no response. They then run
ping 10.10.1.20 and the ping succeeds. Which tool would best help diagnose whether the DNS
query is reaching the nameserver and what response is returned?

- A) traceroute 10.10.1.20
- B) ss -tuln
- C) dig @10.10.1.1 appserver.example.com
- D) ip route show

Correct Answer: C) dig @10.10.1.1 appserver.example.com

Distractor Analysis:

- Why A is incorrect: traceroute shows network path hops to an IP destination. It tests layer-3 reachability but provides no information about DNS resolution or nameserver responses.
- Why B is incorrect: ss -tuln shows listening ports on the local machine. It reveals nothing about remote DNS server behavior or DNS query results.
- Why D is incorrect: ip route show displays the local routing table. It confirms how packets are routed but does not diagnose DNS query failures or test nameserver responses.

---

**Question 6**

An administrator runs ip route show and sees no line beginning with default. What does this
indicate, and what is the immediate effect on outbound connectivity?

- A) The system has no configured IP addresses. Run ip addr show to verify.
- B) The system has no default gateway. Traffic to destinations not on a locally connected network cannot be routed, so external connectivity fails.
- C) The system is in a firewall-blocked state. Run iptables -L to check the rules.
- D) The routing table is empty. Run ip route add 0.0.0.0/0 to initialize it.

Correct Answer: B) The system has no default gateway. Traffic to destinations not on a locally connected network cannot be routed, so external connectivity fails.

Distractor Analysis:

- Why A is incorrect: The absence of a default route does not imply there are no IP addresses. An interface can have an IP address and be able to communicate on its local subnet without having a default gateway configured.
- Why C is incorrect: A missing default route is a routing configuration issue, not a firewall issue. Firewalls block or permit specific traffic; they do not create or remove routing table entries.
- Why D is incorrect: ip route add 0.0.0.0/0 alone is incomplete — it requires a via GATEWAY argument to specify where to send traffic. Simply adding a route to 0.0.0.0/0 without a gateway would fail.

---

**Question 7**

An administrator needs to add a persistent static route for the 10.50.0.0/16 network through
the gateway 192.168.1.100 using NetworkManager on a system with a connection named "eth0-static."
Which command sequence is correct?

- A) ip route add 10.50.0.0/16 via 192.168.1.100
- B) nmcli con mod "eth0-static" +ipv4.routes "10.50.0.0/16 192.168.1.100" && nmcli con up "eth0-static"
- C) echo "10.50.0.0/16 via 192.168.1.100" >> /etc/routes
- D) route add -net 10.50.0.0 netmask 255.255.0.0 gw 192.168.1.100

Correct Answer: B) nmcli con mod "eth0-static" +ipv4.routes "10.50.0.0/16 192.168.1.100" && nmcli con up "eth0-static"

Distractor Analysis:

- Why A is incorrect: ip route add makes a temporary change that is lost on reboot. The question requires a persistent route.
- Why C is incorrect: /etc/routes is not a standard Linux network configuration file. Routes added this way would not be recognized by any network management service.
- Why D is incorrect: The route command is deprecated (like ifconfig) and makes temporary changes only. Its changes are not persistent across reboots and are not managed by NetworkManager.

---

**Question 8**

A systems administrator captures network traffic on a production server using tcpdump. They
want to save the capture to a file for later analysis with Wireshark. Which command saves
100 packets from interface ens33 to a file named capture.pcap?

- A) tcpdump -i ens33 -n > capture.pcap
- B) tcpdump -i ens33 -c 100 -w capture.pcap
- C) tcpdump -i ens33 --save capture.pcap -count 100
- D) tcpdump -i ens33 | head -100 > capture.pcap

Correct Answer: B) tcpdump -i ens33 -c 100 -w capture.pcap

Distractor Analysis:

- Why A is incorrect: Redirecting tcpdump output to a file with > saves the human-readable text output, not the binary pcap format that Wireshark requires. The -w flag creates a proper binary pcap file.
- Why C is incorrect: --save and --count are not valid tcpdump flags. The correct flags are -w for output file and -c for packet count.
- Why D is incorrect: Piping tcpdump to head and redirecting to a file has the same problem as option A: it saves text output, not binary pcap format. Additionally, head counts text lines, not packets, so the count would not be accurate.

---

**Question 9**

An administrator sets a hostname using hostnamectl set-hostname server01.prod.example.com.
The hostname changes immediately in the shell prompt. The administrator then checks
/etc/hostname and it shows the new hostname. However, after rebooting and SSHing in, the
old hostname appears. What is the most likely explanation?

- A) hostnamectl changes are temporary. The hostname must also be written to /etc/sysconfig/network to persist.
- B) The /etc/hostname file was restored from a backup by a configuration management system (such as Ansible or Chef) that overwrote the change.
- C) The reboot cleared the hostname. Hostnames must be set in /etc/NetworkManager/NetworkManager.conf to persist.
- D) hostnamectl requires a reboot to take effect. The pre-reboot hostname displayed was still cached from the previous session.

Correct Answer: B) The /etc/hostname file was restored from a backup by a configuration management system (such as Ansible or Chef) that overwrote the change.

Distractor Analysis:

- Why A is incorrect: hostnamectl set-hostname writes the hostname persistently to /etc/hostname. Changes persist across reboots without requiring any other file to be edited. /etc/sysconfig/network is a legacy RHEL/CentOS file and is not involved on Ubuntu or modern systemd systems.
- Why C is incorrect: NetworkManager.conf does not manage the system hostname. The hostname is stored in /etc/hostname and managed by systemd-hostnamed. If /etc/hostname shows the correct hostname, hostnamectl has done its job correctly.
- Why D is incorrect: hostnamectl takes effect immediately without a reboot. The new hostname shows in the running system as soon as the command completes. If the hostname changed back after reboot, the file was overwritten by an external process.

---

**Question 10**

An administrator runs ping -c 4 8.8.8.8 and gets 0% packet loss with good response times.
They then run ping -c 4 google.com and get "Name or service not known." What is the most
likely cause and the correct diagnostic command?

- A) The network cable is disconnected. Run ip link show to check the interface state.
- B) DNS resolution is failing. Run dig google.com or dig @8.8.8.8 google.com to query the configured DNS server and a known-good server for comparison.
- C) The firewall is blocking ICMP to hostnames. Run iptables -L INPUT to inspect the rules.
- D) google.com has blocked ICMP from this IP. Use curl google.com instead.

Correct Answer: B) DNS resolution is failing. Run dig google.com or dig @8.8.8.8 google.com to query the configured DNS server and a known-good server for comparison.

Distractor Analysis:

- Why A is incorrect: If the network cable were disconnected, ping 8.8.8.8 (by IP address) would also fail. Since that succeeded, IP connectivity is working and the problem is above Layer 3.
- Why C is incorrect: Firewalls filter based on IP addresses and ports, not on whether a command uses a hostname or an IP address. If 8.8.8.8 is reachable by IP, ICMP to an IP resolved from google.com would also be allowed. The issue is that the hostname never gets resolved, not that the ping itself is blocked.
- Why D is incorrect: curl google.com would also require DNS resolution to work. If DNS is failing for ping, it will also fail for curl. The symptom (Name or service not known) is specifically a DNS resolution failure.
