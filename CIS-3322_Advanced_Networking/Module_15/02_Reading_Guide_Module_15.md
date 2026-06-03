# Reading Guide: Module 15 — Automation and Programmability

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
