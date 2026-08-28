# Video Script: Module 14 — Network Troubleshooting Methodology (Part 1 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

## Introduction

Welcome to Module 14 of CIS-3321 Network Administration. I am Professor Nash. This module is about network troubleshooting — one of the most heavily tested topics on the CompTIA Network+ N10-008 exam and one of the most valuable skills you will use every single day as a network professional.

Troubleshooting is not guessing. It is a systematic process. CompTIA defines a specific seven-step troubleshooting methodology, and the exam will present you with scenario questions designed to test whether you follow that methodology correctly.

Part 1 covers the seven-step CompTIA troubleshooting model and applies it to common network problem scenarios. Part 2 covers hardware failure symptoms, cable testing, and the specific scenario types you will encounter on the Network+ exam.

---

## Section 1: Why a Methodology Matters

Before we look at the seven steps, let me explain why using a formal troubleshooting process matters.

When a network goes down, there is pressure — from users, from managers, from SLAs. That pressure makes people want to jump to conclusions and start changing things immediately. The result is often "shotgun troubleshooting" — randomly changing settings hoping something will fix the problem. This approach causes new problems, wastes time, and leaves the root cause unresolved.

A systematic methodology forces you to:

- Understand the actual problem before acting
- Gather evidence before forming hypotheses
- Test one change at a time
- Document what you did so the problem can be resolved repeatably

The CompTIA troubleshooting methodology is not just an exam topic — it is a professional discipline.

---

## Section 2: The CompTIA Network+ Seven-Step Troubleshooting Model

CompTIA defines the following seven steps. These steps appear in the Network+ exam objectives and are directly tested.

### Step 1 — Identify the Problem

The first step is to clearly understand what is wrong. This sounds obvious, but "the network is down" is not a useful problem statement. You need specifics.

Activities in Step 1:

- Gather information from users and affected parties. Ask: What exactly is not working? When did it start? What changed recently? Does it affect everyone or just certain users?
- Identify symptoms. Are there error messages? Which specific services or applications are affected?
- Duplicate the problem if possible. Reproduce the error yourself to confirm what the user is experiencing.
- Question obvious environmental factors. Was there a power outage, a software update, a new device added to the network, a configuration change?

The key tool here is effective questioning. Open-ended questions ("What were you doing when the problem started?") reveal more than yes/no questions.

The output of Step 1 is a clear, specific problem statement — for example: "Users on the third floor cannot access the file server. The issue began this morning. Other floors are unaffected. Users can ping the default gateway but cannot reach the file server by name or IP."

### Step 2 — Establish a Theory of Probable Cause

With a clear problem statement, you now form hypotheses — educated guesses about what might be causing the problem.

Activities in Step 2:

- Consider the most common/likely causes first (Occam's Razor — the simplest explanation is usually correct).
- Use the OSI model as a framework. Start at the bottom: Is Layer 1 (physical) okay? Layer 2 (switching)? Layer 3 (routing)? Work up through the layers.
- Consult documentation, knowledge bases, and previous incident records for similar issues.
- Generate multiple hypotheses — not just one.

Common causes to consider:

- Physical: Cable unplugged, port failure, NIC failure
- Layer 2: Wrong VLAN, STP blocking, MAC table issue
- Layer 3: Wrong IP address, subnet mask error, routing issue, ARP problem
- DNS: Name resolution failure
- Application: Service not running, firewall blocking

Do not act yet — you are still theorizing.

### Step 3 — Test the Theory to Determine Cause

Now you test your hypotheses, starting with the most likely and least disruptive.

Activities in Step 3:

- Run diagnostic commands: `ping`, `traceroute`, `ipconfig/ifconfig`, `nslookup`, `netstat`, `arp`.
- Check interface status: `show interfaces`, `show ip route` (on managed switches and routers).
- Use physical testing tools: cable tester, tone generator, light meter (for fiber).
- Check event logs on servers and network devices.
- If your hypothesis is confirmed — the theory was correct, proceed to Step 4.
- If your hypothesis is not confirmed — return to Step 2 and establish a new theory.

Key principle: Test one thing at a time. If you change multiple variables simultaneously, you will not know which change fixed (or broke) the problem.

### Step 4 — Establish a Plan of Action to Resolve the Problem

Once the cause is identified, plan the fix before implementing it.

Activities in Step 4:

- Identify the solution — what specific action will resolve the root cause?
- Assess the impact: Will the fix require downtime? Will it affect other users or systems?
- Identify potential effects: Could this change cause a different problem?
- Schedule if needed: Is this a change that should happen during a maintenance window?
- Document the plan.

This step prevents reactive fixes that cause outages in other areas. For example, restarting a switch to clear a MAC table issue might fix the original problem but cause a 60-second outage for 200 users. That outage needs to be planned and communicated.

### Step 5 — Implement the Solution or Escalate

Execute the plan.

Activities in Step 5:

- Implement the fix as planned.
- If the fix is beyond your authority, skill level, or scope — escalate to the appropriate team. Escalation is a valid outcome, not a failure.
- Change control: In enterprise environments, significant changes require a Change Request approved before implementation. Bypassing change control is a major professional and operational risk.

Escalation paths:

- Tier 1 help desk → Tier 2 network engineering → Tier 3 vendor support
- For hardware failures: vendor RMA process
- For carrier issues: carrier NOC (Network Operations Center)

### Step 6 — Verify Full System Functionality

After implementing the fix, verify that:

- The original problem is resolved.
- No new problems were introduced.
- All affected systems are functioning correctly.
- Verification is performed from the user's perspective, not just from the admin's console.

Activities in Step 6:

- Have the affected user confirm the problem is resolved.
- Test related systems that may have been affected by the change.
- Run the same diagnostic commands from Step 3 to confirm the expected results are now present.
- Check monitoring systems for any new alerts.

Step 6 is often skipped under time pressure — do not skip it. Incomplete verification is a leading cause of repeat incidents.

### Step 7 — Document Findings, Actions, and Outcomes

The final step is documentation.

Activities in Step 7:

- Record: What was the problem? What was the root cause? What was the solution? What was the impact?
- Update the knowledge base — if this was a novel issue, the resolution should help the next person who encounters it.
- File a change record if a configuration change was made.
- Conduct a post-incident review for major outages — what could be done to prevent recurrence?

Documentation benefits:

- Enables pattern recognition — repeated incidents may indicate a design flaw
- Reduces mean time to repair (MTTR) for future similar incidents
- Provides evidence for change management and compliance
- Protects the administrator — documented changes demonstrate professional practice

---

## Section 3: Applying the OSI Model to Troubleshooting

The OSI model provides a powerful framework for isolating the layer at which a problem exists.

### Bottom-Up Approach

Start at Layer 1 (Physical) and work up:

- Layer 1: Is the cable connected? Are the link lights on? Is the NIC recognized?
- Layer 2: Is the port in the correct VLAN? Is STP blocking the port? Is the MAC address in the table?
- Layer 3: Is the IP address correct? Is the default gateway correct? Is the route present in the routing table?
- Layer 4: Is the port open? Is a firewall blocking the transport layer connection?
- Layer 5–7: Is the DNS name resolving? Is the application service running? Is authentication succeeding?

Bottom-up is most useful when you have no idea where the problem is.

### Top-Down Approach

Start at Layer 7 (Application) and work down. Useful when the issue is clearly application-specific — for example, one application fails but others work.

### Divide and Conquer

Start in the middle — typically Layer 3. If ping succeeds (Layer 3 OK), focus up. If ping fails, work down from Layer 3.

Most experienced troubleshooters use divide and conquer by default, reserving the full bottom-up or top-down approach when divide and conquer does not yield a quick answer.

---

## Section 4: Common Network Troubleshooting Commands

These commands are directly tested on the Network+ exam.

### ping

Tests reachability at Layer 3. Sends ICMP Echo Requests and listens for replies.

- `ping 192.168.1.1` — ping a specific IP
- Successful ping = Layer 1-3 functional to that address
- Failed ping = problem somewhere in layers 1–3 to that destination

### traceroute / tracert

Maps the path packets take through the network. Shows each router hop and round-trip time.

- Linux/macOS: `traceroute`
- Windows: `tracert`
- Identifies where in the path packets are being dropped or delayed

### ipconfig / ifconfig / ip addr

Displays the local IP configuration.

- Windows: `ipconfig /all` — shows IP, subnet, gateway, DNS, MAC address, DHCP server
- Linux: `ip addr show` or legacy `ifconfig`
- Verify: correct IP, correct subnet mask, correct gateway, DNS server present

### nslookup / dig

DNS query tools. Test name resolution.

- `nslookup hostname` — resolves a hostname to IP
- If nslookup succeeds but ping fails by name, problem is likely ARP or firewall
- If nslookup fails, problem is DNS — check DNS server config and network path to DNS server

### netstat

Displays active network connections, listening ports, and routing tables.

- `netstat -an` — all connections with numeric addresses
- `netstat -r` — routing table (equivalent to `route print` on Windows)
- Useful for confirming a service is listening on the expected port

### arp

Displays and manages the ARP cache.

- `arp -a` — display ARP cache
- Incomplete ARP entries may indicate a Layer 2 problem or duplicate IP

---

## Summary of Part 1

Key points from Part 1:

- The CompTIA seven-step model: Identify the problem, Establish a theory, Test the theory, Plan of action, Implement or escalate, Verify full functionality, Document.
- Always identify before acting — "shotgun troubleshooting" wastes time and causes new problems.
- The OSI model provides a structured framework. Bottom-up, top-down, and divide-and-conquer are three approaches.
- Key commands: ping, traceroute/tracert, ipconfig/ip addr, nslookup, netstat, arp.

In Part 2, we will cover physical layer troubleshooting, cable testing, hardware failure symptoms, and the specific scenario question types common on the Network+ exam.
