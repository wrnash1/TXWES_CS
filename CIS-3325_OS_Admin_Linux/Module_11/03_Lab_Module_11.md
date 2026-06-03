# Lab: Module 11 — Networking in Linux

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Lab Overview

**Estimated Time:** 60–75 minutes

**Environment:** Linux virtual machine (Rocky Linux 9 or Ubuntu 22.04 recommended). All tasks can be completed on a single VM with a standard NAT or bridged network adapter.

**Prerequisites:** Module 11 video lectures and reading guide completed. Root or sudo access to the VM.

**Objectives:**

- Inspect and configure network interfaces using the `ip` command
- Create a persistent static IP connection with `nmcli`
- Modify DNS resolution configuration
- Manage firewall rules with `firewall-cmd`
- Perform systematic network troubleshooting
- Configure an SSH client shortcut using `~/.ssh/config`

---

### Lab Environment Setup

Before beginning, verify your VM has network connectivity:

```bash
ping -c 2 8.8.8.8
```

If this fails, fix your VM network adapter settings before proceeding.

Record your current network configuration for reference:

```bash
ip addr show
ip route show
cat /etc/resolv.conf
```

Save this output to a text file — you will need it to restore settings if needed.

---

### Part 1: Exploring the ip Command

**Task 1.1 — Interface Inspection**

Run the following commands and record the output in your lab notebook:

```bash
ip link show
ip addr show
ip -4 addr show
ip -6 addr show
```

Answer these questions from the output:

- What is the name of your primary Ethernet interface?
- What is its IPv4 address and prefix length?
- What is its MTU (Maximum Transmission Unit)?
- Is the interface showing the `LOWER_UP` flag?

**Task 1.2 — Routing Table**

```bash
ip route show
```

- What is the default gateway IP address?
- What interface does the default route use?

Test gateway reachability:

```bash
ping -c 3 <your-gateway-ip>
```

**Task 1.3 — Adding and Removing a Temporary Address**

Add a secondary IP address to your Ethernet interface:

```bash
sudo ip addr add 192.168.200.1/24 dev <your-interface>
```

Verify it was added:

```bash
ip addr show <your-interface>
```

Now remove it:

```bash
sudo ip addr del 192.168.200.1/24 dev <your-interface>
```

Verify it was removed:

```bash
ip addr show <your-interface>
```

**Task 1.4 — ARP Cache**

```bash
ip neigh show
```

- How many ARP entries are currently cached?
- What MAC address corresponds to your gateway?

---

### Part 2: NetworkManager and nmcli

**Task 2.1 — Viewing Connections**

```bash
nmcli general status
nmcli connection show
nmcli device status
```

Record the name of your active connection profile.

**Task 2.2 — Creating a Static IP Connection**

Create a new connection profile with a static IP. Replace `<your-interface>` with your actual interface name, and choose an IP that does not conflict with your existing address:

```bash
sudo nmcli connection add \
  type ethernet \
  con-name "lab-static" \
  ifname <your-interface> \
  ipv4.addresses 192.168.1.200/24 \
  ipv4.gateway 192.168.1.1 \
  ipv4.dns "8.8.8.8 8.8.4.4" \
  ipv4.method manual
```

Verify the profile was created:

```bash
nmcli connection show lab-static
```

**Do NOT activate this connection** — it would replace your current IP. We are only verifying the profile creation.

**Task 2.3 — Modifying a Connection**

Modify the DNS server in the profile you just created:

```bash
sudo nmcli connection modify lab-static ipv4.dns "1.1.1.1 1.0.0.1"
nmcli connection show lab-static | grep ipv4.dns
```

Confirm the DNS was updated.

**Task 2.4 — Cleanup**

Delete the test profile:

```bash
sudo nmcli connection delete lab-static
nmcli connection show
```

Confirm the `lab-static` profile no longer appears.

---

### Part 3: DNS Configuration

**Task 3.1 — Inspect /etc/hosts**

```bash
cat /etc/hosts
```

Add a test entry:

```bash
echo "192.168.99.99  testserver.lab" | sudo tee -a /etc/hosts
```

Test resolution:

```bash
ping -c 2 testserver.lab
```

The ping should attempt to reach `192.168.99.99` (it will fail with "no route to host" but the name resolves — check with `ping -c 1 testserver.lab` and observe the IP in the output).

Remove the test entry when done:

```bash
sudo sed -i '/testserver.lab/d' /etc/hosts
```

**Task 3.2 — Inspect Resolution Order**

```bash
cat /etc/nsswitch.conf | grep "^hosts:"
```

- What is the resolution order on your system?

**Task 3.3 — DNS Query Testing**

```bash
dig google.com
dig google.com MX
dig @1.1.1.1 google.com
nslookup google.com
nslookup -type=MX google.com
```

- What IP addresses does `google.com` resolve to?
- What mail exchanger records are returned?
- Did the results differ when using `1.1.1.1` as the resolver?

---

### Part 4: Firewall Management

**Note:** This section uses `firewall-cmd`. If your system uses `ufw` (Ubuntu default), adapt the commands accordingly or install firewalld: `sudo apt install firewalld`.

**Task 4.1 — View Current Firewall State**

```bash
sudo firewall-cmd --state
sudo firewall-cmd --get-default-zone
sudo firewall-cmd --list-all
```

Record the current zone and all currently allowed services and ports.

**Task 4.2 — Add and Test a Port Rule**

Add port 8080/tcp to the public zone (runtime only — no `--permanent`):

```bash
sudo firewall-cmd --zone=public --add-port=8080/tcp
sudo firewall-cmd --list-ports
```

Confirm the port appears. Now check whether it appears in permanent configuration:

```bash
sudo firewall-cmd --zone=public --list-ports --permanent
```

It should NOT appear in permanent config.

Reload the firewall to clear the runtime rule:

```bash
sudo firewall-cmd --reload
sudo firewall-cmd --list-ports
```

The port should be gone.

Now add it permanently:

```bash
sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
sudo firewall-cmd --list-ports
```

Confirm it persists after reload.

**Task 4.3 — Add and Remove a Service**

```bash
sudo firewall-cmd --zone=public --add-service=http --permanent
sudo firewall-cmd --reload
sudo firewall-cmd --list-services
```

Remove it:

```bash
sudo firewall-cmd --zone=public --remove-service=http --permanent
sudo firewall-cmd --reload
sudo firewall-cmd --list-services
```

**Task 4.4 — Cleanup**

Remove the 8080/tcp port you added:

```bash
sudo firewall-cmd --zone=public --remove-port=8080/tcp --permanent
sudo firewall-cmd --reload
```

---

### Part 5: SSH Client Configuration

**Task 5.1 — Create the ~/.ssh Directory**

Ensure the directory exists with correct permissions:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
```

**Task 5.2 — Create an SSH Client Config**

Create a test configuration file:

```bash
cat > ~/.ssh/config << 'EOF'
Host labserver
    HostName 127.0.0.1
    User root
    Port 22
    ServerAliveInterval 60
    StrictHostKeyChecking yes
EOF
chmod 600 ~/.ssh/config
```

Verify the file:

```bash
cat ~/.ssh/config
ls -la ~/.ssh/config
```

The permissions must be `600` — SSH will refuse to use the config file if it is world-readable.

**Task 5.3 — Test the Alias (Optional)**

If SSH is running on localhost (it usually is), test the alias:

```bash
ssh labserver whoami
```

If SSH is not enabled, skip this step and note it in your lab report.

---

### Part 6: Network Troubleshooting

**Task 6.1 — Connectivity Test Chain**

Execute the full connectivity diagnostic sequence and record results at each step:

```bash
ping -c 2 127.0.0.1         # Step 1: Loopback
ping -c 2 <your-ip>         # Step 2: Own IP
ping -c 2 <gateway-ip>      # Step 3: Gateway
ping -c 2 8.8.8.8           # Step 4: External IP
ping -c 2 google.com        # Step 5: DNS resolution
```

Record: pass or fail at each step.

**Task 6.2 — Socket Statistics**

```bash
ss -tlnp
ss -ulnp
```

- What services are currently listening?
- On which ports?
- Which processes own those sockets?

**Task 6.3 — Route Tracing**

```bash
traceroute 8.8.8.8
```

- How many hops does the packet travel?
- Where does the trace exit your local network?

**Task 6.4 — Packet Capture**

Capture 10 ICMP packets while running a ping in a second terminal:

Terminal 1 (capture):

```bash
sudo tcpdump -i <your-interface> icmp -c 10
```

Terminal 2 (generate traffic):

```bash
ping -c 10 8.8.8.8
```

Observe the capture output. Record the source and destination IP addresses shown.

---

### Lab Submission Requirements

Submit a lab report in PDF format containing:

1. Answers to all questions marked above
2. Screenshot or copy/paste output for each task's verification step
3. A brief paragraph (3–5 sentences) describing the layered troubleshooting methodology and how you would apply it to diagnose a "can't reach the internet" complaint
4. List any tasks that failed or produced unexpected results, and explain why

---

### Grading Rubric

| Section | Points |
|---------|--------|
| Part 1: ip Command | 15 |
| Part 2: nmcli | 20 |
| Part 3: DNS Configuration | 15 |
| Part 4: Firewall Management | 20 |
| Part 5: SSH Config | 10 |
| Part 6: Troubleshooting | 15 |
| Written Analysis | 5 |
| **Total** | **100** |
