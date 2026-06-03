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

End of Quiz — Module 15
