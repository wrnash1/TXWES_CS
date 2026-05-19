#!/usr/bin/env python3
# enrich_course_content.py - Regenerates all 27 courses with rich, detailed, student-friendly markdown files.

import os
import urllib.parse
from generate_real_content import COURSES_DATA as ORIGINAL_DATA

BASE_DIR = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"

# Dictionary of definitions for common IT/CS concepts to generate detailed glossaries
TERM_DEFINITIONS = {
    # Data Structures & Algorithms
    "Big-O notation": "A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.",
    "space complexity": "The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).",
    "asymptotic analysis": "The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.",
    "worst-case": "The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.",
    "best-case": "The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).",
    "average-case": "The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.",
    "Node pointer": "A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.",
    "head node": "The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.",
    "tail node": "The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.",
    "doubly linked nodes": "Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.",
    "traversal overhead": "The additional execution time and CPU operations spent visiting nodes sequentially in memory, which is higher in linked structures than in contiguous arrays.",
    "LIFO (Last-In-First-Out)": "The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.",
    "FIFO (First-In-First-Out)": "The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.",
    "push/pop": "The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.",
    "enqueue/dequeue": "The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.",
    "Base case": "The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.",
    "recursive call": "An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.",
    "stack overflow risk": "The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.",
    "call stack frame": "The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.",
    "Root node": "The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.",
    "leaf node": "A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.",
    "binary search tree invariant": "The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.",
    "left child": "The descendant node connected to the left branch of a parent node in a binary tree structure.",
    "right child": "The descendant node connected to the right branch of a parent node in a binary tree structure.",
    "Self-balancing tree": "A binary search tree that automatically adjusts its height during insertions and deletions (e.g., AVL, Red-Black) to maintain logarithmic operations.",
    "balance factor": "The difference in height between the left and right subtrees of a node in an AVL tree, which must be -1, 0, or 1 to remain balanced.",
    "tree rotation": "An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.",
    "node recoloring": "An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.",
    "Min-heap": "A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.",
    "max-heap": "A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.",
    "heapify": "The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.",
    "complete binary tree": "A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.",
    "array representation": "An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).",
    
    # Web Development
    "Semantic markup": "HTML tags that convey the meaning and structure of the enclosed content to both the browser and search engines (e.g., <header>, <article>, <footer>) instead of generic containers.",
    "SEO optimization": "Search Engine Optimization; practices designed to improve the visibility and ranking of web pages in search engine results through clean HTML, meta tags, and alt text.",
    "head tags": "Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.",
    "accessibility guidelines (WCAG)": "Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).",
    "metadata": "Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.",
    "Flexbox": "Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.",
    "CSS Grid": "A two-dimensional CSS layout system that allows developers to design complex grid-based user interfaces with rows and columns, offering precise control over alignment.",
    "display attributes": "CSS properties (like block, inline, flex, grid) that determine how an element is rendered and how it behaves relative to surrounding elements.",
    "box model": "The core CSS layout block consisting of margins, borders, padding, and the actual content area, defining the sizing and spacing of every page element.",
    "sizing properties": "CSS rules (like width, height, max-width, box-sizing) that dictate how the dimensions of elements are calculated and rendered.",
    
    # CompTIA / Security / Cloud
    "ESD protection": "Electrostatic Discharge protection; tools (like wrist straps, grounding mats) used to prevent static electricity from destroying sensitive microchips when handling hardware.",
    "grounding": "The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.",
    "CIA triad": "The core security model consisting of Confidentiality (preventing unauthorized access), Integrity (preventing unauthorized modification), and Availability (ensuring systems are accessible when needed).",
    "NIST Risk Management Framework": "A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.",
    "Single Loss Expectancy (SLE)": "The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV * EF).",
    "Annualized Loss Expectancy (ALE)": "The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).",
    "Recovery Time Objective (RTO)": "The maximum acceptable duration of downtime before a business process or system must be restored to operation after a disaster.",
    "Recovery Point Objective (RPO)": "The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.",
    "Maximum Tolerable Downtime (MTD)": "The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.",
    "Blue-Green Deployment": "A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.",
    "Role-Based Access Control (RBAC)": "An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.",
    "Separation of Duties (SoD)": "A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).",
    
    # Defaults / Generic Fallback
    "default settings": "The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.",
}

# 10 New Courses Databases structured exactly like ORIGINAL_DATA
NEW_COURSES_DATA = {
    "CIS-2315_Data_Structures_Algorithms": {
        "cert": "Technical Interview Readiness (LeetCode / HackerRank)",
        "desc": "Data structures and algorithms, time and space complexity, recursion, balanced trees, heaps, graphs, sorting, and dynamic programming.",
        "oer": "OpenDSA (opendsa-server.cs.vt.edu)",
        "weeks": [
            {
                "topic": "Time & Space Complexity",
                "terms": "Big-O notation, space complexity, asymptotic analysis, worst-case, best-case, average-case.",
                "lab": ["Create a loop-based script and analyze its operations count", "Measure execution time of linear search vs binary search", "Document memory usage differences of array sizes"],
                "q": "What is the worst-case time complexity of inserting an element into a standard dynamic array (ArrayList) when it needs resizing?",
                "opts": ["A) O(1)", "B) O(log N)", "C) O(N)", "D) O(N log N)"],
                "ans": "C",
                "expl": "When a dynamic array runs out of capacity, it must allocate a new larger array and copy all N elements, taking O(N) time.",
                "dist": "O(1) is the amortized insertion time when no resize is needed. O(log N) is typical for binary search trees. O(N log N) represents comparison sorting."
            },
            {
                "topic": "Singly & Doubly Linked Lists",
                "terms": "Node pointer, head node, tail node, doubly linked nodes, traversal overhead.",
                "lab": ["Implement a singly linked list class in Python/C", "Write a method to reverse a singly linked list in place", "Measure list traversal times against array indexing"],
                "q": "What is the primary advantage of a doubly linked list over a singly linked list?",
                "opts": ["A) Requires less memory per node", "B) Allows traversal in both directions (forward and backward)", "C) O(1) random index access", "D) Faster sorting speed"],
                "ans": "B",
                "expl": "Each node in a doubly linked list contains pointers to both the next and previous nodes, allowing bidirectional traversal.",
                "dist": "A is incorrect because the previous pointer increases memory. C is wrong because linked lists require O(N) traversal to reach an index. D is false since list node link-rebuilding doesn't change algorithm bounds."
            },
            {
                "topic": "Stacks & Queues",
                "terms": "LIFO (Last-In-First-Out), FIFO (First-In-First-Out), push/pop, enqueue/dequeue.",
                "lab": ["Build a custom stack class using an array backend", "Build a queue using a linked list structure", "Implement a matching parenthesis checker using a stack"],
                "q": "Which data structure follows the LIFO (Last-In-First-Out) principle?",
                "opts": ["A) Queue", "B) Priority Queue", "C) Stack", "D) Hash Table"],
                "ans": "C",
                "expl": "A Stack works by inserting and removing from the same end, matching Last-In-First-Out behavior.",
                "dist": "Queue is FIFO (First-In-First-Out). Priority Queue removes based on key value, not order. Hash Table uses direct keys."
            },
            {
                "topic": "Recursion & Backtracking",
                "terms": "Base case, recursive call, stack overflow risk, call stack frame.",
                "lab": ["Write a recursive function to compute Fibonacci numbers", "Write a recursive factorial finder", "Debug recursive call stacks to trace frame allocations"],
                "q": "What must every functional recursive function include to avoid infinite recursion and stack overflow?",
                "opts": ["A) A global loop variable", "B) A base case that terminates recursion", "C) A try-except error wrapper", "D) A class destructor"],
                "ans": "B",
                "expl": "The base case acts as the exit condition where the recursion stops calling itself.",
                "dist": "Loops are not required for recursion. Error wrappers only capture crashes but don't prevent them. Destructors manage memory deallocation but not logical call structures."
            },
            {
                "topic": "Binary Trees & BSTs",
                "terms": "Root node, leaf node, binary search tree invariant, left child, right child.",
                "lab": ["Define a TreeNode class", "Implement insert and find methods for a BST", "Verify tree traversal orders (inorder, preorder, postorder)"],
                "q": "In a valid Binary Search Tree (BST), what property must be true for every node N?",
                "opts": ["A) All left descendants <= N, and all right descendants > N", "B) Left child and right child must have equal height", "C) Every node must have exactly two child nodes", "D) The tree must be balanced"],
                "ans": "A",
                "expl": "The BST invariant requires all values in the left subtree of N to be less than or equal to N, and all values in the right subtree to be greater.",
                "dist": "Equal height defines balanced trees. Node count properties define strict binary trees."
            },
            {
                "topic": "AVL Trees & Red-Black Trees",
                "terms": "Self-balancing tree, balance factor, tree rotation, node recoloring.",
                "lab": ["Simulate balance factor calculation of nodes", "Trace left/right tree rotations on paper", "Draw AVL inserts step-by-step"],
                "q": "What is the maximum height of an AVL tree containing N nodes?",
                "opts": ["A) O(1)", "B) O(log N)", "C) O(N)", "D) O(N^2)"],
                "ans": "B",
                "expl": "AVL trees guarantee a logarithmic height by maintaining a strict balance factor difference of at most 1.",
                "dist": "O(N) is the height of an unbalanced degenerate tree (linked list)."
            },
            {
                "topic": "Heaps & Priority Queues",
                "terms": "Min-heap, max-heap, heapify, complete binary tree, array representation.",
                "lab": ["Build a min-heap array index mapper", "Use Python heapq module to sort a list", "Find top K elements using heaps"],
                "q": "Which array index represents the parent of a node located at index i in a 0-indexed binary heap?",
                "opts": ["A) 2*i + 1", "B) 2*i + 2", "C) (i - 1) // 2", "D) i // 2"],
                "ans": "C",
                "expl": "For any 0-indexed element i, its parent is located at index floor((i-1)/2).",
                "dist": "2*i+1 is left child. 2*i+2 is right child."
            },
            {
                "topic": "Hash Tables & Hash Collisions",
                "terms": "Hash function, load factor, collision resolution, chaining, open addressing.",
                "lab": ["Implement a simple modulo hash table", "Simulate collision resolution using linear probing", "Compare lookup times"],
                "q": "What is the average-case time complexity of searching for a key in a well-distributed Hash Table?",
                "opts": ["A) O(1)", "B) O(log N)", "C) O(N)", "D) O(N log N)"],
                "ans": "A",
                "expl": "If the hash function distributes keys evenly, finding a key via constant hash mapping takes O(1) time.",
                "dist": "O(N) is the worst-case hash table lookup (when all keys collide into a single chain)."
            },
            {
                "topic": "Graph Representations",
                "terms": "Adjacency matrix, adjacency list, directed graph, undirected graph, edge weights.",
                "lab": ["Construct a graph using adjacency list representation", "Construct the same graph as adjacency matrix", "Analyze memory constraints"],
                "q": "Which representation is most memory-efficient for a sparse graph with N vertices and few edges?",
                "opts": ["A) Adjacency Matrix", "B) Adjacency List", "C) Edge List", "D) Hash Matrix"],
                "ans": "B",
                "expl": "Adjacency lists only store actual links, bypassing the O(N^2) memory footprint of adjacency matrices.",
                "dist": "Adjacency matrix always uses O(V^2) memory space regardless of edge density."
            },
            {
                "topic": "Breadth-First & Depth-First Search",
                "terms": "BFS traversal, DFS traversal, queue frontier, stack frame, visited set.",
                "lab": ["Implement BFS algorithm on adjacency list using a queue", "Implement DFS using recursion/stack", "Trace path discovery"],
                "q": "Which traversal algorithm uses a queue to visit all nodes at the current depth level before moving to the next level?",
                "opts": ["A) Depth-First Search (DFS)", "B) Breadth-First Search (BFS)", "C) Preorder traversal", "D) Postorder traversal"],
                "ans": "B",
                "expl": "BFS processes nodes level by level using a FIFO queue to store discovered frontier vertices.",
                "dist": "DFS travels deep along a branch first, typically implemented using a LIFO stack."
            },
            {
                "topic": "Dijkstra's Shortest Path",
                "terms": "Single-source shortest path, priority queue, edge relaxation, negative edge weights restriction.",
                "lab": ["Write Dijkstra algorithm on weighted adjacency list", "Find shortest path between two nodes", "Verify output correctness"],
                "q": "Why is Dijkstra's algorithm unable to guarantee correct shortest paths in graphs with negative edge weights?",
                "opts": ["A) It uses a queue instead of stack", "B) Once a vertex is visited/relaxed, the algorithm assumes its shortest path is permanently solved", "C) It only works on binary trees", "D) It runs in O(N^3) time"],
                "ans": "B",
                "expl": "Dijkstra's greedy choice assumes that paths can only increase in cost; a negative edge can invalidate earlier evaluations.",
                "dist": "Bellman-Ford is used for graphs with negative weights because it repeatedly relaxes all edges."
            },
            {
                "topic": "Divide & Conquer",
                "terms": "Recursion divide, conquer combining, merge sort, quick sort, pivot selection.",
                "lab": ["Implement Merge Sort", "Implement Quick Sort with in-place swapping", "Compare sorting execution times"],
                "q": "What is the average and worst-case time complexity of the Quick Sort algorithm?",
                "opts": ["A) Average: O(N log N), Worst: O(N^2)", "B) Average: O(N), Worst: O(N log N)", "C) Average: O(N log N), Worst: O(N log N)", "D) Average: O(N^2), Worst: O(N^2)"],
                "ans": "A",
                "expl": "Quick Sort runs in O(N log N) on average, but degrades to O(N^2) if the pivot splits the array highly unevenly (e.g. sorted arrays).",
                "dist": "Merge Sort guarantees O(N log N) in both average and worst cases but requires O(N) extra memory space."
            },
            {
                "topic": "Greedy Algorithms",
                "terms": "Local optimum, global optimum, Minimum Spanning Tree (MST), Kruskal, Prim.",
                "lab": ["Implement Prim's MST algorithm", "Implement Kruskal's algorithm using disjoint sets", "Compute minimum tree weight"],
                "q": "Kruskal's algorithm finds the Minimum Spanning Tree by sorting which properties of the graph first?",
                "opts": ["A) Vertex degrees", "B) Edge weights", "C) Path lengths", "D) Adjacency matrices"],
                "ans": "B",
                "expl": "Kruskal's algorithm is a greedy algorithm that processes edges in ascending order of their weights, checking for cycles.",
                "dist": "Prim's algorithm starts from a root node and expands the tree using local minimum edges."
            },
            {
                "topic": "Dynamic Programming Basics",
                "terms": "Overlapping subproblems, optimal substructure, memoization (top-down), tabulation (bottom-up).",
                "lab": ["Solve Fibonacci using memoization dict", "Solve Knapsack 0/1 using tabulation grid", "Compare execution steps"],
                "q": "What is the difference between Memoization and Tabulation in Dynamic Programming?",
                "opts": ["A) Memoization is bottom-up; Tabulation is top-down", "B) Memoization is top-down recursive; Tabulation is bottom-up iterative", "C) Memoization uses more memory", "D) Tabulation requires recursive helper calls"],
                "ans": "B",
                "expl": "Memoization caches recursive call outputs (top-down). Tabulation fills a table iteratively from basic inputs (bottom-up).",
                "dist": "Tabulation is non-recursive, avoiding stack overflow errors."
            },
            {
                "topic": "String Algorithms & Trie",
                "terms": "Prefix search, suffix tree, string matching, Knuth-Morris-Pratt (KMP), Trie node.",
                "lab": ["Implement a Trie class with insert and search methods", "Implement startsWith prefix search", "Test autocomplete matches"],
                "q": "Which data structure is most suitable for implementing autocomplete systems or dictionary prefix matching?",
                "opts": ["A) AVL Tree", "B) Hash Table", "C) Trie (Prefix Tree)", "D) Max Heap"],
                "ans": "C",
                "expl": "Tries store characters along branches, sharing common prefixes which allows rapid string prefix searches.",
                "dist": "Hash Table can find exact keys, but cannot efficiently match prefixes."
            }
        ]
    },
    "CIS-3340_Full_Stack_Web_Dev": {
        "cert": "AWS Certified Developer - Associate",
        "desc": "HTML5, CSS layouts, asynchronous JavaScript, REST APIs, Express servers, databases, React hooks, JWT security, and AWS EC2/S3 cloud deployment.",
        "oer": "Mozilla Developer Network (developer.mozilla.org)",
        "weeks": [
            {
                "topic": "HTML5 Semantics & SEO",
                "terms": "Semantic markup, SEO optimization, head tags, accessibility guidelines (WCAG), metadata.",
                "lab": ["Draft a structured HTML page using semantic tags", "Verify tags against accessibility validator", "Write descriptive alt text"],
                "q": "Which HTML5 tag is considered a semantic element?",
                "opts": ["A) <div>", "B) <span>", "C) <article>", "D) <b>"],
                "ans": "C",
                "expl": "<article> has semantic meaning, telling the browser and search engines about the nature of the enclosed text content.",
                "dist": "div and span are generic container tags with no semantic value."
            },
            {
                "topic": "Modern CSS Layouts",
                "terms": "Flexbox, CSS Grid, display attributes, box model, sizing properties.",
                "lab": ["Configure a CSS Flexbox card container", "Configure a CSS Grid dashboard interface", "Debug layout overlapping elements"],
                "q": "Which CSS property converts an element into a grid container?",
                "opts": ["A) display: grid", "B) layout: grid", "C) grid-template: true", "D) position: relative"],
                "ans": "A",
                "expl": "Setting display: grid instructs the rendering engine to compute nested children as grid items.",
                "dist": "display is the core CSS layout configuration property."
            },
            {
                "topic": "Responsive Design",
                "terms": "Media queries, viewport configurations, fluid grid units (em, rem, vw), breakpoint guidelines.",
                "lab": ["Configure a mobile-first responsive landing page stylesheet", "Add media queries to handle dynamic resizing", "Test viewport sizing"],
                "q": "What media query rule targets screen sizes that are 768px wide or smaller?",
                "opts": ["A) @media (min-width: 768px)", "B) @media (max-width: 768px)", "C) @media screen 768", "D) @breakpoint 768px"],
                "ans": "B",
                "expl": "max-width: 768px matches screens up to and including 768px in width.",
                "dist": "min-width matches screens that are at least 768px wide."
            },
            {
                "topic": "JavaScript DOM Manipulation",
                "terms": "Document Object Model (DOM), query selectors, event listeners, bubbling and capturing, dynamic DOM trees.",
                "lab": ["Implement DOM selector query loops", "Add keydown/click event listeners to forms", "Dynamically append list elements using JavaScript"],
                "q": "Which DOM query method retrieves all page elements matching a class identifier?",
                "opts": ["A) document.getElementById()", "B) document.querySelector()", "C) document.querySelectorAll()", "D) document.classList()"],
                "ans": "C",
                "expl": "querySelectorAll returns a NodeList of all page elements matching the provided CSS selector.",
                "dist": "querySelector only returns the first matching node."
            },
            {
                "topic": "Asynchronous JavaScript",
                "terms": "Call stack, event loop, callback queue, Promises, async/await constructs, error handling.",
                "lab": ["Write callback loops", "Write fetch calls returning Promises", "Refactor promises using async/await syntax and try-catch blocks"],
                "q": "What state does a JavaScript Promise enter once it has completed successfully?",
                "opts": ["A) Pending", "B) Fulfilled", "C) Rejected", "D) Resolved"],
                "ans": "B",
                "expl": "Promises transition from Pending to either Fulfilled (resolved successfully) or Rejected (errored out).",
                "dist": "Resolved is the general term for completion, but the explicit state is Fulfilled."
            },
            {
                "topic": "RESTful API Principles",
                "terms": "Representational State Transfer (REST), endpoints, resource identifiers, HTTP verbs, status codes.",
                "lab": ["Map HTTP endpoints using standard RESTful naming conventions", "Test endpoints using mock client payloads", "Inspect API headers"],
                "q": "Which HTTP status code class indicates a server-side processing error occurred?",
                "opts": ["A) 2xx", "B) 3xx", "C) 4xx", "D) 5xx"],
                "ans": "D",
                "expl": "5xx status codes (e.g. 500 Internal Server Error) represent backend processing failures.",
                "dist": "4xx is for client-side input errors (e.g. 404 Not Found)."
            },
            {
                "topic": "Node.js & Express Server",
                "terms": "Node event loop, package manager (NPM), Express framework, server setup, listening sockets.",
                "lab": ["Initialize npm package settings", "Create base Express routing script file", "Listen to connections on port 3000"],
                "q": "Which code snippet initializes a basic Express application instance?",
                "opts": ["A) const app = express()", "B) const app = new express.App()", "C) const app = require('express').start()", "D) const app = Express.init()"],
                "ans": "A",
                "expl": "Invoking the required express module function creates an application instance.",
                "dist": "The other options show incorrect module instantiation syntax."
            },
            {
                "topic": "Server-Side Routing & Middleware",
                "terms": "Middleware pipeline, request parsing, routing parameters, CORS handling, next() function.",
                "lab": ["Implement logging middleware printing timestamp data", "Create parametrized routes (e.g. /users/:id)", "Configure JSON request body parsing"],
                "q": "What function must be invoked at the end of a custom Express middleware handler to pass control to the next function in line?",
                "opts": ["A) end()", "B) send()", "C) next()", "D) forward()"],
                "ans": "C",
                "expl": "Invoking the next() callback tells Express to progress to the subsequent handler in the pipeline.",
                "dist": "Failing to call next() will cause the request to hang."
            },
            {
                "topic": "Relational Databases with PostgreSQL",
                "terms": "SQL schema structure, relational tables, PRIMARY KEY, FOREIGN KEY constraints, JOIN queries.",
                "lab": ["Write raw SQL scripts to create tables", "Insert mock data records using INSERT queries", "Perform INNER JOIN queries to return relational records"],
                "q": "Which SQL constraint uniquely identifies each record in a database table?",
                "opts": ["A) FOREIGN KEY", "B) UNIQUE INDEX", "C) PRIMARY KEY", "D) DEFAULT"],
                "ans": "C",
                "expl": "The PRIMARY KEY constraint enforces unique, non-null values for the primary database identifier column.",
                "dist": "FOREIGN KEY links rows to parent tables."
            },
            {
                "topic": "NoSQL Databases with MongoDB",
                "terms": "Document database, collections, BSON, schema design, mongoose model operations.",
                "lab": ["Establish a mongoose server connection profile", "Define user models with schema validation", "Write CRUD queries to write records"],
                "q": "Which data format does MongoDB use natively to store documents in collections?",
                "opts": ["A) XML", "B) CSV", "C) BSON (Binary JSON)", "D) SQL Table Structure"],
                "ans": "C",
                "expl": "MongoDB processes data objects as BSON, an optimized binary representation of JSON files.",
                "dist": "BSON supports more data types (such as dates) than plain JSON."
            },
            {
                "topic": "Frontend Frameworks (React)",
                "terms": "Single Page Application (SPA), React virtual DOM, components, JSX syntax, build pipelines.",
                "lab": ["Setup base react project skeleton", "Convert HTML blocks to JSX component templates", "Inspect virtual DOM structures"],
                "q": "How does React's Virtual DOM improve application rendering performance?",
                "opts": ["A) It updates all page elements on every interaction", "B) It compiles javascript to machine code", "C) It computes changes in memory first and only updates altered elements in the real DOM", "D) It bypasses CSS parsing"],
                "ans": "C",
                "expl": "React compares changes in a virtual DOM tree (reconciliation) and updates only the necessary elements, avoiding expensive global repaints.",
                "dist": "Bypassing calculations or writing machine code is not how React operates."
            },
            {
                "topic": "React State & Props",
                "terms": "Functional components, React hooks, useState, immutable props, event handling.",
                "lab": ["Configure useState hook controls to manage component arrays", "Pass props to nested child elements", "Handle button interactions to update view state"],
                "q": "Which React Hook is used to add local state variables to functional components?",
                "opts": ["A) useEffect", "B) useContext", "C) useState", "D) useStateVariable"],
                "ans": "C",
                "expl": "The useState hook returns a state value and a setter function to trigger re-renders.",
                "dist": "useEffect handles side effects. useContext handles global context."
            },
            {
                "topic": "Web Security (JWT & CORS)",
                "terms": "Cross-Origin Resource Sharing (CORS), JSON Web Tokens (JWT), signing keys, payload structures, bcrypt.",
                "lab": ["Configure CORS origins in Express app", "Hash passwords using bcrypt before saving", "Generate and verify signing JWT payloads"],
                "q": "What are the three parts of a JSON Web Token (JWT)?",
                "opts": ["A) Header, Payload, Signature", "B) ID, Key, Secret", "C) Username, Date, Salt", "D) Origin, Destination, Protocol"],
                "ans": "A",
                "expl": "A JWT is a dot-separated string containing a Header (metadata), a Payload (claims), and a cryptographically verified Signature.",
                "dist": "Only the base structure guarantees validation."
            },
            {
                "topic": "Deployment to AWS",
                "terms": "AWS S3, EC2 hosting, security groups, public ports, PM2 service manager.",
                "lab": ["Deploy static build files to AWS S3 bucket", "Launch a virtual Linux instance on AWS EC2", "Configure inbound security rules for HTTP/SSH ports"],
                "q": "Which AWS compute service provides resizable, raw virtual machines for hosting backend applications?",
                "opts": ["A) Amazon S3", "B) Amazon EC2", "C) AWS Lambda", "D) Amazon RDS"],
                "ans": "B",
                "expl": "EC2 (Elastic Compute Cloud) provides virtual machines (instances) for running backend service code.",
                "dist": "S3 is object storage. Lambda is serverless function execution."
            },
            {
                "topic": "Web Sockets",
                "terms": "Socket.io, TCP duplex streams, polling fallbacks, real-time message streams.",
                "lab": ["Configure Socket.io servers", "Listen to websocket connection event triggers", "Broadcast events to connected clients"],
                "q": "What is the primary benefit of WebSockets over standard HTTP polling?",
                "opts": ["A) WebSockets encrypt data automatically", "B) WebSockets provide full-duplex, persistent connection channels over a single TCP socket", "C) WebSockets do not require ports", "D) WebSockets run faster than compiled C++ code"],
                "ans": "B",
                "expl": "WebSockets allow continuous, bi-directional real-time communication without the overhead of repeating HTTP headers.",
                "dist": "Encryption requires WSS (Secure), and ports are still utilized."
            }
        ]
    },
    "CIS-3350_Software_Engineering_Agile": {
        "cert": "Professional Scrum Master (PSM I)",
        "desc": "SDLC phases, Git workflows, clean code, SOLID patterns, testing, Scrum roles, sprint ceremonies, backlog grooming, and Agile relative sizing.",
        "oer": "Official Scrum Guide (scrumguides.org)",
        "weeks": [
            {
                "topic": "SDLC Models",
                "terms": "Software Development Life Cycle, Waterfall model, Agile model, iterative phases, risk evaluation.",
                "lab": ["Document SDLC model characteristics", "Compare development scenarios for Waterfall vs Agile", "Identify project risks"],
                "q": "Which SDLC model is characterized by linear, sequential phases where each phase must complete before the next begins?",
                "opts": ["A) Scrum", "B) Waterfall", "C) Spiral", "D) Kanban"],
                "ans": "B",
                "expl": "Waterfall is the classic linear-sequential model with distinct, non-overlapping development phases.",
                "dist": "Scrum and Kanban are iterative Agile frameworks. Spiral is risk-driven."
            },
            {
                "topic": "Git Workflows & Branching",
                "terms": "Git branch, merge conflicts, pull requests, Gitflow workflow, rebase vs merge.",
                "lab": ["Initialize local Git repo", "Create feature branches and resolve simulated merge conflicts", "Submit a mock pull request"],
                "q": "In Gitflow workflow, which branch contains production-ready code that is deployed to live systems?",
                "opts": ["A) develop", "B) feature", "C) main (master)", "D) hotfix"],
                "ans": "C",
                "expl": "The main/master branch holds the stable, tested, production-released codebase.",
                "dist": "develop branch aggregates feature branches under active development."
            },
            {
                "topic": "Clean Code & Refactoring",
                "terms": "Code smells, refactoring techniques, DRY (Don't Repeat Yourself), descriptive naming, comment overhead.",
                "lab": ["Review a legacy script containing poor naming and duplicate loops", "Refactor variables and functions to follow clean guidelines", "Test code execution"],
                "q": "What software design principle is violated when you copy and paste identical blocks of code across multiple parts of a program?",
                "opts": ["A) SOLID", "B) DRY (Don't Repeat Yourself)", "C) KISS (Keep It Simple, Stupid)", "D) YAGNI (You Aren't Gonna Need It)"],
                "ans": "B",
                "expl": "DRY demands that every piece of knowledge must have a single, unambiguous representation within a system.",
                "dist": "YAGNI cautions against building unused features ahead of time."
            },
            {
                "topic": "Object-Oriented Design (SOLID)",
                "terms": "SOLID principles, Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.",
                "lab": ["Analyze class layouts violating SOLID rules", "Re-architect classes to conform to Open/Closed and Single Responsibility principles", "Verify class inheritance relations"],
                "q": "Which SOLID principle states that software entities (classes, modules) should be open for extension but closed for modification?",
                "opts": ["A) Single Responsibility Principle", "B) Open/Closed Principle", "C) Liskov Substitution Principle", "D) Interface Segregation Principle"],
                "ans": "B",
                "expl": "The Open/Closed Principle allows extending class behavior (usually via inheritance or polymorphism) without changing the existing class source code.",
                "dist": "Single Responsibility states a class should have only one reason to change."
            },
            {
                "topic": "UML Diagrams",
                "terms": "Unified Modeling Language, Class diagram, Use Case diagram, Sequence diagram, multiplicity relations.",
                "lab": ["Draft a Use Case diagram mapping actor workflows", "Create a Class diagram showing database model attributes and relations", "Draw sequence diagrams"],
                "q": "Which UML diagram is best suited to visualize the logical lifecycle of objects and the exact order of messages passed between them over time?",
                "opts": ["A) Class Diagram", "B) Use Case Diagram", "C) Sequence Diagram", "D) Deployment Diagram"],
                "ans": "C",
                "expl": "Sequence diagrams are behavioral diagrams showing step-by-step object interactions and message sequences ordered chronologically.",
                "dist": "Class diagrams are structural and show static linkages, not timeline-based calls."
            },
            {
                "topic": "Design Patterns (Creational)",
                "terms": "Design pattern classifications, Singleton pattern, Factory Method pattern, object instantiation.",
                "lab": ["Write a thread-safe Singleton class in Python", "Write a Factory pattern dynamically creating database connectors", "Test object instance memory locations"],
                "q": "What is the primary purpose of the Singleton design pattern?",
                "opts": ["A) To abstract subclass creation", "B) To ensure a class has only one instance and provides a global point of access to it", "C) To convert interface structures", "D) To monitor runtime events"],
                "ans": "B",
                "expl": "Singleton restricts class instantiation to a single object, routing all calls through a shared instance reference.",
                "dist": "Factory Method handles subclass creation without specifying exact types."
            },
            {
                "topic": "Design Patterns (Structural & Behavioral)",
                "terms": "Observer pattern, Strategy pattern, decoupled components, state machines.",
                "lab": ["Implement Observer pattern to notify clients on data updates", "Implement Strategy pattern swapping payment calculators", "Verify decoupled state dependencies"],
                "q": "Which behavioral design pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified?",
                "opts": ["A) Adapter Pattern", "B) Decorator Pattern", "C) Observer Pattern", "D) Strategy Pattern"],
                "ans": "C",
                "expl": "The Observer pattern enables decoupling pub-sub mechanisms where subjects notify observers without tight linkages.",
                "dist": "Adapter links mismatched interfaces. Decorator adds behavior dynamically."
            },
            {
                "topic": "Software Testing Levels",
                "terms": "Unit tests, integration tests, system tests, mock inputs, assertion statements.",
                "lab": ["Write pytest unit test cases asserting function returns", "Mock database connection responses", "Measure test coverage indicators"],
                "q": "Which level of testing focuses on validating that individual functions, methods, or classes behave correctly in isolation?",
                "opts": ["A) Unit Testing", "B) Integration Testing", "C) System Testing", "D) Acceptance Testing"],
                "ans": "A",
                "expl": "Unit testing tests smallest testable parts (units) of an application independently from database or network APIs.",
                "dist": "Integration testing verifies interface communication between modules."
            },
            {
                "topic": "Test-Driven Development (TDD)",
                "terms": "TDD lifecycle (Red, Green, Refactor), test suites, assertions, code coverage.",
                "lab": ["Write failing test case based on spec sheet", "Write absolute minimum functional code to make test pass", "Refactor code structure keeping test green"],
                "q": "What is the correct sequence of phases in the Test-Driven Development (TDD) cycle?",
                "opts": ["A) Refactor, Write Code, Verify Test", "B) Write Test (Red), Implement Code (Green), Refactor", "C) Design, Code, Test, Release", "D) Assert, Clean, Deploy"],
                "ans": "B",
                "expl": "TDD operates in a tight loop: write a failing test (Red), implement code just enough to pass (Green), then clean up/refactor structure.",
                "dist": "Writing code before test cases violates the core philosophy of TDD."
            },
            {
                "topic": "CI/CD Foundations",
                "terms": "Continuous Integration, Continuous Deployment, automation runners, pipeline syntax, deployment registries.",
                "lab": ["Create local script running lint checks", "Map build stages in a mock configuration file", "Review pipeline output reports"],
                "q": "What is the primary goal of Continuous Integration (CI)?",
                "opts": ["A) To manually deploy builds to production servers", "B) To automatically build, lint, and run tests on code changes whenever developer merges to shared branches", "C) To write project charters", "D) To backup database files"],
                "ans": "B",
                "expl": "CI automatically verifies new changes pushed to repositories using automation pipelines, detecting compilation and test failures early.",
                "dist": "Continuous Delivery/Deployment (CD) handles the automation of software releases to targets."
            },
            {
                "topic": "Scrum Framework Roles",
                "terms": "Scrum Guide, Scrum Team, Product Owner, Scrum Master, Developers, self-managing teams.",
                "lab": ["Assign project tasks matching Scrum roles", "Map Scrum team interaction guidelines", "Document scope ownership profiles"],
                "q": "Who on the Scrum Team is accountable for maximizing the value of the product and managing the Product Backlog?",
                "opts": ["A) Scrum Master", "B) Developers", "C) Product Owner", "D) Project Manager"],
                "ans": "C",
                "expl": "The Product Owner represents client stakeholders and maintains the prioritization of product backlog items.",
                "dist": "Scrum Master manages process adherence. Developers implement features."
            },
            {
                "topic": "Scrum Events",
                "terms": "Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, timeboxing rules.",
                "lab": ["Simulate Scrum event time allocations", "Draft a Sprint Retrospective improvements matrix", "Outline daily standup updates"],
                "q": "What is the maximum timebox duration for the Daily Scrum event?",
                "opts": ["A) 5 minutes", "B) 15 minutes", "C) 30 minutes", "D) 1 hour"],
                "ans": "B",
                "expl": "The Daily Scrum is strictly timeboxed to 15 minutes to keep alignment meetings focused and brief.",
                "dist": "Other durations are too long for daily alignment."
            },
            {
                "topic": "Backlog Refinement & Estimation",
                "terms": "Product backlog items, user stories, Planning Poker, story points, Fibonacci sequence.",
                "lab": ["Draft user stories in standard format", "Use Planning Poker to assign story points to tasks", "Determine team velocity limits"],
                "q": "Why does Scrum use relative estimation metrics like Story Points instead of hours to estimate task sizes?",
                "opts": ["A) Hours are too complex to sum", "B) Story points account for complexity, effort, and risk in a way that is consistent across different developer skill levels", "C) Clients demand story points", "D) Story points allow skipping QA"],
                "ans": "B",
                "expl": "Relative sizing (using Fibonacci scales) enables developers to estimate scope size and complexity without micro-managing hourly commitments.",
                "dist": "Hours do not reflect variable experience or unexpected integration risks."
            },
            {
                "topic": "Software Security & Coding Standards",
                "terms": "Secure coding guidelines, OWASP standards, input validation, output encoding, cryptography principles.",
                "lab": ["Review code templates for security issues", "Apply sanitization rules to clean inputs", "Test application behaviors"],
                "q": "Which security practice is most critical to prevent buffer overflows or injection vulnerability issues?",
                "opts": ["A) Writing verbose comments", "B) Input validation and sanitization", "C) Reducing compiler speed", "D) Disabling firewalls"],
                "ans": "B",
                "expl": "Validating input parameters against type and length boundaries stops malicious payloads from executing.",
                "dist": "Comments or compiler configurations do not alter security execution characteristics."
            },
            {
                "topic": "DevOps Principles",
                "terms": "DevOps lifecycle, infrastructure automation, container orchestration, telemetry metrics.",
                "lab": ["Analyze infrastructure requirements for web apps", "Map DevOps lifecycle loops", "Identify delivery constraints"],
                "q": "Which core principle emphasizes breaking down silos between software creators and operational system administrators?",
                "opts": ["A) Waterfall", "B) Systems Analysis", "C) DevOps", "D) Strict Isolation"],
                "ans": "C",
                "expl": "DevOps integrates development workflows with systems operations, aligning development speed with server stability.",
                "dist": "Waterfall and isolation reinforce team silos rather than resolving them."
            }
        ]
    },
    "CIS-4345_Machine_Learning_Deep_Learning": {
        "cert": "TensorFlow Developer Certificate",
        "desc": "ML pipelines, regression models, classification performance, SVM, random forests, dimensionality reduction, neural networks, CNNs, LSTMs, and model serving.",
        "oer": "Scikit-Learn & TensorFlow Documentation (scikit-learn.org / tensorflow.org)",
        "weeks": [
            {
                "topic": "Introduction to ML Pipelines",
                "terms": "Machine learning lifecycle, data collection, feature extraction, train-test split, label definitions.",
                "lab": ["Setup ML project directory", "Verify scikit-learn installations", "Split a sample database matrix into training and testing partitions"],
                "q": "What is the primary reason for splitting data into Training and Testing datasets?",
                "opts": ["A) To save disk storage space", "B) To evaluate how the model performs on unseen data and detect overfitting", "C) To double compile datasets", "D) To format files for database engines"],
                "ans": "B",
                "expl": "Testing datasets provide unbiased metrics indicating how well models generalize to new inputs.",
                "dist": "It does not optimize space or compile script files."
            },
            {
                "topic": "Linear Regression",
                "terms": "Continuous output variables, cost function (MSE), gradient descent steps, weights and biases.",
                "lab": ["Train linear regression model", "Fit features: model.fit(X, y)", "Print intercept and slope values"],
                "q": "What is the objective of the Gradient Descent algorithm in model training?",
                "opts": ["A) To select random features", "B) To iteratively adjust model weights to minimize the cost function value", "C) To prune decision tree leaves", "D) To backup SQL tables"],
                "ans": "B",
                "expl": "Gradient Descent is an optimization method that computes cost gradients to update weights toward minimum cost levels.",
                "dist": "Pruning trees and database administration are independent tasks."
            },
            {
                "topic": "Logistic Regression",
                "terms": "Binary classification, sigmoid activation, probability mapping, threshold values.",
                "lab": ["Train logistic regression model", "Predict binary class output labels", "Analyze probability arrays using predict_proba()"],
                "q": "Which mathematical function maps real number inputs to a probability value between 0 and 1 in logistic regression?",
                "opts": ["A) Linear function", "B) Sigmoid (Logistic) function", "C) Step function", "D) Relu function"],
                "ans": "B",
                "expl": "The sigmoid function (1 / (1 + e^-x)) outputs values bounded between 0 and 1, representing probabilities.",
                "dist": "Linear function can return infinite outputs. ReLU is max(0, x)."
            },
            {
                "topic": "Regularization Techniques",
                "terms": "Overfitting indicators, high variance, L1 regularization (Lasso), L2 regularization (Ridge), alpha penalty.",
                "lab": ["Import Ridge and Lasso classes", "Train models with varying alpha levels", "Observe feature weights dropping toward zero"],
                "q": "How does L1 regularization (Lasso) differ from L2 regularization (Ridge)?",
                "opts": ["A) L1 adds squared penalties, L2 adds absolute penalties", "B) L1 can force feature weights exactly to zero, performing feature selection", "C) L2 is only used in unsupervised learning", "D) L1 increases model training time by 10x"],
                "ans": "B",
                "expl": "Lasso adds an absolute weight penalty to the cost, leading to sparse coefficients (forces unimportant features to 0).",
                "dist": "Ridge uses squared penalties (L2) and shrinks weights close to but not exactly to 0."
            },
            {
                "topic": "Support Vector Machines",
                "terms": "Hyperplane separation, support vectors, margin maximization, kernel trick, soft margins.",
                "lab": ["Train Support Vector Classifier", "Map linear vs radial basis function (RBF) kernels", "Plot decision boundaries"],
                "q": "What are support vectors in the context of Support Vector Machines?",
                "opts": ["A) Empty dimensions", "B) The data points closest to the separating hyperplane that define the margin boundaries", "C) The outputs of activation layers", "D) Target variable index arrays"],
                "ans": "B",
                "expl": "Support vectors are the data points closest to the separating hyperplane that define the margin boundaries.",
                "dist": "Support vectors are real points, not dimensions or activations."
            },
            {
                "topic": "Decision Trees & Random Forests",
                "terms": "Entropy index, Gini impurity, node splitting, ensemble methods, bagging, bootstrap samples.",
                "lab": ["Train a decision tree on classifier data", "Train a Random Forest classifier", "Compare test accuracy metrics"],
                "q": "Which process describes the 'Bagging' ensemble technique used in Random Forests?",
                "opts": ["A) Sequential tree boosting", "B) Training multiple independent decision trees on bootstrap datasets and averaging their votes", "C) Regularizing feature weight matrices", "D) Compressing tree layers into a single node"],
                "ans": "B",
                "expl": "Bootstrap Aggregation (Bagging) reduces variance by training multiple trees on random sub-samples and combining predictions.",
                "dist": "Sequential tree training is characteristic of Boosting."
            },
            {
                "topic": "K-Means & Hierarchical Clustering",
                "terms": "Unsupervised learning, centroids, inertia, elbow method, dendrogram structures.",
                "lab": ["Train K-Means clustering algorithm", "Plot elbow curve using inertia metrics", "Classify unlabeled customer profiles"],
                "q": "How do you determine the optimal number of clusters (K) in K-Means clustering using the Elbow Method?",
                "opts": ["A) Look for the point where the cost curve changes from steep to shallow (inertia drops level off)", "B) Find the highest classification score", "C) Check the number of columns", "D) Count the total row count"],
                "ans": "A",
                "expl": "The 'elbow' represents a point of diminishing returns where adding more clusters yields minimal reduction in inertia.",
                "dist": "Classification scores are unavailable since K-Means is unsupervised."
            },
            {
                "topic": "Dimensionality Reduction (PCA)",
                "terms": "Curse of dimensionality, principal components, covariance matrix, explained variance ratio.",
                "lab": ["Import PCA class", "Reduce high-dimension dataset to 2 components", "Verify explained variance outcomes"],
                "q": "What is the main purpose of Principal Component Analysis (PCA)?",
                "opts": ["A) To predict label outputs", "B) To project high-dimensional data onto lower-dimensional spaces while preserving maximum variance", "C) To cluster similar users", "D) To balance binary classes"],
                "ans": "B",
                "expl": "PCA simplifies data structures by identifying orthogonal principal components that capture the most information.",
                "dist": "PCA is a linear transformer, not a predictor or clustering engine."
            },
            {
                "topic": "Introduction to Neural Networks",
                "terms": "Deep learning models, artificial neuron structure, inputs, weights, bias, hidden layers, output activations.",
                "lab": ["Build a simple neuron representation using numpy dot products", "Trace forward propagation variables", "Inspect weight matrices"],
                "q": "What is the primary function of a hidden layer in an artificial neural network?",
                "opts": ["A) To store inputs exactly", "B) To learn non-linear feature representations from input data patterns", "C) To write files to disk", "D) To communicate directly with user interfaces"],
                "ans": "B",
                "expl": "Hidden layers apply weights and activation functions to extract high-level feature mappings from preceding inputs.",
                "dist": "Hidden layers are intermediate computation steps, isolated from raw files and client frontends."
            },
            {
                "topic": "Activation & Backpropagation",
                "terms": "Activation functions (ReLU, Sigmoid, Softmax), forward pass, loss calculations, backpropagation, chain rule.",
                "lab": ["Calculate derivative outputs of Sigmoid and ReLU functions", "Implement simple backprop weight adjust updates", "Test learning convergence"],
                "q": "Which mathematical derivative rule is utilized to compute gradients of nested layers during the backpropagation step?",
                "opts": ["A) Product Rule", "B) Quotient Rule", "C) Chain Rule", "D) Addition Rule"],
                "ans": "C",
                "expl": "Backpropagation computes error gradients starting at the output layer and propagating backward using the Chain Rule.",
                "dist": "The chain rule handles derivatives of composed functions."
            },
            {
                "topic": "Convolutional Neural Networks",
                "terms": "Image array structures, convolution filters, stride settings, pooling layers (max pooling), flatten step.",
                "lab": ["Define a CNN layout using TensorFlow Keras Sequential API", "Add Conv2D and MaxPooling2D layers", "Print model summary layouts"],
                "q": "Why are Convolutional layers superior to Fully Connected layers for image processing tasks?",
                "opts": ["A) They require larger database spaces", "B) They preserve spatial relationships and reduce parameters through weight sharing", "C) They do not require activation functions", "D) They compile directly to C++ binaries"],
                "ans": "B",
                "expl": "CNN filters scan local pixel neighborhoods, capturing spatial patterns (edges, shapes) regardless of position in the image.",
                "dist": "Fully connected layers flatten images, destroying spatial layout and causing parameters to explode."
            },
            {
                "topic": "Recurrent Neural Networks (RNN/LSTM)",
                "terms": "Sequence databases, recurrent loops, hidden states, vanishing gradients, Long Short-Term Memory (LSTM) cells.",
                "lab": ["Define a simple LSTM model layout in Keras", "Format text or time-series data array dimensions", "Train model and print outcomes"],
                "q": "What problem do Long Short-Term Memory (LSTM) cells solve compared to basic Recurrent Neural Networks (RNNs)?",
                "opts": ["A) Memory leak errors", "B) The vanishing gradient problem, allowing the model to learn long-term dependencies", "C) The lack of GPU drivers", "D) High compilation speeds"],
                "ans": "B",
                "expl": "LSTMs use internal gating mechanisms (forget gate, input gate, output gate) to maintain state values across many sequence steps.",
                "dist": "LSTMs do not change computer hardware drivers or execution speeds."
            },
            {
                "topic": "Natural Language Processing",
                "terms": "Text processing pipelines, token vectors, vocabulary lookup, word embeddings (Word2Vec), cosine similarity.",
                "lab": ["Tokenize text paragraphs into indices", "Build word vector representations", "Compute cosine similarity values between vectors"],
                "q": "What is a word embedding in Natural Language Processing (NLP)?",
                "opts": ["A) A dictionary lookup string", "B) A dense vector representation where words with similar semantic meanings are mapped close together", "C) A file compression method", "D) A type of database primary key"],
                "ans": "B",
                "expl": "Word embeddings project words into high-dimensional geometric spaces, encoding semantic relationships.",
                "dist": "It is not a static dictionary lookup or a database key."
            },
            {
                "topic": "Model Optimization & Tuning",
                "terms": "Learning rate adjustments, optimizer configurations (Adam, SGD), dropout layers, batch size settings.",
                "lab": ["Train a neural network with varying learning rates", "Add Dropout layers to reduce overfitting", "Plot loss convergence charts"],
                "q": "How does the Dropout technique prevent overfitting in deep neural networks?",
                "opts": ["A) It drops input rows", "B) It randomly deactivates a fraction of neurons during each training step, forcing redundancy", "C) It deletes model files", "D) It turns off the CPU"],
                "ans": "B",
                "expl": "Dropout stops co-adaptation by ensuring no single neuron can dominate feature representation.",
                "dist": "It is applied during training steps, not row deletion."
            },
            {
                "topic": "Model Deployment & Serving",
                "terms": "Model serialization (Keras H5, TensorFlow SavedModel), REST API frameworks, hosting options.",
                "lab": ["Save a trained TensorFlow model file", "Build a Flask/FastAPI backend to load model and serve predictions", "Test endpoint with curl payloads"],
                "q": "What format is typically used to exchange model prediction input payloads over HTTP APIs?",
                "opts": ["A) XML", "B) JSON", "C) CSV", "D) SQL Data"],
                "ans": "B",
                "expl": "REST APIs typically use JSON format to structure features and return class labels or scores.",
                "dist": "JSON is the standard format for modern HTTP REST requests."
            }
        ]
    },
    "CIS-3310_IT_Project_Management": {
        "cert": "CompTIA Project+ / PMI CAPM",
        "desc": "Project charters, WBS packages, Gantt chart scheduling, critical path slack times, cost baseline estimates, RACI maps, risk registers, and change controls.",
        "oer": "PMI Project Management Body of Knowledge (PMBOK Guide)",
        "weeks": [
            {
                "topic": "IT Project Framework",
                "terms": "Project vs operations, triple constraint (Scope, Time, Cost), project lifecycle phases.",
                "lab": ["Draft a project charter template", "Identify project constraints for an IT upgrade", "Define lifecycle steps"],
                "q": "What are the three pillars of the Project Management Triple Constraint?",
                "opts": ["A) Scope, Time, Cost", "B) Quality, Speed, Safety", "C) Staff, Hardware, Software", "D) Planning, Execution, Closure"],
                "ans": "A",
                "expl": "Any change to scope, schedule (time), or budget (cost) impacts the other variables and overall quality.",
                "dist": "Staff and planning are resources and phases, not core constraints."
            },
            {
                "topic": "Project Charter Development",
                "terms": "Project charter purpose, business case, project objectives, stakeholder registers.",
                "lab": ["Write a project charter for a server migration project", "Identify project sponsors and key stakeholders", "Document business benefits"],
                "q": "Which document authorizes the formal existence of a project and gives the project manager authority to apply resources?",
                "opts": ["A) Project Scope Statement", "B) Project Charter", "C) Work Breakdown Structure", "D) Statement of Work (SOW)"],
                "ans": "B",
                "expl": "The Project Charter is signed by sponsors to initiate the project and authorize resources.",
                "dist": "Scope statement defines deliverables. WBS is a decomposition tree."
            },
            {
                "topic": "Defining Scope & WBS",
                "terms": "Work Breakdown Structure (WBS), decomposition, work packages, scope creep, WBS dictionary.",
                "lab": ["Decompose a software project into WBS levels", "Create a WBS hierarchy diagram", "Write definitions for work packages"],
                "q": "What is the lowest level of decomposition in a Work Breakdown Structure (WBS) called?",
                "opts": ["A) Sub-project", "B) Task group", "C) Work Package", "D) Milestone"],
                "ans": "C",
                "expl": "Work packages are the granular units at the bottom of the WBS tree, where costs and schedules can be estimated.",
                "dist": "Milestones are points in time with zero duration."
            },
            {
                "topic": "Project Schedule & Gantt Charts",
                "terms": "Activity sequencing, dependency types (Finish-to-Start), Gantt chart configurations, lead and lag times.",
                "lab": ["Create an activity list with estimated durations", "Draw a Gantt chart mapping task timelines", "Add FS dependencies"],
                "q": "Which dependency type describes a scenario where Task B cannot start until Task A has completed?",
                "opts": ["A) Start-to-Start (SS)", "B) Finish-to-Start (FS)", "C) Finish-to-Finish (FF)", "D) Start-to-Finish (SF)"],
                "ans": "B",
                "expl": "Finish-to-Start is the most common scheduling linkage; preceding activity must end before successor begins.",
                "dist": "Start-to-Start requires both tasks to begin concurrently."
            },
            {
                "topic": "Critical Path Method",
                "terms": "Network diagram, forward pass (early start/finish), backward pass (late start/finish), float/slack time.",
                "lab": ["Calculate ES/EF and LS/LF for a network diagram", "Identify critical path with zero float time", "Compute project duration"],
                "q": "What is the definition of the Critical Path in project scheduling?",
                "opts": ["A) The path containing the most complex tasks", "B) The longest path of dependent activities that determines the shortest possible project duration", "C) The path with the highest cost", "D) The sequence of non-dependent milestones"],
                "ans": "B",
                "expl": "The critical path has zero slack (float) time. Any delay to critical path tasks directly delays the project completion date.",
                "dist": "It is determined by sequence duration, not complexity or cost."
            },
            {
                "topic": "Cost Estimation & Budgeting",
                "terms": "Analogous vs parametric estimating, bottom-up estimation, contingency reserves, cost baseline.",
                "lab": ["Calculate project costs using parametric estimating models", "Create a bottom-up budget database", "Determine reserve levels"],
                "q": "Which cost estimation technique uses historical data from similar projects as the basis for the current estimate?",
                "opts": ["A) Parametric Estimating", "B) Analogous (Top-down) Estimating", "C) Bottom-up Estimating", "D) Three-point Estimating"],
                "ans": "B",
                "expl": "Analogous estimating compares the current scope to past projects, providing quick but less precise estimates.",
                "dist": "Parametric estimating uses statistical modeling (e.g. cost per square foot)."
            },
            {
                "topic": "Quality Management & Metrics",
                "terms": "Quality planning, quality assurance vs quality control, metrics, Pareto charts, check sheets.",
                "lab": ["Draft a quality management plan for software testing", "Analyze defect logs using a Pareto diagram", "Verify quality check metrics"],
                "q": "What is the main focus of Quality Assurance (QA) compared to Quality Control (QC)?",
                "opts": ["A) QA focuses on preventing defects in processes, while QC focuses on identifying defects in final products", "B) QA runs unit tests", "C) QC manages project budgets", "D) QA is done only by project managers"],
                "ans": "A",
                "expl": "QA is process-oriented (proactive prevention). QC is product-oriented (reactive inspection of deliverables).",
                "dist": "Both teams write tests, but their scope targets process vs product."
            },
            {
                "topic": "Resource Allocation",
                "terms": "Resource loading, resource leveling, RACI matrix (Responsible, Accountable, Consulted, Informed), resource conflicts.",
                "lab": ["Create a RACI matrix for project team members", "Resolve resource overallocation conflicts", "Verify assignment grids"],
                "q": "What does the 'A' stand for in a RACI assignment matrix?",
                "opts": ["A) Assigned", "B) Accountable", "C) Authorized", "D) Approved"],
                "ans": "B",
                "expl": "Accountable represents the single person answerable for the correct completion of the task (only one 'A' per task).",
                "dist": "Responsible executes the work. Accountable owns the outcome."
            },
            {
                "topic": "Communication & Stakeholder Management",
                "terms": "Communication channels formula (N*(N-1)/2), communication plan parameters, stakeholder registers.",
                "lab": ["Calculate communication channels for team scaling", "Draft a communication matrix specifying email/meeting schedules", "Identify stakeholder impacts"],
                "q": "How many communication channels exist in a project team containing 8 members?",
                "opts": ["A) 8", "B) 16", "C) 28", "D) 56"],
                "ans": "C",
                "expl": "Using the channel formula: 8 * (8 - 1) / 2 = 8 * 7 / 2 = 56 / 2 = 28 channels.",
                "dist": "The formula tracks unique connections between all members."
            },
            {
                "topic": "Risk Identification & Management",
                "terms": "Risk register, qualitative risk analysis (probability vs impact), risk response strategies (avoid, transfer, mitigate, accept).",
                "lab": ["Build a risk register table detailing threats", "Calculate risk score rankings (probability * impact)", "Draft risk mitigation workflows"],
                "q": "Which risk response strategy involves buying an insurance policy or outsourcing a database migration task to a vendor?",
                "opts": ["A) Avoid", "B) Transfer", "C) Mitigate", "D) Accept"],
                "ans": "B",
                "expl": "Transferring shifts the financial ownership or operational threat to a third party (e.g. hosting provider or insurer).",
                "dist": "Mitigation reduces probability or impact directly."
            },
            {
                "topic": "IT Procurement & Contracts",
                "terms": "Request for Proposal (RFP), contract types (Fixed Price, Time & Materials, Cost Reimbursable), SLA terms.",
                "lab": ["Review a vendor service level agreement (SLA)", "Compare contract scenarios for procurement pricing", "Draft contract parameters"],
                "q": "Which contract type carries the highest risk for the buyer but low risk for the seller?",
                "opts": ["A) Firm-Fixed-Price (FFP)", "B) Cost-Reimbursable (CR)", "C) Time and Materials (T&M)", "D) Fixed-Price-Incentive-Fee (FPIF)"],
                "ans": "B",
                "expl": "In cost-reimbursable contracts, the buyer pays all actual costs plus a fee, meaning cost overruns are paid by the buyer.",
                "dist": "Fixed-price shifts cost overrun risk onto the seller."
            },
            {
                "topic": "Agile Project Management Overview",
                "terms": "Agile methodologies, sprint cycles, Kanban boards, velocity metrics, adaptive planning.",
                "lab": ["Map Agile sprint cycles for a mobile app project", "Track task progress on a physical/digital Kanban board", "Verify project backlog items"],
                "q": "How does scope changes management differ in Agile compared to traditional Waterfall project management?",
                "opts": ["A) Agile permits changes at any time by prioritizing the backlog, while Waterfall uses strict change control boards", "B) Agile does not allow any changes", "C) Waterfall updates code dynamically", "D) Agile requires more documentation"],
                "ans": "A",
                "expl": "Agile welcomes change by re-evaluating the prioritizations of user stories before every sprint.",
                "dist": "Waterfall freezes scope early, requiring formal change management approval for revisions."
            },
            {
                "topic": "Project Execution & Performance Reporting",
                "terms": "Earned Value Management (EVM), Planned Value (PV), Actual Cost (AC), Earned Value (EV), CV, SV, CPI, SPI.",
                "lab": ["Calculate cost variance (CV) and schedule variance (SV)", "Determine project budget health using CPI and SPI indexes", "Analyze performance charts"],
                "q": "A project has a Cost Performance Index (CPI) of 0.85 and a Schedule Performance Index (SPI) of 1.10. What is the status?",
                "opts": ["A) Under budget and ahead of schedule", "B) Over budget and behind schedule", "C) Over budget and ahead of schedule", "D) Under budget and behind schedule"],
                "ans": "C",
                "expl": "CPI < 1 indicates the project is spending more than planned (over budget). SPI > 1 indicates tasks are ending ahead of schedule.",
                "dist": "Value 1.0 is right on targets; values below 1 are negative/late."
            },
            {
                "topic": "Project Change Control",
                "terms": "Change request forms, Change Control Board (CCB), configuration management, impact assessment.",
                "lab": ["Draft a change request form template", "Analyze scope impacts of a requested software revision", "Document CCB approval pathways"],
                "q": "What is the primary role of a Change Control Board (CCB) in project management?",
                "opts": ["A) To write programming code", "B) To review, evaluate, and approve or reject requested project scope modifications", "C) To buy software licenses", "D) To hire developers"],
                "ans": "B",
                "expl": "The CCB is a formal group of stakeholders that verifies changes before they are integrated into baselines.",
                "dist": "CCB handles scope governance, not raw development."
            },
            {
                "topic": "Project Closure & Post-Mortem",
                "terms": "Administrative closure, project handoff, contract closeout, lessons learned, post-mortem reports.",
                "lab": ["Draft a lessons learned survey questionnaire", "Complete a final project acceptance sign-off document", "Write post-mortem report outlines"],
                "q": "What is the primary purpose of conducting a Lessons Learned session during project closure?",
                "opts": ["A) To assign blame for failures", "B) To identify successes and failures to improve future organizational projects", "C) To calculate final employee bonuses", "D) To archive server hardware logs"],
                "ans": "B",
                "expl": "Lessons learned capture historical insights to ensure subsequent projects avoid similar pitfalls.",
                "dist": "Lessons learned focus on process optimization, not assigning blame."
            }
        ]
    },
    "CIS-3312_Systems_Analysis_Design": {
        "cert": "IIBA Entry Certificate in Business Analysis (ECBA)",
        "desc": "System analyst functions, feasibility tests, requirements elicitation, use case modeling, process flow mapping (DFDs), normalization, UAT, and installation cutovers.",
        "oer": "IIBA Business Analysis Body of Knowledge (BABOK Guide)",
        "weeks": [
            {
                "topic": "Role of System Analyst & SDLC",
                "terms": "System analyst responsibilities, business analysis definition, SDLC stages, systems planning.",
                "lab": ["Map business analyst workflows", "Evaluate a business case scenario", "Define system boundaries"],
                "q": "What is the primary responsibility of a Systems Analyst?",
                "opts": ["A) Writing compiled server assembly code", "B) Analyzing business requirements and designing information systems solutions to bridge business and IT", "C) Selling software licenses", "D) Configuring firewall ports"],
                "ans": "B",
                "expl": "Analysts serve as the interface, translating business needs into detailed technical specifications for programmers.",
                "dist": "They focus on analysis and design, not raw code creation or network security configurations."
            },
            {
                "topic": "Feasibility Analysis",
                "terms": "Technical feasibility, economic feasibility (ROI, NPV, Payback period), operational feasibility.",
                "lab": ["Compute Return on Investment (ROI) and Payback Period", "Calculate Net Present Value (NPV) for IT proposal", "Draft feasibility matrix reports"],
                "q": "Which feasibility aspect determines if the organization has the programming and infrastructure capability to build the proposed system?",
                "opts": ["A) Economic Feasibility", "B) Operational Feasibility", "C) Technical Feasibility", "D) Schedule Feasibility"],
                "ans": "C",
                "expl": "Technical feasibility evaluates hardware, software, and development team capability limitations.",
                "dist": "Economic feasibility focuses on project costs and financial payback metrics."
            },
            {
                "topic": "Requirement Gathering",
                "terms": "Functional vs non-functional requirements, interview strategies, questionnaires, JAD sessions, prototyping.",
                "lab": ["Draft a requirements definition template", "Differentiate system requirement lists into functional/non-functional", "Design a questionnaire survey form"],
                "q": "Which item represents a non-functional system requirement?",
                "opts": ["A) The system must send an email receipt on checkout", "B) The user must login using their email address", "C) The database query must return results within 2 seconds", "D) The system must export reports in PDF"],
                "ans": "C",
                "expl": "Non-functional requirements specify operational qualities (performance, security, usability) rather than specific feature tasks.",
                "dist": "Sending emails and logging in represent specific functional operations."
            },
            {
                "topic": "Use Case Analysis",
                "terms": "Actors, use case scenarios, preconditions, postconditions, extend vs include relationships.",
                "lab": ["Write a detailed use case description for 'Checkout Basket'", "Trace normal and exception flows of events", "Identify actor scopes"],
                "q": "In a Use Case diagram, which relationship is used when a use case requires the mandatory execution of another use case?",
                "opts": ["A) <<extend>>", "B) <<include>>", "C) <<generalize>>", "D) <<dependency>>"],
                "ans": "B",
                "expl": "The <<include>> relationship indicates that the base use case incorporates the behavior of the target use case as a mandatory step.",
                "dist": "<<extend>> marks optional behaviors triggered only under specific conditions."
            },
            {
                "topic": "Process Modeling (DFD)",
                "terms": "Data Flow Diagrams (DFD), Gane & Sarson notation, processes, data flows, data stores, external entities, context diagram.",
                "lab": ["Draw a Context Diagram (Level 0 DFD) showing external system links", "Decompose Context to Level-1 DFD showing processes", "Verify data balance rules"],
                "q": "Which element in a Data Flow Diagram represents a person, organization, or external system that sends or receives data but is outside the boundary of the system?",
                "opts": ["A) Process", "B) Data Store", "C) External Entity (Terminator)", "D) Data Flow Link"],
                "ans": "C",
                "expl": "External entities act as sources or destinations of information crossing system boundaries.",
                "dist": "Data stores represent persistent tables or files inside the system."
            },
            {
                "topic": "Data Modeling (ERD)",
                "terms": "Entity Relationship Diagrams (ERD), entities, attributes, relationships, cardinality (1:1, 1:N, M:N), Crow's Foot notation.",
                "lab": ["Identify entities and attributes in a customer ordering scenario", "Draw an ERD using Crow's Foot notation mapping relationships", "Resolve M:N relationships"],
                "q": "How must a many-to-many (M:N) relationship between two database entities be resolved in relational database design?",
                "opts": ["A) Using a direct foreign key link", "B) Creating an associative (junction) entity that links both tables using 1:N relationships", "C) Combining both tables", "D) Deleting one of the entities"],
                "ans": "B",
                "expl": "Relational engines do not support direct M:N tables; an associative entity maps many-to-many links through two one-to-many relations.",
                "dist": "Direct keys only map 1:1 or 1:N linkages."
            },
            {
                "topic": "Object-Oriented Analysis UML",
                "terms": "Unified Modeling Language, Object-oriented analysis, class models, associations, encapsulation.",
                "lab": ["Map relational ERD models to UML class structures", "Define class attributes and operations", "Trace instantiation flows"],
                "q": "Which UML concept involves grouping data fields and the operations that modify them into a single class container to restrict direct access?",
                "opts": ["A) Inheritance", "B) Encapsulation", "C) Polymorphism", "D) Abstraction"],
                "ans": "B",
                "expl": "Encapsulation protects object state by hiding internal data and requiring updates through public methods.",
                "dist": "Polymorphism handles interface execution variance. Inheritance defines subclass lines."
            },
            {
                "topic": "System Architecture & Design",
                "terms": "Architecture design, client-server models, cloud vs local hosting, network layouts.",
                "lab": ["Map client-server architecture layouts", "Compare latency impacts of database placements", "Review system node diagrams"],
                "q": "Which architecture model distributes application logic across client devices and central database nodes?",
                "opts": ["A) Mainframe architecture", "B) Client-Server architecture", "C) Peer-to-Peer architecture", "D) Monolithic architecture"],
                "ans": "B",
                "expl": "Client-server structures split processing between client applications (web/mobile frontends) and backend database/application services.",
                "dist": "Mainframes process all calculations centrally."
            },
            {
                "topic": "User Interface Design",
                "terms": "User Interface (UI) design principles, navigation design, layout grids, wireframes, user experience (UX) feedback.",
                "lab": ["Sketch wireframe interfaces for client portal screens", "Map page navigation routes", "Design entry validation rules"],
                "q": "What is the primary objective of User Interface design?",
                "opts": ["A) To write sql queries", "B) To make interactions user-friendly, efficient, and intuitive for final users", "C) To minimize CPU load", "D) To compile web server configurations"],
                "ans": "B",
                "expl": "UI/UX design is concerned with usability, accessibility, and facilitating user tasks efficiently.",
                "dist": "It targets human interaction interfaces rather than backend logic compilation."
            },
            {
                "topic": "Database Design & Normalization",
                "terms": "Normalization steps, First Normal Form (1NF), Second Normal Form (2NF), Third Normal Form (3NF), transitive dependencies.",
                "lab": ["Normalize a raw flat spreadsheet file into 1NF, 2NF, and 3NF relational tables", "Define keys and indexes", "Verify database integrity constraints"],
                "q": "What is the primary requirement for a database table to conform to Third Normal Form (3NF)?",
                "opts": ["A) It must be in 2NF and contain no transitive dependencies (no non-key column depends on another non-key column)", "B) It must contain no null values", "C) It must use integer primary keys", "D) It must contain multiple tables"],
                "ans": "A",
                "expl": "3NF removes dependencies between non-primary key columns, eliminating redundant data modification anomalies.",
                "dist": "Null values are allowed in 3NF under appropriate designs."
            },
            {
                "topic": "Input and Output Design",
                "terms": "Data entry validation rules (range check, presence check), report layout structures, output formats.",
                "lab": ["Design data entry form validation logic templates", "Format transaction report outputs", "Audit input fields for errors"],
                "q": "Which form validation rule verifies that a value has actually been entered and is not left blank?",
                "opts": ["A) Range Check", "B) Presence (Completeness) Check", "C) Format Check", "D) Consistency Check"],
                "ans": "B",
                "expl": "Presence checks verify that required fields contain data before submissions are processed.",
                "dist": "Range checks verify if numbers fall inside specific boundaries."
            },
            {
                "topic": "Program Design",
                "terms": "Structure charts, pseudo-code, modular design, coupling vs cohesion.",
                "lab": ["Draft pseudo-code specifications for core functions", "Create structure charts showing parameters passed", "Review module coupling variables"],
                "q": "What software architecture relationship is preferred in modular system design?",
                "opts": ["A) High Coupling and High Cohesion", "B) Low Coupling and Low Cohesion", "C) Low Coupling and High Cohesion", "D) High Coupling and Low Cohesion"],
                "ans": "C",
                "expl": "Modular design aims for high cohesion (modules perform single tasks) and low coupling (modules are independent).",
                "dist": "High coupling creates tight dependencies, making system changes difficult."
            },
            {
                "topic": "System Integration & Testing",
                "terms": "Integration test models, alpha testing, beta testing, user acceptance testing (UAT).",
                "lab": ["Draft a UAT test script template", "Determine defect report parameters", "Verify system test logs"],
                "q": "Which testing type is conducted by actual business users in their operational environment to verify the system meets business objectives?",
                "opts": ["A) Unit Testing", "B) Alpha Testing", "C) User Acceptance Testing (UAT)", "D) Regression Testing"],
                "ans": "C",
                "expl": "UAT validates operational readiness and is the final step before the system is signed off for production release.",
                "dist": "Alpha testing is internal testing by the development team."
            },
            {
                "topic": "System Installation & Conversion",
                "terms": "Conversion strategies: Direct cutover, Parallel conversion, Phased conversion, Pilot conversion.",
                "lab": ["Evaluate migration risk scenarios", "Draft a system conversion plan comparing Direct vs Parallel options", "Schedule data cutover times"],
                "q": "Which conversion strategy is the lowest risk because both the old and new systems are run simultaneously for a period of time?",
                "opts": ["A) Direct Cutover", "B) Parallel Conversion", "C) Phased Conversion", "D) Pilot Conversion"],
                "ans": "B",
                "expl": "Parallel conversion allows verification of new outputs against the old system, fallback is immediate if failures occur.",
                "dist": "Direct cutover drops the old system immediately, presenting high risk."
            },
            {
                "topic": "Post-Implementation & Support",
                "terms": "Maintenance categories (corrective, adaptive, perfective, preventive), help desk setups, change management audits.",
                "lab": ["Classify maintenance requests into categories", "Draft system review templates", "Verify log updates"],
                "q": "Which type of software maintenance involves modifying a working system to support new operating system updates or server migrations?",
                "opts": ["A) Corrective Maintenance", "B) Adaptive Maintenance", "C) Perfective Maintenance", "D) Preventive Maintenance"],
                "ans": "B",
                "expl": "Adaptive maintenance alters software to operate in changed hardware or software environments.",
                "dist": "Corrective maintenance fixes bugs. Perfective adds user-requested features."
            }
        ]
    },
    "CIS-4315_Cyber_Governance_Risk_Compliance": {
        "cert": "ISACA Certified Information Security Manager (CISM)",
        "desc": "Security steering committees, policies vs standards, NIST Risk Management Framework, quantitative ALE calculation, BIA recovery objectives, GDPR privacy, and SOC auditing.",
        "oer": "NIST Cybersecurity Framework (nist.gov/cyberframework)",
        "weeks": [
            {
                "topic": "Security Governance Frameworks",
                "terms": "Information security governance, CIA triad, security alignments, strategic objectives.",
                "lab": ["Map security program alignments to corporate goals", "Review CIA triad definitions", "Document security steering committee responsibilities"],
                "q": "What is the primary objective of Information Security Governance?",
                "opts": ["A) Installing host antiviruses", "B) Aligning the information security strategy with overall business objectives and goals", "C) Blocking internet traffic", "D) Encrypting database backups"],
                "ans": "B",
                "expl": "Governance ensures security operations support business goals, manage risks, and conform to corporate policies.",
                "dist": "Antivirus installations and network blocks are technical operations, not governance planning."
            },
            {
                "topic": "Security Policies & Standards",
                "terms": "Security policies, standards, guidelines, procedures, policy life cycles.",
                "lab": ["Draft an acceptable use policy (AUP) template", "Differentiate standards from guidelines", "Write standard operating procedures"],
                "q": "Which document type contains mandatory, baseline rules specifying hardware and software requirements across the organization?",
                "opts": ["A) Policy", "B) Standard", "C) Guideline", "D) Procedure"],
                "ans": "B",
                "expl": "Standards are compulsory specifications. Policies are high-level goal definitions. Guidelines are recommended options.",
                "dist": "Guidelines are non-mandatory suggestions."
            },
            {
                "topic": "Risk Management Frameworks",
                "terms": "Risk management frameworks, NIST SP 800-37 (RMF), risk categorization, control selections.",
                "lab": ["Review NIST SP 800-37 steps", "Categorize a mock system based on FIPS 199 parameters", "Draft security control baseline selection criteria"],
                "q": "What is the first step of the NIST Risk Management Framework (RMF)?",
                "opts": ["A) Categorize System", "B) Select Controls", "C) Prepare", "D) Implement Controls"],
                "ans": "C",
                "expl": "The RMF updated structure introduces Prepare as the initial step to align security goals prior to categorization.",
                "dist": "Categorize is the subsequent analytical step."
            },
            {
                "topic": "Asset Identification & Valuation",
                "terms": "Information assets, asset inventory, classification tiers (public, confidential), asset valuation metrics.",
                "lab": ["Create an asset inventory schema list", "Classify assets into security tiers", "Assign business value scores to databases"],
                "q": "Why is asset classification critical to risk management?",
                "opts": ["A) To speed up network connections", "B) To ensure appropriate security controls are applied based on value and sensitivity of data", "C) To save local hard drive space", "D) To write database schema code"],
                "ans": "B",
                "expl": "Classification allows organizations to apply cost-effective, high-tier security parameters to sensitive assets.",
                "dist": "It is a resource prioritization mechanism, not a database design or network performance tool."
            },
            {
                "topic": "Risk Assessment Methodology",
                "terms": "Qualitative vs quantitative assessment, threats, vulnerabilities, likelihood, impact, Single Loss Expectancy (SLE), Annualized Loss Expectancy (ALE).",
                "lab": ["Calculate SLE (Asset Value * Exposure Factor)", "Calculate ALE (SLE * Annualized Rate of Occurrence)", "Perform qualitative risk mapping"],
                "q": "An asset worth $100,000 has an exposure factor of 40% if a server room flood occurs. The flood risk occurs once every 5 years. What is the ALE?",
                "opts": ["A) $40,000", "B) $200,000", "C) $8,000", "D) $20,000"],
                "ans": "C",
                "expl": "SLE = $100,000 * 0.40 = $40,000. ARO = 1/5 = 0.2. ALE = SLE * ARO = $40,000 * 0.2 = $8,000.",
                "dist": "40,000 is the SLE. 8,000 is the annualized expected loss."
            },
            {
                "topic": "Risk Mitigation Strategies",
                "terms": "Risk treatment plans, risk acceptance limits, risk avoidance, risk mitigation, risk sharing/transfer.",
                "lab": ["Draft a risk treatment plan template", "Outline control recommendations for identified vulnerabilities", "Review risk registry balances"],
                "q": "Which risk treatment option involves completely eliminating the threat by stopping the business activity associated with the risk?",
                "opts": ["A) Mitigation", "B) Avoidance", "C) Acceptance", "D) Transfer"],
                "ans": "B",
                "expl": "Risk avoidance stops the activity (e.g. disabling external website features to prevent SQL attacks completely).",
                "dist": "Mitigation implements controls (e.g. firewalls) to reduce risk while keeping the activity active."
            },
            {
                "topic": "Business Impact Analysis",
                "terms": "Business Impact Analysis (BIA), critical business functions, Recovery Time Objective (RTO), Recovery Point Objective (RPO), Maximum Tolerable Downtime (MTD).",
                "lab": ["Draft a BIA questionnaire layout", "Identify critical business processes and assign MTD scores", "Determine RTO/RPO limits"],
                "q": "Which metric defines the maximum acceptable age of data that must be recovered from backup storage after a system failure?",
                "opts": ["A) Recovery Time Objective (RTO)", "B) Recovery Point Objective (RPO)", "C) Maximum Tolerable Downtime (MTD)", "D) Mean Time to Repair (MTTR)"],
                "ans": "B",
                "expl": "RPO measures data loss limits (e.g. RPO of 4 hours means backups must run at least every 4 hours).",
                "dist": "RTO measures recovery duration (how long systems can remain offline)."
            },
            {
                "topic": "Disaster Recovery & Business Continuity",
                "terms": "Business Continuity Plan (BCP), Disaster Recovery Plan (DRP), hot/warm/cold sites, testing DRP (tabletop, walkthrough).",
                "lab": ["Draft table-top exercise test agendas", "Compare hot vs cold recovery site parameters", "Write emergency activation procedures"],
                "q": "Which recovery site type is fully operational, contains real-time mirrored datasets, and can take over production workflows within minutes?",
                "opts": ["A) Cold Site", "B) Warm Site", "C) Hot Site", "D) Mirror Store"],
                "ans": "C",
                "expl": "Hot sites are equipped with matching hardware, power, and synchronized datasets for rapid failovers.",
                "dist": "Cold sites have floor space and power but no hardware or data backups pre-loaded."
            },
            {
                "topic": "Regulatory Compliance (HIPAA, SOX)",
                "terms": "Regulatory compliance, Sarbanes-Oxley (SOX), Health Insurance Portability and Accountability Act (HIPAA), GLBA.",
                "lab": ["Audit system documentation for HIPAA privacy rule indicators", "Map SOX IT financial controls", "Review regulatory logs"],
                "q": "Which regulatory law mandates strict electronic security and privacy controls to protect patient health records?",
                "opts": ["A) SOX", "B) HIPAA", "C) GLBA", "D) FISMA"],
                "ans": "B",
                "expl": "HIPAA enforces security controls surrounding protected health information (PHI).",
                "dist": "SOX targets financial audit accuracy in public corporations."
            },
            {
                "topic": "Privacy Regulations (GDPR, CCPA)",
                "terms": "General Data Protection Regulation (GDPR), California Consumer Privacy Act (CCPA), Personally Identifiable Information (PII), right to be forgotten.",
                "lab": ["Document PII database tables locations", "Draft a GDPR right-to-be-forgotten deletion workflow script template", "Review privacy warnings"],
                "q": "What is the primary focus of the General Data Protection Regulation (GDPR)?",
                "opts": ["A) Securing financial reports", "B) Protecting data privacy and individual rights for citizens of the European Union", "C) Regulating defense networks", "D) Setting software speed targets"],
                "ans": "B",
                "expl": "GDPR enforces strict guidelines on how personal data (PII) is collected, stored, and processed for EU residents.",
                "dist": "GDPR covers personal privacy, not corporate accounting or military systems."
            },
            {
                "topic": "Industry Standards (PCI-DSS, ISO)",
                "terms": "Payment Card Industry Data Security Standard (PCI-DSS), ISO/IEC 27001, security controls certification.",
                "lab": ["Review PCI-DSS 12 core requirements checklists", "Map ISO 27001 Annex A controls to company security policies", "Audit network segments"],
                "q": "Which standard is mandatory for any organization processing, storing, or transmitting credit card information?",
                "opts": ["A) ISO 27001", "B) PCI-DSS", "C) NIST 800-53", "D) SOC 2"],
                "ans": "B",
                "expl": "PCI-DSS is established by major card brands to secure cardholder data environments.",
                "dist": "ISO 27001 is a voluntary international security framework."
            },
            {
                "topic": "Security Auditing Procedures",
                "terms": "IT audit, internal audit vs external audit, audit evidence, audit trail logs, control testing.",
                "lab": ["Draft an audit evidence request sheet", "Inspect system login logs for audit trail verification", "Review audit guidelines"],
                "q": "What is the primary purpose of an IT security audit?",
                "opts": ["A) To write clean code", "B) To evaluate system operations and verify controls align with regulatory policies and design objectives", "C) To speed up database loops", "D) To purchase firewalls"],
                "ans": "B",
                "expl": "Auditors independently verify that documented security policies and control systems are actually operating as intended.",
                "dist": "It is an validation check, not a development or purchasing role."
            },
            {
                "topic": "Vendor Risk Management",
                "terms": "Third-party risk, vendor assessment, SOC 2 reports, service level agreements (SLA), security questionnaires.",
                "lab": ["Evaluate third-party vendor security disclosures", "Analyze a mock SOC 2 Type II report for control deficiencies", "Review vendor SLA metrics"],
                "q": "What is the key difference between a SOC 2 Type I and a SOC 2 Type II report?",
                "opts": ["A) Type I covers security", "B) Type I assesses control design at a point in time; Type II evaluates operational effectiveness over a period of time", "C) Type I is public; Type II is confidential", "D) Type I is for software; Type II is for hardware"],
                "ans": "B",
                "expl": "Type II reports provide audit evidence confirming that controls were actively working over a testing window (usually 6-12 months).",
                "dist": "Type I only checks if controls were documented and set up on a specific date."
            },
            {
                "topic": "Security Awareness Programs",
                "terms": "Social engineering mitigation, phishing simulations, user training metrics, security culture.",
                "lab": ["Draft a phishing simulation training slide outline", "Review metric statistics for user link clicks during tests", "Outline training agendas"],
                "q": "Which security measure is most effective at reducing the risk of successful phishing attacks against employees?",
                "opts": ["A) Implementing longer passwords", "B) Continuous security awareness training and phishing simulations", "C) Turning off email servers", "D) Changing employee usernames"],
                "ans": "B",
                "expl": "Simulated training educates employees to spot warning signs (mismatched domains, urgent requests) before clicking links.",
                "dist": "Lengthy passwords do not stop users from typing credentials into fake sites."
            },
            {
                "topic": "Incident Response Governance",
                "terms": "Incident classification, escalation pathways, communication logs, post-incident reviews, regulatory notifications.",
                "lab": ["Draft an incident escalation flow chart", "Calculate regulatory breach notification schedules", "Complete post-incident analysis reports"],
                "q": "Why is establishing an incident escalation pathway critical in governance?",
                "opts": ["A) To prevent compiler warnings", "B) To ensure security breaches are reported to appropriate executive management and legal teams within required schedules", "C) To speed up disk speeds", "D) To write code comments"],
                "ans": "B",
                "expl": "Escalation rules ensure critical security events receive immediate senior-level focus and meet regulatory notification laws.",
                "dist": "It targets communications and compliance governance."
            }
        ]
    },
    "CIS-4320_Enterprise_Systems_ERP": {
        "cert": "Salesforce Certified Associate / SAP Certified Associate",
        "desc": "ERP database integrations, business processes mapping (BPMN), ledger accounting, MRP supply chains, Salesforce/SAP customize triggers, ETL migrations, and RBAC Separation of Duties.",
        "oer": "Salesforce Trailhead (trailhead.salesforce.com)",
        "weeks": [
            {
                "topic": "Enterprise Systems Concepts",
                "terms": "Enterprise Resource Planning (ERP), functional silos, integrated data, modular architectures.",
                "lab": ["Map business functional silos", "Evaluate database data redundency patterns", "Identify ERP business integration components"],
                "q": "What is the primary business value of implementing an Enterprise Resource Planning (ERP) system?",
                "opts": ["A) It lets developers write custom Python games", "B) It integrates business data from disparate departments (finance, sales, inventory) into a single database system", "C) It removes the need for web servers", "D) It speeds up local CPU clock cycles"],
                "ans": "B",
                "expl": "ERP breaks down departmental silos by providing a single source of truth for business transaction data.",
                "dist": "ERP target integration of business logistics, not programming compilers."
            },
            {
                "topic": "Business Process Management",
                "terms": "Business Process Management (BPM), BPMN 2.0 notation, swimlanes, events, gateways, process optimization.",
                "lab": ["Draft a procurement process map using BPMN 2.0 swimlanes", "Analyze bottlenecks in a fulfillment pipeline", "Define event gateways"],
                "q": "In BPMN 2.0, what element is used to categorize activities based on which department or role performs them?",
                "opts": ["A) Task box", "B) Gateway diamond", "C) Swimlane (Pool/Lane)", "D) Event circle"],
                "ans": "C",
                "expl": "Swimlanes separate tasks visually, assigning operational ownership to specific departments or users.",
                "dist": "Gateways direct logical splits in process routing."
            },
            {
                "topic": "ERP Selection & Vendor Landscape",
                "terms": "ERP vendors (SAP, Oracle, Microsoft Dynamics), selection criteria, total cost of ownership (TCO), RFP processes.",
                "lab": ["Compare ERP hosting scenarios (SaaS vs On-premise)", "Calculate TCO parameters for ERP proposals", "Draft vendor evaluation forms"],
                "q": "Which ERP vendor is historically the global market leader in enterprise application software?",
                "opts": ["A) Salesforce", "B) SAP", "C) Adobe", "D) Red Hat"],
                "ans": "B",
                "expl": "SAP is the dominant enterprise database and ERP platform provider, utilized by the majority of global corporations.",
                "dist": "Salesforce is the leader in CRM systems specifically, rather than core ERP backbones."
            },
            {
                "topic": "ERP Implementation Lifecycle",
                "terms": "ERP implementation phases: Planning, Design, Customization, Testing, Go-live, change management.",
                "lab": ["Draft an ERP project timeline", "Analyze failure risks in ERP implementations", "Define system cutover checklists"],
                "q": "Why do ERP implementation projects historically have high failure rates?",
                "opts": ["A) Lack of programming compilers", "B) Failure to manage organizational change and inadequate business process alignment", "C) Insufficient database disk space", "D) High network latency"],
                "ans": "B",
                "expl": "ERP success requires users to change how they work; resistance to new workflows and poor design mapping leads to failure.",
                "dist": "Hardware limitations are rarely the core cause of project failure."
            },
            {
                "topic": "Financial Management Modules",
                "terms": "General Ledger, Accounts Payable, Accounts Receivable, asset accounting, cost accounting, financial reporting.",
                "lab": ["Examine General Ledger double-entry transaction database links", "Map account matching rules", "Draft financial report templates"],
                "q": "Which ERP module records all financial transactions and serves as the primary data source for balance sheets?",
                "opts": ["A) Material Management", "B) General Ledger (FI-GL)", "C) Sales and Distribution", "D) Human Capital Management"],
                "ans": "B",
                "expl": "The General Ledger is the central repository mapping accounts and balancing debits and credits.",
                "dist": "Material Management tracks warehouse inventory assets, not corporate accounting ledgers."
            },
            {
                "topic": "Supply Chain Management Integrations",
                "terms": "Supply Chain Management (SCM), inventory control, material requirements planning (MRP), logistics, vendor records.",
                "lab": ["Run a mock Material Requirements Planning (MRP) request", "Track inventory levels and purchase triggers", "Map supply chain links"],
                "q": "What is the function of Material Requirements Planning (MRP) in an ERP system?",
                "opts": ["A) To design UI screens", "B) To calculate what materials are needed, in what quantities, and by what dates to meet production schedules", "C) To monitor database speeds", "D) To compile python scripts"],
                "ans": "B",
                "expl": "MRP uses inventory data, sales orders, and bill of materials (BOM) to schedule component purchases dynamically.",
                "dist": "MRP is logistics math, not UI styling or compiler optimization."
            },
            {
                "topic": "Customer Relationship Management Modules",
                "terms": "Customer Relationship Management (CRM), lead tracking, sales pipelines, account management, ticket systems.",
                "lab": ["Configure a sales lead tracking pipeline mapping stages", "Create customer profile database entries", "Map support ticket escalations"],
                "q": "Which business entity is the primary focus of a Customer Relationship Management (CRM) module?",
                "opts": ["A) Raw material vendors", "B) Warehouse locations", "C) Customers and sales leads", "D) Corporate employee records"],
                "ans": "C",
                "expl": "CRM systems track customer details, sales interactions, pipelines, and helpdesk tickets to improve business relationships.",
                "dist": "HCM tracks employees. ERP warehouse modules track locations."
            },
            {
                "topic": "Human Capital Management Modules",
                "terms": "Human Capital Management (HCM), payroll processing, time tracking, employee onboarding, performance metrics.",
                "lab": ["Review payroll transaction database tables", "Map employee onboarding workflows", "Verify timecard hours calculations"],
                "q": "Which data class is managed inside an ERP Human Capital Management (HCM) module?",
                "opts": ["A) Product pricing lists", "B) Employee records, payroll, benefits, and timecard logs", "C) Firewall security configurations", "D) DNS lookup zones"],
                "ans": "B",
                "expl": "HCM modules handle personnel files, payroll allocations, tax filings, and organizational structure mappings.",
                "dist": "Pricing is in sales modules. Firewall logs are system administration tasks."
            },
            {
                "topic": "ERP Database Structures",
                "terms": "Normalized tables, high transaction volume, indexing schemas, data dictionaries.",
                "lab": ["Analyze transactional table structures", "Trace index usage on high-volume queries", "Examine ERP database schemas"],
                "q": "Why do ERP databases utilize strict indexing and normalization layouts?",
                "opts": ["A) To prevent users from writing queries", "B) To ensure high transactional integrity (ACID) and prevent data duplication across large volumes", "C) To run faster than standard HTML", "D) To bypass operating system checks"],
                "ans": "B",
                "expl": "ERP databases handle millions of records daily; normalization prevents update anomalies, and indexes speed up searches.",
                "dist": "HTML does not run databases, and OS checks are not related to normalization."
            },
            {
                "topic": "Customizing ERP Systems",
                "terms": "Low-code tools, proprietary scripting (Salesforce Apex, SAP ABAP), database triggers, validation rules.",
                "lab": ["Write a mock validation rule checking email syntax", "Draft APEX trigger pseudo-code updating database records", "Test trigger conditions"],
                "q": "Which programming language is proprietary to SAP and used to develop custom reports and database integrations?",
                "opts": ["A) Python", "B) ABAP", "C) Apex", "D) SQL Server"],
                "ans": "B",
                "expl": "ABAP (Advanced Business Application Programming) is SAP's primary custom programming language.",
                "dist": "Apex is used for customizing Salesforce cloud platforms."
            },
            {
                "topic": "Enterprise Application Integration (EAI)",
                "terms": "EAI principles, REST/SOAP APIs, middleware brokers (MuleSoft), data transformation schemas.",
                "lab": ["Map database values to JSON API formats", "Draft middleware broker mapping definitions", "Trace REST integrations"],
                "q": "What role does middleware like MuleSoft play in enterprise system integration?",
                "opts": ["A) It replaces database engines", "B) It acts as a broker, translating and routing data payloads between disparate applications", "C) It builds front-end client screens", "D) It hosts virtual machines"],
                "ans": "B",
                "expl": "Middleware connects different architectures (e.g. cloud CRM to legacy on-premise ERP) by translating data formats on-the-fly.",
                "dist": "It is a routing and translation layer, not storage or virtualization."
            },
            {
                "topic": "Data Migration",
                "terms": "Extract, Transform, Load (ETL), data cleaning, mapping templates, validation checks.",
                "lab": ["Clean database records removing duplicate contacts", "Map field variables from legacy CSV to ERP tables", "Verify import logs"],
                "q": "What does the Transform step in the ETL (Extract, Transform, Load) data migration process involve?",
                "opts": ["A) Moving files to tape drives", "B) Cleaning, reformatting, and mapping raw data to match target database requirements", "C) Deleting records permanently", "D) Running compiler updates"],
                "ans": "B",
                "expl": "Transform adjusts data structures (e.g. splitting full names into first/last name columns) to match the target database schema.",
                "dist": "Extract pulls raw data. Load writes data to the new database."
            },
            {
                "topic": "ERP Security & Roles",
                "terms": "Role-Based Access Control (RBAC), Separation of Duties (SoD), audit profiles, permission sets.",
                "lab": ["Create user roles mapping permissions", "Audit roles for Separation of Duties (SoD) conflicts", "Document profile access scopes"],
                "q": "Which security concept is violated if a single ERP user is authorized to both approve purchase orders and issue vendor payments?",
                "opts": ["A) Least Privilege", "B) Separation of Duties (SoD)", "C) High Availability", "D) Single Sign-On"],
                "ans": "B",
                "expl": "SoD prevents fraud by dividing critical transactional tasks (e.g. creating invoices vs paying them) between different users.",
                "dist": "Least Privilege restricts access to baseline requirements but doesn't specifically target fraud-prevention workflow splits."
            },
            {
                "topic": "Cloud ERP hosting",
                "terms": "Software as a Service (SaaS), hybrid clouds, multi-tenant databases, upgrade schedules.",
                "lab": ["Analyze SaaS upgrade cycles impacts on custom code", "Map multi-tenant database designs", "Compare cloud hosting SLA metrics"],
                "q": "What is a characteristic of a multi-tenant cloud database design?",
                "opts": ["A) Each customer has their own physical server", "B) Multiple customers share the same database application instance and physical infrastructure, isolated logically", "C) It is unencrypted", "D) It does not support SQL"],
                "ans": "B",
                "expl": "Multi-tenancy allows cloud providers to scale resources by sharing physical infrastructure among customers while preserving strict security boundaries.",
                "dist": "Dedicated servers represent single-tenant infrastructure."
            },
            {
                "topic": "ERP Post-Implementation",
                "terms": "User adoption tracking, system performance reviews, bug databases, upgrading modules.",
                "lab": ["Draft user satisfaction survey templates", "Analyze system performance queries logs", "Write bug ticket triage outlines"],
                "q": "Why is post-implementation auditing critical for ERP deployments?",
                "opts": ["A) To write code comments", "B) To evaluate if the system met the business objectives defined in the charter and address operational bugs", "C) To configure DNS records", "D) To clear hard drive logs"],
                "ans": "B",
                "expl": "Audits check if the system actually realized projected ROI, resolved bottlenecks, and is being utilized correctly by staff.",
                "dist": "It focuses on business value evaluation."
            }
        ]
    },
    "CIS-4350_DevSecOps_CICD_Pipelines": {
        "cert": "Certified DevSecOps Professional (CDP)",
        "desc": "DevSecOps shift-left automation, commit linters, GitHub Actions YAML workflows, Docker setups, SAST/DAST testing, SCA dependencies, Vault secret masking, and chaos injections.",
        "oer": "DevSecOps Reference Architecture (devsecops.org)",
        "weeks": [
            {
                "topic": "DevSecOps Culture",
                "terms": "DevSecOps definition, shift-left security, pipeline automation, feedback loops.",
                "lab": ["Map security gate checks in development lifecycle", "Analyze cost differences of finding bugs early vs late", "Document pipeline structures"],
                "q": "What does the term Shift-Left mean in DevSecOps methodology?",
                "opts": ["A) Moving the development team to another room", "B) Integrating security practices, scanning, and testing earlier in the software development lifecycle", "C) Postponing testing until production", "D) Aligning script text to the left margin"],
                "ans": "B",
                "expl": "Shift-left brings security scanners directly into the developer's commit pipeline, resolving issues before deployments occur.",
                "dist": "It refers to workflow timing, not physical location or code formatting."
            },
            {
                "topic": "Continuous Integration Concepts",
                "terms": "Automation runners, local commit hooks, git triggers, linting steps.",
                "lab": ["Configure a local git pre-commit hook running code linters", "Analyze lint configuration files", "Test local commit constraints"],
                "q": "What is the primary function of a linter tool in a Continuous Integration pipeline?",
                "opts": ["A) To compile binaries", "B) To analyze source code for programmatic errors, code smells, and style guide violations", "C) To host REST APIs", "D) To decrypt database keys"],
                "ans": "B",
                "expl": "Linters check code syntax and styling against standard formats (e.g. PEP 8 for Python), catching basic errors early.",
                "dist": "Compilers convert code. Linters analyze source text."
            },
            {
                "topic": "GitHub Actions Workflow",
                "terms": "GitHub Actions, YAML syntax, runner environments, steps, jobs, trigger events.",
                "lab": ["Write a GitHub Actions workflow script using YAML", "Configure runner triggers on git push events", "Verify build execution logs"],
                "q": "Which file format is used to configure GitHub Actions workflow pipeline scripts?",
                "opts": ["A) JSON", "B) XML", "C) YAML", "D) CSV"],
                "ans": "C",
                "expl": "GitHub Actions workflows are declared in YAML files located inside the .github/workflows/ directory.",
                "dist": "YAML is standard for configuration scripts due to its human-readable layout."
            },
            {
                "topic": "Package & Artifact Management",
                "terms": "Artifact registries, package management (npm, pip), version tagging, securing packages.",
                "lab": ["Build package directories", "Configure build artifacts outputs inside pipelines", "Upload build packages to mock registries"],
                "q": "Why should pipelines upload validated builds to a secure artifact registry?",
                "opts": ["A) To delete local source files", "B) To maintain single, unalterable build versions that can be deployed repeatably across target environments", "C) To run tests faster", "D) To bypass license checks"],
                "ans": "B",
                "expl": "Registry repositories host ready-to-deploy, version-controlled binaries, ensuring environment consistency.",
                "dist": "It is about build consistency and repeatability."
            },
            {
                "topic": "Docker Containerization in CI/CD",
                "terms": "Dockerfile syntax, container layers, caching strategies, building images in pipelines.",
                "lab": ["Write a multi-stage Dockerfile for a node app", "Configure docker build steps in CI pipeline", "Test container locally"],
                "q": "What is the benefit of using multi-stage builds in a Dockerfile?",
                "opts": ["A) It compiles the container to run on multiple ports", "B) It allows separate build environments and produces smaller, minimized final deployment images", "C) It encrypts container data", "D) It requires no base image"],
                "ans": "B",
                "expl": "Multi-stage builds allow compiler tools to run in early stages, copying only the final binaries to the lean deployment image.",
                "dist": "It focuses on reducing the final attack surface and image size."
            },
            {
                "topic": "Static Application Security Testing",
                "terms": "SAST scanners, static analysis, pattern matching, false positives management.",
                "lab": ["Configure a SAST scanner tool in pipeline", "Scan a repository containing security issues", "Review scan reports"],
                "q": "What is the characteristic behavior of a SAST (Static Application Security Testing) tool?",
                "opts": ["A) It scans code by executing the application in a test sandbox", "B) It analyzes source code files statically without running the application", "C) It monitors CPU fan speeds", "D) It blocks network ports dynamically"],
                "ans": "B",
                "expl": "SAST scanners evaluate source files against known vulnerability patterns (e.g. hardcoded keys, SQL concatenation).",
                "dist": "Dynamic testing (DAST) requires executing the code."
            },
            {
                "topic": "Dynamic Application Security Testing",
                "terms": "DAST scanners, OWASP ZAP, active scanning, sandbox testing, network responses.",
                "lab": ["Setup web app in a pipeline container", "Run a DAST scanner against web endpoint", "Verify vulnerability detections"],
                "q": "How does DAST (Dynamic Application Security Testing) scan for security vulnerabilities?",
                "opts": ["A) By reading source code files", "B) By testing the running application, simulating real attacks from an external perspective", "C) By analyzing database backups on disk", "D) By scanning the developer's laptop"],
                "ans": "B",
                "expl": "DAST scanners send requests (like SQL injection tests) to active endpoints to evaluate responses.",
                "dist": "SAST reads code text; DAST tests live responses."
            },
            {
                "topic": "Software Composition Analysis",
                "terms": "Software Composition Analysis (SCA), dependency trees, CVE databases, license compliance.",
                "lab": ["Run a SCA scan on dependencies", "Identify vulnerable packages", "Review update mitigations"],
                "q": "What is the primary function of a Software Composition Analysis (SCA) tool?",
                "opts": ["A) To design UI screens", "B) To identify open-source third-party dependencies with known security vulnerabilities (CVEs)", "C) To speed up network links", "D) To compile python packages"],
                "ans": "B",
                "expl": "SCA scans dependency definition files (e.g. package.json, requirements.txt) against vulnerability databases.",
                "dist": "It maps external package risks, not local code logic or compilation."
            },
            {
                "topic": "Infrastructure as Code CI/CD Integration",
                "terms": "IaC validation, linter checks (tflint), security scanning (checkov, tfsec), pipeline execution.",
                "lab": ["Write checkov scanning script for terraform files", "Integrate tfsec scanner in pipeline", "Analyze security failures in outputs"],
                "q": "What does a tool like Checkov or tfsec scan for in a DevSecOps pipeline?",
                "opts": ["A) Variable name typos", "B) Misconfigured cloud resources and security violations in IaC templates", "C) Operating system crashes", "D) Hard drive block sizes"],
                "ans": "B",
                "expl": "IaC scanners flag security risks (such as open S3 buckets or unencrypted disks) before the cloud resources are built.",
                "dist": "They target IaC configurations, not compiled software errors."
            },
            {
                "topic": "Automated Cloud Deployment",
                "terms": "Deployment strategies, canary releases, blue-green deployment, rollback procedures.",
                "lab": ["Map blue-green deployment server routing configurations", "Draft rollback triggers on health failure tests", "Verify system node health"],
                "q": "Which deployment strategy maintains two identical environments, routing traffic to one while updating and testing the other?",
                "opts": ["A) Direct Cutover", "B) Blue-Green Deployment", "C) Rolling Update", "D) Shadow Deployment"],
                "ans": "B",
                "expl": "Blue-green deployment minimizes downtime and risk; if the new environment (green) fails, routing redirects to the old (blue).",
                "dist": "Canary releases slowly roll out updates to a small subset of users."
            },
            {
                "topic": "Secret Management in Pipelines",
                "terms": "Secret scanning, git leaks prevention, HashiCorp Vault, encrypted env variables.",
                "lab": ["Configure github actions secrets variables", "Run a git leak scan detecting exposed tokens", "Verify secrets masking in logs"],
                "q": "Why should API keys and database passwords never be hardcoded in Git source files?",
                "opts": ["A) Git cannot compile files with secrets", "B) Once pushed, keys are saved in history logs and can be exposed to unauthorized parties", "C) Secrets slow down code execution", "D) Secrets cause network routing loops"],
                "ans": "B",
                "expl": "Git histories are persistent; exposing keys allows attackers to scrape repositories and compromise systems.",
                "dist": "It is a severe security risk, not a compilation or speed constraint."
            },
            {
                "topic": "Container Security & Scan",
                "terms": "Container base images, image scanning (Trivy), rootless containers, registry configurations.",
                "lab": ["Run Trivy container scan", "Identify high vulnerability counts", "Refactor Dockerfile to use alpine base image"],
                "q": "Which base image is preferred in container security to minimize vulnerability footprints?",
                "opts": ["A) Ubuntu Desktop", "B) Alpine Linux (minimal)", "C) Windows Server Core", "D) Debian Bullseye (Full)"],
                "ans": "B",
                "expl": "Alpine is a lightweight Linux distribution containing minimal binaries, reducing the attack surface.",
                "dist": "Standard distributions package hundreds of packages, raising vulnerability risks."
            },
            {
                "topic": "Monitoring, Logging & Telemetry",
                "terms": "Log aggregates, application telemetry, ELK stack, Prometheus, system alerts.",
                "lab": ["Map application telemetry flows", "Configure alert parameters on server failure states", "Review centralized logs dashboards"],
                "q": "What is the purpose of centralized logging in DevOps?",
                "opts": ["A) To write code logic", "B) To aggregate system and application logs from all servers into a single queried portal", "C) To host DNS domains", "D) To execute unit tests"],
                "ans": "B",
                "expl": "Centralized logs permit rapid query searches across microservices during system failures, debugging issues quickly.",
                "dist": "It targets operations management, not software compilation."
            },
            {
                "topic": "Chaos Engineering Basics",
                "terms": "Chaos engineering definition, failure injection (Chaos Monkey), resilience testing, fallback paths.",
                "lab": ["Map server crash scenarios", "Outline system resilience paths handling cluster node drops", "Document fallback workflows"],
                "q": "What is the primary goal of Chaos Engineering?",
                "opts": ["A) To write disorganized code", "B) To proactively inject failures into production systems to test and improve system resilience", "C) To reduce network bandwidth", "D) To bypass security firewalls"],
                "ans": "B",
                "expl": "Chaos engineering validates that clusters and databases degrade gracefully and auto-recover from server failures.",
                "dist": "It targets infrastructure testing, not code layout or network throttling."
            },
            {
                "topic": "DevSecOps Compliance & Audit",
                "terms": "Compliance as Code, pipeline audit logs, signed commits, build logs validation.",
                "lab": ["Verify signed git commits indicators", "Audit pipeline logs for control compliance checks", "Draft release approval forms"],
                "q": "How does automated pipeline logging support regulatory compliance audits?",
                "opts": ["A) It compiles python scripts", "B) It provides unalterable audit trails proving that every code release was tested, scanned, and authorized", "C) It deletes code history", "D) It speeds up database speeds"],
                "ans": "B",
                "expl": "Auditors require proof that release procedures are followed; CI/CD logs serve as immutable operational logs.",
                "dist": "It supports regulatory audit checks, not compiler execution."
            }
        ]
    },
    "CIS-4355_IoT_Embedded_Systems": {
        "cert": "IoT & Embedded Security (General Principles)",
        "desc": "IoT sensing layer interfaces, bitwise GPIO operations, memory constraints, RTOS scheduling, MQTT pub-sub, secure boot verification, OTA signing, and edge processing.",
        "oer": "OWASP IoT Security Project (owasp.org/www-project-internet-of-things)",
        "weeks": [
            {
                "topic": "IoT Architecture Layers",
                "terms": "IoT layers (Perception, Network, Support, Application), edge devices, smart sensors, gateways.",
                "lab": ["Map IoT component configurations", "Analyze latency differences of edge processing vs cloud", "Identify network points"],
                "q": "Which IoT architecture layer contains the sensors, actuators, and hardware components that interact with the physical environment?",
                "opts": ["A) Application Layer", "B) Perception (Sensing) Layer", "C) Network Layer", "D) Support Layer"],
                "ans": "B",
                "expl": "The Perception layer handles physical signals (temperature, light, motions) and digitizes them.",
                "dist": "Network layer handles communications routing (gateways, routers)."
            },
            {
                "topic": "Microcontrollers & Interfaces",
                "terms": "General Purpose Input/Output (GPIO), I2C protocol, SPI bus, analog-to-digital converter (ADC).",
                "lab": ["Trace pin connections layouts", "Write sensor reading loop scripts using Python/C modules", "Inspect communication timing"],
                "q": "How many data wire lines are used in the I2C communication protocol?",
                "opts": ["A) One wire", "B) Two wires (SDA and SCL)", "C) Four wires (MISO, MOSI, SCK, CS)", "D) Eight wires"],
                "ans": "B",
                "expl": "I2C uses a Serial Data (SDA) line and a Serial Clock (SCL) line, supporting multiple master/slave nodes.",
                "dist": "SPI uses four wire lines (MISO, MOSI, SCK, CS)."
            },
            {
                "topic": "Embedded Programming C/C++",
                "terms": "Memory constraints, pointers, bitwise operations, registers mapping, static allocations.",
                "lab": ["Write a C script compiling bitwise shifts toggling flags", "Manage memory pointers without leaks", "Verify memory usage"],
                "q": "Why is static memory allocation preferred over dynamic allocation (malloc) in high-reliability embedded systems?",
                "opts": ["A) Static memory runs slower", "B) Dynamic allocation risks heap fragmentation and runtime memory exhaustion (out-of-memory crashes)", "C) C does not support dynamic allocation", "D) Pointers are not allowed"],
                "ans": "B",
                "expl": "Microcontrollers have tiny RAM capacities; heap fragmentation can trigger unpredictable system crashes during long-term runs.",
                "dist": "Dynamic memory is supported in C but highly restricted in embedded code."
            },
            {
                "topic": "RTOS Concepts",
                "terms": "Real-Time Operating System (RTOS), deterministic scheduling, task priority, preemptive kernels, semaphores.",
                "lab": ["Map task priorities schedules in RTOS framework", "Trace semaphore locking processes", "Verify task execution"],
                "q": "What is the defining characteristic of a Real-Time Operating System (RTOS)?",
                "opts": ["A) It features a graphical user interface", "B) It guarantees deterministic, predictable task execution and meeting timing constraints", "C) It requires massive hard drive spaces", "D) It only supports web servers"],
                "ans": "B",
                "expl": "RTOS priority-driven scheduling guarantees that critical tasks complete within strict deadlines.",
                "dist": "RTOS environments are minimal and rarely include graphical UI systems."
            },
            {
                "topic": "IoT Protocols (MQTT/CoAP)",
                "terms": "Message Queuing Telemetry Transport (MQTT), publisher-subscriber, MQTT broker, CoAP (UDP-based).",
                "lab": ["Configure a local MQTT broker (Mosquitto) server", "Publish sensor message packets using CLI command", "Subscribe client to topics"],
                "q": "What is the communication pattern utilized in the MQTT protocol?",
                "opts": ["A) Client-Server HTTP", "B) Publish-Subscribe (Pub/Sub)", "C) Peer-to-Peer streaming", "D) File Transfer Protocol"],
                "ans": "B",
                "expl": "Clients publish data to topics on a central broker, which routes the messages to subscribed clients.",
                "dist": "HTTP uses a standard Request-Response pattern."
            },
            {
                "topic": "Wireless Technologies",
                "terms": "Bluetooth Low Energy (BLE), Zigbee mesh, LoRaWAN long-range, Wi-Fi constraints, energy usage.",
                "lab": ["Compare wireless parameters (range, power, bandwidth) for IoT", "Analyze mesh routing topologies", "Verify network link ranges"],
                "q": "Which wireless protocol is best suited for low-power, long-range sensor networks deployed across agricultural fields?",
                "opts": ["A) Bluetooth Low Energy (BLE)", "B) LoRaWAN", "C) Wi-Fi (802.11)", "D) Zigbee"],
                "ans": "B",
                "expl": "LoRaWAN offers long-range (kilometers) communications at extremely low power rates, sacrificing bandwidth.",
                "dist": "BLE is restricted to short ranges (meters). Wi-Fi consumes too much power."
            },
            {
                "topic": "Cloud IoT Gateways",
                "terms": "Cloud IoT registries, device identity, telemetry ingest, cloud integrations, MQTT bridges.",
                "lab": ["Map device registries registry settings", "Draft secure keys authentication scripts for devices", "Trace telemetry logs"],
                "q": "What is the primary function of a Cloud IoT Gateway?",
                "opts": ["A) To compile device firmware binaries", "B) To authenticate devices securely and ingest massive streams of telemetry data into cloud systems", "C) To host web client pages", "D) To execute local physical tasks"],
                "ans": "B",
                "expl": "Cloud IoT Gateways provide the connection bridge, managing client device security certificates and ingesting raw sensor metrics.",
                "dist": "Gateways route messages, they do not write compiled firmware."
            },
            {
                "topic": "Embedded Security Threats",
                "terms": "OWASP IoT Top 10, default credentials, physical tampering, insecure firmware, missing encryption.",
                "lab": ["Audit device interfaces for open ports", "Locate vulnerable configurations", "Review attack methods"],
                "q": "According to the OWASP IoT Top 10, which vulnerability is historically the most exploited entry point for building device botnets?",
                "opts": ["A) SQL Injection", "B) Use of hardcoded, weak, or default credentials", "C) High CPU temperatures", "D) Missing code comments"],
                "ans": "B",
                "expl": "Default telnet/SSH credentials allow automated scripts to brute-force devices and load malicious botnet scripts.",
                "dist": "IoT devices rarely host relational SQL databases."
            },
            {
                "topic": "Cryptography in Constrained Devices",
                "terms": "Symmetric vs asymmetric keys, hardware encryption modules (TPM), resource constraints, hashing.",
                "lab": ["Measure encryption execution speeds of AES vs RSA on test platform", "Analyze CPU load differences", "Verify crypt keys"],
                "q": "Why is symmetric cryptography (like AES) preferred over asymmetric cryptography (like RSA) for securing sensor data transmissions directly on microcontrollers?",
                "opts": ["A) Symmetric crypto does not require keys", "B) Asymmetric math is highly resource-intensive and computationally expensive for low-power CPUs", "C) Symmetric crypto is not secure", "D) Asymmetric is only allowed on servers"],
                "ans": "B",
                "expl": "AES utilizes lightweight bitwise operations that execute quickly on small chips with minimal RAM and power.",
                "dist": "Both use keys, and asymmetric can run on small devices but consumes significant battery."
            },
            {
                "topic": "Secure Boot & OTA updates",
                "terms": "Secure boot process, crypt signatures, firmware verification, Over-The-Air (OTA) updates, rollback prevention.",
                "lab": ["Simulate firmware hash verification checks", "Review OTA secure signing certificate criteria", "Verify boot configurations"],
                "q": "How does Secure Boot protect an embedded IoT device?",
                "opts": ["A) It boots the system faster", "B) It cryptographically verifies the signature of the bootloader and firmware before executing, preventing unsigned code runs", "C) It disables the power button", "D) It deletes system database logs"],
                "ans": "B",
                "expl": "Secure Boot checks digital signatures against keys burned into the hardware's root-of-trust, blocking tampered firmware.",
                "dist": "It is a verification check, not a boot booster."
            },
            {
                "topic": "IoT Gateway Security",
                "terms": "Local gateway configurations, protocol translation security, device isolation, firewall rules.",
                "lab": ["Configure firewall routing rules on a mock gateway interface", "Isolate IoT devices in separate VLAN subnet", "Audit network logs"],
                "q": "Why should IoT devices be isolated on a separate network segment (VLAN) from corporate workstations?",
                "opts": ["A) To prevent devices from running out of batteries", "B) To contain security breaches, preventing compromised devices from being used to attack corporate assets", "C) To double network speeds", "D) To hide device MAC addresses"],
                "ans": "B",
                "expl": "Segmentation restricts lateral movement; if a smart camera is breached, the attacker cannot reach finance servers.",
                "dist": "It is about blast-radius containment, not battery life or speed."
            },
            {
                "topic": "Data Privacy in IoT Networks",
                "terms": "Sensor privacy, encrypting data at rest/transit, anonymization techniques, data storage limits.",
                "lab": ["Review database records for unencrypted sensor logs", "Draft data masking scripts for customer telemetry data", "Verify encryption"],
                "q": "What risk is presented by storing unencrypted device telemetry logs in a cloud database?",
                "opts": ["A) Logs run out of space", "B) Unauthorized parties can read sensitive location or activity data during a database breach", "C) Databases cannot index logs", "D) The CPU utilization increases"],
                "ans": "B",
                "expl": "Telemetry data can contain sensitive information (GPS, power consumption). Encryption protects it from data leaks.",
                "dist": "It is a confidentiality risk, not a database index limit."
            },
            {
                "topic": "Edge Computing Concepts",
                "terms": "Edge computing vs cloud computing, data filtering, local analytics, offline operations.",
                "lab": ["Write a script filtering sensor spikes locally before sending to cloud", "Compare network payload size savings", "Verify data streams"],
                "q": "What is the primary advantage of Edge Computing in IoT systems?",
                "opts": ["A) It eliminates the need for sensor hardware", "B) It processes data locally near the source, reducing latency, bandwidth consumption, and cloud reliance", "C) It runs without power", "D) It compiles web client designs"],
                "ans": "B",
                "expl": "Filtering and analyzing metrics at the gateway level reduces the volume of redundant data sent over network channels.",
                "dist": "Edge nodes still require hardware and power to execute operations."
            },
            {
                "topic": "Analyzing Telemetry Data",
                "terms": "Data streams, time-series data, database storage (InfluxDB), anomaly pattern detections.",
                "lab": ["Import time-series data using Pandas", "Plot sensor values over time", "Write basic anomaly threshold rules detecting outliers"],
                "q": "Which database type is optimized specifically for storing and querying continuous streams of sensor data tagged with timestamps?",
                "opts": ["A) Relational Database (SQL)", "B) Time-Series Database (TSDB)", "C) Graph Database", "D) Key-Value Store"],
                "ans": "B",
                "expl": "TSDBs (e.g. InfluxDB) are optimized for sequential write speeds and calculating moving averages over time windows.",
                "dist": "Graph databases track node linkages. Key-value stores hold configuration data."
            },
            {
                "topic": "Secure IoT Network Architecture",
                "terms": "End-to-end security, trust boundaries, device lifecycle management, final system audits.",
                "lab": ["Draft a security audit report for an IoT system design", "Identify trust boundaries and gaps", "Formulate security improvements"],
                "q": "Which design principle recommends securing an IoT system at the device level, the network level, and the cloud application level?",
                "opts": ["A) Single Point of Failure", "B) Defense in Depth (End-to-End Security)", "C) Simple Access Controls", "D) Direct Interface Trust"],
                "ans": "B",
                "expl": "Defense-in-depth ensures that if a control fails at one layer (e.g. Wi-Fi security), other layers (e.g. device auth, TLS) protect the system.",
                "dist": "Direct interface trust assumes elements inside are safe, which is a security risk."
            }
        ]
    }
}

# Combines all courses
ALL_COURSES = {}
for code, val in ORIGINAL_DATA.items():
    ALL_COURSES[code] = val
for code, val in NEW_COURSES_DATA.items():
    ALL_COURSES[code] = val

ALL_COURSES["CIS-1320_Intro_to_JavaScript"] = {
    "cert": "JSE (Certified Associate in JavaScript Programming)",
    "desc": "Introduction to JavaScript Programming, covering basic syntax, variables, data types, control flow, loops, functions, objects, arrays, DOM manipulation, asynchronous programming, and error handling.",
    "oer": "W3Schools JavaScript Tutorial / MDN Web Docs",
    "weeks": [
        {
            "topic": "JavaScript Introduction & Execution",
            "terms": "Scripting tag, client-side, JS engine, console log, execution context, statements.",
            "lab": ["Create a basic HTML page with an inline script tag", "Use console.log to print hello world", "Verify script execution in browser console"],
            "q": "Which HTML tag is used to embed or reference client-side JavaScript code within a web page?",
            "opts": ["A) <javascript>", "B) <script>", "C) <js>", "D) <code class='javascript'>"],
            "ans": "B",
            "expl": "The `<script>` tag is the standard HTML element used to embed or link external JavaScript code.",
            "dist": "The other options represent non-existent HTML tags."
        },
        {
            "topic": "Variables, Constants, and Scope",
            "terms": "var keyword, let keyword, const keyword, block scope, hoisting, global variable.",
            "lab": ["Declare variables using var, let, and const", "Demonstrate block scope behavior of let vs var", "Trigger a TypeError by reassigning a const variable"],
            "q": "Which keyword was introduced in ES6 to declare block-scoped variables that can be reassigned?",
            "opts": ["A) var", "B) let", "C) const", "D) define"],
            "ans": "B",
            "expl": "The `let` keyword declares block-scoped variables that can be reassigned.",
            "dist": "var is function-scoped and hoisted. const cannot be reassigned. define is not a variable declaration keyword."
        },
        {
            "topic": "Data Types & Operators",
            "terms": "Primitive types, type coercion, strict equality, arithmetic operators, typeof operator, null vs undefined.",
            "lab": ["Verify the type of variables using the typeof operator", "Demonstrate type coercion using the + operator with numbers and strings", "Compare values using == and ==="],
            "q": "What is the difference between the double-equality operator (==) and the triple-equality operator (===) in JavaScript?",
            "opts": ["A) == performs type coercion before comparing; === compares both value and type without coercion", "B) === performs type coercion; == does not", "C) == is used for strings; === is used for numbers", "D) There is no difference; they are interchangeable"],
            "ans": "A",
            "expl": "The strict equality operator (===) requires both operands to be of the same type and value, whereas == performs type coercion first.",
            "dist": "B is inverted. C is false because both operators can be used with any type. D is incorrect."
        },
        {
            "topic": "Control Flow & Conditionals",
            "terms": "if statement, else if clause, switch statement, ternary operator, logical operators, truthy vs falsy.",
            "lab": ["Write a conditional block evaluating test grades", "Implement a switch statement mapping weekdays", "Rewrite an if/else block using a ternary operator"],
            "q": "Which of the following values is evaluated as 'truthy' in a JavaScript conditional statement?",
            "opts": ["A) 0", "B) '' (empty string)", "C) [] (empty array)", "D) null"],
            "ans": "C",
            "expl": "In JavaScript, empty arrays `[]` and empty objects `{}` are truthy, whereas 0, empty strings, null, and undefined are falsy.",
            "dist": "0, empty string, and null are all falsy values."
        },
        {
            "topic": "Loops & Iteration",
            "terms": "for loop, while loop, do-while loop, break statement, continue statement, infinite loop.",
            "lab": ["Write a for loop that prints numbers 1 to 10", "Write a while loop that processes an array", "Use continue to skip printing odd numbers"],
            "q": "What is the primary characteristic of a do-while loop compared to a standard while loop?",
            "opts": ["A) It executes the code block at least once before checking the condition", "B) It does not check any conditions", "C) It only runs if the condition is false", "D) It cannot run indefinitely"],
            "ans": "A",
            "expl": "A do-while loop evaluates its condition after executing the body, ensuring the block runs at least once.",
            "dist": "The other options represent incorrect looping behaviors."
        },
        {
            "topic": "Functions & Arrow Functions",
            "terms": "Function declaration, function expression, arrow function, parameters, return statement, default arguments.",
            "lab": ["Define a function using standard function declaration", "Create an arrow function to calculate tax", "Use default parameters in a greeting function"],
            "q": "How does an arrow function handle the binding of the 'this' keyword?",
            "opts": ["A) It binds 'this' dynamically at runtime", "B) It has no 'this' of its own; it inherits 'this' from the lexical context", "C) It binds 'this' to the global window object always", "D) It forces 'this' to be undefined"],
            "ans": "B",
            "expl": "Arrow functions do not define their own `this` context; they inherit it from the surrounding lexical scope.",
            "dist": "Standard functions bind `this` dynamically based on execution context."
        },
        {
            "topic": "Objects & Properties",
            "terms": "Object literal, dot notation, bracket notation, methods, this keyword, key-value pairs.",
            "lab": ["Create a user object literal", "Access properties using dot and bracket notation", "Define a method that references this.username"],
            "q": "Which syntax is required to access an object property dynamically using a variable containing the property name?",
            "opts": ["A) dot notation (object.variableName)", "B) bracket notation (object[variableName])", "C) parenthetical notation (object(variableName))", "D) arrow notation (object->variableName)"],
            "ans": "B",
            "expl": "Bracket notation allows variable-based dynamic key lookup (e.g. `obj[key]`), whereas dot notation expects a literal identifier name.",
            "dist": "A will lookup a property literally named 'variableName'. C and D are syntactically invalid for property access in JavaScript."
        },
        {
            "topic": "Midterm Prep & Arrays",
            "terms": "Array literal, array index, push/pop, shift/unshift, array length, review concepts.",
            "lab": ["Create an array of fruits and manipulate elements", "Add elements using push and unshift", "Remove elements using pop and shift"],
            "q": "Which array method adds one or more elements to the *beginning* of an array and returns the new length?",
            "opts": ["A) push()", "B) pop()", "C) shift()", "D) unshift()"],
            "ans": "D",
            "expl": "The `unshift()` method adds elements to the front of the array; `push()` adds them to the end.",
            "dist": "push adds to the end. pop removes from the end. shift removes from the front."
        },
        {
            "topic": "Array Iteration & Callback Functions",
            "terms": "forEach method, map method, filter method, reduce method, callback execution.",
            "lab": ["Iterate over an array using forEach", "Create a new array of squared numbers using map", "Filter out odd numbers from a list"],
            "q": "Which array iteration method creates and returns a new array containing only elements that pass a logical condition?",
            "opts": ["A) map()", "B) filter()", "C) forEach()", "D) reduce()"],
            "ans": "B",
            "expl": "The `filter()` method returns a new array with elements that return true for the callback's condition.",
            "dist": "map transforms all elements. forEach iterates without returning a new array. reduce accumulates values."
        },
        {
            "topic": "Document Object Model (DOM) Basics",
            "terms": "DOM tree, document object, querySelector, querySelectorAll, getElementById, textContent.",
            "lab": ["Access elements by ID and Class", "Use querySelector to target elements", "Change element text using textContent"],
            "q": "Which DOM query method returns a static NodeList of all elements matching a specified CSS selector group?",
            "opts": ["A) getElementById()", "B) querySelector()", "C) querySelectorAll()", "D) getElementsByClassName()"],
            "ans": "C",
            "expl": "The `querySelectorAll()` method targets all elements matching a CSS selector and returns them in a NodeList.",
            "dist": "getElementById returns a single element. querySelector returns only the first matching element. getElementsByClassName returns an HTMLCollection."
        },
        {
            "topic": "DOM Manipulation & Styling",
            "terms": "createElement, appendChild, classList, setAttribute, inline styles, DOM hierarchy.",
            "lab": ["Create a new list item element dynamically", "Append elements to a list container", "Toggle classes using classList.toggle"],
            "q": "What is the recommended method to add a new CSS class to an element without overwriting existing classes?",
            "opts": ["A) element.className = 'new-class'", "B) element.classList.add('new-class')", "C) element.setAttribute('class', 'new-class')", "D) element.style.class = 'new-class'"],
            "ans": "B",
            "expl": "The `classList.add()` method appends the new class, preserving existing classes.",
            "dist": "className assignment and setAttribute overwrite the entire class attribute. style.class is invalid syntax."
        },
        {
            "topic": "Event Handling & Listeners",
            "terms": "addEventListener, click event, event object, event target, preventDefault, bubbling.",
            "lab": ["Attach a click handler to a button", "Access event details using the event parameter", "Use preventDefault on a form submit event"],
            "q": "Which method on the event object is used to stop the default browser action, such as navigating a link or submitting a form?",
            "opts": ["A) stopPropagation()", "B) preventDefault()", "C) stopImmediatePropagation()", "D) cancelEvent()"],
            "ans": "B",
            "expl": "The `preventDefault()` method tells the user agent that if the event goes unhandled, its default action should not be taken.",
            "dist": "stopPropagation prevents event bubbling. cancelEvent is not a valid method name."
        },
        {
            "topic": "Asynchronous JavaScript",
            "terms": "Synchronous block, callback queue, event loop, setTimeout, setInterval, stack execution.",
            "lab": ["Create a delayed alert using setTimeout", "Implement a digital clock using setInterval", "Demonstrate non-blocking execution order in console logs"],
            "q": "What is the purpose of the Event Loop in the JavaScript runtime environment?",
            "opts": ["A) To compile JavaScript source code into machine code", "B) To monitor the call stack and callback queue, pushing queued tasks when the stack is empty", "C) To handle garbage collection and memory allocation", "D) To execute SQL queries directly on the browser database"],
            "ans": "B",
            "expl": "The event loop continuously checks if the execution call stack is empty; if it is, it pulls tasks from the callback queue to run.",
            "dist": "The other options represent compiler, memory manager, or database functions."
        },
        {
            "topic": "Promises & Async/Await",
            "terms": "Promise state, resolve/reject, then/catch, async keyword, await expression, fetch API.",
            "lab": ["Create and resolve a custom Promise", "Fetch data from a public API using fetch and then()", "Refactor fetch calls using async/await syntax"],
            "q": "What does a function declared with the 'async' keyword always return?",
            "opts": ["A) An array of values", "B) A Promise", "C) A boolean representing success or failure", "D) The direct return value without wrapping"],
            "ans": "B",
            "expl": "An async function always returns a Promise. If the function returns a value, the Promise is resolved with that value.",
            "dist": "The other options are incorrect."
        },
        {
            "topic": "Error Handling & Debugging",
            "terms": "try block, catch clause, throw statement, stack trace, breakpoints, developer tools.",
            "lab": ["Implement a try/catch block to handle division by zero", "Throw a custom error if user input is invalid", "Add debugger statements to trace variables"],
            "q": "Which block in a try/catch statement runs regardless of whether an exception was thrown or caught?",
            "opts": ["A) try", "B) catch", "C) finally", "D) throw"],
            "ans": "C",
            "expl": "The `finally` block is executed immediately after try/catch, whether an error occurs or not.",
            "dist": "try and catch execution depend on the occurrence of errors. throw launches an exception."
        }
    ]
}


def clean_term_key(term):
    # Cleans trailing brackets, parentheses, and backticks for lookup
    t = term.strip().replace("`", "").replace("...", "")
    if "(" in t and ")" in t:
        # e.g. LIFO (Last-In-First-Out)
        return t
    return t

def get_term_definition(term):
    key = clean_term_key(term)
    if key in TERM_DEFINITIONS:
        return TERM_DEFINITIONS[key]
    for k, v in TERM_DEFINITIONS.items():
        if key.lower() in k.lower() or k.lower() in key.lower():
            return v
    # Smart fallback
    return f"A core foundational element of this week's studies, representing a primary parameter or configuration standard required for {key} administration."

def get_youtube_url(course, topic):
    # Returns a direct, helpful YouTube search query matching the topic and course certification
    query = f"{course['cert']} {topic}"
    if "Messer" in course.get("oer", ""):
        query = f"Professor Messer {course['cert']} {topic}"
    elif "CCNA" in course['cert']:
        query = f"Jeremy IT Lab CCNA {topic}"
    elif "Python" in course['cert']:
        query = f"Corey Schafer Python {topic}"
    
    encoded = urllib.parse.quote_plus(query)
    return f"https://www.youtube.com/results?search_query={encoded}"

print("=== STARTING RICH CONTENT GENERATION ===")

for code, data in ALL_COURSES.items():
    print(f"Generating rich files for {code}...")
    course_dir = os.path.join(BASE_DIR, code)
    os.makedirs(course_dir, exist_ok=True)
    
    # 00_Course_Information
    info_dir = os.path.join(course_dir, "00_Course_Information")
    os.makedirs(info_dir, exist_ok=True)
    
    # Generate dynamic weekly schedule blueprint
    weekly_schedule = []
    for w_idx, week in enumerate(data["weeks"], 1):
        weekly_schedule.append(f"*   **Module {w_idx:02d}:** {week['topic']}")
    weekly_schedule.append(f"*   **Module 16:** Final Exam Prep & Certification Exam ({data.get('cert', 'IT Certification')})")
    weekly_schedule_markdown = "\n".join(weekly_schedule)

    syllabus_path = os.path.join(info_dir, "Syllabus.md")
    with open(syllabus_path, "w") as f:
        f.write(f"""# TEXAS WESLEYAN UNIVERSITY
## Department of Computer Science & Information Technology
### Course Syllabus: {code} - {data.get('cert', 'IT Certification')}
**Semester & Year:** Fall 2026
**Course Format:** 100% Online Asynchronous
**Course LMS Portal:** Canvas LMS

---

## Instructor Information
*   **Instructor:** Professor Nash
*   **Department:** Computer Science & Information Technology
*   **Email:** nash@txwes.edu
*   **Office Hours:** Online by appointment (via Zoom/Teams)
*   **Response Time:** Within 24-48 hours on weekdays

---

## Course Overview

### Course Description
{data.get('desc', 'This course covers the primary core requirements and practical capabilities matching standard industry benchmarks.')}

### Course Objectives / Student Learning Outcomes
By the end of this course, students will be able to:
1. Explain and configure core principles of **{data.get('cert', 'IT Certification')}** in a variety of business and technical scenarios.
2. Formulate, execute, and verify terminal-based commands and administrative configurations matching production-level operations.
3. Critically analyze system failures or security vulnerabilities, and propose mitigation strategies.
4. Prepare for and demonstrate competency aligned with the official **{data.get('cert', 'IT Certification')}** certification exam blueprint.

### Required Materials
*   **Zero Textbook Cost (ZTC):** All required reading materials, video lectures, and study guides are provided completely free within the Canvas LMS course shell. No textbook purchase is required.
*   **Primary OER Resources:** Reference materials and official vendor documentation are outlined in the [ZTC OER Guide](../ZTC_OER_Reading_Materials.md).
*   **Hardware/Software Requirements:** Access to a computer running Windows, macOS, or Linux with terminal access, standard development tools, and high-speed internet.

---

## Grading & Evaluation

### Grading Policy
Your final grade is calculated based on the following breakdown:
*   **Weekly Quizzes (Modules 01-15):** 20%
*   **Weekly Discussion Boards (Modules 01-15):** 20%
*   **Hands-on Lab Assignments (Modules 01-15):** 30%
*   **Final Certification Exam (Module 16):** 30%

### Grading Scale
*   **A:** 90% - 100% (Excellent)
*   **B:** 80% - 89% (Good)
*   **C:** 70% - 79% (Satisfactory)
*   **D:** 60% - 69% (Passing)
*   **F:** Below 60% (Failure)

---

## Course Calendars & Blueprint
Below is the week-by-week layout of topics and assignments:

{weekly_schedule_markdown}

---

## University & Departmental Policies

### Attendance & Participation Policy
Since this course is conducted 100% online asynchronously, attendance is measured by weekly engagement. Students must log in to Canvas and submit at least one required assignment (discussion post, lab, or quiz) each week to be marked "Present". Failure to submit work for two consecutive weeks will be flagged for departmental review and may lead to administrative withdrawal in accordance with Texas Wesleyan University Catalog policies.

### Academic Integrity & Generative AI Policy
Texas Wesleyan University values academic honesty. Plagiarism, cheating, or any unauthorized collaboration will result in a zero grade for the assignment and potential disciplinary action, up to and including suspension. Refer to the *Texas Wesleyan Student Handbook* for full policies.
*   **Generative AI Guidelines:** In this course, you are encouraged to use AI tools (e.g. ChatGPT, Gemini, Copilot) to brainstorm concepts, understand error messages, and debug script files. However, all submissions (discussion posts, screenshots, explanations) must represent your own cognitive effort. Directly copy-pasting AI outputs without understanding or attribution is considered academic dishonesty.

### ADA & Disability Accommodations Statement
Texas Wesleyan University is committed to providing equal educational opportunities to all students. In accordance with Section 504 of the Rehabilitation Act of 1973 and the Americans with Disabilities Act (ADA), if you have a documented disability and require academic accommodations, please contact the **Office of Disability Services** (located in the Eunice and James L. West Library) as early in the semester as possible.

### Title IX & Harassment Policy
Texas Wesleyan University is committed to maintaining a learning environment free from all forms of discrimination, harassment, and sexual misconduct. If you experience or witness discrimination, sexual harassment, or assault, please report it to the Title IX Coordinator or consult the student handbook for confidential support services.

### Late Work Policy
All weekly assignments (quizzes, discussions, and labs) are due by **Sunday at 11:59 PM CST**. Late work is accepted up to 3 days (72 hours) past the deadline with a **10% penalty per day**. Submissions made after the 3-day grace period will receive a grade of zero unless documented extenuating circumstances are presented.

### Academic Support Services
Texas Wesleyan offers various free support resources to help you succeed:
*   **University Library:** Academic databases, citation guides, and research assistance.
*   **Tutoring & Learning Center (TLC):** Free peer tutoring for computer science and mathematics courses.
*   **Writing Center:** Assistance with structuring essays, documentation reports, and discussion board writing.

### Syllabus Change Notice
The instructor reserves the right to amend this syllabus or schedule at any time during the semester. Students will be notified of any changes immediately via Canvas Announcements.
""")

    # ZTC Guide
    ztc_path = os.path.join(course_dir, "ZTC_OER_Reading_Materials.md")
    with open(ztc_path, "w") as f:
        f.write(f"""# {code}: Zero Textbook Cost (ZTC) OER Guide

Welcome to the course resource repository! This course is part of our Zero Textbook Cost (ZTC) initiative. You are not required to buy any textbooks for this course.

## Primary Learning Channels
1.  **Primary Open Educational Resource (OER):** {data.get('oer', 'Official Documentation / Open Textbook')}
2.  **Video Lectures:** Curated YouTube streams matching the study units (links are included in each weekly video script).
3.  **Vendor Documentation:** Official developer portals and command reference manuals.

## Study Method
*   **Module Page (Video Script):** Read through the visual and audio narration outline to build a conceptual baseline before studying.
*   **Reading Guide:** Examine high-yield definitions and exam-prep tip blocks.
*   **Lab Activity:** Complete the hands-on commands in your Linux workstation VM, verify outputs, and log submissions.
*   **Practice Quiz:** Test your understanding and review the detailed distractor analyses to build active recall.
""")

    # Modules 01-15
    for i, week in enumerate(data.get("weeks", [])):
        week_num = f"{i+1:02d}"
        mod_dir = os.path.join(course_dir, f"Module_{week_num}")
        os.makedirs(mod_dir, exist_ok=True)
        
        topic = week["topic"]
        terms_str = week["terms"]
        lab_steps = week["lab"]
        
        # Build Glossary
        glossary = ""
        for term in [t.strip() for t in terms_str.split(",") if t.strip()]:
            definition = get_term_definition(term)
            glossary += f"*   **{term}**: {definition}\n"
            
        # Build YouTube Link
        yt_link = get_youtube_url(data, topic)
        
        # Format Lab Steps
        formatted_lab = ""
        for step_idx, step in enumerate(lab_steps):
            formatted_lab += f"{step_idx+1}. **{step}**\n"
            formatted_lab += f"   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.\n"
            
        # Format Quiz Options
        opts_str = ""
        for opt in week["opts"]:
            opts_str += f"*   {opt}\n"
            
        # Distractor Analysis formatting
        ans = week["ans"]
        dist = week.get("dist", "The other options represent alternative IT concepts that do not fit the specific execution constraints of the question.")
        
        # 1. Video Script
        script_path = os.path.join(mod_dir, f"01_Video_Script_Module_{week_num}.md")
        with open(script_path, "w") as f:
            f.write(f"""# Video Script: {code} ({data.get('cert')})
## Module {week_num} - {topic}
**Estimated Duration:** 12-15 minutes

---

### [00:00 - 02:30] Introduction and Certification Alignment
*   **Visual:** Instructor on camera with a title card displaying: **{topic}**.
*   **Audio:** "Hello class! Today we are digging into a vital topic for the **{data.get('cert')}** exam: **{topic}**. If you are new to this concept, don't worry. We will break it down step-by-step. Understanding how these systems communicate and operate is fundamental for passing your certification exam and configuring systems in a real-world enterprise environment."
*   **Study Link:** [Watch Video Lecture / Study Stream on YouTube]({yt_link})

---

### [02:30 - 09:30] Conceptual Deep-Dive
*   **Visual:** Split screen showing slides and a diagram mapping the key configurations.
*   **[Alt-text: A diagram illustrating the operational relationships of {topic} components, highlighting data paths and connection rules.]**
*   **Audio:** "Let's review the terms you need to master for this week's unit:
    {terms_str}
    
    Let's think of this like a real-world analogy. When configuring this setup, we must maintain strict order and safety protocols to ensure our networks and databases remain secure and performant."

---

### [09:30 - End] Walkthrough and Lab Prep
*   **Visual:** Live terminal showing command executions.
*   **[Alt-text: Command line console output showing the verification runs for {topic}.]**
*   **Audio:** "Now, let's step through the commands you will run in this week's lab. We will check statuses, run configurations, and log the completion metadata using the submit utility. Let's get started!"
""")

        # 2. Reading Guide
        guide_path = os.path.join(mod_dir, f"02_Reading_Guide_Module_{week_num}.md")
        with open(guide_path, "w") as f:
            f.write(f"""# Reading Guide: Module {week_num} - {topic}
## Course: {code} ({data.get('cert')})

---

## 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

{glossary}

---

## 2. Certification Exam Tips
*   **Focus Area:** Pay close attention to how these configuration values behave by default. The exam frequently features questions on default ports, parameters, or common diagnostic outputs.
*   **Scenario Trap:** Watch out for questions asking you to troubleshoot a failing configuration. Always verify if permissions or basic connectivity rules are violated first.
*   **Watch this resource:** To reinforce these concepts visually, review this targeted search query: [YouTube Exam Reference Link]({yt_link}).

---

## 3. Study Checklist
- [ ] Read the glossary terms and memorize their operational definitions.
- [ ] Watch the curated YouTube study streams matching **{topic}**.
- [ ] Proceed to the weekly hands-on lab activity.
""")

        # 3. Lab Activity
        lab_path = os.path.join(mod_dir, f"03_Lab_Module_{week_num}.md")
        with open(lab_path, "w") as f:
            f.write(f"""# Lab Activity: Module {week_num} - {topic}
## Course: {code} ({data.get('cert')})

---

## Objective
Configure and verify systems matching the operational parameters of **{topic}**.

---

## Prerequisites
*   Ensure you have access to a terminal or a runtime environment matching the course requirements (e.g., Linux, macOS, Windows, or a cloud/web terminal).
*   Ensure you have administrative privileges if required to install packages or configure system services.

---

## Step-by-Step Instructions
{formatted_lab}
---

## Troubleshooting Guide
*   *Error:* `Permission Denied`
    * *Fix:* Remember to run administrative command sequences using `sudo` or execute with administrative privileges (e.g., Run as Administrator on Windows).
*   *Error:* `Command Not Found`
    * *Fix:* Verify your environmental path settings, or double-check if the utility package is installed.

---

## Deliverables
1. Document your completed steps with screenshots or terminal output logs showing successful execution.
2. Submit your completion report to your Canvas LMS assignment portal for grading.
""")

        # 4. Quiz
        quiz_path = os.path.join(mod_dir, f"04_Quiz_Module_{week_num}.md")
        with open(quiz_path, "w") as f:
            f.write(f"""# Quiz: Module {week_num} - {topic}
## Course: {code} ({data.get('cert')})

---

### Question 1
{week["q"]}

{opts_str}
---

### Answer Key
*   **Correct Option:** **{ans}**

---

### Explanation
{week["expl"]}

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    {dist}
""")

        # 5. Discussion Prompt
        discussion_path = os.path.join(mod_dir, f"05_Discussion_Module_{week_num}.md")
        with open(discussion_path, "w") as f:
            f.write(f"""# Discussion Forum: Module {week_num} - {topic}
## Course: {code} ({data.get('cert')})

---

## Discussion Prompt
Consider the following real-world scenario or technical concept:
*   **Topic Focus:** **{topic}** (specifically focusing on: `{terms_str}`)

**Your Tasks:**
1.  **Initial Post (Due Wednesday at 11:59 PM):** In 150-200 words, explain how you would apply {topic} in an enterprise system. Address the following:
    *   What is the primary benefit of utilizing this configuration or standard in a production environment?
    *   Identify one common security concern or operational challenge related to this topic, and suggest a best-practice mitigation strategy.
2.  **Peer Responses (Due Sunday at 11:59 PM):** Read through your classmates' posts and write constructive replies (at least 50 words each) to at least two peers. In your replies:
    *   Provide feedback on their proposed mitigation strategy.
    *   Share an alternative approach or add context from your own research or lab exercises.

---

## Discussion Rubric (10 Points Total)
*   **Initial Post (6 Points):**
    *   *5-6 pts:* Thoroughly addresses all prompt questions with technical accuracy, clear explanations, and appropriate terminology. Meets the word count.
    *   *3-4 pts:* Addresses some prompt questions, but lacks detail or technical accuracy.
    *   *0-2 pts:* Incomplete or missing initial post.
*   **Peer Responses (4 Points):**
    *   *4 pts:* Responds constructively to at least two peers, contributing meaningful additions to the conversation.
    *   *2 pts:* Responds to only one peer, or comments are superficial (e.g., "Good post!").
    *   *0 pts:* No peer responses submitted.
""")

        # 6. Midterm Review (Only in Module 08)
        if week_num == 8:
            midterm_path = os.path.join(mod_dir, "Midterm_Review_Module_08.md")
            m1_7_topics = []
            for w_idx, w_data in enumerate(data["weeks"]):
                if w_idx < 7:
                    m1_7_topics.append(f"*   **Module 0{w_idx+1}:** {w_data['topic']} (Key terms: {w_data['terms']})")
            m1_7_topics_str = "\n".join(m1_7_topics)
            
            with open(midterm_path, "w") as f:
                f.write(f"""# Midterm Prep & Review Guide
## Course: {code} ({data.get('cert')})

Congratulations on reaching the halfway point of the semester! This review guide is designed to help you prepare for the upcoming Midterm Exam by summarizing key concepts from Modules 01 through 07.

---

## Core Topics for Review
{m1_7_topics_str}

---

## Study Recommendations
1.  **Revisit the Reading Guides:** Read through the *High-Yield Glossary* and *Certification Exam Tips* in each of the first 7 modules.
2.  **Review Quizzes:** Retake the practice quizzes and pay special attention to the *Distractor Analysis* for any questions you missed.
3.  **Lab Checkpoints:** Review the commands and configuration files you set up during the hands-on lab activities. Make sure you understand the diagnostic utilities you ran.
4.  **Practice Active Recall:** Write brief summaries of each module's core topic from memory and compare them to the Reading Guides.
""")

    # Module 16 (Final Exam)
    mod16_dir = os.path.join(course_dir, "Module_16")
    os.makedirs(mod16_dir, exist_ok=True)
    
    with open(os.path.join(mod16_dir, "02_Reading_Guide_Module_16.md"), "w") as f:
        f.write(f"""# Reading Guide: Module 16 - Final Exam Prep
## Course: {code} ({data.get('cert')})

This final module is dedicated to preparing for and completing the official **{data.get('cert')}** certification exam.

## Recommended Study Routine
1.  **Review the Practice Quizzes:** Go back through Modules 01 to 15 and retake the quizzes. Read the distractor analyses to ensure you understand why the wrong options are wrong.
2.  **Hands-on Review:** Re-run the diagnostic commands from the labs to ensure you can troubleshoot configurations.
3.  **Official Practice Tests:** Leverage vendor-provided mock exams (referenced in the course ZTC guide) to familiarize yourself with the timing and question styles.
""")
        
    with open(os.path.join(mod16_dir, "03_Lab_Module_16.md"), "w") as f:
        f.write(f"""# Lab Activity: Module 16 - Final Exam Submission
## Course: {code} ({data.get('cert')})

## Objective
Schedule and complete the official **{data.get('cert')}** industry certification exam, and submit your score verification report to Professor Nash.

## Instructions
1.  Register for the exam at the on-campus testing center or an authorized provider.
2.  Complete the exam.
3.  Obtain your official score report PDF showing your name, passing status, and date.
4.  Upload the official score report PDF to the Canvas LMS assignment box for this module to receive final credit.
""")

print("=== RICH CONTENT GENERATION COMPLETE ===")
