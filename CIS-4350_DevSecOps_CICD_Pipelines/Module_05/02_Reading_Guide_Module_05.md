# Reading Guide: Module 05 - Container Orchestration Security – Kubernetes

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 05 - Container Orchestration Security – Kubernetes**! This module extends container security into orchestration, examining how Kubernetes schedules, manages, and secures containerized workloads at scale. You will learn how multi-stage Dockerfiles reduce the attack surface of images deployed to Kubernetes, how CI/CD pipelines integrate container builds, and how Kubernetes security primitives — namespaces, resource limits, security contexts, and network policies — interact with container image security practices. These concepts are core to the CDP exam and to securing cloud-native production environments.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **Dockerfile syntax**: The set of instructions that define a container image build process layer by layer. In the context of Kubernetes deployments, Dockerfile security directly affects what attack surface is available if a pod is compromised — minimal images (Alpine, distroless) reduce the tools an attacker can use within the container.

* **Container layers**: The immutable, stacked read-only filesystem layers that compose a Docker image. In Kubernetes environments, each pod's container runs from a specific image digest, and the security of that image depends on the hygiene of each layer — avoiding unnecessary packages, secrets, and root-owned files.

* **Caching strategies**: Build-time optimization techniques that reuse unchanged image layers across pipeline runs. In a CI/CD pipeline that builds images for Kubernetes deployment, effective caching reduces build times and ensures consistent image content, while `--no-cache` flags can be used to force full rebuilds when security patches need to be applied immediately.

* **Building images in pipelines**: The CI/CD process of constructing a tagged, scanned, and signed container image from a Dockerfile as part of an automated workflow. Images built in pipelines are the only source of deployable artifacts in a secure Kubernetes environment — no images should be built and deployed manually outside the pipeline.

---

### 2. Certification Exam Tips

* **Multi-Stage Builds for K8s**: The CDP exam tests multi-stage Dockerfile patterns in the context of Kubernetes. Know that a distroless or Alpine final stage image contains no shell, package manager, or debugging tools — this is intentional, as it prevents an attacker who compromises the pod from pivoting using those tools.
* **Image Pull Policy**: In Kubernetes, `imagePullPolicy: Always` ensures pods always pull the latest tagged image from the registry rather than using a cached version on the node. This is important for security patches: always-pull guarantees patched images are used immediately after a pipeline re-deploys.
* **Pipeline → Registry → Kubernetes Flow**: Know the complete CI/CD-to-Kubernetes delivery path: CI pipeline builds image → scans image → pushes to registry → Kubernetes deployment manifest references image tag → K8s pulls image from registry → pod starts. A security failure at any stage should block the next stage.
* **Study Resource**: The [Kubernetes documentation on Pod Security](https://kubernetes.io/docs/concepts/security/pod-security-standards/) covers the Privileged, Baseline, and Restricted security standard profiles — understanding these three levels is directly tested on the CDP exam.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [Kubernetes Pod Security Standards documentation](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — the official Kubernetes reference defining the three security profiles (Privileged, Baseline, Restricted) that govern what container behaviors are permitted in a namespace. These standards map directly to the security context settings tested on the CDP exam.
* **Required Video**: Watch the container orchestration and Kubernetes segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — covers building multi-stage Docker images, pushing to a registry in a CI pipeline, and deploying the scanned image to a Kubernetes cluster.

---

### Lab & Command Integration

In this week's hands-on lab, you will apply Docker and Kubernetes security principles by:

* **Write a multi-stage Dockerfile for a Node.js app**: Create a two-stage Dockerfile — a `builder` stage that runs `npm install` and compiles assets, and a final stage using `node:alpine` that copies only the compiled output, resulting in a minimal production image.
* **Configure docker build steps in CI pipeline**: Add `docker build`, `docker scan` (or `trivy image`), and `docker push` steps to a GitHub Actions workflow, using `${{ secrets.REGISTRY_TOKEN }}` for registry authentication.
* **Test container locally**: Run `docker run --rm -p 3000:3000 myapp:local` and verify the application responds correctly, then inspect the image layers with `docker history myapp:local` to confirm no secrets or unnecessary tools are present in the final stage.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand how each Docker concept relates to Kubernetes container security.
* [ ] Read the Kubernetes Pod Security Standards at [https://kubernetes.io/docs/concepts/security/pod-security-standards/](https://kubernetes.io/docs/concepts/security/pod-security-standards/).
* [ ] Watch the Docker and Kubernetes segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the multi-stage Dockerfile and CI pipeline build steps in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
