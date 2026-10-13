# Video Script: Module 15 - Containerization: Docker Basics on Linux (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">CompTIA Linux+ / Linux Foundation &bull; Operating System Administration &bull; Module 15</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" title="CompTIA Linux+ / Linux Foundation &bull; Operating System Administration" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>CompTIA Linux+ / Linux Foundation &bull; Operating System Administration</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->


**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 11 minutes
**Part:** 2 of 2 - Volumes, Networking, Dockerfile, and Image Management

---

### Opening

Welcome back to Part 2 of Module 15. In Part 1 we covered container concepts, the Docker CLI,
image vs container, and the container lifecycle. In Part 2 we cover persistent storage with
volumes, Docker networking, writing Dockerfiles, and building and managing images.

---

### Section 1: Volumes for Persistent Data

[SHOW TERMINAL]

By default, a container's writable layer is ephemeral — when the container is removed, all data
written inside the container is lost. Volumes solve this.

Three storage options:

* **Volume** — managed by Docker, stored in `/var/lib/docker/volumes/`. Preferred.
* **Bind mount** — maps a host directory directly into the container
* **tmpfs mount** — stored in host RAM only, not persisted to disk

Create and use a named volume:

```bash
docker volume create mydata
docker volume ls
docker volume inspect mydata
```

Run a container with a named volume:

```bash
docker run -d --name db \
  -v mydata:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8
```

* `-v mydata:/var/lib/mysql` — mount the `mydata` volume at `/var/lib/mysql` inside the container
* `-e MYSQL_ROOT_PASSWORD=secret` — set an environment variable

Even if you remove this container and create a new one with the same volume, the database data
persists.

Bind mount example (useful for development):

```bash
docker run -d --name web \
  -v $(pwd)/html:/usr/share/nginx/html \
  -p 8080:80 nginx
```

Changes to files in `./html/` on the host are immediately visible inside the container.

Remove volumes:

```bash
docker volume rm mydata
docker volume prune    # Remove all unused volumes
```

---

### Section 2: Docker Networking

[SHOW TERMINAL]

Docker creates a default bridge network. Containers on the same bridge network can reach each
other by IP but not by name by default.

```bash
docker network ls
docker network inspect bridge
```

Create a custom bridge network (containers on the same custom network can resolve each other by
container name):

```bash
docker network create mynet
docker run -d --name app1 --network mynet nginx
docker run -d --name app2 --network mynet alpine sleep 3600
docker exec app2 ping app1   # Name resolution works on custom networks
```

Connect an existing container to a network:

```bash
docker network connect mynet webserver
```

Port publishing makes a container port accessible on the host:

```bash
docker run -d -p 80:80 nginx        # All interfaces
docker run -d -p 127.0.0.1:80:80 nginx   # Localhost only
```

---

### Section 3: Dockerfile Basics

[SHOW TERMINAL]

A Dockerfile is a text file with instructions for building an image. Each instruction creates a
layer in the image.

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="admin@example.com"

RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

Key Dockerfile instructions:

| Instruction | Purpose |
|-------------|---------|
| `FROM` | Base image (must be first) |
| `RUN` | Execute a command during build (creates a layer) |
| `COPY` | Copy files from build context into image |
| `ADD` | Like COPY but also handles URLs and auto-extracts tar files |
| `ENV` | Set environment variables |
| `EXPOSE` | Document which port the container listens on (does not publish) |
| `CMD` | Default command when container starts (overridable at runtime) |
| `ENTRYPOINT` | Fixed command that always runs (CMD provides arguments) |
| `WORKDIR` | Set working directory for subsequent instructions |
| `USER` | Set the user for subsequent instructions |

Build an image from the Dockerfile:

```bash
docker build -t myapp:1.0 .
```

* `-t myapp:1.0` — tag the image as myapp version 1.0
* `.` — build context is the current directory

---

### Section 4: Image Management

[SHOW TERMINAL]

```bash
docker images              # List local images
docker rmi nginx           # Remove an image (must have no running containers)
docker rmi -f nginx        # Force remove
docker image prune         # Remove dangling (untagged) images
docker image prune -a      # Remove all unused images
```

Pull an image from Docker Hub:

```bash
docker pull nginx:1.25
docker pull ubuntu:22.04
```

Tag an image for pushing:

```bash
docker tag myapp:1.0 myusername/myapp:1.0
```

Push to Docker Hub (requires `docker login` first):

```bash
docker login
docker push myusername/myapp:1.0
```

Save and load images as tar files (for air-gapped environments):

```bash
docker save -o myapp.tar myapp:1.0
docker load -i myapp.tar
```

---

### Section 5: Docker System Maintenance

[SHOW TERMINAL]

```bash
docker system df           # Show disk usage
docker system prune        # Remove stopped containers, unused networks, dangling images
docker system prune -a     # Also remove all unused images
```

These are important on production systems where old images and stopped containers accumulate.

---

### Section 6: Exam Tips for Module 15

Containers vs VMs: containers share the host kernel (namespaces + cgroups). VMs have a full
guest OS on a hypervisor. Containers are faster and lighter; VMs have stronger isolation.

`docker run -d` = detached (background). `-p HOST:CONTAINER` = port mapping.
`-v NAME:PATH` = volume mount. `-e KEY=VALUE` = environment variable.

`docker ps` shows running only. `docker ps -a` shows all. `docker stop` does not delete.
`docker rm` removes a container. `docker rmi` removes an image.

`docker logs` reads stdout/stderr. `docker exec -it` opens an interactive shell in a running
container.

Dockerfile: `FROM` is first. `RUN` creates layers. `CMD` is the default command.
`COPY` copies from build context. `EXPOSE` documents a port but does not publish it.

Volumes vs bind mounts: volumes are managed by Docker in `/var/lib/docker/volumes/`.
Bind mounts map a specific host path. Use volumes for production databases; use bind mounts
during development.

---

### Summary

Module 15 covers containerization essentials for the Linux+ exam: container architecture
(namespaces + cgroups), Docker CLI (run/stop/rm/logs/exec), images vs containers, volumes for
persistence, Docker networking, Dockerfile instructions, and image management.

Module 16 is the final review and Linux+ exam preparation module.

---

### Additional Resources

* professormesser.com - CompTIA Linux+ study materials and practice exams
* comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
