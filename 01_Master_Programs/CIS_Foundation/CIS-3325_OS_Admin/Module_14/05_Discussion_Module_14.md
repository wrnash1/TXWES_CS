# Discussion Forum: Module 14 - SELinux and AppArmor Security

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Points:** 10
**Initial Post Due:** Wednesday at 11:59 PM
**Peer Responses Due:** Sunday at 11:59 PM

---

### Instructions

Choose one of the three scenarios below. Write an initial post of 175 to 225 words that addresses
all three sub-questions for your chosen scenario. After posting, respond to at least two classmates
who chose different scenarios. Each response should be at least 75 words and add substantive
technical content.

---

### Scenario A - SELinux Context Troubleshooting

A developer reports that after deploying a new Python web application to `/opt/webapp/`, the
application returns 500 errors when attempting to read configuration files from `/etc/webapp/`.
The server runs RHEL 9 with SELinux in enforcing mode. You have verified that the Unix file
permissions are correct — the application user can read both directories — but the errors persist.

1. Write the exact diagnostic commands you would run first to determine whether SELinux is causing
   the problem. Explain what AVC denial messages are, where they are stored, and what information
   they contain that helps identify the fix. Include the `audit2why` command in your workflow and
   explain what it adds beyond reading the raw audit log.
2. After confirming SELinux is the cause, you identify that `/etc/webapp/` has the type
   `etc_t` and the application process runs with a custom confined type. Write the complete
   two-command sequence to permanently fix the context for all files in `/etc/webapp/` so they
   survive a future relabeling. Explain why `chcon` alone is not acceptable for a production fix.
3. A colleague suggests simply setting `setenforce 0` permanently to avoid these SELinux issues.
   Write a professional response explaining why this is the wrong approach, what security
   properties are lost when SELinux is disabled, and what the correct long-term solution is
   for managing SELinux in a production environment.

---

### Scenario B - AppArmor Profile Development on Ubuntu

Your team is deploying a new internal tool called `inventoryd` on Ubuntu 22.04. The binary is at
`/usr/local/bin/inventoryd` and currently has no AppArmor profile. The tool reads from
`/etc/inventoryd/`, writes logs to `/var/log/inventoryd/`, and makes outbound HTTPS connections
to an internal API server.

1. Describe the recommended workflow for developing an AppArmor profile for a new application,
   starting from no profile through deployment in enforce mode. Reference the specific tools
   `aa-genprof`, `aa-complain`, `aa-logprof`, and `aa-enforce` in the correct sequence. Explain
   what each tool does and why the complain-mode testing phase is important before switching to
   enforce mode.
2. After running `inventoryd` through its normal operations in complain mode, you run `aa-logprof`
   and it presents several access requests to approve or deny. Explain how you would decide which
   accesses to allow versus deny. Give examples of accesses that should be approved (based on the
   described functionality) and one category of access you would deny as unnecessarily broad.
3. Six months after deployment, a software update to `inventoryd` adds a new feature that writes
   reports to `/var/lib/inventoryd/reports/`. After the update, the feature fails silently. Explain
   the complete workflow to diagnose and fix this AppArmor issue, including the specific log
   command to find the denial, the profile modification needed, and how to reload the profile
   without rebooting.

---

### Scenario C - Comparing SELinux and AppArmor for a New Deployment

Your organization is deploying a standardized Linux baseline across a mixed environment: RHEL 9
servers for backend databases and API services, Ubuntu 22.04 servers for web frontends. The
security team has asked you to document the MAC strategy for both platforms.

1. Compare SELinux and AppArmor on the following dimensions: the underlying access control
   model (label-based vs path-based), the scope of protection (what objects are labeled or
   profiled), the toolset for troubleshooting denials, and the default distribution. Explain
   why the label-based approach of SELinux is more comprehensive but also more complex to
   administer than AppArmor's path-based profiles.
2. Both systems have a mode that logs violations without blocking them. Identify the correct
   mode name for each system (not just "permissive" — use the correct term for AppArmor as
   well). Explain a production scenario where you would deliberately put a system into this
   non-enforcing mode, what risk this introduces, and what procedure you would follow to ensure
   you do not forget to re-enable enforcement.
3. The security team wants to know: if an administrator with root access runs a command that
   SELinux policy forbids, what happens? Does the same apply to AppArmor? Explain how MAC
   overrides DAC, what "root cannot override MAC" means in practice, and under what specific
   conditions a root user can legitimately modify MAC policy.

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 14 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

MAC security is the layer that protects a system even after it has been partially compromised.
If an attacker exploits a vulnerability in your web server and gains code execution, standard
Unix permissions do not stop them from pivoting — they already have the web server's identity.
SELinux and AppArmor constrain what that compromised process can actually do: it cannot read
your SSH keys, cannot write to system binaries, cannot make network connections it was not
designed to make. That containment is the value of MAC. The administrators who disable SELinux
"because it keeps blocking things" are removing their last line of defense for the sake of
avoiding ten minutes of troubleshooting. Learn the tools. Fix the context. Keep enforcement on.
