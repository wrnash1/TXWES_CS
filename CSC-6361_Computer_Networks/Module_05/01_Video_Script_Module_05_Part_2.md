# Video Script: Module 05 – QoS, High Availability & Network Automation
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 2 of 2 | Estimated Duration: 15–18 minutes
## Week 5: November 16–22, 2026 | Due: Sunday, November 22, 2026
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide
[SHOW SLIDE: "CSC-6361 — Module 05 Part 2: Network Automation — Python, Ansible & APIs | Texas Wesleyan University"]

---

### Section 1: Why Network Automation?

[00:00 – 02:30]
[SHOW SLIDE: Side-by-side: manual CLI changes on 50 switches vs Ansible playbook running on all 50 simultaneously]

Network automation is no longer optional for enterprise network engineers. CCNP ENCOR includes automation topics, and every major employer expects engineers to understand scripting, APIs, and infrastructure-as-code tools.

**The Core Problem:**
A large enterprise might have 500 network devices. If you need to change the NTP server on every device, manual CLI on each one takes days. A typo on any single device creates a configuration drift problem. Automation makes changes:
- **Fast:** Execute on all 500 devices in seconds.
- **Consistent:** Same configuration is applied identically everywhere.
- **Auditable:** All changes are in version-controlled code.
- **Repeatable:** Run the same playbook in dev, staging, and production.

---

### Section 2: Python for Network Automation

[02:30 – 07:00]
[SHOW SLIDE: Python code connecting to a router via Netmiko]

**Netmiko — SSH-based Network Automation (Free, Open Source):**
Netmiko is the most widely used Python library for automating Cisco CLI devices via SSH. It handles SSH connection management, device type detection, and command output parsing.

```python
from netmiko import ConnectHandler

# Define the device
device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "Admin@Secure1",
    "secret": "enable_secret",
}

# Connect and run commands
with ConnectHandler(**device) as net_connect:
    net_connect.enable()
    output = net_connect.send_command("show ip route")
    print(output)
    
    # Send configuration commands
    config_commands = [
        "ntp server 10.10.10.100",
        "logging 10.10.10.200",
    ]
    net_connect.send_config_set(config_commands)
    print("Configuration applied successfully")
```

**Scaling with a Device List:**
```python
from netmiko import ConnectHandler

devices = [
    {"device_type": "cisco_ios", "host": "10.0.1.1", "username": "admin", "password": "Admin@Secure1"},
    {"device_type": "cisco_ios", "host": "10.0.1.2", "username": "admin", "password": "Admin@Secure1"},
    {"device_type": "cisco_ios", "host": "10.0.1.3", "username": "admin", "password": "Admin@Secure1"},
]

config_commands = ["ntp server 10.10.10.100", "logging 10.10.10.200"]

for device in devices:
    with ConnectHandler(**device) as conn:
        conn.send_config_set(config_commands)
        print(f"Configured {device['host']}")
```

This script pushes the same NTP and logging configuration to 3 routers simultaneously — and would scale to 500 with the same code.

**TextFSM and ntc-templates — Parsing CLI Output:**
`show ip route` returns unstructured text. TextFSM and the NTC templates library convert CLI output into structured Python data (lists and dictionaries):
```python
output = net_connect.send_command("show ip bgp summary", use_textfsm=True)
# Returns a list of dicts: [{"neighbor": "10.1.1.1", "as": "65001", "updown": "2d13h", ...}]
for neighbor in output:
    print(f"BGP Neighbor: {neighbor['neighbor']} | State: {neighbor['state']}")
```

---

### Section 3: Ansible for Network Automation

[07:00 – 11:00]
[SHOW DIAGRAM: Ansible architecture — Control Node running playbook → Managed devices (routers, switches) via SSH/API]

[Alt-text: A diagram showing a laptop labeled "Ansible Control Node." Arrows from the control node go to three network devices: "Router-1," "Switch-A," and "Firewall-1." Each arrow is labeled "SSH / NETCONF." The laptop has a folder icon labeled "Playbook.yml" and another labeled "Inventory.ini."]

Ansible is an agentless automation framework. No software needs to be installed on the network devices — Ansible connects via SSH (or API) from a control node and pushes changes.

**Ansible Inventory File (hosts.ini):**
```ini
[routers]
192.168.1.1  ansible_user=admin  ansible_password=Admin@Secure1  ansible_network_os=ios
192.168.1.2  ansible_user=admin  ansible_password=Admin@Secure1  ansible_network_os=ios

[switches]
192.168.2.1  ansible_user=admin  ansible_password=Admin@Secure1  ansible_network_os=ios
```

**Ansible Playbook — Configure NTP on All Devices:**
```yaml
---
- name: Configure NTP on All Network Devices
  hosts: routers,switches
  gather_facts: no
  connection: network_cli

  tasks:
    - name: Set NTP Server
      cisco.ios.ios_ntp_global:
        config:
          servers:
            - server: "10.10.10.100"
              prefer: true
        state: merged

    - name: Set logging host
      cisco.ios.ios_logging_global:
        config:
          hosts:
            - hostname: "10.10.10.200"
        state: merged

    - name: Verify NTP status
      cisco.ios.ios_command:
        commands:
          - show ntp status
      register: ntp_output

    - name: Display NTP output
      debug:
        var: ntp_output.stdout_lines
```

Run this playbook against all routers and switches with:
```
ansible-playbook -i hosts.ini configure_ntp.yml
```

> **Graduate Note:** Ansible is **idempotent** — running the same playbook multiple times produces the same result without duplicate changes. If the NTP server is already configured, Ansible confirms the state is correct and takes no action. This is a key difference from simple shell scripts.

**Ansible Roles:**
For complex network configurations, Ansible supports **roles** — a structured directory layout that organizes tasks, variables, templates, and handlers into reusable modules. A `baseline_hardening` role could apply the full CIS IOS benchmark across all devices by running `ansible-playbook site.yml`.

---

### Section 4: REST APIs and NETCONF/YANG

[11:00 – 14:00]
[SHOW DIAGRAM: REST API call — GET /restconf/data/ietf-interfaces:interfaces → JSON response]

**REST APIs on Modern Cisco Devices:**
IOS-XE (17.x+) supports **RESTCONF**, a REST API that exposes network configuration as JSON or XML resources. This allows automation tools, scripts, and orchestration platforms to configure network devices via HTTP — no CLI needed.

```python
import requests
import json

# GET — retrieve all interfaces
url = "https://192.168.1.1/restconf/data/ietf-interfaces:interfaces"
headers = {"Content-Type": "application/yang-data+json", "Accept": "application/yang-data+json"}
auth = ("admin", "Admin@Secure1")

response = requests.get(url, headers=headers, auth=auth, verify=False)
interfaces = response.json()
print(json.dumps(interfaces, indent=2))

# PATCH — configure an interface description
patch_url = "https://192.168.1.1/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"
payload = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet1",
        "description": "WAN-Link-to-ISP"
    }
}
requests.patch(patch_url, headers=headers, auth=auth, json=payload, verify=False)
```

**NETCONF and YANG:**
NETCONF is an XML-based protocol for network configuration management. **YANG** (Yet Another Next Generation) defines the data models — the structured schema of network configuration data. Together, NETCONF/YANG provide a vendor-neutral, structured approach to network configuration that is the foundation of modern network automation.

```
! Enable NETCONF on Cisco IOS-XE
netconf-yang
restconf
```

---

### Section 5: Module 05 Lab Preview

[14:00 – 15:30]
[SHOW SLIDE: Module 05 Lab — QoS + HSRP configuration]

The Module 05 lab covers two components:
1. **QoS:** Configure a DiffServ QoS policy using MQC (LLQ for voice, CBWFQ for data). Apply it to the WAN interface of a router. Verify traffic classification.
2. **HSRP:** Configure HSRP on two distribution switches with preemption. Verify Active/Standby state. Simulate Active router failure and confirm standby takes over.

The Python automation exercises are provided as code walkthroughs in the Reading Guide (Packet Tracer does not support Python/NETCONF).

**Assignments due: Sunday, November 22, 2026 at 11:59 PM CST**

---
*End of Part 2 — Module 05*
