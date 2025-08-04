---
title: Django Todo App Deployment - EC2, Virtual Environments, and Docker 
pubDatetime: 2025-07-25
featured: true
tags:
  - aws
  - Hands On Lab

description: guiding you through deploying your Django todo app on an AWS EC2 instance, covering both traditional virtual environment setup and containerization with Docker.
---

So, you've built a fantastic Django todo app, and it's running perfectly on your local machine. Now, you're ready to share it with the world by deploying it to a cloud server\! **AWS EC2**

----



### 1\. Connect to Your EC2 Instance via SSH

  **Connect:**
    ```bash
     ssh -i ~/.ssh/aws-janak.pem  ubuntu@13.221.102.188
    ```

### 2\. Prepare the EC2 Server Environment

Once connected via SSH to your EC2 instance:

1.  **Update System Packages:**

    ```bash
    sudo apt update
    sudo apt upgrade -y
    ```

2.  **Install Essential Software:**

    ```bash
    sudo apt install python3-pip python3.12-venv docker.io -y
    ```

      * `python3-pip`: Python's package installer.
      * `python3.12-venv`: For creating isolated Python environments.
    

-----

## Part 2: Deploying with a Python Virtual Environment 🐍

This is a straightforward way to get your app running without Docker.

### 1\. Clone Your Django Project

On your **EC2 instance's terminal**:

  **Clone your project:**
    ```bash
    git clone https://github.com/shreys7/django-todo.git
    cd django-todo
    ```

### 2\. Create and Activate Virtual Environment (on EC2)

1.  **Create:**
    ```bash
    python3 -m venv venv
    ```
2.  **Activate:**
    ```bash
    source venv/bin/activate
    ```
    Your prompt should now show `(venv)` at the beginning, indicating the virtual environment is active.

### 4\. Install Dependencies

1.  **Install from `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```
    *If `pip` command doesn't work directly (e.g., `Command 'pip' not found`), use `python3 -m pip install -r requirements.txt` instead.*

### 5\. Configure Django Settings

You need to tell Django about your EC2 instance's public IP and prepare it for a production-like environment.

1.  **Open `settings.py`:**
    ```bash
    nano todoApp/settings.py
    ```
    *(Replace `todoApp` with your actual main Django project folder name if different).*
2.  **Set `DEBUG = False`:**
    Find `DEBUG = True` and change it to:
    ```python
    DEBUG = False
    ```
    **Never run with `DEBUG = True` in production\! It exposes sensitive information.**
3.  **Add your EC2 Public IP to `ALLOWED_HOSTS`:**
    Find `ALLOWED_HOSTS = []` and add your instance's public IP.
    ```python
    ALLOWED_HOSTS = ['your_instance_public_ip']
    # Example: ALLOWED_HOSTS = ['52.202.151.15']
    ```
    If you get a domain name later, add it here too: `['your_instance_public_ip', 'your-domain.com']`.
4.  **Configure `STATIC_ROOT`:**
    Ensure these lines are present (add `import os` at the top if missing):
    ```python
    import os
    # ... other settings ...
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    ```
5.  **Save and Exit:** Press `Ctrl+X`, then `Y`, then `Enter`.

### 6\. Prepare Database and Static Files

1.  **Collect Static Files:**
    ```bash
    python3 manage.py collectstatic
    ```
    Type `yes` when prompted. This gathers all static assets (CSS, JS, images) into the `staticfiles` folder.
2.  **Apply Migrations:**
    ```bash
    python3 manage.py makemigrations # Only needed if you made model changes
    python3 manage.py migrate
    ```
3.  **Create Superuser (Optional):**
    ```bash
    python3 manage.py createsuperuser
    ```

### 7\. Test with Django's Development Server (Temporary)

This is just to confirm your app runs before setting up production servers.

1.  **Run the server:**
    ```bash
    python3 manage.py runserver 0.0.0.0:8000
    ```
    You'll see warnings about it being a development server, which is expected.
2.  **Access in browser:** Open your browser and go to `http://your_instance_public_ip:8000/`.
    *If you get a `DisallowedHost` error, double-check that your EC2 Public IP is correctly added to `ALLOWED_HOSTS` in `settings.py`.*
    *Make sure **Port 8000** is open in your EC2 instance's Security Group (as set up in Part 1).*

### 8\. Run in Background with `nohup` (Temporary)

To keep the development server running even after you close your SSH session:

1.  **Stop the current `runserver`** (if running) by pressing `Ctrl+C`.
2.  **Run with `nohup`:**
    ```bash
    nohup python3 manage.py runserver 0.0.0.0:8000 &
    ```
    You'll see a message about output being redirected to `nohup.out`. You can check it with `tail -f nohup.out`.
    *To stop it later: `ps aux | grep 'runserver' | grep -v 'grep'` to find the PID, then `kill <PID>`.*

-----

## Part 3: Containerizing with Docker (Optional, but Recommended) 🐳

Docker provides a consistent and isolated environment for your app, making deployments more reliable.

### 1\. Ensure Dockerfile and .dockerignore are Ready

You mentioned you already have your `Dockerfile` and `.dockerignore` files. Make sure they are in the root of your Django project.

  * Your `.dockerignore` file should exclude unnecessary files like `venv/`, `__pycache__/`, `.git/`, `db.sqlite3`, etc.
  * Your `Dockerfile` should look something like this (you've already confirmed you have it):
    ```dockerfile
    FROM python:3
    RUN pip install django==5.2.4
    COPY . .
    RUN python3 manage.py migrate
    CMD ["python3","manage.py", "runserver", "0.0.0.0:8001"]
    ```
    *(Remember, for production, you'd typically use `pip install -r requirements.txt` and `gunicorn` as the `CMD`.)*

### 2\. Build the Docker Image

On your **EC2 instance**, in your project's root:

```bash
sudo docker build -t django-todo-app .
```

  * This command reads your `Dockerfile` and creates a Docker image named `django-todo-app`.

### 3\. Run the Docker Container

To run your app in a Docker container in the background:

```bash
sudo docker run -d -p 8001:8001 django-todo-app
```

  * `-d`: Runs the container in "detached" (background) mode.
  * `-p 8001:8001`: Maps port 8001 on your EC2 instance (host) to port 8001 inside the container.

### 4\. Verify and Access Your Dockerized App

1.  **Check if the container is running:**
    ```bash
    sudo docker ps
    ```
    You should see your `django-todo-app` container listed with a `Status` of "Up...".
2.  **Access in browser:** Ensure **Port 8001** is open in your EC2 Security Group. Then, open your web browser and go to `http://your_instance_public_ip:8001/`.

-----

## What's Next for Production? 🚀

While your app is now accessible, remember the warnings about using the Django development server. For a truly production-ready setup, you would:

1.  **Replace `runserver` with Gunicorn:** Update your `Dockerfile`'s `CMD` to use Gunicorn.
2.  **Implement Nginx as a Reverse Proxy:** Configure Nginx on your EC2 instance to serve static files directly and forward dynamic requests to Gunicorn. This is crucial for performance and security.
3.  **Use a Production Database:** Migrate from SQLite to a robust database like PostgreSQL, ideally using AWS RDS for managed services.
4.  **Set up HTTPS (SSL/TLS):** Secure your application with an SSL certificate (e.g., using Certbot with Let's Encrypt).
5.  **Environment Variables:** Store sensitive data (like Django's `SECRET_KEY`, database credentials) using environment variables or AWS Secrets Manager, not directly in `settings.py`.

Congratulations\! You've successfully deployed your Django todo app to an AWS EC2 instance using both a virtual environment and Docker for testing. This is a huge step in your cloud journey\!
\</immersive\>