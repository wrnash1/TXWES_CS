# Quiz: Module 05 - Docker Containerization in CI/CD
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Question 1
What is the benefit of using multi-stage builds in a Dockerfile?

*   A) It compiles the container to run on multiple ports
*   B) It allows separate build environments and produces smaller, minimized final deployment images
*   C) It encrypts container data
*   D) It requires no base image

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Multi-stage builds allow compiler tools to run in early stages, copying only the final binaries to the lean deployment image.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    It focuses on reducing the final attack surface and image size.
