# Quiz: Module 09 - Elastic Load Balancing & Auto Scaling
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Question 1
Which type of load balancer is best suited for routing millions of ultra-low latency TCP requests at Layer 4?

*   A) Application Load Balancer (ALB)
*   B) Network Load Balancer (NLB)
*   C) Classic Load Balancer
*   D) Gateway Load Balancer

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
NLB operates at Layer 4 (Transport) and handles volatile network spikes and TCP/UDP traffic at extreme speeds.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    ALB operates at Layer 7 and evaluates HTTP headers and paths.
