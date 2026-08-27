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

---

**Question 11**

An administrator runs `ip addr show ens33` and sees the interface has no IP address assigned.
They run `ip addr add 192.168.10.50/24 dev ens33` and the address appears. After a reboot,
the address is gone. What must they do to make the address persist?

- A) Add the address to /etc/hosts with the interface name.
- B) Configure the address in NetworkManager using nmcli con mod and nmcli con up, then verify the connection file in /etc/NetworkManager/system-connections/.
- C) Add the ip addr add command to /etc/rc.local so it runs at every boot.
- D) Run ip addr add with the --permanent flag to write it to the kernel routing table permanently.

Correct Answer: B) Configure the address in NetworkManager using nmcli con mod and nmcli con up, then verify the connection file in /etc/NetworkManager/system-connections/.

Distractor Analysis:

- Why A is incorrect: /etc/hosts maps hostnames to IP addresses for name resolution. It does not assign IP addresses to network interfaces and has no effect on interface configuration.
- Why C is incorrect: While /etc/rc.local would technically run the ip addr add command at boot, this approach bypasses NetworkManager, creates configuration drift, and would be overwritten whenever NetworkManager brings the connection up with its own settings. Using nmcli is the correct persistent configuration method on modern Ubuntu systems.
- Why D is incorrect: There is no --permanent flag for the ip addr add command. The ip command from the iproute2 suite always makes temporary changes to kernel state. Persistence requires writing configuration to NetworkManager or a netplan YAML file.

---

**Question 12**

A server running Ubuntu 22.04 has two network interfaces: `ens33` connected to a 192.168.1.0/24
network and `ens36` connected to a 10.0.0.0/8 network. The routing table shows a default route
via ens33. An application on the server needs to reach 10.5.5.5 but cannot. Which command adds
the correct specific route?

- A) ip route add 10.0.0.0/8 via 192.168.1.1 dev ens33
- B) ip route add 10.0.0.0/8 dev ens36
- C) ip route add default via 10.0.0.1 dev ens36
- D) nmcli con mod ens36 ipv4.routes "10.5.5.5/32 0.0.0.0"

Correct Answer: B) ip route add 10.0.0.0/8 dev ens36

Distractor Analysis:

- Why A is incorrect: Routing the 10.0.0.0/8 network via the ens33 gateway (192.168.1.1) would send traffic out the wrong interface. The ens33 gateway handles the 192.168.1.0/24 network, not the 10.0.0.0/8 network. Traffic to 10.5.5.5 must leave via ens36.
- Why C is incorrect: Replacing the default route with a gateway via ens36 would break connectivity to the internet and all other destinations currently reached via ens33. Adding a specific host or network route is the correct approach, not replacing the default route.
- Why D is incorrect: While nmcli can add persistent routes, the syntax shown is incorrect. The correct nmcli route syntax is "NETWORK/PREFIX GATEWAY" (e.g., "10.0.0.0/8 0.0.0.0" to use the interface directly). Additionally, a /32 host route for only 10.5.5.5 would work for that one host but would not fix general reachability to the 10.0.0.0/8 network.

---

**Question 13**

An administrator runs `ss -tulnp` and sees this line:

```
tcp  LISTEN  0  128  0.0.0.0:22  0.0.0.0:*  users:(("sshd",pid=1234,fd=3))
```

What does `0.0.0.0:22` mean in the Local Address:Port column?

- A) SSH is only accessible from the loopback address 127.0.0.1 on port 22.
- B) SSH is listening on all IPv4 interfaces on port 22 and will accept connections from any source.
- C) SSH is listening on the broadcast address and will send connection offers to all clients on the subnet.
- D) SSH is disabled. The 0.0.0.0 address means the service has no bound address.

Correct Answer: B) SSH is listening on all IPv4 interfaces on port 22 and will accept connections from any source.

Distractor Analysis:

- Why A is incorrect: 127.0.0.1 is the loopback address. A service bound to the loopback address would show 127.0.0.1:22 in the output, not 0.0.0.0:22. Binding to 0.0.0.0 means all interfaces, which includes the loopback but also all physical and virtual interfaces.
- Why C is incorrect: 0.0.0.0 is the "unspecified" or "any" address for binding purposes. It is not the broadcast address (255.255.255.255 or the subnet broadcast). Services bind to 0.0.0.0 to accept incoming connections on all interfaces, not to broadcast.
- Why D is incorrect: LISTEN state with a valid port number means the service is actively accepting connections. A value of 0.0.0.0 in the local address indicates binding to all interfaces, which is the most permissive and common configuration for a server daemon.

---

**Question 14**

The file `/etc/nsswitch.conf` contains the line:

```
hosts: files dns
```

An administrator adds `192.168.5.100 appserver` to `/etc/hosts` but the DNS record for
`appserver` points to `192.168.5.200`. When the application resolves `appserver`, which
address does it get and why?

- A) 192.168.5.200, because DNS records always take precedence over /etc/hosts on modern systems.
- B) 192.168.5.100, because the nsswitch.conf hosts line lists files before dns, so /etc/hosts is consulted first.
- C) Both addresses are returned and the application chooses based on its own logic.
- D) Neither address is returned because having conflicting entries causes a resolution failure.

Correct Answer: B) 192.168.5.100, because the nsswitch.conf hosts line lists files before dns, so /etc/hosts is consulted first.

Distractor Analysis:

- Why A is incorrect: DNS does not always take precedence. The resolution order is explicitly controlled by /etc/nsswitch.conf. The default Ubuntu configuration lists files (meaning /etc/hosts) before dns, so a matching /etc/hosts entry always takes precedence over DNS.
- Why C is incorrect: The resolver follows the nsswitch.conf order and returns the first successful result. It does not query both sources and return combined results. Once /etc/hosts returns a match, DNS is not consulted.
- Why D is incorrect: Having different values in /etc/hosts and DNS is not an error condition. The system resolves normally according to the nsswitch.conf order and returns the first match found. No failure or error occurs.

---

**Question 15**

An administrator runs `traceroute 8.8.8.8` and sees that hops 3 through 6 all display `* * *`.
Hop 7 resumes showing IP addresses, and the final destination responds. What is the correct
interpretation?

- A) The network path is broken between hops 3 and 6 and packets are being dropped silently.
- B) The routers at hops 3 through 6 are configured to not respond to ICMP TTL-exceeded messages but are still forwarding packets, as evidenced by the path reaching its destination.
- C) The traceroute command timed out and must be rerun with a longer timeout using the -w flag.
- D) Hops 3 through 6 are on a VPN segment that blocks all visibility but the destination is outside the VPN.

Correct Answer: B) The routers at hops 3 through 6 are configured to not respond to ICMP TTL-exceeded messages but are still forwarding packets, as evidenced by the path reaching its destination.

Distractor Analysis:

- Why A is incorrect: If packets were actually dropped between hops 3 and 6, the traceroute would never reach hop 7 or the destination. The fact that hops resume after hop 6 and the destination responds confirms that packet forwarding is working correctly.
- Why C is incorrect: A timeout for a specific hop produces `* * *` for that hop in a single traceroute run. This is expected behavior when a router filters ICMP TTL-exceeded responses, not a sign that the entire traceroute command needs to be rerun.
- Why D is incorrect: While a VPN could cause some hops to be invisible, the explanation that all invisible hops are still forwarding is correct regardless of the cause. The key diagnostic fact is that the destination responds, proving the path works end-to-end.

---

**Question 16**

A junior administrator wants to find which process is listening on TCP port 8080. Which
command provides both the port and the process name with its PID?

- A) netstat -an | grep 8080
- B) lsof -i :8080
- C) ss -tulnp | grep 8080
- D) Both B and C provide the process name and PID.

Correct Answer: D) Both B and C provide the process name and PID.

Distractor Analysis:

- Why A is incorrect: netstat -an shows the listening port but does not include process names or PIDs without the -p flag. The correct netstat command for process information would be netstat -tulnp. Additionally, ss has replaced netstat as the preferred tool on modern Linux systems.
- Why B alone is incorrect: lsof -i :8080 does show the process name and PID for processes using port 8080. However, option D is more complete because ss -tulnp also provides this information and is the preferred modern command.
- Why C alone is incorrect: ss -tulnp | grep 8080 does show the process name and PID in the users:() field. However, option D is more complete because lsof -i :8080 also provides this information in a different format.

---

**Question 17**

An administrator edits `/etc/resolv.conf` directly to change the DNS server from 8.8.8.8 to
a local DNS server at 192.168.1.10. After a reboot, the file reverts to the original content.
What is the most likely cause?

- A) /etc/resolv.conf is a read-only file protected by immutable flag. Use chattr -i to remove the flag.
- B) NetworkManager automatically regenerates /etc/resolv.conf from its connection configuration on each boot or reconnect, overwriting manual edits.
- C) systemd-networkd restores /etc/resolv.conf from a backup stored in /run/systemd/resolve/.
- D) Direct edits to /etc/resolv.conf require running resolvectl apply to commit them permanently.

Correct Answer: B) NetworkManager automatically regenerates /etc/resolv.conf from its connection configuration on each boot or reconnect, overwriting manual edits.

Distractor Analysis:

- Why A is incorrect: While chattr +i can make a file immutable, /etc/resolv.conf is not set immutable by default. This is not a standard Ubuntu configuration. The actual cause is NetworkManager overwriting the file, not a filesystem attribute.
- Why C is incorrect: /run/systemd/resolve/ is used by systemd-resolved for its runtime state. On systems using systemd-resolved, /etc/resolv.conf is often a symlink to /run/systemd/resolve/stub-resolv.conf. But the overwrite cause is still the resolver management system (NetworkManager or systemd-resolved), not a direct backup restoration.
- Why D is incorrect: There is no resolvectl apply command. resolvectl is a tool for querying and configuring systemd-resolved. The correct approach to making persistent DNS changes on a NetworkManager system is to use nmcli con mod to set ipv4.dns on the connection profile.

---

**Question 18**

A network interface `ens33` has the IP address `10.10.1.5/24`. An administrator runs:

```
ip route show
```

And sees no default route. They run `ping 10.10.1.1` successfully but `ping 8.8.8.8` fails
with "Network is unreachable." What is the correct command to add a temporary default route?

- A) ip route add default dev ens33
- B) ip route add 0.0.0.0/0 via 10.10.1.1
- C) ip link set ens33 default gw 10.10.1.1
- D) nmcli con mod ens33 ipv4.gateway 10.10.1.1

Correct Answer: B) ip route add 0.0.0.0/0 via 10.10.1.1

Distractor Analysis:

- Why A is incorrect: ip route add default dev ens33 without a via gateway creates a route that sends all traffic directly out ens33 without a next-hop gateway. This would work only for directly connected hosts and would not provide internet connectivity.
- Why C is incorrect: ip link is used to manage network interface properties (up/down state, MTU, MAC address). It does not have a default gw subcommand and cannot configure routes.
- Why D is incorrect: nmcli con mod changes the persistent NetworkManager connection profile. This would persist the gateway across reboots, which is correct for permanent configuration, but the question asks for a temporary route added with the ip command, not a persistent change.

---

**Question 19**

An administrator uses `dig` to query a domain and sees the following in the output:

```
;; ANSWER SECTION:
example.com.  300  IN  A  93.184.216.34
```

What does the number `300` represent?

- A) The TCP port used for the DNS query.
- B) The TTL (Time to Live) in seconds — how long resolvers and clients may cache this record before re-querying.
- C) The serial number of the DNS zone file.
- D) The record weight used for load balancing among multiple A records.

Correct Answer: B) The TTL (Time to Live) in seconds — how long resolvers and clients may cache this record before re-querying.

Distractor Analysis:

- Why A is incorrect: DNS queries use port 53 (UDP or TCP), not port 300. Port numbers are not shown in the answer section of dig output; they appear in the connection header.
- Why C is incorrect: The zone serial number appears in SOA (Start of Authority) records, not in A records. The SOA serial is used to track zone file versions for DNS zone transfers between primary and secondary name servers.
- Why D is incorrect: DNS record weight (used for load balancing) is a property of SRV records, not A records. A record weight-based selection is performed by DNS clients at the application level in some implementations, but the number in the second column of a dig answer section is always the TTL.

---

**Question 20**

An administrator runs `nmcli device status` and sees that interface `ens36` shows state
`unmanaged`. They want NetworkManager to manage this interface. Which command corrects this?

- A) ip link set ens36 up
- B) nmcli device set ens36 managed yes
- C) systemctl restart NetworkManager
- D) Add ens36 to /etc/network/interfaces and run ifup ens36.

Correct Answer: B) nmcli device set ens36 managed yes

Distractor Analysis:

- Why A is incorrect: ip link set ens36 up brings the interface to UP state at the kernel level but does not change NetworkManager's management status. The interface would still show as unmanaged in nmcli device status after this command.
- Why C is incorrect: Restarting NetworkManager reloads its configuration but does not change the managed status of a specific interface. If the interface is explicitly excluded from management (e.g., via a keyfile or udev rule), restarting NetworkManager will not change that.
- Why D is incorrect: /etc/network/interfaces is the legacy ifupdown configuration file. On modern Ubuntu systems using NetworkManager, managing an interface via /etc/network/interfaces can actually cause conflicts that make NetworkManager treat the interface as unmanaged. The correct tool is nmcli.
