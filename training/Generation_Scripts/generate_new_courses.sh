#!/bin/bash
# generate_new_courses.sh - Scaffolds and populates 10 new courses using standard Bash scripting

BASE_DIR="/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"

declare -A CERTS
CERTS["CIS-2315_Data_Structures_Algorithms"]="Technical Interview Readiness (LeetCode / HackerRank)"
CERTS["CIS-3340_Full_Stack_Web_Dev"]="AWS Certified Developer - Associate"
CERTS["CIS-3350_Software_Engineering_Agile"]="Professional Scrum Master (PSM I)"
CERTS["CIS-4345_Machine_Learning_Deep_Learning"]="TensorFlow Developer Certificate"
CERTS["CIS-3310_IT_Project_Management"]="CompTIA Project+ / PMI CAPM"
CERTS["CIS-3312_Systems_Analysis_Design"]="IIBA Entry Certificate in Business Analysis (ECBA)"
CERTS["CIS-4315_Cyber_Governance_Risk_Compliance"]="ISACA Certified Information Security Manager (CISM)"
CERTS["CIS-4320_Enterprise_Systems_ERP"]="Salesforce Certified Associate / SAP Certified Associate"
CERTS["CIS-4350_DevSecOps_CICD_Pipelines"]="Certified DevSecOps Professional (CDP)"
CERTS["CIS-4355_IoT_Embedded_Systems"]="IoT & Embedded Security (General Principles)"

declare -A DESCS
DESCS["CIS-2315_Data_Structures_Algorithms"]="Data structures and algorithms, time and space complexity, recursion, balanced trees, heaps, graphs, sorting, and dynamic programming."
DESCS["CIS-3340_Full_Stack_Web_Dev"]="HTML5, CSS layouts, asynchronous JavaScript, REST APIs, Express servers, databases, React hooks, JWT security, and AWS EC2/S3 cloud deployment."
DESCS["CIS-3350_Software_Engineering_Agile"]="SDLC phases, Git workflows, clean code, SOLID patterns, testing, Scrum roles, sprint ceremonies, backlog grooming, and Agile relative sizing."
DESCS["CIS-4345_Machine_Learning_Deep_Learning"]="ML pipelines, regression models, classification performance, SVM, random forests, dimensionality reduction, neural networks, CNNs, LSTMs, and model serving."
DESCS["CIS-3310_IT_Project_Management"]="Project charters, WBS packages, Gantt chart scheduling, critical path slack times, cost baseline estimates, RACI maps, risk registers, and change controls."
DESCS["CIS-3312_Systems_Analysis_Design"]="System analyst functions, feasibility tests, requirements elicitation, use case modeling, process flow mapping (DFDs), normalization, UAT, and installation cutovers."
DESCS["CIS-4315_Cyber_Governance_Risk_Compliance"]="Security steering committees, policies vs standards, NIST Risk Management Framework, quantitative ALE calculation, BIA recovery objectives, GDPR privacy, and SOC auditing."
DESCS["CIS-4320_Enterprise_Systems_ERP"]="ERP database integrations, business processes mapping (BPMN), ledger accounting, MRP supply chains, Salesforce/SAP customize triggers, ETL migrations, and RBAC Separation of Duties."
DESCS["CIS-4350_DevSecOps_CICD_Pipelines"]="DevSecOps shift-left automation, commit linters, GitHub Actions YAML workflows, Docker setups, SAST/DAST testing, SCA dependencies, Vault secret masking, and chaos injections."
DESCS["CIS-4355_IoT_Embedded_Systems"]="IoT sensing layer interfaces, bitwise GPIO operations, memory constraints, RTOS scheduling, MQTT pub-sub, secure boot verification, OTA signing, and edge processing."

declare -A OERS
OERS["CIS-2315_Data_Structures_Algorithms"]="OpenDSA (opendsa-server.cs.vt.edu)"
OERS["CIS-3340_Full_Stack_Web_Dev"]="Mozilla Developer Network (developer.mozilla.org)"
OERS["CIS-3350_Software_Engineering_Agile"]="Official Scrum Guide (scrumguides.org)"
OERS["CIS-4345_Machine_Learning_Deep_Learning"]="Scikit-Learn & TensorFlow Documentation (scikit-learn.org / tensorflow.org)"
OERS["CIS-3310_IT_Project_Management"]="PMI Project Management Body of Knowledge (PMBOK Guide)"
OERS["CIS-3312_Systems_Analysis_Design"]="IIBA Business Analysis Body of Knowledge (BABOK Guide)"
OERS["CIS-4315_Cyber_Governance_Risk_Compliance"]="NIST Cybersecurity Framework (nist.gov/cyberframework)"
OERS["CIS-4320_Enterprise_Systems_ERP"]="Salesforce Trailhead (trailhead.salesforce.com)"
OERS["CIS-4350_DevSecOps_CICD_Pipelines"]="DevSecOps Reference Architecture (devsecops.org)"
OERS["CIS-4355_IoT_Embedded_Systems"]="OWASP IoT Security Project (owasp.org/www-project-internet-of-things)"

# Function to get week data for a course
get_week_data() {
  local course=$1
  local week=$2
  
  case "$course" in
    "CIS-2315_Data_Structures_Algorithms")
      case "$week" in
        1)
          TOPIC="Time & Space Complexity"
          TERMS="Big-O notation, space complexity, asymptotic analysis, worst-case, best-case, average-case."
          LAB_STEPS="1. Analyze time complexity of a loop script\n2. Measure execution time of linear search vs binary search\n3. Document space overhead of arrays"
          Q="What is the worst-case time complexity of inserting an element into a standard dynamic array (ArrayList) when it needs resizing?"
          OPTS="A) O(1)\nB) O(log N)\nC) O(N)\nD) O(N log N)"
          ANS="C"
          EXPL="When a dynamic array runs out of capacity, it must allocate a new larger array and copy all N elements, taking O(N) time."
          DIST="O(1) is the amortized insertion time. O(log N) is for binary search trees."
          ;;
        2)
          TOPIC="Singly & Doubly Linked Lists"
          TERMS="Node pointer, head node, tail node, doubly linked nodes, traversal overhead."
          LAB_STEPS="1. Implement a singly linked list class in Python\n2. Write a method to reverse a singly linked list\n3. Measure traversal times"
          Q="What is the primary advantage of a doubly linked list over a singly linked list?"
          OPTS="A) Requires less memory per node\nB) Allows traversal in both directions (forward and backward)\nC) O(1) random index access\nD) Faster sorting speed"
          ANS="B"
          EXPL="Each node in a doubly linked list contains pointers to both the next and previous nodes, allowing bidirectional traversal."
          DIST="It requires more memory due to the extra pointer. Accessing a random index still takes O(N) time."
          ;;
        3)
          TOPIC="Stacks & Queues"
          TERMS="LIFO (Last-In-First-Out), FIFO (First-In-First-Out), push/pop, enqueue/dequeue."
          LAB_STEPS="1. Build a stack class using a list wrapper\n2. Build a queue using collections.deque\n3. Implement a matching parenthesis algorithm"
          Q="Which data structure follows the LIFO (Last-In-First-Out) principle?"
          OPTS="A) Queue\nB) Priority Queue\nC) Stack\nD) Hash Table"
          ANS="C"
          EXPL="A Stack works by inserting and removing from the same end, matching Last-In-First-Out behavior."
          DIST="Queue is FIFO. Priority Queue removes based on key value. Hash Table uses keys."
          ;;
        4)
          TOPIC="Recursion & Backtracking"
          TERMS="Base case, recursive call, stack overflow risk, call stack frame."
          LAB_STEPS="1. Write a recursive function to compute Fibonacci numbers\n2. Write a recursive factorial finder\n3. Debug recursive call stacks"
          Q="What must every functional recursive function include to avoid infinite recursion and stack overflow?"
          OPTS="A) A global loop variable\nB) A base case that terminates recursion\nC) A try-except error wrapper\nD) A class destructor"
          ANS="B"
          EXPL="The base case acts as the exit condition where the recursion stops calling itself."
          DIST="A recursive function does not require loops, try-except blocks, or class destructors to terminate."
          ;;
        5)
          TOPIC="Binary Trees & BSTs"
          TERMS="Root node, leaf node, binary search tree invariant, left child, right child."
          LAB_STEPS="1. Define a TreeNode class\n2. Implement insert and find methods for a BST\n3. Verify tree traversal orders (inorder, preorder, postorder)"
          Q="In a valid Binary Search Tree (BST), what property must be true for every node N?"
          OPTS="A) All left descendants <= N, and all right descendants > N\nB) Left child and right child must have equal height\nC) Every node must have exactly two child nodes\nD) The tree must be balanced"
          ANS="A"
          EXPL="The BST invariant requires all values in the left subtree of N to be less than or equal to N, and all values in the right subtree to be greater."
          DIST="Equal height defines balanced trees. Node count properties define strict binary trees."
          ;;
        6)
          TOPIC="AVL Trees & Red-Black Trees"
          TERMS="Self-balancing tree, balance factor, tree rotation, node recoloring."
          LAB_STEPS="1. Simulate balance factor calculation of nodes\n2. Trace left/right tree rotations on paper\n3. Draw AVL inserts step-by-step"
          Q="What is the maximum height of an AVL tree containing N nodes?"
          OPTS="A) O(1)\nB) O(log N)\nC) O(N)\nD) O(N^2)"
          ANS="B"
          EXPL="AVL trees guarantee a logarithmic height by maintaining a strict balance factor difference of at most 1."
          DIST="O(N) is the height of an unbalanced degenerate tree (linked list)."
          ;;
        7)
          TOPIC="Heaps & Priority Queues"
          TERMS="Min-heap, max-heap, heapify, complete binary tree, array representation."
          LAB_STEPS="1. Build a min-heap array index mapper\n2. Use Python heapq module to sort a list\n3. Find top K elements using heaps"
          Q="Which array index represents the parent of a node located at index i in a 0-indexed binary heap?"
          OPTS="A) 2*i + 1\nB) 2*i + 2\nC) (i - 1) // 2\nD) i // 2"
          ANS="C"
          EXPL="For any 0-indexed element i, its parent is located at index floor((i-1)/2)."
          DIST="2*i+1 is left child. 2*i+2 is right child."
          ;;
        8)
          TOPIC="Hash Tables & Hash Collisions"
          TERMS="Hash function, load factor, collision resolution, chaining, open addressing."
          LAB_STEPS="1. Implement a simple modulo hash table\n2. Simulate collision resolution using linear probing\n3. Compare lookup times"
          Q="What is the average-case time complexity of searching for a key in a well-distributed Hash Table?"
          OPTS="A) O(1)\nB) O(log N)\nC) O(N)\nD) O(N log N)"
          ANS="A"
          EXPL="If the hash function distributes keys evenly, finding a key via constant hash mapping takes O(1) time."
          DIST="O(N) is the worst-case hash table lookup (when all keys collide into a single chain)."
          ;;
        9)
          TOPIC="Graph Representations"
          TERMS="Adjacency matrix, adjacency list, directed graph, undirected graph, edge weights."
          LAB_STEPS="1. Construct a graph using adjacency list representation\n2. Construct the same graph as adjacency matrix\n3. Analyze memory constraints"
          Q="Which representation is most memory-efficient for a sparse graph with N vertices and few edges?"
          OPTS="A) Adjacency Matrix\nB) Adjacency List\nC) Edge List\nD) Hash Matrix"
          ANS="B"
          EXPL="Adjacency lists only store actual links, bypassing the O(N^2) memory footprint of adjacency matrices."
          DIST="Adjacency matrix always uses O(V^2) memory space regardless of edge density."
          ;;
        10)
          TOPIC="Breadth-First & Depth-First Search"
          TERMS="BFS traversal, DFS traversal, queue frontier, stack frame, visited set."
          LAB_STEPS="1. Implement BFS algorithm on adjacency list using a queue\n2. Implement DFS using recursion/stack\n3. Trace path discovery"
          Q="Which traversal algorithm uses a queue to visit all nodes at the current depth level before moving to the next level?"
          OPTS="A) Depth-First Search (DFS)\nB) Breadth-First Search (BFS)\nC) Preorder traversal\nD) Postorder traversal"
          ANS="B"
          EXPL="BFS processes nodes level by level using a FIFO queue to store discovered frontier vertices."
          DIST="DFS travels deep along a branch first, typically implemented using a LIFO stack."
          ;;
        11)
          TOPIC="Dijkstra's Shortest Path"
          TERMS="Single-source shortest path, priority queue, edge relaxation, negative edge weights restriction."
          LAB_STEPS="1. Write Dijkstra algorithm on weighted adjacency list\n2. Find shortest path between two nodes\n3. Verify output correctness"
          Q="Why is Dijkstra's algorithm unable to guarantee correct shortest paths in graphs with negative edge weights?"
          OPTS="A) It uses a queue instead of stack\nB) Once a vertex is visited/relaxed, the algorithm assumes its shortest path is permanently solved\nC) It only works on binary trees\nD) It runs in O(N^3) time"
          ANS="B"
          EXPL="Dijkstra's greedy choice assumes that paths can only increase in cost; a negative edge can invalidate earlier evaluations."
          DIST="Bellman-Ford is used for graphs with negative weights because it repeatedly relaxes all edges."
          ;;
        12)
          TOPIC="Divide & Conquer"
          TERMS="Recursion divide, conquer combining, merge sort, quick sort, pivot selection."
          LAB_STEPS="1. Implement Merge Sort\n2. Implement Quick Sort with in-place swapping\n3. Compare sorting execution times"
          Q="What is the average and worst-case time complexity of the Quick Sort algorithm?"
          OPTS="A) Average: O(N log N), Worst: O(N^2)\nB) Average: O(N), Worst: O(N log N)\nC) Average: O(N log N), Worst: O(N log N)\nD) Average: O(N^2), Worst: O(N^2)"
          ANS="A"
          EXPL="Quick Sort runs in O(N log N) on average, but degrades to O(N^2) if the pivot splits the array highly unevenly (e.g. sorted arrays)."
          DIST="Merge Sort guarantees O(N log N) in both average and worst cases but requires O(N) extra memory space."
          ;;
        13)
          TOPIC="Greedy Algorithms"
          TERMS="Local optimum, global optimum, Minimum Spanning Tree (MST), Kruskal, Prim."
          LAB_STEPS="1. Implement Prim's MST algorithm\n2. Implement Kruskal's algorithm using disjoint sets\n3. Compute minimum tree weight"
          Q="Kruskal's algorithm finds the Minimum Spanning Tree by sorting which properties of the graph first?"
          OPTS="A) Vertex degrees\nB) Edge weights\nC) Path lengths\nD) Adjacency matrices"
          ANS="B"
          EXPL="Kruskal's algorithm is a greedy algorithm that processes edges in ascending order of their weights, checking for cycles."
          DIST="Prim's algorithm starts from a root node and expands the tree using local minimum edges."
          ;;
        14)
          TOPIC="Dynamic Programming Basics"
          TERMS="Overlapping subproblems, optimal substructure, memoization (top-down), tabulation (bottom-up)."
          LAB_STEPS="1. Solve Fibonacci using memoization dict\n2. Solve Knapsack 0/1 using tabulation grid\n3. Compare execution steps"
          Q="What is the difference between Memoization and Tabulation in Dynamic Programming?"
          OPTS="A) Memoization is bottom-up; Tabulation is top-down\nB) Memoization is top-down recursive; Tabulation is bottom-up iterative\nC) Memoization uses more memory\nD) Tabulation requires recursive helper calls"
          ANS="B"
          EXPL="Memoization caches recursive call outputs (top-down). Tabulation fills a table iteratively from basic inputs (bottom-up)."
          DIST="Tabulation is non-recursive, avoiding stack overflow errors."
          ;;
        15)
          TOPIC="String Algorithms & Trie"
          TERMS="Prefix search, suffix tree, string matching, Knuth-Morris-Pratt (KMP), Trie node."
          LAB_STEPS="1. Implement a Trie class with insert and search methods\n2. Implement startsWith prefix search\n3. Test autocomplete matches"
          Q="Which data structure is most suitable for implementing autocomplete systems or dictionary prefix matching?"
          OPTS="A) AVL Tree\nB) Hash Table\nC) Trie (Prefix Tree)\nD) Max Heap"
          ANS="C"
          EXPL="Tries store characters along branches, sharing common prefixes which allows rapid string prefix searches."
          DIST="Hash Table can find exact keys, but cannot efficiently match prefixes."
          ;;
      esac
      ;;
    "CIS-3340_Full_Stack_Web_Dev")
      case "$week" in
        1)
          TOPIC="HTML5 Semantics & SEO"
          TERMS="Semantic markup, SEO optimization, head tags, accessibility guidelines (WCAG), metadata."
          LAB_STEPS="1. Draft a structured HTML page using semantic tags\n2. Verify tags against accessibility validator\n3. Write descriptive alt text"
          Q="Which HTML5 tag is considered a semantic element?"
          OPTS="A) <div>\nB) <span>\nC) <article>\nD) <b>"
          ANS="C"
          EXPL="<article> has semantic meaning, telling the browser and search engines about the nature of the enclosed text content."
          DIST="div and span are generic container tags with no semantic value."
          ;;
        2)
          TOPIC="Modern CSS Layouts"
          TERMS="Flexbox, CSS Grid, display attributes, box model, sizing properties."
          LAB_STEPS="1. Configure a CSS Flexbox card container\n2. Configure a CSS Grid dashboard interface\n3. Debug layout overlapping elements"
          Q="Which CSS property converts an element into a grid container?"
          OPTS="A) display: grid\nB) layout: grid\nC) grid-template: true\nD) position: relative"
          ANS="A"
          EXPL="Setting display: grid instructs the rendering engine to compute nested children as grid items."
          DIST="display is the core CSS layout configuration property."
          ;;
        3)
          TOPIC="Responsive Design"
          TERMS="Media queries, viewport configurations, fluid grid units (em, rem, vw), breakpoint guidelines."
          LAB_STEPS="1. Configure a mobile-first responsive landing page stylesheet\n2. Add media queries to handle dynamic resizing\n3. Test viewport sizing"
          Q="What media query rule targets screen sizes that are 768px wide or smaller?"
          OPTS="A) @media (min-width: 768px)\nB) @media (max-width: 768px)\nC) @media screen 768\nD) @breakpoint 768px"
          ANS="B"
          EXPL="max-width: 768px matches screens up to and including 768px in width."
          DIST="min-width matches screens that are at least 768px wide."
          ;;
        4)
          TOPIC="JavaScript DOM Manipulation"
          TERMS="Document Object Model (DOM), query selectors, event listeners, bubbling and capturing, dynamic DOM trees."
          LAB_STEPS="1. Implement DOM selector query loops\n2. Add keydown/click event listeners to forms\n3. Dynamically append list elements using JavaScript"
          Q="Which DOM query method retrieves all page elements matching a class identifier?"
          OPTS="A) document.getElementById()\nB) document.querySelector()\nC) document.querySelectorAll()\nD) document.classList()"
          ANS="C"
          EXPL="querySelectorAll returns a NodeList of all page elements matching the provided CSS selector."
          DIST="querySelector only returns the first matching node."
          ;;
        5)
          TOPIC="Asynchronous JavaScript"
          TERMS="Call stack, event loop, callback queue, Promises, async/await constructs, error handling."
          LAB_STEPS="1. Write callback loops\n2. Write fetch calls returning Promises\n3. Refactor promises using async/await syntax and try-catch blocks"
          Q="What state does a JavaScript Promise enter once it has completed successfully?"
          OPTS="A) Pending\nB) Fulfilled\nC) Rejected\nD) Resolved"
          ANS="B"
          EXPL="Promises transition from Pending to either Fulfilled (resolved successfully) or Rejected (errored out)."
          DIST="Resolved is the general term for completion, but the explicit state is Fulfilled."
          ;;
        6)
          TOPIC="RESTful API Principles"
          TERMS="Representational State Transfer (REST), endpoints, resource identifiers, HTTP verbs, status codes."
          LAB_STEPS="1. Map HTTP endpoints using standard RESTful naming conventions\n2. Test endpoints using mock client payloads\n3. Inspect API headers"
          Q="Which HTTP status code class indicates a server-side processing error occurred?"
          OPTS="A) 2xx\nB) 3xx\nC) 4xx\nD) 5xx"
          ANS="D"
          EXPL="5xx status codes (e.g. 500 Internal Server Error) represent backend processing failures."
          DIST="4xx is for client-side input errors (e.g. 404 Not Found)."
          ;;
        7)
          TOPIC="Node.js & Express Server"
          TERMS="Node event loop, package manager (NPM), Express framework, server setup, listening sockets."
          LAB_STEPS="1. Initialize npm package settings\n2. Create base Express routing script file\n3. Listen to connections on port 3000"
          Q="Which code snippet initializes a basic Express application instance?"
          OPTS="A) const app = express()\nB) const app = new express.App()\nC) const app = require('express').start()\nD) const app = Express.init()"
          ANS="A"
          EXPL="Invoking the required express module function creates an application instance."
          DIST="The other options show incorrect module instantiation syntax."
          ;;
        8)
          TOPIC="Server-Side Routing & Middleware"
          TERMS="Middleware pipeline, request parsing, routing parameters, CORS handling, next() function."
          LAB_STEPS="1. Implement logging middleware printing timestamp data\n2. Create parametrized routes (e.g. /users/:id)\n3. Configure JSON request body parsing"
          Q="What function must be invoked at the end of a custom Express middleware handler to pass control to the next function in line?"
          OPTS="A) end()\nB) send()\nC) next()\nD) forward()"
          ANS="C"
          EXPL="Invoking the next() callback tells Express to progress to the subsequent handler in the pipeline."
          DIST="Failing to call next() will cause the request to hang."
          ;;
        9)
          TOPIC="Relational Databases with PostgreSQL"
          TERMS="SQL schema structure, relational tables, PRIMARY KEY, FOREIGN KEY constraints, JOIN queries."
          LAB_STEPS="1. Write raw SQL scripts to create tables\n2. Insert mock data records using INSERT queries\n3. Perform INNER JOIN queries to return relational records"
          Q="Which SQL constraint uniquely identifies each record in a database table?"
          OPTS="A) FOREIGN KEY\nB) UNIQUE INDEX\nC) PRIMARY KEY\nD) DEFAULT"
          ANS="C"
          EXPL="The PRIMARY KEY constraint enforces unique, non-null values for the primary database identifier column."
          DIST="FOREIGN KEY links rows to parent tables."
          ;;
        10)
          TOPIC="NoSQL Databases with MongoDB"
          TERMS="Document database, collections, BSON, schema design, mongoose model operations."
          LAB_STEPS="1. Establish a mongoose server connection profile\n2. Define user models with schema validation\n3. Write CRUD queries to write records"
          Q="Which data format does MongoDB use natively to store documents in collections?"
          OPTS="A) XML\nB) CSV\nC) BSON (Binary JSON)\nD) SQL Table Structure"
          ANS="C"
          EXPL="MongoDB processes data objects as BSON, an optimized binary representation of JSON files."
          DIST="BSON supports more data types (such as dates) than plain JSON."
          ;;
        11)
          TOPIC="Frontend Frameworks (React)"
          TERMS="Single Page Application (SPA), React virtual DOM, components, JSX syntax, build pipelines."
          LAB_STEPS="1. Setup base react project skeleton\n2. Convert HTML blocks to JSX component templates\n3. Inspect virtual DOM structures"
          Q="How does React's Virtual DOM improve application rendering performance?"
          OPTS="A) It updates all page elements on every interaction\nB) It compiles javascript to machine code\nC) It computes changes in memory first and only updates altered elements in the real DOM\nD) It bypasses CSS parsing"
          ANS="C"
          EXPL="React compares changes in a virtual DOM tree (reconciliation) and updates only the necessary elements, avoiding expensive global repaints."
          DIST="Bypassing calculations or writing machine code is not how React operates."
          ;;
        12)
          TOPIC="React State & Props"
          TERMS="Functional components, React hooks, useState, immutable props, event handling."
          LAB_STEPS="1. Configure useState hook controls to manage component arrays\n2. Pass props to nested child elements\n3. Handle button interactions to update view state"
          Q="Which React Hook is used to add local state variables to functional components?"
          OPTS="A) useEffect\nB) useContext\nC) useState\nD) useStateVariable"
          ANS="C"
          EXPL="The useState hook returns a state value and a setter function to trigger re-renders."
          DIST="useEffect handles side effects. useContext handles global context."
          ;;
        13)
          TOPIC="Web Security (JWT & CORS)"
          TERMS="Cross-Origin Resource Sharing (CORS), JSON Web Tokens (JWT), signing keys, payload structures, bcrypt."
          LAB_STEPS="1. Configure CORS origins in Express app\n2. Hash passwords using bcrypt before saving\n3. Generate and verify signing JWT payloads"
          Q="What are the three parts of a JSON Web Token (JWT)?"
          OPTS="A) Header, Payload, Signature\nB) ID, Key, Secret\nC) Username, Date, Salt\nD) Origin, Destination, Protocol"
          ANS="A"
          EXPL="A JWT is a dot-separated string containing a Header (metadata), a Payload (claims), and a cryptographically verified Signature."
          DIST="Only the base structure guarantees validation."
          ;;
        14)
          TOPIC="Deployment to AWS"
          TERMS="AWS S3, EC2 hosting, security groups, public ports, PM2 service manager."
          LAB_STEPS="1. Deploy static build files to AWS S3 bucket\n2. Launch a virtual Linux instance on AWS EC2\n3. Configure inbound security rules for HTTP/SSH ports"
          Q="Which AWS compute service provides resizable, raw virtual machines for hosting backend applications?"
          OPTS="A) Amazon S3\nB) Amazon EC2\nC) AWS Lambda\nD) Amazon RDS"
          ANS="B"
          EXPL="EC2 (Elastic Compute Cloud) provides virtual machines (instances) for running backend service code."
          DIST="S3 is object storage. Lambda is serverless function execution."
          ;;
        15)
          TOPIC="Web Sockets"
          TERMS="Socket.io, TCP duplex streams, polling fallbacks, real-time message streams."
          LAB_STEPS="1. Configure Socket.io servers\n2. Listen to websocket connection event triggers\n3. Broadcast events to connected clients"
          Q="What is the primary benefit of WebSockets over standard HTTP polling?"
          OPTS="A) WebSockets encrypt data automatically\nB) WebSockets provide full-duplex, persistent connection channels over a single TCP socket\nC) WebSockets do not require ports\nD) WebSockets run faster than compiled C++ code"
          ANS="B"
          EXPL="WebSockets allow continuous, bi-directional real-time communication without the overhead of repeating HTTP headers."
          DIST="Encryption requires WSS (Secure), and ports are still utilized."
          ;;
      esac
      ;;
    "CIS-3350_Software_Engineering_Agile")
      case "$week" in
        1)
          TOPIC="SDLC Models"
          TERMS="Software Development Life Cycle, Waterfall model, Agile model, iterative phases, risk evaluation."
          LAB_STEPS="1. Document SDLC model characteristics\n2. Compare development scenarios for Waterfall vs Agile\n3. Identify project risks"
          Q="Which SDLC model is characterized by linear, sequential phases where each phase must complete before the next begins?"
          OPTS="A) Scrum\nB) Waterfall\nC) Spiral\nD) Kanban"
          ANS="B"
          EXPL="Waterfall is the classic linear-sequential model with distinct, non-overlapping development phases."
          DIST="Scrum and Kanban are iterative Agile frameworks. Spiral is risk-driven."
          ;;
        2)
          TOPIC="Git Workflows & Branching"
          TERMS="Git branch, merge conflicts, pull requests, Gitflow workflow, rebase vs merge."
          LAB_STEPS="1. Initialize local Git repo\n2. Create feature branches and resolve simulated merge conflicts\n3. Submit a mock pull request"
          Q="In Gitflow workflow, which branch contains production-ready code that is deployed to live systems?"
          OPTS="A) develop\nB) feature\nC) main (master)\nD) hotfix"
          ANS="C"
          EXPL="The main/master branch holds the stable, tested, production-released codebase."
          DIST="develop branch aggregates feature branches under active development."
          ;;
        3)
          TOPIC="Clean Code & Refactoring"
          TERMS="Code smells, refactoring techniques, DRY (Don't Repeat Yourself), descriptive naming, comment overhead."
          LAB_STEPS="1. Review a legacy script containing poor naming and duplicate loops\n2. Refactor variables and functions to follow clean guidelines\n3. Test code execution"
          Q="What software design principle is violated when you copy and paste identical blocks of code across multiple parts of a program?"
          OPTS="A) SOLID\nB) DRY (Don't Repeat Yourself)\nC) KISS (Keep It Simple, Stupid)\nD) YAGNI (You Aren't Gonna Need It)"
          ANS="B"
          EXPL="DRY demands that every piece of knowledge must have a single, unambiguous representation within a system."
          DIST="YAGNI cautions against building unused features ahead of time."
          ;;
        4)
          TOPIC="Object-Oriented Design (SOLID)"
          TERMS="SOLID principles, Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion."
          LAB_STEPS="1. Analyze class layouts violating SOLID rules\n2. Re-architect classes to conform to Open/Closed and Single Responsibility principles\n3. Verify class inheritance relations"
          Q="Which SOLID principle states that software entities (classes, modules) should be open for extension but closed for modification?"
          OPTS="A) Single Responsibility Principle\nB) Open/Closed Principle\nC) Liskov Substitution Principle\nD) Interface Segregation Principle"
          ANS="B"
          EXPL="The Open/Closed Principle allows extending class behavior (usually via inheritance or polymorphism) without changing the existing class source code."
          DIST="Single Responsibility states a class should have only one reason to change."
          ;;
        5)
          TOPIC="UML Diagrams"
          TERMS="Unified Modeling Language, Class diagram, Use Case diagram, Sequence diagram, multiplicity relations."
          LAB_STEPS="1. Draft a Use Case diagram mapping actor workflows\n2. Create a Class diagram showing database model attributes and relations\n3. Draw sequence diagrams"
          Q="Which UML diagram is best suited to visualize the logical lifecycle of objects and the exact order of messages passed between them over time?"
          OPTS="A) Class Diagram\nB) Use Case Diagram\nC) Sequence Diagram\nD) Deployment Diagram"
          ANS="C"
          EXPL="Sequence diagrams are behavioral diagrams showing step-by-step object interactions and message sequences ordered chronologically."
          DIST="Class diagrams are structural and show static linkages, not timeline-based calls."
          ;;
        6)
          TOPIC="Design Patterns (Creational)"
          TERMS="Design pattern classifications, Singleton pattern, Factory Method pattern, object instantiation."
          LAB_STEPS="1. Write a thread-safe Singleton class in Python\n2. Write a Factory pattern dynamically creating database connectors\n3. Test object instance memory locations"
          Q="What is the primary purpose of the Singleton design pattern?"
          OPTS="A) To abstract subclass creation\nB) To ensure a class has only one instance and provides a global point of access to it\nC) To convert interface structures\nD) To monitor runtime events"
          ANS="B"
          EXPL="Singleton restricts class instantiation to a single object, routing all calls through a shared instance reference."
          DIST="Factory Method handles subclass creation without specifying exact types."
          ;;
        7)
          TOPIC="Design Patterns (Structural & Behavioral)"
          TERMS="Observer pattern, Strategy pattern, decoupled components, state machines."
          LAB_STEPS="1. Implement Observer pattern to notify clients on data updates\n2. Implement Strategy pattern swapping payment calculators\n3. Verify decoupled state dependencies"
          Q="Which behavioral design pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified?"
          OPTS="A) Adapter Pattern\nB) Decorator Pattern\nC) Observer Pattern\nD) Strategy Pattern"
          ANS="C"
          EXPL="The Observer pattern enables decoupling pub-sub mechanisms where subjects notify observers without tight linkages."
          DIST="Adapter links mismatched interfaces. Decorator adds behavior dynamically."
          ;;
        8)
          TOPIC="Software Testing Levels"
          TERMS="Unit tests, integration tests, system tests, mock inputs, assertion statements."
          LAB_STEPS="1. Write pytest unit test cases asserting function returns\n2. Mock database connection responses\n3. Measure test coverage indicators"
          Q="Which level of testing focuses on validating that individual functions, methods, or classes behave correctly in isolation?"
          OPTS="A) Unit Testing\nB) Integration Testing\nC) System Testing\nD) Acceptance Testing"
          ANS="A"
          EXPL="Unit testing tests smallest testable parts (units) of an application independently from database or network APIs."
          DIST="Integration testing verifies interface communication between modules."
          ;;
        9)
          TOPIC="Test-Driven Development (TDD)"
          TERMS="TDD lifecycle (Red, Green, Refactor), test suites, assertions, code coverage."
          LAB_STEPS="1. Write failing test case based on spec sheet\n2. Write absolute minimum functional code to make test pass\n3. Refactor code structure keeping test green"
          Q="What is the correct sequence of phases in the Test-Driven Development (TDD) cycle?"
          OPTS="A) Refactor, Write Code, Verify Test\nB) Write Test (Red), Implement Code (Green), Refactor\nC) Design, Code, Test, Release\nD) Assert, Clean, Deploy"
          ANS="B"
          EXPL="TDD operates in a tight loop: write a failing test (Red), implement code just enough to pass (Green), then clean up/refactor structure."
          DIST="Writing code before test cases violates the core philosophy of TDD."
          ;;
        10)
          TOPIC="CI/CD Foundations"
          TERMS="Continuous Integration, Continuous Deployment, automation runners, pipeline syntax, deployment registries."
          LAB_STEPS="1. Create local script running lint checks\n2. Map build stages in a mock configuration file\n3. Review pipeline output reports"
          Q="What is the primary goal of Continuous Integration (CI)?"
          OPTS="A) To manually deploy builds to production servers\nB) To automatically build, lint, and run tests on code changes whenever developer merges to shared branches\nC) To write project charters\nD) To backup database files"
          ANS="B"
          EXPL="CI automatically verifies new changes pushed to repositories using automation pipelines, detecting compilation and test failures early."
          DIST="Continuous Delivery/Deployment (CD) handles the automation of software releases to targets."
          ;;
        11)
          TOPIC="Scrum Framework Roles"
          TERMS="Scrum Guide, Scrum Team, Product Owner, Scrum Master, Developers, self-managing teams."
          LAB_STEPS="1. Assign project tasks matching Scrum roles\n2. Map Scrum team interaction guidelines\n3. Document scope ownership profiles"
          Q="Who on the Scrum Team is accountable for maximizing the value of the product and managing the Product Backlog?"
          OPTS="A) Scrum Master\nB) Developers\nC) Product Owner\nD) Project Manager"
          ANS="C"
          EXPL="The Product Owner represents client stakeholders and maintains the prioritization of product backlog items."
          DIST="Scrum Master manages process adherence. Developers implement features."
          ;;
        12)
          TOPIC="Scrum Events"
          TERMS="Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, timeboxing rules."
          LAB_STEPS="1. Simulate Scrum event time allocations\n2. Draft a Sprint Retrospective improvements matrix\n3. Outline daily standup updates"
          Q="What is the maximum timebox duration for the Daily Scrum event?"
          OPTS="A) 5 minutes\nB) 15 minutes\nC) 30 minutes\nD) 1 hour"
          ANS="B"
          EXPL="The Daily Scrum is strictly timeboxed to 15 minutes to keep alignment meetings focused and brief."
          DIST="Other durations are too long for daily alignment."
          ;;
        13)
          TOPIC="Backlog Refinement & Estimation"
          TERMS="Product backlog items, user stories, Planning Poker, story points, Fibonacci sequence."
          LAB_STEPS="1. Draft user stories in standard format\n2. Use Planning Poker to assign story points to tasks\n3. Determine team velocity limits"
          Q="Why does Scrum use relative estimation metrics like Story Points instead of hours to estimate task sizes?"
          OPTS="A) Hours are too complex to sum\nB) Story points account for complexity, effort, and risk in a way that is consistent across different developer skill levels\nC) Clients demand story points\nD) Story points allow skipping QA"
          ANS="B"
          EXPL="Relative sizing (using Fibonacci scales) enables developers to estimate scope size and complexity without micro-managing hourly commitments."
          DIST="Hours do not reflect variable experience or unexpected integration risks."
          ;;
        14)
          TOPIC="Software Security & Coding Standards"
          TERMS="Secure coding guidelines, OWASP standards, input validation, output encoding, cryptography principles."
          LAB_STEPS="1. Review code templates for security issues\n2. Apply sanitization rules to clean inputs\n3. Test application behaviors"
          Q="Which security practice is most critical to prevent buffer overflows or injection vulnerability issues?"
          OPTS="A) Writing verbose comments\nB) Input validation and sanitization\nC) Reducing compiler speed\nD) Disabling firewalls"
          ANS="B"
          EXPL="Validating input parameters against type and length boundaries stops malicious payloads from executing."
          DIST="Comments or compiler configurations do not alter security execution characteristics."
          ;;
        15)
          TOPIC="DevOps Principles"
          TERMS="DevOps lifecycle, infrastructure automation, container orchestration, telemetry metrics."
          LAB_STEPS="1. Analyze infrastructure requirements for web apps\n2. Map DevOps lifecycle loops\n3. Identify delivery constraints"
          Q="Which core principle emphasizes breaking down silos between software creators and operational system administrators?"
          OPTS="A) Waterfall\nB) Systems Analysis\nC) DevOps\nD) Strict Isolation"
          ANS="C"
          EXPL="DevOps integrates development workflows with systems operations, aligning development speed with server stability."
          DIST="Waterfall and isolation reinforce team silos rather than resolving them."
          ;;
      esac
      ;;
  esac
}

# Helper to get week data for courses 4-6
get_week_data_2() {
  local course=$1
  local week=$2
  
  case "$course" in
    "CIS-4345_Machine_Learning_Deep_Learning")
      case "$week" in
        1)
          TOPIC="Introduction to ML Pipelines"
          TERMS="Machine learning lifecycle, data collection, feature extraction, train-test split, label definitions."
          LAB_STEPS="1. Setup ML project directory\n2. Verify scikit-learn installations\n3. Split a sample database matrix into training and testing partitions"
          Q="What is the primary reason for splitting data into Training and Testing datasets?"
          OPTS="A) To save disk storage space\nB) To evaluate how the model performs on unseen data and detect overfitting\nC) To double compile datasets\nD) To format files for database engines"
          ANS="B"
          EXPL="Testing datasets provide unbiased metrics indicating how well models generalize to new inputs."
          DIST="It does not optimize space or compile script files."
          ;;
        2)
          TOPIC="Linear Regression"
          TERMS="Continuous output variables, cost function (MSE), gradient descent steps, weights and biases."
          LAB_STEPS="1. Train linear regression model\n2. Fit features: model.fit(X, y)\n3. Print intercept and slope values"
          Q="What is the objective of the Gradient Descent algorithm in model training?"
          OPTS="A) To select random features\nB) To iteratively adjust model weights to minimize the cost function value\nC) To prune decision tree leaves\nD) To backup SQL tables"
          ANS="B"
          EXPL="Gradient Descent is an optimization method that computes cost gradients to update weights toward minimum cost levels."
          DIST="Pruning trees and database administration are independent tasks."
          ;;
        3)
          TOPIC="Logistic Regression"
          TERMS="Binary classification, sigmoid activation, probability mapping, threshold values."
          LAB_STEPS="1. Train logistic regression model\n2. Predict binary class output labels\n3. Analyze probability arrays using predict_proba()"
          Q="Which mathematical function maps real number inputs to a probability value between 0 and 1 in logistic regression?"
          OPTS="A) Linear function\nB) Sigmoid (Logistic) function\nC) Step function\nD) Relu function"
          ANS="B"
          EXPL="The sigmoid function (1 / (1 + e^-x)) outputs values bounded between 0 and 1, representing probabilities."
          DIST="Linear function can return infinite outputs. ReLU is max(0, x)."
          ;;
        4)
          TOPIC="Regularization Techniques"
          TERMS="Overfitting indicators, high variance, L1 regularization (Lasso), L2 regularization (Ridge), alpha penalty."
          LAB_STEPS="1. Import Ridge and Lasso classes\n2. Train models with varying alpha levels\n3. Observe feature weights dropping toward zero"
          Q="How does L1 regularization (Lasso) differ from L2 regularization (Ridge)?"
          OPTS="A) L1 adds squared penalties, L2 adds absolute penalties\nB) L1 can force feature weights exactly to zero, performing feature selection\nC) L2 is only used in unsupervised learning\nD) L1 increases model training time by 10x"
          ANS="B"
          EXPL="Lasso adds an absolute weight penalty to the cost, leading to sparse coefficients (forces unimportant features to 0)."
          DIST="Ridge uses squared penalties (L2) and shrinks weights close to but not exactly to 0."
          ;;
        5)
          TOPIC="Support Vector Machines"
          TERMS="Hyperplane separation, support vectors, margin maximization, kernel trick, soft margins."
          LAB_STEPS="1. Train Support Vector Classifier\n2. Map linear vs radial basis function (RBF) kernels\n3. Plot decision boundaries"
          Q="What are support vectors in the context of Support Vector Machines?"
          OPTS="A) Empty dimensions\nB) The data points closest to the separating hyperplane that define the margin boundaries\nC) The outputs of activation layers\nD) Target variable index arrays"
          ANS="B"
          EXPL="Support vectors are the critical data points that lie directly on the margins; removing them changes the placement of the decision boundary."
          DIST="Support vectors are real points, not dimensions or activations."
          ;;
        6)
          TOPIC="Decision Trees & Random Forests"
          TERMS="Entropy index, Gini impurity, node splitting, ensemble methods, bagging, bootstrap samples."
          LAB_STEPS="1. Train a decision tree on classifier data\n2. Train a Random Forest classifier\n3. Compare test accuracy metrics"
          Q="Which process describes the 'Bagging' ensemble technique used in Random Forests?"
          OPTS="A) Sequential tree boosting\nB) Training multiple independent decision trees on bootstrap datasets and averaging their votes\nC) Regularizing feature weight matrices\nD) Compressing tree layers into a single node"
          ANS="B"
          EXPL="Bootstrap Aggregation (Bagging) reduces variance by training multiple trees on random sub-samples and combining predictions."
          DIST="Sequential tree training is characteristic of Boosting (e.g. XGBoost)."
          ;;
        7)
          TOPIC="K-Means & Hierarchical Clustering"
          TERMS="Unsupervised learning, centroids, inertia, elbow method, dendrogram structures."
          LAB_STEPS="1. Train K-Means clustering algorithm\n2. Plot elbow curve using inertia metrics\n3. Classify unlabeled customer profiles"
          Q="How do you determine the optimal number of clusters (K) in K-Means clustering using the Elbow Method?"
          OPTS="A) Look for the point where the cost curve changes from steep to shallow (inertia drops level off)\nB) Find the highest classification score\nC) Check the number of columns\nD) Count the total row count"
          ANS="A"
          EXPL="The 'elbow' represents a point of diminishing returns where adding more clusters yields minimal reduction in inertia."
          DIST="Classification scores are unavailable since K-Means is unsupervised."
          ;;
        8)
          TOPIC="Dimensionality Reduction (PCA)"
          TERMS="Curse of dimensionality, principal components, covariance matrix, explained variance ratio."
          LAB_STEPS="1. Import PCA class\n2. Reduce high-dimension dataset to 2 components\n3. Verify explained variance outcomes"
          Q="What is the main purpose of Principal Component Analysis (PCA)?"
          OPTS="A) To predict label outputs\nB) To project high-dimensional data onto lower-dimensional spaces while preserving maximum variance\nC) To cluster similar users\nD) To balance binary classes"
          ANS="B"
          EXPL="PCA simplifies data structures by identifying orthogonal principal components that capture the most information."
          DIST="PCA is a linear transformer, not a predictor or clustering engine."
          ;;
        9)
          TOPIC="Introduction to Neural Networks"
          TERMS="Deep learning models, artificial neuron structure, inputs, weights, bias, hidden layers, output activations."
          LAB_STEPS="1. Build a simple neuron representation using numpy dot products\n2. Trace forward propagation variables\n3. Inspect weight matrices"
          Q="What is the primary function of a hidden layer in an artificial neural network?"
          OPTS="A) To store inputs exactly\nB) To learn non-linear feature representations from input data patterns\nC) To write files to disk\nD) To communicate directly with user interfaces"
          ANS="B"
          EXPL="Hidden layers apply weights and activation functions to extract high-level feature mappings from preceding inputs."
          DIST="Hidden layers are intermediate computation steps, isolated from raw files and client frontends."
          ;;
        10)
          TOPIC="Activation & Backpropagation"
          TERMS="Activation functions (ReLU, Sigmoid, Softmax), forward pass, loss calculations, backpropagation, chain rule."
          LAB_STEPS="1. Calculate derivative outputs of Sigmoid and ReLU functions\n2. Implement simple backprop weight adjust updates\n3. Test learning convergence"
          Q="Which mathematical derivative rule is utilized to compute gradients of nested layers during the backpropagation step?"
          OPTS="A) Product Rule\nB) Quotient Rule\nC) Chain Rule\nD) Addition Rule"
          ANS="C"
          EXPL="Backpropagation computes error gradients starting at the output layer and propagating backward using the Chain Rule of calculus."
          DIST="The chain rule handles derivatives of composed functions."
          ;;
        11)
          TOPIC="Convolutional Neural Networks"
          TERMS="Image array structures, convolution filters, stride settings, pooling layers (max pooling), flatten step."
          LAB_STEPS="1. Define a CNN layout using TensorFlow Keras Sequential API\n2. Add Conv2D and MaxPooling2D layers\n3. Print model summary layouts"
          Q="Why are Convolutional layers superior to Fully Connected layers for image processing tasks?"
          OPTS="A) They require larger database spaces\nB) They preserve spatial relationships and reduce parameters through weight sharing\nC) They do not require activation functions\nD) They compile directly to C++ binaries"
          ANS="B"
          EXPL="CNN filters scan local pixel neighborhoods, capturing spatial patterns (edges, shapes) regardless of position in the image."
          DIST="Fully connected layers flatten images, destroying spatial layout and causing parameters to explode."
          ;;
        12)
          TOPIC="Recurrent Neural Networks (RNN/LSTM)"
          TERMS="Sequence databases, recurrent loops, hidden states, vanishing gradients, Long Short-Term Memory (LSTM) cells."
          LAB_STEPS="1. Define a simple LSTM model layout in Keras\n2. Format text or time-series data array dimensions\n3. Train model and print outcomes"
          Q="What problem do Long Short-Term Memory (LSTM) cells solve compared to basic Recurrent Neural Networks (RNNs)?"
          OPTS="A) Memory leak errors\nB) The vanishing gradient problem, allowing the model to learn long-term dependencies\nC) The lack of GPU drivers\nD) High compilation speeds"
          ANS="B"
          EXPL="LSTMs use internal gating mechanisms (forget gate, input gate, output gate) to maintain state values across many sequence steps."
          DIST="LSTMs do not change computer hardware drivers or execution speeds."
          ;;
        13)
          TOPIC="Natural Language Processing"
          TERMS="Text processing pipelines, token vectors, vocabulary lookup, word embeddings (Word2Vec), cosine similarity."
          LAB_STEPS="1. Tokenize text paragraphs into indices\n2. Build word vector representations\n3. Compute cosine similarity values between vectors"
          Q="What is a word embedding in Natural Language Processing (NLP)?"
          OPTS="A) A dictionary lookup string\nB) A dense vector representation where words with similar semantic meanings are mapped close together\nC) A file compression method\nD) A type of database primary key"
          ANS="B"
          EXPL="Word embeddings project words into high-dimensional geometric spaces, encoding semantic relationships."
          DIST="It is not a static dictionary lookup or a database key."
          ;;
        14)
          TOPIC="Model Optimization & Tuning"
          TERMS="Learning rate adjustments, optimizer configurations (Adam, SGD), dropout layers, batch size settings."
          LAB_STEPS="1. Train a neural network with varying learning rates\n2. Add Dropout layers to reduce overfitting\n3. Plot loss convergence charts"
          Q="How does the Dropout technique prevent overfitting in deep neural networks?"
          OPTS="A) It drops input rows\nB) It randomly deactivates a fraction of neurons during each training step, forcing redundancy\nC) It deletes model files\nD) It turns off the CPU"
          ANS="B"
          EXPL="Dropout stops co-adaptation by ensuring no single neuron can dominate feature representation."
          DIST="It is applied during training steps, not row deletion."
          ;;
        15)
          TOPIC="Model Deployment & Serving"
          TERMS="Model serialization (Keras H5, TensorFlow SavedModel), REST API frameworks, hosting options."
          LAB_STEPS="1. Save a trained TensorFlow model file\n2. Build a Flask/FastAPI backend to load model and serve predictions\n3. Test endpoint with curl payloads"
          Q="What format is typically used to exchange model prediction input payloads over HTTP APIs?"
          OPTS="A) XML\nB) JSON\nC) CSV\nD) SQL Data"
          ANS="B"
          EXPL="REST APIs typically use JSON format to structure features and return class labels or scores."
          DIST="JSON is the standard format for modern HTTP REST requests."
          ;;
      esac
      ;;
    "CIS-3310_IT_Project_Management")
      case "$week" in
        1)
          TOPIC="IT Project Framework"
          TERMS="Project vs operations, triple constraint (Scope, Time, Cost), project lifecycle phases."
          LAB_STEPS="1. Draft a project charter template\n2. Identify project constraints for an IT upgrade\n3. Define lifecycle steps"
          Q="What are the three pillars of the Project Management Triple Constraint?"
          OPTS="A) Scope, Time, Cost\nB) Quality, Speed, Safety\nC) Staff, Hardware, Software\nD) Planning, Execution, Closure"
          ANS="A"
          EXPL="Any change to scope, schedule (time), or budget (cost) impacts the other variables and overall quality."
          DIST="Staff and planning are resources and phases, not core constraints."
          ;;
        2)
          TOPIC="Project Charter Development"
          TERMS="Project charter purpose, business case, project objectives, stakeholder registers."
          LAB_STEPS="1. Write a project charter for a server migration project\n2. Identify project sponsors and key stakeholders\n3. Document business benefits"
          Q="Which document authorizes the formal existence of a project and gives the project manager authority to apply resources?"
          OPTS="A) Project Scope Statement\nB) Project Charter\nC) Work Breakdown Structure\nD) Statement of Work (SOW)"
          ANS="B"
          EXPL="The Project Charter is signed by sponsors to initiate the project and authorize resources."
          DIST="Scope statement defines deliverables. WBS is a decomposition tree."
          ;;
        3)
          TOPIC="Defining Scope & WBS"
          TERMS="Work Breakdown Structure (WBS), decomposition, work packages, scope creep, WBS dictionary."
          LAB_STEPS="1. Decompose a software project into WBS levels\n2. Create a WBS hierarchy diagram\n3. Write definitions for work packages"
          Q="What is the lowest level of decomposition in a Work Breakdown Structure (WBS) called?"
          OPTS="A) Sub-project\nB) Task group\nC) Work Package\nD) Milestone"
          ANS="C"
          EXPL="Work packages are the granular units at the bottom of the WBS tree, where costs and schedules can be estimated."
          DIST="Milestones are points in time with zero duration."
          ;;
        4)
          TOPIC="Project Schedule & Gantt Charts"
          TERMS="Activity sequencing, dependency types (Finish-to-Start), Gantt chart configurations, lead and lag times."
          LAB_STEPS="1. Create an activity list with estimated durations\n2. Draw a Gantt chart mapping task timelines\n3. Add FS dependencies"
          Q="Which dependency type describes a scenario where Task B cannot start until Task A has completed?"
          OPTS="A) Start-to-Start (SS)\nB) Finish-to-Start (FS)\nC) Finish-to-Finish (FF)\nD) Start-to-Finish (SF)"
          ANS="B"
          EXPL="Finish-to-Start is the most common scheduling linkage; preceding activity must end before successor begins."
          DIST="Start-to-Start requires both tasks to begin concurrently."
          ;;
        5)
          TOPIC="Critical Path Method"
          TERMS="Network diagram, forward pass (early start/finish), backward pass (late start/finish), float/slack time."
          LAB_STEPS="1. Calculate ES/EF and LS/LF for a network diagram\n2. Identify critical path with zero float time\n3. Compute project duration"
          Q="What is the definition of the Critical Path in project scheduling?"
          OPTS="A) The path containing the most complex tasks\nB) The longest path of dependent activities that determines the shortest possible project duration\nC) The path with the highest cost\nD) The sequence of non-dependent milestones"
          ANS="B"
          EXPL="The critical path has zero slack (float) time. Any delay to critical path tasks directly delays the project completion date."
          DIST="It is determined by sequence duration, not complexity or cost."
          ;;
        6)
          TOPIC="Cost Estimation & Budgeting"
          TERMS="Analogous vs parametric estimating, bottom-up estimation, contingency reserves, cost baseline."
          LAB_STEPS="1. Calculate project costs using parametric estimating models\n2. Create a bottom-up budget database\n3. Determine reserve levels"
          Q="Which cost estimation technique uses historical data from similar projects as the basis for the current estimate?"
          OPTS="A) Parametric Estimating\nB) Analogous (Top-down) Estimating\nC) Bottom-up Estimating\nD) Three-point Estimating"
          ANS="B"
          EXPL="Analogous estimating compares the current scope to past projects, providing quick but less precise estimates."
          DIST="Parametric estimating uses statistical modeling (e.g. cost per square foot)."
          ;;
        7)
          TOPIC="Quality Management & Metrics"
          TERMS="Quality planning, quality assurance vs quality control, metrics, Pareto charts, check sheets."
          LAB_STEPS="1. Draft a quality management plan for software testing\n2. Analyze defect logs using a Pareto diagram\n3. Verify quality check metrics"
          Q="What is the main focus of Quality Assurance (QA) compared to Quality Control (QC)?"
          OPTS="A) QA focuses on preventing defects in processes, while QC focuses on identifying defects in final products\nB) QA runs unit tests\nC) QC manages project budgets\nD) QA is done only by project managers"
          ANS="A"
          EXPL="QA is process-oriented (proactive prevention). QC is product-oriented (reactive inspection of deliverables)."
          DIST="Both teams write tests, but their scope targets process vs product."
          ;;
        8)
          TOPIC="Resource Allocation"
          TERMS="Resource loading, resource leveling, RACI matrix (Responsible, Accountable, Consulted, Informed), resource conflicts."
          LAB_STEPS="1. Create a RACI matrix for project team members\n2. Resolve resource overallocation conflicts\n3. Verify assignment grids"
          Q="What does the 'A' stand for in a RACI assignment matrix?"
          OPTS="A) Assigned\nB) Accountable\nC) Authorized\nD) Approved"
          ANS="B"
          EXPL="Accountable represents the single person answerable for the correct completion of the task (only one 'A' per task)."
          DIST="Responsible executes the work. Accountable owns the outcome."
          ;;
        9)
          TOPIC="Communication & Stakeholder Management"
          TERMS="Communication channels formula (N*(N-1)/2), communication plan parameters, stakeholder registers."
          LAB_STEPS="1. Calculate communication channels for team scaling\n2. Draft a communication matrix specifying email/meeting schedules\n3. Identify stakeholder impacts"
          Q="How many communication channels exist in a project team containing 8 members?"
          OPTS="A) 8\nB) 16\nC) 28\nD) 56"
          ANS="C"
          EXPL="Using the channel formula: 8 * (8 - 1) / 2 = 8 * 7 / 2 = 56 / 2 = 28 channels."
          DIST="The formula tracks unique connections between all members."
          ;;
        10)
          TOPIC="Risk Identification & Management"
          TERMS="Risk register, qualitative risk analysis (probability vs impact), risk response strategies (avoid, transfer, mitigate, accept)."
          LAB_STEPS="1. Build a risk register table detailing threats\n2. Calculate risk score rankings (probability * impact)\n3. Draft risk mitigation workflows"
          Q="Which risk response strategy involves buying an insurance policy or outsourcing a database migration task to a vendor?"
          OPTS="A) Avoid\nB) Transfer\nC) Mitigate\nD) Accept"
          ANS="B"
          EXPL="Transferring shifts the financial ownership or operational threat to a third party (e.g. hosting provider or insurer)."
          DIST="Mitigation reduces probability or impact directly."
          ;;
        11)
          TOPIC="IT Procurement & Contracts"
          TERMS="Request for Proposal (RFP), contract types (Fixed Price, Time & Materials, Cost Reimbursable), SLA terms."
          LAB_STEPS="1. Review a vendor service level agreement (SLA)\n2. Compare contract scenarios for procurement pricing\n3. Draft contract parameters"
          Q="Which contract type carries the highest risk for the buyer but low risk for the seller?"
          OPTS="A) Firm-Fixed-Price (FFP)\nB) Cost-Reimbursable (CR)\nC) Time and Materials (T&M)\nD) Fixed-Price-Incentive-Fee (FPIF)"
          ANS="B"
          EXPL="In cost-reimbursable contracts, the buyer pays all actual costs plus a fee, meaning cost overruns are paid by the buyer."
          DIST="Fixed-price shifts cost overrun risk onto the seller."
          ;;
        12)
          TOPIC="Agile Project Management Overview"
          TERMS="Agile methodologies, sprint cycles, Kanban boards, velocity metrics, adaptive planning."
          LAB_STEPS="1. Map Agile sprint cycles for a mobile app project\n2. Track task progress on a physical/digital Kanban board\n3. Verify project backlog items"
          Q="How does scope changes management differ in Agile compared to traditional Waterfall project management?"
          OPTS="A) Agile permits changes at any time by prioritizing the backlog, while Waterfall uses strict change control boards\nB) Agile does not allow any changes\nC) Waterfall updates code dynamically\nD) Agile requires more documentation"
          ANS="A"
          EXPL="Agile welcomes change by re-evaluating the prioritizations of user stories before every sprint."
          DIST="Waterfall freezes scope early, requiring formal change management approval for revisions."
          ;;
        13)
          TOPIC="Project Execution & Performance Reporting"
          TERMS="Earned Value Management (EVM), Planned Value (PV), Actual Cost (AC), Earned Value (EV), CV, SV, CPI, SPI."
          LAB_STEPS="1. Calculate cost variance (CV) and schedule variance (SV)\n2. Determine project budget health using CPI and SPI indexes\n3. Analyze performance charts"
          Q="A project has a Cost Performance Index (CPI) of 0.85 and a Schedule Performance Index (SPI) of 1.10. What is the status?"
          OPTS="A) Under budget and ahead of schedule\nB) Over budget and behind schedule\nC) Over budget and ahead of schedule\nD) Under budget and behind schedule"
          ANS="C"
          EXPL="CPI < 1 indicates the project is spending more than planned (over budget). SPI > 1 indicates tasks are ending ahead of schedule."
          DIST="Value 1.0 is right on targets; values below 1 are negative/late."
          ;;
        14)
          TOPIC="Project Change Control"
          TERMS="Change request forms, Change Control Board (CCB), configuration management, impact assessment."
          LAB_STEPS="1. Draft a change request form template\n2. Analyze scope impacts of a requested software revision\n3. Document CCB approval pathways"
          Q="What is the primary role of a Change Control Board (CCB) in project management?"
          OPTS="A) To write programming code\nB) To review, evaluate, and approve or reject requested project scope modifications\nC) To buy software licenses\nD) To hire developers"
          ANS="B"
          EXPL="The CCB is a formal group of stakeholders that verifies changes before they are integrated into baselines."
          DIST="CCB handles scope governance, not raw development."
          ;;
        15)
          TOPIC="Project Closure & Post-Mortem"
          TERMS="Administrative closure, project handoff, contract closeout, lessons learned, post-mortem reports."
          LAB_STEPS="1. Draft a lessons learned survey questionnaire\n2. Complete a final project acceptance sign-off document\n3. Write post-mortem report outlines"
          Q="What is the primary purpose of conducting a Lessons Learned session during project closure?"
          OPTS="A) To assign blame for failures\nB) To identify successes and failures to improve future organizational projects\nC) To calculate final employee bonuses\nD) To archive server hardware logs"
          ANS="B"
          EXPL="Lessons learned capture historical insights to ensure subsequent projects avoid similar pitfalls."
          DIST="Lessons learned focus on process optimization, not assigning blame."
          ;;
      esac
      ;;
    "CIS-3312_Systems_Analysis_Design")
      case "$week" in
        1)
          TOPIC="Role of System Analyst & SDLC"
          TERMS="System analyst responsibilities, business analysis definition, SDLC stages, systems planning."
          LAB_STEPS="1. Map business analyst workflows\n2. Evaluate a business case scenario\n3. Define system boundaries"
          Q="What is the primary responsibility of a Systems Analyst?"
          OPTS="A) Writing compiled server assembly code\nB) Analyzing business requirements and designing information systems solutions to bridge business and IT\nC) Selling software licenses\nD) Configuring firewall ports"
          ANS="B"
          EXPL="Analysts serve as the interface, translating business needs into detailed technical specifications for programmers."
          DIST="They focus on analysis and design, not raw code creation or network security configurations."
          ;;
        2)
          TOPIC="Feasibility Analysis"
          TERMS="Technical feasibility, economic feasibility (ROI, NPV, Payback period), operational feasibility."
          LAB_STEPS="1. Compute Return on Investment (ROI) and Payback Period\n2. Calculate Net Present Value (NPV) for IT proposal\n3. Draft feasibility matrix reports"
          Q="Which feasibility aspect determines if the organization has the programming and infrastructure capability to build the proposed system?"
          OPTS="A) Economic Feasibility\nB) Operational Feasibility\nC) Technical Feasibility\nD) Schedule Feasibility"
          ANS="C"
          EXPL="Technical feasibility evaluates hardware, software, and development team capability limitations."
          DIST="Economic feasibility focuses on project costs and financial payback metrics."
          ;;
        3)
          TOPIC="Requirement Gathering"
          TERMS="Functional vs non-functional requirements, interview strategies, questionnaires, JAD sessions, prototyping."
          LAB_STEPS="1. Draft a requirements definition template\n2. Differentiate system requirement lists into functional/non-functional\n3. Design a questionnaire survey form"
          Q="Which item represents a non-functional system requirement?"
          OPTS="A) The system must send an email receipt on checkout\nB) The user must login using their email address\nC) The database query must return results within 2 seconds\nD) The system must export reports in PDF"
          ANS="C"
          EXPL="Non-functional requirements specify operational qualities (performance, security, usability) rather than specific feature tasks."
          DIST="Sending emails and logging in represent specific functional operations."
          ;;
        4)
          TOPIC="Use Case Analysis"
          TERMS="Actors, use case scenarios, preconditions, postconditions, extend vs include relationships."
          LAB_STEPS="1. Write a detailed use case description for 'Checkout Basket'\n2. Trace normal and exception flows of events\n3. Identify actor scopes"
          Q="In a Use Case diagram, which relationship is used when a use case requires the mandatory execution of another use case?"
          OPTS="A) <<extend>>\nB) <<include>>\nC) <<generalize>>\nD) <<dependency>>"
          ANS="B"
          EXPL="The <<include>> relationship indicates that the base use case incorporates the behavior of the target use case as a mandatory step."
          DIST="<<extend>> marks optional behaviors triggered only under specific conditions."
          ;;
        5)
          TOPIC="Process Modeling (DFD)"
          TERMS="Data Flow Diagrams (DFD), Gane & Sarson notation, processes, data flows, data stores, external entities, context diagram."
          LAB_STEPS="1. Draw a Context Diagram (Level 0 DFD) showing external system links\n2. Decompose Context to Level-1 DFD showing processes\n3. Verify data balance rules"
          Q="Which element in a Data Flow Diagram represents a person, organization, or external system that sends or receives data but is outside the boundary of the system?"
          OPTS="A) Process\nB) Data Store\nC) External Entity (Terminator)\nD) Data Flow Link"
          ANS="C"
          EXPL="External entities act as sources or destinations of information crossing system boundaries."
          DIST="Data stores represent persistent tables or files inside the system."
          ;;
        6)
          TOPIC="Data Modeling (ERD)"
          TERMS="Entity Relationship Diagrams (ERD), entities, attributes, relationships, cardinality (1:1, 1:N, M:N), Crow's Foot notation."
          LAB_STEPS="1. Identify entities and attributes in a customer ordering scenario\n2. Draw an ERD using Crow's Foot notation mapping relationships\n3. Resolve M:N relationships"
          Q="How must a many-to-many (M:N) relationship between two database entities be resolved in relational database design?"
          OPTS="A) Using a direct foreign key link\nB) Creating an associative (junction) entity that links both tables using 1:N relationships\nC) Combining both tables\nD) Deleting one of the entities"
          ANS="B"
          EXPL="Relational engines do not support direct M:N tables; an associative entity maps many-to-many links through two one-to-many relations."
          DIST="Direct keys only map 1:1 or 1:N linkages."
          ;;
        7)
          TOPIC="Object-Oriented Analysis UML"
          TERMS="Unified Modeling Language, Object-oriented analysis, class models, associations, encapsulation."
          LAB_STEPS="1. Map relational ERD models to UML class structures\n2. Define class attributes and operations\n3. Trace instantiation flows"
          Q="Which UML concept involves grouping data fields and the operations that modify them into a single class container to restrict direct access?"
          OPTS="A) Inheritance\nB) Encapsulation\nC) Polymorphism\nD) Abstraction"
          ANS="B"
          EXPL="Encapsulation protects object state by hiding internal data and requiring updates through public methods."
          DIST="Polymorphism handles interface execution variance. Inheritance defines subclass lines."
          ;;
        8)
          TOPIC="System Architecture & Design"
          TERMS="Architecture design, client-server models, cloud vs local hosting, network layouts."
          LAB_STEPS="1. Map client-server architecture layouts\n2. Compare latency impacts of database placements\n3. Review system node diagrams"
          Q="Which architecture model distributes application logic across client devices and central database nodes?"
          OPTS="A) Mainframe architecture\nB) Client-Server architecture\nC) Peer-to-Peer architecture\nD) Monolithic architecture"
          ANS="B"
          EXPL="Client-server structures split processing between client applications (web/mobile frontends) and backend database/application services."
          DIST="Mainframes process all calculations centrally."
          ;;
        9)
          TOPIC="User Interface Design"
          TERMS="User Interface (UI) design principles, navigation design, layout grids, wireframes, user experience (UX) feedback."
          LAB_STEPS="1. Sketch wireframe interfaces for client portal screens\n2. Map page navigation routes\n3. Design entry validation rules"
          Q="What is the primary objective of User Interface design?"
          OPTS="A) To write sql queries\nB) To make interactions user-friendly, efficient, and intuitive for final users\nC) To minimize CPU load\nD) To compile web server configurations"
          ANS="B"
          EXPL="UI/UX design is concerned with usability, accessibility, and facilitating user tasks efficiently."
          DIST="It targets human interaction interfaces rather than backend logic compilation."
          ;;
        10)
          TOPIC="Database Design & Normalization"
          TERMS="Normalization steps, First Normal Form (1NF), Second Normal Form (2NF), Third Normal Form (3NF), transitive dependencies."
          LAB_STEPS="1. Normalize a raw flat spreadsheet file into 1NF, 2NF, and 3NF relational tables\n2. Define keys and indexes\n3. Verify database integrity constraints"
          Q="What is the primary requirement for a database table to conform to Third Normal Form (3NF)?"
          OPTS="A) It must be in 2NF and contain no transitive dependencies (no non-key column depends on another non-key column)\nB) It must contain no null values\nC) It must use integer primary keys\nD) It must contain multiple tables"
          ANS="A"
          EXPL="3NF removes dependencies between non-primary key columns, eliminating redundant data modification anomalies."
          DIST="Null values are allowed in 3NF under appropriate designs."
          ;;
        11)
          TOPIC="Input and Output Design"
          TERMS="Data entry validation rules (range check, presence check), report layout structures, output formats."
          LAB_STEPS="1. Design data entry form validation logic templates\n2. Format transaction report outputs\n3. Audit input fields for errors"
          Q="Which form validation rule verifies that a value has actually been entered and is not left blank?"
          OPTS="A) Range Check\nB) Presence (Completeness) Check\nC) Format Check\nD) Consistency Check"
          ANS="B"
          EXPL="Presence checks verify that required fields contain data before submissions are processed."
          DIST="Range checks verify if numbers fall inside specific boundaries."
          ;;
        12)
          TOPIC="Program Design"
          TERMS="Structure charts, pseudo-code, modular design, coupling vs cohesion."
          LAB_STEPS="1. Draft pseudo-code specifications for core functions\n2. Create structure charts showing parameters passed\n3. Review module coupling variables"
          Q="What software architecture relationship is preferred in modular system design?"
          OPTS="A) High Coupling and High Cohesion\nB) Low Coupling and Low Cohesion\nC) Low Coupling and High Cohesion\nD) High Coupling and Low Cohesion"
          ANS="C"
          EXPL="Modular design aims for high cohesion (modules perform single tasks) and low coupling (modules are independent)."
          DIST="High coupling creates tight dependencies, making system changes difficult."
          ;;
        13)
          TOPIC="System Integration & Testing"
          TERMS="Integration test models, alpha testing, beta testing, user acceptance testing (UAT)."
          LAB_STEPS="1. Draft a UAT test script template\n2. Determine defect report parameters\n3. Verify system test logs"
          Q="Which testing type is conducted by actual business users in their operational environment to verify the system meets business objectives?"
          OPTS="A) Unit Testing\nB) Alpha Testing\nC) User Acceptance Testing (UAT)\nD) Regression Testing"
          ANS="C"
          EXPL="UAT validates operational readiness and is the final step before the system is signed off for production release."
          DIST="Alpha testing is internal testing by the development team."
          ;;
        14)
          TOPIC="System Installation & Conversion"
          TERMS="Conversion strategies: Direct cutover, Parallel conversion, Phased conversion, Pilot conversion."
          LAB_STEPS="1. Evaluate migration risk scenarios\n2. Draft a system conversion plan comparing Direct vs Parallel options\n3. Schedule data cutover times"
          Q="Which conversion strategy is the lowest risk because both the old and new systems are run simultaneously for a period of time?"
          OPTS="A) Direct Cutover\nB) Parallel Conversion\nC) Phased Conversion\nD) Pilot Conversion"
          ANS="B"
          EXPL="Parallel conversion allows verification of new outputs against the old system, fallback is immediate if failures occur."
          DIST="Direct cutover drops the old system immediately, presenting high risk."
          ;;
        15)
          TOPIC="Post-Implementation & Support"
          TERMS="Maintenance categories (corrective, adaptive, perfective, preventive), help desk setups, change management audits."
          LAB_STEPS="1. Classify maintenance requests into categories\n2. Draft system review templates\n3. Verify log updates"
          Q="Which type of software maintenance involves modifying a working system to support new operating system updates or server migrations?"
          OPTS="A) Corrective Maintenance\nB) Adaptive Maintenance\nC) Perfective Maintenance\nD) Preventive Maintenance"
          ANS="B"
          EXPL="Adaptive maintenance alters software to operate in changed hardware or software environments."
          DIST="Corrective maintenance fixes bugs. Perfective adds user-requested features."
          ;;
      esac
      ;;
  esac
}

# Helper to get week data for courses 7-10
get_week_data_3() {
  local course=$1
  local week=$2
  
  case "$course" in
    "CIS-4315_Cyber_Governance_Risk_Compliance")
      case "$week" in
        1)
          TOPIC="Security Governance Frameworks"
          TERMS="Information security governance, CIA triad, security alignments, strategic objectives."
          LAB_STEPS="1. Map security program alignments to corporate goals\n2. Review CIA triad definitions\n3. Document security steering committee responsibilities"
          Q="What is the primary objective of Information Security Governance?"
          OPTS="A) Installing host antiviruses\nB) Aligning the information security strategy with overall business objectives and goals\nC) Blocking internet traffic\nD) Encrypting database backups"
          ANS="B"
          EXPL="Governance ensures security operations support business goals, manage risks, and conform to corporate policies."
          DIST="Antivirus installations and network blocks are technical operations, not governance planning."
          ;;
        2)
          TOPIC="Security Policies & Standards"
          TERMS="Security policies, standards, guidelines, procedures, policy life cycles."
          LAB_STEPS="1. Draft an acceptable use policy (AUP) template\n2. Differentiate standards from guidelines\n3. Write standard operating procedures"
          Q="Which document type contains mandatory, baseline rules specifying hardware and software requirements across the organization?"
          OPTS="A) Policy\nB) Standard\nC) Guideline\nD) Procedure"
          ANS="B"
          EXPL="Standards are compulsory specifications. Policies are high-level goal definitions. Guidelines are recommended options."
          DIST="Guidelines are non-mandatory suggestions."
          ;;
        3)
          TOPIC="Risk Management Frameworks"
          TERMS="Risk management frameworks, NIST SP 800-37 (RMF), risk categorization, control selections."
          LAB_STEPS="1. Review NIST SP 800-37 steps\n2. Categorize a mock system based on FIPS 199 parameters\n3. Draft security control baseline selection criteria"
          Q="What is the first step of the NIST Risk Management Framework (RMF)?"
          OPTS="A) Categorize System\nB) Select Controls\nC) Prepare\nD) Implement Controls"
          ANS="C"
          EXPL="The RMF updated structure introduces Prepare as the initial step to align security goals prior to categorization."
          DIST="Categorize is the subsequent analytical step."
          ;;
        4)
          TOPIC="Asset Identification & Valuation"
          TERMS="Information assets, asset inventory, classification tiers (public, confidential), asset valuation metrics."
          LAB_STEPS="1. Create an asset inventory schema list\n2. Classify assets into security tiers\n3. Assign business value scores to databases"
          Q="Why is asset classification critical to risk management?"
          OPTS="A) To speed up network connections\nB) To ensure appropriate security controls are applied based on value and sensitivity of data\nC) To save local hard drive space\nD) To write database schema code"
          ANS="B"
          EXPL="Classification allows organizations to apply cost-effective, high-tier security parameters to sensitive assets."
          DIST="It is a resource prioritization mechanism, not a database design or network performance tool."
          ;;
        5)
          TOPIC="Risk Assessment Methodology"
          TERMS="Qualitative vs quantitative assessment, threats, vulnerabilities, likelihood, impact, Single Loss Expectancy (SLE), Annualized Loss Expectancy (ALE)."
          LAB_STEPS="1. Calculate SLE (Asset Value * Exposure Factor)\n2. Calculate ALE (SLE * Annualized Rate of Occurrence)\n3. Perform qualitative risk mapping"
          Q="An asset worth \$100,000 has an exposure factor of 40% if a server room flood occurs. The flood risk occurs once every 5 years. What is the ALE?"
          OPTS="A) \$40,000\nB) \$200,000\nC) \$8,000\nD) \$20,000"
          ANS="C"
          EXPL="SLE = \$100,000 * 0.40 = \$40,000. ARO = 1/5 = 0.2. ALE = SLE * ARO = \$40,000 * 0.2 = \$8,000."
          DIST="40,000 is the SLE. 8,000 is the annualized expected loss."
          ;;
        6)
          TOPIC="Risk Mitigation Strategies"
          TERMS="Risk treatment plans, risk acceptance limits, risk avoidance, risk mitigation, risk sharing/transfer."
          LAB_STEPS="1. Draft a risk treatment plan template\n2. Outline control recommendations for identified vulnerabilities\n3. Review risk registry balances"
          Q="Which risk treatment option involves completely eliminating the threat by stopping the business activity associated with the risk?"
          OPTS="A) Mitigation\nB) Avoidance\nC) Acceptance\nD) Transfer"
          ANS="B"
          EXPL="Risk avoidance stops the activity (e.g. disabling external website features to prevent SQL attacks completely)."
          DIST="Mitigation implements controls (e.g. firewalls) to reduce risk while keeping the activity active."
          ;;
        7)
          TOPIC="Business Impact Analysis"
          TERMS="Business Impact Analysis (BIA), critical business functions, Recovery Time Objective (RTO), Recovery Point Objective (RPO), Maximum Tolerable Downtime (MTD)."
          LAB_STEPS="1. Draft a BIA questionnaire layout\n2. Identify critical business processes and assign MTD scores\n3. Determine RTO/RPO limits"
          Q="Which metric defines the maximum acceptable age of data that must be recovered from backup storage after a system failure?"
          OPTS="A) Recovery Time Objective (RTO)\nB) Recovery Point Objective (RPO)\nC) Maximum Tolerable Downtime (MTD)\nD) Mean Time to Repair (MTTR)"
          ANS="B"
          EXPL="RPO measures data loss limits (e.g. RPO of 4 hours means backups must run at least every 4 hours)."
          DIST="RTO measures recovery duration (how long systems can remain offline)."
          ;;
        8)
          TOPIC="Disaster Recovery & Business Continuity"
          TERMS="Business Continuity Plan (BCP), Disaster Recovery Plan (DRP), hot/warm/cold sites, testing DRP (tabletop, walkthrough)."
          LAB_STEPS="1. Draft table-top exercise test agendas\n2. Compare hot vs cold recovery site parameters\n3. Write emergency activation procedures"
          Q="Which recovery site type is fully operational, contains real-time mirrored datasets, and can take over production workflows within minutes?"
          OPTS="A) Cold Site\nB) Warm Site\nC) Hot Site\nD) Mirror Store"
          ANS="C"
          EXPL="Hot sites are equipped with matching hardware, power, and synchronized datasets for rapid failovers."
          DIST="Cold sites have floor space and power but no hardware or data backups pre-loaded."
          ;;
        9)
          TOPIC="Regulatory Compliance (HIPAA, SOX)"
          TERMS="Regulatory compliance, Sarbanes-Oxley (SOX), Health Insurance Portability and Accountability Act (HIPAA), GLBA."
          LAB_STEPS="1. Audit system documentation for HIPAA privacy rule indicators\n2. Map SOX IT financial controls\n3. Review regulatory logs"
          Q="Which regulatory law mandates strict electronic security and privacy controls to protect patient health records?"
          OPTS="A) SOX\nB) HIPAA\nC) GLBA\nD) FISMA"
          ANS="B"
          EXPL="HIPAA enforces security controls surrounding protected health information (PHI)."
          DIST="SOX targets financial audit accuracy in public corporations."
          ;;
        10)
          TOPIC="Privacy Regulations (GDPR, CCPA)"
          TERMS="General Data Protection Regulation (GDPR), California Consumer Privacy Act (CCPA), Personally Identifiable Information (PII), right to be forgotten."
          LAB_STEPS="1. Document PII database tables locations\n2. Draft a GDPR right-to-be-forgotten deletion workflow script template\n3. Review privacy warnings"
          Q="What is the primary focus of the General Data Protection Regulation (GDPR)?"
          OPTS="A) Securing financial reports\nB) Protecting data privacy and individual rights for citizens of the European Union\nC) Regulating defense networks\nD) Setting software speed targets"
          ANS="B"
          EXPL="GDPR enforces strict guidelines on how personal data (PII) is collected, stored, and processed for EU residents."
          DIST="GDPR covers personal privacy, not corporate accounting or military systems."
          ;;
        11)
          TOPIC="Industry Standards (PCI-DSS, ISO)"
          TERMS="Payment Card Industry Data Security Standard (PCI-DSS), ISO/IEC 27001, security controls certification."
          LAB_STEPS="1. Review PCI-DSS 12 core requirements checklists\n2. Map ISO 27001 Annex A controls to company security policies\n3. Audit network segments"
          Q="Which standard is mandatory for any organization processing, storing, or transmitting credit card information?"
          OPTS="A) ISO 27001\nB) PCI-DSS\nC) NIST 800-53\nD) SOC 2"
          ANS="B"
          EXPL="PCI-DSS is established by major card brands to secure cardholder data environments."
          DIST="ISO 27001 is a voluntary international security framework."
          ;;
        12)
          TOPIC="Security Auditing Procedures"
          TERMS="IT audit, internal audit vs external audit, audit evidence, audit trail logs, control testing."
          LAB_STEPS="1. Draft an audit evidence request sheet\n2. Inspect system login logs for audit trail verification\n3. Review audit guidelines"
          Q="What is the primary purpose of an IT security audit?"
          OPTS="A) To write clean code\nB) To evaluate system operations and verify controls align with regulatory policies and design objectives\nC) To speed up database loops\nD) To purchase firewalls"
          ANS="B"
          EXPL="Auditors independently verify that documented security policies and control systems are actually operating as intended."
          DIST="It is an validation check, not a development or purchasing role."
          ;;
        13)
          TOPIC="Vendor Risk Management"
          TERMS="Third-party risk, vendor assessment, SOC 2 reports, service level agreements (SLA), security questionnaires."
          LAB_STEPS="1. Evaluate third-party vendor security disclosures\n2. Analyze a mock SOC 2 Type II report for control deficiencies\n3. Review vendor SLA metrics"
          Q="What is the key difference between a SOC 2 Type I and a SOC 2 Type II report?"
          OPTS="A) Type I covers security\nB) Type I assesses control design at a point in time; Type II evaluates operational effectiveness over a period of time\nC) Type I is public; Type II is confidential\nD) Type I is for software; Type II is for hardware"
          ANS="B"
          EXPL="Type II reports provide audit evidence confirming that controls were actively working over a testing window (usually 6-12 months)."
          DIST="Type I only checks if controls were documented and set up on a specific date."
          ;;
        14)
          TOPIC="Security Awareness Programs"
          TERMS="Social engineering mitigation, phishing simulations, user training metrics, security culture."
          LAB_STEPS="1. Draft a phishing simulation training slide outline\n2. Review metric statistics for user link clicks during tests\n3. Outline training agendas"
          Q="Which security measure is most effective at reducing the risk of successful phishing attacks against employees?"
          OPTS="A) Implementing longer passwords\nB) Continuous security awareness training and phishing simulations\nC) Turning off email servers\nD) Changing employee usernames"
          ANS="B"
          EXPL="Simulated training educates employees to spot warning signs (mismatched domains, urgent requests) before clicking links."
          DIST="Lengthy passwords do not stop users from typing credentials into fake sites."
          ;;
        15)
          TOPIC="Incident Response Governance"
          TERMS="Incident classification, escalation pathways, communication logs, post-incident reviews, regulatory notifications."
          LAB_STEPS="1. Draft an incident escalation flow chart\n2. Calculate regulatory breach notification schedules\n3. Complete post-incident analysis reports"
          Q="Why is establishing an incident escalation pathway critical in governance?"
          OPTS="A) To prevent compiler warnings\nB) To ensure security breaches are reported to appropriate executive management and legal teams within required schedules\nC) To speed up disk speeds\nD) To write code comments"
          ANS="B"
          EXPL="Escalation rules ensure critical security events receive immediate senior-level focus and meet regulatory notification laws."
          DIST="It targets communications and compliance governance."
          ;;
      esac
      ;;
    "CIS-4320_Enterprise_Systems_ERP")
      case "$week" in
        1)
          TOPIC="Enterprise Systems Concepts"
          TERMS="Enterprise Resource Planning (ERP), functional silos, integrated data, modular architectures."
          LAB_STEPS="1. Map business functional silos\n2. Evaluate database data redundency patterns\n3. Identify ERP business integration components"
          Q="What is the primary business value of implementing an Enterprise Resource Planning (ERP) system?"
          OPTS="A) It lets developers write custom Python games\nB) It integrates business data from disparate departments (finance, sales, inventory) into a single database system\nC) It removes the need for web servers\nD) It speeds up local CPU clock cycles"
          ANS="B"
          EXPL="ERP breaks down departmental silos by providing a single source of truth for business transaction data."
          DIST="ERP target integration of business logistics, not programming compilers."
          ;;
        2)
          TOPIC="Business Process Management"
          TERMS="Business Process Management (BPM), BPMN 2.0 notation, swimlanes, events, gateways, process optimization."
          LAB_STEPS="1. Draft a procurement process map using BPMN 2.0 swimlanes\n2. Analyze bottlenecks in a fulfillment pipeline\n3. Define event gateways"
          Q="In BPMN 2.0, what element is used to categorize activities based on which department or role performs them?"
          OPTS="A) Task box\nB) Gateway diamond\nC) Swimlane (Pool/Lane)\nD) Event circle"
          ANS="C"
          EXPL="Swimlanes separate tasks visually, assigning operational ownership to specific departments or users."
          DIST="Gateways direct logical splits in process routing."
          ;;
        3)
          TOPIC="ERP Selection & Vendor Landscape"
          TERMS="ERP vendors (SAP, Oracle, Microsoft Dynamics), selection criteria, total cost of ownership (TCO), RFP processes."
          LAB_STEPS="1. Compare ERP hosting scenarios (SaaS vs On-premise)\n2. Calculate TCO parameters for ERP proposals\n3. Draft vendor evaluation forms"
          Q="Which ERP vendor is historically the global market leader in enterprise application software?"
          OPTS="A) Salesforce\nB) SAP\nC) Adobe\nD) Red Hat"
          ANS="B"
          EXPL="SAP is the dominant enterprise database and ERP platform provider, utilized by the majority of global corporations."
          DIST="Salesforce is the leader in CRM systems specifically, rather than core ERP backbones."
          ;;
        4)
          TOPIC="ERP Implementation Lifecycle"
          TERMS="ERP implementation phases: Planning, Design, Customization, Testing, Go-live, change management."
          LAB_STEPS="1. Draft an ERP project timeline\n2. Analyze failure risks in ERP implementations\n3. Define system cutover checklists"
          Q="Why do ERP implementation projects historically have high failure rates?"
          OPTS="A) Lack of programming compilers\nB) Failure to manage organizational change and inadequate business process alignment\nC) Insufficient database disk space\nD) High network latency"
          ANS="B"
          EXPL="ERP success requires users to change how they work; resistance to new workflows and poor design mapping leads to failure."
          DIST="Hardware limitations are rarely the core cause of project failure."
          ;;
        5)
          TOPIC="Financial Management Modules"
          TERMS="General Ledger, Accounts Payable, Accounts Receivable, asset accounting, cost accounting, financial reporting."
          LAB_STEPS="1. Examine General Ledger double-entry transaction database links\n2. Map account matching rules\n3. Draft financial report templates"
          Q="Which ERP module records all financial transactions and serves as the primary data source for balance sheets?"
          OPTS="A) Material Management\nB) General Ledger (FI-GL)\nC) Sales and Distribution\nD) Human Capital Management"
          ANS="B"
          EXPL="The General Ledger is the central repository mapping accounts and balancing debits and credits."
          DIST="Material Management tracks warehouse inventory assets, not corporate accounting ledgers."
          ;;
        6)
          TOPIC="Supply Chain Management Integrations"
          TERMS="Supply Chain Management (SCM), inventory control, material requirements planning (MRP), logistics, vendor records."
          LAB_STEPS="1. Run a mock Material Requirements Planning (MRP) request\n2. Track inventory levels and purchase triggers\n3. Map supply chain links"
          Q="What is the function of Material Requirements Planning (MRP) in an ERP system?"
          OPTS="A) To design UI screens\nB) To calculate what materials are needed, in what quantities, and by what dates to meet production schedules\nC) To monitor database speeds\nD) To compile python scripts"
          ANS="B"
          EXPL="MRP uses inventory data, sales orders, and bill of materials (BOM) to schedule component purchases dynamically."
          DIST="MRP is logistics math, not UI styling or compiler optimization."
          ;;
        7)
          TOPIC="Customer Relationship Management Modules"
          TERMS="Customer Relationship Management (CRM), lead tracking, sales pipelines, account management, ticket systems."
          LAB_STEPS="1. Configure a sales lead tracking pipeline mapping stages\n2. Create customer profile database entries\n3. Map support ticket escalations"
          Q="Which business entity is the primary focus of a Customer Relationship Management (CRM) module?"
          OPTS="A) Raw material vendors\nB) Warehouse locations\nC) Customers and sales leads\nD) Corporate employee records"
          ANS="C"
          EXPL="CRM systems track customer details, sales interactions, pipelines, and helpdesk tickets to improve business relationships."
          DIST="HCM tracks employees. ERP warehouse modules track locations."
          ;;
        8)
          TOPIC="Human Capital Management Modules"
          TERMS="Human Capital Management (HCM), payroll processing, time tracking, employee onboarding, performance metrics."
          LAB_STEPS="1. Review payroll transaction database tables\n2. Map employee onboarding workflows\n3. Verify timecard hours calculations"
          Q="Which data class is managed inside an ERP Human Capital Management (HCM) module?"
          OPTS="A) Product pricing lists\nB) Employee records, payroll, benefits, and timecard logs\nC) Firewall security configurations\nD) DNS lookup zones"
          ANS="B"
          EXPL="HCM modules handle personnel files, payroll allocations, tax filings, and organizational structure mappings."
          DIST="Pricing is in sales modules. Firewall logs are system administration tasks."
          ;;
        9)
          TOPIC="ERP Database Structures"
          TERMS="Normalized tables, high transaction volume, indexing schemas, data dictionaries."
          LAB_STEPS="1. Analyze transactional table structures\n2. Trace index usage on high-volume queries\n3. Examine ERP database schemas"
          Q="Why do ERP databases utilize strict indexing and normalization layouts?"
          OPTS="A) To prevent users from writing queries\nB) To ensure high transactional integrity (ACID) and prevent data duplication across large volumes\nC) To run faster than standard HTML\nD) To bypass operating system checks"
          ANS="B"
          EXPL="ERP databases handle millions of records daily; normalization prevents update anomalies, and indexes speed up searches."
          DIST="HTML does not run databases, and OS checks are not related to normalization."
          ;;
        10)
          TOPIC="Customizing ERP Systems"
          TERMS="Low-code tools, proprietary scripting (Salesforce Apex, SAP ABAP), database triggers, validation rules."
          LAB_STEPS="1. Write a mock validation rule checking email syntax\n2. Draft APEX trigger pseudo-code updating database records\n3. Test trigger conditions"
          Q="Which programming language is proprietary to SAP and used to develop custom reports and database integrations?"
          OPTS="A) Python\nB) ABAP\nC) Apex\nD) SQL Server"
          ANS="B"
          EXPL="ABAP (Advanced Business Application Programming) is SAP's primary custom programming language."
          DIST="Apex is used for customizing Salesforce cloud platforms."
          ;;
        11)
          TOPIC="Enterprise Application Integration (EAI)"
          TERMS="EAI principles, REST/SOAP APIs, middleware brokers (MuleSoft), data transformation schemas."
          LAB_STEPS="1. Map database values to JSON API formats\n2. Draft middleware broker mapping definitions\n3. Trace REST integrations"
          Q="What role does middleware like MuleSoft play in enterprise system integration?"
          OPTS="A) It replaces database engines\nB) It acts as a broker, translating and routing data payloads between disparate applications\nC) It builds front-end client screens\nD) It hosts virtual machines"
          ANS="B"
          EXPL="Middleware connects different architectures (e.g. cloud CRM to legacy on-premise ERP) by translating data formats on-the-fly."
          DIST="It is a routing and translation layer, not storage or virtualization."
          ;;
        12)
          TOPIC="Data Migration"
          TERMS="Extract, Transform, Load (ETL), data cleaning, mapping templates, validation checks."
          LAB_STEPS="1. Clean database records removing duplicate contacts\n2. Map field variables from legacy CSV to ERP tables\n3. Verify import logs"
          Q="What does the Transform step in the ETL (Extract, Transform, Load) data migration process involve?"
          OPTS="A) Moving files to tape drives\nB) Cleaning, reformatting, and mapping raw data to match target database requirements\nC) Deleting records permanently\nD) Running compiler updates"
          ANS="B"
          EXPL="Transform adjusts data structures (e.g. splitting full names into first/last name columns) to match the target database schema."
          DIST="Extract pulls raw data. Load writes data to the new database."
          ;;
        13)
          TOPIC="ERP Security & Roles"
          TERMS="Role-Based Access Control (RBAC), Separation of Duties (SoD), audit profiles, permission sets."
          LAB_STEPS="1. Create user roles mapping permissions\n2. Audit roles for Separation of Duties (SoD) conflicts\n3. Document profile access scopes"
          Q="Which security concept is violated if a single ERP user is authorized to both approve purchase orders and issue vendor payments?"
          OPTS="A) Least Privilege\nB) Separation of Duties (SoD)\nC) High Availability\nD) Single Sign-On"
          ANS="B"
          EXPL="SoD prevents fraud by dividing critical transactional tasks (e.g. creating invoices vs paying them) between different users."
          DIST="Least Privilege restricts access to baseline requirements but doesn't specifically target fraud-prevention workflow splits."
          ;;
        14)
          TOPIC="Cloud ERP hosting"
          TERMS="Software as a Service (SaaS), hybrid clouds, multi-tenant databases, upgrade schedules."
          LAB_STEPS="1. Analyze SaaS upgrade cycles impacts on custom code\n2. Map multi-tenant database designs\n3. Compare cloud hosting SLA metrics"
          Q="What is a characteristic of a multi-tenant cloud database design?"
          OPTS="A) Each customer has their own physical server\nB) Multiple customers share the same database application instance and physical infrastructure, isolated logically\nC) It is unencrypted\nD) It does not support SQL"
          ANS="B"
          EXPL="Multi-tenancy allows cloud providers to scale resources by sharing physical infrastructure among customers while preserving strict security boundaries."
          DIST="Dedicated servers represent single-tenant infrastructure."
          ;;
        15)
          TOPIC="ERP Post-Implementation"
          TERMS="User adoption tracking, system performance reviews, bug databases, upgrading modules."
          LAB_STEPS="1. Draft user satisfaction survey templates\n2. Analyze system performance queries logs\n3. Write bug ticket triage outlines"
          Q="Why is post-implementation auditing critical for ERP deployments?"
          OPTS="A) To write code comments\nB) To evaluate if the system met the business objectives defined in the charter and address operational bugs\nC) To configure DNS records\nD) To clear hard drive logs"
          ANS="B"
          EXPL="Audits check if the system actually realized projected ROI, resolved bottlenecks, and is being utilized correctly by staff."
          DIST="It focuses on business value evaluation."
          ;;
      esac
      ;;
    "CIS-4350_DevSecOps_CICD_Pipelines")
      case "$week" in
        1)
          TOPIC="DevSecOps Culture"
          TERMS="DevSecOps definition, shift-left security, pipeline automation, feedback loops."
          LAB_STEPS="1. Map security gate checks in development lifecycle\n2. Analyze cost differences of finding bugs early vs late\n3. Document pipeline structures"
          Q="What does the term Shift-Left mean in DevSecOps methodology?"
          OPTS="A) Moving the development team to another room\nB) Integrating security practices, scanning, and testing earlier in the software development lifecycle\nC) Postponing testing until production\nD) Aligning script text to the left margin"
          ANS="B"
          EXPL="Shift-left brings security scanners directly into the developer's commit pipeline, resolving issues before deployments occur."
          DIST="It refers to workflow timing, not physical location or code formatting."
          ;;
        2)
          TOPIC="Continuous Integration Concepts"
          TERMS="Automation runners, local commit hooks, git triggers, linting steps."
          LAB_STEPS="1. Configure a local git pre-commit hook running code linters\n2. Analyze lint configuration files\n3. Test local commit constraints"
          Q="What is the primary function of a linter tool in a Continuous Integration pipeline?"
          OPTS="A) To compile binaries\nB) To analyze source code for programmatic errors, code smells, and style guide violations\nC) To host REST APIs\nD) To decrypt database keys"
          ANS="B"
          EXPL="Linters check code syntax and styling against standard formats (e.g. PEP 8 for Python), catching basic errors early."
          DIST="Compilers convert code. Linters analyze source text."
          ;;
        3)
          TOPIC="GitHub Actions Workflow"
          TERMS="GitHub Actions, YAML syntax, runner environments, steps, jobs, trigger events."
          LAB_STEPS="1. Write a GitHub Actions workflow script using YAML\n2. Configure runner triggers on git push events\n3. Verify build execution logs"
          Q="Which file format is used to configure GitHub Actions workflow pipeline scripts?"
          OPTS="A) JSON\nB) XML\nC) YAML\nD) CSV"
          ANS="C"
          EXPL="GitHub Actions workflows are declared in YAML files located inside the .github/workflows/ directory."
          DIST="YAML is standard for configuration scripts due to its human-readable layout."
          ;;
        4)
          TOPIC="Package & Artifact Management"
          TERMS="Artifact registries, package management (npm, pip), version tagging, securing packages."
          LAB_STEPS="1. Build package directories\n2. Configure build artifacts outputs inside pipelines\n3. Upload build packages to mock registries"
          Q="Why should pipelines upload validated builds to a secure artifact registry?"
          OPTS="A) To delete local source files\nB) To maintain single, unalterable build versions that can be deployed repeatably across target environments\nC) To run tests faster\nD) To bypass license checks"
          ANS="B"
          EXPL="Registry repositories host ready-to-deploy, version-controlled binaries, ensuring environment consistency."
          DIST="It is about build consistency and repeatability."
          ;;
        5)
          TOPIC="Docker Containerization in CI/CD"
          TERMS="Dockerfile syntax, container layers, caching strategies, building images in pipelines."
          LAB_STEPS="1. Write a multi-stage Dockerfile for a node app\n2. Configure docker build steps in CI pipeline\n3. Test container locally"
          Q="What is the benefit of using multi-stage builds in a Dockerfile?"
          OPTS="A) It compiles the container to run on multiple ports\nB) It allows separate build environments and produces smaller, minimized final deployment images\nC) It encrypts container data\nD) It requires no base image"
          ANS="B"
          EXPL="Multi-stage builds allow compiler tools to run in early stages, copying only the final binaries to the lean deployment image."
          DIST="It focuses on reducing the final attack surface and image size."
          ;;
        6)
          TOPIC="Static Application Security Testing"
          TERMS="SAST scanners, static analysis, pattern matching, false positives management."
          LAB_STEPS="1. Configure a SAST scanner tool in pipeline\n2. Scan a repository containing security issues\n3. Review scan reports"
          Q="What is the characteristic behavior of a SAST (Static Application Security Testing) tool?"
          OPTS="A) It scans code by executing the application in a test sandbox\nB) It analyzes source code files statically without running the application\nC) It monitors CPU fan speeds\nD) It blocks network ports dynamically"
          ANS="B"
          EXPL="SAST scanners evaluate source files against known vulnerability patterns (e.g. hardcoded keys, SQL concatenation)."
          DIST="Dynamic testing (DAST) requires executing the code."
          ;;
        7)
          TOPIC="Dynamic Application Security Testing"
          TERMS="DAST scanners, OWASP ZAP, active scanning, sandbox testing, network responses."
          LAB_STEPS="1. Setup web app in a pipeline container\n2. Run a DAST scanner against web endpoint\n3. Verify vulnerability detections"
          Q="How does DAST (Dynamic Application Security Testing) scan for security vulnerabilities?"
          OPTS="A) By reading source code files\nB) By testing the running application, simulating real attacks from an external perspective\nC) By analyzing database backups on disk\nD) By scanning the developer's laptop"
          ANS="B"
          EXPL="DAST scanners send requests (like SQL injection tests) to active endpoints to evaluate responses."
          DIST="SAST reads code text; DAST tests live responses."
          ;;
        8)
          TOPIC="Software Composition Analysis"
          TERMS="Software Composition Analysis (SCA), dependency trees, CVE databases, license compliance."
          LAB_STEPS="1. Run a SCA scan on dependencies\n2. Identify vulnerable packages\n3. Review update mitigations"
          Q="What is the primary function of a Software Composition Analysis (SCA) tool?"
          OPTS="A) To design UI screens\nB) To identify open-source third-party dependencies with known security vulnerabilities (CVEs)\nC) To speed up network links\nD) To compile python packages"
          ANS="B"
          EXPL="SCA scans dependency definition files (e.g. package.json, requirements.txt) against vulnerability databases."
          DIST="It maps external package risks, not local code logic or compilation."
          ;;
        9)
          TOPIC="Infrastructure as Code CI/CD Integration"
          TERMS="IaC validation, linter checks (tflint), security scanning (checkov, tfsec), pipeline execution."
          LAB_STEPS="1. Write checkov scanning script for terraform files\n2. Integrate tfsec scanner in pipeline\n3. Analyze security failures in outputs"
          Q="What does a tool like Checkov or tfsec scan for in a DevSecOps pipeline?"
          OPTS="A) Variable name typos\nB) Misconfigured cloud resources and security violations in IaC templates\nC) Operating system crashes\nD) Hard drive block sizes"
          ANS="B"
          EXPL="IaC scanners flag security risks (such as open S3 buckets or unencrypted disks) before the cloud resources are built."
          DIST="They target IaC configurations, not compiled software errors."
          ;;
        10)
          TOPIC="Automated Cloud Deployment"
          TERMS="Deployment strategies, canary releases, blue-green deployment, rollback procedures."
          LAB_STEPS="1. Map blue-green deployment server routing configurations\n2. Draft rollback triggers on health failure tests\n3. Verify system node health"
          Q="Which deployment strategy maintains two identical environments, routing traffic to one while updating and testing the other?"
          OPTS="A) Direct Cutover\nB) Blue-Green Deployment\nC) Rolling Update\nD) Shadow Deployment"
          ANS="B"
          EXPL="Blue-green deployment minimizes downtime and risk; if the new environment (green) fails, routing redirects to the old (blue)."
          DIST="Canary releases slowly roll out updates to a small subset of users."
          ;;
        11)
          TOPIC="Secret Management in Pipelines"
          TERMS="Secret scanning, git leaks prevention, HashiCorp Vault, encrypted env variables."
          LAB_STEPS="1. Configure github actions secrets variables\n2. Run a git leak scan detecting exposed tokens\n3. Verify secrets masking in logs"
          Q="Why should API keys and database passwords never be hardcoded in Git source files?"
          OPTS="A) Git cannot compile files with secrets\nB) Once pushed, keys are saved in history logs and can be exposed to unauthorized parties\nC) Secrets slow down code execution\nD) Secrets cause network routing loops"
          ANS="B"
          EXPL="Git histories are persistent; exposing keys allows attackers to scrape repositories and compromise systems."
          DIST="It is a severe security risk, not a compilation or speed constraint."
          ;;
        12)
          TOPIC="Container Security & Scan"
          TERMS="Container base images, image scanning (Trivy), rootless containers, registry configurations."
          LAB_STEPS="1. Run Trivy container scan\n2. Identify high vulnerability counts\n3. Refactor Dockerfile to use alpine base image"
          Q="Which base image is preferred in container security to minimize vulnerability footprints?"
          OPTS="A) Ubuntu Desktop\nB) Alpine Linux (minimal)\nC) Windows Server Core\nD) Debian Bullseye (Full)"
          ANS="B"
          EXPL="Alpine is a lightweight Linux distribution containing minimal binaries, reducing the attack surface."
          DIST="Standard distributions package hundreds of packages, raising vulnerability risks."
          ;;
        13)
          TOPIC="Monitoring, Logging & Telemetry"
          TERMS="Log aggregates, application telemetry, ELK stack, Prometheus, system alerts."
          LAB_STEPS="1. Map application telemetry flows\n2. Configure alert parameters on server failure states\n3. Review centralized logs dashboards"
          Q="What is the purpose of centralized logging in DevOps?"
          OPTS="A) To write code logic\nB) To aggregate system and application logs from all servers into a single queried portal\nC) To host DNS domains\nD) To execute unit tests"
          ANS="B"
          EXPL="Centralized logs permit rapid query searches across microservices during system failures, debugging issues quickly."
          DIST="It targets operations management, not software compilation."
          ;;
        14)
          TOPIC="Chaos Engineering Basics"
          TERMS="Chaos engineering definition, failure injection (Chaos Monkey), resilience testing, fallback paths."
          LAB_STEPS="1. Map server crash scenarios\n2. Outline system resilience paths handling cluster node drops\n3. Document fallback workflows"
          Q="What is the primary goal of Chaos Engineering?"
          OPTS="A) To write disorganized code\nB) To proactively inject failures into production systems to test and improve system resilience\nC) To reduce network bandwidth\nD) To bypass security firewalls"
          ANS="B"
          EXPL="Chaos engineering validates that clusters and databases degrade gracefully and auto-recover from server failures."
          DIST="It targets infrastructure testing, not code layout or network throttling."
          ;;
        15)
          TOPIC="DevSecOps Compliance & Audit"
          TERMS="Compliance as Code, pipeline audit logs, signed commits, build logs validation."
          LAB_STEPS="1. Verify signed git commits indicators\n2. Audit pipeline logs for control compliance checks\n3. Draft release approval forms"
          Q="How does automated pipeline logging support regulatory compliance audits?"
          OPTS="A) It compiles python scripts\nB) It provides unalterable audit trails proving that every code release was tested, scanned, and authorized\nC) It deletes code history\nD) It speeds up database speeds"
          ANS="B"
          EXPL="Auditors require proof that release procedures are followed; CI/CD logs serve as immutable operational logs."
          DIST="It supports regulatory audit checks, not compiler execution."
          ;;
      esac
      ;;
    "CIS-4355_IoT_Embedded_Systems")
      case "$week" in
        1)
          TOPIC="IoT Architecture Layers"
          TERMS="IoT layers (Perception, Network, Support, Application), edge devices, smart sensors, gateways."
          LAB_STEPS="1. Map IoT component configurations\n2. Analyze latency differences of edge processing vs cloud\n3. Identify network points"
          Q="Which IoT architecture layer contains the sensors, actuators, and hardware components that interact with the physical environment?"
          OPTS="A) Application Layer\nB) Perception (Sensing) Layer\nC) Network Layer\nD) Support Layer"
          ANS="B"
          EXPL="The Perception layer handles physical signals (temperature, light, motions) and digitizes them."
          DIST="Network layer handles communications routing (gateways, routers)."
          ;;
        2)
          TOPIC="Microcontrollers & Interfaces"
          TERMS="General Purpose Input/Output (GPIO), I2C protocol, SPI bus, analog-to-digital converter (ADC)."
          LAB_STEPS="1. Trace pin connections layouts\n2. Write sensor reading loop scripts using Python/C modules\n3. Inspect communication timing"
          Q="How many data wire lines are used in the I2C communication protocol?"
          OPTS="A) One wire\nB) Two wires (SDA and SCL)\nC) Four wires (MISO, MOSI, SCK, CS)\nD) Eight wires"
          ANS="B"
          EXPL="I2C uses a Serial Data (SDA) line and a Serial Clock (SCL) line, supporting multiple master/slave nodes."
          DIST="SPI uses four wire lines (MISO, MOSI, SCK, CS)."
          ;;
        3)
          TOPIC="Embedded Programming C/C++"
          TERMS="Memory constraints, pointers, bitwise operations, registers mapping, static allocations."
          LAB_STEPS="1. Write a C script compiling bitwise shifts toggling flags\n2. Manage memory pointers without leaks\n3. Verify memory usage"
          Q="Why is static memory allocation preferred over dynamic allocation (malloc) in high-reliability embedded systems?"
          OPTS="A) Static memory runs slower\nB) Dynamic allocation risks heap fragmentation and runtime memory exhaustion (out-of-memory crashes)\nC) C does not support dynamic allocation\nD) Pointers are not allowed"
          ANS="B"
          EXPL="Microcontrollers have tiny RAM capacities; heap fragmentation can trigger unpredictable system crashes during long-term runs."
          DIST="Dynamic memory is supported in C but highly restricted in embedded code."
          ;;
        4)
          TOPIC="RTOS Concepts"
          TERMS="Real-Time Operating System (RTOS), deterministic scheduling, task priority, preemptive kernels, semaphores."
          LAB_STEPS="1. Map task priorities schedules in RTOS framework\n2. Trace semaphore locking processes\n3. Verify task execution"
          Q="What is the defining characteristic of a Real-Time Operating System (RTOS)?"
          OPTS="A) It features a graphical user interface\nB) It guarantees deterministic, predictable task execution and meeting timing constraints\nC) It requires massive hard drive spaces\nD) It only supports web servers"
          ANS="B"
          EXPL="RTOS priority-driven scheduling guarantees that critical tasks complete within strict deadlines."
          DIST="RTOS environments are minimal and rarely include graphical UI systems."
          ;;
        5)
          TOPIC="IoT Protocols (MQTT/CoAP)"
          TERMS="Message Queuing Telemetry Transport (MQTT), publisher-subscriber, MQTT broker, CoAP (UDP-based)."
          LAB_STEPS="1. Configure a local MQTT broker (Mosquitto) server\n2. Publish sensor message packets using CLI command\n3. Subscribe client to topics"
          Q="What is the communication pattern utilized in the MQTT protocol?"
          OPTS="A) Client-Server HTTP\nB) Publish-Subscribe (Pub/Sub)\nC) Peer-to-Peer streaming\nD) File Transfer Protocol"
          ANS="B"
          EXPL="Clients publish data to topics on a central broker, which routes the messages to subscribed clients."
          DIST="HTTP uses a standard Request-Response pattern."
          ;;
        6)
          TOPIC="Wireless Technologies"
          TERMS="Bluetooth Low Energy (BLE), Zigbee mesh, LoRaWAN long-range, Wi-Fi constraints, energy usage."
          LAB_STEPS="1. Compare wireless parameters (range, power, bandwidth) for IoT\n2. Analyze mesh routing topologies\n3. Verify network link ranges"
          Q="Which wireless protocol is best suited for low-power, long-range sensor networks deployed across agricultural fields?"
          OPTS="A) Bluetooth Low Energy (BLE)\nB) LoRaWAN\nC) Wi-Fi (802.11)\nD) Zigbee"
          ANS="B"
          EXPL="LoRaWAN offers long-range (kilometers) communications at extremely low power rates, sacrificing bandwidth."
          DIST="BLE is restricted to short ranges (meters). Wi-Fi consumes too much power."
          ;;
        7)
          TOPIC="Cloud IoT Gateways"
          TERMS="Cloud IoT registries, device identity, telemetry ingest, cloud integrations, MQTT bridges."
          LAB_STEPS="1. Map device registries registry settings\n2. Draft secure keys authentication scripts for devices\n3. Trace telemetry logs"
          Q="What is the primary function of a Cloud IoT Gateway?"
          OPTS="A) To compile device firmware binaries\nB) To authenticate devices securely and ingest massive streams of telemetry data into cloud systems\nC) To host web client pages\nD) To execute local physical tasks"
          ANS="B"
          EXPL="Cloud IoT Gateways provide the connection bridge, managing client device security certificates and ingesting raw sensor metrics."
          DIST="Gateways route messages, they do not write compiled firmware."
          ;;
        8)
          TOPIC="Embedded Security Threats"
          TERMS="OWASP IoT Top 10, default credentials, physical tampering, insecure firmware, missing encryption."
          LAB_STEPS="1. Audit device interfaces for open ports\n2. Locate vulnerable configurations\n3. Review attack methods"
          Q="According to the OWASP IoT Top 10, which vulnerability is historically the most exploited entry point for building device botnets?"
          OPTS="A) SQL Injection\nB) Use of hardcoded, weak, or default credentials\nC) High CPU temperatures\nD) Missing code comments"
          ANS="B"
          EXPL="Default telnet/SSH credentials allow automated scripts to brute-force devices and load malicious botnet scripts."
          DIST="IoT devices rarely host relational SQL databases."
          ;;
        9)
          TOPIC="Cryptography in Constrained Devices"
          TERMS="Symmetric vs asymmetric keys, hardware encryption modules (TPM), resource constraints, hashing."
          LAB_STEPS="1. Measure encryption execution speeds of AES vs RSA on test platform\n2. Analyze CPU load differences\n3. Verify crypt keys"
          Q="Why is symmetric cryptography (like AES) preferred over asymmetric cryptography (like RSA) for securing sensor data transmissions directly on microcontrollers?"
          OPTS="A) Symmetric crypto does not require keys\nB) Asymmetric math is highly resource-intensive and computationally expensive for low-power CPUs\nC) Symmetric crypto is not secure\nD) Asymmetric is only allowed on servers"
          ANS="B"
          EXPL="AES utilizes lightweight bitwise operations that execute quickly on small chips with minimal RAM and power."
          DIST="Both use keys, and asymmetric can run on small devices but consumes significant battery."
          ;;
        10)
          TOPIC="Secure Boot & OTA updates"
          TERMS="Secure boot process, crypt signatures, firmware verification, Over-The-Air (OTA) updates, rollback prevention."
          LAB_STEPS="1. Simulate firmware hash verification checks\n2. Review OTA secure signing certificate criteria\n3. Verify boot configurations"
          Q="How does Secure Boot protect an embedded IoT device?"
          OPTS="A) It boots the system faster\nB) It cryptographically verifies the signature of the bootloader and firmware before executing, preventing unsigned code runs\nC) It disables the power button\nD) It deletes system database logs"
          ANS="B"
          EXPL="Secure Boot checks digital signatures against keys burned into the hardware's root-of-trust, blocking tampered firmware."
          DIST="It is a verification check, not a boot booster."
          ;;
        11)
          TOPIC="IoT Gateway Security"
          TERMS="Local gateway configurations, protocol translation security, device isolation, firewall rules."
          LAB_STEPS="1. Configure firewall routing rules on a mock gateway interface\n2. Isolate IoT devices in separate VLAN subnet\n3. Audit network logs"
          Q="Why should IoT devices be isolated on a separate network segment (VLAN) from corporate workstations?"
          OPTS="A) To prevent devices from running out of batteries\nB) To contain security breaches, preventing compromised devices from being used to attack corporate assets\nC) To double network speeds\nD) To hide device MAC addresses"
          ANS="B"
          EXPL="Segmentation restricts lateral movement; if a smart camera is breached, the attacker cannot reach finance servers."
          DIST="It is about blast-radius containment, not battery life or speed."
          ;;
        12)
          TOPIC="Data Privacy in IoT Networks"
          TERMS="Sensor privacy, encrypting data at rest/transit, anonymization techniques, data storage limits."
          LAB_STEPS="1. Review database records for unencrypted sensor logs\n2. Draft data masking scripts for customer telemetry data\n3. Verify encryption"
          Q="What risk is presented by storing unencrypted device telemetry logs in a cloud database?"
          OPTS="A) Logs run out of space\nB) Unauthorized parties can read sensitive location or activity data during a database breach\nC) Databases cannot index logs\nD) The CPU utilization increases"
          ANS="B"
          EXPL="Telemetry data can contain sensitive information (GPS, power consumption). Encryption protects it from data leaks."
          DIST="It is a confidentiality risk, not a database index limit."
          ;;
        13)
          TOPIC="Edge Computing Concepts"
          TERMS="Edge computing vs cloud computing, data filtering, local analytics, offline operations."
          LAB_STEPS="1. Write a script filtering sensor spikes locally before sending to cloud\n2. Compare network payload size savings\n3. Verify data streams"
          Q="What is the primary advantage of Edge Computing in IoT systems?"
          OPTS="A) It eliminates the need for sensor hardware\nB) It processes data locally near the source, reducing latency, bandwidth consumption, and cloud reliance\nC) It runs without power\nD) It compiles web client designs"
          ANS="B"
          EXPL="Filtering and analyzing metrics at the gateway level reduces the volume of redundant data sent over network channels."
          DIST="Edge nodes still require hardware and power to execute operations."
          ;;
        14)
          TOPIC="Analyzing Telemetry Data"
          TERMS="Data streams, time-series data, database storage (InfluxDB), anomaly pattern detections."
          LAB_STEPS="1. Import time-series data using Pandas\n2. Plot sensor values over time\n3. Write basic anomaly threshold rules detecting outliers"
          Q="Which database type is optimized specifically for storing and querying continuous streams of sensor data tagged with timestamps?"
          OPTS="A) Relational Database (SQL)\nB) Time-Series Database (TSDB)\nC) Graph Database\nD) Key-Value Store"
          ANS="B"
          EXPL="TSDBs (e.g. InfluxDB) are optimized for sequential write speeds and calculating moving averages over time windows."
          DIST="Graph databases track node linkages. Key-value stores hold configuration data."
          ;;
        15)
          TOPIC="Secure IoT Network Architecture"
          TERMS="End-to-end security, trust boundaries, device lifecycle management, final system audits."
          LAB_STEPS="1. Draft a security audit report for an IoT system design\n2. Identify trust boundaries and gaps\n3. Formulate security improvements"
          Q="Which design principle recommends securing an IoT system at the device level, the network level, and the cloud application level?"
          OPTS="A) Single Point of Failure\nB) Defense in Depth (End-to-End Security)\nC) Simple Access Controls\nD) Direct Interface Trust"
          ANS="B"
          EXPL="Defense-in-depth ensures that if a control fails at one layer (e.g. Wi-Fi security), other layers (e.g. device auth, TLS) protect the system."
          DIST="Direct interface trust assumes elements inside are safe, which is a security risk."
          ;;
      esac
      ;;
  esac
}

echo "=== STARTING BASH COURSE GENERATOR ==="

COURSES=(
  "CIS-2315_Data_Structures_Algorithms"
  "CIS-3340_Full_Stack_Web_Dev"
  "CIS-3350_Software_Engineering_Agile"
  "CIS-4345_Machine_Learning_Deep_Learning"
  "CIS-3310_IT_Project_Management"
  "CIS-3312_Systems_Analysis_Design"
  "CIS-4315_Cyber_Governance_Risk_Compliance"
  "CIS-4320_Enterprise_Systems_ERP"
  "CIS-4350_DevSecOps_CICD_Pipelines"
  "CIS-4355_IoT_Embedded_Systems"
)

for course in "${COURSES[@]}"; do
  echo "Processing $course..."
  COURSE_DIR="$BASE_DIR/$course"
  mkdir -p "$COURSE_DIR"
  
  # Course Info
  mkdir -p "$COURSE_DIR/00_Course_Information"
  cat << EOF > "$COURSE_DIR/00_Course_Information/Syllabus.md"
# Course Syllabus: $course

**Description:** ${DESCS[$course]}

**Certification Path:** ${CERTS[$course]}

**OER Source:** ${OERS[$course]}
EOF

  # ZTC OER Guide
  cat << EOF > "$COURSE_DIR/ZTC_OER_Reading_Materials.md"
# $course: Zero Textbook Cost (ZTC) OER Guide
**Target Certification:** ${CERTS[$course]}

This course utilizes free open educational resources:
* **Primary Source:** ${OERS[$course]}
* **Secondary Source:** Official Vendor Documentation.
EOF

  # Modules 01 to 15
  for week in {1..15}; do
    # Format week number with leading zero
    WEEK_PAD=$(printf "%02d" $week)
    MOD_DIR="$COURSE_DIR/Module_$WEEK_PAD"
    mkdir -p "$MOD_DIR"
    
    # Initialize variables
    TOPIC=""
    TERMS=""
    LAB_STEPS=""
    Q=""
    OPTS=""
    ANS=""
    EXPL=""
    DIST=""
    
    # Retrieve week details
    if [[ "$course" == "CIS-2315_Data_Structures_Algorithms" || "$course" == "CIS-3340_Full_Stack_Web_Dev" || "$course" == "CIS-3350_Software_Engineering_Agile" ]]; then
      get_week_data "$course" $week
    elif [[ "$course" == "CIS-4345_Machine_Learning_Deep_Learning" || "$course" == "CIS-3310_IT_Project_Management" || "$course" == "CIS-3312_Systems_Analysis_Design" ]]; then
      get_week_data_2 "$course" $week
    else
      get_week_data_3 "$course" $week
    fi
    
    # If variables are empty, provide fallback
    if [ -z "$TOPIC" ]; then
      TOPIC="Introduction to $course - Topic $week"
      TERMS="Core terms, configurations, concepts, administration rules."
      LAB_STEPS="1. Boot local sandbox workstation environment\n2. Perform verification test runs\n3. Log script deliverables to central ledger"
      Q="Which concept represents the primary focus of $course in Week $week?"
      OPTS="A) Option One\nB) Option Two\nC) Option Three\nD) Option Four"
      ANS="A"
      EXPL="Option One represents the correct design choice for this week."
      DIST="Options B, C, and D are distractor answers."
    fi
    
    # Write Video Script
    cat << EOF > "$MOD_DIR/01_Video_Script_Module_$WEEK_PAD.md"
### Video Script: Module $WEEK_PAD - $TOPIC
**Target Certification:** ${CERTS[$course]}
**Estimated Duration:** 12-15 minutes

#### Visual Block
1. **Scene 1: Introduction (00:00 - 02:00)**
   * *Visual:* Instructor on screen with a background slide showing the module title: **$TOPIC**.
   * *Visual Details:* High-contrast diagram mapping the key concepts: $TERMS.
   
2. **Scene 2: Core Concept Deep-Dive (02:00 - 08:00)**
   * *Visual:* Split screen showing a code editor/terminal configuration window.
   * *Alt-Text Definition:* "Terminal interface showing command inputs and corresponding system outputs for the weekly lab topics."

3. **Scene 3: Lab Walkthrough & Summary (08:00 - End)**
   * *Visual:* Live terminal execution of verification commands. Diagram summarizing the final configuration state.

#### Audio Narration
* **Instructor:** "Welcome back! In this module, we are diving deep into **$TOPIC** as part of our preparation for the **${CERTS[$course]}** exam. We will cover: $TERMS. Let's boot up our systems and examine the configurations."
EOF

    # Write Reading Guide
    cat << EOF > "$MOD_DIR/02_Reading_Guide_Module_$WEEK_PAD.md"
### Reading Guide: Module $WEEK_PAD - $TOPIC
**Target Certification:** ${CERTS[$course]}

#### High-Yield Concepts
* **Core Objective:** Understand the mechanics, security parameters, and operational design of **$TOPIC**.
* **Key Terms:** $TERMS
* **Exam Tip:** Keep in mind that ${CERTS[$course]} questions frequently test the practical relationships between these terms and their default command parameters.

#### OER Study Reference
For detailed analysis, review the relevant chapters and sections in:
* **Primary Source:** Official Vendor Documentation for ${CERTS[$course]}.
* **Secondary Source:** Community Tutorials (linked in the course introduction guide).
EOF

    # Write Lab Activity
    cat << EOF > "$MOD_DIR/03_Lab_Module_$WEEK_PAD.md"
### Lab Activity: Module $WEEK_PAD - $TOPIC
**Target Certification:** ${CERTS[$course]}

#### Objective
Apply practical configurations for **$TOPIC** inside the virtual laboratory workstation.

#### Instructions
$(echo -e "$LAB_STEPS")

#### Deliverables
1. Capture a screenshot showing the successful verification command outcomes.
2. Log your submission details using the local script: \`/home/student/Training/txwes-submit.sh\`.
EOF

    # Write Quiz
    cat << EOF > "$MOD_DIR/04_Quiz_Module_$WEEK_PAD.md"
### Quiz: Module $WEEK_PAD - $TOPIC
**Target Certification:** ${CERTS[$course]}

**Question 1:**
$Q

$(echo -e "$OPTS")

---

* **Correct Answer:** $ANS
* **Explanation:** $EXPL
* **Distractor Analysis:** $DIST
EOF

  done

  # Module 16 (Final Exam)
  mkdir -p "$COURSE_DIR/Module_16"
  cat << EOF > "$COURSE_DIR/Module_16/02_Reading_Guide_Module_16.md"
### Reading Guide: Module 16 - Final Exam Prep

Review all study guides and practice quizzes from Module 01 through Module 15 in preparation for the official **${CERTS[$course]}** certification exam.
EOF

  cat << EOF > "$COURSE_DIR/Module_16/03_Lab_Module_16.md"
### Lab Activity: Module 16 - Final Exam Submission

**Objective:** Complete the official **${CERTS[$course]}** exam at the testing center and upload your score report to this dropbox to receive course credit.
EOF

done

echo "=== BASH COURSE GENERATION COMPLETE ==="
