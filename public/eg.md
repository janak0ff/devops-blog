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

***


### Alternative 1: LXQt (The Minimalist Choice)

LXQt is the result of the merger between LXDE and Razor-Qt projects. It is arguably the **lightest** full desktop environment available, making it perfect for your smallest cloud instances.

#### Installation Steps for LXQt

1.  **Install LXQt and XRDP:**

    ```bash
    sudo apt update
    sudo apt install lxqt xrdp -y
    ```

    *Note: The `sddm` display manager may be installed as a dependency. It's safe to accept the default prompts.*

2.  **Configure XRDP to use LXQt:**
    Create or edit the `.xsession` file to launch the LXQt session:

    ```bash
    echo startlxqt > ~/.xsession
    ```

3.  **Set permissions and restart XRDP:**

    ```bash
    sudo chown -R $USER:$USER /home/$USER/.xsession
    sudo systemctl restart xrdp
    ```

### Alternative 2: MATE (The Traditionalist's Choice)

MATE is a continuation of the classic **GNOME 2** desktop environment. It offers a very traditional, intuitive user experience that is extremely stable and requires moderate resources—more than LXQt, but still significantly less than the default GNOME or KDE.

#### Installation Steps for MATE

1.  **Install MATE Desktop and XRDP:**

    ```bash
    sudo apt update
    sudo apt install ubuntu-mate-desktop xrdp -y
    ```

2.  **Configure XRDP to use MATE:**
    Create or edit the `.xsession` file to launch the MATE session:

    ```bash
    echo mate-session > ~/.xsession
    ```
