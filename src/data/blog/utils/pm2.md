---
title: PM2 Complete Guide to Theory, Installation & Essential Commands (2025)
pubDatetime: 2025-12-22
featured: false
tags:
  - Node.js
  - PM2
description: PM2 Complete Guide to Theory, Installation & Essential Commands (2025).
---

# Complete Guide to PM2: Theory, Installation & Essential Commands (2025)

If you run Node.js applications on a Linux server, you need a process manager that keeps your app running 24/7, restarts automatically on crashes, handles logs, and survives system reboots.
**PM2** is the most popular tool for that.

This guide covers everything:
✔ What PM2 is
✔ Why developers use it
✔ How to install it
✔ How to start/stop/manage apps
✔ All essential PM2 commands you need daily

---

##  What is PM2?

**PM2 (Process Manager 2)** is a production-grade process manager for Node.js applications. It ensures your app:

* Stays running **even after crashes**
* Automatically restarts after **server reboot**
* Runs multiple apps concurrently
* Monitors CPU & RAM usage
* Provides live logs
* Supports zero-downtime reloads

PM2 is widely used in MERN, MEAN, Express.js APIs, Next.js, Vite, and other Node-based applications.

---

## 🧠 How PM2 Works (Simple Theory)

PM2 sits between your app and the operating system:

```
User → PM2 → Node.js App → System
```

Key responsibilities:

### 1️⃣ **Process Management**

PM2 starts your app and keeps it alive.
If the app crashes, PM2 restarts it instantly.

### 2️⃣ **Monitoring**

PM2 monitors CPU/RAM and gives you live dashboards.

### 3️⃣ **Logging**

It merges stdout and stderr logs:

```
~/.pm2/logs/
```

### 4️⃣ **Auto-Restart on Boot**

PM2 generates a startup script so your app launches after reboot.

### 5️⃣ **Clustering (Optional)**

PM2 can run your app in multiple instances to use all CPU cores:

```sh
pm2 start app.js -i max
```

---

# 🛠️ Installing PM2

You only need Node.js + npm installed.

### Install globally:

```sh
npm install -g pm2
```

Check version:

```sh
pm2 -v
```

You’re ready to use PM2.

---

# 🚀 Starting Apps with PM2

### Start a Node.js app:

```sh
pm2 start app.js
```

### Start with a custom name:

```sh
pm2 start app.js --name api
```

### Start an app using an npm script (React, Vite, Next.js, MERN frontend)

```sh
pm2 start npm --name frontend -- run dev
```

### Start MERN backend:

```sh
pm2 start npm --name backend -- run dev
```

---

# 📌 Essential PM2 Commands (Cheat Sheet)

The most complete list for practical usage:

---

## 🔵 Process Management

### Start:

```sh
pm2 start app.js
pm2 start npm --name frontend -- run dev
```

### Stop:

```sh
pm2 stop app
pm2 stop all
```

### Restart:

```sh
pm2 restart app
pm2 restart all
```

### Delete (stop + remove from PM2):

```sh
pm2 delete app
pm2 delete all
```

---

## 🔵 Monitoring & Logs

### List running apps:

```sh
pm2 list
```

### Detailed info:

```sh
pm2 describe app
```

### View logs:

```sh
pm2 logs
pm2 logs app
```

### View last 200 lines:

```sh
pm2 logs --lines 200
```

### Real-time monitoring dashboard:

```sh
pm2 monit
```

---

## 🔵 Auto-Start After Reboot

### Enable startup script:

```sh
pm2 startup
```

Run the command it prints.

### Save currently running processes:

```sh
pm2 save
```

### Restore processes after reboot manually:

```sh
pm2 resurrect
```

---

## 🔵 Maintenance Commands

### Clear all logs:

```sh
pm2 flush
```

### Completely kill PM2:

```sh
pm2 kill
```

---

# 🎯 Bonus: Use PM2 with an Ecosystem File

Generate an ecosystem file:

```sh
pm2 init
```

Example (two apps: frontend + backend):

```js
module.exports = {
  apps: [
    {
      name: "backend",
      script: "npm",
      args: "run dev",
      cwd: "./backend"
    },
    {
      name: "frontend",
      script: "npm",
      args: "run dev",
      cwd: "./frontend"
    }
  ]
}
```

Start all apps:

```sh
pm2 start ecosystem.config.js
```

---

# 🧾 Summary

PM2 is a must-have tool for running production Node.js applications. It keeps apps alive, handles logs, manages restarts, and offers monitoring — all while being extremely easy to use.

### What you learned:

✔ What PM2 is
✔ How it works
✔ How to install it
✔ How to manage apps
✔ How to monitor logs
✔ How to auto-start after reboot
✔ Every essential PM2 command

Use this guide as your go-to reference whenever you deploy MERN or Node.js apps.

---
