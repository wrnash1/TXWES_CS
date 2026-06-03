# Lab Activity: Module 15 — Automation and Programmability

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Lab Overview

In this lab you will use Python and the Cisco DevNet Always-On DNA Center sandbox to make real REST API calls, parse JSON responses, and automate a configuration task. You will also write a basic Ansible playbook structure and analyze JSON and XML data formats. No physical hardware is required — all work uses the free Cisco DevNet sandbox environment and a local Python installation.

**Estimated Time:** 80 minutes

**Prerequisites:**

* Python 3.8 or later installed (python.org)
* `requests` library installed: `pip install requests`
* Web browser for DevNet sandbox access

**DevNet Sandbox:** developer.cisco.com/site/sandbox — use the Always-On DNA Center sandbox (no reservation required)

---

## Part 1: REST API Fundamentals — HTTP Methods and Status Codes

### Step 1.1 — Review the HTTP Method Table

Before writing any code, complete the following table from memory. Then verify your answers using the reading guide.

| HTTP Method | CRUD Operation | Description |
|---|---|---|
| GET | | |
| POST | | |
| PUT | | |
| DELETE | | |

### Step 1.2 — Status Code Identification Exercise

Match each scenario to the correct HTTP status code:

1. A GET request successfully retrieves a list of network devices. Status code: ______
2. A POST request creates a new network policy. Status code: ______
3. A GET request uses an expired authentication token. Status code: ______
4. A DELETE request removes a VLAN that does not exist. Status code: ______
5. The API server crashes while processing a request. Status code: ______

Answers: 200, 201, 401, 404, 500

---

## Part 2: JSON and XML Format Analysis

### Step 2.1 — Identify the Data Format

Examine each code block and identify whether it is JSON or XML. Explain your reasoning.

Code Block A:

```json
{
  "response": [
    {
      "hostname": "asr1001-x.abc.inc",
      "managementIpAddress": "10.10.22.253",
      "platformId": "ASR1001-X",
      "reachabilityStatus": "Reachable"
    }
  ]
}
```

Format: ______ | Reason: ______

Code Block B:

```xml
<device>
  <hostname>asr1001-x.abc.inc</hostname>
  <managementIpAddress>10.10.22.253</managementIpAddress>
  <platformId>ASR1001-X</platformId>
  <reachabilityStatus>Reachable</reachabilityStatus>
</device>
```

Format: ______ | Reason: ______

### Step 2.2 — JSON Structure Analysis

Using Code Block A above, answer the following:

1. What is the data type of the outer `response` value? (string / number / object / array) ______
2. What is the value of `platformId` for the first device? ______
3. How many device objects are in the response array? ______
4. Write the Python expression to access the hostname of the first device, given the response is stored in a variable named `data`: ______

---

## Part 3: Python REST API Lab — DNA Center Sandbox

### Step 3.1 — Authenticate to DNA Center

Create a file named `dnac_lab.py` and enter the following code:

```python
import requests
import json
import urllib3

# Suppress SSL warnings for sandbox (not for production)
urllib3.disable_warnings()

# DNA Center Always-On Sandbox credentials
DNAC_URL = "https://sandboxdnac.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

def get_auth_token():
    """Authenticate to DNA Center and return a token."""
    url = f"{DNAC_URL}/dna/system/api/v1/auth/token"
    response = requests.post(
        url,
        auth=(USERNAME, PASSWORD),
        verify=False
    )
    if response.status_code == 200:
        token = response.json()["Token"]
        print(f"Authentication successful. Token: {token[:20]}...")
        return token
    else:
        print(f"Authentication failed. Status: {response.status_code}")
        return None

if __name__ == "__main__":
    token = get_auth_token()
```

Run the script: `python dnac_lab.py`

Record the first 20 characters of the returned token: ______

### Step 3.2 — Retrieve Network Device List

Add the following function to `dnac_lab.py`:

```python
def get_network_devices(token):
    """Retrieve all network devices from DNA Center."""
    url = f"{DNAC_URL}/dna/intent/api/v1/network-device"
    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        devices = response.json()["response"]
        print(f"\nFound {len(devices)} network devices:")
        print("-" * 50)
        for device in devices:
            hostname = device.get("hostname", "N/A")
            ip = device.get("managementIpAddress", "N/A")
            platform = device.get("platformId", "N/A")
            status = device.get("reachabilityStatus", "N/A")
            print(f"  Hostname: {hostname}")
            print(f"  IP:       {ip}")
            print(f"  Platform: {platform}")
            print(f"  Status:   {status}")
            print()
        return devices
    else:
        print(f"Failed to retrieve devices. Status: {response.status_code}")
        return []
```

Update the `__main__` block:

```python
if __name__ == "__main__":
    token = get_auth_token()
    if token:
        devices = get_network_devices(token)
```

Run the updated script and record:

* Total number of devices returned: ______
* Hostname of the first device: ______
* Management IP of the first device: ______

### Step 3.3 — Filter Reachable Devices

Add a filtering function:

```python
def filter_reachable_devices(devices):
    """Return only devices with Reachable status."""
    reachable = [d for d in devices if d.get("reachabilityStatus") == "Reachable"]
    print(f"\nReachable devices: {len(reachable)} of {len(devices)} total")
    for device in reachable:
        print(f"  {device['hostname']} ({device['managementIpAddress']})")
    return reachable
```

Call this function in `__main__` after `get_network_devices()`.

Record: How many devices are in Reachable status? ______

---

## Part 4: Ansible Playbook Structure

### Step 4.1 — Analyze a Playbook

Review the following Ansible playbook and answer the questions below:

```yaml
---
- name: Configure NTP on all Cisco routers
  hosts: routers
  gather_facts: false
  connection: network_cli

  vars:
    ntp_server: "10.0.0.5"

  tasks:
    - name: Configure NTP server
      cisco.ios.ios_ntp_global:
        config:
          peers:
            - peer: "{{ ntp_server }}"
        state: merged

    - name: Verify NTP configuration
      cisco.ios.ios_command:
        commands:
          - show ntp status
      register: ntp_output

    - name: Display NTP status
      debug:
        var: ntp_output.stdout_lines
```

Answer the following questions:

1. What does `hosts: routers` specify? ______
2. What does `gather_facts: false` mean for a network device? ______
3. What is the purpose of `connection: network_cli`? ______
4. How many tasks does this playbook contain? ______
5. What is the `register` keyword doing in the second task? ______

### Step 4.2 — Ansible vs. Puppet vs. Chef Comparison

Complete the following table:

| Feature | Ansible | Puppet | Chef |
|---|---|---|---|
| Agent required on device | | | |
| Execution model | | | |
| Configuration language | | | |
| Best suited for network devices | | | |

---

## Part 5: SDN Architecture Diagram

### Step 5.1 — Draw the SDN Model

On paper or in a drawing tool, draw the three-layer SDN architecture including:

* Application plane with two example applications
* Control plane with the SDN controller labeled
* Data plane with three network devices
* Northbound API arrow with label and protocol example
* Southbound API arrow with label and protocol examples (at least two)

Take a photo or export the diagram and attach it to your submission.

### Step 5.2 — Identify API Direction

For each scenario, identify whether it uses a northbound or southbound API:

1. A security application calls the DNA Center API to quarantine a host. Direction: ______
2. DNA Center sends NETCONF commands to configure a Cisco IOS-XE switch. Direction: ______
3. A Python script uses the DNA Center REST API to retrieve device inventory. Direction: ______
4. The SDN controller uses OpenFlow to program flow tables in a switch. Direction: ______

---

## Part 6: Lab Cleanup and Documentation

### Step 6.1 — Save Your Script

Save your completed `dnac_lab.py` file. Add a comment block at the top:

```python
# CIS-3322 Advanced Networking
# Module 15 Lab — REST API with Cisco DNA Center
# Student: [Your Name]
# Date: [Today's Date]
# Sandbox: Cisco DevNet Always-On DNA Center
```

### Step 6.2 — Reflection Questions

Answer in 2–3 sentences each:

1. How does using a REST API to retrieve device information differ from using SSH and CLI commands?
2. What is one advantage of Ansible's agentless architecture for a network of 500 Cisco routers?
3. Why is NETCONF preferred over CLI for large-scale automated configuration changes?

---

## Lab Rubric

| Task | Points | Criteria |
|---|---|---|
| Part 1: HTTP methods and status codes | 10 | Table completed correctly; status codes matched |
| Part 2: JSON/XML identification and analysis | 15 | Format identified with correct reasoning; Python access expression correct |
| Part 3: Python script — authentication | 20 | Script runs; token returned; token characters recorded |
| Part 3: Python script — device retrieval | 20 | Devices listed correctly; count and hostname recorded |
| Part 4: Ansible analysis | 15 | All five questions answered correctly; comparison table complete |
| Part 5: SDN diagram | 10 | All components labeled; API directions correct |
| Part 6: Reflection questions | 10 | Three reflections written; technically accurate |
| **Total** | **100** | |

---

## Submission Instructions

Submit through the course LMS:

1. Your completed `dnac_lab.py` Python file
2. A screenshot of the script output showing the device list
3. Your SDN architecture diagram (photo or exported image)
4. The completed worksheet sections (Parts 1, 2, 4, 5, 6) as a PDF or Word document
