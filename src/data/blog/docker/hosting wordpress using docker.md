---
title: Hosting wordpress website using just Docker in simple steps.
pubDatetime: 2025-09-22
featured: false
tags:
  - docker
  - Wordpress
  - Hands On Lab
description: Hosting wordpress website using just Docker in simple steps.

---

**simple step-by-step guide to host WordPress website using Docker**:

---

### **1. Install Docker & Docker Compose**

If not already installed:

```bash
sudo apt install docker.io docker-compose -y
sudo systemctl enable docker
sudo systemctl start docker
```
![output](@/assets/images/Screenshot_20250922_015723.png)

---

### **2. Create a Project Directory**

```bash
mkdir Docker-wordpress && cd Docker-wordpress
```

---

### **3. Create `docker-compose.yml`**

Make a file called `docker-compose.yml`:

```yaml
version: "3.9"

services:
  wordpress:
    image: wordpress:latest
    restart: always
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: janak
      WORDPRESS_DB_PASSWORD: janak0ff
      WORDPRESS_DB_NAME: janak
    volumes:
      - ./wordpress_data:/var/www/html

  db:
    image: mariadb:latest
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: janak0ff
      MYSQL_DATABASE: janak
      MYSQL_USER: janak
      MYSQL_PASSWORD: janak0ff
    volumes:
      - ./db_data:/var/lib/mysql

volumes:
  wordpress_data:
  db_data:
```

---

### **4. Start Containers**

```bash
docker-compose up -d
```
![output](@/assets/images/Screenshot_20250922_021256.png)


---

### **5. Access WordPress**

Open in browser:

```
http://192.168.63.132:8080
```
![output](@/assets/images/Screenshot_20250922_021604.png)
![output](@/assets/images/Screenshot_20250922_023921.png)



---

# Thank You
---

