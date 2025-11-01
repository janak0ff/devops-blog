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

3.  **Install the Desktop Environment and Configure:**
    **Configure the user's session:**
    Create or edit the `.xsession` file in the home directory of the user you will use to connect. This file tells XRDP which desktop to launch.

---

- Install XFCE DEs:
```bash
sudo apt install xfce4 -y 
sudo apt install xubuntu-desktop -y # The full Xubuntu experience.
```

```bash
echo xfce4-session > ~/.xsession
echo startxfce4 > ~/.xsession
```

![output](@/assets/images/Screenshot_20251031_172654.png)


---

- Install LXQt DEs:
```bash
sudo apt install lxqt -y # The full Lubuntu (now LXQt-based) experience.
sudo apt install lubuntu-desktop -y # The full Lubuntu (now LXQt-based) experience.
```

```bash
echo startlxqt > ~/.xsession
```
![output](@/assets/images/Screenshot_20251031_165528.png)

---

- Install MATE DEs:
```bash
sudo apt install ubuntu-mate-desktop -y # The full Ubuntu MATE experience.
sudo apt install mate-desktop-environment -y # A more standard MATE install.
sudo apt install mate-session-manager -y # Installs the core session manager.
```

```bash
echo mate-session > ~/.xsession
```

![output](@/assets/images/Screenshot_20251031_171435.png)

---

- Install Cinnamon DEs:
```bash
sudo apt install cinnamon-desktop-environment -y # Standard Cinnamon installation.
sudo apt install cinnamon -y # Installs the core Cinnamon package.
```

```bash
echo cinnamon-session > ~/.xsession
```

![output](@/assets/images/Screenshot_20251031_173606.png)

---

- Install Enlightenment (E) DEs:
```bash
sudo apt install enlightenment -y # A unique, lightweight, and fast DE/WM.
```

```bash
echo enlightenment_start > ~/.xsession
```

![output](@/assets/images/Screenshot_20251031_174205.png)

---

- Install Gnome DEs:
```bash
sudo apt install ubuntu-desktop -y # The full, default Ubuntu experience.
sudo apt install gnome-session # Installs the core session manager.
sudo apt install gnome-core # Installs a minimal GNOME experience.
```
```bash
echo gnome-session > ~/.xsession
```

![output](@/assets/images/Screenshot_20251101_110535.png)

---

- Install KDE Plasma DEs:
```bash
sudo apt install kubuntu-desktop -y # The full Kubuntu experience.
sudo apt install plasma-desktop # Installs a more basic version of Plasma.
sudo apt install gkde-plasma-desktop # Minimal
```
```bash
echo startplasma-x11 > ~/.xsession
```

![output](@/assets/images/Screenshot_20251101_123423.png)

---

2.  **Set correct permissions** for the `.xsession` file:

    ```bash
    sudo chown -R $USER:$USER /home/$USER/.xsession
    ```

3.  **Restart the XRDP service** to load the new configuration:

    ```bash
    sudo systemctl restart xrdp
    ```

-----

## Step 3: Configure the Firewall

The default RDP port is **3389**. You must open this port in your server's firewall to allow incoming connections.

If you are using **UFW (Uncomplicated Firewall)**, run this command:

```bash
sudo ufw allow 3389/tcp
sudo ufw enable
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

