---
title: Configure Bind9 as a Caching or Forwarding DNS Server on Ubuntu
pubDatetime: 2025-09-29
featured: false
tags:
  - Hands On Lab
  - Linux
  - NFS
description: Configure Bind as a Caching or Forwarding DNS Server on Ubuntu.
---

![output](@/assets/images/Screenshot_20251007_053150.png)



### Host Fixes for RDP (KDE Blank Screen Fix)**

This step fixes the common issue where RDP connects but immediately closes or shows a blank screen on KDE/Plasma environments.

1.  **Modify the xRDP Startup Script:** This tells xRDP exactly which desktop environment to launch.
    ```bash
    sudo nano /etc/xrdp/startwm.sh
    ```
2.  **Edit the Script:** Scroll to the bottom and **comment out** the two default startup lines, then **add** the `startplasma-x11` command:
    ```bash
    # test -x /etc/X11/Xsession && exec /etc/X11/Xsession
    # exec /bin/sh /etc/X11/Xsession

    # Add these lines for KDE
    startplasma-x11
    ```
3.  **Create `.xinitrc` File:** This ensures the session environment is initialized correctly for your user.
    ```bash
    nano ~/.xinitrc
    ```
    *Paste:*
    ```bash
    #!/bin/sh
    exec startplasma-x11
    ```
4.  **Restart xRDP Service:** Apply the session changes.
    ```bash
    sudo systemctl restart xrdp
    ```

-----


-----
I appreciate your patience\! We've hit a wall due to the **specific version and command structure** of your `cloudflared` installation. It appears your version of the `cloudflared` client does **not support the `--config` flag** with the `service install` command.

The older command structure is causing the "Incorrect Usage" error.

Since you've shown you can successfully run the tunnel using the correct configuration file manually, we will bypass the automated installation and **manually create the `systemd` service file.** This is a guaranteed fix.

-----

## 🛠️ Guaranteed Fix: Manual Systemd Service Creation

We will create a service file that explicitly tells the operating system to run `cloudflared` using your user's configuration file.

### 1\. Stop the Foreground Tunnel (If Running)

Make sure you've pressed **Ctrl + C** in the terminal where the tunnel was running.

### 2\. Create the Service File

You need to create a new file for the service definition.

**On the Host Machine:**

```bash
sudo nano /etc/systemd/system/cloudflared-remote.service
```

### 3\. Paste the Service Configuration

Paste the following configuration into the file. **This file is configured specifically for your setup:**

  * It uses your username (`janak`).
  * It points directly to your configuration file (`/home/janak/.cloudflared/config.yml`).
  * It uses the correct tunnel name (`remote-ssh`).

<!-- end list -->

```ini
[Unit]
Description=Cloudflare Tunnel Remote SSH Service
After=network.target

[Service]
# Set the user and group to run the tunnel as
User=janak
# The main executable. We use 'tunnel run' with the name of your tunnel.
ExecStart=/usr/local/bin/cloudflared tunnel run remote-ssh
# Ensure the service restarts if it fails
Restart=always
# Point the service to your existing config file
Environment="CLOUDFLARED_OPTS=--config /home/janak/.cloudflared/config.yml"
# Give up waiting if start takes too long
TimeoutStopSec=5

[Install]
WantedBy=multi-user.target
```

*Note: Make sure to verify the username `janak` is correct.*

Save the file and exit the editor.

### 4\. Enable and Start the Service

Now, tell `systemd` about the new service file, enable it for boot, and start it.

**On the Host Machine:**

```bash
# Reload the systemd manager configuration
sudo systemctl daemon-reload

# Enable the service to start automatically on boot
sudo systemctl enable cloudflared-remote.service

# Start the tunnel service
sudo systemctl start cloudflared-remote.service
```

### 5\. Verify the Status

Check that the service is running successfully in the background.

**On the Host Machine:**

```bash
sudo systemctl status cloudflared-remote.service
```

You should see **"Active: active (running)"**. You can now close your host terminal, and the tunnel will remain active.

After verifying the status, you should be able to connect via SSH from your client machine persistently\!


---

## 🛡️ 3. Stronger Authentication (SSH Keys)

Relying on a password is less secure than using SSH keys. Since your SSH server is now running, you should configure key-based authentication.

**On the Client Machine (Your Laptop):**

1.  **Generate a new SSH key pair** (if you don't already have one):

    ```bash
    ssh-keygen -t ed25519
    ```

2.  **Copy the public key** to your remote server:

    ```bash
    ssh-copy-id remote-ssh-janak
    ```

    *This command will prompt for your server password one last time and then install your public key (`~/.ssh/id_ed25519.pub`) into the `~/.ssh/authorized_keys` file on the remote server.*

After this, when you run `ssh remote-ssh-janak`, you will no longer be asked for a password, as your secure SSH key will handle the final authentication step automatically.

Would you like me to clarify any part of the Cloudflare Access setup or key management?

----