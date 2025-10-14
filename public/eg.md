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


Here is the completed table explaining the commands, which are useful for troubleshooting and verifying your server's IP address and DNS resolution:


***

### Additional Useful Commands for Server Verification

| Command | Explanation |
| :--- | :--- |
| `sudo netstat -tulnp | grep :53` | Checks if the BIND service (`named`) is actively listening for connections on the standard DNS **port 53** for both TCP and UDP protocols. |
| `sudo systemctl status nginx` | Checks the running status of the Nginx web server to ensure it is **active (running)** and serving web content. |
| `curl http://127.0.0.1` | **Internal Web Test:** Requests your `index.html` page directly from the Nginx server on the local machine. This tests your Nginx configuration without relying on DNS or firewall rules. |
| `dig @10.10.1.20 janakkumarshrestha0.com.np` | **Specific DNS Test:** Forces the query to be sent only to your server's private IP, bypassing the default system resolver. This is the best way to test BIND directly from another internal machine. |