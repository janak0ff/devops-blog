---
title: Module 2 - Introduction to Linux Commands
pubDatetime: 2025-05-20
tags:
  - Linux Introduction
  - Introduction
description: Learn how to use common Linux commands. what a shell and shell commands are, and how to use commands to do various tasks in Linux. How to use informational commands to find relevant information about your system, navigation commands to navigate files and directories, and management commands to create, delete, copy, and move files and directories. Learn to sort and view files in useful ways and extract specific lines and fields from your files. Use networking commands to examine your network configuration and evaluate, identify, and retrieve data from URLs. Cover file archiving and compression commands.
---

# **Overview of Common Linux Shell Commands**

---

## **1. What is a Shell?**

### **Definition**

A **shell** is a powerful **command-line interpreter** used in Unix-like operating systems (like Linux and macOS).

- It acts as both:
  - An **interactive command language** for users to interact with the OS.
  - A **scripting language** for automating tasks.

### **Common Shells in Linux**

| Shell                  | Description                                        |
| ---------------------- | -------------------------------------------------- |
| **Bash** (`/bin/bash`) | Bourne Again SHell – Default on most Linux distros |
| **sh**                 | Original Bourne shell                              |
| **ksh**                | KornShell – Enhanced version of sh                 |
| **tcsh**               | Extended C Shell with advanced features            |
| **zsh**                | Z Shell – Modern, feature-rich                     |
| **fish**               | Friendly Interactive SHell – beginner-friendly     |

> In this course, we will use **Bash**, the default shell on most Linux systems.

### **How to Check Your Current Shell**

```bash
printenv SHELL
```

Example output:

```
/bin/bash
```

If not Bash, you can switch by typing:

```bash
bash
```

---

## **2. Applications of Shell Commands**

Shell commands are essential for various tasks such as:

| Task Category              | Examples                           |
| -------------------------- | ---------------------------------- |
| **System Info**            | `uname`, `date`, `whoami`          |
| **File Management**        | `cp`, `mv`, `rm`, `touch`          |
| **Directory Navigation**   | `ls`, `cd`, `pwd`, `mkdir`         |
| **Text Display**           | `cat`, `head`, `tail`, `echo`      |
| **Search & Filter**        | `grep`, `find`                     |
| **Compression**            | `tar`, `zip`, `unzip`              |
| **Networking**             | `curl`, `wget`, `ping`, `hostname` |
| **Performance Monitoring** | `top`, `ps`, `df`                  |

---

## **3. Common Shell Commands**

### **A. System Information Commands**

| Command         | Description                          |
| --------------- | ------------------------------------ |
| `whoami`        | Displays current username            |
| `id`            | Shows user and group IDs             |
| `uname`         | Displays OS name and version         |
| `ps`            | Lists running processes              |
| `top`           | Real-time system monitoring tool     |
| `df`            | Shows disk space usage               |
| `man [command]` | Displays manual/help for any command |
| `date`          | Prints current date and time         |

---

### **B. File Management Commands**

| Command                  | Description                              |
| ------------------------ | ---------------------------------------- |
| `cp file1 file2`         | Copy files or directories                |
| `mv file1 file2`         | Move or rename files                     |
| `rm file`                | Remove/delete a file                     |
| `touch file`             | Create an empty file or update timestamp |
| `chmod permissions file` | Change file access permissions           |
| `wc file`                | Count lines, words, characters in a file |
| `grep "pattern" file`    | Search for text within a file            |

---

### **C. Directory Navigation Commands**

| Command                | Description                        |
| ---------------------- | ---------------------------------- |
| `ls`                   | List contents of current directory |
| `find . -name "*.txt"` | Find files matching a pattern      |
| `pwd`                  | Print working (current) directory  |
| `mkdir dir_name`       | Make a new directory               |
| `cd dir_name`          | Change to another directory        |
| `rmdir dir_name`       | Remove an empty directory          |

---

### **D. File Content Viewing Commands**

| Command         | Description                               |
| --------------- | ----------------------------------------- |
| `cat file.txt`  | Concatenate and print full file content   |
| `more file.txt` | View file content one page at a time      |
| `head file.txt` | Show first few lines of a file            |
| `tail file.txt` | Show last few lines of a file             |
| `echo "text"`   | Print text or variable values to terminal |

---

### **E. File Compression & Archiving**

| Command                            | Description                |
| ---------------------------------- | -------------------------- |
| `tar -cvf archive.tar file1 file2` | Archive files into `.tar`  |
| `tar -xvf archive.tar`             | Extract from `.tar` file   |
| `zip archive.zip file1 file2`      | Compress files into `.zip` |
| `unzip archive.zip`                | Extract `.zip` archive     |

---

### **F. Networking Commands**

| Command                            | Description                          |
| ---------------------------------- | ------------------------------------ |
| `hostname`                         | Show system hostname                 |
| `ping google.com`                  | Test network connectivity            |
| `ifconfig`                         | Configure or view network interfaces |
| `curl http://example.com`          | Transfer data from a URL             |
| `wget http://example.com/file.txt` | Download files from the web          |

---

## **4. Running Linux on Windows**

You can run Linux commands on a Windows machine using these methods:

| Method                                | Description                                            |
| ------------------------------------- | ------------------------------------------------------ |
| **Dual Boot**                         | Install Linux alongside Windows on separate partitions |
| **Virtual Machine (VM)**              | Run Linux inside a VM like VirtualBox or VMware        |
| **Linux Emulator (e.g., Cygwin)**     | Run Linux tools in a simulated environment             |
| **Windows Subsystem for Linux (WSL)** | Native Linux compatibility layer on Windows 10/11      |

---

## **5. Summary**

✅ The **role of a shell** in Linux as both a command interpreter and scripting tool.  
✅ How to **check and switch shells** using commands like `printenv SHELL` and `bash`.  
✅ The **main applications** of shell commands across system info, file management, networking, and automation.  
✅ The **most common shell commands** grouped by function for easy reference.

---

## **Quick Reference Table**

| Purpose            | Command                                        |
| ------------------ | ---------------------------------------------- |
| **User Info**      | `whoami`, `id`                                 |
| **System Info**    | `uname`, `date`, `top`, `df`                   |
| **File Ops**       | `cp`, `mv`, `rm`, `touch`, `chmod`, `grep`     |
| **Dir Navigation** | `ls`, `cd`, `pwd`, `mkdir`, `rmdir`, `find`    |
| **View Content**   | `cat`, `head`, `tail`, `more`, `echo`          |
| **Compression**    | `tar`, `zip`, `unzip`                          |
| **Networking**     | `curl`, `wget`, `ping`, `hostname`, `ifconfig` |

---

---

# 🔧 **Linux Shell Commands Cheat Sheet**

> This cheat sheet includes **common Linux shell commands**, their **syntax**, and **examples**. Designed for quick reference and learning.

---

## 🧑‍💻 Basic Navigation

| Command    | Description                     | Example                        |
| ---------- | ------------------------------- | ------------------------------ |
| `pwd`      | Print Working Directory         | `pwd` → `/home/user/documents` |
| `cd <dir>` | Change Directory                | `cd /home/user`                |
| `ls`       | List files in current directory | `ls`                           |
| `ls -l`    | Long listing format             | `ls -l`                        |
| `ls -a`    | Show hidden files               | `ls -a`                        |

---

## 🗂️ File & Directory Management

| Command           | Description               | Example               |
| ----------------- | ------------------------- | --------------------- |
| `touch <file>`    | Create an empty file      | `touch myfile.txt`    |
| `mkdir <dir>`     | Make a new directory      | `mkdir myfolder`      |
| `cp <src> <dest>` | Copy files/dirs           | `cp file.txt backup/` |
| `mv <src> <dest>` | Move or rename files      | `mv old.txt new.txt`  |
| `rm <file>`       | Remove/delete a file      | `rm temp.txt`         |
| `rm -r <dir>`     | Remove a directory        | `rm -r myfolder`      |
| `rmdir <dir>`     | Remove an empty directory | `rmdir empty_folder`  |

---

## 📄 Viewing and Editing Files

| Command                  | Description            | Example                    |
| ------------------------ | ---------------------- | -------------------------- |
| `cat <file>`             | View entire file       | `cat myfile.txt`           |
| `more <file>`            | View file page by page | `more bigfile.txt`         |
| `head <file>`            | Show first 10 lines    | `head myfile.txt`          |
| `tail <file>`            | Show last 10 lines     | `tail myfile.txt`          |
| `nano <file>`            | Edit file using nano   | `nano notes.txt`           |
| `echo "<text>" > <file>` | Write text to a file   | `echo "Hello" > hello.txt` |

---

## 🔍 Searching and Filtering

| Command                         | Description                    | Example                |
| ------------------------------- | ------------------------------ | ---------------------- |
| `grep "<pattern>" <file>`       | Search for pattern in file     | `grep "error" log.txt` |
| `find <path> -name "<pattern>"` | Find files matching name       | `find . -name "*.log"` |
| `wc <file>`                     | Count lines, words, characters | `wc myfile.txt`        |

---

## 🧰 System Information

| Command    | Description               | Example    |
| ---------- | ------------------------- | ---------- |
| `whoami`   | Show current user         | `whoami`   |
| `id`       | Show user and group IDs   | `id`       |
| `uname -a` | Show OS info              | `uname -a` |
| `date`     | Show current date/time    | `date`     |
| `top`      | Real-time process monitor | `top`      |
| `df -h`    | Disk space usage          | `df -h`    |
| `ps`       | List running processes    | `ps`       |

---

## 📦 Compression & Archiving

| Command                          | Description         | Example                     |
| -------------------------------- | ------------------- | --------------------------- |
| `tar -cvf <archive.tar> <files>` | Create tar archive  | `tar -cvf backup.tar *.txt` |
| `tar -xvf <archive.tar>`         | Extract tar archive | `tar -xvf backup.tar`       |
| `zip <archive.zip> <files>`      | Compress files      | `zip docs.zip *.docx`       |
| `unzip <archive.zip>`            | Extract zip archive | `unzip docs.zip`            |

---

## 🌐 Networking

| Command       | Description                            | Example                            |
| ------------- | -------------------------------------- | ---------------------------------- |
| `hostname`    | Show system hostname                   | `hostname`                         |
| `ping <host>` | Test network connection                | `ping google.com`                  |
| `ifconfig`    | Show network interfaces _(deprecated)_ | `ifconfig`                         |
| `ip addr`     | Alternative to ifconfig                | `ip addr show`                     |
| `curl <url>`  | Download from URL                      | `curl http://example.com`          |
| `wget <url>`  | Download and save file                 | `wget http://example.com/file.txt` |

---

## 💾 Package Management

### Debian/Ubuntu (.deb)

| Command                  | Description          | Example                 |
| ------------------------ | -------------------- | ----------------------- |
| `sudo apt update`        | Update package list  | `sudo apt update`       |
| `sudo apt upgrade`       | Upgrade all packages | `sudo apt upgrade`      |
| `sudo apt install <pkg>` | Install a package    | `sudo apt install curl` |

### Red Hat/CentOS/Fedora (.rpm)

| Command                  | Description         | Example                 |
| ------------------------ | ------------------- | ----------------------- |
| `sudo yum update`        | Update all packages | `sudo yum update`       |
| `sudo yum install <pkg>` | Install a package   | `sudo yum install wget` |

---

## 🖥️ Shell Utilities

| Command         | Description           | Example   |
| --------------- | --------------------- | --------- |
| `man <command>` | View manual/help      | `man ls`  |
| `history`       | Show command history  | `history` |
| `clear`         | Clear terminal screen | `clear`   |
| `exit`          | Exit shell session    | `exit`    |

---

# **Linux Informational Commands Cheat Sheet**

---

## 🔍 1. **User & Identity Info**

| Command  | Description             | Example           |
| -------- | ----------------------- | ----------------- |
| `whoami` | Show current username   | `whoami` → `john` |
| `id`     | Show user and group IDs | `id`              |
| `id -u`  | Show numeric user ID    | `id -u` → `1001`  |
| `id -un` | Show username from UID  | `id -un` → `john` |

---

## 🖥️ 2. **Operating System Info**

| Command    | Description                  | Example                          |
| ---------- | ---------------------------- | -------------------------------- |
| `uname`    | Show OS name                 | `uname` → `Linux`                |
| `uname -s` | Show OS name (same as above) | `uname -s`                       |
| `uname -r` | Show kernel release version  | `uname -r` → `5.15.0-76-generic` |
| `uname -v` | Show kernel version          | `uname -v`                       |
| `uname -a` | Show all system info         | `uname -a`                       |

---

## 💾 3. **Disk Usage Info**

| Command        | Description                           | Example             |
| -------------- | ------------------------------------- | ------------------- |
| `df -h ~`      | Disk usage of home directory          | `df -h ~`           |
| `df -h`        | Disk usage of all mounted filesystems | `df -h`             |
| `du -sh <dir>` | Show size of a directory              | `du -sh /home/john` |

> `-h` makes output human-readable (e.g., GB instead of bytes)

---

## 🔄 4. **Process Monitoring**

| Command    | Description                                          | Example    |
| ---------- | ---------------------------------------------------- | ---------- |
| `ps`       | Show running processes (current shell only)          | `ps`       |
| `ps -e`    | Show all running processes                           | `ps -e`    |
| `top`      | Real-time process monitor                            | `top`      |
| `top -n 3` | Show top 3 processes                                 | `top -n 3` |
| `htop`     | Enhanced interactive process viewer _(if installed)_ | `htop`     |

---

## 🖨️ 5. **Printing Strings, Variables, and Dates**

| Command              | Description                              | Example                                     |
| -------------------- | ---------------------------------------- | ------------------------------------------- |
| `echo "text"`        | Print text to terminal                   | `echo "Hello World"`                        |
| `echo $PATH`         | Print value of an environment variable   | `echo $HOME`                                |
| `date`               | Print current date/time (default format) | `date`                                      |
| `date +"%j %Y"`      | Print day of year and year               | `date +"Day %j of %Y"` → `Day 097 of 2023`  |
| `date +"%A, %j, %Y"` | Day name, day of year, year              | `date +"%A, %j, %Y"` → `Tuesday, 097, 2023` |

---

## 📚 6. **Command Manuals**

| Command      | Description                        | Example      |
| ------------ | ---------------------------------- | ------------ |
| `man whoami` | View manual for `whoami`           | `man whoami` |
| `man id`     | View manual for `id`               | `man id`     |
| `man df`     | View manual for `df`               | `man df`     |
| `man ps`     | View manual for `ps`               | `man ps`     |
| `man date`   | View manual for `date`             | `man date`   |
| `man man`    | Learn how to use the `man` command | `man man`    |

---

### 📚 **Getting Help for Linux Commands – A Complete Guide**

When working with Linux, knowing how to find help is just as important as knowing the commands themselves. Here’s a structured approach to getting assistance when you’re stuck or curious.

---

## 🔍 1. **Use the Built-in `man` Command**

The `man` (manual) command is the traditional and most comprehensive way to get help in Linux.

### 🧾 How to Use It:

```bash
man command_name
```

Example:

```bash
man ls
```

### 📘 Man Page Sections:

| Section     | Description                                   |
| ----------- | --------------------------------------------- |
| NAME        | Name and brief description of the command     |
| SYNOPSIS    | How to use the command, including options     |
| DESCRIPTION | Detailed explanation of what the command does |
| OPTIONS     | List of available flags or arguments          |
| EXAMPLES    | Common usage examples                         |
| SEE ALSO    | Related commands or documentation             |

### 📋 View All Available Man Pages:

```bash
man -k .
```

This lists all commands with manual pages and a short description.

---

## 📝 2. **Install and Use the `tldr` Command**

`tldr` provides **simplified**, **example-based** help for common commands — perfect for quick reference.

### 💾 Install it:

If Node.js is installed:

```bash
npm install -g tldr
```

### 🚀 Usage:

```bash
tldr ls
```

You’ll see concise examples like:

```
ls
List directory contents.

- List files one per line:
  ls -1

- List all files, including hidden ones:
  ls -a
```

Ideal for users who want **just enough info to get the job done**.

---

## 💬 3. **Search Stack Overflow**

Stack Overflow is a powerful community-driven Q&A platform for developers and sysadmins.

### 🔍 Tips for Searching:

- Use the search bar on [https://stackoverflow.com/questions/tagged/linux](https://stackoverflow.com/questions/tagged/linux)
- Include relevant tags: `linux`, `bash`, `shell`, `command-line`
- Check the date of answers and read comments for context

> 📌 Example query:  
> `"how to delete a file in linux" site:stackoverflow.com`

---

## 🤖 4. **Search Stack Exchange (Unix & Linux)**

[Unix & Linux Stack Exchange](https://unix.stackexchange.com/) is ideal for deeper technical questions.

### 🎯 Best For:

- More detailed explanations than Stack Overflow
- Complex issues involving system administration, scripting, or obscure commands

---

## 🔍 5. **Just Google It!**

Sometimes, a simple web search is the fastest way to solve a problem.

### ✅ Tips:

- Include keywords like `Linux`, `Ubuntu`, or `bash`
- Add sources like `site:wikipedia.org` or `site:askubuntu.com`
- Avoid blindly trusting old or unverified results

---

## 📋 6. **Use Course Cheat Sheets**

Throughout this course, you'll encounter cheat sheets that:

- Condense key commands into easy-to-reference formats
- Help you review and apply concepts faster
- Are great for exam prep and real-world use

---

## 📄 7. **Refer to Wikipedia's List of Unix Commands**

Wikipedia maintains a list of Unix/Linux commands:
🔗 [List of Unix Commands (Wikipedia)](https://en.wikipedia.org/wiki/List_of_Unix_commands)

Includes:

- Command name
- Category (e.g., Filesystem, Process management)
- Description
- First appearance (e.g., Version 7 AT&T UNIX)

Great for historical context and discovering lesser-known utilities.

---

## 🧠 Summary Table: Ways to Get Help

| Method         | Best For                                 | Example                                                                      |
| -------------- | ---------------------------------------- | ---------------------------------------------------------------------------- |
| `man`          | Full, official documentation             | `man ls`                                                                     |
| `tldr`         | Quick examples and cheatsheet-style help | `tldr cp`                                                                    |
| Stack Overflow | Programming-related issues               | Search "how to rename file in Linux"                                         |
| Stack Exchange | Advanced Unix/Linux topics               | Visit [Unix & Linux SE](https://unix.stackexchange.com/)                     |
| Google         | Fast solutions and general knowledge     | Search "Linux sort file"                                                     |
| Cheat Sheets   | Quick reference and learning             | Provided in this course                                                      |
| Wikipedia      | Overview and history of commands         | [List of Unix Commands](https://en.wikipedia.org/wiki/List_of_Unix_commands) |

---

### 📌 **Exercise 1 - Informational Commands**

In this exercise, you explored several **Linux commands** that provide valuable system and user information. These commands are essential for understanding your environment, troubleshooting issues, and monitoring system performance.

---

## 🔍 Overview of Commands Covered

| Command  | Purpose                                             |
| -------- | --------------------------------------------------- |
| `whoami` | Displays the current user                           |
| `uname`  | Shows kernel/OS info                                |
| `id`     | Displays user and group IDs                         |
| `df`     | Shows disk space usage                              |
| `ps`     | Lists running processes                             |
| `top`    | Real-time view of running processes and system load |
| `echo`   | Prints text or variables to the terminal            |
| `date`   | Displays or sets the system date and time           |
| `man`    | Displays manual pages for commands                  |

---

## 🧾 Detailed Breakdown

### ✅ 1.1 Display Current User

```bash
whoami
```

- Output: `theia`
- Tells you which user is currently logged in.

---

### ✅ 1.2 Get OS Info with `uname`

```bash
uname
```

- Outputs: `Linux`

To get full system info:

```bash
uname -a
```

This includes:

- Kernel name
- Hostname
- Kernel release
- Kernel version
- Machine hardware name
- Processor type
- Operating system

---

### ✅ 1.3 View User Identity

```bash
id
```

- Shows:
  - `uid`: User ID
  - `gid`: Group ID
  - List of groups the user belongs to

---

### ✅ 1.4 Check Disk Space

```bash
df
```

- Shows disk usage in **512-byte blocks**

For human-readable format:

```bash
df -h
```

- Shows sizes in KB, MB, GB

---

### ✅ 1.5 View Running Processes

```bash
ps
```

- Lists processes owned by the current user

To see all processes:

```bash
ps -e
```

---

### ✅ 1.6 Real-Time Process Monitoring with `top`

```bash
top
```

- Gives live updates of:
  - Running processes
  - CPU and memory usage
  - System uptime
  - Load average

To exit: Press `q` or `Ctrl + C`  
To limit refreshes:

```bash
top -n 10
```

Sorting options (while `top` is running):

- `Shift + M` → Sort by memory
- `Shift + P` → Sort by CPU usage
- `Shift + N` → Sort by PID
- `Shift + T` → Sort by runtime

---

### ✅ 1.7 Print Messages with `echo`

```bash
echo "Welcome to the Linux lab"
```

Output:

```
Welcome to the Linux lab
```

Use `-e` to interpret escape characters:

```bash
echo -e "Line one\nLine two"
```

Output:

```
Line one
Line two
```

Common escape characters:

- `\n` – New line
- `\t` – Tab

---

### ✅ 1.8 Show Date and Time

```bash
date
```

- Shows full current date and time

Custom formats:

```bash
date "+%D"     # mm/dd/yy
date "+%Y-%m-%d %T"  # 2025-04-05 14:30:00
```

Popular format specifiers:
| Specifier | Meaning |
|----------|---------|
| `%d` | Day of month |
| `%h` | Abbreviated month (Jan-Dec) |
| `%m` | Month number |
| `%Y` | 4-digit year |
| `%T` | Time in HH:MM:SS |
| `%H` | Hour (00–23) |

---

### ✅ 1.9 View Manual Pages

```bash
man ls
```

- Opens the manual page for the `ls` command

To list all available man pages:

```bash
man -k .
```

Man pages typically include:

- NAME
- SYNOPSIS
- DESCRIPTION
- OPTIONS
- EXAMPLES
- SEE ALSO

---

## 📋 Summary Table

| Task                   | Command                   |
| ---------------------- | ------------------------- |
| Show current user      | `whoami`                  |
| Show OS info           | `uname`, `uname -a`       |
| Show user identity     | `id`                      |
| Show disk usage        | `df`, `df -h`             |
| List running processes | `ps`, `ps -e`             |
| Monitor processes live | `top`, `top -n 10`        |
| Print text             | `echo`, `echo -e`         |
| Show date/time         | `date`, `date "+format"`  |
| View command help      | `man command`, `man -k .` |

---

## 💡 Tips & Best Practices

- Use `--help` with many commands for quick usage examples:
  ```bash
  ls --help
  ```
- Combine `man` and `tldr` for both depth and speed:
  ```bash
  tldr df
  ```
- Use `watch` for repeated execution:
  ```bash
  watch df -h
  ```

---

### 📚 **Practice Exercises with Solutions**

Here are the practice exercises along with hints and complete solutions to reinforce your understanding of essential Linux commands.

---

## 🔹 **1. Get basic information about the operating system**

### 💡 Hint:

Use the `uname` command for kernel and OS-related information.

### ✅ Solution:

```bash
uname -a
```

This will display detailed system information, including:

- Kernel name
- Hostname
- Kernel release version
- Machine hardware name
- Operating system

---

## 🔹 **2. View all running processes on the system**

### 💡 Hint:

The `ps` command lists running processes. Use an option to show **all** processes.

### ✅ Solution:

```bash
ps -e
```

This shows every process currently running on the system, not just those owned by the current user.

---

## 🔹 **3. Get the table of processes and sort by memory usage**

### 💡 Hint:

Use the `top` command and a keyboard shortcut to sort by memory.

### ✅ Solution:

```bash
top
```

Once inside `top`, press:

```
Shift + M
```

This sorts the list by **memory usage**, allowing you to quickly identify which processes are using the most RAM.

> To exit `top`, press `q`.

---

## 🔹 **4. Display the current time**

### 💡 Hint:

Use the `date` command with a format specifier to show only the time.

### ✅ Solution:

```bash
date "+%T"
```

Output example:

```
14:25:36
```

Other useful formats:

- `date "+%H:%M"` → `14:25`
- `date "+%r"` → `02:25:36 PM`

---

## 🔹 **5. Using one command, display the messages "Hello!" and "Goodbye!" separated by a new line**

### 💡 Hint:

Use the `echo` command with the `-e` option to interpret escape sequences like `\n`.

### ✅ Solution:

```bash
echo -e "Hello!\nGoodbye!"
```

Output:

```
Hello!
Goodbye!
```

> The `-e` flag enables interpretation of backslash escapes like `\n` (new line) and `\t` (tab).

---

## 🎯 Bonus Tips

- Combine `echo` with redirection to write text into files:
  ```bash
  echo "Hello World" > hello.txt
  ```
- Use `watch` to monitor changing output:
  ```bash
  watch "ps -e | head -n 10"
  ```

---

# **File and Directory Navigation Commands in Linux**

---

## **Introduction**

This video introduces the essential **Linux commands for navigating files and directories**. After watching, you will be able to:

✅ Use `ls` to list directory contents  
✅ Navigate between directories using `cd`  
✅ Understand **relative vs absolute paths**  
✅ Search for files using the `find` command

---

## **1. List Files and Directories: `ls` Command**

### **Purpose**

The `ls` (list) command is used to display the contents of a directory.

### **Basic Usage**

- To list files in the current directory:

  ```bash
  ls
  ```

- To list files in a specific directory:
  ```bash
  ls Downloads
  ```

### **Common Options**

| Option | Description                                                  | Example  |
| ------ | ------------------------------------------------------------ | -------- |
| `-l`   | Long format – shows permissions, owner, size, date, and name | `ls -l`  |
| `-a`   | Show hidden files (files starting with `.`)                  | `ls -a`  |
| `-la`  | Detailed list including hidden files                         | `ls -la` |

> The output from `ls -l` includes:

- File type and permissions (`drwxr-xr-x`)
- Number of links
- Owner name
- Group name
- Size in bytes
- Date of last modification
- File or directory name

---

## **2. Show Current Working Directory: `pwd`**

### **Purpose**

The `pwd` (print working directory) command shows your **current location** in the file system.

### **Usage**

```bash
pwd
```

> Example Output:

```
/home/user/Documents
```

Useful when:

- You're unsure which directory you are in.
- You want to verify your location before running commands.

---

## **3. Change Directory: `cd` Command**

### **Purpose**

The `cd` (change directory) command lets you move between directories.

### **Basic Syntax**

```bash
cd <directory_path>
```

### **Examples**

| Command                         | Description                               |
| ------------------------------- | ----------------------------------------- |
| `cd Documents`                  | Move into the `Documents` subdirectory    |
| `cd ..`                         | Move up one level to the parent directory |
| `cd ~` or just `cd`             | Go to your home directory                 |
| `cd /home/user/Documents/Notes` | Move to an absolute path                  |
| `cd ./projects`                 | Move to a relative path                   |

### **Understanding Path Types**

| Type              | Description                                  | Example              |
| ----------------- | -------------------------------------------- | -------------------- |
| **Absolute Path** | Starts from root `/`, always starts with `/` | `/var/log/syslog`    |
| **Relative Path** | Relative to current working directory        | `../images/logo.png` |

---

## **4. Find Files: `find` Command**

### **Purpose**

The `find` command helps you locate files and directories based on various criteria like name, type, size, etc.

### **Basic Syntax**

```bash
find <starting_directory> <options>
```

### **Common Examples**

| Command                         | Description                                             |
| ------------------------------- | ------------------------------------------------------- |
| `find . -name "a.txt"`          | Find all files named `a.txt` in current directory (`.`) |
| `find /home/user -name "*.txt"` | Find all `.txt` files in user's home directory          |
| `find . -iname "a.txt"`         | Case-insensitive search for `a.txt`                     |
| `find . -type d -name "Images"` | Find directories named `Images`                         |
| `find . -type f`                | Find only files in current directory tree               |

> Tip: The `.` means “start searching here” — it’s useful when you want to limit the scope of your search.

---

## **5. Summary of Key Concepts**

### ✅ `ls` – Listing Contents

- Lists files and directories.
- Use options like `-l`, `-a`, and `-la` for more detailed views.

### ✅ `pwd` – Knowing Where You Are

- Displays the full path of the current working directory.

### ✅ `cd` – Moving Around

- Supports both **absolute** and **relative** paths.
- Use `~` to go to your home directory.
- Use `..` to move up one level.

### ✅ `find` – Searching Efficiently

- Powerful tool for locating files and folders.
- Can use exact names, wildcards, case-insensitive searches, and filters by type.

---

## **6. Quick Reference Table**

| Task                            | Command                          |
| ------------------------------- | -------------------------------- |
| List files in current directory | `ls`                             |
| List with details               | `ls -l`                          |
| Show hidden files               | `ls -a`                          |
| Print current directory         | `pwd`                            |
| Move into a directory           | `cd <dir>`                       |
| Move to home directory          | `cd ~` or `cd`                   |
| Move up one level               | `cd ..`                          |
| Move to absolute path           | `cd /path/to/dir`                |
| Find files by name              | `find . -name "filename"`        |
| Find files case-insensitively   | `find . -iname "filename"`       |
| Find directories only           | `find . -type d -name "dirname"` |

---

## **7. Final Thoughts**

Mastering these navigation commands gives you control over your Linux environment. Whether you're organizing files, troubleshooting issues, or writing scripts, understanding how to navigate the filesystem efficiently is crucial.

---

# **File and Directory Management Commands in Linux V2**

---

## **1. Introduction**

✅ Creating and deleting files and directories  
✅ Copying and moving files and folders  
✅ Managing file permissions (e.g., making a script executable)

These commands are essential for managing your system, organizing data, and working with scripts or configuration files.

---

## **2. Creating and Removing Files and Directories**

### **A. `mkdir` – Make Directory**

- **Purpose**: Create new directories.
- **Syntax**:
  ```bash
  mkdir <directory_name>
  ```
- **Example**:
  ```bash
  mkdir test
  ```

> Creates a directory named `test` in the current location.

---

### **B. `rm` – Remove Files or Directories**

- **Purpose**: Delete files or directories.
- **Syntax**:

  ```bash
  rm <filename>
  ```

- **Remove a file**:

  ```bash
  rm file1.txt
  ```

- **Remove a directory and its contents**:
  ```bash
  rm -r folder1
  ```

> ⚠️ **Warning**: Use `rm -r` carefully — it deletes everything inside the directory recursively.

---

### **C. `rmdir` – Remove Empty Directories**

- **Purpose**: Delete only **empty** directories.
- **Syntax**:

  ```bash
  rmdir <directory_name>
  ```

- **Example**:
  ```bash
  rmdir empty_folder
  ```

> If the folder contains files or subdirectories, this command will fail — use `rm -r` instead.

---

### **D. `touch` – Create Empty Files or Update Timestamps**

- **Purpose**: Create an empty file or update the last-modified timestamp of an existing one.
- **Syntax**:

  ```bash
  touch <filename>
  ```

- **Create multiple files**:

  ```bash
  touch a.txt b.txt c.txt
  ```

- **Update timestamp on an existing file**:
  ```bash
  touch notes.txt
  ```

> Useful for testing, scripting, or resetting file timestamps.

---

## **3. Copying and Moving Files and Directories**

### **A. `cp` – Copy Files or Directories**

- **Purpose**: Copy files from one location to another.
- **Syntax**:

  ```bash
  cp <source> <destination>
  ```

- **Copy a single file**:

  ```bash
  cp notes.txt Documents/
  ```

- **Copy and rename a file**:

  ```bash
  cp notes.txt Documents/backup_notes.txt
  ```

- **Copy a directory and all contents**:
  ```bash
  cp -r Documents Docs_copy
  ```

> The `-r` option enables recursive copying of directories and their contents.

---

### **B. `mv` – Move or Rename Files/Directories**

- **Purpose**: Move files/dirs or rename them.
- **Syntax**:

  ```bash
  mv <source> <destination>
  ```

- **Move a file into a directory**:

  ```bash
  mv my_script.sh Scripts/
  ```

- **Rename a file**:

  ```bash
  mv old_name.txt new_name.txt
  ```

- **Move multiple directories into another**:
  ```bash
  mv Scripts Notes Documents/
  ```

> Unlike `cp`, `mv` does **not duplicate** the original — it moves or renames.

---

## **4. Managing File Permissions with `chmod`**

### **A. `chmod` – Change File Mode (Permissions)**

- **Purpose**: Set or change **read**, **write**, and **execute** permissions on files.
- **Syntax**:
  ```bash
  chmod [options] <filename>
  ```

### **Common Options**

| Option | Description               |
| ------ | ------------------------- |
| `+r`   | Add read permission       |
| `+w`   | Add write permission      |
| `+x`   | Add execute permission    |
| `-r`   | Remove read permission    |
| `-w`   | Remove write permission   |
| `-x`   | Remove execute permission |

### **Example: Making a Script Executable**

```bash
chmod +x my_script.sh
```

- Before:

  ```bash
  -rw-r--r-- 1 user group 0 Jan 1 12:00 my_script.sh
  ```

- After:
  ```bash
  -rwxr-xr-x 1 user group 0 Jan 1 12:00 my_script.sh
  ```

Now you can run the script:

```bash
./my_script.sh
```

---

## **5. Summary of Key Commands**

| Task                            | Command           | Notes                       |
| ------------------------------- | ----------------- | --------------------------- |
| Create a directory              | `mkdir <dir>`     |                             |
| Remove a file                   | `rm <file>`       |                             |
| Remove a directory and contents | `rm -r <dir>`     | Use with caution            |
| Remove an empty directory       | `rmdir <dir>`     | Safe alternative            |
| Create or update a file         | `touch <file>`    | Sets current timestamp      |
| Copy files                      | `cp <src> <dest>` | Use `cp -r` for directories |
| Move or rename files            | `mv <src> <dest>` | Also used for renaming      |
| Change file permissions         | `chmod +x <file>` | Makes a file executable     |

---

## **6. Final Tips**

- Always double-check before using `rm -r` — it's irreversible.
- Use `rmdir` when removing empty directories to avoid accidental deletion.
- `chmod` is essential for running scripts or setting up secure environments.
- Combine these commands with others like `ls`, `cd`, and `find` for powerful file operations.

---

### 📁 Exercise 1 - Navigating Files and Directories

In this exercise, you practiced essential Linux commands for **navigating the filesystem**, **listing directory contents**, and understanding **file patterns**.

---

## 📍 1.1 Get the Location of the Present Working Directory

### Command:

```bash
pwd
```

### What It Does:

- Stands for **"Print Working Directory"**
- Shows the **full path** to the directory where you are currently located

Example output:

```
/home/theia
```

---

## 📋 1.2 List Files and Directories in a Directory

### Basic Usage:

```bash
ls
```

- Lists all **non-hidden files and directories** in the current location
- If the directory is empty, it returns nothing

### View Contents of `/bin` (Binary Directory):

```bash
ls /bin
```

- Displays system-level commands like `ls`, `cd`, `cp`, etc.
- You can also look at specific files:
  ```bash
  ls /bin/ls
  ```

### Use Wildcards to Match Patterns:

#### 🔍 All files starting with `b`:

```bash
ls /bin/b*
```

#### 🔍 All files ending with `r`:

```bash
ls /bin/*r
```

> 💡 The `*` wildcard matches any number of characters

---

## 📄 Long Listing Format

### See detailed file information:

```bash
ls -l
```

Includes:

- File type and permissions
- Number of links
- Owner
- Group
- Size in bytes
- Last modification date/time
- File or directory name

### Common `ls` Options:

| Option | Description                                 |
| ------ | ------------------------------------------- |
| `-a`   | Show hidden files (those starting with `.`) |
| `-d`   | Show directories only                       |
| `-h`   | Human-readable sizes (e.g., KB, MB)         |
| `-l`   | Long listing format                         |
| `-S`   | Sort by file size (largest first)           |
| `-t`   | Sort by modification time (newest first)    |
| `-r`   | Reverse sort order                          |

### Example: List all files (including hidden ones) in long format:

```bash
ls -la
```

### Example: List all files in `/etc` with details:

```bash
ls -la /etc
```

This helps you explore system-wide configuration files.

---

## ✅ Summary Table

| Task                        | Command                    |
| --------------------------- | -------------------------- |
| Show current directory      | `pwd`                      |
| List files in current dir   | `ls`                       |
| List files in `/bin`        | `ls /bin`                  |
| List files matching pattern | `ls /bin/b*`, `ls /bin/*r` |
| Long list format            | `ls -l`                    |
| Show hidden files           | `ls -a`                    |
| Long list including hidden  | `ls -la`                   |
| Human-readable sizes        | `ls -lh`                   |

---

## 💡 Pro Tips

- Combine options:
  ```bash
  ls -lah   # Long list, human-readable, include hidden
  ```
- Use tab completion to avoid typing full paths:
  ```bash
  ls /bi<TAB>
  ```
  Becomes:
  ```bash
  ls /bin/
  ```

---

### 📁 Exercise 2 - Creating Files and Directories

In this exercise, you practiced using Linux commands to **create directories**, **navigate the filesystem**, and **create or update files** using the `touch` command.

---

## ✅ Summary of Commands Covered

| Task                                     | Command                |
| ---------------------------------------- | ---------------------- |
| Create a directory                       | `mkdir directory_name` |
| Change working directory                 | `cd directory_name`    |
| Move up one directory level              | `cd ..`                |
| Go back to home directory                | `cd`                   |
| Create an empty file or update timestamp | `touch filename`       |

---

## 🧾 Step-by-Step Breakdown

### 🔹 2.1 Create a Directory with `mkdir`

```bash
mkdir scripts
```

- Creates a new directory named `scripts` in your current location

Verify it was created:

```bash
ls
```

You should see `scripts` listed.

---

### 🔹 2.2 Change Working Directory with `cd`

Move into the `scripts` directory:

```bash
cd scripts
```

Check your current location:

```bash
pwd
```

Return to your home directory:

```bash
cd
```

Move up one level (to the parent directory):

```bash
cd ..
```

This is useful when navigating through nested directories.

---

### 🔹 2.3 Create an Empty File with `touch`

Go back to your home directory:

```bash
cd
```

Create a new file called `myfile.txt`:

```bash
touch myfile.txt
```

Verify the file exists:

```bash
ls
```

If the file already exists, `touch` updates its **last-modified timestamp**:

```bash
touch myfile.txt
```

To check the updated timestamp:

```bash
date -r myfile.txt
```

This shows the last time the file was accessed or modified.

---

## 📋 Tips & Tricks

- You can create multiple directories at once:
  ```bash
  mkdir dir1 dir2 dir3
  ```
- Make a nested directory structure easily:
  ```bash
  mkdir -p project/files/data
  ```
  The `-p` option creates parent directories as needed.
- Use tab completion for faster navigation:
  ```bash
  cd scri<TAB>
  ```
  Completes to:
  ```bash
  cd scripts
  ```

---

## 🧠 Why These Commands Matter

These basic tools are essential for managing your workspace in Linux:

- `mkdir`: Organize your files by creating structured directories
- `cd`: Navigate between folders quickly
- `touch`: Create placeholder files or update timestamps for testing or scripting purposes

---

### 📁 Exercise 3 - Managing Files and Directories

In this exercise, you practiced essential Linux commands for **searching**, **removing**, **moving**, **renaming**, and **copying** files and directories — key skills for managing your system effectively.

---

## ✅ Summary of Commands Covered

| Task                  | Command       |
| --------------------- | ------------- |
| Search for files      | `find`        |
| Remove (delete) files | `rm`, `rm -i` |
| Move or rename files  | `mv`          |
| Copy files            | `cp`          |

---

## 🔍 Step-by-Step Breakdown

### 🔹 3.1 Search for Files Using `find`

```bash
find /etc -name '*.txt'
```

- Searches the `/etc` directory and its subdirectories for all `.txt` files.
- `-name` specifies a filename pattern to match.
- You may see "Permission denied" errors — these are normal due to access restrictions in lab environments.

---

### 🔹 3.2 Remove Files with `rm`

```bash
rm -i myfile.txt
```

- The `-i` option prompts for confirmation before deletion:
  ```
  rm: remove regular file 'myfile.txt'? y/n
  ```

After deletion, verify:

```bash
ls
```

> ⚠️ Warning: Deleted files **cannot be recovered easily**. Always double-check what you're deleting.

Use without `-i` only when sure:

```bash
rm myfile.txt
```

Delete multiple files safely using confirmation:

```bash
rm -i *.txt
```

---

### 🔹 3.3 Move or Rename Files with `mv`

#### ✏️ Rename a File:

```bash
mv users.txt user-info.txt
```

This renames `users.txt` to `user-info.txt` in the same directory.

Verify:

```bash
ls
```

#### 📦 Move a File to Another Directory:

```bash
mv user-info.txt /tmp
```

Moves `user-info.txt` to the `/tmp` directory.

Verify:

```bash
ls
ls -l /tmp
```

> 💡 If the target file already exists, it will be overwritten silently — always be cautious!

---

### 🔹 3.4 Copy Files with `cp`

#### 📄 Copy from One Location to Another:

```bash
cp /tmp/user-info.txt user-info.txt
```

This copies the file back to your current working directory.

Verify:

```bash
ls
```

#### 📂 Copy Content of a System File:

```bash
cp /etc/passwd users.txt
```

This creates a new file `users.txt` containing the contents of `/etc/passwd`.

Check that the copy was successful:

```bash
ls
cat users.txt
```

You can also view the first few lines:

```bash
head users.txt
```

---

## 🧰 Pro Tips

- Use wildcards to move or copy groups of files:
  ```bash
  cp *.txt /backup/
  mv *.log logs/
  ```
- Combine `cp` with `-r` to copy entire directories:
  ```bash
  cp -r myfolder/ backup/
  ```
- Use `rm -r` carefully to delete directories and their contents:
  ```bash
  rm -r myfolder
  ```

---

## 🧠 Why These Commands Matter

These tools give you full control over your filesystem:

- `find`: Locate files across your system
- `rm`: Clean up unwanted files
- `mv`: Reorganize or rename files
- `cp`: Duplicate or archive content

They form the foundation for automating tasks, writing scripts, and managing data efficiently.

---

### 📚 **Practice Exercises – Managing Files and Directories**

Here are the practice exercises with **hints** and **solutions** to help reinforce your understanding of Linux commands for navigating, creating, moving, copying, and deleting files and directories.

---

## 🔹 **1. Display the contents of the /home directory**

### 💡 Hint:

Use the `ls` command to list directory contents.

### ✅ Solution:

```bash
ls /home
```

This shows all user directories inside `/home`.

---

## 🔹 **2. Ensure that you are in your home directory**

### 💡 Hint:

Use the `cd` command without arguments to return to your home directory.

### ✅ Solution:

```bash
cd
```

You can verify using:

```bash
pwd
```

It should output something like:

```
/home/theia
```

---

## 🔹 **3. Create a new directory called tmp and verify its creation**

### 💡 Hint:

Use `mkdir` to create a directory and `ls` to confirm it exists.

### ✅ Solution:

```bash
mkdir tmp
ls
```

You should see `tmp` listed in the output.

---

## 🔹 **4. Create a new, empty file named display.sh in the tmp directory, and verify its creation**

### 💡 Hint:

Navigate into the `tmp` directory and use `touch` to create an empty file.

### ✅ Solution:

```bash
cd tmp
touch display.sh
ls
```

You should see `display.sh` listed.

---

## 🔹 **5. Create a copy of display.sh, called report.sh, within the same directory**

### 💡 Hint:

Use the `cp` command to make a copy of a file.

### ✅ Solution:

```bash
cp display.sh report.sh
ls
```

Now both `display.sh` and `report.sh` should be listed.

---

## 🔹 **6. Move your copied file, report.sh, up one level in the directory tree to the parent directory. Verify your changes**

### 💡 Hint:

Use `mv` to move the file and `cd ..` or `ls -l ../` to check.

### ✅ Solution:

```bash
mv report.sh ..
ls ..
```

Or:

```bash
cd ..
ls
```

You should now see `report.sh` in the parent directory.

---

## 🔹 **7. Delete the file display.sh**

### 💡 Hint:

Use the `rm` command to delete a file. Consider using `-i` for confirmation (optional).

### ✅ Solution:

```bash
rm display.sh
```

To verify:

```bash
ls
```

The file `display.sh` should no longer appear.

---

## 🔹 **8. List the files in /etc directory in the ascending order of their access time**

### 💡 Hint:

Use the `ls` command with appropriate options to sort by access time.

### ✅ Solution:

```bash
ls -ltu /etc
```

- `-l` = long listing format
- `-t` = sort by modification time (but combined with `-u`, sorts by access time)
- `-u` = use access time for sorting

> This lists files sorted by when they were last accessed, newest first.

---

## 🔹 **9. Copy the file /var/log/bootstrap.log to your current directory**

### 💡 Hint:

Use the `cp` command to copy a file from its source path to the current directory.

### ✅ Solution:

```bash
cp /var/log/bootstrap.log .
```

To verify:

```bash
ls
```

You should see `bootstrap.log` in your current directory.

---

## 🧠 Bonus Tips

- Use tab completion to avoid typing full paths:
  ```bash
  cp /va<TAB>/lo<TAB>/boo<TAB> .
  ```
- Combine `ls` options for better readability:
  ```bash
  ls -lh
  ```
- Use `rm -i` when unsure:
  ```bash
  rm -i *.tmp
  ```

---

Great job completing these hands-on exercises! You're now comfortable with basic file and directory management in Linux.

---

### 🔒 **Security: Managing File Permissions and Ownership – Summary & Guide**

In this reading, you learned how to manage **file permissions** and **ownership** in Linux — a crucial skill for protecting sensitive data and ensuring system security.

---

## 🎯 **Learning Objectives Recap**

By the end of this section, you should be able to:

- Explain file ownership and permissions
- View file and directory permissions
- Make files private by changing permission settings

---

## 🔐 Why File Permissions Matter

Linux is a **multi-user operating system**, which means multiple people can access the same machine. Without proper permissions:

- Anyone could **read or modify your files**
- Malicious users might **execute harmful scripts**
- Sensitive documents (like tax records or company IP) could be **exposed**

That’s why **permissions and ownership** allow fine-grained control over who can read, write, or execute files.

---

## 👤 Types of Owners in Linux

There are **three categories** of users that determine permission levels:

| Category      | Meaning                                     |
| ------------- | ------------------------------------------- |
| **user (u)**  | The owner of the file (usually the creator) |
| **group (g)** | A group of users assigned to the file       |
| **other (o)** | Everyone else with access to the system     |

Each category has its own set of permissions:

- `r` = Read
- `w` = Write
- `x` = Execute

---

## 👀 Viewing File Permissions

Use:

```bash
ls -l filename
```

Example output:

```
-rw-r--r-- 1 theia users 25 Dec 22 17:47 my_new_file
```

- `-`: Indicates it's a regular file
- `rw-`: User (owner) permissions
- `r--`: Group permissions
- `r--`: Others' permissions

📘 For directories:

- `d` at the start indicates it's a directory
- Permissions mean:
  - `r`: Can list contents (`ls`)
  - `w`: Can create or delete files inside
  - `x`: Can enter the directory (`cd`)

---

## 🔧 Changing File Permissions with `chmod`

You can change permissions using:

```bash
chmod [options] filename
```

### Example: Make a file private

```bash
chmod go-r my_new_file
```

This removes **read** permission for **group** and **others**.

After running:

```bash
ls -l my_new_file
```

You'll see:

```
-rw------- 1 theia users 24 Dec 22 18:49 my_new_file
```

Now only the **owner** can read and write to the file.

> ⚠️ Only the **owner** or **root** can change permissions on a file.

---

## 🛠️ Common `chmod` Syntax Options

| Command               | Action                                       |
| --------------------- | -------------------------------------------- |
| `chmod u+x file.sh`   | Add execute permission for the user          |
| `chmod go-w file.txt` | Remove write permission for group and others |
| `chmod 755 file.sh`   | Set numeric permissions (see below)          |

### Numeric Permission Notation

Each permission level has a number value:

- `r` = 4
- `w` = 2
- `x` = 1

Sum them to get numeric values:

| Permission | Value |
| ---------- | ----- |
| `rwx`      | 7     |
| `rw-`      | 6     |
| `r-x`      | 5     |
| `r--`      | 4     |

Example:

```bash
chmod 600 secret.txt
```

Only the owner has **read and write** access.

---

## 📁 Executable Files and Shell Scripts

To make a shell script executable:

1. Add a **shebang** line at the top:
   ```bash
   #!/bin/bash
   ```
2. Give it execute permission:
   ```bash
   chmod +x script.sh
   ```
3. Run it:
   ```bash
   ./script.sh
   ```

This tells the OS that the file is a program written in Bash (or another interpreter).

---

## ✅ Summary Table

| Concept                | Description                                    |
| ---------------------- | ---------------------------------------------- |
| **User (u)**           | Owner of the file                              |
| **Group (g)**          | Group of users who share ownership             |
| **Other (o)**          | All other users                                |
| **Permissions**        | `r` = read, `w` = write, `x` = execute         |
| **View Permissions**   | `ls -l`                                        |
| **Change Permissions** | `chmod`                                        |
| **Make Private**       | `chmod go-rwx filename`                        |
| **Numeric Mode**       | `chmod 600 filename`                           |
| **Directories**        | `r` = list, `w` = modify contents, `x` = enter |

---

## 💡 Pro Tips

- Use `chmod 700 folder` to keep a directory private
- Protect sensitive scripts with `chmod 600 script.sh`
- Use `id` to see what groups you belong to
- Use `chown` (as root) to change file ownership

---

You're now equipped with the knowledge to **secure your files**, **control access**, and **protect sensitive data** in a Linux environment.

---

### 🛠️ Exercise 1 - Viewing and Modifying File Access Permissions

In this exercise, you learned how to **view** and **modify file permissions** in Linux using the `ls -l` and `chmod` commands. Understanding and managing permissions is essential for maintaining system security and controlling access to your files.

---

## 📁 1.1 View File Access Permissions

### 🔧 Steps:

1. Navigate to your project directory:

   ```bash
   cd /home/project
   ```

2. Download the required file:

   ```bash
   wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/usdoi.txt
   ```

3. View the file's permissions:
   ```bash
   ls -l usdoi.txt
   ```

### ✅ Sample Output:

```
-rw-r--r-- 1 theia theia 8121 May 31 16:45 usdoi.txt
```

### 📝 Breakdown of Permission String: `-rw-r--r--`

| Part  | Meaning                                       |
| ----- | --------------------------------------------- |
| `-`   | It's a regular file (use `d` for directories) |
| `rw-` | User (owner) has **read** and **write**       |
| `r--` | Group has only **read**                       |
| `r--` | Others have only **read**                     |

---

## 🔐 1.2 Change File Access Permissions with `chmod`

The `chmod` command allows you to modify who can **read**, **write**, or **execute** a file.

### 🔧 Syntax:

```bash
chmod [who][operator][permission] filename
```

| Component    | Values                                           |
| ------------ | ------------------------------------------------ |
| `who`        | `u` = user, `g` = group, `o` = others, `a` = all |
| `operator`   | `+` = add, `-` = remove, `=` = set exactly       |
| `permission` | `r` = read, `w` = write, `x` = execute           |

---

### 🔍 Example Commands

#### ❌ Remove read permission for all users:

```bash
chmod -r usdoi.txt
```

Verify:

```bash
ls -l usdoi.txt
```

You'll see something like:

```
--w------- 1 theia theia 8121 May 31 16:45 usdoi.txt
```

#### ✅ Restore read permission for all users:

```bash
chmod +r usdoi.txt
```

Verify:

```bash
ls -l usdoi.txt
```

You should return to:

```
-rw-r--r-- 1 theia theia 8121 May 31 16:45 usdoi.txt
```

#### 🚫 Remove read permission only for "other":

```bash
chmod o-r usdoi.txt
```

Verify:

```bash
ls -l usdoi.txt
```

Now output will be:

```
-rw-r----- 1 theia theia 8121 May 31 16:45 usdoi.txt
```

Only **user** and **group** can read the file now.

---

## 🧠 Summary Table

| Task                                    | Command              |
| --------------------------------------- | -------------------- |
| View file permissions                   | `ls -l filename`     |
| Remove read from all                    | `chmod -r filename`  |
| Add read to all                         | `chmod +r filename`  |
| Remove read from others                 | `chmod o-r filename` |
| Add execute to user                     | `chmod u+x filename` |
| Set exact permissions (e.g., rw-------) | `chmod 600 filename` |

---

## 💡 Pro Tips

- Use **numeric mode** for precision:
  ```bash
  chmod 644 usdoi.txt    # rw-r--r--
  chmod 700 secret.sh     # rwx------
  ```
- Always double-check permissions on sensitive files:
  ```bash
  ls -l secret.txt
  ```
- Only the **file owner** or **root** can change permissions.

---

Great job completing this exercise! You're now able to view and manage file permissions — an essential skill for working securely in Linux.

---

### 📁 Exercise 2 - Understanding Directory Access Permissions

In this exercise, you explored how **directory permissions** in Linux work and how they differ from file permissions. You learned that **execute (`x`) permission is required to enter a directory**, and **write (`w`) permission is needed to create or delete files inside it**.

---

## 🔍 Summary of What You Learned

| Permission    | Meaning for Directories                  |
| ------------- | ---------------------------------------- |
| `r` (read)    | Allows listing contents with `ls`        |
| `w` (write)   | Allows adding/removing files             |
| `x` (execute) | Allows entering the directory using `cd` |

> ⚠️ Even if you have write access, you can't modify contents without execute permission!

---

## 🧾 Step-by-Step Breakdown

### 🔹 2.1 View Default Directory Access Permissions

#### Create a new directory:

```bash
cd /home/project
mkdir test
```

#### Check its permissions:

```bash
ls -l
```

Output example:

```
drwxr-sr-x 2 theia users 4096 May 15 14:06 test
```

- `d`: Indicates it's a directory
- `rwx`: Owner (user) has read, write, and execute
- `r-s`: Group has read and setgid (special permission)
- `r-x`: Others have read and execute

You verified that:

- You could enter the directory
- You could create a subdirectory inside it

Commands used:

```bash
cd test
mkdir test2
cd ..
```

> 💡 The `s` in group permissions is a special flag called **setgid** — it ensures new files inherit the group of the parent directory.

---

### 🔹 2.2 Remove User Execute Permissions

#### Remove execute permission for owner:

```bash
chmod u-x test
```

Now try:

```bash
cd test
```

❌ Output:

```
bash: cd: test: Permission denied
```

Even though you still have read and write permissions, **you can't enter the directory** without execute permission.

Try listing contents:

```bash
ls -l test
```

✅ Works — because you still have **read** permission.

Try creating a subdirectory:

```bash
mkdir test/test3
```

❌ Fails — because **write requires execute**.

---

### 🔁 Restore Permissions

#### Add back execute:

```bash
chmod u+x test
```

#### Remove write:

```bash
chmod u-w test
```

Check current permissions:

```bash
ls -l
```

Now try:

```bash
cd test
mkdir test_again
```

❌ Output:

```
mkdir: cannot create directory ‘test_again’: Permission denied
```

You can **enter** the directory (thanks to `x`), but you **can't modify** it (because you don’t have `w`).

---

## 🧠 Key Takeaways

| Scenario               | Required Permission                             |
| ---------------------- | ----------------------------------------------- |
| List contents (`ls`)   | `r`                                             |
| Enter directory (`cd`) | `x`                                             |
| Create/delete files    | `w` + `x`                                       |
| Rename or move files   | `w` + `x` in both source and target directories |

> 🧩 Think of `x` as a key to open a door — you need it before you can do anything useful inside a directory.

---

## ✅ Summary Table

| Command            | Effect                                                    |
| ------------------ | --------------------------------------------------------- |
| `ls -l`            | Show directory permissions                                |
| `chmod u+x dir`    | Allow user to enter directory                             |
| `chmod u-w dir`    | Prevent user from modifying directory contents            |
| `cd dir`           | Requires execute (`x`) permission                         |
| `ls dir`           | Requires read (`r`) permission                            |
| `mkdir dir/subdir` | Requires write (`w`) + execute (`x`) permissions on `dir` |

---

You've now mastered how **directory permissions** control access differently than file permissions — an essential concept for securing and managing your Linux system effectively.

---

### 🛠️ **Practice Exercises – File and Directory Permissions**

Here are the **practice exercises** with hints and full solutions to help you reinforce your understanding of Linux file and directory permissions.

---

## 🔹 **1. List the permissions set for the file `usdoi.txt`**

### 💡 Hint:

Use the `ls -l` command to view file permissions.

### ✅ Solution:

```bash
ls -l usdoi.txt
```

Example output:

```
-rw-r--r-- 1 theia users 8121 May 31 16:45 usdoi.txt
```

This shows that:

- The owner has **read and write**
- The group has **read**
- Others have **read**

---

## 🔹 **2. Revoke the write permission on `usdoi.txt` for the user, and verify**

### 💡 Hint:

Use `chmod u-w` to remove write access for the user.

### ✅ Solution:

```bash
chmod u-w usdoi.txt
ls -l usdoi.txt
```

New output:

```
-r--r--r-- 1 theia users 8121 May 31 16:45 usdoi.txt
```

The user (owner) no longer has **write** permission.

---

## 🔹 **3. What happens if you try to delete `usdoi.txt` after revoking write permissions?**

### 💡 Hint:

You don’t need write permission to delete a file — but you **do** need write permission in the **directory** it’s in.

### ✅ Solution:

Try deleting:

```bash
rm usdoi.txt
```

✅ It works!  
Even though you removed write permission **on the file**, you can still delete it because:

- You own the file
- You have **write permission in the directory**

> 🔍 Note: If you didn’t own the file, you could still delete it as long as:
>
> - You had **write** permission in the directory
> - You didn't own the file

---

## 🔹 **4. Create a new directory called `tmp_dir` in your home directory**

### 💡 Hint:

Use the `mkdir` command.

### ✅ Solution:

```bash
cd ~
mkdir tmp_dir
```

Now you have a new directory in your home folder.

---

## 🔹 **5. View the permissions of the newly created directory `tmp_dir`**

### 💡 Hint:

Use `ls -l` again to see directory permissions.

### ✅ Solution:

```bash
ls -l
```

Output will include something like:

```
drwxr-xr-x 2 theia users 4096 Apr 5 10:00 tmp_dir
```

This means:

- User: read, write, execute
- Group: read, execute
- Others: read, execute

---

## 🔹 **6. Revoke the user write permission for `tmp_dir`**

### 💡 Hint:

Use `chmod u-w` on the directory.

### ✅ Solution:

```bash
chmod u-w tmp_dir
ls -l
```

New output:

```
dr-xr-xr-x 2 theia users 4096 Apr 5 10:00 tmp_dir
```

User now only has **execute** and **read** — not **write**.

---

## 🔹 **7. Check whether you can create a subdirectory `sub_dir` inside `tmp_dir`**

### 💡 Hint:

Use `mkdir` to attempt creating a subdirectory.

### ✅ Solution 1:

```bash
mkdir tmp_dir/sub_dir
```

❌ Output:

```
mkdir: cannot create directory ‘tmp_dir/sub_dir’: Permission denied
```

### ✅ Solution 2 Explanation:

Even though you have **execute** (`x`) permission on `tmp_dir`, which allows you to **enter** the directory, you **don’t have write** (`w`) permission — so you **can't modify** its contents (like creating or deleting files or directories).

---

## 🧠 Summary Table

| Task                        | Command                                            |
| --------------------------- | -------------------------------------------------- |
| View file permissions       | `ls -l filename`                                   |
| Remove write from user      | `chmod u-w filename`                               |
| Delete a file               | `rm filename` _(requires write in directory)_      |
| Create a directory          | `mkdir dirname`                                    |
| View directory permissions  | `ls -l`                                            |
| Remove write from directory | `chmod u-w dirname`                                |
| Create subdirectory         | `mkdir dirname/subdir` _(fails without `w` + `x`)_ |

---

Great job working through these permission exercises! You're building strong skills in managing **file access control**, **user permissions**, and **directory behavior** in Linux.

---
