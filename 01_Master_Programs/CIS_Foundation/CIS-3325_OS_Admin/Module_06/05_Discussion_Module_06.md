# Discussion Forum: Module 06 - Process Management

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

### Scenario A - Runaway Process on a Production Web Server

You are the on-call administrator for a production e-commerce site. At 2 AM you receive an alert
that the web server is unresponsive. You log in and find that a PHP worker process with PID 18432
is consuming 99% CPU and has been running for 6 hours. The process is not responding to anything.
Active customer sessions are currently connected to the server.

1. Describe the correct sequence of signals to send to PID 18432, starting with the least
   disruptive option and escalating only if necessary. Explain what each signal does and why
   the order matters for a production environment with live sessions.
2. After terminating the process, you notice that three zombie processes appear with PPID 18432.
   Explain why these zombies appeared and what will happen to them now that their parent is gone.
3. To prevent this situation from recurring, you want the PHP process manager service to
   automatically restart if it crashes. Write the systemctl command sequence and the unit file
   configuration option that enables automatic service restart.

---

### Scenario B - Service Deployment and Boot Configuration

Your team has developed a new internal monitoring agent that runs as a Linux daemon. The agent
has been packaged as a systemd service unit file and placed at /etc/systemd/system/monitor-agent.service.
You need to deploy it to a production server that cannot be rebooted during business hours.

1. Write the complete sequence of systemctl commands needed to: reload systemd's unit file
   cache, start the agent immediately, verify it is running, and configure it to survive reboots.
   Explain why each step is necessary and what would happen if you skipped daemon-reload.
2. Three weeks later, a developer edits the unit file to add a new environment variable. The
   developer runs systemctl restart monitor-agent but the new variable is not in effect.
   Identify the missing step and explain in technical terms why systemctl restart alone is
   insufficient after a unit file change.
3. You need to write a brief shell script that checks whether monitor-agent is active and
   emails the team if it is not. Write the systemctl command whose exit code you would test
   in the script and explain how exit codes make this suitable for automated monitoring.

---

### Scenario C - System Performance Investigation

Users are reporting that a Linux server is responding slowly. You log in and run top. You observe:
load average 8.42, 7.91, 6.23 on a 4-CPU system. The CPU breakdown shows us=12%, sy=8%, wa=74%,
id=5%. There are 47 processes in D state. Two processes have been running with nice value -10
for weeks with no administrative record of who set that priority.

1. Interpret the load average and CPU breakdown. What do these numbers indicate about the
   nature of the performance problem? What hardware component is most likely the bottleneck
   and what command would you use to confirm your diagnosis?
2. The processes in D state cannot be killed with SIGKILL. Explain why this is the case and
   what the D state represents. What is the correct diagnostic approach and what conditions
   would allow these processes to eventually exit the D state?
3. Address the unauthorized nice value of -10 on the two mystery processes. Explain what
   this priority level means relative to default processes and other users' processes.
   Write the renice command to return both processes to the default priority, and explain
   what controls you would implement to prevent unauthorized priority escalation in the future.

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 06 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

Process management is where abstract concepts meet real system behavior. The difference between an
administrator who panics at 2 AM and one who methodically diagnoses is usually the ability to read
ps output accurately, apply the right signal at the right time, and understand why a zombie cannot
be killed. systemd has made service management more consistent across Linux distributions, but the
underlying concepts — signals, process states, parent-child relationships — predate systemd by
decades and will outlast it. Know the fundamentals well enough that the tools are secondary.
