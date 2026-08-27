# Lab Activity: Module 14 - SELinux and AppArmor Security

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Time:** 80 minutes
**Points:** 100

---

### Objectives

By the end of this lab you will be able to:

* Check SELinux mode and interpret `getenforce` output on a RHEL-family system
* Identify SELinux file contexts and find AVC denial messages
* Apply a permanent SELinux context fix using `semanage fcontext` and `restorecon`
* Toggle SELinux booleans at runtime and persistently
* Check AppArmor profile status on Ubuntu and switch between complain and enforce mode
* Locate AppArmor denial messages in the journal
* Apply the correct troubleshooting workflow for each MAC system

---

### Lab Structure

This lab has two sections. Parts 1-4 cover SELinux and are performed on a RHEL 9 virtual machine
(or Rocky Linux 9 / AlmaLinux 9 — all are equivalent for this lab). Parts 5-6 cover AppArmor
and are performed on an Ubuntu 22.04 virtual machine.

If you only have access to one VM type, complete the parts that match your distribution and read
through the other section carefully to understand the concepts.

---

### Prerequisites

**RHEL 9 VM:**

* SELinux in enforcing mode (default on RHEL 9)
* `policycoreutils-python-utils` installed: `sudo dnf install -y policycoreutils-python-utils`
* Apache httpd installed: `sudo dnf install -y httpd`

**Ubuntu 22.04 VM:**

* AppArmor installed and running (default on Ubuntu 22.04)
* `apparmor-utils` installed: `sudo apt install -y apparmor-utils`
* nginx installed: `sudo apt install -y nginx`

---

### Part 1 — SELinux Mode and Status (RHEL) (15 points)

#### Step 1.1 — Check current SELinux mode

```bash
getenforce
sestatus
```

Record the current mode. On a default RHEL 9 install it should be `Enforcing`.

#### Step 1.2 — Check the persistent configuration

```bash
cat /etc/selinux/config
```

Locate the `SELINUX=` line. This is the mode that will be applied at next boot.

#### Step 1.3 — Switch to permissive mode and back

```bash
sudo setenforce 0
getenforce
sudo setenforce 1
getenforce
```

Confirm the mode changes immediately with `getenforce`. Note that `/etc/selinux/config` is
unchanged — `setenforce` only affects the current runtime state.

#### Step 1.4 — Inspect file contexts

```bash
ls -Z /var/www/html/
ls -Z /etc/httpd/conf/httpd.conf
ls -Z /tmp/
```

Note the type field in each context. Web content uses `httpd_sys_content_t`. Config files use
`httpd_config_t`. Files in `/tmp` use `tmp_t`.

#### Step 1.5 — Inspect process contexts

```bash
sudo systemctl start httpd
ps auxZ | grep httpd | head -3
```

The Apache process should show the `httpd_t` type. Only processes with `httpd_t` context can
access files typed `httpd_sys_content_t` under the default policy.

---

### Part 2 — SELinux Context Fix Workflow (RHEL) (25 points)

#### Step 2.1 — Create a file with the wrong context

```bash
sudo mkdir -p /srv/weblab
echo "<h1>Lab 14 Test Page</h1>" | sudo tee /srv/weblab/index.html
ls -Z /srv/weblab/index.html
```

The file will have a context like `unconfined_u:object_r:var_t:s0` — not the `httpd_sys_content_t`
that Apache requires.

#### Step 2.2 — Configure Apache to serve from the new directory

```bash
sudo tee /etc/httpd/conf.d/weblab.conf > /dev/null << 'EOF'
Alias /weblab /srv/weblab
<Directory /srv/weblab>
    Require all granted
</Directory>
EOF
sudo systemctl restart httpd
```

#### Step 2.3 — Test and observe the failure

```bash
curl http://localhost/weblab/
```

You should receive a 403 Forbidden error. DAC permissions are open, but SELinux is blocking it.

#### Step 2.4 — Find the AVC denial

```bash
sudo ausearch -m avc -ts recent
```

Identify the denial for the `/srv/weblab/index.html` file. Look for `httpd_t` attempting to access
the file and being denied.

```bash
sudo ausearch -m avc -ts recent | audit2why
```

This gives a plain-English explanation and suggests a fix.

#### Step 2.5 — Apply the temporary fix with chcon

```bash
sudo chcon -t httpd_sys_content_t /srv/weblab/index.html
ls -Z /srv/weblab/index.html
curl http://localhost/weblab/
```

The page should now load. But this fix is temporary.

#### Step 2.6 — Reset and apply the permanent fix

```bash
sudo restorecon /srv/weblab/index.html
ls -Z /srv/weblab/index.html
curl http://localhost/weblab/
```

After `restorecon`, the context reverts and the page fails again — confirming `chcon` was
temporary.

Now apply the permanent fix:

```bash
sudo semanage fcontext -a -t httpd_sys_content_t "/srv/weblab(/.*)?"
sudo restorecon -Rv /srv/weblab/
ls -Z /srv/weblab/index.html
curl http://localhost/weblab/
```

The context is now correct and permanent. Even if you run `restorecon` again, the file keeps the
right context because the rule is in the policy database.

---

### Part 3 — SELinux Booleans (RHEL) (15 points)

#### Step 3.1 — List and search booleans

```bash
getsebool -a | grep httpd | head -20
```

Review the available httpd booleans and their current states.

#### Step 3.2 — Check a specific boolean

```bash
getsebool httpd_can_network_connect
```

On a default RHEL 9 system this is `off`.

#### Step 3.3 — Set a boolean temporarily

```bash
sudo setsebool httpd_can_network_connect on
getsebool httpd_can_network_connect
```

The value is now `on` at runtime.

#### Step 3.4 — Reboot simulation: check persistence

Without actually rebooting, check the persistent state:

```bash
semanage boolean -l | grep httpd_can_network_connect
```

The output shows the current (runtime) value and the persistent (default) value. Because we did
not use `-P`, the persistent value is still `off`.

#### Step 3.5 — Set the boolean persistently

```bash
sudo setsebool -P httpd_can_network_connect on
semanage boolean -l | grep httpd_can_network_connect
```

Now both the runtime and persistent values show `on`.

Reset it when done:

```bash
sudo setsebool -P httpd_can_network_connect off
```

---

### Part 4 — SELinux Cleanup (RHEL) (5 points)

```bash
sudo rm -f /etc/httpd/conf.d/weblab.conf
sudo rm -rf /srv/weblab
sudo systemctl stop httpd
sudo semanage fcontext -d "/srv/weblab(/.*)?" 2>/dev/null
echo "SELinux lab cleanup complete"
```

---

### Part 5 — AppArmor Status and Modes (Ubuntu) (20 points)

#### Step 5.1 — Check AppArmor service status

```bash
sudo systemctl status apparmor
sudo aa-status
```

Review the output. Note how many profiles are loaded in enforce mode vs complain mode.

#### Step 5.2 — Find the nginx profile

```bash
ls /etc/apparmor.d/ | grep nginx
sudo aa-status | grep nginx
```

The nginx profile should be listed. If it is in enforce mode, note that.

#### Step 5.3 — Switch nginx to complain mode

```bash
sudo aa-complain /etc/apparmor.d/usr.sbin.nginx
sudo aa-status | grep nginx
```

Confirm nginx is now in complain mode.

#### Step 5.4 — Switch nginx back to enforce mode

```bash
sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx
sudo aa-status | grep nginx
```

Confirm nginx is back in enforce mode.

#### Step 5.5 — Verify nginx still works after mode changes

```bash
sudo systemctl restart nginx
curl http://localhost/ | head -5
```

nginx should respond normally — the profile has not changed, only the mode was toggled.

---

### Part 6 — AppArmor Log Analysis (Ubuntu) (20 points)

#### Step 6.1 — Create a file that nginx cannot access

```bash
sudo mkdir -p /srv/weblab-ubuntu
echo "<h1>AppArmor Test</h1>" | sudo tee /srv/weblab-ubuntu/index.html
sudo chmod 644 /srv/weblab-ubuntu/index.html
```

#### Step 6.2 — Configure nginx to serve from that directory

```bash
sudo tee /etc/nginx/sites-available/weblab << 'EOF'
server {
    listen 8099;
    root /srv/weblab-ubuntu;
    index index.html;
}
EOF
sudo ln -sf /etc/nginx/sites-available/weblab /etc/nginx/sites-enabled/weblab
sudo systemctl reload nginx
```

#### Step 6.3 — Test and observe the AppArmor denial

```bash
curl http://localhost:8099/
```

This will return a 403 because the nginx AppArmor profile does not allow access to `/srv/weblab-ubuntu/`.

#### Step 6.4 — Find the AppArmor denial

```bash
sudo journalctl -k | grep apparmor | tail -10
```

Look for a DENIED entry showing nginx attempting to access `/srv/weblab-ubuntu/index.html`.

#### Step 6.5 — Switch to complain mode and confirm the page loads

```bash
sudo aa-complain /etc/apparmor.d/usr.sbin.nginx
sudo systemctl reload nginx
curl http://localhost:8099/
```

In complain mode, the access is allowed and the page loads. The denial is only logged, not
enforced.

#### Step 6.6 — Check the complain-mode log entry

```bash
sudo journalctl -k | grep apparmor | tail -5
```

You should now see an `ALLOWED` entry (complain mode) instead of `DENIED`.

Switch back to enforce mode:

```bash
sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx
sudo systemctl reload nginx
```

---

### Analysis Questions

Answer these questions in writing after completing the lab. Submit with your lab screenshots.

1. Explain the difference between `chcon` and the `semanage fcontext + restorecon` two-step approach. In what scenario would `chcon` be the right tool, and when is the permanent approach always required?

2. You use `setenforce 0` to troubleshoot a problem and confirm SELinux was causing it. List the exact steps to properly fix the issue and restore SELinux to enforcing mode, ensuring the fix survives a reboot.

3. What does `ausearch -m avc -ts recent | audit2why` tell you that `ausearch -m avc -ts recent` alone does not? Why is `audit2why` useful in the troubleshooting workflow?

4. You run `aa-status` on an Ubuntu server and see nginx listed under "profiles in complain mode." A developer reports that nginx cannot read files from `/opt/webapp/`. Will AppArmor block that access? Explain what complain mode does and what you would need to do to permanently allow nginx to read `/opt/webapp/`.

5. Compare SELinux Permissive mode and AppArmor complain mode. In what way are they functionally equivalent? In what way does the underlying mechanism differ between the two MAC systems?

---

### Submission Requirements

* Screenshots of each Part completion (terminal output visible)
* Written answers to all 5 analysis questions
* Screenshot of the permanent SELinux context fix showing `ls -Z` before and after

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| Part 1: SELinux mode checked and runtime toggle demonstrated | 15 |
| Part 2: AVC denial found and permanent context fix applied | 25 |
| Part 3: Boolean set temporarily and persistently | 15 |
| Part 4: Cleanup completed | 5 |
| Part 5: AppArmor modes toggled correctly | 20 |
| Part 6: AppArmor denial found in journal | 20 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: SELinux Custom Port Context (RHEL)
A custom web application needs Apache to listen on port 8443 in addition to the standard ports. SELinux blocks Apache from binding to non-standard ports.
1. Verify the denial by starting httpd with a custom `Listen 8443` directive in `/etc/httpd/conf.d/lab14-port.conf` and checking `ausearch -m avc -ts recent` for the port bind denial.
2. Use `semanage port -l | grep http` to confirm port 8443 is not currently assigned the `http_port_t` type.
3. Run the correct `semanage port -a` command to add port 8443 to the `http_port_t` type for TCP.
4. Restart Apache and confirm it now binds to 8443 with `ss -tuln | grep 8443`. Clean up by removing the port context and the test config file when finished.

### Challenge 2: AppArmor Profile Refinement with aa-logprof (Ubuntu)
Practice the full AppArmor profile development workflow for a script-based application.
1. Create a simple shell script at `/usr/local/bin/lab14-reader.sh` that reads `/etc/hostname` and writes output to `/tmp/lab14-out.txt`. Make it executable.
2. Generate an initial restrictive profile with `sudo aa-genprof /usr/local/bin/lab14-reader.sh` — when prompted, run the script in a second terminal and then press S to scan for events, accepting suggested rules. Finish and save.
3. Confirm the profile is in enforce mode with `sudo aa-status | grep lab14-reader`.
4. Add a new write operation to the script (e.g., also write to `/tmp/lab14-out2.txt`) and run it again — the new path will be denied. Run `sudo aa-logprof` to review the denial, accept the suggested rule, and reload the profile with `apparmor_parser -r`. Confirm the script now runs without denial.

### Reflection Questions
1. Explain why `chcon` changes are overwritten when `restorecon` runs, but `semanage fcontext` changes are not. What is the underlying difference in where each tool stores its information?
2. A security audit finds that SELinux is in permissive mode on a production RHEL server. The previous administrator left a note saying "needed permissive mode to make the application work." Describe the correct process to identify exactly what SELinux was blocking and implement a targeted fix that allows enforcing mode to be restored.

---

### Cleanup (Ubuntu)

```bash
sudo rm -f /etc/nginx/sites-enabled/weblab
sudo rm -f /etc/nginx/sites-available/weblab
sudo rm -rf /srv/weblab-ubuntu
sudo systemctl reload nginx
echo "AppArmor lab cleanup complete"
```
