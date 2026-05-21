# Reading Guide: Module 09 - Networking Configuration
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 09 – Networking Configuration**! This week covers Linux network stack fundamentals — from IP address assignment and interface management with `ip` and `nmcli`, through hostname resolution with `/etc/hosts` and `/etc/resolv.conf`, to testing connectivity with `ping`, `traceroute`, and `ss`. Networking is heavily tested on CompTIA Linux+ XK0-005 under Domain 1.0 (System Management) and Domain 2.0 (Security).

As you work through this material you will learn how to view and configure network interfaces, set static and DHCP addresses, troubleshoot connectivity, and configure DNS name resolution — skills essential for both the exam and daily Linux administration.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **`ip` command**: The modern replacement for the deprecated `ifconfig`. Used to display and configure network interfaces, routes, and addresses. Key subcommands: `ip addr show` (list interfaces and IPs), `ip link set eth0 up/down` (bring interface up or down), `ip route show` (display routing table), `ip addr add 192.168.1.10/24 dev eth0` (assign an IP address temporarily). Changes made with `ip` are not persistent across reboots.
*   **`nmcli` (NetworkManager CLI)**: A command-line interface to NetworkManager, the service that manages network connections persistently on most modern Linux distributions. `nmcli con show` lists connections; `nmcli con up <name>` activates a connection; `nmcli dev status` shows interface states; `nmcli con mod <name> ipv4.addresses 192.168.1.10/24` modifies a connection persistently. Configuration is stored in `/etc/NetworkManager/system-connections/`.
*   **`/etc/hosts`**: A static hostname-to-IP mapping file processed before DNS. Each line contains an IP address followed by one or more hostnames: `192.168.1.5  webserver webserver.local`. Useful for local name resolution without a DNS server. On Linux, the resolution order is controlled by `/etc/nsswitch.conf` — typically `files dns`, meaning `/etc/hosts` is checked first.
*   **`/etc/resolv.conf`**: Configures DNS resolver behavior. The `nameserver` directive specifies the DNS server IP (e.g., `nameserver 8.8.8.8`). The `search` directive appends domain suffixes for short hostnames. On systems using NetworkManager or systemd-resolved, this file may be a symlink managed automatically — manual edits may be overwritten.
*   **`ss` and `netstat`**: Tools for displaying socket and connection information. `ss -tuln` shows all TCP and UDP listening ports without resolving names — the modern replacement for `netstat -tuln`. `ss -tp` shows TCP connections with the associated process. `netstat` is deprecated on modern systems but still appears on the CompTIA Linux+ exam.
*   **`ping`, `traceroute`, `dig`**: Connectivity testing and DNS diagnostic tools. `ping -c 4 hostname` sends 4 ICMP echo requests to test reachability. `traceroute hostname` (or `tracepath`) shows each network hop to a destination. `dig hostname` performs a detailed DNS lookup showing the full query/response; `dig @8.8.8.8 hostname` queries a specific nameserver directly.

---

### 2. Certification Exam Tips
*   **Domain alignment:** Networking maps to Linux+ Domain 1.0 (System Management) and Domain 2.0 (Security). Expect 5–7 questions on interface configuration, name resolution, and connectivity testing.
*   **`ip` vs `ifconfig` trap:** The exam presents both commands — know that `ifconfig` is deprecated and not installed by default on RHEL 8+/Ubuntu 20.04+. The exam-preferred answer for interface management is `ip addr show` or `ip link`. If both appear as options, choose `ip`.
*   **Persistent vs temporary configuration:** `ip addr add` changes are lost at reboot. For persistence use `nmcli con mod` or edit `/etc/sysconfig/network-scripts/ifcfg-<name>` (RHEL) or Netplan YAML (Ubuntu 18.04+). The exam tests whether you know the difference between a live change and a persistent one.
*   **`/etc/hosts` vs DNS resolution order:** Know that `/etc/nsswitch.conf` controls resolution order. The default `hosts: files dns` means `/etc/hosts` is checked first. A question may ask how to make `webserver` resolve to a private IP on a single machine — the answer is to add an entry to `/etc/hosts`, not to configure DNS.
*   **`ss -tuln` vs `netstat`:** The exam may ask which command shows listening TCP/UDP ports. `ss -tuln` is the modern answer. Know the flags: `-t` TCP, `-u` UDP, `-l` listening only, `-n` numeric (no name resolution).
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) covers networking utilities in chapter 17. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) includes video demonstrations of `ip`, `nmcli`, and network troubleshooting workflows in a live environment.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read chapter 17 of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), covering networking tools including `ping`, `traceroute`, `netstat`, and remote access utilities on Linux.
*   **Required Video:** Watch the networking configuration videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free YouTube playlist that demonstrates interface management, IP assignment, and DNS configuration with live examples.

---

### Lab & Command Integration
In this week's hands-on lab you will use `ip addr show` to identify interfaces, assign a temporary IP with `ip addr add`, verify routing with `ip route show`, add a host entry to `/etc/hosts`, test connectivity with `ping`, and view listening ports with `ss -tuln`.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read chapter 17 in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the networking videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
