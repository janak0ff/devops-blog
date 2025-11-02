---
title: Secure SSH and RDP to Your Linux PC from Anywhere Using Cloudflare Tunnel
pubDatetime: 2025-11-02
featured: false
tags:
  - Hands On Lab
  - Linux
  - local ssh server
  - cloudflare
description: Secure SSH and RDP to Your Linux PC from Anywhere Using Cloudflare Tunnel
---

## 💻 Prerequisites

Before you start, make sure you have:

  * A **Cloudflare account**.
  * A **domain name** added to your Cloudflare account and using Cloudflare's nameservers.
  * **SSH server running** on your local PC (e.g., OpenSSH on Linux/macOS, or an SSH server on Windows) on the default port **22** (or your custom port).
  * On my local/host server firewall is inactive, if you have enable then add rules for tcp(22,3389 and 3000) ports.


### I am gonna do ssh

-----

## Host Setup – The Local Linux Server**

The Host Machine is your local PC that you want to access remotely.

### Install Cloudflare Tunnel (`cloudflared`) on you local/host server

The `cloudflared` daemon is the service that creates the secure tunnel.

1.  **Download and Install:** Use the appropriate package manager for your Linux distribution (e.g., Debian/Ubuntu): On the Host Machine
    ```bash
    wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
    sudo dpkg -i cloudflared-linux-amd64.deb
    ```
2.  **Verify Path:** Confirm the installation path.
    ```bash
    which cloudflared
    ```
  - Expected output: /usr/local/bin/cloudflared

### Install and Verify Services (SSH & RDP) on you local/host server

We must ensure the services are installed and listening locally before the tunnel can expose them.

#### OpenSSH Server

1. Install OpenSSH server:
   ```
   sudo apt update
   sudo apt install openssh-server -y
   ```
2. Enable and start the SSH service:
   ```
   sudo systemctl enable --now ssh
   ```
3. Verify SSH service status:
   ```bash
   sudo systemctl restart ssh
   # OR
   sudo systemctl restart sshd
   ```
   You should see the service as active (running).

#### XRDP

1. Install xrdp:
   ```
   sudo apt update
   sudo apt install xrdp -y
   ```
2. Add xrdp user to ssl-cert group for certificate access:
   ```
   sudo adduser xrdp ssl-cert
   ```
3. Enable and start the xrdp service:
   ```
   sudo systemctl enable --now xrdp
   ```
4. Verify xrdp service status:
   ```
   sudo systemctl status xrdp
   ```
   You should see it active (running).

This will set up SSH server for remote terminal access on port 22 and xrdp for remote desktop protocol (RDP) access on port 3389 on your linux machine. Both services will be enabled to start automatically on system boot.|

Run the following command to check the service on specifed port.

```bash
sudo ss -tuln | grep -E ':22 |:3389 |:3000 '
sudo ss -tuln | grep 22
```


### Create the Named Tunnel and Configuration**

1.  **Authenticate Cloudflared:**
    This opens a browser. Log in to your Cloudflare account, authorize and save cert.pem.
    ```bash
    cloudflared tunnel login
    ```
2.  **Create a new tunnel. You can name it whatever you like (`remote-ssh`):**
    ```bash
    cloudflared tunnel create remote-ssh
    ```
   This generates your UUID (tunnel ID) (e.g., bbfb870f-c972-...) and JSON credentials inside /home/USERNAME/.cloudflared/.



3.  **Create/Edit `config.yml`:** Define the hostnames and the services they map to.
    ```bash
    nano ~/.cloudflared/config.yml
    ```
    *Paste your configuration (substituting your UUID):*
    ```yaml
    #tunnel: YOUR_TUNNEL_ID
    tunnel: bbfb870f-c972-4653-97af-41667bd5cb71  # Your Tunnel UUID
    #credentials-file: /home/YOUR_USERNAME/.cloudflared/YOUR_TUNNEL_ID.json
    credentials-file: /home/janak/.cloudflared/bbfb870f-c972-4653-97af-41667bd5cb71.json # Give path acccording to yours  
    ingress:
      - hostname: ssh.janakkumarshrestha0.com.np # for ssh server
        service: ssh://localhost:22
      - hostname: desktop.janakkumarshrestha0.com.np # For remote desktop
        service: tcp://localhost:3389    
      - hostname: localnode.janakkumarshrestha0.com.np # For node app
        service: tcp://localhost:3000
      #If you have any other services on local host, go on like this...
      - service: http_status:404
    ```

----

### DNS Configuration - **Create DNS Records (Cloudflare)**

You need to tell Cloudflare to route traffic from your chosen hostname to the tunnel.

- ##### Using the cloudflared CLI (Recommended) - The easiest way to create the correct DNS record is by running the command from your terminal
```bash
cloudflared tunnel route dns remote-ssh ssh.janakkumarshrestha0.com.np # for ssh server
cloudflared tunnel route dns remote-ssh desktop.janakkumarshrestha0.com.np # For remote desktop
cloudflared tunnel route dns remote-ssh localnode.janakkumarshrestha0.com.np # For node app
```
This command automatically creates the correct CNAME record in your Cloudflare DNS, pointing your all hostname to the tunnel named remote-ssh.

### OR

- ##### Alternatively - Adding dns record manually 
Go to your Cloudflare DNS settings and add the CNAME records.

1.  **Add CNAME for SSH:**
      * **Name:** `ssh`
      * **Target:** `[YOUR-TUNNEL-UUID].cfargotunnel.com`
      * **Proxy Status:** **Proxied (Orange Cloud)**
2.  **Add CNAME for RDP:**
      * **Name:** `desktop`
      * **Target:** `[YOUR-TUNNEL-UUID].cfargotunnel.com`
      * **Proxy Status:** **Proxied (Orange Cloud)**
3.  **Add CNAME for local node app:**
      * **Name:** `localnode`
      * **Target:** `[YOUR-TUNNEL-UUID].cfargotunnel.com`
      * **Proxy Status:** **Proxied (Orange Cloud)**

----

### Run the Tunnel
Start the tunnel service so it can connect to the Cloudflare network and begin listening for traffic:

```bash
cloudflared tunnel run remote-ssh # Replace with you tunnel name
```

  * Keep this process running, as it maintains the connection between your local PC and the Cloudflare edge.

----

### Client Configuration the SSH Client (Client Machine on different network)

On the PC you're connecting **from** (your remote client or there pc on different networks), you need to install `cloudflared` and configure your SSH client to use it as a proxy.

```bash
sudo apt update
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb
which cloudflared
```
 **Edit your SSH configuration file** (on Linux/macOS, or a similar configuration on Windows tools like PuTTY).
1.  **Edit `~/.ssh/config`:**
    ```bash
    nano ~/.ssh/config
    ```
2.  **Add SSH Configuration:**
    ```ini
    Host remote-ssh-janak # Give host name you like
      Hostname ssh.janakkumarshrestha0.com.np   # Replace with you actual host name.
      # The key line that uses cloudflared to proxy the connection
      ProxyCommand /usr/local/bin/cloudflared access ssh --hostname %h
      User janak  # Replace with the username on the local server / host machine.

      # (Optional) Use a specific port if your server isn't on default port, otherwise, this line isn't necessary
      # Port 22
    ```
    * The `ProxyCommand` tells the SSH client to route the connection through `cloudflared`, which handles the tunnel authentication. Replace or match the ouptput form `which cloudflared` command in `/usr/local/bin/cloudflared` path.
    Note: Make sure the path to cloudflared (`/usr/local/bin/cloudflared`) is correct for your client machine's installation. Check using this command `which cloudflared` and match.

3.  **Connect via SSH**

You can now connect to your local PC from anywhere on the internet using the simplified SSH command from the client machine:

```bash
ssh remote-ssh-janak
# or
ssh -vvv remote-ssh-janak
```

  * The first time, you may be prompted to authenticate with Cloudflare Access (e.g., a browser login). After that, you will be prompted for your local PC's SSH password or key.
-----

## Final Security and Persistence**


#### **If you want to  Make the Tunnel Permanent/auto start on boot (Host Machine)**

1.  **Stop Foreground:** If running, stop the tunnel (Ctrl+C).
2.  **Create and Start Service:** (Uses your existing service definition)
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start cloudflared-remote.service
    sudo systemctl enable cloudflared-remote.service
    ```

#### **Step 7: Apply Zero Trust Access Policies**

You must secure both new hostnames in your Cloudflare Zero Trust Dashboard $\to$ **Access** $\to$ **Applications**, creating a separate **Self-hosted Application** for:

  * `ssh.janakkumarshrestha0.com.np`
  * `desktop.janakkumarshrestha0.com.np`

For both, set the **Access Policy** to **Allow** only your verified **Email Address**.

-----

### **Phase 6: Connection Methods**

| Protocol | Purpose | Client Command/Action |
| :--- | :--- | :--- |
| **SSH** (Command Line) | Secure terminal access. | **`ssh remote-ssh-janak`** |
| **RDP** (Remote Desktop) | Graphical desktop access. | **1. Run Proxy (Terminal):** `cloudflared access tcp --hostname desktop.janakkumarshrestha0.com.np --url 127.0.0.1:33389` **2. Connect RDP Client:** Target `127.0.0.1:33389` |

Your system is now fully set up for secure, persistent, multi-protocol remote access\!