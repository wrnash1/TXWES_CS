# Quiz: Module 09 - Networking Configuration
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
An administrator needs to display the IP address and subnet mask currently assigned to all network interfaces on a Linux server. Which command is correct?
A) ifconfig -a
B) ip addr show
C) nmcli dev status
D) netstat -i
*   **Correct Answer:** B) ip addr show
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `ifconfig -a` works on older systems but is deprecated and not installed by default on RHEL 8+ or Ubuntu 20.04+. The exam-current answer for interface information is the `ip` command.
    *   *Why C is incorrect:* `nmcli dev status` shows interface connection state (connected/disconnected) and the NetworkManager connection profile name, but does not display assigned IP addresses or subnet masks.
    *   *Why D is incorrect:* `netstat -i` shows interface statistics such as packet counts and errors, not assigned IP addresses or subnet masks.

---

---

**Question 2**
A Linux administrator wants to add a persistent static IP address to the `ens33` interface using NetworkManager so the configuration survives a reboot. Which command achieves this?
A) ip addr add 10.0.0.5/24 dev ens33
B) echo "IPADDR=10.0.0.5" >> /etc/network/interfaces
C) nmcli con mod ens33 ipv4.addresses 10.0.0.5/24 ipv4.method manual
D) ifconfig ens33 10.0.0.5 netmask 255.255.255.0
*   **Correct Answer:** C) nmcli con mod ens33 ipv4.addresses 10.0.0.5/24 ipv4.method manual
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `ip addr add` makes a temporary, runtime-only change. The configuration is lost when the system reboots or when NetworkManager resets the interface.
    *   *Why B is incorrect:* `/etc/network/interfaces` is the Debian/Ubuntu legacy network configuration file, not used on RHEL/CentOS systems or systems managed by NetworkManager. It is not the correct method for NetworkManager-based persistence.
    *   *Why D is incorrect:* `ifconfig` is deprecated and its changes are not persistent. Like `ip addr add`, any address set with `ifconfig` is lost at reboot.

---

---

**Question 3**
A server administrator needs to verify which TCP ports are currently listening on a Linux system without performing DNS lookups on the addresses. Which command is most appropriate?
A) netstat -rn
B) ss -tuln
C) ip route show
D) lsof -i tcp
*   **Correct Answer:** B) ss -tuln
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `netstat -rn` displays the kernel routing table with numeric addresses — it shows routes, not listening ports.
    *   *Why C is incorrect:* `ip route show` displays the routing table entries. It does not list open sockets or listening ports.
    *   *Why D is incorrect:* `lsof -i tcp` lists open TCP connections and sockets but includes all connections (established, listening, closing) and performs name resolution by default. `ss -tuln` is the standard, faster, modern tool for listing listeners.

---

**Question 4**
An administrator edits `/etc/hosts` on a workstation to add the line `10.10.1.20  appserver`. After saving, a `ping appserver` command still fails to resolve the name. Which file controls the order in which `/etc/hosts` and DNS are queried, and what should the administrator check?
A) `/etc/resolv.conf` — verify the `nameserver` line points to the correct DNS server.
B) `/etc/nsswitch.conf` — verify the `hosts:` line includes `files` before `dns`.
C) `/etc/hostname` — verify the system's own hostname matches `appserver`.
D) `/etc/NetworkManager/NetworkManager.conf` — verify `dns=none` is set so NetworkManager does not overwrite the hosts file.
*   **Correct Answer:** B) `/etc/nsswitch.conf` — verify the `hosts:` line includes `files` before `dns`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `/etc/resolv.conf` configures which DNS servers to query. It does not control whether `/etc/hosts` is consulted at all or what priority it receives relative to DNS.
    *   *Why C is incorrect:* `/etc/hostname` sets the system's own hostname, not the resolution of arbitrary hostnames. Editing it would not affect how `appserver` resolves.
    *   *Why D is incorrect:* `dns=none` in NetworkManager.conf tells NetworkManager not to manage `/etc/resolv.conf`, but it has no bearing on whether the resolver reads `/etc/hosts`. The resolution order is governed by `nsswitch.conf`.

---

**Question 5**
An administrator uses `dig appserver.example.com` and gets no response. They then run `ping 10.10.1.20` and the ping succeeds. Which tool would best help diagnose whether the DNS query is reaching the nameserver and what response is returned?
A) traceroute 10.10.1.20
B) ss -tuln
C) dig @10.10.1.1 appserver.example.com
D) ip route show
*   **Correct Answer:** C) dig @10.10.1.1 appserver.example.com
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `traceroute` shows network path hops to an IP destination. It tests layer-3 reachability but provides no information about DNS resolution or nameserver responses.
    *   *Why B is incorrect:* `ss -tuln` shows listening ports on the local machine. It reveals nothing about remote DNS server behavior or DNS query results.
    *   *Why D is incorrect:* `ip route show` displays the local routing table. It confirms how packets are routed but does not diagnose DNS query failures or test nameserver responses.
