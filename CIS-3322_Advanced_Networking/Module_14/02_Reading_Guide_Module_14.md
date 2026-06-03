# Reading Guide: Module 14 - Network Automation and REST APIs

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

---

## Overview

Network automation and programmability is CCNA 200-301 Domain 6, representing 15% of the exam. This domain is frequently underprepared because it differs from the traditional CLI configuration topics covered elsewhere in the course. This guide covers all testable automation topics: SDN architecture, northbound and southbound APIs, REST API methods, JSON and XML data formats, NETCONF and RESTCONF, configuration management tools, and Cisco DNA Center concepts.

---

## 1. Traditional Networking vs Software-Defined Networking

### The Traditional Model

In traditional networking, each device has:

- A control plane — makes forwarding decisions (routing protocols, spanning tree, MAC learning)
- A data plane — forwards packets based on those decisions at hardware speed

Both planes are integrated inside every device. Changes require CLI access to individual devices. There is no centralized view of the network.

### The SDN Model

Software-Defined Networking separates the control plane from the data plane:

| Plane | Location in SDN | Function |
|-------|-----------------|----------|
| Application plane | Business applications, monitoring tools | Defines desired network behavior |
| Control plane | SDN Controller (centralized software) | Makes forwarding decisions for the entire network |
| Data plane | Network devices (switches, routers) | Forwards packets at hardware speed |

The SDN controller has a global network topology view. It programs forwarding behavior into all devices from a single point using southbound APIs.

### SDN Planes of Operation

```text
Application Plane (monitoring apps, orchestration, security)
          |
          |  Northbound API (REST/JSON)
          v
Control Plane (SDN Controller — Cisco DNA Center)
          |
          |  Southbound API (OpenFlow, NETCONF, RESTCONF)
          v
Data Plane (routers, switches — hardware packet forwarding)
```

---

## 2. API Direction Reference

### Northbound vs Southbound

| API Direction | Direction from controller | Communication | Common Protocols |
|---------------|--------------------------|---------------|------------------|
| Northbound | Controller to Applications | Applications request network services | REST over HTTPS (JSON or XML) |
| Southbound | Controller to Network devices | Controller programs forwarding rules | OpenFlow, NETCONF, RESTCONF |

Memory aid: The controller is in the center. Applications are above it (north). Devices are below it (south).

### East-West APIs

East-west APIs enable communication between controllers at the same layer — for example, between a WAN controller and a campus controller. Less commonly tested on CCNA but may appear as a distractor option.

---

## 3. REST API Reference

### REST Fundamentals

REST (Representational State Transfer) is an architectural style for building APIs over HTTP or HTTPS. REST APIs use standard HTTP methods to perform operations on resources identified by URLs.

### HTTP Methods (CRUD Mapping)

| HTTP Method | CRUD Operation | Description | Common Use |
|-------------|----------------|-------------|------------|
| GET | Read | Retrieve a resource without modifying it | Query device list, interface stats |
| POST | Create | Submit data to create a new resource | Create a new network policy |
| PUT | Update or Replace | Replace an existing resource entirely | Update a device configuration |
| DELETE | Delete | Remove a resource | Remove a VLAN or policy |

Note: PATCH is sometimes used for partial updates but is not emphasized on the CCNA exam.

### HTTP Status Code Reference

| Range | Category | Key Codes | Meaning |
|-------|----------|-----------|---------|
| 2xx | Success | 200 OK, 201 Created, 204 No Content | Request succeeded |
| 3xx | Redirection | 301 Moved Permanently | Resource location changed |
| 4xx | Client Error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found | Problem with the request |
| 5xx | Server Error | 500 Internal Server Error, 503 Service Unavailable | Server-side problem |

### REST API Request Components

| Component | Purpose | Example |
|-----------|---------|---------|
| HTTP Method | Operation type | GET |
| URL (endpoint) | Resource being accessed | `https://host/api/v1/devices` |
| Headers | Metadata, authentication | `Authorization: Bearer <token>` |
| Body | Data payload (POST and PUT only) | JSON or XML content |

---

## 4. Data Formats Reference

### JSON

JSON (JavaScript Object Notation) is the dominant data format for modern REST APIs. It uses a key-value structure.

```json
{
  "devices": [
    {
      "hostname": "R1",
      "managementIpAddress": "10.0.0.1",
      "platformId": "ISR4451",
      "softwareVersion": "16.9.5"
    }
  ]
}
```

### JSON Structure Rules

| Element | Syntax | Example |
|---------|--------|---------|
| Object | Curly braces | `{ "key": "value" }` |
| Array | Square brackets | `[ "item1", "item2" ]` |
| String | Double quotes | `"hostname"` |
| Number | No quotes | `42` or `3.14` |
| Boolean | Lowercase | `true` or `false` |
| Null | Lowercase | `null` |

### XML

XML (Extensible Markup Language) uses paired tags to structure data. It is more verbose than JSON and is used by NETCONF.

```xml
<device>
  <hostname>R1</hostname>
  <managementIpAddress>10.0.0.1</managementIpAddress>
  <platformId>ISR4451</platformId>
  <softwareVersion>16.9.5</softwareVersion>
</device>
```

### JSON vs XML Comparison

| Feature | JSON | XML |
|---------|------|-----|
| Verbosity | Compact | More verbose |
| Human readability | Higher | Lower |
| Array support | Native | Requires convention |
| Common protocols | REST APIs | NETCONF, SOAP |
| CCNA exam focus | Primary | Secondary |

---

## 5. NETCONF and RESTCONF

### NETCONF

NETCONF (Network Configuration Protocol, RFC 6241) is a standards-based protocol for configuring and retrieving network device state.

| Attribute | Value |
|-----------|-------|
| Transport | SSH (port 830) |
| Data format | XML |
| Operations | get, get-config, edit-config, commit, delete-config |
| Target | Cisco IOS-XE, IOS-XR, Junos, and YANG-supported platforms |

### RESTCONF

RESTCONF (RFC 8040) provides a REST API interface over NETCONF datastores.

| Attribute | Value |
|-----------|-------|
| Transport | HTTPS |
| Data format | JSON or XML |
| Operations | GET, POST, PUT, PATCH, DELETE (HTTP methods) |
| Target | Cisco IOS-XE (16.6+) and YANG-supported platforms |

RESTCONF is conceptually a REST-based wrapper around NETCONF data models. It uses the same YANG data models as NETCONF but exposes them via standard HTTP methods.

---

## 6. Configuration Management Tools Reference

### Ansible

| Feature | Value |
|---------|-------|
| Agent required | No — agentless |
| Communication | SSH (Linux), HTTPS (network APIs) |
| Configuration language | YAML (playbooks, inventory) |
| Model | Push — control node pushes to managed hosts |
| Idempotency | Yes |
| Network support | Cisco IOS, NX-OS, IOS-XE, IOS-XR, Juniper, Arista |

### Puppet

| Feature | Value |
|---------|-------|
| Agent required | Yes — Puppet agent on managed nodes |
| Communication | HTTPS between agent and Puppet master |
| Configuration language | Puppet DSL (declarative) |
| Model | Pull — agents poll master for configuration |
| Network support | Limited native support |

### Chef

| Feature | Value |
|---------|-------|
| Agent required | Yes — Chef client on managed nodes |
| Configuration language | Ruby (Cookbooks and Recipes) |
| Model | Pull — clients check in with Chef server |
| Network support | Limited native support |

### Comparison Summary

| Feature | Ansible | Puppet | Chef |
|---------|---------|--------|------|
| Agent required | No | Yes | Yes |
| Model | Push | Pull | Pull |
| Language | YAML | Puppet DSL | Ruby |
| Network focus | Strong | Limited | Limited |

---

## 7. Cisco DNA Center (Catalyst Center)

Cisco DNA Center (now called Cisco Catalyst Center) is Cisco's enterprise intent-based networking platform and SDN controller.

| Capability | Description |
|------------|-------------|
| Intent-based networking | Administrator defines desired behavior; DNA Center translates to device configs |
| Northbound REST API | External applications query and configure via REST API |
| Southbound protocols | NETCONF and RESTCONF to IOS-XE; SNMP and SSH to legacy devices |
| Network assurance | Continuous monitoring and anomaly detection |
| Automated provisioning | Zero-touch provisioning (ZTP) for new devices |

---

## 8. CCNA Exam Tips

**Tip 1 — Southbound goes down, northbound goes up.** Southbound APIs connect the controller to network devices (below the controller). Northbound APIs connect applications to the controller (above the controller). Both directions are from the controller's perspective.

**Tip 2 — HTTP method CRUD mapping.** GET = Read, POST = Create, PUT = Update or Replace, DELETE = Delete. The exam tests all four. "Retrieve interface statistics" = GET. "Create a new policy" = POST.

**Tip 3 — JSON uses curly braces, XML uses tags.** If the exam shows a code block and asks you to identify the format, look for `{` and `}` for JSON, or `<tag>` for XML. NETCONF uses XML. REST APIs typically use JSON.

**Tip 4 — Ansible is agentless.** This is the most tested distinction between configuration management tools. Ansible requires no agent on managed devices — it uses SSH. Puppet and Chef both require an agent installed on the managed node.

**Tip 5 — Ansible is a push model; Puppet and Chef are pull models.** In the push model (Ansible), the controller node initiates changes. In the pull model (Puppet and Chef), managed nodes periodically check the server for new configuration.

**Tip 6 — OpenFlow is a southbound protocol.** OpenFlow programs flow tables in switches from the SDN controller. On the CCNA exam, OpenFlow is always a southbound API — never northbound.

**Tip 7 — NETCONF uses SSH port 830.** If a question asks which protocol is used to configure Cisco IOS-XE devices over SSH using XML data models, the answer is NETCONF on port 830.

**Tip 8 — 200 OK vs 201 Created.** A GET request that succeeds returns 200 OK. A POST request that creates a new resource returns 201 Created. A successful DELETE may return 204 No Content.

---

## 9. Study Checklist

Work through each item before taking the Module 14 quiz.

- [ ] Draw the three-layer SDN model from memory and label application, control, and data planes
- [ ] Explain northbound API vs southbound API from the controller's perspective
- [ ] List all four HTTP methods and their corresponding CRUD operations from memory
- [ ] Identify whether a given code block is JSON or XML based on its syntax
- [ ] State the key difference between Ansible and Puppet or Chef regarding agents
- [ ] State the push vs pull model for Ansible, Puppet, and Chef
- [ ] Explain what NETCONF does and what transport and port it uses
- [ ] Explain what Cisco DNA Center (Catalyst Center) is and what its northbound interface is
- [ ] Complete the Module 14 lab
- [ ] Post your Module 14 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and practice questions: professormesser.com
