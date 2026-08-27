# Quiz: Module 15 — Automation and Programmability

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points.

---

## Question 1

In an SDN architecture, which term describes the API that connects an SDN controller to the network applications and management tools above it?

A. Southbound API

B. Eastbound API

C. Northbound API

D. Westbound API

Correct Answer: C — The northbound API connects the SDN controller to the application plane above it. Applications use the northbound API (typically REST over HTTPS) to request network services and retrieve network state. The controller is the reference point; applications are "north" of the controller.

Distractor Analysis:

* A — The southbound API connects the controller downward to network devices. Examples include OpenFlow, NETCONF, and RESTCONF.
* B — East-west APIs connect controllers at the same architectural layer to each other; they are not above the controller.
* D — "Westbound" is not a standard SDN API direction term and appears as a distractor on many practice exams.

---

## Question 2

A network automation script needs to retrieve the current list of network devices from Cisco DNA Center without making any changes. Which HTTP method should the script use?

A. POST

B. PUT

C. DELETE

D. GET

Correct Answer: D — GET retrieves data from a REST API resource without modifying server state. Reading a device list, querying interface statistics, or retrieving a configuration are all GET operations. GET is idempotent — calling it multiple times has no side effects.

Distractor Analysis:

* A — POST creates a new resource. Using POST to retrieve data would be incorrect and would likely return a 400 or 404 error.
* B — PUT replaces an existing resource. It is used for updates, not reads.
* C — DELETE removes a resource. Using DELETE on a device list endpoint would attempt to remove devices.

---

## Question 3

A Python script sends a POST request to the Cisco DNA Center API to create a new network policy. The API returns HTTP status code 201. What does this status code indicate?

A. The request failed because the policy already exists.

B. The request succeeded and a new resource was created.

C. The request succeeded and the existing resource was updated.

D. The request requires authentication before it can be processed.

Correct Answer: B — HTTP status code 201 Created indicates that a POST request was processed successfully and a new resource was created on the server. A 200 OK is returned for successful GET or PUT requests. A 201 is specific to successful resource creation via POST.

Distractor Analysis:

* A — A duplicate resource conflict would typically return 409 Conflict, not 201.
* C — A successful PUT update would return 200 OK, not 201 Created.
* D — An authentication challenge would return 401 Unauthorized, not 201.

---

## Question 4

A network engineer is examining an API response and sees the following data structure: `{ "hostname": "R1", "ipAddress": "10.0.0.1" }`. Which data format is this, and what is the identifying characteristic?

A. XML — identified by the opening and closing angle bracket tags

B. JSON — identified by the curly braces containing key-value pairs

C. YAML — identified by the colon-separated key-value pairs

D. CSV — identified by the comma-separated values

Correct Answer: B — The curly braces `{}` containing colon-separated key-value pairs with string values in double quotes identify this as JSON (JavaScript Object Notation). JSON is the dominant format for REST API data exchange and is the format used by Cisco DNA Center APIs.

Distractor Analysis:

* A — XML uses `<tag>value</tag>` syntax with paired angle bracket tags. No tags are present in this example.
* C — YAML uses indentation-based structure (e.g., `hostname: R1`) without curly braces, though YAML can represent the same data differently.
* D — CSV uses comma-separated values in a flat structure with no key names. The structure shown is clearly key-value, not CSV.

---

## Question 5

Which network automation tool is agentless and uses a push model to deploy configuration changes to Cisco network devices?

A. Puppet

B. Chef

C. Ansible

D. OpenFlow

Correct Answer: C — Ansible is agentless — it requires no software installed on managed network devices. It uses SSH (or HTTPS APIs) to communicate. Ansible uses a push model where the control node initiates and pushes configuration to all managed devices simultaneously. Playbooks are written in YAML.

Distractor Analysis:

* A — Puppet requires a Puppet agent installed on managed nodes and uses a pull model where agents check the Puppet server for configuration updates.
* B — Chef requires a Chef client on managed nodes and uses a pull model. It uses Ruby-based Cookbooks.
* D — OpenFlow is a southbound protocol that programs flow tables in switches from an SDN controller. It is not a configuration management tool.

---

## Question 6

Which protocol uses SSH on port 830, exchanges data in XML format, and supports transactional configuration commits?

A. RESTCONF

B. NETCONF

C. OpenFlow

D. SNMP

Correct Answer: B — NETCONF (RFC 6241) uses SSH on port 830, XML as its data format, and YANG data models. Its transactional commit model allows administrators to stage configuration changes in a candidate datastore and commit them atomically — all changes succeed or none are applied. This is significantly safer than CLI-based changes.

Distractor Analysis:

* A — RESTCONF uses HTTPS (not SSH port 830) and supports both JSON and XML. It provides REST-style access to the same YANG models as NETCONF.
* C — OpenFlow is a southbound protocol for programming switch flow tables. It does not use SSH port 830 or XML.
* D — SNMP uses UDP ports 161/162 and is primarily a monitoring and read-only management protocol, not a configuration protocol.

---

## Question 7

A network engineer writes an Ansible playbook that configures NTP on 200 Cisco routers. She runs the playbook twice without any configuration changes in between. What will happen the second time the playbook runs?

A. The playbook will fail because NTP is already configured.

B. The playbook will reconfigure all 200 routers, overwriting existing settings.

C. The playbook will make no changes because Ansible is idempotent.

D. The playbook will skip all tasks that previously succeeded.

Correct Answer: C — Ansible is idempotent. When a playbook task specifies a desired state that already matches the current state of a device, Ansible makes no changes and reports the task as "ok" rather than "changed." This means running the same playbook multiple times is safe and produces the same result without unnecessary device changes.

Distractor Analysis:

* A — Ansible does not fail when a configuration already exists; it compares desired state to current state.
* B — Idempotency prevents redundant reconfigurations. Ansible checks current state before making any change.
* D — Ansible does not "skip" tasks due to previous success. It checks current state on every run and only makes changes when there is a difference.

---

## Question 8

In SDN architecture, which function remains in the network devices (data plane) rather than being centralized in the SDN controller?

A. Routing protocol computation (OSPF SPF calculations)

B. Policy enforcement and access control decisions

C. Client association management in wireless networks

D. Hardware packet forwarding based on programmed flow tables

Correct Answer: D — The data plane remains in network device hardware because packet forwarding must occur at line rate (millions of packets per second). SDN moves the control plane (routing decisions, policy logic) to the centralized controller but leaves hardware forwarding in the ASICs of switches and routers.

Distractor Analysis:

* A — Routing protocol computation (control plane function) is centralized in the SDN controller. Devices no longer need to independently run OSPF or EIGRP.
* B — Policy enforcement decisions are made by the controller (control plane); devices only execute the forwarding rules programmed by the controller.
* C — In controller-based wireless, client association is handled by the WLC (controller), not the AP hardware, which is another example of control-plane centralization.

---

## Question 9

A developer queries the DNA Center REST API using a valid token and receives an HTTP 404 response. What is the most likely cause?

A. The authentication token has expired.

B. The requested resource URL does not exist or the resource ID is incorrect.

C. The server is temporarily unavailable due to maintenance.

D. The client sent a malformed JSON request body.

Correct Answer: B — HTTP 404 Not Found means the server understood the request but could not find the resource at the specified URL. This typically means the endpoint URL is wrong, the resource ID (such as a device ID in the URL path) does not match any existing resource, or the API version in the URL is incorrect.

Distractor Analysis:

* A — An expired token returns 401 Unauthorized, not 404.
* C — A temporarily unavailable server returns 503 Service Unavailable or 500 Internal Server Error, not 404.
* D — A malformed request body returns 400 Bad Request, not 404. A 404 means the URL path itself resolves to no resource.

---

## Question 10

Which of the following correctly describes how RESTCONF differs from NETCONF?

A. RESTCONF uses SSH on port 830; NETCONF uses HTTPS.

B. RESTCONF uses HTTP methods and supports JSON; NETCONF uses SSH and XML exclusively.

C. RESTCONF requires a YANG data model; NETCONF does not use data models.

D. RESTCONF is a southbound protocol; NETCONF is a northbound protocol.

Correct Answer: B — RESTCONF uses standard HTTP methods (GET, POST, PUT, DELETE) over HTTPS and supports both JSON and XML. NETCONF uses SSH on port 830 and uses XML exclusively. Both protocols use YANG data models. RESTCONF is conceptually a REST-based interface to the same underlying YANG data models that NETCONF uses.

Distractor Analysis:

* A — This reverses the transports. NETCONF uses SSH port 830; RESTCONF uses HTTPS. This reversal is the most common exam trap on this topic.
* C — Both NETCONF and RESTCONF use YANG data models. YANG is not exclusive to RESTCONF.
* D — Both NETCONF and RESTCONF are southbound protocols — they run between the SDN controller and the managed network devices. Neither is a northbound protocol.

---

---

## Question 11

A network engineer writes a Python script using the `requests` library to retrieve device information from Cisco DNA Center. The script returns a 401 HTTP status code. What is the most likely cause?

A. The DNA Center server is unreachable at the specified IP address.

B. The script is missing or providing an invalid authentication token in the request header.

C. The GET request URL contains a typo and the resource does not exist.

D. The JSON response body is malformed and cannot be parsed.

Correct Answer: B — HTTP 401 Unauthorized indicates that the request lacks valid authentication credentials. For DNA Center REST APIs, every request must include a valid bearer token in the `X-Auth-Token` header. A missing token, an expired token, or an incorrect token all return 401. The fix is to re-authenticate (POST to the auth endpoint) to obtain a fresh token and include it in all subsequent requests.

Distractor Analysis:

* A — An unreachable server returns a connection error (requests.exceptions.ConnectionError) or a timeout — not an HTTP 401. An HTTP status code means the server was reached and understood the request.
* C — A typo in the URL causing a missing resource returns 404 Not Found, not 401. A 404 means the server found no resource at that path.
* D — A malformed JSON body returns 400 Bad Request from the server. However, a malformed response body would be a client-side parsing error in Python, not an HTTP status code from the server.

---

## Question 12

In an SDN deployment, the control plane is separated from the data plane. A network device receives a packet that does not match any existing flow table entry. What happens next in a typical OpenFlow-based SDN architecture?

A. The device drops the packet because it has no local intelligence to determine forwarding.

B. The device floods the packet out all ports to ensure delivery.

C. The device sends a Packet-In message to the SDN controller requesting forwarding instructions.

D. The device applies the default route from its local routing table as a fallback.

Correct Answer: C — When an OpenFlow-enabled switch receives a packet with no matching flow table entry, it generates a Packet-In message and sends it to the SDN controller. The controller then determines the appropriate forwarding action and installs a new flow entry in the switch's flow table (via a Flow-Mod message). Future packets matching that flow are forwarded by the switch using the installed rule without involving the controller.

Distractor Analysis:

* A — Dropping unknown packets is not the default OpenFlow behavior. The table-miss action (configurable) typically sends the packet to the controller via Packet-In.
* B — While flooding is the default behavior in traditional Ethernet switches, OpenFlow-based devices send unknowns to the controller, not flood them (unless the controller instructs flooding as the action).
* D — OpenFlow-based SDN data planes do not maintain independent local routing tables for fallback. All forwarding decisions are programmed by the controller.

---

## Question 13

Which statement correctly describes the difference between traditional distributed networking and SDN?

A. Traditional networking uses faster ASICs; SDN uses slower software-based switching.

B. In traditional networking, each device independently runs control plane protocols; in SDN, control plane intelligence is centralized in a controller.

C. SDN requires replacement of all network hardware with specialized SDN switches; traditional switches cannot be used.

D. SDN eliminates the data plane entirely, processing all packets in software on the controller.

Correct Answer: B — The fundamental distinction is where control plane intelligence resides. In traditional distributed networking, each router or switch independently runs protocols (OSPF, STP, etc.) and makes its own forwarding decisions. In SDN, these decisions are centralized in the controller, which programs forwarding rules into the data plane devices. The data plane hardware remains in the devices but follows instructions from the controller rather than computing them independently.

Distractor Analysis:

* A — SDN data planes use the same high-speed ASIC hardware as traditional switches. The separation of control and data planes does not reduce forwarding performance.
* C — Many SDN architectures use commodity or standard network hardware. OpenFlow-capable software can be added to existing switches. Some SDN overlays (like Cisco SD-WAN) work with standard routers.
* D — SDN does not eliminate the data plane. Packet forwarding still occurs in hardware at line rate within the network devices. Only the control plane logic is centralized.

---

## Question 14

An Ansible playbook contains the following task. What does the `state: merged` parameter specify?

```yaml
- name: Configure interface description
  cisco.ios.ios_interfaces:
    config:
      - name: GigabitEthernet0/1
        description: "Uplink to Core"
    state: merged
```

A. Replace the entire interface configuration with only the values specified.

B. Add or update the specified values without removing existing interface configuration not mentioned in the task.

C. Delete the interface and recreate it with the specified configuration.

D. Verify the current state matches the specified values and report differences without making changes.

Correct Answer: B — In Ansible network resource modules, `state: merged` applies the specified configuration additively. Existing configuration not mentioned in the task is left unchanged. This is the safest state for day-to-day changes — it only adds or modifies what is explicitly defined. Compare with `state: replaced` (replaces all config for the resource) or `state: deleted` (removes config).

Distractor Analysis:

* A — Describes `state: replaced`, which replaces all configuration for the specified resource section.
* C — Describes behavior closer to `state: deleted` followed by `state: merged`, not the `merged` state alone.
* D — Describes `state: gathered` or verification tasks. The `merged` state actively makes changes.

---

## Question 15

A network automation script uses Python to configure VLANs on 100 switches using NETCONF. Which Python library is most appropriate for sending NETCONF requests?

A. `requests`

B. `ncclient`

C. `netmiko`

D. `json`

Correct Answer: B — `ncclient` (NETCONF client) is the Python library specifically designed for NETCONF operations. It establishes SSH connections on port 830, handles NETCONF session management, and provides Python methods for get-config, edit-config, commit, and other NETCONF operations with XML payloads.

Distractor Analysis:

* A — `requests` is an HTTP/HTTPS library used for REST API calls (including RESTCONF). It does not support the SSH-based NETCONF protocol or NETCONF session management.
* C — `netmiko` establishes SSH connections to network devices and sends CLI commands, parsing the text output. It does not use the NETCONF protocol or structured XML data.
* D — `json` is Python's built-in JSON serialization/deserialization library. It handles data formatting but has no network connectivity capabilities.

---

## Question 16

What is the correct HTTP method and expected success status code for updating an existing device configuration entry via a REST API?

A. POST; 201 Created

B. GET; 200 OK

C. PUT; 200 OK

D. DELETE; 204 No Content

Correct Answer: C — PUT is the HTTP method used to update (replace) an existing resource. When a PUT request succeeds, the server typically responds with 200 OK (along with the updated resource) or 204 No Content (no body). POST creates new resources (returns 201); GET reads resources (returns 200); DELETE removes resources (returns 200 or 204).

Distractor Analysis:

* A — POST creates a new resource. Using POST when updating an existing resource is incorrect semantics and typically returns an error or creates a duplicate.
* B — GET is a read-only operation. It retrieves the current state of a resource and never modifies it.
* D — DELETE removes a resource. While 204 No Content is associated with successful DELETE operations, the question asks about updating, not deleting.

---

## Question 17

A YANG data model defines the structure of configuration data for network devices. What is YANG used for in the context of NETCONF and RESTCONF?

A. YANG is the transport protocol that carries XML configuration between the controller and managed devices.

B. YANG defines the structure, data types, and constraints of configuration and operational data for device management.

C. YANG is a query language similar to SQL used to filter NETCONF responses.

D. YANG replaces CLI on network devices, providing a graphical interface for configuration.

Correct Answer: B — YANG (Yet Another Next Generation) is a data modeling language (RFC 6020) that defines the schema for network configuration and operational data. It specifies what data exists, its types (strings, integers, lists), its hierarchy, and its constraints. NETCONF and RESTCONF use YANG models to validate configuration requests and structure responses. Cisco IOS-XE ships with hundreds of standard and vendor-specific YANG models.

Distractor Analysis:

* A — YANG is not a transport protocol. NETCONF uses SSH, RESTCONF uses HTTPS. YANG is only the data model definition language.
* C — YANG is not a query language. NETCONF uses XPath expressions to filter XML data within requests. YANG defines the data structure that XPath navigates.
* D — YANG has nothing to do with graphical interfaces. It is a text-based schema language read by tools and protocol implementations, not by end users directly.

---

## Question 18

Which Cisco platform is the primary management interface for Cisco DNA Center's northbound REST API, allowing external applications to interact with the enterprise network programmatically?

A. Cisco ISE (Identity Services Engine)

B. Cisco WLC (Wireless LAN Controller)

C. Cisco Intent-Based Networking (IBN) API on Catalyst Center

D. Cisco IOS-XE RESTCONF interface

Correct Answer: C — Cisco DNA Center (now rebranded as Catalyst Center) exposes its northbound REST API called the "Intent API" (also referred to as the IBN API). External applications and scripts use this API via HTTPS to interact with the entire network — device inventory, policy, automation, and assurance — through a single management point. This is the northbound interface above the DNA Center controller.

Distractor Analysis:

* A — Cisco ISE is a security policy management platform providing AAA and 802.1X. It has its own API but is not the DNA Center northbound interface for network management.
* B — The WLC manages wireless networks. Its API is a management interface for the WLC specifically, not a network-wide SDN northbound API.
* D — Cisco IOS-XE RESTCONF is a southbound interface — it runs directly on individual IOS-XE devices for per-device configuration. DNA Center's northbound API aggregates management across all devices.

---

## Question 19

A Python script parsing a NETCONF response needs to extract the IP address value from the following XML structure. Which Python code correctly extracts the IP address string?

```xml
<interface>
  <name>GigabitEthernet0/1</name>
  <ipv4>
    <address>
      <ip>192.168.1.1</ip>
    </address>
  </ipv4>
</interface>
```

A. `data["interface"]["ipv4"]["address"]["ip"]`

B. `root.find(".//ip").text`

C. `data.get("ip")`

D. `json.loads(data)["ip"]`

Correct Answer: B — When NETCONF XML is parsed with Python's `xml.etree.ElementTree` library, `root.find(".//ip")` uses XPath syntax to search for the `<ip>` element anywhere in the tree (`//` = recursive search). `.text` retrieves the text content of the element ("192.168.1.1"). This is the standard Python XML navigation pattern for nested elements.

Distractor Analysis:

* A — Dictionary-style bracket notation is used for JSON (parsed to a Python dictionary with `json.loads()`), not XML. XML parsed with ElementTree returns Element objects, not dictionaries.
* C — `data.get("ip")` is a dictionary method that would only work if the XML had already been converted to a flat Python dictionary with an "ip" key. The nested XML structure requires tree traversal.
* D — `json.loads()` parses JSON-formatted strings. The data shown is XML, not JSON. Calling `json.loads()` on an XML string raises a JSON decode error.

---

## Question 20

An organization is evaluating whether to deploy Ansible or Puppet for network device configuration management. The primary requirement is support for agentless management of 300 Cisco IOS routers. Which tool is more appropriate and why?

A. Puppet — it uses a pull model that distributes the load across all managed devices.

B. Ansible — it is agentless and communicates with Cisco IOS routers via SSH without requiring software installation on each device.

C. Chef — it provides the most extensive library of Ruby-based recipes for Cisco device management.

D. Both are equally appropriate because all three tools support agentless Cisco IOS management.

Correct Answer: B — Ansible is the correct choice because it is agentless — it requires no software installation on the 300 Cisco routers. Ansible communicates via SSH using the cisco.ios collection and can configure IOS devices directly. Puppet and Chef require agents installed on managed nodes, which is not feasible on Cisco IOS routers (you cannot install a Puppet agent on a router's IOS).

Distractor Analysis:

* A — Puppet's pull model is a feature of its agent-based architecture, but the pull model requires an agent on each managed node. Cisco IOS routers cannot run the Puppet agent.
* C — Chef uses Ruby-based Cookbooks, but like Puppet, it requires a Chef client on managed nodes. Cisco IOS does not support the Chef client.
* D — Only Ansible is agentless among the three tools. Puppet and Chef are agent-based and cannot directly manage traditional Cisco IOS devices without an agent.

---

End of Quiz — Module 15
