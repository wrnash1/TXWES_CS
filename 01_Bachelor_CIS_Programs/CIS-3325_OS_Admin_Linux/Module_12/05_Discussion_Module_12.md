# Discussion: Module 12 — System Services and Daemons

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This discussion is worth 50 points. Post an original response to the scenario below AND reply substantively to at least two classmates.

**Due Date:** By end of day Sunday of the current module week.

---

### Discussion Prompt

**Scenario:**

You are a Linux administrator at a healthcare company. You have just deployed a new patient data processing application on a Rocky Linux 9 server. The application is a Python daemon that listens on port 8443, runs as a dedicated service account (`appuser`), and must start automatically after every reboot. The vendor provides only a README with the startup command:

```
/usr/bin/python3 /opt/patientapp/server.py --config /etc/patientapp/app.conf
```

Additionally, the following operational requirements have been provided by the IT security team:

- The service must restart automatically if it crashes unexpectedly
- All service output must go to the systemd journal (not a separate log file)
- The service must run as `appuser`, not root
- A daily maintenance script at `/opt/patientapp/maintenance.sh` must run at 2:00 AM every day
- The security team wants a weekly configuration backup every Sunday at midnight

---

### Discussion Questions

Address ALL of the following in your initial post:

**Question 1 — Unit File Design**

Write the complete systemd service unit file for this application. Your unit file must satisfy all requirements listed above. Explain each directive you use and why it is necessary. Include appropriate security hardening directives from the systemd sandboxing options discussed in the reading guide.

**Question 2 — Deployment Procedure**

Walk through the complete sequence of commands an administrator would run to deploy this service, from placing the unit file to verifying it is running and enabled. Explain why order matters (specifically, why `daemon-reload` must precede `enable`).

**Question 3 — Cron Configuration**

Write the crontab entries for both scheduled tasks (daily maintenance and weekly backup). Should these be in the `appuser` crontab, the root crontab, or `/etc/crontab`? Justify your choice based on the principle of least privilege. What output handling would you add to each cron entry?

**Question 4 — Log Analysis**

One week after deployment, the security team reports that the service crashed three times overnight but they don't know why. Write the exact `journalctl` commands you would run to:

- View only the error and critical entries from the service
- Compare the service logs across the last three boot sessions to identify a pattern
- Check whether any system-level errors (kernel or authentication) occurred around the same times

Explain what you would look for in each output.

**Question 5 — Reflection**

In your own words, explain why the transition from SysVinit to systemd matters practically for a Linux administrator — not the technical internals, but the day-to-day operational difference. What capability in systemd do you find most valuable and why?

---

### Reply Requirements

When responding to classmates, engage with at least one of these points:

- Review their unit file — did they include all required directives? Did they overlook any security hardening?
- Evaluate their crontab approach — would you make different privilege choices?
- Share an alternative journalctl command or filter that provides additional diagnostic value

---

### Grading Rubric

| Criterion | Points |
|-----------|--------|
| Unit file is correct, complete, and includes hardening directives | 15 |
| Deployment procedure is in correct order with explanations | 10 |
| Cron entries are syntactically correct with privilege justification | 10 |
| journalctl commands are accurate and analysis is thoughtful | 10 |
| Reflection is substantive and demonstrates understanding | 5 |
| **Total** | **50** |

---

### Instructor Notes

The most common mistakes in this discussion are:

- Writing `ExecStart` with a relative path (must be absolute)
- Forgetting `sudo systemctl daemon-reload` before enabling
- Putting cron jobs in root's crontab when `appuser` has the necessary permissions
- Using `journalctl -u <service>` without time or boot filters, making it hard to isolate the relevant window

Strong posts will also consider what happens if the service fails to start entirely — how would you distinguish between a configuration error, a missing dependency, and a runtime crash using only `systemctl` and `journalctl`?
