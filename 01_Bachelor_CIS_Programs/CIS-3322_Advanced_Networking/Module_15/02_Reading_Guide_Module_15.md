# Reading Guide: Module 15 — Automation and Programmability

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3322 &BULL; ADVANCED NETWORKING & INFRASTRUCTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Overview

This reading guide supports Module 15: Automation and Programmability. This CCNA 200-301 domain (6.0) accounts for 15% of exam questions and is frequently underprepared because it differs from the traditional CLI-based topics covered earlier in the course. This guide covers every testable topic: SDN architecture, northbound/southbound APIs, REST API methods and status codes, JSON and XML, NETCONF and RESTCONF, Python concepts, Ansible vs. Puppet vs. Chef, and Cisco DNA Center.

---

## Section 1: Traditional vs. SDN Architecture

### The Traditional Networking Model

In traditional networking, intelligence is distributed. Every device independently runs:

* Control plane functions — routing protocols (OSPF, EIGRP, BGP), spanning tree, ARP processing
* Data plane functions — hardware packet forwarding based on FIB/CAM table lookups
* Management plane functions — SSH, SNMP, syslog for device access and monitoring

Changes require direct access to each device. There is no global network view from any single point.

### The SDN Model

SDN centralizes the control plane in a software controller while keeping the data plane in hardware devices.

```text
Application Plane
  (monitoring, orchestration, security, business apps)
          |
          |  Northbound API (REST over HTTPS, JSON)
          v
Control Plane
  (SDN Controller — Cisco DNA Center / Catalyst Center)
          |
          |  Southbound API (OpenFlow, NETCONF, RESTCONF)
          v
Data Plane
  (routers, switches — hardware packet forwarding at line rate)
```

### Plane Comparison Table

| Plane | Function | Location in Traditional | Location in SDN |
|---|---|---|---|
| Management | Device access, monitoring | Each device | Each device |
| Control | Routing decisions, STP | Each device | Centralized controller |
| Data | Packet forwarding | Each device (hardware) | Each device (hardware) |

---

## Section 2: API Directions Reference

### Northbound vs. Southbound

| Attribute | Northbound API | Southbound API |
|---|---|---|
| Direction | Applications → Controller | Controller → Network devices |
| Purpose | Applications request network services | Controller programs forwarding rules |
| Common protocols | REST (HTTPS/JSON), Python requests | OpenFlow, NETCONF, RESTCONF |
| Who calls it | Automation scripts, business apps | SDN controller |

The controller is the center point. North = above the controller (applications). South = below the controller (devices).

### East-West APIs

East-west APIs enable communication between controllers at the same architectural layer — for example, between a WAN controller and a campus controller. This appears as a distractor on the CCNA exam. Know what it is; do not confuse it with northbound or southbound.

---

## Section 3: REST API Reference

### REST Principles

REST (Representational State Transfer) is a stateless client-server architectural style. Each request contains all information needed to process it — no server-side session state. REST APIs operate over HTTP or HTTPS and identify resources by URL.

### HTTP Method to CRUD Mapping

| HTTP Method | CRUD Operation | Description | Example use |
|---|---|---|---|
| GET | Read | Retrieve a resource; no side effects | Read device list, interface status |
| POST | Create | Submit data to create a new resource | Create a new network policy |
| PUT | Update/Replace | Replace an existing resource completely | Update device configuration |
| DELETE | Delete | Remove a resource | Remove a VLAN |

Note: PATCH performs a partial update and is not emphasized on the CCNA exam.

### HTTP Status Code Reference

| Code | Name | Meaning | Triggered by |
|---|---|---|---|
| 200 | OK | Request succeeded; body contains data | Successful GET or PUT |
| 201 | Created | Resource successfully created | Successful POST |
| 204 | No Content | Succeeded; no response body | Successful DELETE |
| 400 | Bad Request | Malformed request syntax | Missing required field |
| 401 | Unauthorized | Missing or invalid credentials | No token provided |
| 403 | Forbidden | Authenticated but not authorized | Insufficient privilege |
| 404 | Not Found | Resource does not exist | Wrong URL or ID |
| 500 | Internal Server Error | Server-side failure | API bug or backend error |

### REST API Request Structure

Every REST API request has four components:

* HTTP Method — specifies the operation (GET, POST, PUT, DELETE)
* URL (Endpoint) — identifies the resource being accessed
* Headers — metadata including `Content-Type: application/json` and `Authorization: Bearer <token>`
* Body — data payload used with POST and PUT; absent for GET and DELETE

### DNA Center API Authentication Flow

```text
Step 1: POST /dna/system/api/v1/auth/token
        Body: Basic Auth (username:password base64 encoded)
        Response: { "Token": "eyJhbGciOiJSUzI1NiJ9..." }

Step 2: GET /dna/intent/api/v1/network-device
        Header: X-Auth-Token: eyJhbGciOiJSUzI1NiJ9...
        Response: JSON array of device objects
```

---

## Section 4: Data Format Reference

### JSON

JSON (JavaScript Object Notation) is the primary data format for modern REST APIs. It is human-readable and compact.

#### JSON Syntax Rules

| Element | Syntax | Example |
|---|---|---|
| Object | Curly braces containing key-value pairs | `{ "hostname": "R1" }` |
| Array | Square brackets containing ordered values | `[ "R1", "R2", "R3" ]` |
| String | Value in double quotes | `"10.0.0.1"` |
| Number | Value without quotes | `42` or `3.14` |
| Boolean | Lowercase true or false | `true` |
| Null | Lowercase null | `null` |
| Nested object | Object as a value | `{ "device": { "ip": "10.0.0.1" } }` |

#### JSON Example

```json
{
  "networkDevices": [
    {
      "hostname": "SW1",
      "managementIpAddress": "10.0.0.10",
      "platformId": "WS-C3850",
      "reachabilityStatus": "Reachable"
    },
    {
      "hostname": "R1",
      "managementIpAddress": "10.0.0.1",
      "platformId": "ISR4451",
      "reachabilityStatus": "Reachable"
    }
  ]
}
```

### XML

XML (Extensible Markup Language) uses paired tags to structure hierarchical data. Used by NETCONF and some legacy REST APIs.

#### XML Example

```xml
<networkDevices>
  <device>
    <hostname>SW1</hostname>
    <managementIpAddress>10.0.0.10</managementIpAddress>
    <platformId>WS-C3850</platformId>
  </device>
</networkDevices>
```

### JSON vs. XML for the Exam

| Feature | JSON | XML |
|---|---|---|
| Delimiter | Curly braces `{}`, square brackets `[]` | Opening/closing tags `<tag></tag>` |
| Verbosity | Compact | Verbose |
| Common use | REST APIs | NETCONF, SOAP |
| Array syntax | Native `[]` | Repeated elements (no native array) |
| Comment support | None | Yes (`<!-- comment -->`) |

---

## Section 5: NETCONF and RESTCONF

### NETCONF

NETCONF (Network Configuration Protocol) is defined in RFC 6241. It provides transactional, model-driven configuration management.

| Attribute | Value |
|---|---|
| Transport | SSH — specifically port 830 |
| Data format | XML |
| Data model | YANG (Yet Another Next Generation) |
| Key feature | Transactional commits — all-or-nothing configuration changes |
| Supported by | Cisco IOS-XE, IOS-XR, Juniper, and YANG-capable platforms |

#### NETCONF Operations Reference

| Operation | Purpose |
|---|---|
| `get` | Retrieve running state and configuration |
| `get-config` | Retrieve configuration from a specific datastore |
| `edit-config` | Modify the configuration in a datastore |
| `commit` | Apply candidate configuration to running |
| `delete-config` | Delete an entire configuration datastore |
| `lock` / `unlock` | Lock a datastore to prevent concurrent changes |

### RESTCONF

RESTCONF (RFC 8040) is a REST API wrapper over NETCONF YANG data models.

| Attribute | Value |
|---|---|
| Transport | HTTPS |
| Data format | JSON or XML |
| Operations | HTTP methods (GET, POST, PUT, PATCH, DELETE) |
| Data model | YANG (same models as NETCONF) |
| Supported on | Cisco IOS-XE 16.6+ |

RESTCONF provides the same device configuration capability as NETCONF but through a familiar REST/HTTP interface. It is easier to use from Python scripts than raw NETCONF XML.

---

## Section 6: Configuration Management Tools

### Ansible

Ansible is the dominant tool for network device automation. It is maintained by Red Hat and has a large Cisco-specific collection (cisco.ios).

| Feature | Value |
|---|---|
| Agent required | No — agentless |
| Communication | SSH (network devices), HTTPS (APIs) |
| Configuration language | YAML (playbooks and inventory) |
| Execution model | Push — control node pushes to devices |
| Idempotency | Yes |
| Network support | Cisco IOS, NX-OS, IOS-XE, IOS-XR, Juniper, Arista |

#### Sample Ansible Playbook Structure

```yaml
---
- name: Configure hostname on all routers
  hosts: routers
  gather_facts: false
  connection: network_cli

  tasks:
    - name: Set hostname
      cisco.ios.ios_hostname:
        config:
          hostname: "{{ inventory_hostname }}"
        state: merged
```

### Puppet

| Feature | Value |
|---|---|
| Agent required | Yes — Puppet agent on managed nodes |
| Communication | HTTPS between agent and Puppet server |
| Configuration language | Puppet DSL (declarative) |
| Execution model | Pull — agents poll server for configuration |
| Network device support | Limited native support |

### Chef

| Feature | Value |
|---|---|
| Agent required | Yes — Chef client on managed nodes |
| Configuration language | Ruby (Cookbooks and Recipes) |
| Execution model | Pull — clients check in with Chef server |
| Network device support | Limited native support |

### Three-Tool Comparison Table

| Feature | Ansible | Puppet | Chef |
|---|---|---|---|
| Agent required | No | Yes | Yes |
| Model | Push | Pull | Pull |
| Language | YAML | Puppet DSL | Ruby |
| Network device focus | Strong | Limited | Limited |
| Idempotent | Yes | Yes | Yes |

---

## Section 7: Python Concepts for Networking

### Key Python Libraries

* `requests` — sends HTTP requests; used for REST API calls to DNA Center, WLC APIs
* `netmiko` — establishes SSH connections to network devices; sends commands and parses output
* `nornir` — network automation framework; manages device inventories and concurrent task execution
* `napalm` — network abstraction library; provides a vendor-neutral API over CLI/NETCONF

### Python Code Pattern for REST API Call

```python
import requests

# Step 1: Authenticate and get token
auth_url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
response = requests.post(auth_url, auth=("devnetuser", "Cisco123!"), verify=False)
token = response.json()["Token"]

# Step 2: Use token to retrieve device list
headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
devices_url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
devices = requests.get(devices_url, headers=headers, verify=False)

# Step 3: Print hostnames
for device in devices.json()["response"]:
    print(device["hostname"])
```

### Python Data Types Relevant to Networking

| Type | Description | Example |
|---|---|---|
| String | Text data | `"10.0.0.1"` |
| Integer | Whole number | `24` |
| List | Ordered, mutable collection | `["R1", "R2"]` |
| Dictionary | Key-value pairs | `{"hostname": "R1", "ip": "10.0.0.1"}` |
| Boolean | True or False | `True` |

---

## Section 8: CCNA Exam Tips — Module 15

* Southbound APIs connect the controller to network devices (below the controller). Northbound APIs connect applications to the controller (above). Always from the controller's perspective.
* GET = Read, POST = Create, PUT = Update, DELETE = Delete. All four appear on the exam.
* JSON uses curly braces `{}` for objects and square brackets `[]` for arrays. XML uses paired tags. NETCONF uses XML. REST APIs typically use JSON.
* Ansible is agentless and uses a push model. Puppet and Chef are agent-based and use a pull model. This is the most tested distinction.
* NETCONF runs over SSH on port 830 and uses XML. RESTCONF runs over HTTPS and uses JSON or XML.
* 200 OK = success (GET/PUT). 201 Created = new resource (POST). 404 = not found. 401 = not authenticated.
* OpenFlow is always a southbound protocol. It programs flow tables from the controller to switches.

---

## Study Checkpoint Questions

1. Draw the three-plane SDN model from memory and label all APIs.
2. A script sends a POST request to create a network policy. The server responds with status 201. What does this mean?
3. What is the key difference between NETCONF and RESTCONF?
4. Which configuration management tool requires no software installed on the managed network device?
5. A code block shows `{ "hostname": "R1" }`. What data format is this and how do you know?
6. What Python library is used to send HTTP requests to a REST API?

---

## Supplemental Resources

The following open educational resources extend automation and programmability concepts to CCNA exam depth. All resources are freely available.

1. **Cisco Networking Academy — CCNA: Enterprise Networking, Security, and Automation, Chapters 12–13 (Network Automation and Programmability)** (skillsforall.com): Free chapters covering SDN architecture, REST APIs and HTTP methods, JSON and XML data formats, NETCONF and RESTCONF, Python with `requests`, and Ansible playbook basics — exactly the content tested in the CCNA Automation domain.

2. **Jeremy's IT Lab — Automation and Programmability (Days 61–66)** (youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ): Six video lessons covering SDN planes and APIs, OpenFlow, Cisco DNA Center, REST API operations, JSON/YAML/XML data formats, Ansible vs. Puppet vs. Chef comparison, and NETCONF/RESTCONF. Includes exam-style scenario walkthroughs for the full CCNA Automation domain.

3. **Cisco DevNet Learning Labs** (developer.cisco.com/learning/labs): Cisco's free hands-on learning platform with interactive labs using the DNA Center Always-On sandbox. Labs cover REST API authentication, Python `requests` scripting, NETCONF with `ncclient`, and Ansible network automation — all freely accessible without a Cisco account.

4. **Cisco Networking Academy — Cisco DevNet Associate Fundamentals** (skillsforall.com): Free course covering REST API concepts, HTTP methods, JSON data structures, Python for networking, and introduction to YANG models. Overlaps with CCNA automation content and provides a deeper programmability foundation.

5. **Ansible for Network Automation Documentation** (docs.ansible.com/ansible/latest/network): Ansible's official network automation documentation covering cisco.ios collection modules, playbook structure for network devices, connection types (network_cli, netconf, httpapi), and idempotency behavior — free reference for understanding the Ansible concepts tested on the CCNA exam.
