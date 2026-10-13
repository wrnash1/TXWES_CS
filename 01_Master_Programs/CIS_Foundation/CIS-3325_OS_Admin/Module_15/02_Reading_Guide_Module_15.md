# Reading Guide: Module 15 - Containerization: Docker Basics on Linux

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 4.0 - Automation and Scripting

---

### Glossary

**Container** - A running instance of a Docker image. Uses Linux namespaces and cgroups for isolation. Shares the host kernel. Starts in milliseconds. Has a writable layer on top of the read-only image.

**Image** - A read-only template used to create containers. Built from a Dockerfile. Stored in layers. Multiple containers can run from the same image simultaneously.

**Namespace** - A Linux kernel feature that provides isolated views of system resources (PIDs, network interfaces, mounts, users, hostnames) for each container.

**cgroup (control group)** - A Linux kernel feature that limits and accounts for the CPU, memory, disk I/O, and network resources available to a set of processes.

**Dockerfile** - A text file containing instructions for building a Docker image. Each instruction creates a new image layer.

**Docker Hub** - The default public registry for Docker images. Images are pulled from Docker Hub when no registry is specified.

**Volume** - Docker-managed persistent storage stored in `/var/lib/docker/volumes/`. Survives container removal. Preferred over bind mounts for production data.

**Bind mount** - Maps a specific host directory into a container. Changes on either side are immediately visible on the other. Common in development workflows.

**Port mapping** - Publishing a container port on the host using `-p HOST_PORT:CONTAINER_PORT`. Makes the containerized service accessible from outside the container.

**Build context** - The directory passed to `docker build`. Files referenced in `COPY` instructions must exist in the build context.

---

### Container vs VM Comparison

| Feature | Container | Virtual Machine |
|---------|-----------|----------------|
| Kernel | Shares host kernel | Full guest OS kernel |
| Isolation mechanism | Namespaces + cgroups | Hypervisor hardware boundary |
| Startup time | Milliseconds | Seconds to minutes |
| Image size | Megabytes | Gigabytes |
| Security isolation | Weaker (shared kernel) | Stronger (full OS boundary) |
| Portability | High | Hypervisor-dependent |

---

### Docker Installation (Ubuntu)

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

After `usermod`, log out and back in for the docker group to take effect.

---

### Essential Docker CLI Commands

| Command | Purpose |
|---------|---------|
| `docker images` | List local images |
| `docker pull IMAGE` | Download image from registry |
| `docker run IMAGE` | Create and start a container |
| `docker run -d IMAGE` | Run detached (background) |
| `docker run -it IMAGE CMD` | Run interactive with TTY |
| `docker run -p H:C IMAGE` | Map host port H to container port C |
| `docker run --name NAME IMAGE` | Assign a container name |
| `docker run -v VOL:PATH IMAGE` | Mount volume at PATH |
| `docker run -e KEY=VAL IMAGE` | Set environment variable |
| `docker run --rm IMAGE` | Auto-remove container when it stops |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers (including stopped) |
| `docker stop NAME` | Stop a running container (SIGTERM) |
| `docker start NAME` | Start a stopped container |
| `docker restart NAME` | Stop + start |
| `docker rm NAME` | Remove a stopped container |
| `docker rm -f NAME` | Force remove (stop + delete) |
| `docker rmi IMAGE` | Remove an image |
| `docker logs NAME` | Show container stdout/stderr |
| `docker logs -f NAME` | Follow log output |
| `docker exec -it NAME bash` | Open interactive shell in container |
| `docker exec NAME CMD` | Run command in running container |
| `docker inspect NAME` | Show detailed container/image JSON |
| `docker stats` | Live resource usage for all containers |

---

### Docker Volume Commands

| Command | Purpose |
|---------|---------|
| `docker volume create NAME` | Create a named volume |
| `docker volume ls` | List volumes |
| `docker volume inspect NAME` | Show volume details |
| `docker volume rm NAME` | Remove a volume |
| `docker volume prune` | Remove all unused volumes |

Volume mount syntax: `-v NAME:CONTAINER_PATH`

Bind mount syntax: `-v /host/path:/container/path`

---

### Docker Network Commands

| Command | Purpose |
|---------|---------|
| `docker network ls` | List networks |
| `docker network create NAME` | Create a custom bridge network |
| `docker network inspect NAME` | Show network details |
| `docker network connect NET CONTAINER` | Connect container to network |
| `docker network rm NAME` | Remove a network |

Containers on a custom bridge network can resolve each other by container name. Containers on the default `bridge` network cannot resolve by name — IP only.

---

### Dockerfile Instruction Reference

| Instruction | Purpose |
|-------------|---------|
| `FROM IMAGE` | Set base image (must be first instruction) |
| `RUN CMD` | Execute command during build; creates a layer |
| `COPY SRC DEST` | Copy files from build context into image |
| `ADD SRC DEST` | Like COPY; also handles URLs and tar extraction |
| `ENV KEY=VALUE` | Set environment variable |
| `EXPOSE PORT` | Document port (does not publish to host) |
| `CMD ["CMD","ARG"]` | Default command; overridable with `docker run CMD` |
| `ENTRYPOINT ["CMD"]` | Fixed entry command; CMD provides arguments |
| `WORKDIR PATH` | Set working directory for subsequent instructions |
| `USER NAME` | Set user for subsequent instructions |
| `LABEL key=value` | Add metadata to the image |

---

### Docker Build and Push Workflow

```bash
docker build -t myapp:1.0 .
docker tag myapp:1.0 user/myapp:1.0
docker login
docker push user/myapp:1.0
docker pull user/myapp:1.0
```

---

### Image Management Commands

| Command | Purpose |
|---------|---------|
| `docker image prune` | Remove dangling (untagged) images |
| `docker image prune -a` | Remove all unused images |
| `docker save -o FILE.tar IMAGE` | Export image to tar file |
| `docker load -i FILE.tar` | Import image from tar file |
| `docker system df` | Show disk usage |
| `docker system prune` | Remove stopped containers, unused networks, dangling images |
| `docker system prune -a` | Also remove all unused images |

---

### Exam Tips

1. Containers share the host kernel via namespaces and cgroups. VMs have a full guest OS on a hypervisor. This is the most fundamental distinction and is directly tested.

2. `docker ps` shows only running containers. `docker ps -a` shows all. `docker stop` does not delete. `docker rm` is required to delete. Confusing stop with delete is a common exam trap.

3. `-p HOST:CONTAINER` maps ports. `-v NAME:PATH` mounts volumes. `-e KEY=VALUE` sets environment variables. `-d` runs detached. `-it` runs interactive with TTY. Know all five flags.

4. `docker logs NAME` reads stdout/stderr from the container's main process. `docker exec -it NAME bash` opens a shell inside a running container. These are different operations.

5. Volumes in `/var/lib/docker/volumes/` survive container removal. Bind mounts map host directories directly. Use volumes for databases in production; bind mounts for development source code.

6. Dockerfile: `FROM` is always first. `RUN` creates a new layer. `COPY` copies from the build context on the host. `EXPOSE` only documents a port — it does not publish it. `CMD` is the default command.

7. The build context is the directory passed to `docker build`. `COPY` can only reference files within the build context. Files outside it cause "not found in build context" errors.

8. `docker system prune` removes stopped containers, unused networks, and dangling images. Adding `-a` also removes all unused images. Use `docker system df` to see what is consuming disk space before pruning.

---

## 9. Supplemental Resources

**1. [Docker Engine Documentation — docs.docker.com](https://docs.docker.com/engine/)**
https://docs.docker.com/engine/
The official Docker Engine reference covering installation, CLI command reference, storage drivers, networking modes, and resource constraints. The CLI reference section documents every flag for `docker run`, `docker build`, `docker exec`, and `docker system` commands.

**2. [Dockerfile Reference — docs.docker.com](https://docs.docker.com/reference/dockerfile/)**
https://docs.docker.com/reference/dockerfile/
Complete reference for all Dockerfile instructions including FROM, RUN, COPY, ADD, ENV, EXPOSE, CMD, ENTRYPOINT, WORKDIR, and USER, with detailed explanations of exec form versus shell form and layer caching behavior.

**3. [Linux namespaces and cgroups — kernel.org](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)**
https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
Kernel documentation for cgroup v2, the Linux resource control mechanism underlying Docker's `--memory`, `--cpus`, and `--blkio-weight` limits. Understanding cgroups and namespaces explains how containers achieve isolation without a hypervisor.

---

### Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

* Explain how containers differ from VMs in terms of kernel sharing and isolation mechanism
* Run a container in detached mode with port mapping and a named volume
* View running containers and all containers including stopped ones
* Stop, start, and remove a container
* Open an interactive shell inside a running container with docker exec
* View container log output and follow it in real time
* Write a minimal Dockerfile with FROM, RUN, COPY, EXPOSE, and CMD
* Build an image from a Dockerfile
* Explain the difference between a Docker volume and a bind mount
* Remove stopped containers and unused images with docker system prune
