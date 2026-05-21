# Quiz: Module 11 - Firewall Management
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
An administrator on a RHEL 9 server runs `firewall-cmd --add-service=https` to allow HTTPS traffic. After a reboot, HTTPS is blocked again. What was the cause?
A) The `firewalld` service was not running when the command was executed.
B) The `--permanent` flag was omitted, so the rule was added only to the runtime configuration and not saved persistently.
C) HTTPS requires a separate `--add-port=443/tcp` command in addition to `--add-service=https`.
D) `firewall-cmd` changes require a subsequent `systemctl restart firewalld` to take effect.
*   **Correct Answer:** B) The `--permanent` flag was omitted, so the rule was added only to the runtime configuration and not saved persistently.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* If `firewalld` were not running, the command itself would have failed with an error. The fact that HTTPS worked until the reboot confirms `firewalld` was active and the rule was applied — just not persistently.
    *   *Why C is incorrect:* `--add-service=https` already includes port 443/tcp as part of the service definition in `firewalld`'s service library. A separate `--add-port` is not needed when using a named service.
    *   *Why D is incorrect:* `systemctl restart firewalld` would actually wipe the non-permanent runtime rule. The correct workflow is to use `--permanent` when adding the rule, then run `firewall-cmd --reload` to apply the permanent config to the running state.

---

---

**Question 2**
A security administrator needs to allow TCP port 8443 through the firewall on an Ubuntu 22.04 server using `ufw`. After running `ufw allow 8443/tcp`, traffic on port 8443 is still blocked. What is the most likely cause?
A) `ufw` rules require a reboot to take effect after being added.
B) Port 8443 is reserved and cannot be opened with `ufw`.
C) `ufw` was never enabled with `ufw enable` and is still inactive.
D) The rule must be added to both the `INPUT` and `OUTPUT` chains separately using `ufw allow in 8443/tcp` and `ufw allow out 8443/tcp`.
*   **Correct Answer:** C) `ufw` was never enabled with `ufw enable` and is still inactive.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `ufw` rules take effect immediately when `ufw` is active — no reboot is required. Rules are also automatically persistent across reboots.
    *   *Why B is incorrect:* Port 8443 is a common HTTPS alternate port and is not reserved or restricted. `ufw` has no list of forbidden ports; any valid port number from 1–65535 can be allowed or denied.
    *   *Why D is incorrect:* `ufw allow 8443/tcp` without a direction flag allows inbound traffic on that port, which is the typical requirement for a server service. Separate `in`/`out` rules are not required for standard service exposure.

---

---

**Question 3**
An administrator wants to list all current `iptables` rules in the INPUT chain with packet counts and without DNS resolution of IP addresses. Which command is correct?
A) iptables --show INPUT -v
B) iptables -L INPUT -n -v
C) iptables -S INPUT
D) iptables -F INPUT
*   **Correct Answer:** B) iptables -L INPUT -n -v
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `--show` is not a valid `iptables` flag. The correct flag for listing rules is `-L`. This command would produce an error.
    *   *Why C is incorrect:* `iptables -S INPUT` prints rules in `iptables-restore` format (the save/restore syntax). It does not show packet/byte counts and is used for exporting rules, not for human-readable inspection.
    *   *Why D is incorrect:* `iptables -F INPUT` flushes (deletes) all rules in the INPUT chain. Running this on a production system would remove all inbound filtering rules, not display them.

---

**Question 4**
A Linux administrator needs to block all inbound TCP traffic on port 23 (Telnet) using `iptables` directly. The server's INPUT chain default policy is ACCEPT. Which command correctly adds the blocking rule?
A) iptables -A INPUT -p tcp --dport 23 -j DROP
B) iptables -D INPUT -p tcp --dport 23 -j ACCEPT
C) iptables -P INPUT DROP
D) iptables -A OUTPUT -p tcp --sport 23 -j DROP
*   **Correct Answer:** A) iptables -A INPUT -p tcp --dport 23 -j DROP
*   **Distractor Analysis:**
    *   *Why B is incorrect:* The `-D` flag deletes an existing rule. This command would attempt to delete an ACCEPT rule for port 23 — which likely does not exist — and would fail or have no effect on blocking inbound Telnet.
    *   *Why C is incorrect:* `iptables -P INPUT DROP` sets the default policy for the entire INPUT chain to DROP, blocking all inbound traffic that does not match an explicit ACCEPT rule. This is far broader than blocking a single port and would disrupt all inbound connections including SSH.
    *   *Why D is incorrect:* The `OUTPUT` chain applies to traffic originating from the local host. Blocking port 23 on `OUTPUT` would prevent the server from initiating outbound Telnet connections — it would not block inbound Telnet connections from external clients.

---

**Question 5**
An administrator adds a `firewalld` rule with `--permanent` but notices it is not currently active. What additional step is required to make the permanent rule take effect without rebooting?
A) Run `systemctl restart firewalld` to restart the daemon and load permanent rules.
B) Run `firewall-cmd --reload` to apply the permanent configuration to the running firewall state.
C) Run `firewall-cmd --complete-reload` to flush all active connections and load the permanent rules.
D) Log out and back in so the shell session picks up the new firewall rules.
*   **Correct Answer:** B) Run `firewall-cmd --reload` to apply the permanent configuration to the running firewall state.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `systemctl restart firewalld` restarts the entire daemon, which also loads permanent rules, but it briefly interrupts the firewall service. `firewall-cmd --reload` is the preferred method because it applies permanent rules without a service interruption.
    *   *Why C is incorrect:* `firewall-cmd --complete-reload` drops all active network connections and reloads the kernel modules. This is disruptive and reserved for situations requiring a full module reset. `--reload` is the correct non-disruptive option.
    *   *Why D is incorrect:* Firewall rules are kernel-level configuration managed by `firewalld` — they have no relationship to user shell sessions. Logging out and back in has no effect on firewall rule activation.
