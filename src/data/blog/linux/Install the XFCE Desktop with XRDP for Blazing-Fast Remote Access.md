---
title: Install XFCE Desktop with XRDP for Blazing-Fast Remote Access on Ubuntu Server
pubDatetime: 2025-10-30
featured: false
tags:
  - Hands On Lab
  - Linux
  - xrdp
description: Install XFCE Desktop with XRDP for Blazing-Fast Remote Access on Ubuntu Server
---

# 🚀 Turbocharge Your Cloud Server: Install the XFCE Desktop with XRDP for Blazing-Fast Remote Access

If you're running an Ubuntu server on the cloud and are tired of the slow, resource-heavy experience of a default desktop environment over RDP, you need a change. The secret to a fast, reliable, and efficient remote desktop is pairing the **XRDP** server with a **lightweight Desktop Environment (DE)**.

We recommend **XFCE**. It’s renowned for its **low resource consumption** and **stability**, making it the ideal choice for a cloud server where performance and efficiency are critical.

Here is a step-by-step guide to installing and configuring XFCE and XRDP for a top-tier remote desktop experience.

-----

## Prerequisites

Before you begin, ensure you have:

1.  An **Ubuntu Server** instance (e.g., Ubuntu 20.04 LTS or 22.04 LTS) running in the cloud.
2.  **SSH access** to the server with a user that has `sudo` privileges.

-----

## Step 1: Install XRDP and XFCE

First, we'll update the system, install the necessary XRDP service, and then install the XFCE desktop environment.

1.  **Update your system packages:**

    ```bash
    sudo apt update
    sudo apt upgrade -y
    ```

2.  **Install the XRDP service:**

    ```bash
    sudo apt install xrdp -y
    ```

3.  **Install the XFCE Desktop Environment:**
    We'll install the core XFCE package. This ensures you get a complete, functional desktop.

    ```bash
    sudo apt install xfce4 -y
    ```

    *(**Pro Tip:** If you want a truly minimal installation, you could use `xfce4-session` instead of `xfce4` to install fewer dependencies.)*

-----

## Step 2: Configure XRDP to Use XFCE

By default, XRDP might try to load a different or non-existent session, leading to a blank or slow screen. We must explicitly tell it to use the newly installed XFCE desktop.

1.  **Stop the XRDP service** temporarily before making changes:

    ```bash
    sudo systemctl stop xrdp
    ```

2.  **Configure the user's session:**
    Create or edit the `.xsession` file in the home directory of the user you will use to connect. This file tells XRDP which desktop to launch.

    ```bash
    echo xfce4-session > ~/.xsession
    ```

3.  **Set correct permissions** for the `.xsession` file:

    ```bash
    sudo chown -R $USER:$USER /home/$USER/.xsession
    ```

4.  **Restart the XRDP service** to load the new configuration:

    ```bash
    sudo systemctl restart xrdp
    ```

-----

## Step 3: Configure the Firewall

The default RDP port is **3389**. You must open this port in your server's firewall to allow incoming connections.

If you are using **UFW (Uncomplicated Firewall)**, run this command:

```bash
sudo ufw allow 3389/tcp
sudo ufw reload
```

*(**Note:** If your cloud provider uses its own firewall rules (Security Groups), you must also ensure port 3389 is open there.)*

-----

## Step 4: Connect with an RDP Client

You are now ready to connect\! Use your favorite **RDP client** on your local machine (Windows Remote Desktop Connection, Remmina, Microsoft Remote Desktop for Mac, etc.).

| Setting | Value |
| :--- | :--- |
| **Computer/Server** | Your server's public IP address or hostname. |
| **Port** | 3389 (default RDP port). |
| **Session** | Leave as default or select "Xorg" if prompted. |
| **Username & Password** | The credentials of the Ubuntu user you configured. |


You should now be presented with a responsive, high-performance XFCE desktop, giving you a full graphical interface on your cloud server without the resource overhead\!

![output](@/assets/images/Screenshot_20251030_154700.png)