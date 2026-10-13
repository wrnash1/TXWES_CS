# Discussion Forum: Module 09 - Networking Configuration

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

### Scenario A - New Server Deployment with Static IP

Your team is deploying a new Ubuntu Server for a web application. The server needs a static IP
address of 10.20.30.50/24 with a default gateway of 10.20.30.1 and DNS servers of 10.20.30.10
and 8.8.8.8. The server has one interface named ens192. After deployment, the server must be
reachable via its hostname app01.prod.example.com from other systems on the network.

1. Write the complete nmcli command sequence to configure the static IP, gateway, and DNS
   servers persistently. Include the command to apply the changes and the command to verify
   the configuration took effect. Explain what ipv4.method manual means and what would happen
   if you forgot to set it.
2. After setting the IP and DNS, what changes must be made so that other servers on the
   network can resolve app01.prod.example.com? Describe two approaches: one using
   /etc/hosts on each client server, and one using DNS. Explain the trade-offs of each
   approach for a fleet of 50 servers.
3. You run ss -tulnp after initial setup and see no services listening on ports 80 or 443.
   Write the commands you would run to check whether nginx is installed, installed but not
   started, or running on unexpected ports. Describe what the output of each command tells you.

---

### Scenario B - Network Connectivity Troubleshooting

A developer reports that a staging server cannot reach an external API at api.partner.com
on port 443. Other servers in the same rack can reach the API without problems. You log in
to the affected server and need to systematically diagnose the problem.

1. Describe the layer-by-layer troubleshooting methodology from physical to application
   layer. For each layer, write the specific command you would run on this server and
   describe what a successful result looks like. Include at least five distinct layers
   with separate commands.
2. You discover that ping 8.8.8.8 succeeds but dig api.partner.com returns SERVFAIL from
   the configured nameserver. Meanwhile, dig @8.8.8.8 api.partner.com returns a valid
   IP address. What does this tell you about the nature of the problem? Write the cat
   command to view the current nameserver configuration and the nmcli command to replace
   the broken nameserver with 8.8.8.8 persistently.
3. After fixing DNS, dig api.partner.com resolves correctly, but curl https://api.partner.com
   still fails with "Connection refused." Write the ss and telnet (or nc) commands that
   would confirm the port is blocked before the traffic reaches the remote server, and
   distinguish between a local firewall block and a remote service that is down.

---

### Scenario C - DNS Override and Name Resolution Conflicts

A QA team reports an intermittent problem: their test scripts connect to the production
database instead of the QA database, but only on two of ten QA servers. You investigate
and discover that those two servers have manual entries in /etc/hosts that map the database
hostname to the production IP.

1. Explain the mechanism by which /etc/hosts entries override DNS and which configuration
   file controls this behavior. Describe what would happen if the /etc/nsswitch.conf file
   had dns files instead of files dns on those two servers. Would the problem still occur?
2. Write the commands to find and remove the incorrect /etc/hosts entry on both servers.
   After removal, write the dig command that confirms the hostname now resolves to the
   correct QA database IP from DNS. Also explain why flushing the DNS cache may be
   necessary and how to do it on a systemd-resolved system.
3. To prevent this class of problem in the future, describe two administrative controls
   you would implement: one technical control that detects /etc/hosts overrides automatically,
   and one procedural control that prevents unauthorized changes to resolution configuration
   files. Be specific about the Linux tools or mechanisms involved.

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 09 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

Network configuration problems follow a pattern: something worked, then something changed,
and now it does not work. The administrator who can systematically isolate which layer
changed — physical, IP, routing, DNS, or application — diagnoses in minutes instead of
hours. The tools in this module (ip, ss, dig, ping, traceroute) are not complicated. What
takes experience is knowing which tool to run first and how to interpret the output. Develop
a troubleshooting checklist and follow it every time. Consistency is faster than intuition.
