import os
import re
import random
import urllib.parse
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from enrich_course_content import ALL_COURSES as ENRICHED_COURSES, TERM_DEFINITIONS as BASE_TERM_DEFS

BASE_DIR = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"

# 1. Domain Definitions and Categorization
DOMAINS = {
    "programming": [
        "CIS-1310_Intro_to_Python",
        "CIS-1320_Intro_to_JavaScript",
        "CIS-2315_Data_Structures_Algorithms",
        "CIS-3340_Full_Stack_Web_Dev",
        "CIS-3350_Software_Engineering_Agile",
        "CIS-4350_DevSecOps_CICD_Pipelines"
    ],
    "networking": [
        "CIS-3321_Network_Admin",
        "CIS-3322_Advanced_Networking"
    ],
    "os_admin": [
        "CIS-2320_Hardware_Fund",
        "CIS-3325_OS_Admin",
        "CIS-3326_Windows_Server_Admin",
        "CIS-4337_Infrastructure_Automation"
    ],
    "database": [
        "CIS-4327_Database_Admin",
        "CIS-4336_Data_Analytics",
        "CIS-4320_Enterprise_Systems_ERP"
    ],
    "security": [
        "CIS-4328_Information_Security",
        "CIS-4332_Cyber_Analyst",
        "CIS-4333_Penetration_Testing"
    ],
    "cloud": [
        "CIS-4329_Google_Cloud",
        "CIS-4331_Azure_Cloud",
        "CIS-4334_AWS_Cloud_Architecture"
    ],
    "ai": [
        "CIS-4330_Intro_to_AI",
        "CIS-4345_Machine_Learning_Deep_Learning"
    ],
    "management_services": [
        "CIS-3310_IT_Project_Management",
        "CIS-3312_Systems_Analysis_Design",
        "CIS-4315_Cyber_Governance_Risk_Compliance",
        "CIS-4335_IT_Service_Management",
        "CIS-4355_IoT_Embedded_Systems"
    ]
}

def get_course_domain(course_code):
    for dom, list_courses in DOMAINS.items():
        if course_code in list_courses:
            return dom
    return "management_services"

# 2. Rich Domain-Specific Databases for Question generation
DOMAIN_DATABASE = {
    "programming": {
        "concepts": {
            "Variable Scope": "The region of a program where a variable is accessible, such as local, global, or class scope.",
            "Memory Leak": "An undesired resource consumption where a program fails to release allocated memory that is no longer needed.",
            "Refactoring": "The process of restructuring existing computer code without changing its external behavior to improve readability and reduce complexity.",
            "Inheritance": "A key object-oriented programming concept where a child class derives attributes and behaviors from a parent class.",
            "Polymorphism": "The ability of different classes to respond to the same message or method call in their own unique way.",
            "Encapsulation": "The practice of hiding the internal state and representation of an object, exposing access only through public methods."
        },
        "commands": [
            {"cmd": "python3 -m venv .venv", "desc": "create a sandboxed Python virtual environment to manage dependencies locally"},
            {"cmd": "pip install -r requirements.txt", "desc": "install all external project dependencies specified in the requirements manifest"},
            {"cmd": "git commit -m 'update'", "desc": "record staged code modifications into the repository version history"},
            {"cmd": "pytest", "desc": "run the automated unit testing suite to verify system functionality"}
        ],
        "troubleshooting": [
            {"err": "KeyError", "fix": "Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.", "cause": "The code attempted to access a dictionary key that is not defined in the object."},
            {"err": "IndexError", "fix": "Verify that the index is within the valid range of 0 to len(list)-1.", "cause": "The code attempted to access an element of a sequence using an out-of-bounds index."},
            {"err": "TypeError", "fix": "Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.", "cause": "An operation or function was applied to an object of an inappropriate data type."}
        ],
        "security": [
            {"topic": "SQL Injection Prevention", "fix": "Implement parameterized queries and prepared statements rather than raw string concatenation.", "risk": "Allowing attackers to execute arbitrary SQL commands on the backend database via input forms."},
            {"topic": "Sensitive Data Exposure", "fix": "Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.", "risk": "Storing user credentials in plain text, making them vulnerable to database breaches."}
        ]
    },
    "networking": {
        "concepts": {
            "Subnetting": "The practice of dividing a single logical network into multiple smaller, manageable subnetwork segments to optimize traffic and enhance security.",
            "VLAN (Virtual LAN)": "A logical network segment created on network switches to isolate broadcast domains regardless of physical connections.",
            "Default Gateway": "The node or router interface on a network that serves as an access point to other logical networks or the internet.",
            "Routing Table": "A data table stored in a router or network host that lists the paths and network destinations to determine where packets should be forwarded.",
            "DNS Resolution": "The translation of human-readable domain names into machine-readable IP addresses.",
            "TCP Handshake": "The three-step synchronization protocol (SYN, SYN-ACK, ACK) used to establish a reliable, connection-oriented transport session."
        },
        "commands": [
            {"cmd": "ping", "desc": "verify basic network connectivity and latency to a remote host using ICMP Echo Requests"},
            {"cmd": "traceroute", "desc": "map and trace the exact path of router hops packets travel to reach a target destination"},
            {"cmd": "netstat -ano", "desc": "display all active network connections, listening ports, and corresponding process identifiers"},
            {"cmd": "nslookup", "desc": "query DNS servers to verify domain name resolution and retrieve resource records"}
        ],
        "troubleshooting": [
            {"err": "IP Address Conflict", "fix": "Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.", "cause": "Two devices on the same physical or logical network segment are configured with the identical IP address."},
            {"err": "DNS Failure", "fix": "Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.", "cause": "The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution."},
            {"err": "Subnet Mask Mismatch", "fix": "Correct the subnet mask configuration on the interface to match the network segment parameters.", "cause": "A host is configured with an incorrect subnet mask, preventing it from identifying local vs. remote addresses."}
        ],
        "security": [
            {"topic": "Unencrypted Traffic Exposure", "fix": "Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.", "risk": "Attackers capturing plaintext management passwords or session data using network sniffers."},
            {"topic": "Unauthorized Port Access", "fix": "Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.", "risk": "Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports."}
        ]
    },
    "os_admin": {
        "concepts": {
            "Kernel": "The core component of an operating system that manages hardware resources, memory, and acts as a bridge between applications and hardware.",
            "Process": "An active, running instance of a computer program that has its own isolated memory address space and system resources.",
            "Virtual Memory": "A memory management capability that uses hardware and software to allow a computer to compensate for physical memory shortages by temporarily transferring data to disk.",
            "Group Policy Object (GPO)": "A collection of configuration settings in Microsoft Windows Active Directory that controls user and computer environments.",
            "Active Directory (AD DS)": "A directory service developed by Microsoft that manages domains, resources, users, and computer permissions in an enterprise network.",
            "Daemons / Services": "Background utility processes that run continuously without direct user interaction to handle system tasks."
        },
        "commands": [
            {"cmd": "chmod 600 config.conf", "desc": "restrict file read and write permissions to the file owner only, removing all group and other access"},
            {"cmd": "systemctl restart service", "desc": "instruct the systemd init system to restart a specified background service process"},
            {"cmd": "df -h", "desc": "display total disk space capacity, usage, and available space in a human-readable format"},
            {"cmd": "ps aux", "desc": "list all currently active processes running on the system with CPU and memory usage statistics"}
        ],
        "troubleshooting": [
            {"err": "Permission Denied", "fix": "Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.", "cause": "The current user account lacks the required read, write, or execute permissions for the target file or system call."},
            {"err": "Disk Space Full", "fix": "Run log rotations, clean temporary files, or expand the logical volume capacity.", "cause": "The storage volume has run out of space, preventing files from being written and causing system services to fail."},
            {"err": "Service Failed to Bind Port", "fix": "Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.", "cause": "Another application or stale instance of the service is already listening on the designated network port."}
        ],
        "security": [
            {"topic": "Privileged Access Abuse", "fix": "Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.", "risk": "Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware."},
            {"topic": "Stale Accounts & Services", "fix": "Disable unused system accounts and run a port scan to disable unnecessary active background services.", "risk": "Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access."}
        ]
    },
    "database": {
        "concepts": {
            "Normalization": "The database design process of organizing tables to minimize data redundancy and dependency, dividing large tables into smaller ones.",
            "Primary Key": "A unique identifier column or set of columns in a database table that guarantees every row can be uniquely identified.",
            "Foreign Key": "A column or group of columns in one database table that refers to the primary key in another table, enforcing referential integrity.",
            "ACID Transactions": "The four properties (Atomicity, Consistency, Isolation, Durability) that guarantee database transactions are processed reliably.",
            "Index": "A data structure that improves the speed of data retrieval operations on a database table at the cost of additional write speed and storage.",
            "SQL Joins": "SQL clauses used to combine rows from two or more tables based on a related column between them."
        },
        "commands": [
            {"cmd": "SELECT * FROM users WHERE active = 1;", "desc": "query and retrieve active user records matching specific conditions from the database table"},
            {"cmd": "CREATE INDEX idx_email ON users(email);", "desc": "create a search index on the email column to speed up lookup queries significantly"},
            {"cmd": "GRANT SELECT ON client_db TO analyst_role;", "desc": "assign read-only access privileges on the database to a specific security role"},
            {"cmd": "EXPLAIN ANALYZE SELECT * FROM logs;", "desc": "analyze the database execution plan to identify performance bottlenecks and slow scan steps"}
        ],
        "troubleshooting": [
            {"err": "Database Deadlock", "fix": "Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.", "cause": "Two or more transactions are waiting for each other to release locks on resources, causing a permanent block."},
            {"err": "Slow Query Performance", "fix": "Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.", "cause": "The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax."},
            {"err": "Connection Timeout", "fix": "Increase the database connection pool limit, adjust timeout configurations, or scale database resources.", "cause": "The database server has exhausted its pool of concurrent client connections or is overloaded with work."}
        ],
        "security": [
            {"topic": "SQL Injection Exposure", "fix": "Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.", "risk": "Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents."},
            {"topic": "Unencrypted Storage", "fix": "Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.", "risk": "Unauthorized access to database backup files or physical drives exposing all customer data."}
        ]
    },
    "security": {
        "concepts": {
            "CIA Triad": "The core model of cybersecurity representing three objectives: Confidentiality, Integrity, and Availability.",
            "Multi-Factor Authentication (MFA)": "A security control requiring users to provide two or more verification factors to gain access to resources.",
            "Asymmetric Encryption": "A cryptographic method that uses a public key to encrypt data and a mathematically related private key to decrypt it.",
            "Principle of Least Privilege": "The security rule that users and systems should only be granted the minimum necessary permissions required to perform their tasks.",
            "Phishing": "A social engineering attack where malicious actors send fraudulent messages designed to trick victims into revealing sensitive information.",
            "IDS / IPS": "Intrusion Detection/Prevention Systems that monitor network traffic for suspicious activity or policy violations."
        },
        "commands": [
            {"cmd": "nmap -sV -p 1-1024 target_ip", "desc": "scan ports on a target host to identify active services and their version numbers"},
            {"cmd": "openssl x509 -text -noout -in cert.pem", "desc": "display the detailed metadata and validation parameters of an SSL/TLS digital certificate"},
            {"cmd": "wireshark", "desc": "launch the graphical packet analyzer to capture and dissect network frames in real-time"},
            {"cmd": "hydra -l admin -P passwords.txt ssh://target", "desc": "run a dictionary brute-force attack against the target SSH service to test credential strength"}
        ],
        "troubleshooting": [
            {"err": "Certificate Expired Error", "fix": "Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.", "cause": "The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections."},
            {"err": "IDS False Positives", "fix": "Tune the detection signatures and define exceptions for authorized administrative activities.", "cause": "The network security system flags benign administrative scans or regular traffic patterns as malicious exploits."},
            {"err": "Firewall Blocking Valid Traffic", "fix": "Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.", "cause": "The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted."}
        ],
        "security": [
            {"topic": "Weak Key Strength", "fix": "Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).", "risk": "Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality."},
            {"topic": "Lack of Centralized Logs", "fix": "Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.", "risk": "Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation."}
        ]
    },
    "cloud": {
        "concepts": {
            "Shared Responsibility Model": "The security framework dividing operations between the cloud provider (security OF the cloud) and the customer (security IN the cloud).",
            "VPC (Virtual Private Cloud)": "A logically isolated virtual network dedicated to a cloud account, giving control over subnets, IP ranges, and route tables.",
            "Identity & Access Management (IAM)": "The cloud framework of policies and technologies ensuring that the right entities have appropriate access to resources.",
            "Infrastructure as Code (IaC)": "The practice of managing and provisioning cloud infrastructure through machine-readable definition files (e.g. Terraform).",
            "Auto-scaling": "A cloud feature that dynamically adjusts resource capacity (number of VMs) based on active demand or performance metrics.",
            "Object Storage": "A computer data storage architecture that manages data as objects (e.g. AWS S3, Google Cloud Storage), offering high scalability."
        },
        "commands": [
            {"cmd": "aws s3 sync local_dir s3://my-bucket", "desc": "synchronize local files directly to a cloud object storage bucket"},
            {"cmd": "gcloud compute instances list", "desc": "query the cloud API to retrieve a list of all active virtual machines in the project"},
            {"cmd": "terraform apply", "desc": "execute the infrastructure plan to provision or modify resources defined in the configuration files"},
            {"cmd": "kubectl get pods -n production", "desc": "list all active container pods running in the production namespace of the Kubernetes cluster"}
        ],
        "troubleshooting": [
            {"err": "IAM Access Denied", "fix": "Review the user's IAM policies and attach the specific policy granting permissions for the resource action.", "cause": "The user account or service role lacks the explicit IAM permissions required to execute the API call."},
            {"err": "Cloud Instance Unreachable", "fix": "Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.", "cause": "The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection."},
            {"err": "Cloud Billing Spike", "fix": "Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.", "cause": "Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously."}
        ],
        "security": [
            {"topic": "Publicly Exposed Storage Buckets", "fix": "Enable Block Public Access configurations and enforce access control via IAM or signed URLs.", "risk": "Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches."},
            {"topic": "Compromised Access Keys", "fix": "Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.", "risk": "Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover."}
        ]
    },
    "ai": {
        "concepts": {
            "Overfitting": "A machine learning error where a model learns the training data too well, capturing noise and failing to generalize to new data.",
            "Supervised Learning": "A type of machine learning where the model is trained on labeled training data containing input-output pairs.",
            "Neural Network": "A computational model inspired by the biological brain structure, consisting of interconnected layers of nodes (neurons).",
            "Loss Function": "A mathematical method of evaluating how well a machine learning algorithm models the training dataset.",
            "Feature Engineering": "The process of using domain knowledge to extract features from raw data, improving machine learning model performance.",
            "Deep Learning": "A subset of machine learning based on artificial neural networks with multiple layers (deep architectures)."
        },
        "commands": [
            {"cmd": "import pandas as pd; df = pd.read_csv('data.csv')", "desc": "import the pandas library to load and analyze a tabular dataset"},
            {"cmd": "model.fit(X_train, y_train)", "desc": "train the machine learning model on the training features and targets"},
            {"cmd": "predictions = model.predict(X_test)", "desc": "use the trained model to generate predictions on unseen test data"},
            {"cmd": "accuracy = accuracy_score(y_test, predictions)", "desc": "calculate the accuracy metric of the model predictions against actual labels"}
        ],
        "troubleshooting": [
            {"err": "Low Model Generalization", "fix": "Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.", "cause": "The model has overfit the training data and performs poorly on unseen validation or testing datasets."},
            {"err": "Missing Value Errors", "fix": "Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.", "cause": "The dataset contains null or missing values, causing mathematical operators in the model to fail."},
            {"err": "Data Leakage", "fix": "Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.", "cause": "Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores."}
        ],
        "security": [
            {"topic": "Model Inversion Vulnerability", "fix": "Apply differential privacy methods to the training data and limit public API rate queries.", "risk": "Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs."},
            {"topic": "Adversarial Examples", "fix": "Train models with adversarial inputs and implement input validation/filtering on inputs.", "risk": "Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications."}
        ]
    },
    "management_services": {
        "concepts": {
            "Critical Path Method (CPM)": "A project management technique that identifies the sequence of dependent tasks that determines the shortest time to complete a project.",
            "Scope Creep": "The uncontrolled growth or changes to a project's scope without adjustments to time, cost, and resources.",
            "Service Level Agreement (SLA)": "A commitment between a service provider and a client regarding the service's quality, availability, and responsibilities.",
            "Risk Register": "A project management document that lists identified risks, their severity, likelihood, and mitigation strategies.",
            "Agile Methodology": "A project management approach characterized by building projects incrementally through small, iterative cycles (sprints).",
            "ITIL Framework": "A set of detailed practices for IT service management (ITSM) that focuses on aligning IT services with the needs of business."
        },
        "commands": [
            {"cmd": "git log --oneline -n 5", "desc": "review the last five project commits in a concise single-line format"},
            {"cmd": "docker-compose up -d", "desc": "launch all application services in the background using docker-compose configuration"},
            {"cmd": "terraform validate", "desc": "check the configuration files for syntactic and internal consistency correctness"},
            {"cmd": "systemctl status iot_service", "desc": "verify the active status and resource usage of the background service daemon"}
        ],
        "troubleshooting": [
            {"err": "Scope Exceeded Budget Limit", "fix": "Implement strict change control boards (CCB) and re-baseline the project constraints.", "cause": "The project scope expanded during execution without adjusting budget or schedule allocations."},
            {"err": "Dependency Bottleneck", "fix": "Re-assign resources to critical path tasks and establish clear communication protocols.", "cause": "A critical task is blocked by a delayed prerequisite task, stalling the entire project timeline."},
            {"err": "SLA Breach Alert", "fix": "Optimize service resources, implement load balancing, or update failover mechanisms.", "cause": "A system outage or slow response time has exceeded the limits guaranteed in the Service Level Agreement."}
        ],
        "security": [
            {"topic": "Unauthorized Scope Modification", "fix": "Establish formal authorization procedures and digital signatures for all project scope modifications.", "risk": "Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities."},
            {"topic": "Lack of Business Continuity Plan", "fix": "Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.", "risk": "A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented."}
        ]
    }
}

# 3. Dynamic Question Generator
def generate_term_question(domain, terms_list, cert):
    db = DOMAIN_DATABASE[domain]
    term = random.choice(terms_list) if terms_list else random.choice(list(db["concepts"].keys()))
    term_clean = term.strip().replace("`", "").replace("...", "")
    
    correct_def = db["concepts"].get(term_clean)
    if not correct_def:
        correct_def = BASE_TERM_DEFS.get(term_clean)
    if not correct_def:
        correct_def = f"A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within {domain} operations."
        
    # Get distractors
    all_defs = list(db["concepts"].values()) + list(BASE_TERM_DEFS.values())
    random.shuffle(all_defs)
    distractors = [d for d in all_defs if d != correct_def][:3]
    while len(distractors) < 3:
        distractors.append("An alternative configuration standard used to manage resource limits on legacy systems.")
        
    options = [
        f"A) {correct_def}",
        f"B) {distractors[0]}",
        f"C) {distractors[1]}",
        f"D) {distractors[2]}"
    ]
    random.shuffle(options)
    
    # Identify correct option letter
    correct_letter = "A"
    for opt in options:
        if opt.endswith(correct_def):
            correct_letter = opt[0]
            break
            
    # Format distractor analysis
    dist_analysis = ""
    for opt in options:
        letter = opt[0]
        if letter == correct_letter:
            dist_analysis += f"    * *Why {letter} is correct:* This describes the exact role and function of **{term_clean}**.\n"
        else:
            dist_analysis += f"    * *Why {letter} is incorrect:* This option represents an alternative operational definition that does not apply to **{term_clean}**.\n"
            
    return f"""**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **{term_clean}**?
{options[0]}
{options[1]}
{options[2]}
{options[3]}
*   **Correct Answer:** {correct_letter}) {correct_def}
*   **Distractor Analysis:**
{dist_analysis}"""

def generate_command_question(domain, cert):
    db = DOMAIN_DATABASE[domain]
    cmd_info = random.choice(db["commands"])
    cmd = cmd_info["cmd"]
    desc = cmd_info["desc"]
    
    # Get distractors
    all_cmds = [c["cmd"] for c in db["commands"] if c["cmd"] != cmd]
    random.shuffle(all_cmds)
    distractors = all_cmds[:3]
    while len(distractors) < 3:
        distractors.append("rm -rf /")
        
    options = [
        f"A) {cmd}",
        f"B) {distractors[0]}",
        f"C) {distractors[1]}",
        f"D) {distractors[2]}"
    ]
    random.shuffle(options)
    
    correct_letter = "A"
    for opt in options:
        if opt.endswith(cmd):
            correct_letter = opt[0]
            break
            
    dist_analysis = ""
    for opt in options:
        letter = opt[0]
        if letter == correct_letter:
            dist_analysis += f"    * *Why {letter} is correct:* The `{cmd}` command is directly designed to {desc}.\n"
        else:
            dist_analysis += f"    * *Why {letter} is incorrect:* This command handles alternative administrative tasks.\n"
            
    return f"""**Question 3**
A systems administrator or developer needs to **{desc}**. Which of the following commands is the most appropriate to execute?
{options[0]}
{options[1]}
{options[2]}
{options[3]}
*   **Correct Answer:** {correct_letter}) {cmd}
*   **Distractor Analysis:**
{dist_analysis}"""

def generate_troubleshooting_question(domain, topic, cert):
    db = DOMAIN_DATABASE[domain]
    ts = random.choice(db["troubleshooting"])
    err = ts["err"]
    cause = ts["cause"]
    fix = ts["fix"]
    
    # Get distractors
    all_fixes = [t["fix"] for t in db["troubleshooting"] if t["fix"] != fix]
    random.shuffle(all_fixes)
    distractors = all_fixes[:3]
    while len(distractors) < 3:
        distractors.append("Reboot the physical machine and wait for services to reload.")
        
    options = [
        f"A) {fix}",
        f"B) {distractors[0]}",
        f"C) {distractors[1]}",
        f"D) {distractors[2]}"
    ]
    random.shuffle(options)
    
    correct_letter = "A"
    for opt in options:
        if opt.endswith(fix):
            correct_letter = opt[0]
            break
            
    dist_analysis = ""
    for opt in options:
        letter = opt[0]
        if letter == correct_letter:
            dist_analysis += f"    * *Why {letter} is correct:* Because {cause} The appropriate fix is to {fix}.\n"
        else:
            dist_analysis += f"    * *Why {letter} is incorrect:* This action does not resolve the root cause of {err}.\n"
            
    return f"""**Question 4**
While working on **{topic}** in a production environment, you encounter a system alert indicating a **{err}** error. Which of the following is the most effective troubleshooting action to resolve this issue?
{options[0]}
{options[1]}
{options[2]}
{options[3]}
*   **Correct Answer:** {correct_letter}) {fix}
*   **Distractor Analysis:**
{dist_analysis}"""

def generate_security_question(domain, topic, cert):
    db = DOMAIN_DATABASE[domain]
    sec = random.choice(db["security"])
    sec_topic = sec["topic"]
    risk = sec["risk"]
    fix = sec["fix"]
    
    # Get distractors
    all_fixes = [s["fix"] for s in db["security"] if s["fix"] != fix]
    random.shuffle(all_fixes)
    distractors = all_fixes[:3]
    while len(distractors) < 3:
        distractors.append("Enable full disk encryption on all client endpoints.")
        
    options = [
        f"A) {fix}",
        f"B) {distractors[0]}",
        f"C) {distractors[1]}",
        f"D) {distractors[2]}"
    ]
    random.shuffle(options)
    
    correct_letter = "A"
    for opt in options:
        if opt.endswith(fix):
            correct_letter = opt[0]
            break
            
    dist_analysis = ""
    for opt in options:
        letter = opt[0]
        if letter == correct_letter:
            dist_analysis += f"    * *Why {letter} is correct:* Implementing {fix} mitigates the risk of {risk}.\n"
        else:
            dist_analysis += f"    * *Why {letter} is incorrect:* This does not address the security vulnerability of {sec_topic}.\n"
            
    return f"""**Question 5**
When designing a system for **{topic}**, you must mitigate the risk of **{risk}**. Which of the following security configurations or controls represents the best practice to implement?
{options[0]}
{options[1]}
{options[2]}
{options[3]}
*   **Correct Answer:** {correct_letter}) {fix}
*   **Distractor Analysis:**
{dist_analysis}"""

# 4. Parsers for pre-existing courses
def parse_pre_existing_reading_guide(file_path):
    # Returns (topic, terms_list, defs_dict)
    topic = "Course Topic"
    terms = []
    defs_dict = {}
    if not os.path.exists(file_path):
        return topic, terms, defs_dict
        
    with open(file_path, "r", errors="ignore") as f:
        content = f.read()
        
    # Find topic name
    m_header = re.search(r"#\s*Reading\s*Guide:\s*Module\s*\d+\s*-\s*(.*)", content)
    if m_header:
        topic = m_header.group(1).strip()
        
    # Find numbered terms and definitions
    matches = re.findall(r"\d+\.\s+\*\*(.*?)(?::)?\*\*\s*(?::)?\s*(.*)", content)
    for term, definition in matches:
        t_clean = term.strip().rstrip(":")
        d_clean = definition.strip()
        if t_clean:
            terms.append(t_clean)
            defs_dict[t_clean] = d_clean
        
    # Fallback to bullets
    if not terms:
        matches = re.findall(r"\*\s+\*\*(.*?)(?::)?\*\*\s*(?::)?\s*(.*)", content)
        for term, definition in matches:
            t_clean = term.strip().rstrip(":")
            d_clean = definition.strip()
            if t_clean:
                terms.append(t_clean)
                defs_dict[t_clean] = d_clean
            
    return topic, terms, defs_dict

def parse_pre_existing_quiz(file_path):
    # Returns list of parsed questions
    if not os.path.exists(file_path):
        return []
        
    with open(file_path, "r", errors="ignore") as f:
        content = f.read()
        
    # Split by Question blocks
    q_blocks = re.split(r"\*\*Question\s*\d+\*\*", content)
    if len(q_blocks) <= 1:
        # Try split by Question or ### Question
        q_blocks = re.split(r"###\s*Question\s*\d+", content)
        
    parsed_questions = []
    for block in q_blocks[1:]:
        lines = [line.strip() for line in block.strip().split("\n") if line.strip()]
        if not lines:
            continue
        block_cleaned = block.strip()
        parsed_questions.append(block_cleaned)
        
    return parsed_questions

# 5. Core Generator Loop
print("=== STARTING COMPREHENSIVE CURRICULUM ENRICHMENT ===")

courses_count = 0
modules_count = 0

for course in sorted(os.listdir(BASE_DIR)):
    course_path = os.path.join(BASE_DIR, course)
    if not os.path.isdir(course_path):
        continue
        
    domain = get_course_domain(course)
    
    # Get course details
    cert = "IT Certification Prep"
    desc = "This course covers standard computer science and information technology modules."
    oer = "Official Vendor Documentation"
    
    # Check if course is in ENRICHED_COURSES
    is_pre_existing = True
    course_data = None
    if course in ENRICHED_COURSES:
        is_pre_existing = False
        course_data = ENRICHED_COURSES[course]
        cert = course_data.get("cert", cert)
        desc = course_data.get("desc", desc)
        oer = course_data.get("oer", oer)
    else:
        # Parse syllabus to get cert/desc if possible
        s_path = os.path.join(course_path, "00_Course_Information", "Syllabus.md")
        if os.path.exists(s_path):
            with open(s_path, "r", errors="ignore") as sf:
                s_content = sf.read()
                # Find cert
                m_cert = re.search(r"Course Syllabus:\s*(?:[A-Z0-9_-]+)\s*-\s*(.*)", s_content)
                if m_cert:
                    cert = m_cert.group(1).strip()
                # Find desc
                m_desc = re.search(r"## Course Overview\s*\n+\s*### Course Description\s*\n+(.*)", s_content)
                if m_desc:
                    desc = m_desc.group(1).strip()
                    
    print(f"Processing course: {course} (Domain: {domain}, Cert: {cert})")
    courses_count += 1
    
    # Rebuild ZTC OER Guide to ensure links are working
    ztc_path = os.path.join(course_path, "ZTC_OER_Reading_Materials.md")
    with open(ztc_path, "w") as zf:
        yt_q = cert
        if "Messer" in oer:
            yt_q = f"Professor Messer {cert}"
        encoded_yt = urllib.parse.quote_plus(yt_q)
        
        zf.write(f"""# Zero Textbook Cost (ZTC) & Open Educational Resources (OER) Guide
## Course: {course}

This course is designed as a Zero Textbook Cost (ZTC) curriculum. All core lecture notes, video scripts, lab activities, and practice quizzes are integrated directly within the Canvas LMS course shell.

---

## Recommended Free Study Resources & Links

To help you study and prepare for your examinations, we recommend the following free open-education resources:

1.  **Video Study Stream Lectures (Curated for {cert}):**
    *   [YouTube Search Link for {cert}](https://www.youtube.com/results?search_query={encoded_yt})
    *   *Tip:* Use this link to search for specific module topics as you progress through each week.

2.  **Official Vendor Documentation:**
    *   Refer to the official documentation websites matching this certification standard (such as Microsoft Learn, Google Cloud documentation, AWS documentation, or Linux man pages).

---

## Weekly Reading Guide Integration
Each module's `02_Reading_Guide_Module_XX.md` file contains a targeted checklist pointing you to these resources. Follow the checklists weekly to reinforce your learning before attempting the hands-on lab exercises and practice quizzes.
""")
        
    for mod in os.listdir(course_path):
        mod_path = os.path.join(course_path, mod)
        if not os.path.isdir(mod_path) or not mod.startswith("Module_"):
            continue
            
        week_num = mod[7:9]
        modules_count += 1
        
        topic = "Course Module"
        terms_list = []
        pre_existing_defs = {}
        original_questions = []
        lab_steps = []
        
        rg_file = os.path.join(mod_path, f"02_Reading_Guide_Module_{week_num}.md")
        qz_file = os.path.join(mod_path, f"04_Quiz_Module_{week_num}.md")
        lb_file = os.path.join(mod_path, f"03_Lab_Module_{week_num}.md")
        
        # 1. Gather module data
        if not is_pre_existing and course_data:
            week_idx = int(week_num) - 1
            if week_idx < len(course_data["weeks"]):
                w_data = course_data["weeks"][week_idx]
                topic = w_data["topic"]
                terms_list = [t.strip() for t in w_data["terms"].split(",") if t.strip()]
                lab_steps = w_data["lab"]
                # Build Question 1
                q1_opts = "\n".join([f"*   {o}" for o in w_data["opts"]])
                q1_dist = w_data.get("dist", "The other options represent alternative concepts that do not fit the specific conditions of the question.")
                q1_text = f"""**Question 1**
{w_data["q"]}
{q1_opts}
*   **Correct Answer:** {w_data["ans"]}) {w_data["expl"]}
*   **Distractor Analysis:**
    *   *Why correct:* {w_data["expl"]}
    *   {q1_dist}"""
                original_questions = [q1_text]
        else:
            # Parse from files on disk
            topic, terms_list, pre_existing_defs = parse_pre_existing_reading_guide(rg_file)
            original_questions = parse_pre_existing_quiz(qz_file)
            
            # Parse lab steps if available
            if os.path.exists(lb_file):
                with open(lb_file, "r", errors="ignore") as lf:
                    lb_content = lf.read()
                    lab_steps = re.findall(r"\d+\.\s+\*\*(.*?)\*\*", lb_content)
                    
        # Clean terms list
        terms_list = [t.strip() for t in terms_list if t.strip()]
        if not terms_list:
            terms_list = ["Core Operations", "Best Practices", "System Configuration"]
            
        # 2. Build the detailed reading guide introduction and body
        yt_search = f"{cert} {topic}"
        if "Messer" in oer:
            yt_search = f"Professor Messer {cert} {topic}"
        encoded_yt_mod = urllib.parse.quote_plus(yt_search)
        yt_link = f"https://www.youtube.com/results?search_query={encoded_yt_mod}"
        
        # Make a detailed introduction
        intro = f"""Welcome to **Module {week_num} - {topic}**! This week's study material focuses on the core foundations and configuration mechanics of **{topic}** as aligned with the **{cert}** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity."""
        
        # Build Glossary
        glossary_items = []
        for term in terms_list:
            term_clean = term.replace("`", "").replace("...", "").strip()
            definition = pre_existing_defs.get(term_clean)
            if not definition:
                definition = BASE_TERM_DEFS.get(term_clean)
            if not definition:
                definition = DOMAIN_DATABASE[domain]["concepts"].get(term_clean)
            if not definition:
                definition = f"A primary configuration standard and technical parameter essential for coordinating {topic} activities, enforcing security boundaries, and verifying operational statuses within the {domain} environment."
            glossary_items.append(f"*   **{term_clean}**: {definition}")
            
        glossary_str = "\n".join(glossary_items)
        
        # Build Lab notes
        lab_notes = ""
        if lab_steps:
            steps_desc = "\n".join([f"*   **{step}**: Configure and execute this validation step in your lab environment, verifying exit codes and logging output files." for step in lab_steps])
            lab_notes = f"""### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
{steps_desc}
"""
        else:
            lab_notes = f"""### Lab & Command Integration
In this week's hands-on lab, you will run command sequences to verify configuration files and check service statuses. Make sure to execute administrative commands using elevated privileges (sudo/Administrator) and review console outputs for errors.
"""
            
        # Build Reading Guide Markdown
        rg_content = f"""# Reading Guide: Module {week_num} - {topic}
## Course: {course} ({cert})

---

### Introduction
{intro}

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

{glossary_str}

---

### 2. Certification Exam Tips
*   **Focus Area:** Pay close attention to how these configurations behave by default. The exam frequently features questions on default ports, configuration file paths, and diagnostic console commands.
*   **Scenario Trap:** Watch out for questions asking you to troubleshoot a failing service. Always verify if basic network connectivity, local port conflicts, or permissions are violated first.
*   **Study Resource:** To reinforce these concepts visually, review this targeted search query: [YouTube Exam Study Reference Link]({yt_link}).

---

{lab_notes}

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Watch the curated YouTube study streams matching **{topic}**.
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
"""
        
        with open(rg_file, "w") as rgf:
            rgf.write(rg_content)
            
        # 3. Build the 5-question quiz
        q1_text = ""
        q2_text = ""
        
        if len(original_questions) >= 1:
            q1_text = original_questions[0].strip()
            q1_text = re.sub(r"^(?:###\s*)?\*\*Question\s*\d+\*\*|^(?:###\s*)?Question\s*\d+", "", q1_text).strip()
            q1_text = f"**Question 1**\n{q1_text}"
            
        if len(original_questions) >= 2:
            q2_text = original_questions[1].strip()
            q2_text = re.sub(r"^(?:###\s*)?\*\*Question\s*\d+\*\*|^(?:###\s*)?Question\s*\d+", "", q2_text).strip()
            q2_text = f"**Question 2**\n{q2_text}"
            
        # Generate missing questions
        q_list = []
        
        if q1_text:
            q_list.append(q1_text)
        else:
            q_list.append(generate_term_question(domain, terms_list, cert))
            
        if q2_text:
            q_list.append(q2_text)
        else:
            q_list.append(generate_term_question(domain, [t for t in terms_list if t not in q1_text], cert))
            
        q_list.append(generate_command_question(domain, cert))
        q_list.append(generate_troubleshooting_question(domain, topic, cert))
        q_list.append(generate_security_question(domain, topic, cert))
        
        quiz_content = f"""# Quiz: Module {week_num} - {topic}
## Course: {course} ({cert})

---

{q_list[0]}

---

{q_list[1]}

---

{q_list[2]}

---

{q_list[3]}

---

{q_list[4]}
"""
        
        with open(qz_file, "w") as qzf:
            qzf.write(quiz_content)

print(f"=== COMPLETED COMPREHENSIVE CURRICULUM ENRICHMENT ===")
print(f"Total Courses processed: {courses_count}")
print(f"Total Modules processed: {modules_count}")
