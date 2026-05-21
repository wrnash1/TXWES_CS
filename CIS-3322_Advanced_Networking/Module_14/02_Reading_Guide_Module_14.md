# Reading Guide: Module 14 - Network Automation & REST APIs
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 14 - Network Automation & REST APIs**! This week's study material focuses on the core foundations and configuration mechanics of **Network Automation & REST APIs** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **SDN controller architecture**: Software-Defined Networking separates the control plane (routing/switching decisions) from the data plane (packet forwarding), centralizing intelligence in a software-based controller. The controller has a global view of the network and programs forwarding behavior in all devices via southbound APIs. Examples include Cisco DNA Center (now called Cisco Catalyst Center) and OpenDaylight. This enables centralized policy management, automation, and dynamic network adaptation without manual per-device configuration.
*   **Northbound vs southbound APIs**: In SDN architecture, **southbound APIs** communicate between the controller and network devices (switches, routers) to push forwarding rules — OpenFlow and NETCONF are common southbound protocols. **Northbound APIs** communicate between the controller and applications or management tools (like monitoring dashboards or orchestration systems) — typically using REST over HTTPS with JSON or XML payloads. This layered API model is fundamental to modern intent-based networking.
*   **JSON/XML data formats**: JSON (JavaScript Object Notation) and XML (Extensible Markup Language) are the two dominant data serialization formats used in REST API exchanges between network controllers and applications. JSON uses key-value pairs in curly braces (`{"key": "value"}`) and is more compact and human-readable. XML uses opening/closing tags (`<tag>value</tag>`) and is more verbose. The CCNA exam focuses on reading and recognizing JSON structures, not writing code.

---

### 2. Certification Exam Tips
*   **CCNA Domain:** Network Automation and Programmability accounts for **15%** of the CCNA 200-301 exam — a significant domain that is often underprepared. Expect 4–6 questions on SDN concepts, REST APIs, data formats, and automation tools.
*   **REST HTTP methods — memorize all four:** GET (read data), POST (create new resource), PUT (replace/update resource), DELETE (remove resource). The CCNA exam tests which HTTP method corresponds to each CRUD operation.
*   **Configuration management tools:** Know the basic differences between Ansible (agentless, uses YAML playbooks, push model), Puppet (agent-based, pull model, uses Puppet DSL), and Chef (agent-based, pull model, uses Ruby). The exam asks conceptual questions, not configuration syntax.
*   **Cisco DNA Center (Catalyst Center):** Understand that it provides intent-based networking, a GUI and REST API northbound interface, and uses NETCONF/RESTCONF southbound to program Cisco IOS-XE devices. The exam may show an API call scenario and ask which direction (north or south) it represents.
*   **Study Resource:** Watch the network automation and programmability episodes in the Jeremy's IT Lab CCNA free playlist, which cover SDN architecture, REST API methods, JSON data format, and configuration management tools: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look for the "Network Automation" and "SDN" episodes near the end of the playlist.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Network Automation and Programmability** in the Cisco Skills for All CCNA course. The content covers SDN controllers, REST APIs, JSON/YAML data formats, and Ansible/Puppet/Chef overviews: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to "CCNA: Enterprise Networking, Security, and Automation" — the Automation chapter.
*   **Required Video:** Watch the network automation episodes in the Jeremy's IT Lab CCNA complete playlist. These videos are essential for a domain that is frequently underrepresented in study materials: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Parse a JSON payload using Python dictionary structures**: Study a sample JSON response from a network API (e.g., a Cisco DNA Center device inventory response). Identify key-value pairs, nested objects, and arrays. Practice accessing values using Python dictionary notation (`data["hostname"]`).
*   **Send a mock REST API request using `curl`**: Use `curl -X GET https://[controller-ip]/dna/intent/api/v1/network-device -H "X-Auth-Token: [token]"` to simulate a northbound API GET request. Observe the JSON response structure returned by the controller.
*   **Verify Cisco DNA Center API return values**: Review the JSON response fields for device type, platform ID, software version, and reachability status. Understand how an automation script would parse these values to make configuration decisions.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Network Automation** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the automation and SDN episodes in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
