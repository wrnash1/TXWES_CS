#!/usr/bin/env python3
import os
import shutil

BASE_DIR = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"

COURSES_DATA = {
    "CIS-1310_Intro_to_Python": {
        "cert": "PCAP (Certified Associate in Python Programming)",
        "desc": "Introduction to Python programming, variables, control flow, loops, functions, data structures, and Object-Oriented Programming (OOP).",
        "oer": "Python Institute Free Training (edube.org)",
        "weeks": [
            {
                "topic": "Python Basics & Local Environment",
                "terms": "Interpreted vs Compiled execution, interactive shell (REPL), script mode, indentation rules.",
                "lab": ["Check python version: `python3 --version`", "Start interactive REPL: `python3`", "Execute `print('Hello World')`", "Create `test.py` with print statement and run: `python3 test.py`"],
                "q": "What is Python's execution model?",
                "opts": ["A) Compiled before running", "B) Interpreted line-by-line", "C) Assembled to machine code", "D) None of the above"],
                "ans": "B",
                "expl": "Python is executed by an interpreter that reads and processes code line-by-line.",
                "dist": "Compiled languages compile source code all at once. Python reads and executes code dynamically."
            },
            {
                "topic": "Literals, Operators, and Expressions",
                "terms": "Data types (int, float, string, boolean), arithmetic operators, precedence and associativity.",
                "lab": ["Write a script to compute area of a circle", "Experiment with integer division `//` and modulo `%`", "Examine operator precedence rules: print(2 + 3 * 4)"],
                "q": "What is the result of `print(11 // 3)` in Python?",
                "opts": ["A) 3.666", "B) 3", "C) 2", "D) 4"],
                "ans": "B",
                "expl": "The double slash `//` operator performs floor division, rounding down to the nearest integer.",
                "dist": "A is the result of single slash `/`. C is the remainder from modulo `%`."
            },
            {
                "topic": "Variables and Basic I/O",
                "terms": "Variable naming rules, dynamic typing, `input()` function, type casting (int, float, str).",
                "lab": ["Write a script to prompt the user for their name and age", "Convert age from string to integer using `int()`", "Output a formatted string: f'Hello {name}, you are {age} years old'"],
                "q": "What is the return type of the `input()` function?",
                "opts": ["A) int", "B) float", "C) string", "D) boolean"],
                "ans": "C",
                "expl": "`input()` always returns a string. You must explicitly cast it if you need a numeric value.",
                "dist": "Dynamic typing does not automatically convert text input to integers or floats."
            },
            {
                "topic": "Control Flow - Conditional Statements",
                "terms": "Boolean algebra, relational operators, if-elif-else syntax, nested conditionals.",
                "lab": ["Write a program that takes a score (0-100) and prints the letter grade", "Use if-elif-else statements to check grade boundaries", "Handle invalid inputs (greater than 100 or less than 0)"],
                "q": "Which keyword is used to represent 'else if' in Python?",
                "opts": ["A) elseif", "B) else if", "C) elif", "D) otherwise"],
                "ans": "C",
                "expl": "Python uses `elif` as the syntax-defined keyword for secondary conditional branches.",
                "dist": "elseif and else if are syntax errors in Python. otherwise is not a Python keyword."
            },
            {
                "topic": "Loops - Iteration with While and For",
                "terms": "While loop condition, for loops over ranges, loop control statements (break, continue).",
                "lab": ["Write a while loop that runs until user enters 'quit'", "Write a for loop that calculates sum of numbers from 1 to 100", "Use `continue` to skip odd numbers in a loop"],
                "q": "What does the `break` statement do inside a loop?",
                "opts": ["A) Skips the current iteration", "B) Terminates the loop immediately", "C) Restarts the loop", "D) Exits the entire program"],
                "ans": "B",
                "expl": "The `break` statement exits the innermost loop immediately, bypassing any remaining iterations.",
                "dist": "A describes the `continue` statement. D describes `exit()` or `sys.exit()`."
            },
            {
                "topic": "Bitwise Operations and Lists",
                "terms": "Bitwise AND, OR, XOR, shifts, Python lists, indexing, slicing, mutability.",
                "lab": ["Create a list of 5 colors", "Access colors using positive and negative indices", "Modify the third color", "Perform slicing `colors[1:4]` and print results"],
                "q": "How do you access the last element of a list named `my_list`?",
                "opts": ["A) my_list[0]", "B) my_list[len(my_list)]", "C) my_list[-1]", "D) my_list[last]"],
                "ans": "C",
                "expl": "Negative indexing starts from the end of the list. `my_list[-1]` retrieves the last element.",
                "dist": "A is the first element. B causes an IndexError because indices are 0-indexed. D is undefined."
            },
            {
                "topic": "Advanced List Operations",
                "terms": "List methods (append, insert, remove, pop), list sorting, list copying vs referencing.",
                "lab": ["Write a script to manage a shopping list using append() and pop()", "Sort the list alphabetically", "Demonstrate the difference between list copy `list.copy()` and reference assignment"],
                "q": "Which method adds an item to the end of a Python list?",
                "opts": ["A) add()", "B) append()", "C) push()", "D) insert()"],
                "ans": "B",
                "expl": "The `.append()` method inserts the passed element at the end of the list.",
                "dist": "add() is for sets. push() is not a list method. insert() requires a specific index."
            },
            {
                "topic": "Functions and Parameter Passing",
                "terms": "Function definition (`def`), positional vs keyword arguments, default parameters, return statement.",
                "lab": ["Create a function `calculate_bmi(weight, height)`", "Return calculated BMI value", "Call the function using both positional and keyword arguments"],
                "q": "How are multiple values returned from a Python function?",
                "opts": ["A) Using multiple return statements", "B) Returned as a tuple", "C) Python functions can only return one value", "D) Using the yield keyword"],
                "ans": "B",
                "expl": "Returning multiple items separated by commas in Python automatically packages them into a tuple.",
                "dist": "A is invalid (execution stops at first return). yield makes it a generator, not a standard function return."
            },
            {
                "topic": "Scopes, Namespaces, and Recursion",
                "terms": "Global vs local scope, `global` keyword, recursive functions, call stack and recursion limits.",
                "lab": ["Write a recursive function to calculate factorial of a number", "Demonstrate local scope variable shadow", "Modify a global variable from inside a function using `global`"],
                "q": "What keyword is required to modify a variable defined at the module level from inside a function?",
                "opts": ["A) nonlocal", "B) global", "C) static", "D) public"],
                "ans": "B",
                "expl": "The `global` keyword declares that a variable inside the function refers to the module-level namespace.",
                "dist": "nonlocal is for nested/closure scopes. static and public are not used in Python variable scoping."
            },
            {
                "topic": "Tuples and Dictionaries",
                "terms": "Tuple immutability, key-value pairs in dictionaries, dictionary methods, iterating over dicts.",
                "lab": ["Create a dictionary storing student names and grades", "Retrieve grades using student names", "Iterate through keys and values using `.items()`", "Verify tuples cannot be modified"],
                "q": "Which dictionary method returns both keys and values as tuples?",
                "opts": ["A) keys()", "B) values()", "C) items()", "D) get()"],
                "ans": "C",
                "expl": "The `.items()` method returns a view object containing key-value tuples.",
                "dist": "keys() only returns keys. values() only returns values. get() returns the value of a specific key."
            },
            {
                "topic": "String Methods and Operations",
                "terms": "String immutability, string slicing, string functions (upper, lower, find, split, join, strip).",
                "lab": ["Take a user input string and clean it up (remove whitespace)", "Split it into words based on spaces", "Join the words back together using a hyphen `-` separator"],
                "q": "What is the output of `'python'.upper()`?",
                "opts": ["A) Python", "B) PYTHON", "C) python", "D) TypeError"],
                "ans": "B",
                "expl": "The `.upper()` method returns a new string with all lowercase characters converted to uppercase.",
                "dist": "Strings are immutable, but methods return new strings instead of modifying them in-place."
            },
            {
                "topic": "Exception Handling",
                "terms": "Try-except blocks, handling multiple exception types, `else` and `finally` clauses, raising exceptions.",
                "lab": ["Write a script that takes numbers from user and handles ValueError", "Use try-except-finally to ensure database or file connection is closed", "Raise a custom ValueError if negative values are input"],
                "q": "Which block runs regardless of whether an exception was raised or not?",
                "opts": ["A) except", "B) else", "C) finally", "D) try"],
                "ans": "C",
                "expl": "The `finally` block is guaranteed to execute at the end of the try-except chain, making it perfect for cleanup.",
                "dist": "except only runs if an exception occurs. else only runs if no exception occurs."
            },
            {
                "topic": "Modules and Packages",
                "terms": "Importing modules, namespaces (`import math` vs `from math import *`), `sys.path`, creating custom modules.",
                "lab": ["Import `math` and use `math.sqrt()`", "Create a custom helper module `mymath.py`", "Import and test functions from `mymath.py` in a separate script"],
                "q": "What does `import math` do?",
                "opts": ["A) Copies math functions directly into your file", "B) Imports the math module namespace", "C) Exposes all functions without the math prefix", "D) Compiles the math module"],
                "ans": "B",
                "expl": "It imports the module, keeping its functions under the `math.` namespace to avoid name collisions.",
                "dist": "from math import * exposes functions without prefix, which can overwrite existing names."
            },
            {
                "topic": "Object-Oriented Programming (OOP) Basics",
                "terms": "Classes and objects, constructors (`__init__`), instance variables vs class variables, methods.",
                "lab": ["Define a class `Student` with attributes name and grade", "Create multiple instances of the class", "Implement a method to print student details"],
                "q": "What is the purpose of the `self` parameter in Python class methods?",
                "opts": ["A) It represents the class definition", "B) It refers to the specific object instance", "C) It is a global variable", "D) It is a keyword that cannot be renamed"],
                "ans": "B",
                "expl": "`self` represents the specific instance of the object being operated on, allowing access to instance attributes.",
                "dist": "It represents the instance, not the class. Technically it is a naming convention, not a reserved keyword."
            },
            {
                "topic": "Advanced OOP: Inheritance and Polymorphism",
                "terms": "Single and multiple inheritance, method overriding, super() function, checking types.",
                "lab": ["Create a base class `Vehicle` and subclass `Car`", "Override a method `start_engine` in `Car`", "Use `super().__init__()` to inherit initialization attributes"],
                "q": "How do you call a method in the parent class from a child class?",
                "opts": ["A) parent.method()", "B) super().method()", "C) base.method()", "D) self.method()"],
                "ans": "B",
                "expl": "The `super()` function returns a proxy object that delegates method calls to a parent or sibling class.",
                "dist": "parent and base are not built-in functions or keywords for resolving parent class references."
            }
        ]
    },
    "CIS-2320_Hardware_Fund": {
        "cert": "CompTIA A+",
        "desc": "Introduction to PC hardware components, motherboard form factors, CPUs, storage devices, networks, and mobile connectivity.",
        "oer": "Professor Messer A+ Course (professormesser.com)",
        "weeks": [
            {
                "topic": "Introduction to PC Hardware & Safety",
                "terms": "ESD protection, grounding, safety guidelines, core internal components overview.",
                "lab": ["Identify safety risks in an opened PC case", "Equip an ESD strap and locate grounding points", "Locate internal components: PSU, Motherboard, RAM, CPU"],
                "q": "What is the primary danger when working inside a computer case without ESD safety?",
                "opts": ["A) Electric shock to the user", "B) Electrostatic discharge damaging components", "C) Setting the case on fire", "D) Damaging the hard drive platter"],
                "ans": "B",
                "expl": "ESD can ruin integrated circuits without the user even noticing a spark.",
                "dist": "PSUs store charge, but normal components pose ESD risk to the PC, not electrical shock to the user."
            },
            {
                "topic": "Motherboards and Form Factors",
                "terms": "ATX, Micro-ATX, Mini-ITX form factors, chipsets, expansion slots (PCIe).",
                "lab": ["Compare ATX vs Mini-ITX dimensions", "Identify PCIe x1, x4, and x16 slots on a board", "Locate BIOS/UEFI CMOS battery and jumper pins"],
                "q": "Which form factor is typically used for compact, small-form-factor home theatre PCs?",
                "opts": ["A) ATX", "B) Micro-ATX", "C) Mini-ITX", "D) BTX"],
                "ans": "C",
                "expl": "Mini-ITX motherboard dimensions (6.7 x 6.7 inches) make it perfect for compact devices.",
                "dist": "ATX is full size. Micro-ATX is medium. BTX is an outdated form factor."
            },
            {
                "topic": "Processors (CPUs) and Cooling",
                "terms": "Intel vs AMD socket types, CPU architecture (cores, threads), thermal paste, heat sinks.",
                "lab": ["Install a simulator CPU into LGA or PGA socket", "Apply thermal paste using the 'pea-size' method", "Secure heat sink and connect 4-pin CPU fan header"],
                "q": "Which CPU socket type features pins located on the motherboard rather than the processor itself?",
                "opts": ["A) PGA", "B) LGA", "C) BGA", "D) DIP"],
                "ans": "B",
                "expl": "Land Grid Array (LGA) has pins on the socket. Pin Grid Array (PGA) has pins on the CPU.",
                "dist": "BGA is soldered. DIP is an old integrated circuit package format."
            },
            {
                "topic": "Memory (RAM) Types and Configuration",
                "terms": "DDR3 vs DDR4 vs DDR5 pin counts, SODIMM vs DIMM, dual-channel configuration.",
                "lab": ["Identify slot positions for dual-channel operations (A1/B1)", "Install a DIMM module ensuring locking clips snap shut", "Locate laptop SODIMM memory slots"],
                "q": "Which RAM type is specifically designed for space-constrained laptops and thin clients?",
                "opts": ["A) DIMM", "B) SODIMM", "C) SDRAM", "D) GDDR"],
                "ans": "B",
                "expl": "Small Outline Dual Inline Memory Module (SODIMM) is the standard compact form factor for laptop RAM.",
                "dist": "DIMM is for desktop. GDDR is graphics RAM. SDRAM is the general class of synchronous RAM."
            },
            {
                "topic": "Storage Devices",
                "terms": "HDD vs SATA SSD vs M.2 NVMe, drive form factors (3.5, 2.5), RAID levels (0, 1, 5, 10).",
                "lab": ["Connect a 2.5-inch SATA SSD with power and data cables", "Install an M.2 NVMe drive into PCIe slot and secure it", "Set up a RAID 1 mirror using motherboard BIOS utility"],
                "q": "Which RAID level provides data striping without parity or redundancy?",
                "opts": ["A) RAID 0", "B) RAID 1", "C) RAID 5", "D) RAID 10"],
                "ans": "A",
                "expl": "RAID 0 stripes data for performance but offers zero fault tolerance.",
                "dist": "RAID 1 is mirroring. RAID 5 uses parity. RAID 10 is striped mirrors."
            },
            {
                "topic": "Power Supplies and System Cooling",
                "terms": "PSU wattage, efficiency ratings (80 Plus), modular vs non-modular, case airflow (intake vs exhaust).",
                "lab": ["Calculate system power requirements based on CPU and GPU draw", "Connect 24-pin main motherboard connector", "Examine fan orientations for optimal case airflow"],
                "q": "What standard power connector is used to supply direct auxiliary power to high-end PCIe graphics cards?",
                "opts": ["A) 24-pin ATX", "B) SATA Power", "C) 6-pin or 8-pin PCIe", "D) 4-pin Molex"],
                "ans": "C",
                "expl": "PCIe graphics cards use 6-pin or 8-pin auxiliary cables to draw up to 150W of power.",
                "dist": "24-pin is for motherboard. SATA is for storage. Molex is for legacy accessories."
            },
            {
                "topic": "Display Technologies and Connectors",
                "terms": "OLED vs LCD (IPS, TN, VA), HDMI vs DisplayPort vs DVI, resolution and refresh rates.",
                "lab": ["Configure dual-monitor setup using display settings", "Identify pins and keyings of DisplayPort vs HDMI cables", "Switch display input settings on physical monitor"],
                "q": "Which display connector supports daisy-chaining multiple monitors together from a single source output?",
                "opts": ["A) HDMI", "B) DisplayPort", "C) VGA", "D) DVI"],
                "ans": "B",
                "expl": "DisplayPort supports Multi-Stream Transport (MST), enabling monitor daisy-chaining.",
                "dist": "HDMI does not natively support daisy-chaining. VGA and DVI are legacy interfaces."
            },
            {
                "topic": "Custom PC Configurations",
                "terms": "Component selection for CAD workstations, virtualization hosts, gaming PCs, and NAS/Home servers.",
                "lab": ["Build a bill-of-materials for a virtualization host prioritizing RAM and CPU cores", "Select appropriate GPU and cooling for a gaming system", "Determine storage redundancy requirements for NAS"],
                "q": "What is the most critical hardware component when designing a virtualization workstation?",
                "opts": ["A) High-end GPU", "B) Fast mechanical HDD", "C) Maximum CPU cores and RAM", "D) Liquid nitrogen cooling"],
                "ans": "C",
                "expl": "Virtual machines run concurrently and consume logical cores and physical RAM allocations directly.",
                "dist": "Virtualization hosts do not require heavy 3D rendering GPUs or slow hard drives."
            },
            {
                "topic": "Peripheral Devices and Interfaces",
                "terms": "USB standards (2.0, 3.0, Type-C), Thunderbolt, KVM switches, smart card readers, biometric scanners.",
                "lab": ["Configure a USB 3.0 external drive for fast transfer rates", "Set up a KVM switch to share one monitor/keyboard between two machines", "Install drivers for biometric login scanner"],
                "q": "What is the maximum data transfer speed of USB 3.0 (SuperSpeed)?",
                "opts": ["A) 480 Mbps", "B) 5 Gbps", "C) 10 Gbps", "D) 40 Gbps"],
                "ans": "B",
                "expl": "USB 3.0 operates at a maximum of 5 Gbps.",
                "dist": "480 Mbps is USB 2.0. 10 Gbps is USB 3.1 Gen 2. 40 Gbps is Thunderbolt 3/4."
            },
            {
                "topic": "Troubleshooting Boot Issues",
                "terms": "POST errors, beep codes, BSOD/Kernel Panic, Boot order configuration in BIOS/UEFI.",
                "lab": ["Diagnose a boot failure caused by incorrect RAM seating", "Identify motherboard beep code for missing video card", "Modify boot sequence in UEFI settings to prioritize USB drive"],
                "q": "What does a blank screen with continuous short beeps during startup typically indicate?",
                "opts": ["A) OS is corrupted", "B) POST has failed (typically due to RAM or motherboard issue)", "C) The monitor is unplugged", "D) Keyboard is disconnected"],
                "ans": "B",
                "expl": "Beep codes are diagnostic indicators emitted by the BIOS/UEFI during POST failures.",
                "dist": "Syllabus details: OS corruption occurs after POST. Screen is blank because POST did not complete."
            },
            {
                "topic": "Network Hardware & Connectors",
                "terms": "Cat5e vs Cat6 vs Cat6a, RJ-45 vs RJ-11, fiber optic connections (ST, SC, LC), T568A vs T568B pinouts.",
                "lab": ["Examine copper pairs in an Ethernet cable", "Trace fiber optic LC connectors", "Create a straight-through patch cable using RJ-45 crimper"],
                "q": "Which category of copper cable supports 10 Gbps speeds at a maximum distance of 100 meters?",
                "opts": ["A) Cat5", "B) Cat5e", "C) Cat6", "D) Cat6a"],
                "ans": "D",
                "expl": "Cat6a supports 10 Gbps up to 100m. Cat6 supports 10 Gbps only up to 55m.",
                "dist": "Cat5 is 100 Mbps. Cat5e is 1 Gbps."
            },
            {
                "topic": "Network Infrastructure Devices",
                "terms": "Switches vs Routers, WAPs, firewalls, modems, patch panels, PoE (Power over Ethernet).",
                "lab": ["Identify switch ports vs router WAN interfaces", "Configure a wireless access point SSID and channel", "Plug in a VoIP phone using a PoE port on a switch"],
                "q": "Which device directs traffic between different IP subnetworks based on Layer 3 logical addresses?",
                "opts": ["A) Switch", "B) Hub", "C) Router", "D) Access Point"],
                "ans": "C",
                "expl": "Routers operate at Layer 3 of the OSI model and route packets between different networks.",
                "dist": "Switches operate at Layer 2 using MAC addresses. Hubs repeat traffic to all ports."
            },
            {
                "topic": "Laptop Components and Disassembly",
                "terms": "Laptop keyboard, battery, Wi-Fi card, LCD screen replacement, power jacks.",
                "lab": ["Remove laptop battery safely", "Locate and detach laptop mini-PCIe Wi-Fi card and antenna cables", "Swap laptop keyboard module"],
                "q": "Why must you carefully disconnect laptop antenna wires when swapping a Wi-Fi card?",
                "opts": ["A) The card will catch fire if wires cross", "B) They supply power to the LCD backlight", "C) They are fragile coax connections required for wireless reception", "D) Wires are soldered and cannot be removed"],
                "ans": "C",
                "expl": "Antenna wires carry the radio signals from the LCD bezel and are attached via tiny, fragile snap-on connector pins.",
                "dist": "Antenna wires carry RF signals, not electrical power, and do not pose fire hazards."
            },
            {
                "topic": "Mobile Device Connectivity",
                "terms": "Bluetooth pairing, cellular data (5G, LTE), Wi-Fi profiling, USB syncing, email server settings.",
                "lab": ["Configure a mobile device email account using IMAP and SSL", "Pair a Bluetooth headset with a smartphone", "Set up a mobile hotspot"],
                "q": "Which port is standard for securing incoming IMAP email traffic?",
                "opts": ["A) Port 25", "B) Port 110", "C) Port 993", "D) Port 443"],
                "ans": "C",
                "expl": "IMAP over SSL/TLS uses TCP port 993.",
                "dist": "Port 25 is SMTP. Port 110 is unsecure POP3. Port 443 is HTTPS."
            },
            {
                "topic": "Printers and Imaging",
                "terms": "Laser printing process (EP), inkjet maintenance, thermal paper, 3D printing.",
                "lab": ["Replace toner cartridge in a laser printer", "Clean ink nozzles using software maintenance utility", "Configure network print queue sharing"],
                "q": "What is the correct sequence of steps in the laser printing process?",
                "opts": ["A) Charging, Exposing, Developing, Transferring, Fusing, Cleaning", "B) Exposing, Charging, Transferring, Fusing, Cleaning, Developing", "C) Developing, Exposing, Charging, Transferring, Fusing, Cleaning", "D) Cleaning, Charging, Exposing, Developing, Transferring, Fusing"],
                "ans": "D",
                "expl": "The standard sequence is: Cleaning, Charging, Exposing (writing), Developing, Transferring, Fusing.",
                "dist": "The other sequences place writing or cleaning out of order."
            }
        ]
    },
    "CIS-3322_Advanced_Networking": {
        "cert": "Cisco CCNA (200-301)",
        "desc": "Advanced routing, switching, spanning tree, link aggregation, inter-VLAN routing, and network automation configurations.",
        "oer": "Cisco Networking Academy (netacad.com)",
        "weeks": [
            {
                "topic": "Network Architectures & Topologies",
                "terms": "Three-tier architecture (Core, Distribution, Access), Collapsed Core design, spine-leaf topologies.",
                "lab": ["Draw a three-tier network diagram in Packet Tracer", "Examine routing links at Distribution layer", "Verify VLAN assignments at Access layer switches"],
                "q": "In a three-tier enterprise design, at which layer is routing and policy-based traffic control typically implemented?",
                "opts": ["A) Access Layer", "B) Distribution Layer", "C) Core Layer", "D) Physical Layer"],
                "ans": "B",
                "expl": "The Distribution Layer aggregates access switches, enforces policies (ACLs), and handles routing.",
                "dist": "Access layer connects endpoints. Core layer is designed for high-speed packet forwarding."
            },
            {
                "topic": "Subnetting and VLSM Configurations",
                "terms": "Variable Length Subnet Masking (VLSM), IP allocation strategies, CIDR prefix matching.",
                "lab": ["Subnet a class C network /24 into multiple /27 and /28 subnets", "Assign IP addresses to router interfaces", "Verify ping connectivity between subnets"],
                "q": "How many usable host IP addresses are available in a `/28` subnet mask?",
                "opts": ["A) 16", "B) 14", "C) 30", "D) 6"],
                "ans": "B",
                "expl": "A `/28` mask has 4 host bits (32-28 = 4). 2^4 = 16. Subtracting network and broadcast addresses leaves 14.",
                "dist": "16 is total addresses. 30 is for `/27`. 6 is for `/29`."
            },
            {
                "topic": "IPv6 Addressing and Configuration",
                "terms": "IPv6 link-local vs global unicast, SLAAC, EUI-64 configuration, static routing in IPv6.",
                "lab": ["Enable IPv6 routing globally: `ipv6 unicast-routing`", "Configure interface with IPv6: `ipv6 address 2001:db8::1/64`", "Verify IPv6 neighbor discovery tables"],
                "q": "What command enables a Cisco router to forward IPv6 traffic?",
                "opts": ["A) ip routing", "B) ipv6 address autoconfig", "C) ipv6 unicast-routing", "D) ipv6 routing enable"],
                "ans": "C",
                "expl": "Cisco routers require the global command `ipv6 unicast-routing` to act as an IPv6 router.",
                "dist": "ip routing is for IPv4. autoconfig sets up client address learning. routing enable is invalid syntax."
            },
            {
                "topic": "Switching Concepts & VLANs",
                "terms": "VLAN membership, trunking protocols (802.1Q), Native VLAN, DTP (Dynamic Trunking Protocol).",
                "lab": ["Create VLAN 10 and 20: `vlan 10`", "Assign ports to VLAN: `switchport access vlan 10`", "Configure trunk link: `switchport mode trunk`"],
                "q": "Which frame tagging standard is used to carry traffic for multiple VLANs over a single physical switchport connection?",
                "opts": ["A) ISL", "B) 802.11", "C) 802.1Q", "D) LACP"],
                "ans": "C",
                "expl": "IEEE 802.1Q is the industry-standard frame-tagging protocol for VLAN trunks.",
                "dist": "ISL is Cisco legacy. 802.11 is Wi-Fi. LACP is for EtherChannel."
            },
            {
                "topic": "Spanning Tree Protocol (STP & RSTP)",
                "terms": "Root bridge election, port roles (Root, Designated, Blocked), 802.1D vs 802.1w (RSTP).",
                "lab": ["Inspect STP status: `show spanning-tree`", "Force root bridge election: `spanning-tree vlan 1 root primary`", "Configure PortFast on edge ports"],
                "q": "Which criteria is analyzed FIRST during the Root Bridge election process in Spanning Tree?",
                "opts": ["A) System MAC Address", "B) Port Priority", "C) Bridge Priority Value", "D) Link Speed"],
                "ans": "C",
                "expl": "STP elects the bridge with the lowest Bridge ID (BID), which begins with the Bridge Priority.",
                "dist": "MAC address is used as a tie-breaker if priorities are equal."
            },
            {
                "topic": "EtherChannel Link Aggregation",
                "terms": "LACP vs PAgP, port channel configuration, load balancing algorithms.",
                "lab": ["Configure ports for active negotiation: `channel-group 1 mode active`", "Verify port-channel interface state: `show etherchannel summary`", "Configure EtherChannel load-balancing method"],
                "q": "Which protocol is the open standard for dynamically negotiating EtherChannel links?",
                "opts": ["A) PAgP", "B) LACP", "C) RSTP", "D) VTP"],
                "ans": "B",
                "expl": "Link Aggregation Control Protocol (LACP) is the open-standard (IEEE 802.3ad) link aggregation protocol.",
                "dist": "PAgP is Cisco-proprietary. RSTP is spanning tree. VTP propagates VLANs."
            },
            {
                "topic": "Inter-VLAN Routing Solutions",
                "terms": "Router-on-a-stick, subinterfaces, Layer 3 Switch SVI configuration.",
                "lab": ["Configure router subinterface: `interface g0/0.10`", "Set encapsulation: `encapsulation dot1Q 10`", "Configure IP address on SVI on L3 Switch: `interface vlan 10`"],
                "q": "In a Router-on-a-stick topology, how are multiple VLANs terminated on a single physical router interface?",
                "opts": ["A) Using multiple IP addresses on the primary interface", "B) Creating logical subinterfaces for each VLAN", "C) Plugging in multiple network cables", "D) Enabling PortFast on the router link"],
                "ans": "B",
                "expl": "Subinterfaces allow partition of a physical interface into multiple virtual interfaces, each handling a VLAN.",
                "dist": "A is invalid (only one primary IP). C defeats the purpose of the single trunk link."
            },
            {
                "topic": "OSPFv2 Routing Concepts & Setup",
                "terms": "OSPF states, link-state advertisement, area boundaries, wild-card masks.",
                "lab": ["Configure OSPF instance: `router ospf 1`", "Publish subnet to area 0: `network 10.0.0.0 0.0.0.3 area 0`", "Verify neighbors: `show ip ospf neighbor`"],
                "q": "What wildcard mask corresponds to a standard subnet mask of `255.255.255.252`?",
                "opts": ["A) 0.0.0.3", "B) 0.0.0.255", "C) 255.255.255.255", "D) 0.0.0.7"],
                "ans": "A",
                "expl": "Subtracting `255.255.255.252` from `255.255.255.255` yields wildcard `0.0.0.3`.",
                "dist": "0.0.0.255 is for /24. 0.0.0.7 is for /29."
            },
            {
                "topic": "WAN Technologies & VPNs",
                "terms": "Metro Ethernet, Site-to-Site VPNs, GRE tunnels, IPsec framework components.",
                "lab": ["Configure a generic routing encapsulation (GRE) tunnel interface", "Set tunnel source and destination IPs", "Test routing protocols across the tunnel"],
                "q": "Which IPsec component provides data integrity and origin authentication without confidentiality (encryption)?",
                "opts": ["A) ESP", "B) AH", "C) IKE", "D) Diffie-Hellman"],
                "ans": "B",
                "expl": "Authentication Header (AH) handles authentication and integrity. Encapsulating Security Payload (ESP) handles encryption.",
                "dist": "ESP provides encryption. IKE negotiates keys."
            },
            {
                "topic": "Access Control Lists (ACLs)",
                "terms": "Standard vs Extended ACLs, numbering schemes, wildcard filtering, implicit deny.",
                "lab": ["Create extended ACL: `access-list 101 permit tcp any host 10.1.1.5 eq 80`", "Apply ACL to interface: `ip access-group 101 in`", "Verify matches: `show access-lists`"],
                "q": "Where should a standard access control list typically be applied?",
                "opts": ["A) As close to the source as possible", "B) As close to the destination as possible", "C) On the core router only", "D) On the internet gateway"],
                "ans": "B",
                "expl": "Standard ACLs filter traffic based only on source IP, so applying them near the destination prevents blocking good traffic.",
                "dist": "Extended ACLs should be applied as close to the source as possible."
            },
            {
                "topic": "NAT and PAT Configurations",
                "terms": "Static vs Dynamic NAT, Port Address Translation (PAT) / Overload, inside local/global definitions.",
                "lab": ["Configure NAT pool: `ip nat pool ...`", "Map inside list to interface with overload: `ip nat inside source list 1 interface g0/0 overload`", "Verify mappings: `show ip nat translations`"],
                "q": "Which NAT terminology describes the public IP address of an inside host as seen by external devices on the internet?",
                "opts": ["A) Inside Local", "B) Inside Global", "C) Outside Local", "D) Outside Global"],
                "ans": "B",
                "expl": "Inside Global is the public address mapped to the internal host's Inside Local private address.",
                "dist": "Inside Local is the private IP. Outside Global is the target public IP."
            },
            {
                "topic": "Wireless LANs (WLAN) & WLC",
                "terms": "Wireless architectures (autonomous vs lightweight APs), WLC configuration, SSID deployment, WPA2 vs WPA3.",
                "lab": ["Configure a lightweight WAP profile on a Cisco Wireless LAN Controller (WLC)", "Set up a secure SSID with WPA2-Enterprise", "Verify client association"],
                "q": "Which protocol is used by lightweight access points to communicate with a central Wireless LAN Controller?",
                "opts": ["A) LACP", "B) CAPWAP", "C) SNMP", "D) 802.1Q"],
                "ans": "B",
                "expl": "Control and Provisioning of Wireless Access Points (CAPWAP) encapsulates AP-to-WLC management and data traffic.",
                "dist": "LACP is link aggregation. SNMP is management. 802.1Q is trunking."
            },
            {
                "topic": "Quality of Service (QoS) Fundamentals",
                "terms": "Traffic classification and marking (CoS, DSCP), queuing mechanisms (FIFO, WFQ), congestion avoidance.",
                "lab": ["Configure a class-map to match VoIP traffic", "Define a policy-map prioritizing Voip to high priority queue", "Apply policy-map to interface: `service-policy output QoS-Policy`"],
                "q": "Which Layer 3 marking field in the IP header is used for configuring Quality of Service (QoS)?",
                "opts": ["A) Class of Service (CoS)", "B) Differentiated Services Code Point (DSCP)", "C) MAC Priority", "D) VLAN Tag"],
                "ans": "B",
                "expl": "DSCP uses 6 bits in the Type of Service (ToS) field of the IPv4 header (Layer 3) to mark packets.",
                "dist": "CoS is a Layer 2 marking found inside 802.1Q tags."
            },
            {
                "topic": "Network Automation & REST APIs",
                "terms": "SDN controller architecture, northbound vs southbound APIs, JSON/XML data formats.",
                "lab": ["Parse a JSON payload using Python dictionary structures", "Send a mock REST API request using `curl`", "Verify Cisco DNA Center API return values"],
                "q": "In a Software-Defined Networking architecture, which API is used to communicate between the controller and the application layer?",
                "opts": ["A) Southbound API", "B) Northbound API", "C) Eastbound API", "D) OpenFlow"],
                "ans": "B",
                "expl": "Northbound APIs connect the controller to applications and orchestration tools. Southbound APIs connect to network devices.",
                "dist": "OpenFlow is a southbound protocol."
            },
            {
                "topic": "CCNA Review and Diagnostics",
                "terms": "Troubleshooting methodology, interface states, routing loops, mismatch symptoms.",
                "lab": ["Diagnose a duplex mismatch between router and switch", "Solve a routing loop issue using CLI interface counters", "Trace routing paths: `traceroute`"],
                "q": "What interface status indicates a physical layer cable disconnection on a Cisco device?",
                "opts": ["A) administratively down, line protocol is down", "B) up, line protocol is down", "C) down, line protocol is down", "D) up, line protocol is up"],
                "ans": "C",
                "expl": "Down/Down indicates a layer 1 (cabling or connector) problem. Up/Down is Layer 2.",
                "dist": "Administratively down means the interface has been shut down via the `shutdown` command."
            }
        ]
    },
    "CIS-4330_Intro_to_AI": {
        "cert": "AI-900 (Microsoft Azure AI Fundamentals)",
        "desc": "Introduction to artificial intelligence, machine learning, data preparation, evaluation metrics, deep learning, computer vision, NLP, and cloud AI services.",
        "oer": "Microsoft Learn AI-900 Learning Path (learn.microsoft.com)",
        "weeks": [
            {
                "topic": "Introduction to AI & Machine Learning",
                "terms": "Artificial intelligence definition, machine learning vs deep learning, predictive modeling workloads.",
                "lab": ["Set up python development folder", "Install NumPy and Pandas: `pip install numpy pandas`", "Create basic script to verify packages import successfully"],
                "q": "What is the primary characteristic of Machine Learning?",
                "opts": ["A) Hardcoded if-else statements", "B) Using algorithms that learn patterns directly from data", "C) Mimicking human speech using search trees", "D) Database indexing"],
                "ans": "B",
                "expl": "Machine Learning algorithms use input data to build mathematical models that perform tasks without explicit, hardcoded instructions.",
                "dist": "Hardcoded statements are traditional programming. Database indexing is database structure."
            },
            {
                "topic": "Supervised vs Unsupervised Learning",
                "terms": "Labeled vs unlabeled data, regression, classification, clustering, anomaly detection.",
                "lab": ["Identify dataset types: regression vs classification", "Examine a dataset to classify customers into segments", "Filter a dataset based on feature target values"],
                "q": "Which type of machine learning uses labeled data to predict continuous numerical values?",
                "opts": ["A) Classification", "B) Clustering", "C) Regression", "D) Dimensionality Reduction"],
                "ans": "C",
                "expl": "Regression is a supervised learning task designed to predict continuous values (e.g., home prices).",
                "dist": "Classification predicts discrete labels. Clustering deals with unlabeled groupings."
            },
            {
                "topic": "Python Data Exploration",
                "terms": "Pandas DataFrames, loading CSV files, descriptive statistics, basic plots.",
                "lab": ["Load Iris dataset: `df = pd.read_csv('iris_sample.csv')`", "Inspect top 5 rows: `df.head()`", "Generate dataset descriptive summary: `df.describe()`"],
                "q": "Which Pandas DataFrame method displays count, mean, standard deviation, and quartile ranges?",
                "opts": ["A) head()", "B) info()", "C) describe()", "D) summary()"],
                "ans": "C",
                "expl": "The `.describe()` method generates descriptive statistics for numerical columns in a DataFrame.",
                "dist": "head() shows rows. info() shows data types. summary() is not a Pandas method."
            },
            {
                "topic": "Data Preprocessing",
                "terms": "Handling missing data, normalization, feature scaling, one-hot encoding for categorical values.",
                "lab": ["Impute missing values using Pandas `fillna()` method", "Scale numerical features to 0-1 range using MinMaxScaler", "Convert text categories to binary columns using `get_dummies()`"],
                "q": "What is the purpose of one-hot encoding in data preprocessing?",
                "opts": ["A) To compress files", "B) To convert categorical text features into binary vectors", "C) To clean out duplicates", "D) To normalize numeric data"],
                "ans": "B",
                "expl": "One-hot encoding converts labels or categories into binary indicators (0 or 1) that machine learning models can compute.",
                "dist": "Normalization scales numbers. Compression and deduplication are general data administration."
            },
            {
                "topic": "Linear and Logistic Regression Models",
                "terms": "Linear equation ($y=mx+b$), cost function, gradient descent, logistic sigmoid curve for classification.",
                "lab": ["Import `LinearRegression` from `sklearn.linear_model`", "Fit a model: `model.fit(X, y)`", "Predict outcomes and print model coefficients"],
                "q": "Which model is appropriate for predicting binary (yes/no) output class labels?",
                "opts": ["A) Linear Regression", "B) Logistic Regression", "C) K-Means Clustering", "D) Principal Component Analysis"],
                "ans": "B",
                "expl": "Logistic regression maps output predictions to a probability between 0 and 1, making it ideal for binary classification.",
                "dist": "Linear regression is for continuous variables. K-Means is for grouping."
            },
            {
                "topic": "Decision Trees and Random Forests",
                "terms": "Splitting criteria (Gini, Entropy), leaf nodes, ensemble methods, bootstrap aggregation.",
                "lab": ["Train a Decision Tree Classifier on flower classifications", "Examine feature importance outputs", "Train a Random Forest Ensemble model and compare accuracy"],
                "q": "What type of machine learning model is a Random Forest?",
                "opts": ["A) Linear Model", "B) Single Decision Tree", "C) Ensemble Model", "D) Neural Network"],
                "ans": "C",
                "expl": "A Random Forest is an ensemble model that combines the predictions of multiple decision trees to improve overall stability.",
                "dist": "It is an ensemble (collection) of trees, not a single tree or linear model."
            },
            {
                "topic": "Evaluating Machine Learning Models",
                "terms": "Confusion matrix, Accuracy, Precision, Recall, F1-Score, Mean Squared Error (MSE).",
                "lab": ["Generate a confusion matrix output", "Calculate model accuracy and recall values", "Compute Mean Squared Error (MSE) of regression predictions"],
                "q": "Which metric measures the fraction of actual positive instances that were correctly identified by a classification model?",
                "opts": ["A) Precision", "B) Recall (Sensitivity)", "C) Accuracy", "D) Specificity"],
                "ans": "B",
                "expl": "Recall (True Positives / (True Positives + False Negatives)) measures the model's ability to find all actual positive cases.",
                "dist": "Precision measures how many predicted positives are actually positive."
            },
            {
                "topic": "Deep Learning & Neural Networks",
                "terms": "Neurons, activation functions (ReLU, Sigmoid), layers (input, hidden, output), backpropagation.",
                "lab": ["Define a basic neural network layer layout", "Examine activation thresholds", "Trace forward propagation pathways"],
                "q": "What activation function is typically used in the hidden layers of modern neural networks to prevent vanishing gradients?",
                "opts": ["A) Sigmoid", "B) Rectified Linear Unit (ReLU)", "C) Tanh", "D) Step function"],
                "ans": "B",
                "expl": "ReLU (outputting max(0, x)) is widely used in hidden layers because of its computational simplicity and prevention of vanishing gradients.",
                "dist": "Sigmoid and Tanh are prone to vanishing gradients in deep networks."
            },
            {
                "topic": "Computer Vision Concepts",
                "terms": "Image classification, object detection, semantic segmentation, optical character recognition (OCR).",
                "lab": ["Examine an image array representation in Python", "Process image matrix dimensions", "Use pre-trained model APIs to detect objects in an image file"],
                "q": "Which computer vision task involves identifying both the locations and classes of multiple objects inside an image using bounding boxes?",
                "opts": ["A) Image Classification", "B) Object Detection", "C) Semantic Segmentation", "D) Optical Character Recognition"],
                "ans": "B",
                "expl": "Object detection locates boundaries (bounding boxes) and labels the objects within them.",
                "dist": "Classification labels the whole image. Segmentation labels individual pixels. OCR reads text."
            },
            {
                "topic": "Natural Language Processing (NLP)",
                "terms": "Tokenization, stop-word removal, lemmatization, bag-of-words representation, sentiment analysis.",
                "lab": ["Tokenize a sample paragraph into individual words", "Filter out common stop words (e.g. 'the', 'is')", "Perform sentiment scoring on text segments"],
                "q": "What is the process of breaking down a continuous stream of text into individual words or punctuation marks called?",
                "opts": ["A) Lemmatization", "B) Tokenization", "C) Stemming", "D) Vectorization"],
                "ans": "B",
                "expl": "Tokenization splits a string of text into smaller units (tokens) for lexical analysis.",
                "dist": "Lemmatization and stemming reduce words to root forms. Vectorization converts tokens to numbers."
            },
            {
                "topic": "Generative AI and Large Language Models",
                "terms": "Transformer architecture, self-attention mechanisms, prompt engineering, fine-tuning, embeddings.",
                "lab": ["Examine prompt templates for LLM interactions", "Write structured prompts with context constraints", "Analyze model outputs for hallucination indicators"],
                "q": "What core neural network architecture is the foundation for modern Large Language Models (LLMs) like GPT?",
                "opts": ["A) Convolutional Neural Network (CNN)", "B) Recurrent Neural Network (RNN)", "C) Transformer", "D) Support Vector Machine (SVM)"],
                "ans": "C",
                "expl": "Transformers utilize self-attention mechanisms to process sequence tokens in parallel, enabling training on large datasets.",
                "dist": "CNN is for images. RNN is sequential but superseded by Transformers for LLMs. SVM is a linear model."
            },
            {
                "topic": "Ethical AI and Responsible Deployment",
                "terms": "Microsoft's 6 principles of Responsible AI: Fairness, Reliability, Privacy/Security, Inclusiveness, Transparency, Accountability.",
                "lab": ["Analyze a dataset for demographic bias indicators", "Review AI model parameters for privacy disclosures", "Document model lineage and limitations"],
                "q": "Which Responsible AI principle states that AI systems should treat all people fairly without demographic discrimination?",
                "opts": ["A) Reliability and Safety", "B) Privacy and Security", "C) Fairness", "D) Transparency"],
                "ans": "C",
                "expl": "Fairness ensures that algorithms do not make biased assertions based on gender, race, or demographics.",
                "dist": "Safety focuses on system operational hazards. Privacy focuses on data protection."
            },
            {
                "topic": "Cloud AI Services",
                "terms": "Cognitive APIs, pre-trained vs custom models, deploying endpoint services.",
                "lab": ["Provision a Cognitive Service resource in cloud portal simulator", "Retrieve API keys and endpoint URLs", "Make a curl request to a translation API endpoint"],
                "q": "What is the benefit of using Cloud Cognitive Services over building models from scratch?",
                "opts": ["A) Pre-trained models save development time and compute resources", "B) They are always free", "C) They do not require an internet connection", "D) They support any custom hardware"],
                "ans": "A",
                "expl": "Cloud cognitive APIs provide pre-trained, vendor-hosted models that can be integrated via simple HTTP requests, bypassing complex local model training.",
                "dist": "They are billed services, require internet connections, and run on cloud hardware."
            },
            {
                "topic": "Automated Machine Learning (AutoML)",
                "terms": "AutoML pipelines, hyperparameter tuning, model selection sweeps.",
                "lab": ["Configure a mock AutoML run selecting classification as target", "Inspect performance rankings of multiple trained models", "Select the best model for deployment"],
                "q": "What does Automated Machine Learning (AutoML) automate?",
                "opts": ["A) Data collection from websites", "B) Feature selection, algorithm sweep, and hyperparameter tuning", "C) Writing Python code for front-end web layouts", "D) Database backups"],
                "ans": "B",
                "expl": "AutoML automates the iterative process of model training, sweeping across algorithms and tuning hyperparameters to find the optimal model.",
                "dist": "AutoML does not collect data or write web app UI code."
            },
            {
                "topic": "AI System Deployment",
                "terms": "Model serialization (pickle, ONNX), containerization (Docker), REST API deployment, monitoring endpoints.",
                "lab": ["Serialize a scikit-learn model: `import pickle; pickle.dump(...)`", "Create a mock Dockerfile for hosting the model", "Send input data payload to verify API output response"],
                "q": "How is a trained machine learning model typically exposed to client applications?",
                "opts": ["A) As a raw Python script", "B) As a web-accessible REST API endpoint", "C) Direct connection to SQL server", "D) Inside an email attachment"],
                "ans": "B",
                "expl": "Models are usually deployed inside containerized web services that expose REST API endpoints for clients to submit data and receive predictions.",
                "dist": "Direct client access to script files or SQL servers is not recommended for scalable production deployments."
            }
        ]
    },
    "CIS-4331_Azure_Cloud": {
        "cert": "Microsoft Azure Fundamentals (AZ-900)",
        "desc": "Azure Cloud architectural components, storage services, networking, database services, and identity management.",
        "oer": "Microsoft Learn AZ-900 Path (learn.microsoft.com)",
        "weeks": [
            {
                "topic": "Cloud Computing Concepts",
                "terms": "IaaS, PaaS, SaaS, Public/Private/Hybrid clouds, shared responsibility model, CAPEX vs OPEX.",
                "lab": ["Classify hosting scenarios into IaaS, PaaS, or SaaS", "Determine operational ownership for virtualization layers", "Estimate costs using TCO Calculator"],
                "q": "Which service model gives the consumer the greatest control over virtual machines and operating systems?",
                "opts": ["A) Software as a Service (SaaS)", "B) Platform as a Service (PaaS)", "C) Infrastructure as a Service (IaaS)", "D) Database as a Service (DBaaS)"],
                "ans": "C",
                "expl": "IaaS provides raw infrastructure (VMs, networking, storage), leaving OS and software management to the customer.",
                "dist": "PaaS and SaaS manage the OS layer for you, reducing your control."
            },
            {
                "topic": "Azure Physical Architecture",
                "terms": "Azure Regions, Region Pairs, Availability Zones, Resource Groups, Azure Resource Manager.",
                "lab": ["Inspect Azure geography layout", "Create a Resource Group in a specific region", "Review Resource Group lock configurations"],
                "q": "How many separate physical datacenters must exist within a single Azure Availability Zone?",
                "opts": ["A) At least one", "B) Exactly three", "C) Ten", "D) Availability Zones do not contain physical datacenters"],
                "ans": "A",
                "expl": "An Availability Zone is made up of one or more physical datacenters equipped with independent power, cooling, and networking.",
                "dist": "Exactly three is a common misconception (an Azure region with AZ support has at least three zones, not datacenters per zone)."
            },
            {
                "topic": "Azure Virtual Machines & Scale Sets",
                "terms": "Azure Compute services, Virtual Machines, Virtual Machine Scale Sets (VMSS), Azure App Services.",
                "lab": ["Provision an Azure Linux VM using portal template", "Set up auto-scaling properties on a VM Scale Set", "Verify VM SSH access"],
                "q": "Which Azure compute service allows you to automatically deploy and manage a set of identical, auto-scaling VMs?",
                "opts": ["A) Azure App Service", "B) Azure Functions", "C) Virtual Machine Scale Sets", "D) Azure Container Instances"],
                "ans": "C",
                "expl": "VMSS enables automatic scaling of identical VMs based on CPU load or schedules.",
                "dist": "App Service is for web apps. Functions is serverless."
            },
            {
                "topic": "Azure Container Services",
                "terms": "Azure Container Instances (ACI), Azure Kubernetes Service (AKS), serverless computing.",
                "lab": ["Deploy a container using Azure Container Instances", "Verify the container running state", "Examine Kubernetes orchestration structures in AKS"],
                "q": "What is the fastest way to run a single Docker container in Azure without provisioning virtual machines?",
                "opts": ["A) Azure Kubernetes Service (AKS)", "B) Azure Container Instances (ACI)", "C) Azure Functions", "D) Windows Server container host"],
                "ans": "B",
                "expl": "ACI is a serverless container solution designed to quickly run single containers without VM management overhead.",
                "dist": "AKS is for full container orchestrations and requires cluster provisioning."
            },
            {
                "topic": "Azure Virtual Networking",
                "terms": "Virtual Networks (VNet), subnets, Network Security Groups (NSGs), Azure ExpressRoute, VPN Gateways.",
                "lab": ["Create a VNet with public and private subnets", "Configure an NSG rule to block port 80 traffic", "Trace VPN routing tables"],
                "q": "Which Azure service allows secure, dedicated, private fiber-optic connection from an on-premises datacenter directly to Azure?",
                "opts": ["A) Azure VPN Gateway", "B) Azure ExpressRoute", "C) Azure Bastion", "D) VNet Peering"],
                "ans": "B",
                "expl": "ExpressRoute bypasses the public internet completely to provide high-speed, private connections to Azure.",
                "dist": "VPN Gateway travels over the public internet using encryption."
            },
            {
                "topic": "Azure Storage Services",
                "terms": "Blob storage (Hot, Cool, Cold, Archive), Azure Files, Disk Storage, storage replication types.",
                "lab": ["Create an Azure Storage Account", "Upload a blob to a Container", "Modify blob access tier from Hot to Archive"],
                "q": "Which storage tier has the lowest storage cost but the highest data retrieval latency?",
                "opts": ["A) Hot Tier", "B) Cool Tier", "C) Cold Tier", "D) Archive Tier"],
                "ans": "D",
                "expl": "Archive storage offers the cheapest capacity rates but requires hours to rehydrate/retrieve data.",
                "dist": "Hot, Cool, and Cold tiers keep data online for immediate access at higher costs."
            },
            {
                "topic": "Azure Database Services",
                "terms": "Azure SQL Database, Cosmos DB (multi-model, global distribution), Azure Database for MySQL/PostgreSQL.",
                "lab": ["Deploy an Azure SQL database instance", "Examine connection strings", "Configure Cosmos DB global replica sites"],
                "q": "Which Azure database service is a globally distributed, multi-model database engine supporting SQL, MongoDB, and Cassandra APIs?",
                "opts": ["A) Azure SQL Database", "B) Azure Database for PostgreSQL", "C) Azure Cosmos DB", "D) Azure SQL Managed Instance"],
                "ans": "C",
                "expl": "Cosmos DB is Microsoft's NoSQL engine built for global distribution and multi-API access.",
                "dist": "Azure SQL is strictly relational SQL."
            },
            {
                "topic": "Microsoft Entra ID (Azure AD) Basics",
                "terms": "Microsoft Entra ID directory structure, tenant, users, groups, hybrid identity, Azure AD Connect.",
                "lab": ["Add a new user to Microsoft Entra tenant", "Create a security group and assign members", "Configure basic tenant settings"],
                "q": "What is the primary function of Microsoft Entra ID?",
                "opts": ["A) Network routing and DNS", "B) Identity and Access Management", "C) Database storage", "D) Host virtualization"],
                "ans": "B",
                "expl": "Entra ID (formerly Azure Active Directory) handles authentication and access management for cloud identities.",
                "dist": "It is not a domain controller replacement for DNS or database storage."
            },
            {
                "topic": "Entra Authentication and MFA",
                "terms": "Multi-Factor Authentication (MFA), Conditional Access policies, Single Sign-On (SSO).",
                "lab": ["Configure a Conditional Access policy requiring MFA for administrators", "Verify authentication flow", "Configure SSO settings"],
                "q": "Which Entra ID feature allows you to enforce security policies based on signals like user location or device state?",
                "opts": ["A) Multi-Factor Authentication", "B) Conditional Access", "C) Role-Based Access Control", "D) Privileged Identity Management"],
                "ans": "B",
                "expl": "Conditional Access implements 'if-then' policies (e.g. if logging in from outside corporate network, require MFA).",
                "dist": "MFA is the authentication mechanism, but Conditional Access controls when it is triggered."
            },
            {
                "topic": "Azure RBAC and Subscriptions",
                "terms": "Role-Based Access Control (RBAC), built-in roles (Owner, Contributor, Reader), scopes, subscriptions.",
                "lab": ["Assign 'Reader' role to a user at the Resource Group scope", "Verify user cannot delete resources", "Create a custom role template"],
                "q": "What is the scope hierarchy in Azure from largest to smallest?",
                "opts": ["A) Subscription -> Resource Group -> Resource -> Management Group", "B) Management Group -> Subscription -> Resource Group -> Resource", "C) Resource -> Resource Group -> Subscription -> Management Group", "D) Tenant -> Resource -> Resource Group -> Subscription"],
                "ans": "B",
                "expl": "Inheritance flows from Management Groups down to Subscriptions, Resource Groups, and individual Resources.",
                "dist": "A and C represent incorrect orderings. D starts at resource."
            },
            {
                "topic": "Azure Security Tools",
                "terms": "Microsoft Defender for Cloud, Security Center, Azure Key Vault, Azure Sentinel (SIEM).",
                "lab": ["Provision an Azure Key Vault resource", "Securely add a secret to the vault", "Retrieve secret using cloud CLI command"],
                "q": "Which Azure service is designed to securely store and control access to tokens, passwords, certificates, and API keys?",
                "opts": ["A) Azure Bastion", "B) Azure Key Vault", "C) Microsoft Entra ID", "D) Azure Security Center"],
                "ans": "B",
                "expl": "Key Vault provides centralized secrets, keys, and certificate storage with strict access controls.",
                "dist": "Bastion provides secure RDP/SSH. Entra ID is for identities."
            },
            {
                "topic": "Azure Governance & Compliance",
                "terms": "Azure Policy, Azure Blueprints, resource tags, locks (ReadOnly, CanNotDelete).",
                "lab": ["Create a CanNotDelete lock on a virtual network resource", "Verify the VNet cannot be deleted", "Apply tag metadata to resources"],
                "q": "Which resource lock type prevents users from deleting a resource but still allows them to read and modify it?",
                "opts": ["A) ReadOnly", "B) CanNotDelete", "C) WriteLock", "D) DeleteLock"],
                "ans": "B",
                "expl": "The `CanNotDelete` lock allows read and write modifications but blocks deletion requests.",
                "dist": "ReadOnly blocks both deletions and writes."
            },
            {
                "topic": "Azure Monitoring and Diagnostics",
                "terms": "Azure Monitor, Log Analytics, Azure Service Health, Advisor recommendations.",
                "lab": ["Examine Azure Advisor suggestions for cost and security", "Configure an Azure Monitor metric alert", "Verify Service Health dashboard status"],
                "q": "Which Azure service provides personalized recommendations to optimize resource performance, security, and cost?",
                "opts": ["A) Azure Monitor", "B) Azure Log Analytics", "C) Azure Advisor", "D) Microsoft Sentinel"],
                "ans": "C",
                "expl": "Azure Advisor scans your deployment configuration and recommends improvements across five pillars: Cost, Security, Reliability, Performance, and Operational Excellence.",
                "dist": "Azure Monitor collects telemetry metrics."
            },
            {
                "topic": "Azure Cost Management",
                "terms": "Pricing calculator, TCO calculator, cost alerts, factors affecting cost, reservations.",
                "lab": ["Configure a cost budget and warning alert in Azure Cost Management", "Compare price of on-demand vs reserved instances", "Check billing reports"],
                "q": "What purchase option allows you to reduce VM costs by up to 72% by committing to a 1-year or 3-year term?",
                "opts": ["A) Pay-as-you-go", "B) Spot Instances", "C) Azure Reservations", "D) Hybrid Benefit"],
                "ans": "C",
                "expl": "Reservations provide significant discounts in exchange for a committed usage duration.",
                "dist": "Spot instances can be evicted. Hybrid Benefit uses on-premises licensing."
            },
            {
                "topic": "Azure Resource Manager (ARM) & CLI",
                "terms": "ARM templates (declarative JSON), Azure CLI, Azure Cloud Shell, PowerShell module.",
                "lab": ["Launch Azure Cloud Shell", "Run command: `az group list --output table`", "Deploy a resource using a basic ARM template payload"],
                "q": "What file format is used to write Azure Resource Manager (ARM) templates?",
                "opts": ["A) XML", "B) JSON", "C) YAML", "D) CSV"],
                "ans": "B",
                "expl": "ARM templates are written in JSON (JavaScript Object Notation), representing resources declaratively.",
                "dist": "YAML is used for Bicep or Kubernetes configurations but not native ARM templates."
            }
        ]
    },
    "CIS-4332_Cyber_Analyst": {
        "cert": "CompTIA CySA+",
        "desc": "Cybersecurity analysis, threat intelligence, vulnerability scanning, log analysis, SIEM tools, and incident response frameworks.",
        "oer": "CertifyBreakfast CySA+ Series (youtube.com)",
        "weeks": [
            {
                "topic": "Security Operations & Analyst Role",
                "terms": "SOC operations, CIA Triad, threat landscape, intelligence gathering frameworks.",
                "lab": ["Map SOC alert workflows", "Review log collections in a mock SIEM dashboard", "Identify indicator classifications (IOCs)"],
                "q": "What does IOC stand for in security operations?",
                "opts": ["A) Index of Controls", "B) Indicator of Compromise", "C) Institution of Cybersecurity", "D) Internal Operational Check"],
                "ans": "B",
                "expl": "Indicators of Compromise (IOCs) are forensic clues (file hashes, IPs, domains) that indicate a security breach.",
                "dist": "The other options are made up acronyms."
            },
            {
                "topic": "Vulnerability Management Lifecycle",
                "terms": "Vulnerability assessment phases: Identify, Analyze, Prioritize, Remediate, Verify.",
                "lab": ["Draft a vulnerability remediation plan", "Prioritize vulnerabilities based on system criticality", "Schedule patching operations"],
                "q": "What is the first phase of the vulnerability management lifecycle?",
                "opts": ["A) Remediation", "B) Prioritization", "C) Identification", "D) Verification"],
                "ans": "C",
                "expl": "You must identify vulnerabilities first (via scanning or assessment) before you can analyze or remediate them.",
                "dist": "Identification is the initial step."
            },
            {
                "topic": "Infrastructure Scanning Tools",
                "terms": "Network vulnerability scanners, credentialed vs non-credentialed scans, Nmap vulnerability scripts.",
                "lab": ["Configure a basic vulnerability scan target list", "Perform a mock Nmap NSE script scan", "Analyze scanning speed impacts on network bandwidth"],
                "q": "Which type of scan provides the most accurate view of patch levels and installed software on a target host?",
                "opts": ["A) Non-credentialed scan", "B) Credentialed scan", "C) Passive network sniff", "D) Stealth SYN scan"],
                "ans": "B",
                "expl": "Credentialed scans log into the system to read local registry settings and files directly, preventing false positives.",
                "dist": "Non-credentialed scans can only analyze open network ports and banners."
            },
            {
                "topic": "Analyzing Vulnerability Reports",
                "terms": "CVSS scoring system, base/temporal/environmental metrics, reporting metrics.",
                "lab": ["Calculate CVSS score using online vector calculator", "Filter vulnerability reports for CVSS >= 7.0 (High)", "Map CVE IDs to software platforms"],
                "q": "Which CVSS metric group represents the characteristics of a vulnerability that constant over time and across environments?",
                "opts": ["A) Base Metric Group", "B) Temporal Metric Group", "C) Environmental Metric Group", "D) Local Metric Group"],
                "ans": "A",
                "expl": "Base metrics represent the core qualities of the vulnerability that do not change.",
                "dist": "Temporal metrics reflect threat activity. Environmental metrics reflect local network importance."
            },
            {
                "topic": "Threat Intelligence & Hunting",
                "terms": "MITRE ATT&CK framework, Cyber Kill Chain, threat intelligence feeds (STIX/TAXII).",
                "lab": ["Trace an attack technique in MITRE ATT&CK matrix", "Map threat actors to known vulnerabilities", "Configure threat feed feeds integration"],
                "q": "Which protocol is the standard carrier for exchanging structured cyber threat intelligence data over HTTP?",
                "opts": ["A) STIX", "B) TAXII", "C) JSON-RPC", "D) Syslog"],
                "ans": "B",
                "expl": "TAXII (Trusted Automated Exchange of Intelligence Information) is the transport mechanism. STIX is the language format.",
                "dist": "STIX defines the data schema, TAXII carries it."
            },
            {
                "topic": "IDS/IPS Tools & Monitoring",
                "terms": "Signature-based vs anomaly-based detection, Snort rule configuration, inline vs passive placement.",
                "lab": ["Review a Snort rule file structure", "Write a basic rule to alert on ICMP packets", "Examine PCAP captures for alert triggers"],
                "q": "What is the main operational difference between an IDS and an IPS?",
                "opts": ["A) IDS is active, IPS is passive", "B) IDS only detects and alerts, while IPS actively blocks traffic", "C) IDS works at Layer 2, IPS works at Layer 7", "D) IDS does not require rules"],
                "ans": "B",
                "expl": "Intrusion Detection Systems (IDS) detect/log. Intrusion Prevention Systems (IPS) sit inline and can block traffic.",
                "dist": "IDS is passive. IPS is active."
            },
            {
                "topic": "Host-Based Security & EDR",
                "terms": "Endpoint Detection and Response (EDR), file integrity monitoring (FIM), local system audits.",
                "lab": ["Configure a FIM utility (e.g. Tripwire) path watchlist", "Simulate a unauthorized file change in system folder", "Verify alert generated in FIM logs"],
                "q": "Which technology monitors system files in real-time to detect unauthorized file alterations or registry edits?",
                "opts": ["A) Endpoint Detection and Response (EDR)", "B) File Integrity Monitoring (FIM)", "C) Antivirus signatures", "D) Host-based firewall"],
                "ans": "B",
                "expl": "FIM compares cryptographic hashes of files against a baseline to detect modifications.",
                "dist": "EDR is broader. FIM is specific to file tampering."
            },
            {
                "topic": "Log Analysis & SIEM",
                "terms": "Log aggregation, syslog format, correlation rules, event deduplication, dashboards.",
                "lab": ["Query log repository for failed logins: `grep 'Failed password' /var/log/auth.log`", "Correlate failed logins with subsequent successful login from matching IP", "Review dashboard analytics"],
                "q": "What is the primary purpose of event correlation in a SIEM?",
                "opts": ["A) Compressing files to save storage space", "B) Linking separate events together across different systems to identify indicators of an attack", "C) Encrypting log data", "D) Running software updates"],
                "ans": "B",
                "expl": "SIEM correlation engines match logical rules across disparate logs (e.g., firewall deny + failed SQL login = attack alert).",
                "dist": "It is not for compression or updates."
            },
            {
                "topic": "Email & Web Security Analysis",
                "terms": "DKIM, SPF, DMARC, SMTP logs, web proxy traffic review, HTTP status codes.",
                "lab": ["Analyze raw email header details for SPF validation outcomes", "Determine proxy request origin paths", "Trace malicious URL parameters"],
                "q": "Which DNS record type verifies that an email was actually sent by the authorized domain using public key signatures?",
                "opts": ["A) SPF", "B) DKIM", "C) DMARC", "D) MX"],
                "ans": "B",
                "expl": "DKIM (DomainKeys Identified Mail) signs emails cryptographically, validating the sender domain.",
                "dist": "SPF lists authorized IPs. DMARC aligns SPF/DKIM."
            },
            {
                "topic": "IAM Risks and Audit",
                "terms": "Privileged account abuse, orphan accounts, access reviews, multifactor authentication gaps.",
                "lab": ["Audit user directories for accounts inactive for > 90 days", "Analyze logs for administrative privilege escalations", "Review role-based permissions mappings"],
                "q": "What is the risk associated with orphan accounts?",
                "opts": ["A) They waste disk space", "B) They remain active after employees leave, providing unmonitored access points", "C) They cannot be backed up", "D) They cause IP address conflicts"],
                "ans": "B",
                "expl": "Orphan accounts are active accounts belonging to ex-employees that can be hijacked by attackers.",
                "dist": "They represent access risks rather than resource constraints."
            },
            {
                "topic": "Software Security & OWASP",
                "terms": "OWASP Top 10 vulnerabilities (SQLi, XSS, SSRF), secure code reviews, dependency auditing.",
                "lab": ["Identify a SQL Injection vulnerability in a code snippet", "Apply query parameterization to fix the issue", "Inspect OWASP security checklists"],
                "q": "Which vulnerability class allows an attacker to inject client-side scripts into web pages viewed by other users?",
                "opts": ["A) SQL Injection", "B) Cross-Site Scripting (XSS)", "C) Server-Side Request Forgery", "D) Command Injection"],
                "ans": "B",
                "expl": "XSS vulnerabilities occur when web applications execute malicious script in the browser of another user.",
                "dist": "SQLi targets databases. SSRF targets backend server requests."
            },
            {
                "topic": "Incident Response Frameworks",
                "terms": "NIST SP 800-61 phases: Preparation, Detection/Analysis, Containment/Eradication, Post-Incident Activity.",
                "lab": ["Draft containment strategies for a compromised web host", "Analyze indicator severity levels", "Document lessons-learned steps"],
                "q": "During which phase of the NIST incident response lifecycle do you isolate a system to prevent further damage?",
                "opts": ["A) Detection and Analysis", "B) Containment, Eradication, and Recovery", "C) Post-Incident Activity", "D) Preparation"],
                "ans": "B",
                "expl": "Containment limits the scope of the breach (e.g. shutting down ports, isolating subnets).",
                "dist": "Detection comes before containment. Eradication is removing the threat."
            },
            {
                "topic": "Forensics & Evidence Collection",
                "terms": "Order of volatility, chain of custody, write blockers, disk imaging (dd).",
                "lab": ["Write evidence chain of custody forms", "Capture volatile system memory (RAM)", "Create disk image: `dd if=/dev/sdb of=evidence.img`"],
                "q": "Which data source should be collected FIRST during forensic collection due to its volatility?",
                "opts": ["A) HDD storage", "B) CPU Registers and RAM", "C) Log files on disk", "D) Print server spool queue"],
                "ans": "B",
                "expl": "Memory and processor state volatile data is lost immediately on shutdown, placing them first in the order of volatility.",
                "dist": "Disk storage can survive power loss."
            },
            {
                "topic": "Threat Detection & Containment",
                "terms": "DNS sinkholing, firewall IP blocks, isolating VLANs, disabling compromised user accounts.",
                "lab": ["Configure a firewall rule to block command-and-control IP", "Implement a DNS sinkhole mapping for suspicious domain", "Review account suspension scripts"],
                "q": "What is the purpose of DNS sinkholing in incident containment?",
                "opts": ["A) Speeding up DNS requests", "B) Redirecting malicious outbound traffic to a secure internal IP address", "C) Encrypting domain records", "D) Shutting down the DNS server"],
                "ans": "B",
                "expl": "DNS sinkholing resolves blacklisted domains to a controlled IP, preventing communication with C2 servers.",
                "dist": "It is a containment mechanism, not an optimization tool."
            },
            {
                "topic": "Security Controls & Architecture",
                "terms": "Technical vs Administrative vs Physical controls, defense-in-depth, security logging topologies.",
                "lab": ["Audit physical security layouts", "Review technical control configuration details", "Draft a defense-in-depth policy model"],
                "q": "Which control type is a security awareness training program classified as?",
                "opts": ["A) Technical control", "B) Administrative (Managerial) control", "C) Physical control", "D) Deterrent control"],
                "ans": "B",
                "expl": "Administrative controls are written policies, guidelines, and training implemented by management.",
                "dist": "Technical controls are software/hardware locks. Physical controls are fences/badges."
            }
        ]
    },
    "CIS-4333_Penetration_Testing": {
        "cert": "CompTIA PenTest+",
        "desc": "Penetration testing phases, passive and active reconnaissance (OSINT, Nmap), exploit methods, post-exploitation, and reporting.",
        "oer": "TryHackMe PenTest+ Pathway (tryhackme.com)",
        "weeks": [
            {
                "topic": "Planning & Scoping Pen Tests",
                "terms": "Rules of Engagement (RoE), scoping document parameters, target classifications, permission checklists.",
                "lab": ["Draft a mock Rules of Engagement (RoE) document", "Define IP range boundaries for pen test target scope", "Review target disclosure guidelines"],
                "q": "Which document explicitly defines the boundaries, methods, and authorized targets of a penetration test?",
                "opts": ["A) Non-Disclosure Agreement (NDA)", "B) Rules of Engagement (RoE)", "C) Service Level Agreement (SLA)", "D) Master Service Agreement (MSA)"],
                "ans": "B",
                "expl": "The RoE sets rules, exclusions, IP targets, and schedule guidelines for the team.",
                "dist": "NDA protects confidential data. SLA is service uptime. MSA is general commercial agreements."
            },
            {
                "topic": "Legal & Ethical Considerations",
                "terms": "Authorization (get-out-of-jail card), local regulations, regulatory frameworks (PCI-DSS, HIPAA).",
                "lab": ["Review a customer pen test authorization letter", "Determine regulatory compliance requirements", "Examine liability exemptions"],
                "q": "What must a penetration tester secure before executing any port scanning or exploit tools against a client network?",
                "opts": ["A) Public IP certificate", "B) Written authorization from key stakeholders", "C) Insurance coverage", "D) A server license"],
                "ans": "B",
                "expl": "Without written, authorized consent, performing scanning or exploits is considered illegal hacking.",
                "dist": "Authorization is legally required."
            },
            {
                "topic": "Passive Reconnaissance (OSINT)",
                "terms": "Whois queries, DNS interrogation (dig, host), Shodan search filters, harvesting email addresses (theHarvester).",
                "lab": ["Perform whois lookup on a public domain: `whois example.com`", "Use `dig` to find MX and TXT records", "Search Shodan for open webservers in a specific city"],
                "q": "Which command-line tool is used for passive DNS gathering, specifically retrieving mail server configurations?",
                "opts": ["A) dig example.com MX", "B) nmap example.com", "C) ping example.com", "D) traceroute example.com"],
                "ans": "A",
                "expl": "`dig` queries DNS name servers. Passing `MX` retrieves mail records passively without targeting the server directly.",
                "dist": "Nmap is active scanning. Ping sends ICMP traffic. Traceroute routes packets."
            },
            {
                "topic": "Active Reconnaissance (Nmap)",
                "terms": "SYN scans (-sS) vs Connect scans (-sT), service version detection (-sV), OS detection (-O), Nmap scripting engine (-sC).",
                "lab": ["Perform a SYN scan: `nmap -sS target_ip`", "Identify open services and versions: `nmap -sV target_ip`", "Use basic vulnerability scan script: `nmap --script vuln target_ip`"],
                "q": "Which Nmap scan type is known as 'stealth' or 'half-open' scanning because it does not complete the 3-way handshake?",
                "opts": ["A) TCP Connect Scan (-sT)", "B) TCP SYN Scan (-sS)", "C) UDP Scan (-sU)", "D) Ping Sweep (-sn)"],
                "ans": "B",
                "expl": "SYN scans send SYN packets and listen for SYN-ACK, but respond with RST instead of ACK to keep connections half-open.",
                "dist": "Connect scans complete the handshake, leaving log footprints on target sockets."
            },
            {
                "topic": "Vulnerability Scanning",
                "terms": "Configuring scanning parameters, false positives vs false negatives, analyzing severity levels.",
                "lab": ["Setup target scanning profiles", "Filter scanning reports for critical CVE disclosures", "Review scan performance indicators"],
                "q": "What is it called when a vulnerability scanner reports a security issue that does not actually exist on the target system?",
                "opts": ["A) False Negative", "B) False Positive", "C) True Positive", "D) Null Match"],
                "ans": "B",
                "expl": "False Positives occur when scanning rules mismatch background states and assume a vulnerability is present.",
                "dist": "False Negatives are when real issues are missed by the scanner."
            },
            {
                "topic": "Social Engineering Attacks",
                "terms": "Phishing email layout, vishing, tailgating, baiting, spear-phishing vs whaling.",
                "lab": ["Audit email templates for phishing flags", "Analyze tailgating security layouts", "Review baiting attack vectors"],
                "q": "What is a phishing attack that specifically targets high-profile corporate executives (such as CEOs or CFOs) called?",
                "opts": ["A) Spear-phishing", "B) Whaling", "C) Vishing", "D) Smishing"],
                "ans": "B",
                "expl": "Whaling is a sub-class of phishing designed specifically to target high-ranking executive personnel.",
                "dist": "Spear-phishing targets any specific individual. Vishing is voice. Smishing is SMS."
            },
            {
                "topic": "Exploiting Network Vulnerabilities",
                "terms": "Metasploit framework console (msfconsole), search exploits, payloads, reverse vs bind shells.",
                "lab": ["Launch Metasploit: `msfconsole`", "Search for exploit matching target service: `search vsftpd`", "Configure parameters and deploy test reverse shell payload"],
                "q": "Which type of shell payload instructs the target machine to connect back to the attacker's listening machine?",
                "opts": ["A) Bind Shell", "B) Reverse Shell", "C) SSH Shell", "D) Interactive Shell"],
                "ans": "B",
                "expl": "Reverse shells initiate connections outwards from the target, bypassing inbound firewall blocks.",
                "dist": "Bind shells open a port on target and listen for attacker connections."
            },
            {
                "topic": "Exploiting Windows & Active Directory",
                "terms": "Kerberoasting, Pass-the-Hash, LSASS memory dumping, SMB exploitation.",
                "lab": ["Simulate SMB credential verification", "Dump local credentials memory structure", "Analyze Windows privilege tokens"],
                "q": "Which Active Directory attack involves requesting service tickets and attempting to crack the service account password hashes offline?",
                "opts": ["A) Pass-the-Hash", "B) Kerberoasting", "C) AS-REP Roasting", "D) SMB Relay"],
                "ans": "B",
                "expl": "Kerberoasting allows standard AD users to request tickets for service principal names (SPNs) and attempt offline brute-forcing.",
                "dist": "Pass-the-hash uses existing hashes to authenticate without cracking them."
            },
            {
                "topic": "Exploiting Linux Systems",
                "terms": "SSH credential brute-forcing, exploiting SUID binaries, misconfigured sudo rules.",
                "lab": ["Identify SUID binaries: `find / -perm -4000 2>/dev/null`", "Examine sudo permissions: `sudo -l`", "Exploit a misconfigured SUID binary to escalate privilege"],
                "q": "Which file permission bit configuration allows an executable to run with the permissions of the file owner (often root)?",
                "opts": ["A) Write Permission", "B) Sticky Bit", "C) SUID (Set Owner User ID)", "D) Execute Bit"],
                "ans": "C",
                "expl": "SUID allows binaries to execute using root privileges, creating potential escalation targets if misconfigured.",
                "dist": "Sticky bit limits deletions. SGID sets group execution permissions."
            },
            {
                "topic": "Web Application Exploit Methods",
                "terms": "SQL Injection (SQLi), Cross-Site Scripting (XSS), Command injection, directory traversal.",
                "lab": ["Intercept web request using proxy (e.g. OWASP ZAP)", "Test directory traversal URL: `/../../etc/passwd`", "Exploit SQL injection on a login form parameter"],
                "q": "What web vulnerability allows an attacker to append file paths to a URL parameter to retrieve unauthorized server files?",
                "opts": ["A) Directory Traversal", "B) SQL Injection", "C) Cross-Site Scripting", "D) Buffer Overflow"],
                "ans": "A",
                "expl": "Directory Traversal uses dot-dot-slash (`../`) parameters to escape web document roots.",
                "dist": "SQLi targets sql queries. XSS targets client scripts."
            },
            {
                "topic": "Wireless Network Assessment",
                "terms": "WPA2 handshakes, packet capture (airodump-ng), brute-forcing handshakes (aircrack-ng).",
                "lab": ["Put wireless interface in monitor mode: `airmon-ng start wlan0`", "Capture WPA2 4-way handshake using airodump-ng", "Review handshake wordlist cracking syntax"],
                "q": "Which wireless security standard is vulnerable to offline dictionary attacks on its 4-way handshake?",
                "opts": ["A) WPA3", "B) WPA2-Personal (PSK)", "C) WPA2-Enterprise", "D) WEP"],
                "ans": "B",
                "expl": "WPA2-Personal uses a 4-way handshake that can be captured and brute-forced offline. WPA3 replaces this with SAE.",
                "dist": "WEP uses RC4 cracking methods, not handshake brute-forcing. Enterprise uses RADIUS."
            },
            {
                "topic": "Post-Exploitation & Privilege Escalation",
                "terms": "Privilege escalation (Windows UAC bypass, Linux cron jobs), enumeration scripts (LinPeas/WinPeas).",
                "lab": ["Run basic system enumeration script", "Analyze output reports for write-access vulnerabilities", "Simulate a local UAC bypass"],
                "q": "What is the primary goal of privilege escalation during post-exploitation?",
                "opts": ["A) Scanning the local subnet", "B) Elevating privileges from a standard user to administrator/root", "C) Deleting logs", "D) Installing backdoors"],
                "ans": "B",
                "expl": "Privilege escalation focuses on finding paths to gain administrative control after initial access.",
                "dist": "Lateral movement is moving networks. Escalation is increasing privileges."
            },
            {
                "topic": "Maintaining Access & Pivoting",
                "terms": "Persistent backdoors (cron, registry runs), SSH port-forwarding, pivoting, proxychains.",
                "lab": ["Configure a cron-based listener connection", "Create SSH local port forward tunnel", "Route traffic through tunnel using proxychains"],
                "q": "Which technique allows a tester to route traffic through a compromised host to access a internal network subnet?",
                "opts": ["A) Privilege Escalation", "B) Pivoting", "C) Vulnerability Scanning", "D) Social Engineering"],
                "ans": "B",
                "expl": "Pivoting uses a compromised dual-homed host as a bridge to send traffic into internal systems.",
                "dist": "Escalation increases local permission level."
            },
            {
                "topic": "Penetration Testing Reports",
                "terms": "Executive summary, technical findings, CVSS scoring, remediation recommendations.",
                "lab": ["Draft an executive summary outlining high-level risk findings", "Format technical finding descriptions with remediation steps", "Assign CVSS ratings to findings"],
                "q": "What section of a penetration testing report is written specifically for non-technical stakeholders?",
                "opts": ["A) Technical Findings List", "B) Executive Summary", "C) Remediation Timeline", "D) IP Address Scope List"],
                "ans": "B",
                "expl": "The Executive Summary translates technical security risks into business impact, costs, and high-level summaries.",
                "dist": "Technical findings detail raw exploit steps."
            },
            {
                "topic": "Post-Report Cleanup & Debriefing",
                "terms": "Removing shells/backdoors, restore configuration settings, client debriefing sessions.",
                "lab": ["Document all backdoor removal verifications", "Restore system configuration defaults", "Prepare customer slide summaries"],
                "q": "Why is cleanup critical after completing a penetration test?",
                "opts": ["A) To speed up network performance", "B) To ensure no backdoors, shells, or mock payloads are left behind for real attackers to exploit", "C) Because the contract requires it", "D) None of the above"],
                "ans": "B",
                "expl": "Leftover backdoors created during tests represent serious security risks that actual hackers can compromise.",
                "dist": "Performance impact is minimal, and cleanup is first and foremost a security requirement."
            }
        ]
    },
    "CIS-4334_AWS_Cloud_Architecture": {
        "cert": "AWS Certified Solutions Architect - Associate",
        "desc": "AWS global infrastructure, virtual private clouds, network security, identity access management, S3 storage, relational and NoSQL database setups.",
        "oer": "AWS Skill Builder Portal (skillbuilder.aws)",
        "weeks": [
            {
                "topic": "AWS Infrastructure & Core Architecture",
                "terms": "AWS Regions, Availability Zones, Edge Locations, AWS Global Infrastructure, shared responsibility model.",
                "lab": ["Inspect global AWS availability zones", "Locate regional pairs", "Map out service architectures"],
                "q": "Which AWS infrastructure component consists of one or more discrete datacenters with redundant power and networking?",
                "opts": ["A) Region", "B) Edge Location", "C) Availability Zone", "D) Local Zone"],
                "ans": "C",
                "expl": "An Availability Zone (AZ) is a group of datacenters inside a Region, designed for fault isolation.",
                "dist": "Regions contain multiple AZs. Edge locations cache content."
            },
            {
                "topic": "Amazon EC2 Compute Instances",
                "terms": "EC2 instance types, Amazon Machine Images (AMIs), storage options (EBS), security keys.",
                "lab": ["Provision an EC2 Linux instance using AMI template", "Configure security keys for SSH authentication", "Verify system ping connectivity"],
                "q": "Which storage type is standard for acting as the boot volume for an Amazon EC2 virtual machine?",
                "opts": ["A) Amazon S3", "B) Amazon EBS (Elastic Block Store)", "C) Amazon EFS", "D) AWS Storage Gateway"],
                "ans": "B",
                "expl": "EBS provides block-level storage volumes designed for persistent boot partitions and database disks.",
                "dist": "S3 is object storage and cannot mount directly as boot volumes."
            },
            {
                "topic": "Amazon VPC Virtual Networks",
                "terms": "VPC, public vs private subnets, Internet Gateways (IGWs), route tables.",
                "lab": ["Create a VPC network wrapper", "Define CIDR block allocations", "Set up a public routing subnet"],
                "q": "What VPC component is required to route traffic from a public subnet out to the public internet?",
                "opts": ["A) NAT Gateway", "B) Internet Gateway (IGW)", "C) Customer Gateway", "D) Direct Connect"],
                "ans": "B",
                "expl": "An Internet Gateway links the VPC to the public internet, enabling bidirectional communication.",
                "dist": "NAT Gateway provides outbound-only internet access for private subnets."
            },
            {
                "topic": "AWS Network Security",
                "terms": "Security Groups (stateful) vs Network ACLs (stateless), inbound/outbound rules.",
                "lab": ["Configure a stateful Security Group rule for port 80 traffic", "Create a stateless NACL rule blocking specific subnet range", "Verify rule matching outcomes"],
                "q": "What is the key operational difference between Security Groups and Network ACLs?",
                "opts": ["A) Security Groups are stateless, NACLs are stateful", "B) Security Groups are stateful, NACLs are stateless", "C) Security Groups filter Layer 7, NACLs filter Layer 2", "D) None of the above"],
                "ans": "B",
                "expl": "Security Groups are stateful (allowing inbound traffic automatically allows return traffic). NACLs are stateless (requires explicit inbound/outbound rules).",
                "dist": "A is reversed."
            },
            {
                "topic": "AWS IAM (Identity Access Management)",
                "terms": "IAM users, groups, roles, JSON policy policies, multifactor authentication.",
                "lab": ["Add user to IAM group", "Assign policies managing EC2 permissions", "Configure multi-factor authentication requirements"],
                "q": "Which IAM identity should be assigned to an EC2 instance to allow it to securely query an S3 bucket without hardcoded keys?",
                "opts": ["A) IAM User", "B) IAM Group", "C) IAM Role", "D) Root User"],
                "ans": "C",
                "expl": "IAM Roles issue temporary security credentials to trusted services like EC2 instances.",
                "dist": "Users are for human credentials. Groups hold users."
            },
            {
                "topic": "Amazon S3 Object Storage",
                "terms": "S3 buckets, folders, storage classes (Standard, Infrequent Access, Glacier), versioning.",
                "lab": ["Create S3 storage bucket", "Upload file to bucket", "Configure versioning rules"],
                "q": "Which S3 storage class offers the lowest retrieval times and cost for archival data accessed once a year?",
                "opts": ["A) S3 Standard", "B) S3 Standard-IA", "C) Amazon S3 Glacier Deep Archive", "D) S3 One Zone-IA"],
                "ans": "C",
                "expl": "Glacier Deep Archive is AWS's lowest-cost archival tier, designed for multi-hour retrieval targets.",
                "dist": "Standard is for active data. IA is for monthly access."
            },
            {
                "topic": "Amazon EBS & EFS Storage Systems",
                "terms": "EBS volume types (SSD, HDD), EFS (multi-instance mount), instance store (ephemeral).",
                "lab": ["Attach EBS volume to running instance", "Configure disk partition formatting", "Mount EFS system on multiple targets"],
                "q": "Which storage service allows you to mount a shared file system on multiple EC2 instances concurrently?",
                "opts": ["A) Amazon EBS", "B) Amazon S3", "C) Amazon EFS (Elastic File System)", "D) Amazon Instance Store"],
                "ans": "C",
                "expl": "EFS supports the NFS protocol, allowing thousands of EC2 instances to share access to the same storage space.",
                "dist": "EBS can only mount to a single instance at a time (except special Multi-Attach volumes in same AZ)."
            },
            {
                "topic": "Amazon RDS and DynamoDB",
                "terms": "Relational Database Service (RDS), database engines, DynamoDB NoSQL key-value store.",
                "lab": ["Provision an RDS SQL server database", "Configure multi-AZ high availability deployments", "Query DynamoDB table"],
                "q": "Which AWS database service is a fully managed NoSQL key-value database designed for single-digit millisecond latency at scale?",
                "opts": ["A) Amazon RDS", "B) Amazon Aurora", "C) Amazon DynamoDB", "D) Amazon Redshift"],
                "ans": "C",
                "expl": "DynamoDB is fully managed key-value NoSQL database engine designed for scale.",
                "dist": "RDS and Aurora are relational. Redshift is data warehouse."
            },
            {
                "topic": "Elastic Load Balancing & Auto Scaling",
                "terms": "Application Load Balancer (ALB) vs Network Load Balancer (NLB), Auto Scaling Groups (ASG).",
                "lab": ["Configure target groups for Application Load Balancer", "Define scale-out threshold rules on an Auto Scaling Group", "Simulate system load spike"],
                "q": "Which type of load balancer is best suited for routing millions of ultra-low latency TCP requests at Layer 4?",
                "opts": ["A) Application Load Balancer (ALB)", "B) Network Load Balancer (NLB)", "C) Classic Load Balancer", "D) Gateway Load Balancer"],
                "ans": "B",
                "expl": "NLB operates at Layer 4 (Transport) and handles volatile network spikes and TCP/UDP traffic at extreme speeds.",
                "dist": "ALB operates at Layer 7 and evaluates HTTP headers and paths."
            },
            {
                "topic": "Route 53 & CloudFront CDN",
                "terms": "Amazon Route 53 DNS records, routing policies, CloudFront CDN edge caching.",
                "lab": ["Configure Route 53 weighted routing rules", "Create a CloudFront distribution profile", "Verify content delivery latency improvements"],
                "q": "Which routing policy in Route 53 directs client traffic to the AWS resource that offers the lowest round-trip network time?",
                "opts": ["A) Simple Routing", "B) Latency-Based Routing", "C) Geolocation Routing", "D) Failover Routing"],
                "ans": "B",
                "expl": "Latency-based routing measures network latency to direct clients to the optimal region.",
                "dist": "Geolocation routing routes based on user continent/country, not speed."
            },
            {
                "topic": "AWS Monitoring & Governance",
                "terms": "Amazon CloudWatch (metrics, alarms), AWS CloudTrail (API audit logs).",
                "lab": ["Configure a CloudWatch alarm warning on high CPU use", "Query CloudTrail logs for user logins", "Setup basic alert metrics dashboard"],
                "q": "Which service should you check to audit who made an API call to terminate an EC2 instance?",
                "opts": ["A) Amazon CloudWatch", "B) AWS CloudTrail", "C) AWS Systems Manager", "D) Amazon Inspector"],
                "ans": "B",
                "expl": "CloudTrail records all API activity, user logins, and console actions across AWS accounts.",
                "dist": "CloudWatch collects metrics and performance logs."
            },
            {
                "topic": "Serverless Implementations",
                "terms": "AWS Lambda, Amazon SNS (pub/sub), Amazon SQS (message queues).",
                "lab": ["Write a basic python AWS Lambda function triggered by S3 uploads", "Configure SQS message queue definitions", "Publish alerts to SNS topic"],
                "q": "Which service provides decoupled, asynchronously stored message queues to help design resilient architectures?",
                "opts": ["A) Amazon SNS", "B) Amazon SQS", "C) AWS Lambda", "D) AWS Step Functions"],
                "ans": "B",
                "expl": "Simple Queue Service (SQS) buffers messages between components, allowing systems to run decoupled.",
                "dist": "SNS is push notifications (pub/sub). Lambda is execution."
            },
            {
                "topic": "AWS CloudFormation (IaC)",
                "terms": "CloudFormation templates, stacks, parameters, resources declarations.",
                "lab": ["Write a CloudFormation template to deploy an S3 bucket", "Deploy template stack via console", "Verify stack creation outcomes"],
                "q": "What is the purpose of AWS CloudFormation?",
                "opts": ["A) Auto-scaling servers", "B) Provisioning resources declaratively using templates (IaC)", "C) Encrypting files", "D) Routing web traffic"],
                "ans": "B",
                "expl": "CloudFormation handles infrastructure provision automations via declarative YAML/JSON templates.",
                "dist": "It is an IaC tool, not auto-scaling or routing software."
            },
            {
                "topic": "AWS High Availability Patterns",
                "terms": "Multi-Region vs Multi-AZ deployments, active-passive vs active-active, RTO and RPO targets.",
                "lab": ["Draft high-availability architecture model", "Map out database replication paths", "Configure active-passive failover routes"],
                "q": "What term describes the maximum acceptable delay of data loss during an outage?",
                "opts": ["A) Recovery Time Objective (RTO)", "B) Recovery Point Objective (RPO)", "C) Mean Time to Repair", "D) Service Level Agreement"],
                "ans": "B",
                "expl": "Recovery Point Objective (RPO) defines how much data (measured in time) can be lost during an outage.",
                "dist": "RTO is the target recovery duration."
            },
            {
                "topic": "Well-Architected Framework",
                "terms": "The 6 pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability.",
                "lab": ["Audit system architectures against the 6 pillars framework", "Identify security improvement targets", "Optimize instance types to reduce cost"],
                "q": "Which pillar of the Well-Architected Framework focuses on running and monitoring systems to deliver business value?",
                "opts": ["A) Reliability", "B) Performance Efficiency", "C) Operational Excellence", "D) Cost Optimization"],
                "ans": "C",
                "expl": "Operational Excellence is the pillar centered on managing and continuously improving system processes.",
                "dist": "Reliability deals with recoverability. Performance deals with compute scaling."
            }
        ]
    },
    "CIS-4335_IT_Service_Management": {
        "cert": "ITIL 4 Foundation",
        "desc": "IT service management framework, service relationships, four dimensions, service value system, service value chain, and ITIL management practices.",
        "oer": "Axelos ITIL 4 Foundation Guide (axelos.com)",
        "weeks": [
            {
                "topic": "Introduction to IT Service Management",
                "terms": "IT Service Management (ITSM), ITIL history, key ITIL 4 components overview.",
                "lab": ["Map out service hierarchies", "Analyze differences between old ITIL versions and ITIL 4", "Draft basic service desk workflow"],
                "q": "What is the primary focus of ITIL 4?",
                "opts": ["A) Writing software code", "B) Co-creating value through service relationships", "C) Virtualization technologies", "D) Relational database indexing"],
                "ans": "B",
                "expl": "ITIL 4 shifts focus from simple service delivery to active value co-creation between provider and consumer.",
                "dist": "It is an administrative/managerial framework, not a software development tool."
            },
            {
                "topic": "Key Concepts: Value & Co-creation",
                "terms": "Value, utility, warranty, service relationships, service providers, service consumers.",
                "lab": ["Classify service characteristics into utility vs warranty", "Identify service providers and consumers in a case study", "Analyze customer value metrics"],
                "q": "Which term describes the functionality offered by a product or service to meet a particular need ('fit for purpose')?",
                "opts": ["A) Warranty", "B) Utility", "C) Service Relationship", "D) Value Streams"],
                "ans": "B",
                "expl": "Utility represents what the service does (fit for purpose). Warranty represents how it performs (fit for use).",
                "dist": "Warranty deals with uptime, security, and capacity."
            },
            {
                "topic": "Service Offerings and Relationships",
                "terms": "Service provision, service consumption, service relationship management.",
                "lab": ["Draft a Service Offering agreement template", "Analyze service consumer feedback reports", "Map relationship interactions"],
                "q": "What joint activity is performed by service providers and consumers to ensure continual value co-creation?",
                "opts": ["A) Service Provision", "B) Service Consumption", "C) Service Relationship Management", "D) Service Level Agreement creation"],
                "ans": "C",
                "expl": "Service Relationship Management coordinates provider and consumer interactions to facilitate value.",
                "dist": "Provision is strictly provider. Consumption is strictly consumer."
            },
            {
                "topic": "The Four Dimensions of ITSM",
                "terms": "Organizations & People, Information & Technology, Partners & Suppliers, Value Streams & Processes.",
                "lab": ["Map a case study failure to one of the four dimensions", "Examine critical suppliers relationships", "Define workflow processes for a new release"],
                "q": "Which of the four dimensions focuses on relations with other organizations involved in design, development, and delivery?",
                "opts": ["A) Organizations and People", "B) Information and Technology", "C) Partners and Suppliers", "D) Value Streams and Processes"],
                "ans": "C",
                "expl": "Partners and Suppliers addresses contracts, integrations, and relationships with vendor companies.",
                "dist": "Organizations covers structures. Value Streams covers workflows."
            },
            {
                "topic": "The Service Value System (SVS)",
                "terms": "SVS inputs, SVS outcomes (Value), SVS components (Guiding Principles, Governance, Service Value Chain, Practices, Continual Improvement).",
                "lab": ["Draw the Service Value System block diagram", "Trace opportunities from input to value output", "Map governance checks"],
                "q": "What is the primary input to the ITIL Service Value System?",
                "opts": ["A) Opportunity and Demand", "B) Incidents and Problems", "C) Budget and Funding", "D) Technology and Code"],
                "ans": "A",
                "expl": "The SVS begins with Opportunity/Demand and transforms these inputs into Value.",
                "dist": "Incidents are inputs to incident management, not the global SVS."
            },
            {
                "topic": "Service Value Chain Activities",
                "terms": "Plan, Improve, Engage, Design & Transition, Obtain/Build, Deliver & Support.",
                "lab": ["Map a release deployment through all value chain activities", "Trace Incident Management from Engage to Deliver & Support", "Document build criteria"],
                "q": "Which value chain activity ensures that service components are available when and where they are needed?",
                "opts": ["A) Design and Transition", "B) Obtain/Build", "C) Deliver and Support", "D) Plan"],
                "ans": "B",
                "expl": "Obtain/Build focuses on acquiring or building components, code, and resources.",
                "dist": "Design and Transition handles implementation. Deliver and Support handles operation."
            },
            {
                "topic": "The ITIL Guiding Principles",
                "terms": "Focus on Value, Start Where You Are, Progress Iteratively with Feedback, Collaborate and Promote Visibility, Think and Work Holistically, Keep It Simple and Practical, Optimize and Automate.",
                "lab": ["Apply guiding principles to a failed IT rollout scenario", "Analyze system dependencies", "Design automation scripts"],
                "q": "Which guiding principle recommends using existing services and processes as a baseline rather than discarding them entirely?",
                "opts": ["A) Focus on Value", "B) Start Where You Are", "C) Keep It Simple and Practical", "D) Optimize and Automate"],
                "ans": "B",
                "expl": "'Start Where You Are' advises assessing current states for reusable elements before building from scratch.",
                "dist": "Keep It Simple focuses on avoiding complexity."
            },
            {
                "topic": "Practices: Continual Improvement",
                "terms": "Continual Improvement model, improvement registers, measurement KPIs.",
                "lab": ["Draft a Continual Improvement entry for a service desk backlog", "Set target metrics", "Define measurement loops"],
                "q": "What database or tool is used to track and prioritize improvement ideas from across an organization?",
                "opts": ["A) Known Error Database", "B) Service Level Agreement", "C) Continual Improvement Register (CIR)", "D) CMDB"],
                "ans": "C",
                "expl": "The CIR records, tracks, and prioritizes improvement opportunities.",
                "dist": "Known Error Database is for problems. CMDB holds configuration items."
            },
            {
                "topic": "Practices: Change Enablement",
                "terms": "Standard changes (pre-authorized), normal changes, emergency changes, change authority.",
                "lab": ["Classify change requests into standard, normal, or emergency", "Define change authority for a major database update", "Review standard change logs"],
                "q": "Which type of change is low-risk, pre-authorized, and can be implemented without additional review?",
                "opts": ["A) Normal Change", "B) Standard Change", "C) Emergency Change", "D) Routine Change"],
                "ans": "B",
                "expl": "Standard changes are low-risk, repeat procedures that are pre-authorized by management.",
                "dist": "Normal changes require authorization cycles. Emergency changes are expedited."
            },
            {
                "topic": "Practices: Incident & Problem Management",
                "terms": "Incident definition, problem definition, workarounds, known errors, root cause analysis.",
                "lab": ["Analyze log files to differentiate incident vs problem", "Document a workaround for an application crash", "Log entry in Known Error database"],
                "q": "What is the primary difference between an incident and a problem in ITIL?",
                "opts": ["A) Incidents are larger than problems", "B) Incidents focus on restoring service; problems focus on identifying root causes", "C) Problems are reported by users; incidents by software", "D) None of the above"],
                "ans": "B",
                "expl": "Incident management restores service quickly. Problem management investigates the underlying causes of incidents.",
                "dist": "A and C are common misconceptions."
            },
            {
                "topic": "Practices: Service Desk & Request Management",
                "terms": "Service Desk channels, service requests vs incidents, request fulfillment pipelines.",
                "lab": ["Configure request categories in a mock service desk platform", "Assign request tickets to fulfillment queues", "Draft email notification templates"],
                "q": "Which of the following is classified as a Service Request rather than an Incident?",
                "opts": ["A) A printer is printing blank pages", "B) A user forgot their password and needs a reset", "C) The database server crashed", "D) A critical application is throwing errors"],
                "ans": "B",
                "expl": "Password resets are routine service requests (requests for access/information). The others represent service disruptions (incidents).",
                "dist": "Disruptions are incidents. Normal requests are service requests."
            },
            {
                "topic": "Practices: Service Level Management",
                "terms": "Service Level Agreements (SLAs), operational level agreements (OLAs), service level targets.",
                "lab": ["Draft SLA uptime metrics", "Define escalation levels in OLA documents", "Analyze SLA compliance logs"],
                "q": "What is a document that defines agreed-upon service targets between an IT provider and its customer called?",
                "opts": ["A) Service Level Agreement (SLA)", "B) Service Catalogue", "C) Service Design Package", "D) Operational Level Agreement"],
                "ans": "A",
                "expl": "The SLA details targets (e.g. 99.9% availability) agreed between provider and client.",
                "dist": "OLAs are agreements between internal departments."
            },
            {
                "topic": "Practices: Security & Relationships",
                "terms": "Information Security Management policies, relationship management, stakeholder engagement.",
                "lab": ["Review security policy guidelines", "Draft communication plan for external stakeholders", "Define access rules"],
                "q": "Which practice establishes and nurtures links between the organization and its stakeholders at strategic levels?",
                "opts": ["A) Service Desk", "B) Relationship Management", "C) Service Level Management", "D) Supplier Management"],
                "ans": "B",
                "expl": "Relationship Management identifies and maintains partnerships with clients and business units.",
                "dist": "Supplier management deals with vendors. Service desk deals with operations."
            },
            {
                "topic": "Practices: Release & Deployment Management",
                "terms": "Release packages, deployment steps, sandboxed testing, rollback plans.",
                "lab": ["Create a release transition checklist", "Define staging environment testing constraints", "Write a rollback strategy script"],
                "q": "Which practice is responsible for moving new or changed components to live environments?",
                "opts": ["A) Release Management", "B) Deployment Management", "C) Service Configuration Management", "D) Change Enablement"],
                "ans": "B",
                "expl": "Deployment Management physically moves code/hardware to live environments. Release makes services available to users.",
                "dist": "Release is the logical rollout. Deployment is the technical move."
            },
            {
                "topic": "ITIL Exam Prep Strategies",
                "terms": "ITIL 4 syllabus objectives, mock exam assessments, glossary review.",
                "lab": ["Complete a comprehensive mock exam block", "Check answers against ITIL syllabus definitions", "Identify weak areas for review"],
                "q": "What is the correct definition of a service?",
                "opts": ["A) A configuration item that runs code", "B) A means of enabling value co-creation by facilitating outcomes customers want to achieve without the customer having to manage specific costs and risks", "C) A set of resources deployed in a cloud network", "D) A contract between a buyer and seller"],
                "ans": "B",
                "expl": "This is Axelos' official definition of a service under ITIL 4.",
                "dist": "The other options represent components or contracts, not the ITIL definition."
            }
        ]
    },
    "CIS-4336_Data_Analytics": {
        "cert": "CompTIA Data+",
        "desc": "Data analytics lifecycle, database structures, data acquisition (SQL), cleaning, statistical concepts, data visualization, and data governance.",
        "oer": "CompTIA Data+ Learning Materials (comptia.org)",
        "weeks": [
            {
                "topic": "Fundamentals of Data Analytics",
                "terms": "Data analytics lifecycle, structured vs unstructured data, qualitative vs quantitative variables.",
                "lab": ["Classify raw data inputs as qualitative or quantitative", "Identify structured vs unstructured datasets", "Map the steps of the analytics lifecycle"],
                "q": "What type of data is a database table containing names, dates, and currency values classified as?",
                "opts": ["A) Unstructured data", "B) Semi-structured data", "C) Structured data", "D) Qualitative data only"],
                "ans": "C",
                "expl": "Structured data is highly organized into rigid columns and tables (e.g. relational databases).",
                "dist": "Unstructured data has no predefined schema (e.g. videos)."
            },
            {
                "topic": "Database Structures & Schemas",
                "terms": "Relational databases, primary keys, foreign keys, star schemas, snowflake schemas.",
                "lab": ["Identify primary keys in a table layout", "Link tables using foreign key relationships", "Draw a basic star schema diagram"],
                "q": "In database design, which key uniquely identifies each row within its own table?",
                "opts": ["A) Foreign Key", "B) Primary Key", "C) Candidate Key", "D) Composite Key"],
                "ans": "B",
                "expl": "A Primary Key enforces entity integrity by uniquely identifying table rows.",
                "dist": "Foreign keys link rows in separate tables."
            },
            {
                "topic": "Data Acquisition and SQL",
                "terms": "SQL SELECT, WHERE, JOIN (INNER, LEFT, RIGHT), GROUP BY, HAVING, aggregation functions.",
                "lab": ["Write SQL query: `SELECT * FROM students WHERE grade >= 90`", "Write query joining students and courses tables", "Group results by course and calculate average grade"],
                "q": "Which SQL clause is used to filter group results after aggregation has occurred?",
                "opts": ["A) WHERE", "B) HAVING", "C) GROUP BY", "D) SELECT"],
                "ans": "B",
                "expl": "`HAVING` filters aggregated values. `WHERE` filters individual rows before aggregation.",
                "dist": "WHERE filters rows beforehand."
            },
            {
                "topic": "Data Cleaning & Normalization",
                "terms": "Deduplication, handling missing values, type casting, text cleaning (regex), normalizing schemas.",
                "lab": ["Deduplicate a list of transaction records", "Convert text columns to uppercase", "Handle empty entries using baseline values"],
                "q": "What is the primary goal of data normalization?",
                "opts": ["A) Compressing files to save space", "B) Reducing data redundancy and improving data integrity", "C) Creating visual charts", "D) Encrypting data"],
                "ans": "B",
                "expl": "Normalization splits data into smaller tables to reduce redundant duplicates and avoid anomaly risks.",
                "dist": "It is not for compression or encryption."
            },
            {
                "topic": "Handling Missing Data and Outliers",
                "terms": "Imputation, deletion methods, identifying outliers using Z-score and Interquartile Range (IQR).",
                "lab": ["Calculate IQR for a dataset of house prices", "Identify outlier prices using IQR thresholds", "Impute missing ages using dataset median"],
                "q": "Which method involves replacing missing dataset values with statistical estimates like mean or median?",
                "opts": ["A) Deletion", "B) Imputation", "C) Normalization", "D) Deduplication"],
                "ans": "B",
                "expl": "Imputation calculates replacing values rather than omitting records entirely.",
                "dist": "Deletion drops rows. Deduplication removes duplicates."
            },
            {
                "topic": "Data Profiling and Verification",
                "terms": "Data quality dimensions (accuracy, completeness, consistency, validity, uniqueness), profiling statistics.",
                "lab": ["Profile a database table to count null percentages", "Validate formats of zip codes and email entries", "Identify duplicate rows"],
                "q": "Which data quality dimension measures whether all required data fields are populated in a record?",
                "opts": ["A) Accuracy", "B) Completeness", "C) Consistency", "D) Validity"],
                "ans": "B",
                "expl": "Completeness confirms that all expected attributes are recorded, leaving no missing entries.",
                "dist": "Accuracy checks for correctness. Validity checks for format alignment."
            },
            {
                "topic": "Basic Statistical Concepts",
                "terms": "Mean, median, mode, standard deviation, variance, range.",
                "lab": ["Calculate mean and median for a set of test scores", "Analyze variance between two score sheets", "Determine mode"],
                "q": "Which statistical metric represents the middle value of a sorted list of numbers?",
                "opts": ["A) Mean", "B) Median", "C) Mode", "D) Variance"],
                "ans": "B",
                "expl": "The median divides the sorted dataset in half, representing the exact middle value.",
                "dist": "Mean is the average. Mode is the most frequent."
            },
            {
                "topic": "Descriptive vs Inferential Statistics",
                "terms": "Population vs sample, descriptive statistics summaries, hypothesis testing, p-values.",
                "lab": ["Differentiate population vs sample data parameters", "Generate summary charts", "Analyze p-value significance in a mock A/B test report"],
                "q": "Which type of statistics uses sample data to make predictions or draw conclusions about a larger population?",
                "opts": ["A) Descriptive Statistics", "B) Inferential Statistics", "C) Qualitative Statistics", "D) Mathematical Statistics"],
                "ans": "B",
                "expl": "Inferential statistics uses hypothesis tests and samples to infer traits about larger populations.",
                "dist": "Descriptive statistics only summarizes the data at hand."
            },
            {
                "topic": "Data Visualization Principles",
                "terms": "Chart types (bar, line, scatter, pie, box-and-whisker), color choices, labeling best practices.",
                "lab": ["Select appropriate charts for showing sales trends over time (Line) vs relationships (Scatter)", "Audit color palettes for accessibility", "Format chart axes"],
                "q": "Which chart type is best suited for showing the relationship or correlation between two numerical variables?",
                "opts": ["A) Bar Chart", "B) Line Chart", "C) Scatter Plot", "D) Pie Chart"],
                "ans": "C",
                "expl": "Scatter plots map two metrics on x and y axes to show distribution correlations.",
                "dist": "Line charts show trends over time. Bar charts compare categorical values."
            },
            {
                "topic": "Creating Dashboards & Reports",
                "terms": "Dashboard layouts, filter controls, drill-down parameters, report distribution.",
                "lab": ["Wireframe a KPI dashboard layout", "Configure filter requirements for regional sales data", "Select key metrics for dashboard header"],
                "q": "Why should dashboards have interactive filters?",
                "opts": ["A) To speed up database processing", "B) To allow users to drill down and customize the data shown", "C) To secure the server", "D) To compile code"],
                "ans": "B",
                "expl": "Interactive filters let business users segment data (e.g. by region or date) without requiring new custom reports.",
                "dist": "Filters do not speed up backend database configurations."
            },
            {
                "topic": "KPIs & Business Metrics",
                "terms": "Key Performance Indicators (KPIs), metrics, baseline targets, dashboard design.",
                "lab": ["Define KPIs for customer retention", "Calculate growth rates based on baseline targets", "Review metrics alignment"],
                "q": "What makes a metric a Key Performance Indicator (KPI)?",
                "opts": ["A) It is generated by an SQL query", "B) It aligns directly with critical business goals and measures success", "C) It is represented as a percentage", "D) None of the above"],
                "ans": "B",
                "expl": "KPIs measure success against defined strategic priorities, unlike general telemetry metrics.",
                "dist": "Any data is a metric, but only critical success metrics are KPIs."
            },
            {
                "topic": "Data Analysis Methods",
                "terms": "Cohort analysis, churn rate, trend analysis, predictive forecasting.",
                "lab": ["Calculate monthly churn rate for a subscription dataset", "Review a cohort analysis table grid", "Chart historical trends to predict next month sales"],
                "q": "Which analysis method groups users based on a shared characteristic or start date to track behavior over time?",
                "opts": ["A) Churn Analysis", "B) Cohort Analysis", "C) Outlier Analysis", "D) Regression Analysis"],
                "ans": "B",
                "expl": "Cohort analysis tracks defined groups over time to identify usage or drop-off trends.",
                "dist": "Churn only tracks cancellations."
            },
            {
                "topic": "Data Governance & Privacy",
                "terms": "Data privacy laws (GDPR, CCPA), personally identifiable information (PII), data masking, access control.",
                "lab": ["Identify PII columns in a customer dataset (e.g. email, SSN)", "Apply data masking to hide credit card digits", "Document data access roles"],
                "q": "Which of the following is classified as Personally Identifiable Information (PII)?",
                "opts": ["A) Server uptime stats", "B) Aggregate store sales totals", "C) Email address and Social Security Number", "D) Operating system version"],
                "ans": "C",
                "expl": "PII is any information that can identify a specific individual.",
                "dist": "Uptime, sales totals, and OS versions do not identify individuals."
            },
            {
                "topic": "Data Warehousing and ETL",
                "terms": "Extract, Transform, Load (ETL), data lakes, data warehouses, schema migrations.",
                "lab": ["Design an ETL pipeline workflow", "Map transformation steps: format, clean, compute", "Define warehouse loading schema"],
                "q": "What does the 'Transform' step in an ETL pipeline involve?",
                "opts": ["A) Extracting raw data from sources", "B) Cleaning, formatting, and preparing the data for analysis", "C) Loading the data into a data warehouse", "D) Backing up the files"],
                "ans": "B",
                "expl": "Transformation converts data from source schemas to target structures, cleaning and verifying it.",
                "dist": "Extract is retrieval. Load is writing to target."
            },
            {
                "topic": "Data Quality Controls",
                "terms": "Establishing data quality baselines, automated alerts on quality checks.",
                "lab": ["Write a script verifying that email columns match standard regex formats", "Set up warning thresholds on null value counts", "Verify datatypes match schema"],
                "q": "What is the purpose of running data quality checks during ingestion?",
                "opts": ["A) To encrypt datasets", "B) To catch and isolate corrupt records before they pollute dashboards", "C) To compress log files", "D) None of the above"],
                "ans": "B",
                "expl": "Checks verify that incoming data conforms to validation rules, stopping malformed inputs before they disrupt metrics.",
                "dist": "It is not for compression or encryption."
            }
        ]
    },
    "CIS-4337_Infrastructure_Automation": {
        "cert": "HashiCorp Certified: Terraform Associate",
        "desc": "Infrastructure as Code (IaC) concepts, Terraform settings, providers, state management, modules, workspaces, and CI/CD pipelines.",
        "oer": "HashiCorp Learn Platform (learn.hashicorp.com)",
        "weeks": [
            {
                "topic": "IaC Concepts & Benefits",
                "terms": "Infrastructure as Code (IaC), declarative vs imperative, drift, state, automation.",
                "lab": ["Compare manual server provisioning vs automated script configuration", "Review declarative IaC configurations", "Examine infrastructure drift symptoms"],
                "q": "What is a primary advantage of declarative IaC over imperative scripting?",
                "opts": ["A) Declarative requires detailing exact deployment commands", "B) Declarative defines the target end-state; the tool handles deployment steps", "C) Declarative executes faster", "D) Declarative does not require code"],
                "ans": "B",
                "expl": "Declarative tools (like Terraform) allow you to specify 'what' you want, rather than scripting the 'how' step-by-step.",
                "dist": "Imperative requires detailing exact script commands."
            },
            {
                "topic": "Terraform Architecture",
                "terms": "Terraform Core, plugins, providers, HCL (HashiCorp Configuration Language), terraform init.",
                "lab": ["Install Terraform CLI local binary", "Create `main.tf` configuration wrapper", "Initialize directory: `terraform init`"],
                "q": "Which command downloads and installs the provider plugins defined in your Terraform configuration files?",
                "opts": ["A) terraform apply", "B) terraform init", "C) terraform plan", "D) terraform get"],
                "ans": "B",
                "expl": "`terraform init` initializes the folder, creating directory paths and downloading required provider plugins.",
                "dist": "apply deploys resources. plan creates templates. get fetches modules."
            },
            {
                "topic": "Settings, Providers, & Resources",
                "terms": "Terraform blocks, provider block parameters, resource block parameters, dependency resolution.",
                "lab": ["Configure a provider (e.g. AWS or Local)", "Declare a resource block creating a file or instance", "Deploy changes: `terraform apply`"],
                "q": "What block type in HCL is used to configure plugins that interact with cloud platforms (e.g., AWS, Azure)?",
                "opts": ["A) resource", "B) variable", "C) provider", "D) output"],
                "ans": "C",
                "expl": "The `provider` block configures the plugins that translate HCL declarations into API calls.",
                "dist": "resource declares infrastructure objects."
            },
            {
                "topic": "Terraform Variables & Outputs",
                "terms": "Input variables (string, list, map), default parameters, outputs, local variables.",
                "lab": ["Define input variables for resource parameters", "Set variable values in a `terraform.tfvars` file", "Declare outputs to print deployment values"],
                "q": "Which file extension is default for storing variable values in a Terraform project?",
                "opts": ["A) .tf", "B) .tfvars", "C) .json", "D) .hcl"],
                "ans": "B",
                "expl": "Terraform automatically loads variables values from files ending with `.tfvars`.",
                "dist": ".tf stores declarations. .json is alternative layout."
            },
            {
                "topic": "Terraform State Management",
                "terms": "Terraform state (`terraform.tfstate`), state tracking, mapping local files to cloud APIs.",
                "lab": ["Inspect state file content details: `terraform.tfstate`", "Query state registry list: `terraform state list`", "Examine sensitive attributes stored inside state"],
                "q": "What is the primary purpose of the `terraform.tfstate` file?",
                "opts": ["A) To store user passwords", "B) To map HCL declarations directly to real-world resources", "C) To write shell logs", "D) To compile python modules"],
                "ans": "B",
                "expl": "The state file acts as a database mapping your configuration declarations to the actual IDs of deployed cloud resources.",
                "dist": "State files store metadata maps."
            },
            {
                "topic": "State Locking & Backends",
                "terms": "Remote backends (S3, GCS, Terraform Cloud), state locking, DynamoDB configurations.",
                "lab": ["Configure remote backend storage block using S3", "Configure state locking using DynamoDB table settings", "Deploy config to verify lock state behavior"],
                "q": "Why is state locking critical in enterprise team environments?",
                "opts": ["A) To encrypt variables", "B) To prevent concurrent runs from corrupting the state file", "C) To speed up provisioning", "D) None of the above"],
                "ans": "B",
                "expl": "State locking ensures that if two users run `apply` at the same time, one is queued to avoid overwriting or corruption.",
                "dist": "Locks do not accelerate deployments or encrypt variables."
            },
            {
                "topic": "Provisioners & Local Exec",
                "terms": "Provisioners (`local-exec`, `remote-exec`), connection blocks, provisioner warnings.",
                "lab": ["Declare a `local-exec` provisioner inside a resource block", "Run a local shell command outputting logs on apply", "Review warnings regarding provisioner dependency risks"],
                "q": "Which provisioner executes a command on the machine running the Terraform CLI?",
                "opts": ["A) remote-exec", "B) local-exec", "C) host-exec", "D) system-exec"],
                "ans": "B",
                "expl": "The `local-exec` provisioner runs commands locally on the operator's shell system.",
                "dist": "remote-exec runs command inside the deployed target virtual machine."
            },
            {
                "topic": "Data Sources & Dynamic Blocks",
                "terms": "Data blocks (read-only queries), dynamic content generation (for_each loops), dynamic blocks.",
                "lab": ["Declare a `data` block to fetch existing VPC configurations", "Use dynamic blocks to loop security rules", "Verify output"],
                "q": "Which block type allows you to query API data from a provider without creating a new resource?",
                "opts": ["A) resource", "B) data", "C) variable", "D) locals"],
                "ans": "B",
                "expl": "Data sources (`data` blocks) read configurations directly from target APIs (e.g. searching for AMI lists).",
                "dist": "resource blocks declare objects that Terraform should manage/create."
            },
            {
                "topic": "HCL Functions & Expressions",
                "terms": "Interpolation, built-in functions (lookup, element, join, file), conditional operators.",
                "lab": ["Test HCL expressions using `terraform console`", "Use `file()` function to load user-data scripts", "Write a conditional statement choosing CPU size based on environment"],
                "q": "Which built-in Terraform function retrieves a value from a map given its key?",
                "opts": ["A) find()", "B) lookup()", "C) element()", "D) map()"],
                "ans": "B",
                "expl": "The `lookup(map, key, default)` function queries map variables dynamically.",
                "dist": "element() retrieves items from lists. find() is not a Terraform function."
            },
            {
                "topic": "Terraform Modules",
                "terms": "Module definition, root module, child modules, input parameters, module output mapping.",
                "lab": ["Create a reusable child module layout under `modules/`", "Declare child module inputs and outputs", "Call the module from root configuration files"],
                "q": "What HCL parameter is required inside a module block to define the location of the module code?",
                "opts": ["A) path", "B) source", "C) location", "D) directory"],
                "ans": "B",
                "expl": "The `source` parameter defines where the module code lives (local folder or registry URL).",
                "dist": "path, location, and directory are not valid HCL parameters."
            },
            {
                "topic": "Workspaces & Multi-Env",
                "terms": "Terraform workspaces, default workspace, workspace directories, workspace isolation.",
                "lab": ["List workspaces: `terraform workspace list`", "Create development workspace: `terraform workspace new dev`", "Deploy resources dynamically named after workspace parameter"],
                "q": "Which environment variable/parameter references the name of the current active Terraform workspace?",
                "opts": ["A) var.workspace", "B) terraform.workspace", "C) local.workspace", "D) active.workspace"],
                "ans": "B",
                "expl": "The `terraform.workspace` path returns the current active workspace name (e.g. 'prod' or 'dev').",
                "dist": "It is a built-in object, not a variable prefix."
            },
            {
                "topic": "Drift Management & Importing",
                "terms": "Infrastructure drift, importing existing resources (`terraform import`), drift reconciliation.",
                "lab": ["Manually modify a file size in console", "Run `terraform plan` to detect the drift", "Import a mock external resource into HCL code configuration"],
                "q": "Which command reads real-world resource details and registers them inside your local state file?",
                "opts": ["A) terraform apply", "B) terraform import", "C) terraform plan", "D) terraform state push"],
                "ans": "B",
                "expl": "`terraform import` reads the target ID and populates it inside your state. You must manually write the matching HCL code.",
                "dist": "import does not generate HCL code; it only writes state."
            },
            {
                "topic": "Terraform Cloud & Registry",
                "terms": "Terraform Cloud workspaces, VCS connection, private registry, run triggers.",
                "lab": ["Configure a cloud workspace connection", "Examine VCS trigger behaviors", "Map run approvals workflow"],
                "q": "Where does state storage and HCL compilation execute when using a VCS-connected Terraform Cloud workspace?",
                "opts": ["A) On the developer's laptop", "B) In the Terraform Cloud remote runtime environment", "C) In the target virtual machine", "D) On the GitHub server"],
                "ans": "B",
                "expl": "Terraform Cloud acts as a remote agent, running `plan` and `apply` actions on its own containers, storing state securely.",
                "dist": "It handles operations remotely, freeing developers from local execution requirements."
            },
            {
                "topic": "Terraform in CI/CD Pipelines",
                "terms": "GitHub Actions, GitLab CI, non-interactive execution (`-auto-approve`), linting/validation.",
                "lab": ["Write a GitHub Actions YAML workflow file", "Run `terraform validate` in pipeline workflow", "Configure automated plan prints on pull requests"],
                "q": "Which flag must be appended to the `apply` command in automation pipelines to prevent it from waiting for user confirmation?",
                "opts": ["A) --force", "B) -auto-approve", "C) --yes", "D) --silent"],
                "ans": "B",
                "expl": "The `-auto-approve` flag executes the apply changes immediately without prompting the console operator.",
                "dist": "--force, --yes, and --silent are not valid CLI options."
            },
            {
                "topic": "Terraform Security & Secrets",
                "terms": "Secret management guidelines, avoiding hardcoded keys, environment variables, sensitive outputs.",
                "lab": ["Mark variable as sensitive: `sensitive = true`", "Verify output does not display values in CLI console", "Inject keys using `TF_VAR_` environment variables"],
                "q": "Which HCL variable attribute prevents its value from being printed to the console stdout during apply runs?",
                "opts": ["A) write = false", "B) sensitive = true", "C) hidden = true", "D) secret = true"],
                "ans": "B",
                "expl": "Declaring `sensitive = true` instructs Terraform to mask the values in logs and console outputs.",
                "dist": "The value is still written to the state file in plain text, making backend security critical."
            }
        ]
    }
}

def generate_video_script(cert, week_num, topic, terms, lab):
    return f"""# Video Script: {cert}
## Module {week_num:02d} - {topic}
**Estimated Duration:** 7 minutes

---

### [00:00 - 01:30] Introduction and Objective
**Visual:** Instructor on camera.
**Audio:** "Welcome back, class. In this module, we are diving deep into **{topic}**, which is a core objective for the {cert} exam. Understanding these concepts is critical before you proceed to your hands-on labs, as the certification exam tests both theoretical design and practical troubleshooting."

---

### [01:30 - 04:30] Core Concepts Breakdown
**Visual:** Whiteboard diagram illustrating the concepts.
**[Alt-text: A diagram depicting key elements of {topic}, detailing the relationships and communication flow between components.]**

**Audio:** "When we discuss **{topic}**, we are looking at:
*   **Key Terminology:** {terms}
*   **Core Functions:** It is essential to memorize the parameters, syntax, and behaviors associated with this layer. 
*   **Operational Context:** In production environments, misconfiguring these settings leads to systemic failures or security vulnerabilities. Make sure you take notes on these specific configurations."

---

### [04:30 - 06:00] Applied Lab Walkthrough
**Visual:** Screencast of the terminal environment showing configuration commands.
**[Alt-text: A console screenshot demonstrating execution of configuration commands for {topic}.]**

**Audio:** "For this week's lab, you will perform active configurations. You will execute commands like:
*   `{lab[0] if len(lab) > 0 else 'Initial setup commands'}`
*   `{lab[1] if len(lab) > 1 else 'Verification commands'}`
*   Remember to always verify your configurations using diagnostic tools before submitting your work."

---

### [06:00 - 07:00] Summary and Quiz Prep
**Visual:** Text slide showing key exam takeaways.
**Audio:** "To wrap up, focus on parsing the differences between various states and commands. Review the OER guide and test your knowledge with the weekly quiz. In the next module, we'll continue our progression. Keep practicing, and I'll see you in the next session."
"""

def generate_reading_guide(cert, week_num, topic, terms):
    return f"""### Reading Guide: {topic}
**Course:** {cert} Module {week_num:02d}

**Zero Textbook Cost (ZTC) Resource Link:**
Please refer to the `ZTC_OER_Reading_Materials.md` file located in the root of the course directory for active links to the free, official Open Educational Resources (OER) for this module.

---

### High-Yield Summaries

*   **Core Concepts:**
    This module centers on **{topic}**. You must master the following primary technologies:
    *   **Focus Areas:** {terms}
    
*   **Exam Tips:**
    *   Memorize common command syntax, flags, port numbers, and protocol types associated with {topic}.
    *   Be prepared to troubleshoot configurations based on output log error codes.

*   **Reference Documentation:**
    Always cross-reference your studies with the official vendor documentation linked in the ZTC materials (Microsoft Learn, AWS Documentation, HashiCorp Learn, or CompTIA objectives) to ensure currency.
"""

def generate_lab_activity(cert, week_num, topic, lab):
    steps_md = "\n".join(f"{idx+1}. {step}" for idx, step in enumerate(lab))
    return f"""### Lab {week_num:02d}: Applied {topic}
**Target Certification:** {cert}

**Objective:**
Apply theoretical knowledge of **{topic}** in a hands-on lab environment to construct and verify a working configuration.

---

### Instructions

{steps_md}

---

### Deliverable

1. Capture a clear screenshot of your terminal/console showing the successful execution of the final verification step.
2. Save your command log or output file.
3. Upload these files to the Blackboard assignment drop-box.

*Note: Ensure all output matches the expected parameters defined in the lab guidelines. Run the `txwes-submit.sh` tool if required by your instructor.*
"""

def generate_quiz(cert, week_num, topic, q, opts, ans, expl, dist):
    # Determine correct letter
    correct_letter = ans
    
    opts_md = "\n".join(opts)
    
    return f"""### Quiz {week_num:02d}: {topic} Question Bank

**Question 1:**
{q}

{opts_md}

---

*   **Correct Answer:** {correct_letter}
*   **Explanation:**
    {expl}
*   **Distractor Analysis:**
    {dist}
"""

def main():
    print("=== STARTING SPECIFIC CONTENT GENERATION ===")
    
    for course_id, data in COURSES_DATA.items():
        cert = data["cert"]
        weeks = data["weeks"]
        course_path = os.path.join(BASE_DIR, course_id)
        
        print(f"Generating content for {course_id}...")
        
        for idx, week_data in enumerate(weeks):
            week_num = idx + 1
            mod_name = f"Module_{week_num:02d}"
            mod_path = os.path.join(course_path, mod_name)
            
            # Ensure the directory exists
            os.makedirs(mod_path, exist_ok=True)
            
            topic = week_data["topic"]
            terms = week_data["terms"]
            lab = week_data["lab"]
            q = week_data["q"]
            opts = week_data["opts"]
            ans = week_data["ans"]
            expl = week_data["expl"]
            dist = week_data["dist"]
            
            # 1. Video Script
            video_filename = f"01_Video_Script_Module_{week_num:02d}.md"
            video_content = generate_video_script(cert, week_num, topic, terms, lab)
            with open(os.path.join(mod_path, video_filename), 'w') as f:
                f.write(video_content)
                
            # 2. Reading Guide
            reading_filename = f"02_Reading_Guide_Module_{week_num:02d}.md"
            reading_content = generate_reading_guide(cert, week_num, topic, terms)
            with open(os.path.join(mod_path, reading_filename), 'w') as f:
                f.write(reading_content)
                
            # 3. Lab Activity
            lab_filename = f"03_Lab_Module_{week_num:02d}.md"
            lab_content = generate_lab_activity(cert, week_num, topic, lab)
            with open(os.path.join(mod_path, lab_filename), 'w') as f:
                f.write(lab_content)
                
            # 4. Quiz
            quiz_filename = f"04_Quiz_Module_{week_num:02d}.md"
            quiz_content = generate_quiz(cert, week_num, topic, q, opts, ans, expl, dist)
            with open(os.path.join(mod_path, quiz_filename), 'w') as f:
                f.write(quiz_content)

        # Ensure Module 16 exists with correct exam details
        mod_16_path = os.path.join(course_path, "Module_16")
        os.makedirs(mod_16_path, exist_ok=True)
        
        # 16 Reading Guide
        with open(os.path.join(mod_16_path, "02_Reading_Guide_Module_16.md"), 'w') as f:
            f.write(f"### Reading Guide: Final Exam Preparation\n\nReview all study guides, video scripts, and practice questions from Module 01 through Module 15 in preparation for the official **{cert}** certification exam.")
            
        # 16 Activity
        with open(os.path.join(mod_16_path, "03_Lab_Module_16.md"), 'w') as f:
            f.write(f"### Final Exam Submission\n\n**Objective:** Complete the official **{cert}** certification exam at the designated ComputerMinds testing center.\n\n**Instructions:**\n1. Register and schedule your certification exam through the official portal.\n2. Complete the exam.\n3. Upload a scan or digital PDF copy of your official score report to this dropbox to receive credit.")
            
        # Delete any leftover non-prefixed files in Module 16 if they exist
        for old_file in ["Reading_Guide_Module_16.md", "Final_Exam_Submission.md", "03_Final_Exam_Submission.md"]:
            old_path = os.path.join(mod_16_path, old_file)
            if os.path.exists(old_path):
                os.remove(old_path)
                
            # Also check inside subdirectories (in case any old folders remained)
            for sub in ["01_Video_Scripts", "02_Reading_Guides", "03_Activities", "Assessments"]:
                sub_path = os.path.join(mod_16_path, sub)
                if os.path.exists(sub_path):
                    shutil.rmtree(sub_path)

    print("=== GENERATION OF ALL REAL CONTENT COMPLETED ===")

if __name__ == "__main__":
    main()
