# Reading Guide: Module 11 - Firewall Management
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 11 – Firewall Management**! This week covers Linux host-based firewall configuration — from the `firewalld` zone model used on RHEL/CentOS/Fedora, to `ufw` (Uncomplicated Firewall) on Debian/Ubuntu, to the underlying `iptables` framework that both tools manage. Firewall management is tested on CompTIA Linux+ XK0-005 under Domain 2.0 (Security) and is a common scenario question topic.

As you work through this material you will learn how to allow and block services and ports, manage firewall zones, make rules persistent, and understand how `iptables` chains and targets work at the packet-filtering level.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **`firewalld` and zones**: The dynamic firewall daemon used on RHEL, CentOS, and Fedora systems. `firewalld` organizes rules into named zones (e.g., `public`, `home`, `trusted`, `drop`) that define how traffic is treated based on the source network or interface. The active zone for an interface is set with `firewall-cmd --zone=public --change-interface=eth0`. List rules with `firewall-cmd --list-all`. Changes made without `--permanent` are runtime-only and lost at reboot.
*   **`firewall-cmd`**: The command-line client for `firewalld`. Key operations: `firewall-cmd --permanent --add-service=http` (allow HTTP), `firewall-cmd --permanent --add-port=8080/tcp` (allow a specific port), `firewall-cmd --permanent --remove-service=ftp` (block a service), `firewall-cmd --reload` (apply permanent rules to the running configuration). The `--permanent` flag writes to the persistent configuration; without it, changes apply only until the next reload or reboot.
*   **`ufw` (Uncomplicated Firewall)**: A simplified front-end for `iptables` used on Debian and Ubuntu systems. `ufw enable` activates the firewall; `ufw allow ssh` or `ufw allow 22/tcp` permits SSH; `ufw deny 23/tcp` blocks Telnet; `ufw status verbose` shows current rules. Rules added with `ufw` are automatically persistent. `ufw` is disabled by default on fresh Ubuntu installs.
*   **`iptables`**: The legacy Linux kernel packet-filtering framework that underlies both `firewalld` and `ufw`. Organizes rules into chains: `INPUT` (inbound to the host), `OUTPUT` (outbound from the host), and `FORWARD` (routed traffic). Each rule specifies a target: `ACCEPT`, `DROP` (silently discard), or `REJECT` (discard and send ICMP error). Rules are processed top-to-bottom; the first match wins. `iptables -L -n -v` lists all rules with packet counts.
*   **Default policy and rule order**: The default policy for a chain (e.g., `iptables -P INPUT DROP`) defines what happens when no rule matches — common secure practice is to default-deny inbound traffic and explicitly allow needed services. Rule order matters: if an ACCEPT rule for port 22 appears before a DROP-all rule, SSH is permitted. The `iptables -I INPUT 1` flag inserts a rule at position 1 (top of the chain).
*   **Persistent `iptables` rules**: Unlike `firewalld` and `ufw`, raw `iptables` rules are not automatically saved. On RHEL systems, install and use `iptables-services` and run `service iptables save`. On Debian/Ubuntu use the `iptables-persistent` package with `netfilter-persistent save`. Without persistence, all rules are lost at reboot.

---

### 2. Certification Exam Tips
*   **Domain alignment:** Firewall management maps to Linux+ Domain 2.0 (Security). Expect 4–6 questions on `firewalld` commands, `ufw` syntax, and `iptables` chain/target concepts.
*   **`--permanent` trap:** The most common `firewall-cmd` exam trap is forgetting `--permanent`. A rule added without `--permanent` is active immediately but disappears after `firewall-cmd --reload` or a reboot. The exam may present a scenario where a rule "stops working after reboot" — the answer is that `--permanent` was omitted.
*   **`firewall-cmd --reload` vs `--complete-reload`:** `--reload` applies permanent rules while keeping existing connections open. `--complete-reload` drops all active connections. On the exam, `--reload` is always the safer answer unless asked about a clean state.
*   **`iptables` chain direction:** Memorize: `INPUT` = traffic destined for the local host, `OUTPUT` = traffic originating from the local host, `FORWARD` = traffic passing through (router function). A web server rule allowing port 80 belongs in the `INPUT` chain, not `OUTPUT`.
*   **`ufw` default state:** `ufw` is inactive by default on Ubuntu. An exam scenario where a firewall rule has no effect may indicate `ufw` has not been enabled with `ufw enable`.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) provides foundational context for Linux networking and security. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) includes video demonstrations of `firewalld`, `ufw`, and `iptables` configuration in a live Linux environment.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the networking and security chapters of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), which provide foundational knowledge of Linux network services and access control relevant to firewall configuration.
*   **Required Video:** Watch the firewall management videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free YouTube playlist that demonstrates `firewalld` zone management, `ufw` rule configuration, and `iptables` chain filtering with live examples.

---

### Lab & Command Integration
In this week's hands-on lab you will enable `ufw`, allow SSH and HTTP, verify rules with `ufw status verbose`, then use `firewall-cmd` to add a permanent service rule, reload the firewall, and verify persistence after a reload. You will also inspect `iptables -L -n` to understand the underlying rules generated by both tools.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the relevant chapters in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the firewall management videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
