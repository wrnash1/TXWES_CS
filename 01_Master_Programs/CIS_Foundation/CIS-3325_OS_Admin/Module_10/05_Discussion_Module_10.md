# Discussion Forum: Module 10 - SSH and Remote Access Security

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

### Scenario A - SSH Hardening for a Public-Facing Server

Your organization deploys a new Ubuntu Server that will be accessible from the public internet
to host a customer-facing web application. The security team requires that SSH be hardened
before the server goes live. The server currently has only password authentication enabled and
root login permitted.

1. Write the complete list of sshd_config changes you would make, with the exact directive and
   value for each. For each change, explain the specific threat it mitigates. Include at minimum:
   PermitRootLogin, PasswordAuthentication, AllowUsers, MaxAuthTries, and LoginGraceTime.
2. Before disabling PasswordAuthentication, you must set up key-based authentication for the
   deployment team of three administrators. Describe the complete workflow, including which
   commands each administrator runs on their own workstation and what you do on the server.
   What would happen if you disabled password authentication before completing this step?
3. After all hardening changes are applied, describe how you would verify that the intended
   changes are effective without being locked out. What is the danger of testing from the same
   SSH session you used to make the changes, and how do you avoid it?

---

### Scenario B - Automated Backup Using rsync and SSH Keys

Your team needs to implement an automated nightly backup from a production web server to a
dedicated backup server. The backup must run unattended at 2 AM without any human interaction.
The source is /var/www and /etc on the production server. The destination is /backups/prod/ on
the backup server.

1. Explain why a passphrase-protected SSH key cannot be used for automated backups without
   additional tooling, and describe the two approaches that allow automated SSH authentication:
   a passphrase-free key and an SSH agent. Discuss the security trade-off of each approach for
   a production backup system.
2. Write the complete rsync command for the backup job that: preserves all permissions and
   timestamps, compresses data in transit, removes files deleted from the source, and logs
   output to /var/log/backup.log. Explain what each flag does.
3. After several months, a new disk is added to the production server and its contents also
   need to be backed up. The backup script currently uses --delete. A junior administrator
   proposes just adding the new path to the rsync command. Explain the risk of changing a
   live rsync --delete job without testing first, and describe the correct testing procedure
   using rsync -n before modifying the production cron job.

---

### Scenario C - SSH Incident Response

Your security monitoring system alerts that there have been 5,000 failed SSH login attempts
from IP addresses in an external range over the past hour against a production server. The
server currently accepts password authentication on port 22. The operations team is concerned
that an account may have been compromised.

1. Describe three immediate technical responses to stop the ongoing brute-force attack. For
   each response, write the specific command and explain whether it is a temporary mitigation
   or a permanent control. Consider both firewall-based and SSH configuration-based responses.
2. To determine whether any account was actually compromised, describe the log files you would
   examine and the specific information (patterns, log entries) that would indicate a successful
   unauthorized login. Write the grep command that would extract successful SSH authentications
   from the relevant log file.
3. Going forward, describe the hardening changes you would implement to make this class of
   attack impossible rather than just difficult. Explain specifically why disabling password
   authentication with key-based auth only is a more robust control than rate limiting or
   changing the port.

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 10 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

SSH is the single most targeted service on internet-facing Linux servers. Every publicly
accessible server running SSH on port 22 with password authentication will receive brute-force
attempts within hours of going online — this is not hypothetical, it is observable. Key-based
authentication makes the brute-force attack category essentially irrelevant because there is
nothing to guess. The combination of PasswordAuthentication no, PermitRootLogin no, and
AllowUsers with an explicit list transforms SSH from a commonly compromised entry point into
a properly controlled administrative channel. Learn these settings well enough to apply them
in your first five minutes on any new server.
