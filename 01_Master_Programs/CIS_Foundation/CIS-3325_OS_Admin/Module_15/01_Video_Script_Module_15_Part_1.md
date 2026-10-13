# Video Script: Module 15 - Containerization: Docker Basics on Linux (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 13 minutes
**Part:** 1 of 2 - Container Concepts and Docker CLI

---

### Opening

Welcome to Module 15. Containers are one of the most significant shifts in how Linux systems are
deployed in the last decade. Understanding containers is now a core Linux administration skill and
is tested on the Linux+ exam. In this module we cover container concepts, the Docker CLI, images
vs containers, volumes, networking, and Dockerfile basics.

---

### Section 1: Containers vs Virtual Machines

[SHOW TERMINAL]

A virtual machine includes a full guest operating system, a kernel, and a hypervisor layer. It
is heavy — typically hundreds of megabytes of RAM at minimum just for the OS overhead.

A container shares the host Linux kernel. It uses two kernel features for isolation:

* **Namespaces** — each container gets its own isolated view of PIDs, network interfaces, mounts,
  users, and hostnames. Processes inside the container cannot see processes in other containers.
* **cgroups (control groups)** — limit and account for the CPU, memory, disk I/O, and network
  resources that a container can use.

A container is just a process (or group of processes) running with namespace and cgroup
constraints. It starts in milliseconds, uses only what the application needs, and shares the
host's kernel.

Key differences:

| | Container | Virtual Machine |
|--|-----------|----------------|
| OS | Shares host kernel | Full guest OS |
| Startup | Milliseconds | Seconds to minutes |
| Size | Megabytes | Gigabytes |
| Isolation | Namespace/cgroup | Hypervisor hardware boundary |
| Portability | Image runs anywhere | VM tied to hypervisor format |

---

### Section 2: Installing Docker on Ubuntu

[SHOW TERMINAL]

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

After adding your user to the `docker` group, log out and back in for the group to take effect.
Without this, every Docker command requires `sudo`.

```bash
docker --version
docker info
```

---

### Section 3: Images vs Containers

[SHOW TERMINAL]

An **image** is a read-only template. It is like a class in object-oriented programming.

A **container** is a running instance of an image. Multiple containers can be created from the
same image. Each container has its own writable layer on top of the read-only image.

```bash
docker images           # List downloaded images
docker ps               # List running containers
docker ps -a            # List all containers (including stopped)
```

---

### Section 4: Running Containers

[SHOW TERMINAL]

```bash
docker run hello-world
```

Downloads the `hello-world` image if not present, creates and runs a container, prints a message,
and exits.

```bash
docker run -it ubuntu bash
```

* `-i` — interactive (keep stdin open)
* `-t` — allocate a pseudo-TTY
* `ubuntu` — image name
* `bash` — command to run inside the container

You are now inside the container. Run `ls`, `cat /etc/os-release`, `exit` to leave.

```bash
docker run -d -p 8080:80 --name webserver nginx
```

* `-d` — detached (run in background)
* `-p 8080:80` — map host port 8080 to container port 80
* `--name webserver` — assign a name
* `nginx` — image

```bash
curl http://localhost:8080/
```

The nginx welcome page confirms the container is running.

---

### Section 5: Container Lifecycle

[SHOW TERMINAL]

```bash
docker ps                       # Show running containers
docker stop webserver           # Stop (sends SIGTERM, then SIGKILL)
docker start webserver          # Restart a stopped container
docker restart webserver        # Stop + start
docker rm webserver             # Remove a stopped container
docker rm -f webserver          # Force remove (stop + remove)
```

`docker stop` does NOT delete the container. The container still exists in stopped state.
`docker ps -a` shows stopped containers. `docker rm` deletes them.

```bash
docker run --rm -d -p 8080:80 nginx
```

`--rm` automatically removes the container when it stops. Good for short-lived containers.

---

### Section 6: Container Logs and Exec

[SHOW TERMINAL]

```bash
docker logs webserver
docker logs -f webserver        # Follow (like tail -f)
docker logs --tail 20 webserver # Last 20 lines
```

`docker logs` captures stdout and stderr from the container's main process.

```bash
docker exec -it webserver bash
```

Opens an interactive shell inside a running container. The container keeps running — this is
like SSH-ing into the container.

```bash
docker exec webserver cat /etc/nginx/nginx.conf
```

Run a single command inside a running container without an interactive shell.

---

### Section 7: Inspecting Containers

[SHOW TERMINAL]

```bash
docker inspect webserver
```

Outputs detailed JSON: network configuration, mount points, environment variables, port bindings,
resource limits. Useful when debugging why a container behaves unexpectedly.

```bash
docker inspect webserver | grep IPAddress
docker inspect --format '{{.NetworkSettings.IPAddress}}' webserver
```

Extract specific fields with `--format` using Go template syntax.

```bash
docker stats
docker stats webserver
```

Live CPU, memory, network I/O, and block I/O usage. Like `top` for containers.

---

### Section 8: Certification Connection

Docker maps to Linux+ Domain 4.0 (Automation and Scripting) and Domain 2.0 (Security). Key
exam topics:

* Containers share the host kernel via namespaces and cgroups — VMs do not
* `docker run -d` is detached; `-p HOST:CONTAINER` maps ports; `--name` assigns a name
* `docker ps` shows running; `docker ps -a` shows all; `docker stop` does not delete
* `docker logs` shows stdout/stderr; `docker exec -it` opens an interactive shell
* `docker rm` removes a stopped container; `docker rmi` removes an image

---

### Transition to Part 2

In Part 2 we cover volumes for persistent data, Docker networking, Dockerfile basics, and image
management (`docker build`, `docker push`, `docker pull`, Docker Hub).

---

### Additional Resources

* professormesser.com - CompTIA Linux+ study materials and practice exams
* comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
