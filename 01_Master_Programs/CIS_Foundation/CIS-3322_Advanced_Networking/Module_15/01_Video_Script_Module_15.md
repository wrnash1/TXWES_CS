# Video Script: Module 15 — Automation and Programmability

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Estimated Duration: 24 Minutes

---

## Segment 1: Introduction (0:00–1:30)

Welcome back to CIS-3322 Advanced Networking. I'm Professor Nash, and this is Module 15: Automation and Programmability. This domain accounts for approximately 15% of your CCNA 200-301 exam score and represents the future of how networks are built and operated.

By the end of this module you will be able to:

* Explain SDN concepts and the three-plane model
* Describe Cisco DNA Center and its role in intent-based networking
* Understand REST API concepts including HTTP methods and status codes
* Identify JSON and XML data structures
* Explain how Python and Ansible are used for network automation
* Describe NETCONF and RESTCONF protocols

Let's get started.

---

## Segment 2: Why Networks Need Automation (1:30–4:00)

For most of this course we have been configuring devices one at a time using CLI commands — SSH in, type commands, verify, repeat on the next device. That model worked when a network had 20 devices. Modern enterprise networks have thousands of devices across hundreds of sites.

Traditional CLI-based management has three fundamental problems at scale. First, it is slow — every change must be applied to each device individually. Second, it is error-prone — human typos cause outages. Third, it is inconsistent — two engineers making the same change often produce slightly different configurations that cause subtle, hard-to-diagnose problems.

Network automation addresses all three. A single intended state is defined once and applied consistently to every device simultaneously, verified programmatically, and documented automatically.

The CCNA exam does not expect you to write production automation code. It expects you to understand the architecture — what SDN is, how APIs work, what data formats are used, and what tools exist.

---

## Segment 3: Software-Defined Networking (4:00–8:30)

Traditional networking embeds both the control plane and the data plane inside every device. Each router runs its own routing protocol instance, makes its own forwarding decisions, and maintains its own state independently.

### The Three Planes

Every network device has three logical planes:

* The management plane handles out-of-band management traffic — SSH sessions, SNMP, syslog. This is how you configure the device.
* The control plane makes forwarding decisions — routing protocols, spanning tree, ARP. This is the device's "brain."
* The data plane forwards packets based on what the control plane decided. This runs at hardware speed in ASICs.

### SDN Architecture

Software-Defined Networking separates the control plane from the data plane. The control plane moves out of individual devices and into a centralized software controller. The data plane stays in the devices — hardware forwarding must happen at line rate.

The SDN controller has a global view of the entire network topology. It calculates optimal paths, enforces policies, and programs forwarding rules into all devices simultaneously from a single point.

### Northbound and Southbound APIs

The SDN controller communicates in two directions.

Southbound APIs connect the controller to the network devices below it. The controller sends forwarding rules and configuration instructions down to switches and routers. Common southbound protocols include OpenFlow, NETCONF, and RESTCONF.

Northbound APIs connect the controller to the applications and management tools above it. Business applications use northbound APIs to request network behavior. A security application might call the northbound API to quarantine a compromised host. Northbound APIs are typically REST APIs using JSON.

The memory aid is straightforward: the controller sits in the center. Applications are above it — that is north. Devices are below it — that is south.

### Cisco DNA Center

Cisco DNA Center — recently renamed Cisco Catalyst Center — is Cisco's enterprise SDN controller for campus and branch networks. It provides:

* An intent-based networking GUI where administrators define desired behavior in plain language
* A northbound REST API for integration with business applications and automation scripts
* Southbound communication to Cisco IOS-XE devices using RESTCONF and NETCONF
* Network assurance with continuous monitoring and anomaly detection

---

## Segment 4: REST APIs (8:30–13:00)

REST — Representational State Transfer — is the architectural style used by most modern network management APIs. REST APIs communicate over HTTP or HTTPS and follow a client-server model.

### HTTP Methods

There are four HTTP methods you must know for the CCNA exam. They map directly to the four CRUD operations — Create, Read, Update, Delete.

GET retrieves data without modifying anything. If you want to read the list of all network devices from DNA Center, you send a GET request. No data is changed on the server.

POST submits new data to create a resource. If you want to deploy a new network policy, you send a POST request with the policy definition in the request body.

PUT replaces an existing resource entirely. If you want to update a device's configuration, you send a PUT request with the complete new configuration.

DELETE removes a resource. If you want to remove a VLAN from the controller, you send a DELETE request.

Memorize: GET equals Read, POST equals Create, PUT equals Update, DELETE equals Delete.

### HTTP Status Codes

The server's response always includes a status code:

* 200 OK — the request succeeded; the response body contains the requested data
* 201 Created — a POST request succeeded and a new resource was created
* 204 No Content — the request succeeded but there is no response body (common for DELETE)
* 400 Bad Request — the client sent a malformed request
* 401 Unauthorized — authentication credentials are missing or invalid
* 403 Forbidden — authenticated but not authorized for this resource
* 404 Not Found — the requested resource does not exist
* 500 Internal Server Error — the server encountered an unexpected error

### Authentication

REST APIs use token-based authentication. You first POST credentials to an authentication endpoint and receive a token. All subsequent requests include that token in the Authorization header:

```text
Authorization: Bearer eyJhbGciOiJSUzI1NiJ9...
```

### Example API Request

A GET request to Cisco DNA Center to retrieve all network devices:

```text
GET https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device
Authorization: Bearer <token>
Content-Type: application/json
```

The response body contains a JSON array of device objects with fields like hostname, managementIpAddress, platformId, and softwareVersion.

---

## Segment 5: JSON and XML (13:00–16:30)

REST APIs exchange data in structured formats. The two formats you must recognize for the CCNA exam are JSON and XML.

### JSON

JSON — JavaScript Object Notation — uses curly braces for objects and square brackets for arrays. It is compact, human-readable, and the default format for most modern REST APIs.

```json
{
  "device": {
    "hostname": "R1",
    "ipAddress": "10.0.0.1",
    "platform": "ISR4451"
  }
}
```

Key JSON structures: an object is `{ "key": "value" }` with curly braces. An array is `[ "item1", "item2" ]` with square brackets. String values use double quotes. Numbers do not use quotes. Booleans are lowercase `true` or `false`.

### XML

XML — Extensible Markup Language — uses opening and closing tags to structure data. It is more verbose than JSON but is used by NETCONF.

```xml
<device>
  <hostname>R1</hostname>
  <ipAddress>10.0.0.1</ipAddress>
  <platform>ISR4451</platform>
</device>
```

The exam tests whether you can identify a valid JSON or XML structure from a code snippet. Look for curly braces and key-value pairs to identify JSON. Look for paired opening and closing tags to identify XML.

---

## Segment 6: Python and Ansible for Networking (16:30–20:30)

### Python Basics for Networking

Python is the dominant scripting language for network automation. The CCNA exam tests conceptual awareness, not Python programming proficiency. Key concepts:

* Variables store values: `hostname = "R1"`
* Lists store ordered collections: `devices = ["R1", "R2", "R3"]`
* Dictionaries store key-value pairs: `device = {"hostname": "R1", "ip": "10.0.0.1"}`
* Loops iterate over collections: `for device in devices:`
* The `requests` library sends HTTP requests to REST APIs
* The `netmiko` library establishes SSH connections and sends IOS commands programmatically

A simple Python script that retrieves device information from DNA Center would:

1. Import the `requests` library
2. POST credentials to the auth endpoint to get a token
3. GET the device list using the token in the Authorization header
4. Parse the JSON response and print the results

### NETCONF

NETCONF — Network Configuration Protocol — is a standards-based protocol defined in RFC 6241 for configuring and managing network devices. Key characteristics:

* Transport: SSH on port 830
* Data format: XML
* Data model: YANG — Yet Another Next Generation — defines the structure of configuration data
* Operations: `get`, `get-config`, `edit-config`, `commit`, `delete-config`

NETCONF provides transactional configuration changes. You can stage changes and commit them atomically — either all changes succeed or none are applied. This is safer than CLI-based changes.

### RESTCONF

RESTCONF — defined in RFC 8040 — provides a REST API interface over the same YANG data models used by NETCONF. Key characteristics:

* Transport: HTTPS
* Data format: JSON or XML
* Operations: standard HTTP methods (GET, POST, PUT, PATCH, DELETE)
* Supported on Cisco IOS-XE version 16.6 and later

RESTCONF is conceptually a REST wrapper around NETCONF data models. It exposes the same YANG-modeled configuration data through a familiar HTTP/JSON interface.

### Ansible for Network Automation

Ansible is the most widely used network automation tool for Cisco environments. Key characteristics:

* Agentless — no software needs to be installed on routers or switches
* Uses SSH or HTTPS APIs to communicate with devices
* Configuration is defined in YAML playbooks — human-readable text files
* Push model — the Ansible control node pushes configuration to managed devices
* Idempotent — running the same playbook multiple times produces the same result without making unnecessary changes

A simple Ansible playbook to configure a hostname on a Cisco router would define the target hosts, the connection type (network_cli), and the IOS commands to execute. Ansible's Cisco IOS collection handles the SSH connection and command execution automatically.

Contrast with Puppet and Chef: both require an agent installed on the managed device (Ansible does not) and use a pull model where devices check the server for configuration (Ansible pushes).

---

## Segment 7: Module Summary (20:30–24:00)

Let's bring this module together.

SDN separates the control plane from the data plane. The controller has a global network view. Southbound APIs (OpenFlow, NETCONF, RESTCONF) connect the controller to devices. Northbound APIs (REST/JSON) connect applications to the controller.

Cisco DNA Center is Cisco's SDN controller for enterprise networks. It uses intent-based networking and exposes a northbound REST API.

REST APIs use four HTTP methods: GET (Read), POST (Create), PUT (Update), DELETE (Delete). Status codes 2xx mean success; 4xx mean client error; 5xx mean server error.

JSON uses curly braces and key-value pairs. XML uses paired opening and closing tags. NETCONF uses XML over SSH port 830. RESTCONF uses JSON or XML over HTTPS.

Python uses the `requests` library for REST API calls and `netmiko` for SSH-based device configuration. Ansible is agentless, uses a push model, and writes playbooks in YAML. Puppet and Chef are agent-based and use a pull model.

Your lab this module gives you hands-on practice with Python REST API calls using Cisco DevNet sandbox environments. Module 16 is your capstone — comprehensive exam review, practice questions, and a multi-topology lab. See you there.

---

Script End — Module 15 | Approximate runtime: 24 minutes
