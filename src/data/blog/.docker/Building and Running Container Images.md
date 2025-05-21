---
title: Building and Running Container Images with Docker
pubDatetime: 2025-05-21
tags:
  - Docker
  - Building and Running
  - command
description: Create, Build, List, Run, Check Your Docker Images, Running Containers, Key Docker Commands, Understanding the Full Workflow, Real-World Analogy
---

## ✅ **What You'll Learn**

By the end of this guide, you will:

- Understand how to build a container image using a **Dockerfile**.
- Know how to create and run a container from an image.
- Be familiar with essential **Docker commands** like `build`, `run`, `images`, `ps`, `pull`, and `push`.

---

## 🧱 Step-by-Step Process: From Dockerfile to Running Container

### 1. **Create a Dockerfile**

A **Dockerfile** is a simple text file that contains instructions for building your Docker image.

#### 🔍 Example Dockerfile

```dockerfile
FROM ubuntu
CMD ["echo", "Hello World"]
```

- `FROM ubuntu` – tells Docker to use the Ubuntu operating system as the base image.
- `CMD ["echo", "Hello World"]` – runs the command `echo "Hello World"` when the container starts.

> 💡 Think of the Dockerfile as a recipe for your application environment.

---

### 2. **Build the Docker Image**

Use the `docker build` command to turn your Dockerfile into a **Docker image**.

#### 🔧 Command:

```bash
docker build -t my-app:v1 .
```

- `-t my-app:v1` – tags (names) your image as `my-app` with version `v1`.
- `.` – tells Docker to look for the Dockerfile in the current directory.

#### 📤 Output You’ll See:

- `Sending build context to Docker Daemon` – Docker collects all files needed to build the image.
- `Successfully built <image-id>` – confirms the image was created.
- `Successfully tagged my-app:v1` – confirms the tag was applied.

---

### 3. **List Your Docker Images**

To verify your image was built successfully:

#### 🔧 Command:

```bash
docker images
```

#### 📋 Output Includes:

| REPOSITORY | TAG | IMAGE ID | CREATED    | SIZE |
| ---------- | --- | -------- | ---------- | ---- |
| my-app     | v1  | abc12345 | 2 mins ago | 70MB |

This shows you now have an image ready to run!

---

### 4. **Run the Container**

Now that you have an image, you can create and start a **container** from it.

#### 🔧 Command:

```bash
docker run my-app:v1
```

This runs the `CMD` instruction from your Dockerfile and prints:

```
Hello World
```

---

### 5. **Check Running Containers**

After running the container, you may want to see if it’s still active or what containers are currently running.

#### 🔧 Command:

```bash
docker ps
```

> ⚠️ If the container ran and exited immediately (like our example), you won’t see it here unless you add the `--all` flag:

```bash
docker ps --all
```

---

## 🛠️ Key Docker Commands for Beginners

| Command         | Purpose                                                            |
| --------------- | ------------------------------------------------------------------ |
| `docker build`  | Builds an image from a Dockerfile                                  |
| `docker images` | Lists all local Docker images                                      |
| `docker run`    | Creates and runs a container from an image                         |
| `docker ps`     | Lists running containers (`docker ps --all` includes stopped ones) |
| `docker pull`   | Downloads an image from a registry (e.g., Docker Hub)              |
| `docker push`   | Uploads an image to a registry (e.g., Docker Hub)                  |

---

## 🧩 Understanding the Full Workflow

1. **Write a Dockerfile** – Define your app’s environment and startup behavior.
2. **Build an Image** – Use `docker build` to turn the Dockerfile into an image.
3. **Run a Container** – Use `docker run` to start a running instance of your image.
4. **Manage Images & Containers** – Use `docker images`, `docker ps`, etc., to view and manage them.

---

## 🎯 Real-World Analogy

Think of Docker like cooking:

- A **Dockerfile** is your recipe.
- The **Image** is the prepared dish ready to be served.
- The **Container** is the actual plate of food someone eats.

---

## 📌 Summary for Quick Reference

| Task                         | Command                      |
| ---------------------------- | ---------------------------- |
| Create image from Dockerfile | `docker build -t name:tag .` |
| List images                  | `docker images`              |
| Run container                | `docker run name:tag`        |
| List running containers      | `docker ps`                  |
| Pull image from registry     | `docker pull name:tag`       |
| Push image to registry       | `docker push name:tag`       |

---

## 📘 Tips for New Users

- Always test your Dockerfile by building and running the image.
- Use descriptive names and versions for your images (e.g., `my-web-app:1.0`).
- Clean up unused images and containers regularly:
  ```bash
  docker image prune -a
  docker container prune
  ```

---
