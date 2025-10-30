---
title: Install KDE Plasma and Remote Desktop (XRDP) on Ubuntu Server
pubDatetime: 2025-10-29
featured: false
tags:
  - Hands On Lab
  - Linux
  - xrdp
description: Install KDE Plasma and Remote Desktop (XRDP) on Ubuntu Server
---

***

# Ultimate Guide: How to Install KDE Plasma and Remote Desktop (XRDP) on Ubuntu Server

Are you running an Ubuntu Server times you just need a full graphical desktop for better visualization, running specific and tired of managing everything through the command line? While the CLI is powerful, some applications, or simply a more familiar environment.

This guide will walk you through transforming your minimal Ubuntu Server into a fully functional, **remotely accessible** workstation using the beautiful and feature-rich **KDE Plasma Desktop Environment** and the **XRDP** server.

-----

## Prerequisites

Before we start, ensure you have the following:

  * **A running Ubuntu Server** (Any recent LTS version, like 22.04 or 24.04).
  * **SSH Access** (You'll perform all initial steps via SSH or the local TTY console).
  * **Sudo Privileges** (You must be a user with administrative rights).
  * **An RDP Client** (Like **Remmina** on Linux, **Microsoft Remote Desktop** on Windows, or the equivalent on macOS).

-----

##  Phase 1: Prepare the Server

The first step is always to ensure your system is up-to-date and ready for the new packages.

### Check and Update the Server

Log in to your server via SSH and execute the following commands:

```bash
# Update the package lists
sudo apt update

# Upgrade all installed packages to their latest versions
sudo apt upgrade -y
```

This ensures a clean installation and avoids potential conflicts with outdated libraries.

### Install Essential Tools (Optional but Recommended)

You might need some fundamental utilities during the process:

```bash
# Install wget and net-tools (for network diagnostics)
sudo apt install wget net-tools -y
```

-----

## Phase 2: Install and Configure KDE Plasma

You have a few options for installing the KDE Plasma desktop environment, ranging from a minimal setup to a full-featured desktop.

### Option A: Full Kubuntu Desktop (Recommended for most users)

This installs the complete KDE Plasma desktop environment along with the standard set of applications (web browser, office suite, media players, etc.), similar to a fresh Kubuntu installation.

```bash
sudo apt install kubuntu-desktop -y
```

### Option B: Basic KDE Plasma Desktop

This installs the KDE Plasma environment with a minimal set of necessary components. It's lighter but requires you to manually install additional applications later.

```bash
sudo apt install kde-plasma-desktop -y
```

### Option C: Minimal Plasma Core

This is the most barebones installation, installing only the core components of the Plasma shell and a display manager. It's intended for advanced users who want maximum control over every installed package.

```bash
sudo apt install plasma-desktop -y
```

**Note:** The installation process may take some time depending on your chosen option and internet speed. You will be prompted to choose a **Display Manager** (like `sddm` or `lightdm`). **`sddm`** is the recommended display manager for KDE Plasma. Use the arrow keys to select, and **Enter** to confirm.


### Set the System to Graphical Target

After installation, your server is still set to boot into command-line mode (`multi-user.target`). We need to switch it to boot into the graphical mode (`graphical.target`).

```bash
# Set the system to boot into graphical mode by default
sudo systemctl set-default graphical.target
```

-----

## Phase 3: Install and Configure XRDP for Remote Access

Since Ubuntu Server doesn't come with an RDP solution, we will install **XRDP** to enable connections from your Remmina client.

### Install the XRDP Server

XRDP is the open-source implementation of the Microsoft Remote Desktop Protocol.

```bash
# Install the XRDP package
sudo apt install xrdp -y
```

### Configure XRDP for KDE Plasma

XRDP often defaults to other desktop environments, so we need to configure it to launch the KDE Plasma session specifically.

1.  **Create/Edit the configuration file:**
    ```bash
    echo startplasma-x11 > ~/.xsession
    ```
2.  **Add the XRDP user to the `ssl-cert` group** (essential for secure operation):
    ```bash
    sudo adduser xrdp ssl-cert
    ```

### Adjust UFW Firewall Settings

The firewall (UFW) blocks all incoming connections by default. We must explicitly open the standard RDP port **3389**.

```bash
# Allow traffic on the default RDP port (3389)
sudo ufw allow 3389/tcp

# Check the firewall status to verify the rule
sudo ufw status
```

You should see an entry like `3389/tcp ALLOW Anywhere`.

### Start and Enable the XRDP Service

Finally, ensure the XRDP service is active and will start automatically after any future reboots.

```bash
# Enable the service to start on boot
sudo systemctl enable xrdp

# Restart the service to apply all new changes
sudo systemctl restart xrdp
```

-----

## Phase 4: Final Reboot and Connect via Remmina

You are now ready to connect\!

###  Reboot the Server

This is a critical step to ensure all system-level changes are fully applied.

```bash
# Reboot the entire system
sudo reboot
```

### Connect with Remmina (or other RDP Client)

On your local machine, open your RDP client:

1.  **Protocol:** Choose **RDP**.
2.  **Server/IP:** Enter the **IP address** of your Ubuntu Server.
3.  **Connect.**
4.  At the XRDP login screen, enter your **Ubuntu Server username and password**.

You should now see the beautiful **KDE Plasma** desktop environment, fully accessible remotely\!

![output](@/assets/images/Screenshot_20251029_132622.png)
![output](@/assets/images/Screenshot_20251029_132919.png)
![output](@/assets/images/Screenshot_20251029_133014.png)

-----

##  Troubleshooting

| Issue | Solution | Command to Run on Server (via SSH) |
| :--- | :--- | :--- |
| **Connection Refused** | XRDP is not running or the firewall is blocking it. | `sudo systemctl status xrdp` (to check) `sudo ufw allow 3389/tcp` (to open port) |
| **Shows CLI after reboot** | The system is still set to boot to the CLI target. | `sudo systemctl set-default graphical.target` `sudo reboot` |
| **Black/Grey Screen on Connect** | XRDP is starting a broken or incorrect session. | `echo startplasma-x11 > ~/.xsession` `sudo systemctl restart xrdp` |

-----
