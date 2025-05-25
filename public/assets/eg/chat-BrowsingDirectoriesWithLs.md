---
author: Sat Naing
pubDatetime: 2022-09-23T15:22:00Z
modDatetime: 2025-03-22T06:25:46.734Z
title: Adding new posts in AstroPaper theme
slug: adding-new-posts-in-astropaper-theme
featured: true
draft: false
tags:
  - docs
description:
  Some rules & recommendations for creating or adding new posts using AstroPaper
  theme.
---

### USER

Exercise 1 - Browsing Directories
ls

In this exercise, you will learn how to browse the content of directories using the ls command.

ls is a special command that the shell interprets and runs as a program.

1.1. Viewing files in the current working directory
Typing and entering ls will display all files and directories contained within your current working directory:

1
ls

Copied!
Your default current working directory in this lab environment, the /home/project directory, is empty. Thus entering ls into the command line will not return anything yet.

1.2. Viewing files and directories within any directory
If you know the path to a directory, you can view its contents by passing the path name as a command line argument to the ls command as follows:

ls [PATH TO DIRECTORY]

For example:

1
ls /

Copied!
will show the contents of 'slash', your Linux system's root directory.

Recall some of the standard subdirectories of 'slash' that you've learned about previously:

Directory Contains
/bin System commands, also called binaries
/sbin System administration binaries
/usr User programs and data
/home Home directory
/media Removable media device directories
For example, entering the following command:

1
ls /bin

Copied!
will display the contents of the /bin directory.

Notice that one of the files in the /bin directory is called "ls". Indeed, when you enter the ls command, Linux searches for and runs the ls command by executing the binary file /bin/ls.

### ASSISTANT

### Exercise 1 - Browsing Directories with `ls`

In this exercise, you're learning how to navigate and view the contents of directories using the `ls` command in a Linux shell environment.

---

### 📌 **Summary of Key Concepts**

#### 🔹 What is `ls`?

- `ls` is a **command** used to **list directory contents**.
- It is actually a program located at `/bin/ls`.
- When you type `ls`, the shell runs `/bin/ls` to show files and folders in the current or specified directory.

---

### ✅ **1.1 Viewing Files in the Current Working Directory**

**Command:**

```bash
ls
```

**Explanation:**

- This lists all files and directories in your **current working directory**.
- In this lab environment, your current directory is `/home/project`.
- Since it's empty, running `ls` returns nothing (no output).

---

### ✅ **1.2 Viewing Files in Any Directory**

You can list the contents of any directory by specifying its **path**:

**Command:**

```bash
ls [PATH TO DIRECTORY]
```

#### Example:

```bash
ls /
```

- Lists the contents of the **root directory (`/`)**.

#### Common System Directories:

| Directory | Contents                                                |
| --------- | ------------------------------------------------------- |
| `/bin`    | Essential user command binaries (like `ls`, `cp`, `mv`) |
| `/sbin`   | System administration binaries                          |
| `/usr`    | User programs and data                                  |
| `/home`   | Home directories for users                              |
| `/media`  | Mount points for removable media                        |

---

### 🧪 Try These Commands

To explore the system, try these in your terminal:

```bash
ls /              # List root directory contents
ls /bin           # List commands available in /bin
ls /home          # See what users exist (you may see 'project')
ls /etc           # Configuration files
ls /usr/bin       # More user-level command binaries
```

---

### 💡 Tip

- If you want to see **hidden files** (those starting with a dot), use:

  ```bash
  ls -a
  ```

- To get a **detailed list** (including file permissions, size, owner, etc.):
  ```bash
  ls -l
  ```

---

Let me know if you'd like to move on to creating files or navigating directories!

### USER

Exercise 2 - Navigating Directories
cd

In this exercise, you will explore directories using the cd command.

Recall the symbols used to navigate to special paths:

Symbol Stands for path to
~ Home directory
/ Root directory
. Current directory
.. Parent directory
2.1. Changing your present working directory to your home directory
To change your current working directory to your default home directory, use the ~ symbol as follows:

1
cd ~

Copied!
Note that your lab environment's default home directory, ~, is /home/theia. After changing directories to ~, you can check this yourself by entering the pwd command, which displays the path to your current working directory.

2.2. Changing your present working directory to its parent directory
To change your current working directory to the parent directory of your present working directory, enter the following command using ..:

1
cd ..

Copied!
For example, if your working directory was /home/theia, then the new working directory will be /home.

2.3. Changing working directory to root directory
To change your current working directory to the root directory, use the following command with the / key:

1
cd /

Copied!
2.4. Changing your present working directory to a child directory
Assuming you are still in your root directory, use the following command to change your present working directory to the /bin directory:

1
cd bin

Copied!
The /bin directory is called a child of the root directory, /, because it's a subdirectory within it.

The cd command understands implicitly that bin is the name of a subdirectory of your current working directory. As a result, it deduces that its path is a combination of the current working directory path (/) and the subdirectory name (bin).

Another method to change directories is to enter the command cd ./bin. In this case, . represents the path to your current working directory.

Give it a try by entering cd ./bin in your command line! What directory did you end up in?

Tip: If cd ./bin doesn't take you to the /bin directory, double-check what directory you are currently in. Remember, . represents the directory you are in. If you're already in /bin, the terminal will attempt to direct you to /bin/bin.

2.5. Changing from your working directory back to your home directory
There are multiple ways to change your current working directory back to your default home directory. One way is to return to your parent directory, .., and type the address of your home directory /home/theia:

1
cd ../home/theia

Copied!
A simpler way to do this would be to use the ~ symbol to quickly and directly navigate to your home directory:

1
cd ~

Copied!
Both methods will change your working directory back to your home directory.

2.6. Changing from your working directory to your project directory
Directories that are contained within the same parent directory are called siblings.

In this environment, we have provided a special empty project directory for your work. This project directory is located at /home/project and is a sibling directory to /home/theia.

Change your current working directory to its sibling directory, your project directory, by entering the following command:

1
cd ../project

### ASSISTANT

### Exercise 2 - Navigating Directories with `cd`

In this exercise, you're learning how to **change directories** using the `cd` (change directory) command in a Linux shell.

---

### 🧭 Key Navigation Symbols

| Symbol | Meaning                              | Example                      |
| ------ | ------------------------------------ | ---------------------------- |
| `~`    | Your **home directory**              | `cd ~` goes to `/home/theia` |
| `/`    | The **root directory** of the system | `cd /`                       |
| `.`    | The **current directory**            | `cd .` stays where you are   |
| `..`   | The **parent directory**             | `cd ..` moves up one level   |

---

### ✅ **2.1 Changing to Your Home Directory**

```bash
cd ~
```

- This takes you to your **default home directory**, which is typically `/home/theia` in this lab environment.
- To confirm:
  ```bash
  pwd
  ```

---

### ✅ **2.2 Going to the Parent Directory**

```bash
cd ..
```

- Moves **up one level** in the directory hierarchy.
- Example: If you're in `/home/theia`, this will take you to `/home`.

---

### ✅ **2.3 Changing to the Root Directory**

```bash
cd /
```

- Takes you to the **top-level directory** of the file system, called the **root directory**.

---

### ✅ **2.4 Changing to a Child Directory**

#### Method 1: Relative Path

```bash
cd bin
```

- From `/`, this will go to `/bin`.
- Assumes `bin` is a subdirectory of your current working directory.

#### Method 2: Using `.` (Current Directory)

```bash
cd ./bin
```

- Also changes to `/bin` if you're currently in `/`.

> ⚠️ Tip: Make sure you're in the correct parent directory before navigating into a child directory. If you're already in `/bin`, typing `cd ./bin` would try to go to `/bin/bin`, which may not exist.

---

### ✅ **2.5 Returning to Your Home Directory**

#### Option 1: Using `~` (Fastest Way)

```bash
cd ~
```

- Directly returns you to `/home/theia`.

#### Option 2: Using Relative Path

```bash
cd ../home/theia
```

- Goes up to `/home`, then into the `theia` folder.

---

### ✅ **2.6 Navigating to the Project Directory**

```bash
cd ../project
```

- This switches you from `/home/theia` to its **sibling directory**: `/home/project`.
- Useful for moving between related folders inside `/home`.

---

### 📌 Final Tips

- Use `pwd` (Print Working Directory) often to see where you are:
  ```bash
  pwd
  ```
- Combine paths using slashes:
  ```bash
  cd /home/project/myfolder
  ```
- Tab completion helps! Start typing a directory name and press **Tab** to auto-complete.

---

Ready for the next step? Try creating and viewing files using `touch`, `cat`, and `echo`!

### USER

Exercise 3 - Using tab completion and the command history
In this exercise, you will gain familiarity with tab completion and the command history.

3.1. Scrolling through your command history
At the command prompt, simply hit the Up Arrow and Down Arrow keys, ↑ and ↓, to scroll through your command history.

Assuming you are still in the same session as you were when you completed the previous exercises in this lab, you should see exactly what commands you have entered so far.

For example, suppose you want to use the cd command to navigate to /bin again. Rather than retyping the command, simply press the Up Arrow key until you see the cd bin displayed at the command prompt and press Enter.

Of course, this command will only work as expected if your current working directory is the correct one. If the command fails, you can keep scrolling through your history until you find the cd command to return to your root directory, (cd /). Enter that command first, then use the Up Arrow key to find and enter the cd bin command from your history.

Your command history is very useful if you are doing repetitive tasks and want to avoid retyping things repeatedly.

3.2. Using tab completion
Tab completion can save you a lot of typing, thinking, and time. Let's take a look at some examples.

Type cd /bi and press the Tab key. As you might expect, the command autocompletes to cd /bin. But what happens if you just type cd /b and press Tab?

In this case, nothing happens. But if you hit Tab a second time, you'll see a list of all the valid candidates for autocompletion, namely bin/ and boot/.

Notice that cd /b reappears in the command prompt. You cannot use tab completion while there are multiple valid candidates for autocompletion. To narrow down your choices, add an i at the end of your line, then press Tab again. This time the prompt will fill with cd /bin, the only valid option remaining.

Tip: Tab completion only works when there is one valid candidate for autocompletion. When there are multiple possible options, the command prompt will prompt you to enter more letters until there is only one possible option.

You can even use tab completion repeatedly to "dig into" a directory tree.

Let's say you have used tab completion to get to the point where ls /home is displayed at the command prompt. You can press Tab twice to get a listing of all the directories under /home. As you did with cd /bin, use tab completion to complete the address of a subdirectory such as ls /home/theia. You can repeat this process as many times as you like until you reach the end of a chosen path.

As an exercise, practice using tab completion repeatedly to build up the command ls /home/theia/dsdriver/bin.

Future labs will cover command options more in-depth. In this lab, you became familiar with the terminal environment and some basic commands.

### ASSISTANT

### Exercise 3 - Using **Tab Completion** and **Command History**

In this exercise, you learned two powerful tools to make working in the terminal **faster**, **easier**, and **less error-prone**:

- 🔁 **Command history**
- ✨ **Tab completion**

---

## 🔄 3.1 Scrolling Through Command History

You can easily **review and reuse** previously entered commands using:

| Key              | Action                 |
| ---------------- | ---------------------- |
| `↑` (Up Arrow)   | Go back one command    |
| `↓` (Down Arrow) | Go forward one command |

### Example:

If you previously typed:

```bash
cd /
cd bin
ls
```

Then pressing `↑` will bring back `ls`, then `cd bin`, then `cd /`, etc.

### Use Case:

Let's say you want to run `cd bin` again:

- Instead of retyping it, press `↑` until you see `cd bin`
- Press `Enter` to execute it again

> 💡 If the command doesn't work because your current directory changed, keep scrolling until you find `cd /`, run that first, then try `cd bin`.

---

## 🧠 3.2 Using Tab Completion

**Tab completion** helps you type faster by auto-filling file and directory names.

### How It Works:

#### Step-by-step example:

1. Type:
   ```bash
   cd /bi
   ```
2. Press **`Tab`**
   - It autocompletes to:
     ```bash
     cd /bin
     ```

#### What if there are multiple matches?

Try typing:

```bash
cd /b
```

Then press **`Tab`** once → nothing happens  
Press **`Tab`** twice → You'll see options like:

```
bin/   boot/
```

Now add an `i`:

```bash
cd /bi
```

Press **`Tab`** again → completes to:

```bash
cd /bin
```

### Tip:

- **Double-tab (`Tab + Tab`)** shows all possible completions.
- Only works when there’s **one match** or you're asking for help with ambiguous paths.

---

## 🛠️ Practice: Digging Into a Path Using Tab Completion

Let’s build a longer command using tab completion:

Start typing:

```bash
ls /ho
```

Press **Tab** → becomes:

```bash
ls /home/
```

Now type:

```bash
ls /home/the
```

Press **Tab** → becomes:

```bash
ls /home/theia
```

Keep going:

```bash
ls /home/theia/dsdriver/bi
```

Press **Tab** → becomes:

```bash
ls /home/theia/dsdriver/bin
```

This way, you built:

```bash
ls /home/theia/dsdriver/bin
```

...without typing the whole thing!

---

### ✅ Summary of Tips

| Feature          | Shortcut    | Description                        |
| ---------------- | ----------- | ---------------------------------- |
| Command History  | `↑` / `↓`   | Scroll through previous commands   |
| Tab Completion   | `Tab`       | Auto-complete file/directory names |
| Show Options     | `Tab + Tab` | List possible completions          |
| Speed & Accuracy | Mix of both | Avoid typos and save time          |

---

### 🚀 Next Steps

Now that you’ve mastered navigating directories and using helpful shell features like **history** and **tab completion**, you’re ready to start creating and editing files, viewing content, and managing permissions!

Would you like help with:

- Creating files with `touch`, `echo`, or `nano`?
- Viewing file contents with `cat`, `less`, or `head`?
- Managing permissions with `chmod`?

Let me know how I can assist!

### USER

Exercise 1 - Upgrading and installing packages
In your lab environment, we provide you access to a system admistration utility called "super-user do", or sudo.

Although this sandbox environment will not require a password to run the sudo command, typical Linux production-oriented environments will require a password to run sudo.

You will need to use the sudo command to activate the powerful apt command. You'll use apt to upgrade nano to its latest version. You will also use apt to install Vim.

apt (Advanced Packaging Tool) is a powerful command line tool. You use it to perform system administration operations such as installing software packages, upgrading existing packages, and updating your system's package list index.

1.1 Updating your Linux sytem's package list index
Before installing or upgrading any packages on your Linux system, it's best practice to first update your package list index. Go ahead and enter this command,

1
sudo apt update

Copied!
to update (re-synchronize) your package index files from their sources. This will take a bit of time to run. While you're waiting, if you're interested, go ahead and open another terminal and view the locations apt uses to access those sources in the file /etc/apt/sources.list.

In short, running apt with the update option ensures all of your package dependencies are up-to-date and correctly specified prior to making any changes to your system's packages.

1.2. Upgrading nano
nano is a simple command line editor that enables you to use the terminal window as a text editor.

nano is already installed on your system. Go ahead and upgrade to the latest supported version of nano by entering:

1
sudo apt upgrade nano

Copied!
You may be prompted: Do you want to continue? [Y/n]

Type Y and press Enter to continue. Updating nano will take some time to complete.

The capital Y in Y/n (yes or no) means "yes" is the default - if you press Enter without typing anything, the terminal assumes you are choosing "yes".

Note: If you encounter a colon (:) similar to the one highlighted in the screenshot while upgrading Nano, please press 'q' to exit and continue with the upgrade process.

You'll get to use nano soon, but first, let's take a look at the other main use case for apt, installing packages.

1.3. Installing Vim
Another popular text-editing program is Vim. Vim is a highly configurable text editor built for efficiency. It takes some practice to get good at using Vim, but the time investment is very worthwhile.

Because Vim isn't preinstalled on your Linux system, you'll need to install it yourself. If you haven't already done so in this session, ensure you run the command sudo apt update. Then to install Vim, enter the following command:

1
sudo apt install vim

Copied!
Similar to when you updated nano, you may again be prompted: Do you want to continue? [Y/n]

Type Y and press Enter to continue. Vim will begin installing on your system.

In a few exercises, you will use Vim to edit a text file.

### ASSISTANT

### Exercise 1 - Upgrading and Installing Packages with `apt`

In this exercise, you learned how to use the **`sudo`** command along with **`apt`**, a powerful package management tool in Linux. You used it to:

- Update your system's package list
- Upgrade an existing package (`nano`)
- Install a new package (`vim`)

---

## 🔐 1.1 Updating Your System’s Package List Index

### Command:

```bash
sudo apt update
```

### What It Does:

- Fetches the latest list of available packages and their versions from configured repositories.
- Ensures that your system knows about the most recent software updates and dependencies.

> 🕒 This command may take a few moments to complete.  
> 💡 You can view the repository sources at `/etc/apt/sources.list`.

---

## ✏️ 1.2 Upgrading `nano`

### Command:

```bash
sudo apt upgrade nano
```

### What Happens:

- Upgrades the already installed `nano` text editor to the latest version.
- You'll be prompted:
  ```
  Do you want to continue? [Y/n]
  ```
- Press **`Y`** then **Enter** to proceed.

> ⚠️ If you see a `:` prompt during the process (like in a pager), press **`q`** to quit and continue.

---

## 💾 1.3 Installing `vim`

### Command:

```bash
sudo apt install vim
```

### Why Vim?

- Vim is a highly configurable, powerful text editor.
- Ideal for editing files directly in the terminal.
- Widely used by developers and system administrators.

### Installation Steps:

1. Run:
   ```bash
   sudo apt install vim
   ```
2. Confirm with:
   ```
   Do you want to continue? [Y/n]
   ```
   Type **`Y`** and press **Enter**

> 🧠 Note: Always run `sudo apt update` before installing or upgrading packages to ensure you're getting the latest software versions.

---

## 📌 Summary Table

| Task                              | Command                 |
| --------------------------------- | ----------------------- |
| Update package list               | `sudo apt update`       |
| Upgrade a package (e.g., nano)    | `sudo apt upgrade nano` |
| Install a new package (e.g., vim) | `sudo apt install vim`  |

---

## 🧪 Quick Tips

- To check if a package is installed:
  ```bash
  which nano
  ```
- To view the version of a program:
  ```bash
  nano --version
  vim --version
  ```

---

You’re now ready to start editing files using both **Nano** and **Vim**! Would you like to try creating and editing files next?

### USER

Exercise 2 - Creating and editing files with nano
In this exercise, you will use the command line editor nano to create and edit a file.

nano is known for being a simple and easy-to-master text editor. Vim is harder to learn, but it has many expert-level features that nano doesn't offer.

2.1 Navigating to the project directory
We provide you with an empty project directory at /home/project. Ensure you're working in this folder by changing directories using the command:

1
cd /home/project

Copied!
Try auto-completing the path by typing cd /home/pr and pressing the Tab key.

If you enter ls here, you shouldn't see any files or subdirectories listed.

2.2 Creating and editing a text file with nano
To create a new file, enter

1
nano hello_world.txt

Copied!
in the terminal. This will simultaneously create a new file called hello_world.txt and enable you to begin editing it using the nano text editor.

Double-check that your new file was created by opening another terminal window and running the ls command on /home/project. You should see hello_world.txt listed.

In your nano terminal, whatever you type will be added to your text buffer, where text is stored until you save it. Type the following text in your nano terminal:

1
Hello world!

Copied!
This will create the text Hello world! in your text buffer.

To create another line of text, press Enter. In your new line, type

1
This is the second line of my first-ever text file created with nano.

Copied!
to create a second line of text in your text buffer.

Now:

Press CTRL+X to exit nano.

You will be prompted as follows:

1
2
3
Save modified buffer (ANSWERING "No" WILL DESTROY CHANGES) ?  
 Y Yes  
 N No ^C Cancel

Copied!
Press Y to save your new lines of text to your file.

Press Enter to confirm the file name.
At this point, nano should have exited and returned you to the command prompt.

2.3 Verifying your new text file
By entering a familiar command, such as

1
cat hello_world.txt

Copied!
you should be able to inspect and verify that your new file contains the two lines you wrote to it with nano. Cool!

### ASSISTANT

### Exercise 2 - Creating and Editing Files with `nano`

In this exercise, you learned how to **create and edit files** using the `nano` text editor from the command line.

---

## 🧭 2.1 Navigating to Your Project Directory

### Command:

```bash
cd /home/project
```

### Tip: Use Tab Completion

You can type:

```bash
cd /home/pr
```

Then press **Tab**, and it will auto-complete to:

```bash
cd /home/project
```

Once there, verify with:

```bash
ls
```

- This shows the contents of your directory.
- Since it’s empty at first, you won’t see anything yet.

---

## ✏️ 2.2 Creating and Editing a File with `nano`

### Create a new file:

```bash
nano hello_world.txt
```

This opens the `nano` editor and creates the file.

### Inside Nano:

1. Type:
   ```
   Hello world!
   ```
2. Press **Enter**
3. Type:
   ```
   This is the second line of my first-ever text file created with nano.
   ```

### Save and Exit:

- Press **CTRL + X** to exit
- You'll be prompted:
  ```
  Save modified buffer?  Y Yes   N No   ^C Cancel
  ```
- Press **Y** to save
- Confirm the filename by pressing **Enter**

Nano saves the file and returns you to the terminal.

---

## 🔍 2.3 Verifying Your File Content

To view the contents of your file:

```bash
cat hello_world.txt
```

You should see:

```
Hello world!
This is the second line of my first-ever text file created with nano.
```

✅ Success! You've just created and edited your first file in Linux using `nano`.

---

## 📋 Summary of Commands

| Action                        | Command                            |
| ----------------------------- | ---------------------------------- |
| Navigate to project directory | `cd /home/project`                 |
| Create/edit a file with nano  | `nano hello_world.txt`             |
| Save and exit in nano         | `CTRL + X`, then `Y`, then `Enter` |
| View file contents            | `cat hello_world.txt`              |

---

🧠 **Pro Tip:**  
If you ever get stuck inside `nano`, remember:

- Use **arrow keys** to navigate
- Look at the bottom of the screen for shortcut hints like `^X` (CTRL+X)

---

Would you like to try editing files with **Vim** next, or explore more ways to view and manage files?

### USER

Exercise 3 - Creating and editing files with Vim
3.1 Quick intro to Vim
Recall that Vim has two basic modes: Insert mode, where you enter text, and Command mode, where you do everything else. You can start Vim simply by entering

1
vim

Copied!
at the command prompt, which displays something like the following in your terminal window:

VIM screen with help commands

Notice that you can get help on Vim by entering :help, and you can quit Vim by entering :q.

Go ahead and enter :help. This brings up an informative help file you can scroll through.

VIM help file

When you are done reading, simply enter :q to quit Vim and return to the command prompt.

Vim is very powerful and takes some time to learn. We're just covering the very basics here and leaving it to you to explore further. Check out the official Vim site at https://www.vim.org .

3.2 Creating and editing a text file with Vim
Begin by navigating back to your /home/project directory if you aren't already there.

Type the command,

1
vim hello_world_2.txt

Copied!
to create a new file called hello_world_2.txtand edit it using Vim.

Once your Vim session has started, go ahead and press i to enter Insert mode. This is the mode where you can enter and delete text in the text buffer.

Go ahead and type some text in the buffer, for example:

1
Hello World!

Copied!
Just like in nano, press Enter to start a new line, and then type

1
This is the second line.

Copied!
to create a second line of text in the buffer.

When you're done typing text in the buffer, press the Escape key, Esc, to exit the Insert mode. This brings you to Command mode.

In Vim, it's easy to accidentally end up in a mode you didn't intend to be in. No worries - you can use the Esc key to return to Command mode.

Now that you are back in Command mode, you can save your work by entering the command :w. This writes the contents of the text buffer to your text file.

Finally, you can exit your Vim session by entering :q.

### ASSISTANT

### Exercise 3 - Creating and Editing Files with **Vim**

In this exercise, you learned how to use **Vim**, a powerful and highly configurable text editor that is widely used in Linux environments. Vim uses different **modes** for editing and executing commands.

---

## 🧭 3.1 Quick Intro to Vim

### Launching Vim

To start Vim:

```bash
vim
```

You’ll see something like:

```
VIM - Vi IMproved
...
:type :q<Enter> to exit
:type :help<Enter> for on-line help
```

### Basic Commands

| Mode                  | Action                    | Command |
| --------------------- | ------------------------- | ------- |
| Normal (Command) Mode | Open help                 | `:help` |
| Normal Mode           | Quit Vim                  | `:q`    |
| Any Mode              | Force quit without saving | `:q!`   |
| Normal Mode           | Save file                 | `:w`    |
| Normal Mode           | Save and quit             | `:wq`   |

#### Try It:

- Enter `:help` to explore the built-in documentation.
- Press `Esc` to make sure you're in **Normal Mode**.
- Type `:q` to exit help or `:q!` to exit Vim without saving changes.

> 💡 Tip: If you ever get stuck in Vim, press `Esc`, then type `:q!` to safely exit without saving.

---

## ✏️ 32.2 Creating and Editing a Text File with Vim

### Step-by-step Instructions:

#### 1. Navigate to your project directory:

```bash
cd /home/project
```

Use tab completion if possible:

```bash
cd /home/pr<TAB>
```

#### 2. Create and open a new file:

```bash
vim hello_world_2.txt
```

This opens a new blank file in **Normal Mode**.

#### 3. Switch to Insert Mode:

Press:

```
i
```

Now you can type into the file.

#### 4. Add content:

Type:

```
Hello World!
```

Press **Enter** to go to the next line, then type:

```
This is the second line.
```

#### 5. Exit Insert Mode:

Press:

```
Esc
```

You’re now back in **Normal Mode**.

#### 6. Save the file:

Type:

```
:w
```

This writes (saves) the contents of the buffer to the file.

#### 7. Quit Vim:

Type:

```
:q
```

You’ll return to the command prompt.

---

## 🔍 Verify Your File Was Saved

Use the `cat` command to view the contents:

```bash
cat hello_world_2.txt
```

You should see:

```
Hello World!
This is the second line.
```

✅ Congratulations! You've created and edited a file using **Vim**.

---

## 📋 Summary of Key Commands in Vim

| Task                | Command            |
| ------------------- | ------------------ |
| Start Vim           | `vim filename.txt` |
| Enter Insert Mode   | `i`                |
| Exit Insert Mode    | `Esc`              |
| Save file           | `:w`               |
| Save and quit       | `:wq`              |
| Quit without saving | `:q!`              |
| Get help            | `:help`            |
| Quit help           | `:q`               |

---

🧠 **Pro Tips:**

- Always press `Esc` before typing `:` to ensure you're in **Normal Mode**.
- Vim has many modes: **Normal**, **Insert**, **Visual**, and more — we only covered the basics here.
- To learn more about Vim, visit [https://www.vim.org](https://www.vim.org), where you'll find tutorials, plugins, and tips from the community.

Would you like to try comparing files, viewing differences, or exploring more advanced Vim features?

### USER

Summary
Congratulations! You've just gained a lot more hands-on experience with the Linux terminal!

By now you are beginning to understand a lot more about how your Linux system functions. In this lab, you learned how to:

Perform some fundamental sys admin operations, such as updating your package list, upgrading existing packages, and installing new packages
Create and edit a few text files using some serious command-line text editors, nano and Vim
Understand how the Bash scripting language can be used to interpret commands you include within a text file
Keep up the great work! We still have many more exciting things for you to explore, and we hope your enthusiasm for Linux is growing!

As usual, if you ever feel like you might have missed anything important or just want some extra practice, you can always return to this lab again. Explore and experiment to your heart's content.

### ASSISTANT

### 🎉 **Summary: Great Job Completing the Lab!**

You've just taken a big step in mastering essential Linux skills. Here's what you accomplished:

---

### 🔧 **System Administration Skills**

You learned how to manage software on your system using `apt` and `sudo`:

- ✅ Updated package list:
  ```bash
  sudo apt update
  ```
- ✅ Upgraded an existing package (`nano`):
  ```bash
  sudo apt upgrade nano
  ```
- ✅ Installed a new package (`vim`):
  ```bash
  sudo apt install vim
  ```

These are foundational skills for maintaining and customizing any Linux environment.

---

### 📝 **Text Editing with Nano and Vim**

You created and edited files using two powerful command-line editors:

- ✏️ **Nano** – beginner-friendly, great for quick edits
  - Created and saved `hello_world.txt`
  - Viewed content using `cat hello_world.txt`
- 💻 **Vim** – powerful and efficient once you learn the modes
  - Created and saved `hello_world_2.txt`
  - Practiced switching between **Insert Mode** and **Command Mode**

This gives you flexibility depending on your use case or preference!

---

### 🖥️ **Bash Shell Proficiency**

Throughout this lab, you became more comfortable with:

- 🧭 Navigating directories using `cd`, `pwd`, and tab completion
- 📁 Listing contents of directories using `ls`
- ⏳ Reusing commands via the **command history** (`↑` / `↓`)
- 🚀 Saving time with **tab auto-completion**
- 💾 Viewing file contents with `cat`

These skills will help you become fluent in the terminal — the heart of Linux system administration and development.

---

### 🌱 What’s Next?

Here are some great next steps to continue building your Linux expertise:

#### 🔍 File Management:

- Learn how to copy, move, and delete files with `cp`, `mv`, and `rm`
- Explore directory trees using `tree` (install it if needed!)

#### 🛠️ Advanced Vim:

- Practice more Vim navigation and editing shortcuts
- Try out visual mode, search/replace, and macros

#### 📊 File Comparison:

- Use `diff` to compare files
- Try `less`, `head`, and `tail` to view large files

#### 🧪 Scripting:

- Start writing your first **Bash script** using `nano` or `vim`
- Make it executable with `chmod +x myscript.sh`

---

### 🙌 Final Words

You're well on your way to becoming confident and proficient in Linux. The more you explore, experiment, and practice, the more natural these tools will feel.

Remember: **The terminal is not scary — it's powerful.** And now, it's yours to master.

If you'd like guided exercises on any of the topics above, just say the word! 👨‍💻✨

### USER

Module 1 Cheat Sheet - Introduction to Linux
Linux terminal tips
Use tab completion to autocomplete pathnames and command names.

Scroll through your command history with the Up Arrow and Down Arrow keys to find and re-run a command you already used.

Getting information
Display the reference manual for the ls command:
1
man ls

Copied!
Browsing and navigating directories
Special paths
Symbol Represents path to
~ home directory
/ root directory
. present working directory
.. parent of present working directory
List files and directories in the current directory:
1
ls

Copied!
List files and directories in a directory:
1
ls path_to_directory

Copied!
Return path to present working directory:
1
pwd

Copied!
Change the current directory to a subdirectory:
1
cd child_directory_name

Copied!
Tip: Because cd looks in the current directory for child_directory_name, you don’t need to type the entire path.

Change the current directory:
Up one level: cd ../

To home: cd ~ or cd

To some other directory: cd path_to_directory

Change the current directory to another one at the same level:
Suppose you have two sibling directories within the same directory, dir_1 and dir_2, and your present working directory is dir_1. To switch to dir_2, enter:

cd ../dir_2

Tip: Using .., you don't need to know the path to the parent directory to switch to a sibling.

Change the current directory back to the directory you were in previously:
cd -

Upgrading and installing packages
Fetch and display up-to-date information about all upgradable packages:
1
sudo apt update

Copied!
Upgrade to the latest supported version of nano:
1
sudo apt upgrade nano

Copied!
Install Vim:
1
sudo apt install vim

Copied!
Creating and editing files
Create a new text file and open it with nano:
1
nano file_name.txt

Copied!
Tip: If the file already exists, nano simply opens it for editing.

### ASSISTANT

# 📄 **Module 1 Cheat Sheet – Introduction to Linux**

This cheat sheet summarizes the essential commands and concepts covered in this module. Keep it handy for quick reference while working in the Linux terminal.

---

## 🔧 **Linux Terminal Tips**

| Task                           | Command              |
| ------------------------------ | -------------------- |
| Autocomplete path or command   | `Tab` key            |
| Scroll through command history | `↑` / `↓` arrow keys |

---

## ❓ **Getting Information**

| Task                                   | Command  |
| -------------------------------------- | -------- |
| View manual for a command (e.g., `ls`) | `man ls` |

---

## 🗂️ **Browsing and Navigating Directories**

### 🧭 Special Path Symbols

| Symbol | Meaning             |
| ------ | ------------------- |
| `~`    | Your home directory |
| `/`    | Root directory      |
| `.`    | Current directory   |
| `..`   | Parent directory    |

### 📁 Directory Commands

| Task                                 | Command                   |
| ------------------------------------ | ------------------------- |
| List contents of current directory   | `ls`                      |
| List contents of another directory   | `ls path_to_directory`    |
| Show current working directory       | `pwd`                     |
| Change to a subdirectory             | `cd child_directory_name` |
| Move up one directory level          | `cd ../`                  |
| Go to your home directory            | `cd ~` or just `cd`       |
| Go to root directory                 | `cd /`                    |
| Switch to a sibling directory        | `cd ../sibling_dir_name`  |
| Return to previous working directory | `cd -`                    |

---

## 📦 **Upgrading and Installing Packages**

> Use `sudo` to run administrative commands.

| Task                                     | Command                 |
| ---------------------------------------- | ----------------------- |
| Update package list                      | `sudo apt update`       |
| Upgrade an existing package (e.g., nano) | `sudo apt upgrade nano` |
| Install a new package (e.g., vim)        | `sudo apt install vim`  |

---

## ✏️ **Creating and Editing Files**

| Task                            | Command              |
| ------------------------------- | -------------------- |
| Create or edit a file with nano | `nano file_name.txt` |
| Create or edit a file with vim  | `vim file_name.txt`  |

### 💻 Vim Modes Reminder

- **Normal Mode**: Press `Esc` – use for navigation and commands
- **Insert Mode**: Press `i` – use for typing/editing text

#### Common Vim Commands (in Normal Mode):

| Action              | Command |
| ------------------- | ------- |
| Save (write) file   | `:w`    |
| Quit                | `:q`    |
| Save and quit       | `:wq`   |
| Quit without saving | `:q!`   |
| Get help            | `:help` |

---

## 🙌 You're Off to a Great Start!

This cheat sheet gives you all the tools you need to begin exploring and managing files and packages in Linux confidently.

Need more practice or want to dive into scripting, permissions, or advanced navigation? Just ask — I'm here to help! 🐧💻

### USER

Summary & Highlights
Congratulations! You have completed this module. At this point, you know that:

In the 1980s, GNU was developed at MIT. GNU stands for “GNU’s not Unix” and was made as a free, open source set of the existing Unix system tools. And in 1991, Linus Torvalds developed a free, open source version of the Unix kernel called Linux.

Linux is widely used today in mobile devices, desktops, supercomputers, data centers, and cloud servers.

Linux distributions (also known as distros) differ by their UIs, shell applications, and how the OS is supported and built.

The design of a distro is catered toward its specific audience and/or use case. Popular Linux distributions include Red Hat Enterprise Linux (RHEL), Debian, Ubuntu, Suse (SLES, SLED, OpenSuse), Fedora, Mint, and Arch.

The Linux system consists of five key layers: the UI, application, OS, kernel, and hardware. The user interface enables users to interact with applications. Applications enable users to perform tasks within the system. The operating system runs on top of the kernel and is vital for system health and stability, and the kernel is the lowest-level software that enables applications to interact with hardware. Hardware includes all the physical or electronic components of your PC.

The Linux filesystem is a tree-like structure consisting of all directories and files on the system.

A Linux shell is an OS-level application that you can use to enter commands. You use a terminal to send commands to the shell, and you can use the `cd` command to navigate around your Linux filesystem.

You can use a variety of command-line or GUI-based text editors such as GNU nano, vim, vi, and gedit.

.deb and .rpm are distinct file types used by package mangers in Linux operating systems.

You can use GUI-based and command-line package managers to update and install software on Linux systems.

### ASSISTANT

### 🎉 **Summary & Highlights – Module Complete!**

Great job completing this module! You've built a solid foundation in **Linux fundamentals**, from its history to core components and practical tools. Here's a concise recap of what you’ve learned:

---

## 🕰️ **A Brief History of Linux**

- **GNU Project** (1980s):  
  Developed at MIT as a free, open-source alternative to Unix — meaning "GNU’s Not Unix".
- **Linux Kernel** (1991):  
  Created by **Linus Torvalds** — a free, open-source Unix-like kernel that became the heart of modern Linux OS.

---

## 💻 **Where Is Linux Used Today?**

Linux powers:

- 📱 Mobile devices (e.g., Android)
- 🖥️ Desktop computers
- 🌐 Servers (including most web servers)
- 🚀 Supercomputers
- ☁️ Cloud infrastructure

Its flexibility and stability make it ideal for both personal and enterprise environments.

---

## 🧩 **Linux Distributions (Distros)**

Different flavors of Linux tailored to specific needs:

| Distribution                        | Use Case                                 |
| ----------------------------------- | ---------------------------------------- |
| **Ubuntu**                          | Beginner-friendly, desktop and server    |
| **Debian**                          | Stable, community-driven                 |
| **Fedora**                          | Cutting-edge features, developer-focused |
| **Red Hat Enterprise Linux (RHEL)** | Enterprise use, commercial support       |
| **SUSE (SLES/SLED/OpenSUSE)**       | Enterprise and development               |
| **Linux Mint**                      | Easy for Windows users to switch         |
| **Arch**                            | DIY-oriented, rolling release model      |

Each distro varies in:

- User interface (UI)
- Package management
- Support structure
- Target audience

---

## 🏗️ **The Five Layers of Linux Architecture**

1. **User Interface (UI)**: Where users interact with applications.
2. **Applications**: Programs used to perform tasks (e.g., browsers, editors).
3. **Operating System**: Manages system resources and ensures smooth operation.
4. **Kernel**: The core of Linux; handles communication between software and hardware.
5. **Hardware**: Physical components like CPU, memory, disk drives.

> Everything runs on top of the **kernel**, which is the bridge between your apps and your computer’s physical components.

---

## 📁 **Filesystem Overview**

- Linux uses a **tree-like hierarchical filesystem**.
- Starts from the **root directory (`/`)**.
- Common directories:
  - `/bin` – essential commands
  - `/etc` – configuration files
  - `/home` – user directories
  - `/usr` – user programs
  - `/var` – variable data (logs, caches)

---

## 🖥️ **Shell and Terminal Basics**

- A **shell** is a command-line interpreter (e.g., Bash).
- You interact with the shell via a **terminal emulator**.
- Key navigation commands:
  - `cd` – change directory
  - `ls` – list contents
  - `pwd` – show current path
  - `man` – view manual pages

---

## ✍️ **Text Editors in Linux**

You can edit files using:

- 🖋️ Command-line editors:
  - `nano` – beginner-friendly
  - `vim` / `vi` – powerful but has a learning curve
- 🖼️ GUI-based editors:
  - `gedit`
  - `Kate`
  - VS Code (available on Linux)

---

## 📦 **Package Management**

Two major package formats:

- `.deb` – used by Debian, Ubuntu, and derivatives
- `.rpm` – used by Red Hat, Fedora, SUSE, and others

Common package managers:

- **APT** (Advanced Packaging Tool) – used in Debian/Ubuntu
- **YUM/DNF** – used in RHEL/Fedora

Basic commands:

```bash
sudo apt update       # Update package list
sudo apt upgrade      # Upgrade packages
sudo apt install      # Install new packages
```

---

## 🧠 Final Thoughts

You now understand:

- The origins and evolution of Linux
- How Linux powers today’s digital world
- The structure of a Linux system
- How to navigate the terminal
- How to manage packages and edit files

This sets the stage for deeper exploration into scripting, permissions, networking, containers, and more!

---

📘 **Ready for the Next Module?**  
Let me know if you'd like to dive into:

- Shell scripting
- File permissions
- Process management
- Networking basics  
  Or any other topic you're curious about!

Keep up the awesome work — Linux mastery is within your reach! 🐧🚀

### USER

Getting Help for Linux Commands
There is huge value in spending time exploring and experimenting with commands, but there are many things you can't figure out just by experimenting. You need to see what's out there, see what's possible, and learn where to look to get answers. Let's take a look at some great ways to get the information you need to help you make progress.

In this reading, you may see links to external sources. You can open them by right-clicking and pressing "Open in new tab."

1. Use the built-in man command
   The man command, which stands for "manual", provides the standard way to access help for Unix-like commands from the command prompt. It has been in development since 1971.

You can get a listing of all the commands on your system that have a manual page by entering:

1
man -k .

Copied!
The resulting list includes a brief description of what each command does.

To see the man page for a command, simply enter:

1
man command_name

Copied!
All man pages are divided into several sections, including:

NAME
The name of the command or feature and a brief description of what it does.

SYNOPSIS
A summary of the command syntax, including any options and arguments that can be used.

DESCRIPTION
A more detailed description of the command, including its function and behavior.

OPTIONS
All the available options and arguments that can be used with the command.

EXAMPLES
Some examples of how to use the command.

SEE ALSO
Related commands and documentation that may be helpful.

You may also see other sections, including: EXIT STATUS, RETURN VALUE, ENVIRONMENT, BUGS, FILES, AUTHOR, REPORTING BUGS, HISTORY, and COPYRIGHT.

2. Install and use the tldr command
   Similar to man pages, TLDR Pages is a free and open-source collaborative documentation effort. The goal is to create documentation that is more accessible than the traditional man pages, which tend to be quite verbose.

TLDR Pages, short for "Too Long; Didn't Read" and also known simply as tldr, provide examples for common use cases of various commands. The format of TLDR pages is similar to that of a cheatsheet.

You can install a command-line tool to access TLDR Pages from your terminal. Install it using the following command:

1
npm install -g tldr

Copied!
Once you've installed the tool, you can use the tldr command to easily access the TLDR page of a command.

1
tldr command_name

Copied!
The tool will display a short, easy-to-understand summary of the command along with some examples of how to use it.

3. Search Stack Overflow
   Stack Overflow is a popular community-driven question and answer platform for programmers, developers, and system administrators. It has a vast repository of questions and answers related to various programming languages, tools, and operating systems, including Linux.

To search for information about commands on Stack Overflow, you can use the search bar on the homepage and enter the name of the command you're looking for, along with any specific keywords or parameters. You can also refine your search by adding relevant tags, such as "linux" or "command-line".

Once you've entered your search query, Stack Overflow will display a list of relevant questions and answers that match your query. You can browse through the results to find the information you need, and even post your own question if you can't find an answer to your specific query.

When searching for information about commands on Stack Overflow, it's important to check the date of the answers to ensure that the information is still current and relevant. You should also read through the comments and discussion threads to get a better understanding of the context and any potential issues or limitations related to the command you're researching.

Newest questions on Stack Overflow tagged "Linux": https://stackoverflow.com/questions/tagged/linux

4. Search Stack Exchange
   Stack Exchange is a network of question and answer communities, similar to Stack Overflow, but covering a broader range of topics beyond just programming. There are several Stack Exchange communities that specialize in topics related to Linux and open source software, such as Unix & Linux, Ask Ubuntu, and Server Fault.

Visit the relevant community to search for information on Stack Exchange. Like Stack Overflow, you can use the search bar to enter the name of the command you're looking for, along with any keywords or parameters.

Unix and Linux community on Stack Exchange: https://unix.stackexchange.com/

5. Just google it!
   Google is a powerful tool that can provide you the answer to almost any question. Learn how to enter the right queries and filter your results, such as by including "Wikipedia", "Stack Overflow", or "Linux" as part of your search. However, use at your own risk. Never blindly trust what you find on the web - there's a lot of noise out there!

6. Use the cheat sheets from this course
   Throughout this course, you will encounter "cheat sheets" that condense the information you've learned into easy-to-reference guides. They are great for reviewing the material you've learned and can also help you out with your graded assignments.

7. Refer to Wikipedia's list of Unix commands:
   Finally, Wikipedia maintains a list of commands that can be found on Unix operating systems, along with a short description. You can check the page to quickly reference a Unix command: https://en.wikipedia.org/wiki/List_of_Unix_commands

Summary
This reading has provided an overview of how to find more information about Linux commands. As you continue to use commands in this course and beyond, you'll likely find yourself using the same command patterns over and over. Each time you use a command, you'll get a little more comfortable and familiar with it. Your fingers will develop muscle memory until using commands becomes second nature!

### ASSISTANT

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

## 🙌 Final Thoughts

As you continue exploring Linux:

- Build your own **reference notes**
- Bookmark useful resources
- Practice using `man` and `tldr` regularly
- Engage with communities like Stack Overflow and Stack Exchange

Remember: **no one knows everything about Linux** — the key is knowing **where to look** when you need help.

Let me know if you'd like a printable version of this guide or a custom cheat sheet for specific commands! 🐧📘

### USER

Exercise 1 - Informational Commands
In this exercise, you will familiarize yourself with useful commands for providing system and user information.

1.1. Display the name of the current user
whoami

Enter the whoami command to return your current username.

1
whoami

Copied!
It will display the user name as theia because you are logged into this lab as theia.

You can get a list of currently logged in users using the command who, but this command doesn't work in the Theia environment yet.

1.2. Get basic information about the operating system
uname

By default the command prints the kernel name. The u in uname refers to "unix-like 0S".

1
uname

Copied!
If you enter the command uname, you will see Linux printed in the output.

Using the -a option prints all the system information.

1
uname -a

Copied!
You will see system information listed in the following order:

Kernel name
Network node hostname
Kernel release date
Kernel version
Machine hardware name
Hardware platform
Operating system
1.3. Obtain the user and group identity information
id

This command displays the user id and group id information of the current user.

1
id

Copied!
It will display the uid (user id) and gid (group id) for the user theia.

1.4 Get available disk space
df

The df command is used to display available disk space.

1
df

Copied!
This command will display available disk space in 512-byte blocks. To get available disk space in a "human-readable" format, enter:

1
df -h

Copied!
This will return the available disk space in units like gigabytes and terabytes.

1.5. View currently running processes
ps

The ps command lists each process that is currently running and its PID (process id).

1
ps

Copied!
However, the output only contains the processes that are owned by you.

By using the -e option, you can display all of the processes running on the system. The includes processes owned by other users.

1
ps -e

Copied!
1.6. Get information on the running processes and system resources
top

The top or "table of processes" command provides a dynamic, real-time view of your system.

1
top

Copied!
The top command displays a table of detailed information related to the processes or threads which are currently running and managed by the kernel. Additionally, it also provides information related to CPU and memory usage per process.

When you start top, you'll be presented with the following elements on the main top screen:

Summary area - shows information like system uptime, number of users, load average, and overall memory usage
Column header - attribute names
Task area - displays the data for each process, or PID
The output keeps refreshing until you press q or Ctrl + c.

If you want to exit automatically after a specified number of repetitions, use the -n option as follows:

1
top -n 10

Copied!
You can press the following keys with Shift while top is running to sort the table:

Key Sorts by
m Memory Usage
p CPU Usage
n Process ID (PID)
t Running Time
For example, you can find out which process is consuming the most memory by entering Shift + m.

1.7. Display Messages
echo

The echo command displays the given text on the screen. For example, entering:

1
echo "Welcome to the linux lab"

Copied!
prints:

1
Welcome to the linux lab.

Copied!
These special characters help you better format your output:

Special Character Effect
\n Start a new line
\t Insert a tab
Use the -e option of the echo command when working with special characters. For example:

1
echo -e "This will be printed \nin two lines"

Copied!
will print:

1
2
This will be printed
in two lines

Copied!
1.8. Display date and time
date

The date command displays the current date and time.

1
date

Copied!
It has several options which allow you to display the current date and time in different formats.

For example, the following command displays the current date in mm/dd/yy format:

1
date "+%D"

Copied!
Here are some popular format specifiers that you can try out:

Specifier Explanation
%d Displays the day of the month (01 to 31)
%h Displays the abbreviated month name (Jan to Dec)
%m Displays the month of year (01 to 12)
%Y Displays the four-digit year
%T Displays the time in 24 hour format as HH:MM:SS
%H Displays the hour
1.9. View the Reference Manual For a Command
man

The man command displays the user manual for any command that you provide as its argument.

For example, to see the manual page for the ls command, enter:

1
man ls

Copied!
Scroll through the command's manual to find any info you may need. When you're done, press q to quit.

You will sometimes encounter a command that does not have a man page avaible on your system. To see all available man pages with a brief description of each command, enter:

1
man -k .

### ASSISTANT

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

You now have a solid toolkit of **informational commands** that will help you understand and manage your Linux system effectively.

Ready to move on to file management, scripting, or permissions? Let me know — I'm here to guide you further! 🐧🚀

### USER

Practice exercises

1. Get basic information about the operating system.
   Click here for Hint
   Click here for Solution
2. View all running processes on the system.
   Click here for Hint
   Click here for Solution
3. Get the table of processes and sort by memory usage.
   Click here for Hint
   Click here for Solution
4. Display the current time.
   Click here for Hint
   Click here for Solution
5. Using one command, display the messages "Hello!" and "Goodbye!" separated by a new line.
   Click here for Hint
   Click here for Solution

### ASSISTANT

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

You're doing great! These exercises help build your confidence in navigating and managing a Linux system from the terminal.

Would you like more practice with file operations, permissions, or scripting? Let me know — I can provide custom labs tailored to your goals! 🐧💻✨

### USER

Exercise 1 - Navigating Files and Directories
In these exercises, you will practice using commands for navigating and managing files and directories.

1.1. Get the location of the present working directory
pwd

When working in a Linux terminal, you will always be working from a directory. By default, you will start in your home directory. To get the absolute path of your present working directory, enter the following:

1
pwd

Copied!
This will print the name of the directory you are currently working in.

1.2. List the files and directories in a directory
ls

To list the files and directories in the current directory, enter the following:

1
ls

Copied!
If your directory happens to be empty, ls will not return anything.

The following command will list the many binary and executable files which are present in your /bin (binaries) directory.

1
ls /bin

Copied!
The /bin directory happens to be where Linux commmands such as ls and pwd are stored. For example, you can see that ls is present by entering the following:

1
ls /bin/ls

Copied!
To list all files starting with b in the /bin directory, try entering the following:

1
ls /bin/b\*

Copied!
Tip: The asterisk \* is a special character called a wildcard. It is used to represent any string of characters.

To list all files ending in r in the /bin directory, enter the following:

1
ls /bin/\*r

Copied!
To print a longer list of files with additional information, such as the last-modified date, enter the following:

1
ls -l

Copied!
Here are some common options that you can try with the ls command:

Option Description
-a list all files, including hidden files
-d list directories only, do not include files
-h with -l and -s, print sizes like 1K, 234M, 2G
-l include attributes like permissions, owner, size, and last-modified date
-S sort by file size, largest first
-t sort by last-modified date, newest first
-r reverse the sort order
To get a long list of all files in /etc, including any hidden files, enter the following:

1
ls -la /etc

Copied!
Here we combined the options -l and -a by using the shorter notation, -la.

### ASSISTANT

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

You're building strong foundational skills in navigating and managing files from the command line! Ready for **Exercise 2 – Creating, Moving, and Deleting Files**? Let me know and I’ll guide you through it step-by-step. 🐧🚀

### USER

Exercise 2 - Creating Files and Directories
2.1. Create a directory
mkdir

The mkdir command is used to create a new directory.

To create a directory named scripts in your current directory, run the following command:

1
mkdir scripts

Copied!
Use the ls command to verify whether the scripts directory was created:

1
ls

Copied!
You should see a directory named scripts listed.

2.2. Change your current working directory
cd

To change your present working directory to the scripts directory, run the following command:

1
cd scripts

Copied!
Now use the pwd command to verify whether your current working directory has changed as expected:

1
pwd

Copied!
You can enter cd without any directory name to move back to your home directory:

1
cd

Copied!
Then, enter the pwd command to verify whether your current working directory has changed:

1
pwd

Copied!
The syntax .. is a shortcut that refers to the parent directory of your current directory. Run the following command to move the directories up one level:

1
cd ..

Copied!
2.3. Create an empty file
touch

First, return to your home directory by entering:

1
cd

Copied!
Next, use the touch command to create an empty file named myfile.txt:

1
touch myfile.txt

Copied!
Now use the ls command to verify the creation of myfile.txt:

1
ls

Copied!
If the file already exists, the touch command updates the access timestamp, or last-modified date of the file. To see this, enter:

1
touch myfile.txt

Copied!
And use the date command to verify the date change:

1
date -r myfile.txt

### ASSISTANT

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

Ready for **Exercise 3 – Copying, Moving, and Deleting Files**?  
Let me know and I’ll walk you through how to manage files like a pro! 🐧📁✨

### USER

Exercise 3 - Managing Files and Directories
3.1. Search for and locate files
find

The find command is used to search for files in a directory. You can search for files based on different attributes, such as the file's name, type, owner, size, or timestamp.

The find command conducts a search of the entire directory tree starting from the given directory name.

For example, the following command finds all .txt files in the /etc directory and all of its subdirectories:

1
find /etc -name \'\*.txt\'

Copied!
Note: Along with listing all the .txt files, the terminal may return "Permission denied" errors.
These errors are normal, as you have limited access permissions on the lab machine.

3.2. Remove files
rm

The rm command is used to delete files, ideally with the -i option, which creates a prompt to ask for confirmation before every deletion.

To remove the file myfile.txt, enter the following command and press y to confirm deletion, or n to deny deletion:

1
rm -i myfile.txt

Copied!
Use the ls command to verify removal:

1
ls

Copied!
Tip: When you are only removing one file with the rm command, the -i option is redundant. But if you want to remove multiple files, for example by using a wildcard to find all filenames matching a pattern, it's best practice to confirm or deny each deletion by including the -i option.

Be careful when deleting files or directories! There is normally no way to restore a deleted file once it is deleted, as there is no trash folder. This is why you should always back up, or archive, your important files. You will learn more about archiving files soon.

3.3. Move and rename a file
mv

You can use the mv command to move files from one directory to another and/or rename them.

Before doing so, let's first create a new file called users.txt:

1
touch users.txt

Copied!
You should always use caution when moving a file. If the target file already exists, it will be overwritten, or replaced, by the source file.

Conveniently, however, when the source and target directories are the same, you can use mv to rename a file.

To illustrate this, use mv to rename users.txt to user-info.txt by entering the following command:

1
mv users.txt user-info.txt

Copied!
Because the source and target directories are the same (your present working directory), the mv command will rename the file.

Now use the ls command to verify the name change:

1
ls

Copied!
Now, you can move user-info.txt to the /tmp directory as follows:

1
mv user-info.txt /tmp

Copied!
Use the ls command twice to verify the move:

1
ls

Copied!
1
ls -l /tmp

Copied!
3.4. Copy files
cp

You can use the cp command to copy user-info.txt, which is now in your /tmp directory, to your current working directory:

1
cp /tmp/user-info.txt user-info.txt

Copied!
Use the ls command to verify that the copy was successful:

1
ls

Copied!
At times, you may want to copy the contents of an existing file into a new one.

The following command copies the content of /etc/passwd to a file named users.txt within the current directory:

1
cp /etc/passwd users.txt

Copied!
Again, use the ls command to verify if the copy was successful:

1
ls

### ASSISTANT

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

Ready for **Exercise 4 – Working with Archives and Compression**?  
Let me know and I’ll show you how to compress and extract files like a pro! 🐧📦✨

### USER

Practice exercises

1. Display the contents of the /home directory.
   Click here for Hint
   Click here for Solution
2. Ensure that you are in your home directory.
   Click here for Hint
   Click here for Solution
3. Create a new directory called tmp and verify its creation.
   Click here for Hint
   Click here for Solution
4. Create a new, empty file named display.sh in the tmp directory, and verify its creation.
   Click here for Hint
   Click here for Solution
5. Create a copy of display.sh, called report.sh, within the same directory.
   Click here for Hint
   Click here for Solution
6. Move your copied file, report.sh, up one level in the directory tree to the parent directory. Verify your changes.
   Click here for Hint
   Click here for Solution
7. Delete the file display.sh.
   Click here for Hint
   Click here for Solution
8. List the files in /etc directory in the ascending order of their access time.
   Click here for Hint
   Click here for Solution
9. Copy the file /var/log/bootstrap.log to your current directory.
   Click here for Hint
   Click here for Solution

### ASSISTANT

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

Would you like to continue with **Exercise 4 – Working with Archives and Compression**, or dive into **permissions and ownership**? Just say the word — I'm here to guide you further! 🐧📦🔒✨

### USER

Security: Managing File Permissions and Ownership
Learning objectives
After completing this reading, you will be able to:

Explain file ownership and permissions
View file and directory permissions
Make a file private
Why do we need file permissions and ownership?
Linux is a multi-user operating system. This means that by default, other users will be able to view any files you store on the system. However, you may have some files, such as your personal tax documents or your employer's intellectual property documents, that are private or confidential. How can you protect these sensitive documents from being viewed or modified by others?

File ownership and permissions
There are three possible levels of file ownership in Linux: user, group, and other.
Whoever creates a file, namely the user at the time of creation, becomes the owner of that file by default. A group of users can also share ownership of a file. The other category essentially refers to anyone in the universe with access to your Linux machine – Exercise caution when assigning ownership permission to this level!

Only an official owner of a file is allowed to change its permissions. This means that only owners can decide who can read the file, write to it, or execute it.

Viewing file permissions
Let's say you've entered the following lines of code:

1
2
3
4
5
$ echo "Who can read this file?" > my_new_file
$ more my_new_file
Who can read this file?
$ ls -l my_new_file
-rw-r--r-- 1 theia users 25 Dec 22 17:47 x

Copied!
Here we've echoed the string "Who can read this file?" into a new file called my_new_file. The next line uses the more command to print the contents of the new file. Finally, the ls command with the -l option displays the file's (default) permissions: rw-r--r--

The first three characters (rw-) define the user permissions, the next three (r--) the group permissions, and the final three (r--) the other permissions.

So you, being the user, have the permission rw-, which means you have read and write permissions by default, but do not have execution permissions. Otherwise, there would be an x in place of the last -.

Thus by looking at the entire line, rw-r--r--, you can see that anyone can read the file, nobody can execute it, and you are the only user that can write to it.

Note: The - at the very beginning of the line in the terminal means that the permissions are referring to a file. If you were getting the permissions to a directory, you would see a d in the front for "directory".

Directory permissions
The permissions for directories are similar but distinct for files. Though directories use the same rwx format, the symbols have slightly different meanings.

The following table illustrates the meanings of each permission for directories:

Directory Permission Permissible action(s)
r List directory contents using ls command
w Add or remove files or directories
x Enter directory using cd command
Setting appropriate permissions on directories is a best practice for both security and stability reasons. Though this reading focuses on security, you will learn more about other reasons for setting file permissions and ownership later in this course.

Making a file private
You can revoke read permissions from your group and all other users by using the chmod command. Ensure successful modification by using the ls -l command again:

1
2
3
chmod go-r my_new_file
ls -l my_new_file
-rw------- 1 theia users 24 Dec 22 18:49 my_new_file

Copied!
In the chmod command, go-r is the permission change to be applied, which in this case means removing for the group (g) and others (o) the read (r) permission. The chmod command can be used with both files and directories.

Executable files - looking ahead
You've learned what it means to read or write to a file, but what does it mean to have permissions to execute a file in Linux?

A Linux file is executable if it contains instructions that can be directly interpreted by the operating system. Basically, an executable file is a ready-to-run program. They're also referred to as binaries or executables.

In this course, you will become very familiar with a particular kind of executable called a script, which is a program written in a scripting language. You'll learn all about shell scripting, or more specifically Bash scripting, which is writing scripts in Bash (Bourne Again Shell), a very popular shell scripting language. A shell script is a plain text file that can be interpreted by a shell.

Formally speaking, for a text file to be considered an executable shell script for a given user, it needs to have two things:

Execute permissions set for that user
A directive, called a "shebang", in its first line to declare itself to the operating system as a binary
All of this will become more clear to you soon when we get to the topic of shell scripting.

Summary
In this reading, you learned that:

There are three possible levels of file ownership in Linux - user, group, and other - which determine who can read, write to, and execute a file.
You can use the ls -l command to view file and directory permissions.
You can change permissions on a file by using the chmod command.

### ASSISTANT

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

Would you like to practice managing file permissions with hands-on exercises? Let me know — I can walk you through real-world scenarios! 🔒🐧✨

### USER

Exercise 1 - Viewing and modifying file access permissions
1.1 View file access permissions
Required files:
Run the following code to download the required files for this exercise:

1
2
cd /home/project
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/usdoi.txt

Copied!
Each file and each directory in your Linux system has permissions set for three permission categories: the 'user', the 'group', and 'all users' (or 'other').

The following permissions are set for each file and directory:

Permission Symbol
read r
write w
execute x
To see the permissions currently set for a file, run the ls command with the -l option.

For example, to see the permissions for the file named usdoi.txt in your current directory, enter the following:

1
ls -l usdoi.txt

Copied!
A sample output looks like the following:

-rw-r--r-- 1 theia theia 8121 May 31 16:45 usdoi.txt

The permissions set here are rw-r--r--. The - preceeding these permissions indicates that usdoi.txt is a file. If it were a directory, you would see a d instead of the -.

The first three entries correspond to the current user, the next three correspond to the group, and the last three are for all others. You can see the user has read and write permissions, while the user group only has read permission, and all other users have only read permission. No users have execute permission, as indicated by the - instead of an x in the third position for each user category.

1.2 Change file access permissions
chmod

The chmod or change mode command lets you change the permissions set for a file.

Specify which permissions to change with a combination of the following characters:

Option Description
r, w, x Permissions: read, write, and execute
u,g, o User categories: user, group, and all others
+, - Operations: grant and revoke
The following command revokes read permissions for all users (user, group, and other) on the file usdoi.txt:

1
chmod -r usdoi.txt

Copied!
You can verify the changed permissions by entering:

1
ls -l usdoi.txt

Copied!
To grant read access to all users on usdoi.txt, enter:

1
chmod +r usdoi.txt

Copied!
Verify the changed permissions again with the following:

1
ls -l usdoi.txt

Copied!
Now to remove the read permission only for 'other' category, enter the following:

1
chmod o-r usdoi.txt

Copied!
Verify the changed permissions as follows:

1
ls -l usdoi.txt

### ASSISTANT

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

Would you like to try **changing file ownership with `chown`** or practice with **directory permissions** next? Let me know — I'm here to help! 🔒🐧✨

### USER

Exercise 2 - Understanding directory access permissions
2.1 View default directory access permissions
Recall the following table, which illustrates the meanings of each permission for directories with examples of allowable operations for a given directory.

Directory Permission Permissible action(s)
r list directory contents using ls command
w add/remove files or directories from directory
x enter directory using cd command
For this exercise, first move to your project directory and create a new directory called test:

1
2
cd /home/project
mkdir test

Copied!
Check the default permissions that the system sets for your new test directory:

1
ls -l

Copied!
As you can see from the resulting output:

1
2
3
total 12
drwxr-sr-x 2 theia users 4096 May 15 14:06 test
-rw-r----- 1 theia users 8121 Sep 28 2022 usdoi.txt

Copied!
You, "theia", as the owner of test, have read, write, and execute permissions set by default. But all others only have read and execute permissions set and cannot write to your test directory. This means users outside your group can't add or remove files from test. They can, however, explore your directory to see what files and directories exist there.

Note: You might be wondering what that s permission is in the execute slot for your group. The s stands for "special permission". It means that any new files created within the directory will have their group ownership set to be the same as the directory owner. We won't go into this level of detail in this course, but you can learn more about advanced Linux permissions here: Linux permissions: SUID, SGID, and sticky bit.

Go ahead and verify for yourself that you have permission to run the following commands. Change the directory to your test directory, create a new directory within it, then return to your parent directory:

1
2
3
cd test
mkdir test2
cd ../

Copied!
2.2 Remove user execute permissions on your test directory
Remove your user execute permissions on test using the following command:

1
chmod u-x test

Copied!
Now, what happens when you try to change directories to test?

1
cd test

Copied!
You get an error message!

bash: cd: test: Permission denied

As you just removed execute permissions for yourself on your test directory, you can no longer make it your present working directory. However, you can still "read" it with the ls command:

1
ls -l

Copied!
Even though you have "write" permissions set, you can't actually create a new directory within test, because removing execute permissions overrides write permissions. For example, entering,

1
mkdir test/test3

Copied!
throws an error:

mkdir: cannot create directory ‘test/test’: Permission denied

This time, try restoring execute permissions on test and denying write permissions. Then verify your changes:

1
2
3
chmod u+x test
chmod u-w test
ls -l

Copied!
Now you can go into test, but you still can't write to it! Entering

1
2
cd test
mkdir test_again

Copied!
throws the error:

mkdir: cannot create directory ‘test_again’: Permission denied

### ASSISTANT

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

Would you like to continue with **Exercise 3 – Changing File Ownership with `chown`**, or dive into **symbolic links and advanced navigation**? Just let me know — I’m here to guide you! 🔒📁🐧✨

### USER

Practice exercises

1. List the permissions set for the file usdoi.txt that you downloaded to your project directory at the beginning of the lab.
   Click here for Hint
   Click here for Solution
2. Revoke the write permission on usdoi.txt for the user, and verify your result.
   Click here for Hint
   Click here for Solution
3. What happens if you try to delete usdoi.txt after revoking write permissions for the user?
   Click here for Hint
   Click here for Solution
4. Create a new directory called tmp_dir in your home directory.
   Click here for Hint
   Click here for Solution
5. View the permissions of the newly created directory, tmp_dir.
   Click here for Hint
   Click here for Solution
6. Revoke the user write permission for tmp_dir.
   Click here for Hint
   Click here for Solution
7. Check whether you can create a subdirectory of tmp_dir called sub_dir.
   Click here for Hint
   Click here for Solution 1
   Click here for Solution 2
   1
   mkdir tmp_dir/sub_dir

Copied!
Again, you should see a "permission denied" error for the mkdir command.

### ASSISTANT

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

Would you like to continue with **Exercise 3 – Changing File Ownership with `chown`**? Let me know — I’ll walk you through it step by step! 🔒📁🐧✨

### USER

Exercise 1 - Viewing file contents
cat
more
less

In this exercise, you will learn how to explore file contents using the cat, more, and less commands to display the file contents in your terminal window.

Begin by changing directories to your default home directory, ~, or \home\theia:

1
cd ~

Copied!
Using the ls command, you should see a file called entrypoint.sh. The .sh is a convention used to identify a text file as being a shell script.

Next, let's take a look inside this file.

1.1. Viewing file content with the cat command
The cat command displays the contents of the file and exits back to the command prompt as follows:

1
cat entrypoint.sh

Copied!
It only displays the tail end of the file, so if the file is too long to fit on the terminal, you won't be able to see some of its contents.

Although the cat command may not be the best way to view the contents of a file, especially larger files, it is quite useful for shell scripting applications. For example, it is often used to concatenate, or append one file onto another.

1.2. Viewing file content with the more command
A better alternative to the cat command for viewing file contents is the more command. By entering the following command:

1
more entrypoint.sh

Copied!
you will see the top portion of the file first.

Tip: The first line of this particular file, #!/bin/bash, is called a shebang. Basically, this shebang line makes the file a bash script by invoking the bash shell. You will learn more about shebang lines later in this course.

When using the more command, you can see only as many lines as will fit on your terminal window at once.

To see the next portion of the file, just press your spacebar. You can keep paging this way, tapping the spacebar until you reach the end of the file. Once you reach the last page, you will exit back to the command prompt.

Another way to exit is simply to type q, which quits and returns to the command prompt.

1.3. Scrolling through file content with the less command
What if you want to move up and down through the file, not just downward? In this case, you can use the less command:

1
less entrypoint.sh

Copied!
Just like more, the less command displays the first page of the file. What's useful about less is that you can use it to move around the file, page by page, using the Page Up and Page Down keys.

You can also scroll up and down through the file line-by-line, using the Up Arrow and Down Arrow keys, ↑ and ↓.

Unlike more, less does not automatically exit when you reach the end of a file, allowing you the option to continue scrolling around. You can quit at any time by typing q.

### ASSISTANT

# 📄 Exercise 1 - Viewing File Contents with `cat`, `more`, and `less`

In this exercise, you learned how to **view and navigate file contents** in the terminal using three essential Linux commands:

- `cat` – for quick viewing and concatenation
- `more` – for basic scrolling through a file
- `less` – for advanced navigation (forward and backward)

These tools are especially useful when working with shell scripts, logs, configuration files, and other text-based data.

---

## 🔧 Step-by-Step Breakdown

### 🏁 Start by navigating to your home directory:

```bash
cd ~
```

### 🔍 Check what files exist:

```bash
ls
```

You should see a file named `entrypoint.sh`. `.sh` is the extension used for **shell scripts**, which are executable text files that contain Bash commands.

---

## ✅ 1.1 View File Content with `cat`

### Command:

```bash
cat entrypoint.sh
```

### What It Does:

- Displays the **entire contents** of the file at once
- Stops at the end and returns to the command prompt

> ⚠️ If the file is longer than your terminal window, you’ll only see the last part — it scrolls past too quickly to read everything.

### 💡 Use Cases:

- Quick inspection of small files
- Concatenating multiple files:
  ```bash
  cat file1.txt file2.txt > combined.txt
  ```

---

## ✅ 1.2 View File Content with `more`

### Command:

```bash
more entrypoint.sh
```

### What It Does:

- Shows one screen of text at a time
- Press **Spacebar** to go to the next page
- Type **q** to quit

### 🔍 Useful Info:

The first line:

```bash
#!/bin/bash
```

is called a **shebang** — it tells the system to use `/bin/bash` to interpret the script.

> 📌 You’ll learn more about writing shell scripts later in the course.

### 💡 Use Cases:

- Reading medium-sized files
- Viewing logs or configuration files from the command line

---

## ✅ 1.3 Scroll Through File Content with `less`

### Command:

```bash
less entrypoint.sh
```

### What It Does:

- Displays one screen of content
- Allows **scrolling forward and backward**
  - **↑ / ↓** keys: scroll line by line
  - **Page Up / Page Down**: scroll page by page
- Press **q** to exit

### 🆕 Why `less` Is Better Than `more`:

- You can move **up and down**, not just down
- You can search inside the file with `/search_term`
- It doesn’t automatically quit at the end

---

## 📋 Summary Table

| Command | Scrolling Direction   | Interactive | Exits Automatically | Best For                  |
| ------- | --------------------- | ----------- | ------------------- | ------------------------- |
| `cat`   | All at once           | No          | Yes                 | Small files, scripting    |
| `more`  | Forward only          | Limited     | Yes                 | Paging through files      |
| `less`  | Both forward/backward | Full        | No                  | Detailed inspection, logs |

---

## 🧠 Tips & Tricks

- Combine with pipes to view output:
  ```bash
  ls -l /etc | less
  ```
- Search inside `less`:
  - Type `/pattern` then press Enter
  - Press `n` to find next match
- Exit early: always press `q` to quit

---

Great job completing this exercise! You now know how to choose the best tool depending on the size and complexity of the file you're viewing.

Would you like to continue with **Exercise 2 – Searching Inside Files with `grep`**, or explore **file redirection and piping**? Let me know — I'm ready to guide you further! 🐧📄🔍✨

### USER

Exercise 2 - Viewing text file contents
In this exercise, you will work with a few more commands for viewing the content of text files.

To begin, run the following commands:

1
2
cd /home/project
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt

Copied!
The wget command downloads a text file called usdoi.txt from the provided URL. You'll see this command again later in the context of networking commands. You can check to see if you successfully downloaded the usdoi.txt by using the ls command.

2.1. Display the first N lines of a file
head

By default, head will print the first 10 lines of a file. To use it with usdoi.txt, enter the following:

1
head usdoi.txt

Copied!
You can also specify the number of lines to be printed. Print only the first 3 lines of text from the file usdoi.txt by entering:

1
head -3 usdoi.txt

Copied!
2.2. Display the last N lines of a file
tail

By default, tail will print the last 10 lines of the file usdoi.txt:

1
tail usdoi.txt

Copied!
Just like with head, you can specify the number of lines to be printed. Print the last 2 lines of the file usdoi.txt by entering the following:

1
tail -2 usdoi.txt

### ASSISTANT

# 📄 Exercise 2 - Viewing Text File Contents

## Using `head` and `tail` to View File Content

In this exercise, you learned how to **inspect specific parts of a text file** using two powerful Linux commands:

- `head` – to view the **beginning** of a file
- `tail` – to view the **end** of a file

These tools are especially useful for:

- Reading large log files
- Monitoring real-time updates (with `tail -f`)
- Extracting headers or footers from data files

---

## 🧾 Step-by-Step Instructions

### 🔧 Download and Navigate to Your Project Directory:

```bash
cd /home/project
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
```

Verify the file was downloaded:

```bash
ls
```

You should see `usdoi.txt` listed.

---

## ✅ 2.1 Display the First N Lines with `head`

### Show the first 10 lines (default):

```bash
head usdoi.txt
```

This is helpful when viewing large documents like logs or configuration files where the most important info may be at the top.

### Show only the first 3 lines:

```bash
head -3 usdoi.txt
```

Example output:

```
When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another...
```

> 💡 Use `head` to quickly preview files without opening the entire contents.

---

## ✅ 2.2 Display the Last N Lines with `tail`

### Show the last 10 lines (default):

```bash
tail usdoi.txt
```

Useful for checking the end of logs or files where recent changes are appended.

### Show only the last 2 lines:

```bash
tail -2 usdoi.txt
```

Example output:

```
...and that government of the people, by the people, for the people shall not perish from the earth.
```

> 🚀 Pro Tip: Use `tail -f` to follow a log file in real time:

```bash
tail -f /var/log/syslog
```

---

## 📋 Summary Table

| Command   | Description                            | Example                   |
| --------- | -------------------------------------- | ------------------------- |
| `head`    | Displays the first 10 lines of a file  | `head filename`           |
| `head -N` | Displays the first N lines             | `head -3 filename`        |
| `tail`    | Displays the last 10 lines of a file   | `tail filename`           |
| `tail -N` | Displays the last N lines              | `tail -2 filename`        |
| `tail -f` | Follows the end of a file in real time | `tail -f /var/log/syslog` |

---

## 🧠 Why These Commands Matter

- **Efficiency**: Avoid opening huge files just to check the start or end.
- **Monitoring**: Track live updates in log files using `tail -f`.
- **Automation**: Use in scripts to extract key information from files.

---

Great work! You now know how to **quickly inspect large text files**, which is essential for system administration, scripting, and data analysis.

Would you like to continue with **Exercise 3 – Searching Inside Files with `grep`**, or dive into **file redirection and piping**? Just say the word — I'm here to help! 🐧📄🔍✨

### USER

Exercise 3 - Getting basic text file stats
3.1. Count lines, words, or characters from a text file
wc

If you want to find the number of lines, words, and characters in a file like usdoi.txt, enter the following command:

1
wc usdoi.txt

Copied!
The output contains the number of lines, followed by the number of words, followed by the number of characters in the file.

To get just the count of lines in usdoi.txt, use the -l option:

1
wc -l usdoi.txt

Copied!
Similarly, for the count of words in usdoi.txt, use the -w option:

1
wc -w usdoi.txt

Copied!
To print the number of characters in usdoi.txt, use the -c option:

1
wc -c usdoi.txt

### ASSISTANT

# 📊 Exercise 3 - Getting Basic Text File Stats with `wc`

In this exercise, you learned how to use the **`wc`** (word count) command to get basic statistics about a text file — including the number of **lines**, **words**, and **characters**.

This is especially useful when:

- You're analyzing large text files
- You need to verify file contents before processing
- You're writing scripts that depend on file size or structure

---

## 🔧 Step-by-Step Breakdown

### Start by navigating to your project directory and using `wc`:

```bash
cd /home/project
wc usdoi.txt
```

### Example Output:

```
     21     268    1654 usdoi.txt
```

The output shows:

1. Number of **lines**
2. Number of **words**
3. Number of **characters**
4. File name

---

## ✅ View Specific Stats

### 🔢 Count Lines Only:

```bash
wc -l usdoi.txt
```

Useful for checking how many entries are in a list or log file.

---

### 📝 Count Words Only:

```bash
wc -w usdoi.txt
```

Great for content analysis or verifying document length.

---

### 🔤 Count Characters Only:

```bash
wc -c usdoi.txt
```

Tells you the total byte size of the file — useful for storage and transmission planning.

> 💡 Note: `wc -c` counts bytes, not just visible characters — so whitespace and punctuation are included.

---

## 📋 Summary Table

| Command          | Output                       |
| ---------------- | ---------------------------- |
| `wc filename`    | Lines, words, characters     |
| `wc -l filename` | Number of lines              |
| `wc -w filename` | Number of words              |
| `wc -c filename` | Number of bytes (characters) |

---

## 🧠 Why `wc` Is Useful

- **Automation**: Use in scripts to validate input data size
- **Analysis**: Get quick stats without opening the file
- **Debugging**: Check if a file has expected content structure

---

You're doing great! With these tools, you can now **analyze text files efficiently** and extract meaningful insights from their content.

Ready for **Exercise 4 – Searching Inside Files with `grep`**?  
Let me know and I’ll walk you through how to find specific text patterns in files like a pro! 🐧📄🔍📊✨

### USER

Exercise 4 - Basic text wrangling: sorting lines and dropping duplicates
4.1. Sort and display lines of file alphanumerically
sort

You can use the sort command to display the lines of a file sorted alphanumerically.

To view the lines of usdoi.txt sorted alphanumerically, enter:

1
sort usdoi.txt

Copied!
To view those lines sorted in reverse order, enter:

1
sort -r usdoi.txt

Copied!
4.2. Drop consecutive duplicated lines and display result
uniq

First download the following file:

1
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/zoo.txt

Copied!
View the raw contents of zoo.txt with the cat command:

1
cat zoo.txt

Copied!
View the contents of zoo.txt with identical, consecutive lines dropped using the uniq command:

1
uniq zoo.txt

Copied!
The uniq line will drop any lines in the file that are identical and consecutive. This is similar to what is known as "dropping duplicates". As you can see from this example, however, there can still be duplicated lines left over if these lines are not repeated right after the other.

### ASSISTANT

# 🧹 Exercise 4 - Basic Text Wrangling: Sorting Lines and Dropping Duplicates

In this exercise, you learned how to **clean up and organize text data** using two powerful Linux utilities:

- `sort` – to **alphabetically or numerically sort lines**
- `uniq` – to **remove consecutive duplicate lines**

These tools are essential for:

- Data cleaning
- Log file analysis
- Preparing input for scripts
- Removing redundant output

---

## 🔧 Step-by-Step Breakdown

### ✅ 4.1 Sort Lines Alphanumerically with `sort`

#### Display the lines of `usdoi.txt` sorted alphanumerically:

```bash
sort usdoi.txt
```

This command rearranges all the lines in alphabetical order (A–Z), making it easier to scan or analyze content.

#### Sort in reverse order (Z–A):

```bash
sort -r usdoi.txt
```

> 💡 This is useful when you want to see the "end" of an alphabetized list first — like viewing the latest entries in a log.

---

### ✅ 4.2 Remove Consecutive Duplicate Lines with `uniq`

#### First, download a new file:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/zoo.txt
```

#### View the contents:

```bash
cat zoo.txt
```

You’ll notice some repeated animal names, especially `zebra`.

#### Remove **consecutive duplicates**:

```bash
uniq zoo.txt
```

This removes only lines that appear **one after another**, so:

```
zebra
zebra
lion
tiger
zebra
```

Becomes:

```
zebra
lion
tiger
zebra
```

Only the **first two zebras** are removed as duplicates — the last one stays because it's not directly after another zebra.

---

## 📋 Summary Table

| Command            | Description                            |
| ------------------ | -------------------------------------- | -------------------------------------------- |
| `sort filename`    | Sort lines alphabetically              |
| `sort -r filename` | Sort lines in reverse order            |
| `uniq filename`    | Remove **consecutive** duplicate lines |
| `sort file         | uniq`                                  | Sort then remove all duplicates (if grouped) |

---

## 🧠 Pro Tips

- To remove **all duplicate lines** regardless of order:

  ```bash
  sort zoo.txt | uniq
  ```

- Count how many times each line appears:

  ```bash
  sort zoo.txt | uniq -c
  ```

- Show only lines that appear **more than once**:

  ```bash
  sort zoo.txt | uniq -d
  ```

- Show only lines that appear **exactly once**:
  ```bash
  sort zoo.txt | uniq -u
  ```

---

## 🛠️ Real-World Use Cases

| Task                              | Command                      |
| --------------------------------- | ---------------------------- | ------------------------ | -------- | -------- | ----------- |
| Clean up a messy list of emails   | `sort emails.txt             | uniq > clean_emails.txt` |
| Count unique IP addresses in logs | `cut -d' ' -f1 access.log    | sort                     | uniq -c` |
| Find most frequently visited URLs | `awk '{print $7}' access.log | sort                     | uniq -c  | sort -nr | head -n 10` |

---

Great job mastering these basic but powerful text processing tools! You're now equipped to **organize**, **clean**, and **analyze** textual data efficiently in Linux.

Ready to move on to **Exercise 5 – Searching Inside Files with `grep`**?  
Just let me know and I’ll guide you through searching for specific patterns and words inside files! 🐧📄🔍🧹✨

### USER

Exercise 5 - Basic text wrangling: extracting lines and fields
5.1. Extract lines matching a specified criterion
grep

The grep command allows you to specify a pattern and search for lines within a file that match that pattern.

For example, the following command prints all lines in the file usdoi.txt which contain the word people:

1
grep people usdoi.txt

Copied!
Some frequently used options for grep include:

Option Description
-n Along with the matching lines, also print the line numbers
-c Get the count of matching lines
-i Ignore the case of the text while matching
-v Print all lines which do not contain the pattern
-w Match only if the pattern matches whole words
You can use these options to print all the lines from the /etc/passwd file which do not contain the pattern login:

1
grep -v login /etc/passwd

Copied!
5.2. Extract fields from lines of text
cut

The cut command allows you to view only specific fields from each line of text in a file.

For example, you can use cut with the -c option to view only the first two characters of each line:

1
cut -c -2 zoo.txt

Copied!
Or to view each line starting from the second character:

1
cut -c 2- zoo.txt

Copied!
The cut command can also be used to extract a field from a delimited file.
To demonstrate this, start by downloading and taking a look at the following comma-separated file:

1
2
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/v4_new_content/labs/names_and_numbers.csv  
cat names_and_numbers.csv

Copied!
Now you can extract just the phone numbers for each person listed in the file using the -d (delimiter) and f (field) options as follows:

1
cut -d "," -f2 names_and_numbers.csv

Copied!
-d "," tells the command that the delimiter is a comma, and -f2 tells it to extract the second field.

### ASSISTANT

# 🧩 Exercise 5 - Basic Text Wrangling: Extracting Lines and Fields

In this exercise, you learned how to **filter lines** using patterns with `grep` and **extract specific parts of text** using the `cut` command.

These tools are essential for:

- Searching through logs
- Filtering data
- Processing structured files like CSVs
- Automating repetitive tasks in scripts

---

## 🔍 Step-by-Step Breakdown

### ✅ 5.1 Extract Lines Matching a Pattern with `grep`

#### Print all lines containing the word "people":

```bash
grep people usdoi.txt
```

This shows only the lines where the word `people` appears.

#### Print matching lines along with line numbers:

```bash
grep -n people usdoi.txt
```

#### Count how many lines contain the pattern:

```bash
grep -c people usdoi.txt
```

#### Ignore case (match both "People" and "people"):

```bash
grep -i people usdoi.txt
```

#### Show lines that **do not** contain the pattern:

```bash
grep -v login /etc/passwd
```

Useful for filtering out system-generated accounts from `/etc/passwd`.

#### Match only whole words:

```bash
grep -w people usdoi.txt
```

Prevents partial matches like `peoples` or `unpeople`.

---

### ✅ 5.2 Extract Fields from Lines Using `cut`

#### View first two characters of each line in `zoo.txt`:

```bash
cut -c -2 zoo.txt
```

#### View text starting from the second character:

```bash
cut -c 2- zoo.txt
```

> These options extract by **character position**, useful for fixed-width formats.

---

### 📥 Work with Delimited Files (e.g., CSV)

#### Download and view the file:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/v4_new_content/labs/names_and_numbers.csv
cat names_and_numbers.csv
```

Sample content:

```
Name,Phone
Alice,555-1234
Bob,555-5678
Charlie,555-9012
```

#### Extract just the phone numbers (second field):

```bash
cut -d "," -f2 names_and_numbers.csv
```

- `-d ","` tells `cut` to split on commas
- `-f2` tells it to return the second field

Output:

```
Phone
555-1234
555-5678
555-9012
```

You can also extract multiple fields:

```bash
cut -d "," -f1,3 names_and_numbers.csv
```

Returns fields 1 and 3 — useful when skipping unnecessary columns.

---

## 📋 Summary Table

| Task                           | Command                                |
| ------------------------------ | -------------------------------------- |
| Find lines containing a word   | `grep pattern file`                    |
| Show line numbers              | `grep -n pattern file`                 |
| Count matches                  | `grep -c pattern file`                 |
| Case-insensitive search        | `grep -i pattern file`                 |
| Invert match (not containing)  | `grep -v pattern file`                 |
| Match whole word only          | `grep -w pattern file`                 |
| Extract characters by position | `cut -c START-END file`                |
| Extract fields by delimiter    | `cut -d "DELIM" -f FIELD_NUMBERS file` |

---

## 🧠 Why These Tools Matter

| Tool   | Use Case                                                       |
| ------ | -------------------------------------------------------------- |
| `grep` | Search, filter, and count patterns in text                     |
| `cut`  | Extract specific parts of text based on position or delimiters |

They're often used together in pipelines:

```bash
grep "New York" contacts.csv | cut -d "," -f2
```

This finds all entries for New York and extracts their phone numbers.

---

Great job mastering **text filtering** and **field extraction**! You now have the skills to process and analyze text-based data efficiently.

Would you like to continue with **Exercise 6 – Combining Commands with Pipes and Redirection**, or dive into **regular expressions with grep**? Just let me know — I'm ready to guide you further! 🐧📄🔍🧩✨

### USER

Exercise 6 - Basic text wrangling: merging lines as fields
6.1. Merge text files line-by-line, aligned as columns
paste

Use the paste command to merge lines of multiple files together.

Download the following file:

1
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/zoo_ages.txt

Copied!
Then use the paste command to view the two files merged together, line-by-line, as columns delimited by a Tab character:

1
paste zoo.txt zoo_ages.txt

Copied!
Try changing the delimiter. Instead of the default Tab delimiter, you can specify a comma , as follows:

1
paste -d "," zoo.txt zoo_ages.txt

### ASSISTANT

# 🧩 Exercise 6 - Basic Text Wrangling: Merging Lines as Fields

In this exercise, you learned how to use the **`paste`** command to **merge lines from multiple files side-by-side**, like combining columns in a spreadsheet.

This is especially useful when:

- You're working with related data stored in separate files
- You want to align rows for analysis or reporting
- You need to build structured output from flat files

---

## 🔧 Step-by-Step Breakdown

### ✅ Download an additional file:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/zoo_ages.txt
```

You already have `zoo.txt`, which contains animal names. Now `zoo_ages.txt` has corresponding age data.

### ✅ Merge both files line-by-line using `paste`:

```bash
paste zoo.txt zoo_ages.txt
```

By default, `paste` uses a **Tab (`\t`)** character to separate merged fields.

Example Output:

```
lion	5
tiger	4
zebra	6
elephant	10
```

This makes it easy to combine related data into a single view.

---

### ✅ Change the Delimiter to Comma (`,`) for CSV-like Output:

```bash
paste -d "," zoo.txt zoo_ages.txt
```

Now the output looks like:

```
lion,5
tiger,4
zebra,6
elephant,10
```

> 💡 This is useful for creating CSV files or preparing data for scripts and databases.

You can also use other delimiters like space, colon, or semicolon:

```bash
paste -d " " zoo.txt zoo_ages.txt   # Space
paste -d ":" zoo.txt zoo_ages.txt  # Colon
```

---

## 📋 Summary Table

| Command                                 | Description                                      |
| --------------------------------------- | ------------------------------------------------ |
| `paste file1 file2`                     | Merge two files line-by-line using Tab delimiter |
| `paste -d "," file1 file2`              | Merge using comma as delimiter                   |
| `paste -s file.txt`                     | Paste all lines of a file into one line          |
| `paste -d ":" file1 file2 > merged.csv` | Save merged output to a new file                 |

---

## 🧠 Why `paste` Is Useful

| Use Case                            | Example                                        |
| ----------------------------------- | ---------------------------------------------- |
| Combine logs from different sources | `paste access.log user_agents.log`             |
| Build CSV files from parallel data  | `paste -d "," names.csv ages.csv > people.csv` |
| Align configuration values          | Match hostnames with IPs                       |
| Create input for scripts            | Generate formatted input for another tool      |

---

## 🛠️ Try It Out – Real-World Examples

#### Combine Names and Ages into One File:

```bash
paste -d "," zoo.txt zoo_ages.txt > animals.csv
```

Creates a new file `animals.csv` that's ready for import into Excel or a database.

#### Merge Multiple Files:

```bash
paste names.txt emails.txt phones.txt
```

Merges three files — one per column — ideal for building contact lists.

---

Great job mastering the `paste` command! You now know how to **combine and structure text data** efficiently in Linux.

Would you like to continue with **Exercise 7 – Combining Commands with Pipes and Redirection**, or explore more advanced text processing? Just say the word — I'm here to help! 🐧📄🧩📎✨

### USER

Practice Exercises
Before you begin, ensure you're working in your home directory by entering:

1
2
cd ~
pwd

Copied!

1. Display the number of lines in the /etc/passwd file.
   Click here for Hint
   Click here for Solution
2. Display the lines that contain the string "not installed" in /var/log/bootstrap.log.
   Click here for Hint
   Click here for Solution
3. The text file at https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/top-sites.txt contains a list of popular websites. Find all the websites on the list that have the word "org" in them.
   Click here for Hint
   Click here for Solution
   Alternative Solution
4. Print the first seven lines of top-sites.txt.
   Click here for Hint
   Click here for Solution
5. Print the last seven lines of top-sites.txt.
   Click here for Hint
   Click here for Solution
6. Print the first three characters of each line from top-sites.txt.
   Click here for Hint
   Click here for Solution
7. Extract and view only the names, without their phone numbers, from the file names_and_numbers.csv.
   Click here for Hint
   Click here for Solution

### ASSISTANT

# 🛠️ **Practice Exercises – Text Processing in Linux**

These hands-on exercises help reinforce your knowledge of **file inspection**, **searching**, and **text manipulation** using essential Linux commands like `wc`, `grep`, `head`, `tail`, `cut`, and more.

---

## 🔧 Before You Begin

Make sure you're in your home directory:

```bash
cd ~
pwd
```

---

## 📝 Practice Exercise Solutions

### 1. **Display the number of lines in `/etc/passwd`**

#### ✅ Solution:

```bash
wc -l /etc/passwd
```

This shows how many user accounts exist on the system (each line in `/etc/passwd` represents a user).

---

### 2. **Display lines containing "not installed" in `/var/log/bootstrap.log`**

#### ✅ Solution:

```bash
grep "not installed" /var/log/bootstrap.log
```

This helps identify packages or services that failed to install during system boot.

---

### 3. **Find websites with "org" in them from `top-sites.txt`**

#### First, download the file:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/top-sites.txt
```

#### ✅ Use `grep` to search for "org":

```bash
grep "org" top-sites.txt
```

This lists all URLs or domains that include "org".

#### 🔄 Alternative solution using case-insensitive match:

```bash
grep -i "org" top-sites.txt
```

Useful if you want to catch both "org" and "ORG", etc.

---

### 4. **Print the first 7 lines of `top-sites.txt`**

#### ✅ Solution:

```bash
head -7 top-sites.txt
```

This gives a quick preview of the top sites list.

---

### 5. **Print the last 7 lines of `top-sites.txt`**

#### ✅ Solution:

```bash
tail -7 top-sites.txt
```

Handy when you're interested in newer entries at the end of a list or log file.

---

### 6. **Print the first three characters of each line from `top-sites.txt`**

#### ✅ Solution:

```bash
cut -c -3 top-sites.txt
```

This extracts only the first 3 characters from every line — useful for fixed-width data or codes.

---

### 7. **Extract and view only the names from `names_and_numbers.csv`**

Assuming the file already exists:

```bash
cat names_and_numbers.csv
```

#### ✅ Solution:

```bash
cut -d "," -f1 names_and_numbers.csv
```

- `-d ","` tells `cut` to use comma as the delimiter
- `-f1` selects the **first field** — which is the name column

You can also skip the header if needed:

```bash
tail -n +2 names_and_numbers.csv | cut -d "," -f1
```

---

## 📋 Summary Table: Commands Used

| Task                      | Command                                    |
| ------------------------- | ------------------------------------------ |
| Count lines in a file     | `wc -l filename`                           |
| Search for text in a file | `grep "pattern" filename`                  |
| Print first N lines       | `head -N filename`                         |
| Print last N lines        | `tail -N filename`                         |
| Extract character range   | `cut -c START-END filename`                |
| Extract by delimiter      | `cut -d "DELIM" -f FIELD_NUMBERS filename` |

---

## 🧠 Why These Skills Matter

You now have the tools to:

- **Analyze logs**
- **Filter and extract data**
- **Process CSVs and structured files**
- **Build automation pipelines** using command-line tools

These are foundational skills for scripting, system administration, and data analysis in Linux.

---

Would you like to continue with **Exercise 7 – Combining Commands with Pipes and Redirection**, or dive into **writing your first shell script**? Just let me know — I'm ready to guide you further! 🐧📄🧩✨

### USER

Summary
In this lab, you learned how to:

View file contents with cat, more, and less
See the first and last N lines of a file using head and tail
Find the number of lines, words, and characters in a file with wc
Sort lines and drop duplicates using sort and uniq
Extract lines and fields from a file with grep and cut
Merge text files using paste

### ASSISTANT

### 🎉 **Summary – Great Job Completing the Lab!**

You've just gained hands-on experience with some of the most essential **Linux text processing and file inspection tools**. These skills are fundamental for working efficiently in a Linux environment — whether you're managing logs, analyzing data, or writing shell scripts.

---

## 🔍 What You Learned

Here's a quick recap of the core commands and skills you practiced:

| Skill                                     | Command(s) Used       |
| ----------------------------------------- | --------------------- |
| **Viewing file contents**                 | `cat`, `more`, `less` |
| **Inspecting start/end of files**         | `head`, `tail`        |
| **Count lines, words, characters**        | `wc`                  |
| **Sort and deduplicate lines**            | `sort`, `uniq`        |
| **Search for patterns in files**          | `grep`                |
| **Extract specific fields or characters** | `cut`                 |
| **Merge files line-by-line**              | `paste`               |

---

## 💡 Why This Matters

These tools form the foundation of **text-based data manipulation** in Linux:

- They allow you to **quickly inspect and analyze** large files
- You can **filter**, **format**, and **combine** data using simple yet powerful utilities
- Together, they enable **pipeline-style scripting** (e.g., `grep | sort | uniq`) — a key part of Linux automation

---

## 🧠 Pro Tip: Combine Commands with Pipes!

Now that you know these individual tools, try combining them using the **pipe (`|`)** operator:

```bash
grep "error" /var/log/syslog | wc -l
```

> Counts how many error messages are in the system log.

Or:

```bash
cat top-sites.txt | tail -10 | grep "org" | sort
```

> Gets the last 10 sites, filters for "org", and sorts alphabetically.

---

## 🚀 Next Steps

Would you like to continue with:

- **Exercise 7 – Combining Commands with Pipes and Redirection**
- **Introduction to Shell Scripting**
- **Automating Tasks with Bash Scripts**

Let me know where you'd like to go next — I'm here to help you keep building your Linux mastery! 🐧💻📘✨

### USER

yes continue

### ASSISTANT

### 🚀 Great! Let's Continue with:

## **Exercise 7 – Combining Commands with Pipes and Redirection**

In this exercise, you’ll learn how to:

- Combine multiple Linux commands using **pipes (`|`)**
- Redirect command output to files using `>` and `>>`
- Use input redirection with `<`
- Build powerful **command pipelines** that process data step-by-step

These skills are essential for:

- Automating repetitive tasks
- Processing logs or large datasets
- Writing shell scripts
- Becoming a more efficient Linux user

---

## 🔧 What is Piping?

The **pipe operator (`|`)** takes the **output of one command** and feeds it as **input to another**.

This lets you chain together small tools to build complex operations.

### Example:

```bash
ls -l | grep "Jan" | wc -l
```

This pipeline:

1. Lists all files (`ls -l`)
2. Filters only those modified in January (`grep "Jan"`)
3. Counts them (`wc -l`)

---

## 📥 Input and Output Redirection

You can also control where input comes from and where output goes using:

| Operator | Purpose                                | Example                        |
| -------- | -------------------------------------- | ------------------------------ |
| `>`      | Redirect output to a file (overwrites) | `ls > files.txt`               |
| `>>`     | Append output to a file                | `echo "New line" >> files.txt` |
| `<`      | Redirect input from a file             | `sort < names.txt`             |

### Example:

```bash
grep "error" /var/log/syslog > errors.txt
```

Saves all lines containing "error" from the system log into a new file.

---

## 💡 Hands-On Practice

Let’s go through some guided examples.

### ✅ 1. Chain `grep`, `sort`, and `uniq` to Analyze Log Data

#### Find unique IP addresses in an access log:

```bash
grep "Failed password" /var/log/auth.log | awk '{print $9}' | sort | uniq
```

- `grep`: filters for failed login attempts
- `awk`: extracts the IP address field
- `sort`: prepares for deduplication
- `uniq`: removes duplicates

> You'll learn about `awk` soon — it's a powerful text processing tool.

---

### ✅ 2. Save Command Output to a File

#### Save your list of running processes to a file:

```bash
ps -e > process_list.txt
```

Now view it:

```bash
cat process_list.txt
```

---

### ✅ 3. Count Words in a File Using a Pipeline

#### Count how many times each word appears in `usdoi.txt`:

```bash
tr ' ' '\n' < usdoi.txt | sort | uniq -c | sort -nr
```

What this does:

- `tr ' ' '\n'`: replaces spaces with newlines (puts each word on its own line)
- `sort`: sorts words alphabetically
- `uniq -c`: counts occurrences
- `sort -nr`: sorts numerically in reverse order

---

### ✅ 4. View Command Output One Page at a Time

Sometimes output fills your screen. Use `less` to page through it:

```bash
history | less
```

Use ↑ ↓ keys to scroll, and press `q` to quit.

---

## 📋 Summary Table: Pipes & Redirection

| Task                           | Command               |
| ------------------------------ | --------------------- | --------- |
| Pipe output to another command | `command1             | command2` |
| Redirect output to a file      | `command > file.txt`  |
| Append output to a file        | `command >> file.txt` |
| Read input from a file         | `command < file.txt`  |

---

## 🧠 Why This Matters

With pipes and redirection, you can:

- **Automate workflows** with simple, reusable components
- **Process large amounts of data** efficiently
- **Build custom scripts** that do exactly what you need

---

Would you like to dive deeper into:

- **Shell scripting basics**
- **Using `awk` and `sed` for advanced text processing**
- **Creating reusable command-line pipelines**

Just say the word — I’ll guide you through the next steps in your Linux journey! 🐧📘🧩✨

### USER

A Brief Introduction to Networking
Here we introduce some key concepts related to computer networking. This is an optional but recommended reading which is designed to help you build context for what you will be learning later about networking and informational commands.

Learning Objectives
After completing this reading, you will be able to:

Describe computer networks, network resources, and network nodes
Explain hosts, clients, and servers
Describe packets and pings
Explain URLs and IP addresses
Computer Networks
A computer network is a set of computers that are able to communicate with each other and share resources provided by network nodes.

Examples of computer networks include Local Area Networks (LANs), Wide Area Networks (WANs), and the entire Internet. The Internet, or World Wide Web, is essentially a giant network of computer networks.

A network resource is any object, such as a file or document, which can be identified by the network.

An object is identifiable if it can be assigned a unique name and address that the network can use to identify and access it.

A network node is any device that participates in a network.

A network can include any device which is not necessarily a computer but is part of the network’s infrastructure. Examples of network nodes include modems, network switches, hubs, and wifi hotspots.

Hosts, Clients, and Servers
A host is a special type of node in a computer network - it is a computer that can function as a server or a client on a network.

A server is a host computer that is able to accept a connection from a client host and fulfill certain resource requests made by the client.

Many hosts can perform either role, acting as both client and server.

Packets and Pings
A network packet is a formatted chunk of data that can be transmitted over a network.

Today's computer networks typically use communication protocols that are based on such packets of information. Every packet consists of two types of data: 1. the control information, and 2. the payload. The control information is data about how and where to deliver the payload, such as the source and destination network addresses, while the payload is the message being sent.

The ping command works by sending special 'echo request' packets to a host and waiting for a response from the host.

ping is a utility available on most operating systems that have networking capability. Linux has its own implementation of the ping command that's used to test and troubleshoot connectivity to other network hosts.

URLs and IP Adresses
IP stands for "Internet Protocol" which defines the format of data transmitted over the internet or a local network.

An IP address is a code used to uniquely identify any host on a network.

An IP address can be used to establish a connection to a host and exchange packets with it, for example using the ping command. In addition to their payload, IP packets - a type of network packet that conforms to the Internet Protocol - contain the IP addresses of the source and destination hosts.

A URL, more commonly known as a web address, stands for Uniform Resource Locator.

A URL uniquely identifies a web resource and enables access to that resource. Typically the resource that a URL points to is a web page, but it can also be used for tasks such as transferring files, sending emails, and accessing databases.

For example, the URL to the Wikipedia page for URL is https://en.wikipedia.org/wiki/URL. Just like for a typical URL, its format indicates a protocol (https), a hostname (en.wikipedia.org), and a file name (/wiki/URL).

Summary
In this reading, you learned that:

A computer network is a set of computers that are able to communicate with each other and share resources. A network resource is any object, such as a file or document, which can be identified by the network. A network node is any device that participates in a network.
A host is a computer that can function as a server or a client on a network. A server is a host computer that is able to accept a connection from a client host and fulfill certain resource requests made by the client.
A network packet is a formatted chunk of data that can be transmitted over a network. The ping command works by sending special 'echo request' packets to a host and waiting for a response from the host.
An IP address is a code used to uniquely identify any host on a network. A URL identifies a web resource and enables access to that resource.

### ASSISTANT

# 🌐 A Brief Introduction to Networking – Summary & Highlights

Great job reading through this foundational networking guide! This optional but valuable reading introduced you to **core concepts in computer networking**, helping you understand how computers communicate, share resources, and connect across networks like the Internet.

---

## 🎯 Learning Objectives Recap

After completing this reading, you are now able to:

✅ **Describe** computer networks, network resources, and network nodes  
✅ **Explain** the roles of **hosts**, **clients**, and **servers**  
✅ **Understand** what **packets** and **pings** are  
✅ **Differentiate between URLs and IP addresses**

---

## 🧩 Key Concepts Explained

### 🔹 Computer Networks

- A **computer network** is a collection of interconnected devices that can communicate and share resources.
- Examples:
  - **LAN (Local Area Network)** – small, localized network (e.g., home or office)
  - **WAN (Wide Area Network)** – covers large geographical areas (e.g., the internet)
  - **The Internet** – a global network of networks

> 💡 The internet is essentially a **network of computer networks**.

---

### 🔁 Hosts, Clients, and Servers

| Term       | Description                                                                       |
| ---------- | --------------------------------------------------------------------------------- |
| **Host**   | Any device on a network with an IP address. Can act as a **server** or **client** |
| **Client** | Requests services or data from a server                                           |
| **Server** | Provides services or data to clients (e.g., web servers, email servers)           |

> 💡 Many devices can switch roles — acting as both client and server when needed.

---

### 📦 Packets and Pings

#### What Is a Network Packet?

- A packet is a **formatted unit of data** sent over a network.
- Contains:
  - **Control information**: source, destination, routing info
  - **Payload**: actual data being transmitted

#### What Is `ping`?

- A utility used to test connectivity between two hosts
- Works by sending an **"echo request"** packet and waiting for a response
- Helps diagnose connection issues (e.g., "Can I reach Google's servers?")

Example command:

```bash
ping google.com
```

---

### 🌍 URLs and IP Addresses

#### What Is an IP Address?

- Stands for **Internet Protocol Address**
- A unique identifier assigned to each device connected to a network
- Used to **locate and communicate** with other devices
- Example IPv4 address: `192.168.1.1`
- Example IPv6 address: `2001:0db8:85a3::8a2e:0370:7334`

> 💡 When you use `ping`, it uses **IP addresses** to send and receive packets.

---

#### What Is a URL?

- Stands for **Uniform Resource Locator**
- Also known as a **web address**
- Identifies the location of a resource on the internet and how to access it

#### URL Format:

```
protocol://hostname/path
```

Example:

```
https://en.wikipedia.org/wiki/URL
```

Breakdown:

- **Protocol**: `https` – method to retrieve the resource
- **Hostname**: `en.wikipedia.org` – server where the resource lives
- **Path**: `/wiki/URL` – specific file/resource on the server

> 📌 URLs make it easier for humans to access resources without needing to remember complex IP addresses.

---

## 🧠 Why These Concepts Matter

Understanding these basics helps you:

- Troubleshoot network issues using commands like `ping`
- Understand how computers communicate over the internet
- Work more effectively with web-based tools and services
- Prepare for deeper learning about Linux networking commands

---

## ✅ Summary Table

| Concept              | Description                                                                |
| -------------------- | -------------------------------------------------------------------------- |
| **Computer Network** | Interconnected computers sharing resources                                 |
| **Network Resource** | Anything identifiable and accessible via a network (e.g., files, printers) |
| **Network Node**     | Any device participating in the network (computers, routers, etc.)         |
| **Host**             | A device that can be a client or server                                    |
| **Client**           | Requests data or services from a server                                    |
| **Server**           | Provides data or services to clients                                       |
| **Packet**           | Unit of data containing control info + payload                             |
| **Ping**             | Tests network connectivity by sending echo requests                        |
| **IP Address**       | Unique identifier for a device on a network                                |
| **URL**              | Human-readable address pointing to a web resource                          |

---

## 🚀 Next Steps

Would you like to continue with:

- **Exercise – Using Networking Commands (`ping`, `ifconfig`, `ip`, `curl`)**
- **Introduction to Ports and Services**
- **Using `wget` and `curl` to download files from the terminal**

Let me know and I’ll walk you through the next stage of your Linux networking journey! 🐧🌐📘✨

### USER

Exercise 1 - View configuration info about your network
1.1. Display your system's hostname and IP address
hostname

A hostname is a name that is assigned to a computer or device on a network, and it is used to identify and communicate with that device.

To view the current hostname, run the command below:

1
hostname

Copied!
An IP address (Internet Protocol address) is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.

You can use the -i option to view the IP address of the host:

1
hostname -i

Copied!
1.2. Display network interface configuration
Please execute the below commands to install the iproute2 package:

1
2
sudo apt update
sudo apt install iproute2

Copied!
iproute2
The ip command is used to configure or display network interface parameters for a network.

To display the configuration of all network interfaces of your system, enter:

1
ip a

Copied!
To display the configuration of a particular device, such as the ethernet adapter eth0, enter:

1
ip addr show eth0

Copied!
eth0 is usually the primary network interface that connects your server to the network.

You can see your server's IP address in line 2 after the word inet.

### ASSISTANT

# 🧾 Exercise 1 – View Configuration Info About Your Network

In this exercise, you learned how to **view your system's network configuration**, including:

- Hostname
- IP address
- Network interface details using `hostname` and `ip`

This is essential for understanding how your machine connects to the network and communicates with other systems.

---

## 🔍 Overview of What You Learned

| Task                                              | Command             |
| ------------------------------------------------- | ------------------- |
| View system hostname                              | `hostname`          |
| View system IP address                            | `hostname -i`       |
| Show all network interfaces                       | `ip a` or `ip addr` |
| Show info about a specific interface (e.g., eth0) | `ip addr show eth0` |

---

## ✅ Step-by-Step Breakdown

### 🔹 1.1 Display Your System’s Hostname and IP Address

#### View the current **hostname**:

```bash
hostname
```

Example output:

```
theia-2c65847f
```

The **hostname** helps identify your machine on a network — especially useful in server environments.

#### View the system's **IP address**:

```bash
hostname -i
```

Example output:

```
172.17.0.2
```

> 💡 This shows the **IPv4 address** associated with your host.

---

### 🔹 1.2 Display Network Interface Configuration

Before running the `ip` command, you installed the `iproute2` package:

#### Update and install:

```bash
sudo apt update
sudo apt install iproute2
```

Now you can use the powerful `ip` command.

#### Show all network interfaces:

```bash
ip a
```

or

```bash
ip addr
```

This displays information like:

- Interface name (`lo`, `eth0`, etc.)
- IP addresses (`inet`, `inet6`)
- MAC address (`link/ether`)
- Status (`UP`, `DOWN`)

Example output line:

```
inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
```

Here, `172.17.0.2` is your **IPv4 address**.

#### Show configuration for a specific interface (like `eth0`):

```bash
ip addr show eth0
```

> 📌 `eth0` is typically the **primary Ethernet interface** used to connect to the network.

You'll see:

- The device status (`UP`)
- Its IPv4 and IPv6 addresses
- Broadcast and subnet mask info

---

## 📋 Summary Table: Useful Commands

| Purpose                              | Command             |
| ------------------------------------ | ------------------- |
| View system hostname                 | `hostname`          |
| View system IP address               | `hostname -i`       |
| List all network interfaces          | `ip a` or `ip addr` |
| View specific interface (e.g., eth0) | `ip addr show eth0` |

---

## 🧠 Why These Tools Matter

Understanding your **network configuration** helps with:

- Troubleshooting connectivity issues
- Configuring servers
- Monitoring network usage
- Writing scripts that depend on network state

The `ip` command is a modern replacement for older tools like `ifconfig`, and it offers more flexibility and control.

---

## 🛠️ Real-World Use Cases

| Task                                | Command                                                   |
| ----------------------------------- | --------------------------------------------------------- |
| Check if network is up              | `ip link show eth0`                                       |
| Find your public IP (from terminal) | `curl ifconfig.me`                                        |
| Monitor interface changes           | `ip monitor`                                              |
| Bring an interface up/down          | `sudo ip link set eth0 up` / `sudo ip link set eth0 down` |

---

Great job exploring your **Linux network configuration**! You now know how to view your **hostname**, **IP address**, and **interface settings** — key skills for working in Linux environments.

Would you like to continue with:

- **Exercise 2 – Testing Connectivity with `ping`**
- **Using `curl` and `wget` to download files over the network**
- **Exploring DNS with `nslookup` or `dig`**

Let me know and I’ll guide you through the next step! 🐧🌐📘✨

### USER

Exercise 2 - Test network connectivity
2.1. Test connectivity to a host
ping

Use the ping command to check if www.google.com is reachable. The command keeps pinging data packets to server at www.google.com and prints the response it gets back. (Press Ctrl+c to stop pinging.)

1
ping www.google.com

Copied!
If you want to ping only a limited number of times, use -c option.

1
ping -c 5 www.google.com

### ASSISTANT

# 🧪 Exercise 2 – Test Network Connectivity with `ping`

In this exercise, you learned how to use the **`ping`** command to test whether your system can successfully communicate with another device or website over the network.

This is a fundamental tool for:

- Checking internet connectivity
- Diagnosing network issues
- Testing server availability

---

## 🔍 Overview of What You Learned

| Task                                   | Command                    |
| -------------------------------------- | -------------------------- |
| Ping a host continuously               | `ping www.google.com`      |
| Ping a host a specific number of times | `ping -c 5 www.google.com` |

---

## ✅ Step-by-Step Breakdown

### 🔹 2.1 Test Connectivity to a Host Using `ping`

#### Ping Google continuously:

```bash
ping www.google.com
```

You’ll see output like:

```
64 bytes from 142.251.42.78: icmp_seq=1 ttl=115 time=15.3 ms
64 bytes from 142.251.42.78: icmp_seq=2 ttl=115 time=14.9 ms
...
```

Each line shows:

- The size of the response
- The IP address of the responding server
- Sequence number
- Time-to-live (TTL)
- Round-trip time in milliseconds

> ⚠️ To stop the ping process, press **Ctrl + C**

---

#### Ping a Host a Specific Number of Times

To limit the number of packets sent, use the `-c` option:

```bash
ping -c 5 www.google.com
```

This sends **exactly 5 packets**, then stops automatically.

Useful for:

- Scripting and automation
- Quick tests without manually stopping the command

---

## 📋 Summary Table

| Command                | Description                             |
| ---------------------- | --------------------------------------- |
| `ping hostname`        | Tests if a remote host is reachable     |
| `ping -c N hostname`   | Pings the host exactly N times          |
| `ping -c 5 google.com` | Sends 5 packets to google.com and stops |

---

## 🧠 Why This Matters

Using `ping` helps you quickly determine:

- Whether you have **internet access**
- If a **remote server is online**
- How fast your connection is (based on **response time**)
- If there’s packet loss or high latency

It's one of the most basic yet powerful tools in any Linux user's networking toolkit.

---

## 🛠️ Real-World Use Cases

| Scenario                      | Command                                    |
| ----------------------------- | ------------------------------------------ |
| Check if you're online        | `ping -c 4 google.com`                     |
| Troubleshoot slow connections | `ping google.com` (observe response times) |
| Test local network devices    | `ping 192.168.1.1`                         |
| Monitor server availability   | `ping -c 10 server.example.com`            |

---

Great job mastering the basics of **network testing** with `ping`!

Would you like to continue with:

- **Exercise 3 – Exploring DNS and Looking Up Domain Information**
- **Using `curl` and `wget` to Transfer Files Over the Network**
- **Checking Open Ports with `netstat` or `ss`**

Let me know — I'm ready to help you dive deeper into Linux networking! 🐧🌐📘✨

### USER

Exercise 3 - View or download data from a server
3.1. Transfer data from a server
curl

You can use curl to access the file at the following URL and display the file's contents on your screen:

1
curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt

Copied!
To access the file at the given URL and also save it in your current working directory, use the -O option:

1
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt

Copied!
You can also use curl to view the HTML code for any web page if you know its URL.

3.2. Download file(s) from a URL
wget

The wget command is similar to curl, however its primary use is for file downloading. One unique feature of wget is that it can recursively download files at a URL.

To see wget in action, first remove usdoi.txt from your current directory:

1
rm usdoi.txt

Copied!
then download it again using wget as follows:

1
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt

### ASSISTANT

# 📥 Exercise 3 – View or Download Data from a Server

In this exercise, you learned how to **retrieve data from remote servers** using two powerful command-line tools:

- `curl` – for transferring data and viewing content directly in the terminal
- `wget` – for downloading files (and even entire websites)

These tools are essential for:

- Fetching configuration files
- Downloading software or scripts
- Interacting with APIs
- Automating tasks that involve remote data

---

## 🔍 Overview of What You Learned

| Task                          | Command         |
| ----------------------------- | --------------- |
| View file contents from a URL | `curl [URL]`    |
| Download and save a file      | `curl -O [URL]` |
| Download a file using wget    | `wget [URL]`    |

---

## ✅ Step-by-Step Breakdown

### 🔹 3.1 Transfer Data from a Server Using `curl`

#### View file contents from a URL:

```bash
curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
```

This displays the full text of the **U.S. Declaration of Independence** directly in your terminal.

> 💡 This is useful when you want to inspect remote files without saving them.

---

#### Save the file to your current directory:

```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
```

Now you have a local copy named `usdoi.txt`.

> 📁 The `-O` option tells `curl` to save the file using its original filename.

---

### 🔹 3.2 Download Files Using `wget`

#### First, remove the file if it already exists:

```bash
rm usdoi.txt
```

#### Then download it again using `wget`:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
```

This downloads the file and saves it in your current directory.

> ⚙️ `wget` is especially useful because:
>
> - It works well in scripts
> - Supports recursive downloads (`-r`)
> - Can continue interrupted downloads (`-c`)
> - Doesn't require user interaction once started

---

## 📋 Summary Table: `curl` vs `wget`

| Feature                      | `curl`                      | `wget`                    |
| ---------------------------- | --------------------------- | ------------------------- |
| View content in terminal     | ✅ Yes                      | ❌ No                     |
| Save file with original name | ✅ With `-O`                | ✅ Yes                    |
| Recursive download           | ❌ No                       | ✅ Yes with `-r`          |
| Resume broken download       | ❌ By default               | ✅ With `-c`              |
| Works silently               | ❌ Noisy by default         | ✅ With `-q`              |
| Use case                     | API calls, quick inspection | File downloads, scripting |

---

## 🧠 Why These Tools Matter

With `curl` and `wget`, you can:

- **Automate downloads** in scripts
- **Fetch live data** from APIs or web services
- **Download large datasets** or software packages
- **Troubleshoot HTTP responses** and server connectivity

They're foundational tools for working with **networked resources** in Linux.

---

## 🛠️ Real-World Examples

### 🔽 Download a file silently with `wget`:

```bash
wget -q https://example.com/file.zip
```

### 🖥️ Download and display JSON from an API:

```bash
curl https://api.github.com/users/octocat
```

### 📂 Recursively download an entire website:

```bash
wget -r https://example.com
```

### 📥 Resume a partially downloaded file:

```bash
wget -c http://example.com/largefile.iso
```

---

Great job learning how to **fetch and download data from the internet** using the Linux terminal!

Would you like to continue with:

- **Exercise 4 – Exploring DNS with `nslookup` or `dig`**
- **Checking Open Ports with `netstat` or `ss`**
- **Analyzing Network Traffic with `tcpdump`**

Let me know — I'm ready to guide you further into the world of Linux networking! 🐧🌐📘✨

### USER

yes continue

### ASSISTANT

# 🚀 Let's Continue with:

## **Exercise 4 – Exploring DNS and Looking Up Domain Information**

In this exercise, you'll learn how to:

- Understand what **DNS** is and why it matters
- Use `nslookup` and `dig` to look up domain information
- Check **IP addresses**, **name servers**, and **mail servers** associated with a domain

These tools are essential for:

- Troubleshooting domain issues
- Checking website availability
- Understanding how domains resolve to IP addresses
- Debugging email delivery problems using MX records

---

## 🌐 What Is DNS?

**DNS (Domain Name System)** is like the phonebook of the internet.

It maps **human-readable domain names** (like `google.com`) to **machine-readable IP addresses** (like `172.217.174.78`), so your computer knows where to find a website or service.

### Key DNS Concepts:

| Term            | Meaning                                            |
| --------------- | -------------------------------------------------- |
| **A Record**    | Maps a domain name to an IPv4 address              |
| **AAAA Record** | Maps a domain to an IPv6 address                   |
| **CNAME**       | Alias record pointing one domain to another        |
| **MX Record**   | Specifies mail servers for a domain                |
| **NS Record**   | Identifies authoritative name servers for a domain |

---

## 🔍 Step-by-Step: Using `nslookup`

The `nslookup` command helps you query DNS servers to get domain-related information.

### ✅ View Basic DNS Info for a Website

```bash
nslookup google.com
```

This shows:

- The **IP address** of the domain
- The **DNS server** used to retrieve the info

---

### ✅ Look Up Mail Servers (MX Records)

```bash
nslookup -type=mx gmail.com
```

This lists the **mail exchange (MX) servers** responsible for receiving emails for `gmail.com`.

---

### ✅ Query Name Servers (NS Records)

```bash
nslookup -type=ns ibm.com
```

This shows which **name servers** are responsible for managing the domain’s DNS records.

---

## 🔎 Step-by-Step: Using `dig`

`dig` (**Domain Information Groper**) is a more detailed and powerful tool than `nslookup`. It gives you full control over DNS queries.

### ✅ View A Record for a Domain

```bash
dig google.com
```

Look for the **ANSWER SECTION**:

```
google.com.     299     IN      A       172.217.174.78
```

This shows the **IPv4 address** that `google.com` resolves to.

---

### ✅ Look Up MX Records with `dig`

```bash
dig MX gmail.com
```

Scroll down to the **ANSWER SECTION** to see which servers handle email for Gmail.

---

### ✅ Get All DNS Records for a Domain

```bash
dig ANY ibm.com
```

This fetches all available DNS records for `ibm.com`, including:

- A / AAAA
- CNAME
- MX
- NS
- TXT (used for SPF, DKIM, etc.)

> ⚠️ Some domains may restrict "ANY" queries for security reasons.

---

## 📋 Summary Table: Useful DNS Commands

| Task                           | Command                       |
| ------------------------------ | ----------------------------- |
| View basic DNS info            | `nslookup google.com`         |
| Look up MX records (for email) | `nslookup -type=mx gmail.com` |
| Look up name servers           | `nslookup -type=ns ibm.com`   |
| View A record                  | `dig google.com`              |
| View MX records                | `dig MX gmail.com`            |
| View all DNS records           | `dig ANY ibm.com`             |

---

## 🧠 Why This Matters

Understanding DNS helps you:

- Diagnose **domain resolution issues**
- Verify **email server settings**
- Configure **custom domains**
- Troubleshoot **website downtime**

Tools like `nslookup` and `dig` are invaluable for system administrators, developers, and anyone working with web services.

---

## 🛠️ Real-World Examples

| Scenario                            | Command                                                |
| ----------------------------------- | ------------------------------------------------------ |
| Check if a site resolves correctly  | `dig example.com`                                      |
| Find who handles a domain’s email   | `dig MX example.com`                                   |
| Debug DNS propagation after changes | `dig @8.8.8.8 example.com` _(use Google's public DNS)_ |
| Test local DNS cache                | `nslookup example.com` _(before and after flush)_      |

---

Would you like to continue with:

- **Exercise 5 – Checking Open Ports with `netstat` or `ss`**
- **Analyzing Network Traffic with `tcpdump`**
- **Using `traceroute` to Track Network Paths**

Let me know — I’ll guide you through the next step in your Linux networking journey! 🐧🌐📘✨

### USER

Practice exercises
Before you begin, ensure you're in your /home/project directory by entering:

1
2
cd `/home/project`
pwd

Copied!

1. Display your host's IP address.
   Click here for Hint
   Click here for Solution
2. Get connectivity stats on your connection to www.google.com.
   Click here for Hint
   Click here for Solution
3. View info about your ethernet adapter eth0.
   Click here for Hint
   Click here for Solution
4. View the HTML code for www.google.com's landing page.
   Click here for Hint
   Click here for Solution
5. Download the HTML code for www.google.com's landing page.
   Click here for Hint
   Click here for Solution
   1
   wget www.google.com

Copied!
Note: wget saves the HTML code as index.html. You can check this with:

1
ls -l

### ASSISTANT

# 🛠️ **Practice Exercises – Networking in Linux**

These exercises will help reinforce your understanding of **network-related commands** in Linux. You'll be working with tools like `hostname`, `ping`, `ip`, `curl`, and `wget` to inspect network configuration, test connectivity, and transfer data.

---

## 🔧 Before You Begin

Make sure you're in the correct directory:

```bash
cd /home/project
pwd
```

You should see:

```
/home/project
```

Now let's go through each exercise step-by-step.

---

## ✅ 1. Display Your Host’s IP Address

### 💡 Hint:

Use the `hostname` command with an option that shows the IP address.

### ✅ Solution:

```bash
hostname -i
```

This displays your system’s internal **IPv4 address**, such as:

```
172.17.0.2
```

> This is useful for checking what IP address your machine is using on the local network.

---

## ✅ 2. Get Connectivity Stats on Your Connection to www.google.com

### 💡 Hint:

Use the `ping` command with a limited number of packets.

### ✅ Solution:

```bash
ping -c 5 www.google.com
```

This sends **5 ICMP echo requests** to Google's servers and returns stats like:

- Round-trip time (latency)
- Packet loss

Example output:

```
--- www.google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4005ms
rtt min/avg/max/mdev = 10.2/11.8/13.9/1.2 ms
```

> This helps determine if your system can reach external sites and how fast it does so.

---

## ✅ 3. View Info About Your Ethernet Adapter `eth0`

### 💡 Hint:

Use the `ip` command to show details about the network interface.

### ✅ Solution:

```bash
ip addr show eth0
```

This shows:

- Interface status (`UP`)
- IPv4 and IPv6 addresses
- MAC address
- Broadcast and subnet info

Look for the line starting with `inet` — this is your **IP address**.

Example:

```
inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
```

> This is helpful when troubleshooting or configuring network interfaces.

---

## ✅ 4. View the HTML Code for www.google.com’s Landing Page

### 💡 Hint:

Use `curl` to fetch and display remote content.

### ✅ Solution:

```bash
curl www.google.com
```

This displays the raw **HTML source code** of Google's homepage directly in your terminal.

> Tip: If the output looks messy, try saving it to a file instead (next step).

---

## ✅ 5. Download the HTML Code for www.google.com’s Landing Page

### 💡 Hint:

Use `wget` to download and save the page.

### ✅ Solution:

```bash
wget www.google.com
```

This saves the downloaded HTML as:

```
index.html
```

Verify the file exists:

```bash
ls -l
```

You’ll see something like:

```
-rw-r--r-- 1 user user 12345 Apr 5 10:00 index.html
```

> You now have a local copy of Google's home page!

---

## 📋 Summary Table

| Task                        | Command                    |
| --------------------------- | -------------------------- |
| Show host IP address        | `hostname -i`              |
| Test connectivity to Google | `ping -c 5 www.google.com` |
| View eth0 interface info    | `ip addr show eth0`        |
| View HTML of Google         | `curl www.google.com`      |
| Download Google's HTML      | `wget www.google.com`      |

---

Great job completing these networking practice exercises!  
You've now learned how to:

- Check your **IP address**
- Test **connectivity**
- Inspect **network interfaces**
- Fetch and **download web content**

These are foundational skills for anyone working with Linux systems, especially in development, DevOps, or system administration roles.

Would you like to continue with:

- **Exercise 5 – Checking Open Ports with `netstat` or `ss`**
- **Using `traceroute` to Diagnose Network Paths**
- **Exploring System Logs in `/var/log`**

Let me know — I'm ready to help you keep building your Linux networking expertise! 🐧🌐📘✨

### USER

Exercise 1 - File and folder archiving and compression
1.1. Create and manage file archives
tar

The tar command allows you to pack multiple files and directories into a single archive file.

The following command creates an archive of the entire /bin directory and writes the archive to a single file named bin.tar.

The options used are as follows:

Option Description
-c Create new archive file
-v Verbosely list files processed
-f Archive file name
1
tar -cvf bin.tar /bin

Copied!
To see the list of files in the archive, use the -t option:

1
tar -tvf bin.tar

Copied!
To untar the archive or extract files from the archive, use the -x option:

1
tar -xvf bin.tar

Copied!
Use the ls command to verify that the folder bin is extracted.

1
ls -l

Copied!
1.2. Package and compress archive files
zip

The zip command allows you to compress files.

The following command creates a zip file named config.zip consisting of all the files with extension .conf in the /etc directory.

1
zip config.zip /etc/\*.conf

Copied!
The -r option can be used to zip an entire directory.
The -y flag to prevent symbolic links from being followed recursively:

The following command creates an archive of the /bin directory.

1
zip -ry bin.zip /bin

Copied!
1.3. Extract, list, or test compressed files in a ZIP archive
unzip

The unzip command allows you to extract files.

To list the files of the archive config.zip, enter the following:

1
unzip -l config.zip

Copied!
The following command extracts all the files in the archive bin.zip.

1
unzip -o bin.zip

Copied!
We added the -o option to force overwrite in case you run the command more than once.

You should see a folder named bin created in your directory.

### ASSISTANT

# 📦 Exercise 1 - File and Folder Archiving and Compression

In this exercise, you learned how to **package**, **compress**, and **extract** files using the Linux command line tools:

- `tar` – for creating `.tar` archives
- `zip` – for compressing into `.zip` format
- `unzip` – for extracting `.zip` files

These are essential skills for:

- Backing up data
- Transferring multiple files as a single package
- Saving disk space with compression
- Managing software distributions or logs

---

## 🔧 Step-by-Step Breakdown

### 🔹 1.1 Create and Manage File Archives with `tar`

#### Create a `.tar` archive of the `/bin` directory:

```bash
tar -cvf bin.tar /bin
```

- `-c` = create a new archive
- `-v` = show progress (verbose)
- `-f` = specify filename (`bin.tar`)

This creates a large file called `bin.tar`, which contains all files from the `/bin` directory.

---

#### List contents of the `.tar` archive:

```bash
tar -tvf bin.tar
```

This shows a detailed list of files inside the archive — useful for verifying contents before extraction.

---

#### Extract files from the `.tar` archive:

```bash
tar -xvf bin.tar
```

- `-x` = extract
- `-v` = show progress
- `-f` = specify filename

After extraction, you'll see a folder named `bin` in your current directory.

> Tip: Use `ls -l` to confirm it was extracted correctly.

---

### 🔹 1.2 Package and Compress Archive Files with `zip`

#### Create a `.zip` file of all `.conf` files in `/etc`:

```bash
zip config.zip /etc/*.conf
```

This bundles all configuration files ending in `.conf` into one compressed file: `config.zip`.

---

#### Create a compressed ZIP archive of an entire directory:

```bash
zip -ry bin.zip /bin
```

- `-r` = recursively include all files and subdirectories
- `-y` = store symbolic links as such (instead of following them)

This compresses the entire `/bin` directory into a portable `bin.zip` file.

---

### 🔹 1.3 Extract, List, or Test ZIP Archives with `unzip`

#### List contents of a `.zip` file:

```bash
unzip -l config.zip
```

This shows what’s inside the archive without extracting anything — helpful for previewing.

---

#### Extract all files from a `.zip` archive:

```bash
unzip -o bin.zip
```

- `-o` = overwrite existing files (useful if you run the command more than once)
- Automatically creates a `bin` directory containing the extracted files

---

## 📋 Summary Table

| Task                 | Command                           |
| -------------------- | --------------------------------- |
| Create tar archive   | `tar -cvf archive.tar directory/` |
| List tar contents    | `tar -tvf archive.tar`            |
| Extract tar archive  | `tar -xvf archive.tar`            |
| Zip specific files   | `zip archive.zip file1 file2`     |
| Zip entire directory | `zip -r archive.zip directory/`   |
| List zip contents    | `unzip -l archive.zip`            |
| Extract zip archive  | `unzip -o archive.zip`            |

---

## 🧠 Why This Matters

Understanding archiving and compression helps you:

- Bundle and share multiple files easily
- Save storage space
- Backup important directories
- Transfer data securely between systems

`tar` is commonly used in Linux environments for packaging, while `zip` offers cross-platform compatibility with Windows and macOS.

---

## 💡 Pro Tips

- Combine `tar` and `gzip` for compressed archives:
  ```bash
  tar -czvf archive.tar.gz directory/
  ```
- Use wildcards with zip:
  ```bash
  zip logfiles.zip *.log
  ```
- Exclude files when zipping:
  ```bash
  zip -r project.zip project/ -x "*.git*"
  ```

---

Great job mastering **archiving and compression** in Linux!

Would you like to continue with:

- **Exercise 2 – Using `cron` for Scheduling Tasks**
- **Managing File Permissions on Archives**
- **Compressing Log Files with `gzip` and `bzip2`**

Let me know — I'm here to guide you further! 🐧📦📘✨

### USER

Module Summary & Highlights

Congratulations! You have completed this module. At this point, you know that:

A shell is an interactive user interface. You use shell commands to navigate and work with files and directories.

The `curl` and `wget` commands display and download files from URLs, and the`cat` and `tail`commands display file contents.

You can get user information with the `whoami` and `id`commands, and get operating system information using the `uname` command. You can check system disk usage using the `df` command and monitor processes and resource usage with `ps` and `top`.Print string or variable value using `echo`,print and extract information about the date with the `date` command, and read the manual for any command using `man`.

`ls` lists all files and directories within a specified directory tree and `cd` navigates between directories. The `find` command finds files in your directories.

Relative paths are relative to your current working directory, while absolute paths stand independently

You can create files and directories with the `touch` and `mkdir` commands, delete them with `rm` and `rmdir`, and copy and move them `cp` and `mv`.

The `cat`, `more`, `head`, and `tail` commands allow you to sort and view file contents or view only a certain number of lines. Determine line, word, and character counts with `wc`.

You can use `sort` to view the lines of a file alphanumerically and `uniq` to remove repeated lines from your view. `grep` gets the lines of a file that match your desired criteria, and `cut` extracts slices and fields from lines. You can merge lines from different files using `paste`.

`hostname` and `ip` allow you to view the network configuration. You can test a network connection using `ping` and send and receive data using `curl` and `wget`.

Compression preserves storage space, speeds data transfer, and reduces system load.

`zip` compresses files and folders prior to archiving them. `tar` archives and compresses files and directories into a tarball. `unzip` unpacks and decompresses a zipped archive, and `tar` can also decompress and unpack a tar.gz archive.

### ASSISTANT

# 🎉 Module Summary & Highlights – Great Work!

You've successfully completed a comprehensive module that covers **essential Linux command-line skills**, from navigating the system and managing files to working with networks, processes, and archives.

Here's a clean, organized summary of what you’ve learned — your **Linux command cheat sheet** for future reference.

---

## 🔧 Shell & Terminal Basics

| Task                    | Command                       |
| ----------------------- | ----------------------------- |
| Start shell             | Default shell is Bash         |
| Display current user    | `whoami`                      |
| Show user ID info       | `id`                          |
| Get OS info             | `uname -a`                    |
| List directory contents | `ls`, `ls -l`                 |
| Change directories      | `cd directory_name`           |
| Show current path       | `pwd`                         |
| Find files              | `find /path -name "filename"` |

---

## 📁 File and Directory Management

| Task                     | Command                   |
| ------------------------ | ------------------------- |
| Create file              | `touch filename`          |
| Make directory           | `mkdir dirname`           |
| Copy file/dir            | `cp source destination`   |
| Move or rename           | `mv old new`              |
| Remove file              | `rm filename`             |
| Remove empty dir         | `rmdir dirname`           |
| View file content        | `cat filename`            |
| View first N lines       | `head -N filename`        |
| View last N lines        | `tail -N filename`        |
| Count lines/words/chars  | `wc`, `wc -l filename`    |
| Sort lines               | `sort filename`           |
| Remove duplicates        | `uniq filename`           |
| Search in files          | `grep "pattern" filename` |
| Extract fields           | `cut -d "," -f2 filename` |
| Merge files line-by-line | `paste file1 file2`       |

---

## 💾 Archiving and Compression

| Task                   | Command                            |
| ---------------------- | ---------------------------------- |
| Create `.tar` archive  | `tar -cvf archive.tar folder/`     |
| List `.tar` contents   | `tar -tvf archive.tar`             |
| Extract `.tar` archive | `tar -xvf archive.tar`             |
| Compress into `.zip`   | `zip -r archive.zip folder/`       |
| List `.zip` contents   | `unzip -l archive.zip`             |
| Extract `.zip` archive | `unzip archive.zip`                |
| Combine tar + gzip     | `tar -czvf archive.tar.gz folder/` |

---

## 🌐 Networking Tools

| Task                       | Command                                     |
| -------------------------- | ------------------------------------------- |
| View hostname              | `hostname`                                  |
| View IP address            | `hostname -i`                               |
| Inspect network interfaces | `ip addr` or `ip a`                         |
| Test connectivity          | `ping www.google.com`                       |
| Transfer data              | `curl https://example.com/file.txt`         |
| Download files             | `wget https://example.com/file.txt`         |
| Look up DNS records        | `nslookup example.com` or `dig example.com` |

---

## 🖥️ System Monitoring & Info

| Task              | Command          |
| ----------------- | ---------------- |
| Disk space        | `df -h`          |
| Running processes | `ps -e`, `top`   |
| Current date/time | `date`           |
| Print text/values | `echo "message"` |
| Read manual pages | `man command`    |

---

## 🔒 File Permissions and Ownership

| Task               | Command                                       |
| ------------------ | --------------------------------------------- |
| View permissions   | `ls -l`                                       |
| Change permissions | `chmod u+rwx filename`                        |
| Change ownership   | `chown user:group filename` _(requires root)_ |

---

## 🛠️ Text Processing & Data Wrangling

| Task                     | Command                   |
| ------------------------ | ------------------------- | ----- |
| Sort lines               | `sort filename`           |
| Remove duplicate lines   | `sort file                | uniq` |
| Extract patterns         | `grep "search" file`      |
| Cut out columns          | `cut -d "," -f1 file.csv` |
| Merge files side-by-side | `paste file1 file2`       |

---

## 🧠 Why This Matters

You now have a solid foundation in:

- **Navigating and managing files**
- **Searching and processing text**
- **Understanding and controlling file permissions**
- **Working with networked resources**
- **Archiving and compressing files**

These are core skills used daily by:

- **System administrators**
- **Developers**
- **Data engineers**
- **DevOps engineers**
- **Security analysts**

---

## 🚀 Next Steps

Would you like to continue with:

- **Shell Scripting Basics** – write your own automation scripts
- **Scheduling Tasks with `cron`**
- **Process Management and Signals (`kill`, `pkill`, `killall`)**
- **Advanced File Operations (`find`, `rsync`, `scp`)**
- **Using `ssh` to Access Remote Systems**

Let me know where you'd like to go next — I’m here to guide you further on your Linux journey! 🐧💻📘✨

### USER

Module 2 Cheat Sheet - Introduction to Linux Commands
Getting information
Return your user name:
1
whoami

Copied!
Return your user and group id:
1
id

Copied!
Return operating system name, username, and other info:
1
uname -a

Copied!
Display reference manual for a command:
1
man top

Copied!
List available man pages, including a brief description for each command:
1
man -k .

Copied!
Get help on any command (for eg: curl):
1
curl --help

Copied!
This provides a brief overview of the curl command's usage and options.

Return the current date and time:
1
date

Copied!
Navigating and working with directories
List files and directories by date, newest to last:
1
ls -lrt

Copied!
Find files in directory tree that end in .sh:
1
find -name "\*.sh"

Copied!
Return path to present working directory:
1
pwd

Copied!
Make a new directory:
1
mkdir new_folder

Copied!
Change the current directory:
Up one level:

1
cd ../

Copied!
To home:

1
cd ~`or`cd

Copied!
To some other directory: cd path_to_directory

Remove directory verbosely:
1
rmdir temp_directory -v

Copied!
Monitoring system performance and status
List selection of/all running processes and their PIDs:
1
ps

Copied!
1
ps -e

Copied!
Display resource usage:
1
top

Copied!
List mounted file systems and usage:
1
df

Copied!
Creating, copying, moving, and deleting files:
Create an empty file or update existing file's timestamp:
1
touch a_new_file.txt

Copied!
Copy a file:
1
cp file.txt new_path/new_name.txt

Copied!
Change file name or path:
1
mv this_file.txt that_path/that_file.txt

Copied!
Remove a file verbosely:
1
rm this_old_file.txt -v

Copied!
Working with file permissions
Change/modify file permissions to 'execute' for all users:
1
chmod +x my_script.sh

Copied!
Change/modify file permissions to 'execute' only for you, the current user:
1
chmod u+x my_file.txt

Copied!
Remove 'read' permissions from group and other users:
1
chmod go-r

Copied!
Displaying file and string contents
Display file contents:
1
cat my_shell_script.sh

Copied!
Display file contents page-by-page:
1
more ReadMe.txt

Copied!
Display first 10 lines of file:
1
head -10 data_table.csv

Copied!
Display last 10 lines of file:
1
tail -10 data_table.csv

Copied!
Display string or variable value:
1
2
echo "I am not a robot"  
echo "I am $USERNAME"

Copied!
Basic text wrangling
Sorting lines and dropping duplicates:
Sort and display lines of file alphanumerically:
1
sort text_file.txt

Copied!
In reverse order:
1
sort -r text_file.txt

Copied!
Drop consecutive duplicated lines and display result:
1
uniq list_with_duplicated_lines.txt

Copied!
Displaying basic stats:
Display the count of lines, words, or characters in a file:
Lines:

1
wc -l table_of_data.csv

Copied!
Words:

1
wc -w my_essay.txt

Copied!
Characters:

1
wc -m some_document.txt

Copied!
Extracting lines of text containing a pattern:
Some frequently used options for grep:

Option Description
-n Print line numbers along with matching lines
-c Get the count of matching lines
-i Ignore the case of the text while matching
-v Print all lines which do not contain the pattern
-w Match only if the pattern matches whole words
Extract lines containing the word "hello", case insensitive and whole words only:
1
grep -iw hello a_bunch_of_hellos.txt

Copied!
Extract lines containing the pattern "hello" from all files in the current directory ending in .txt:
1
grep -l hello \*.txt

Copied!
Merge two or more files line-by-line, aligned as columns:
Suppose you have three files containing the first and last names of your customers, plus their phone numbers.

Use paste to align file contents into a Tab-delimited table, one row for each customer:
1
paste first_name.txt last_name.txt phone_number.txt

Copied!
Use a comma as a delimiter instead of the default Tab delimiter:
1
paste -d "," first_name.txt last_name.txt phone_number.txt

Copied!
Use the cut command to extract a column from a table-like file:
Suppose you have a text file whos rows consist of first and last names of customers, delimited by a comma.

Extract first names, line-by-line:
1
cut -d "," -f 1 names.csv

Copied!
Extract the second to fifth characters (bytes) from each line of a file:
1
cut -b 2-5 my_text_file.txt

Copied!
Extract the characters (bytes) from each line of a file, starting from the 10th byte to the end of the line:
1
cut -b 10- my_text_file.txt

Copied!
Compression and archiving
Archive a set of files:
1
tar -cvf my_archive.tar.gz file1 file2 file3

Copied!
Compress a set of files:
1
2
zip my_zipped_files.zip file1 file2  
zip my_zipped_folders.zip directory1 directory2

Copied!
Extract files from a compressed zip archive:
1
2
unzip my_zipped_file.zip
unzip my_zipped_file.zip -d extract_to_this_direcory

Copied!
Working with networking commands
Print hostname:
1
hostname

Copied!
Send packets to URL and print response:
1
ping www.google.com

Copied!
Display or configure system network interfaces:
1
ip

Copied!
Display contents of file at a URL:
1
curl <url>

Copied!
Download file from a URL:
1
wget <url>

Copied!

### ASSISTANT

# 📄 Module 2 Cheat Sheet – Introduction to Linux Commands

This cheat sheet is your **go-to reference** for the most commonly used **Linux commands** in system navigation, file management, text processing, networking, and more.

---

## ❓ **Getting Information**

| Task                         | Command       |
| ---------------------------- | ------------- |
| Show current user            | `whoami`      |
| Display user/group ID info   | `id`          |
| Show OS and kernel info      | `uname -a`    |
| View command manual          | `man top`     |
| List all available man pages | `man -k .`    |
| Get help on a command        | `curl --help` |
| Show current date/time       | `date`        |

---

## 🧭 **Navigating and Working with Directories**

| Task                               | Command                   |
| ---------------------------------- | ------------------------- |
| List files by date (newest first)  | `ls -lrt`                 |
| Find `.sh` files in directory tree | `find -name "*.sh"`       |
| Show current working directory     | `pwd`                     |
| Create a new directory             | `mkdir new_folder`        |
| Move up one level                  | `cd ../`                  |
| Go to home directory               | `cd ~` or just `cd`       |
| Remove empty directory             | `rmdir temp_directory -v` |

---

## 🔍 **Monitoring System Performance**

| Task                           | Command                        |
| ------------------------------ | ------------------------------ |
| List running processes         | `ps`                           |
| List all processes             | `ps -e`                        |
| View real-time system stats    | `top`                          |
| Check disk space usage         | `df`                           |
| Show disk usage of directories | `du` _(not listed but useful)_ |

---

## 📁 **Creating, Copying, Moving, and Deleting Files**

| Task                  | Command                                    |
| --------------------- | ------------------------------------------ |
| Create an empty file  | `touch a_new_file.txt`                     |
| Copy a file           | `cp file.txt new_path/new_name.txt`        |
| Rename or move a file | `mv this_file.txt that_path/that_file.txt` |
| Delete a file         | `rm this_old_file.txt -v`                  |

---

## 🔐 **Working with File Permissions**

| Task                              | Command                             |
| --------------------------------- | ----------------------------------- |
| Make file executable for everyone | `chmod +x my_script.sh`             |
| Give owner execute permission     | `chmod u+x my_file.txt`             |
| Remove read from group & others   | `chmod go-r filename`               |
| Change file ownership             | `chown user:group file` _(as root)_ |

---

## 📖 **Displaying File and String Contents**

| Task                     | Command                   |
| ------------------------ | ------------------------- |
| View full file contents  | `cat my_shell_script.sh`  |
| View file page-by-page   | `more ReadMe.txt`         |
| View first N lines       | `head -10 data_table.csv` |
| View last N lines        | `tail -10 data_table.csv` |
| Print string or variable | `echo "I am $USERNAME"`   |

---

## 🧹 **Basic Text Wrangling**

### Sorting and Deduplication

| Task                     | Command                         |
| ------------------------ | ------------------------------- |
| Sort file alphabetically | `sort text_file.txt`            |
| Sort in reverse order    | `sort -r text_file.txt`         |
| Remove duplicate lines   | `uniq list_with_duplicates.txt` |

### Counting Lines/Words/Characters

| Task                       | Command                   |
| -------------------------- | ------------------------- |
| Count lines in a file      | `wc -l table_of_data.csv` |
| Count words in a file      | `wc -w my_essay.txt`      |
| Count characters in a file | `wc -m some_document.txt` |

### Searching with `grep`

| Task                                  | Command                                |
| ------------------------------------- | -------------------------------------- |
| Search case-insensitively for "hello" | `grep -iw hello a_bunch_of_hellos.txt` |
| List files containing "hello"         | `grep -l hello *.txt`                  |

### Merging Files with `paste`

| Task                     | Command                                                      |
| ------------------------ | ------------------------------------------------------------ |
| Merge files side-by-side | `paste first_name.txt last_name.txt phone_number.txt`        |
| Use comma as delimiter   | `paste -d "," first_name.txt last_name.txt phone_number.txt` |

### Extracting Data with `cut`

| Task                             | Command                       |
| -------------------------------- | ----------------------------- |
| Extract first field (CSV)        | `cut -d "," -f 1 names.csv`   |
| Extract bytes 2–5 from each line | `cut -b 2-5 my_text_file.txt` |
| Extract from byte 10 onward      | `cut -b 10- my_text_file.txt` |

---

## 📦 **Compression and Archiving**

| Task                           | Command                                                 |
| ------------------------------ | ------------------------------------------------------- |
| Create tar archive             | `tar -cvf my_archive.tar file1 file2`                   |
| Compress with zip              | `zip my_zipped_files.zip file1 file2`                   |
| Compress directory with zip    | `zip -r my_zipped_folders.zip dir1 dir2`                |
| Extract zip file               | `unzip my_zipped_file.zip`                              |
| Extract zip to specific folder | `unzip my_zipped_file.zip -d extract_to_this_directory` |

---

## 🌐 **Networking Commands**

| Task                              | Command               |
| --------------------------------- | --------------------- |
| Show hostname                     | `hostname`            |
| Test network connectivity         | `ping www.google.com` |
| Configure/view network interfaces | `ip`                  |
| Download content from URL         | `curl <url>`          |
| Download and save file            | `wget <url>`          |

---

## 🧠 Pro Tips

- Combine commands using pipes:
  ```bash
  grep "error" /var/log/syslog | wc -l
  ```
- Use wildcards to match patterns:
  ```bash
  ls *.txt
  ```
- Always double-check what you're about to delete:
  ```bash
  rm -i *.tmp
  ```

---

You're now equipped with a powerful set of tools to work confidently in the Linux environment. Whether you're managing servers, writing scripts, or analyzing logs — this cheat sheet will be your best companion.

Would you like to continue with:

- **Shell Scripting Basics**
- **Automating Tasks with `cron`**
- **Using `ssh` and `scp` for Remote Access**
- **Advanced Text Processing with `awk` and `sed`**

Let me know — I'm here to help you keep leveling up! 🐧💻📘✨

### USER

Reading: A Brief Introduction to Shell Variables
Learning Objectives
After completing this reading, you will be able to:

Describe shell variables
Create shell variables
What is a shell variable?
Shell variables offer a powerful way to store and later access or modify information such as numbers, character strings, and other data structures by name. Let's look at some basic examples to get the idea.

Consider the following example.

1
2
3
$ firstname=Jeff
$ echo $firstname
Jeff

Copied!
The first line assigns the value Jeff to a new variable called firstname. The next line accesses and displays the value of the variable, using the echo command along with the special character $ in front of the variable name to extract its value, which is the string Jeff.

Thus, we have created a new shell variable called firstname for which the value is Jeff.

This is the most basic way to create a shell variable and assign it to a value all in one step.

Reading user input into a shell variable at the command line
Here's another way to create a shell variable, using the read command.
After entering

1
$ read lastname

Copied!
on the command line, the shell waits for you to enter some text:

1
2
3
$ read lastname  
Grossman  
$

Copied!
Now we can see that the value Grossman has just been stored in the variable lastname by the read command:

1
2
3
4
$ read lastname  
Grossman  
$ echo $lastname  
Grossman

Copied!
By the way, notice that you can echo the values of multiple variables at once.

1
2
$ echo $firstname $lastname  
Jeff Grossman

Copied!
As you will soon see, the read command is particularly useful in shell scripting. You can use it within a shell script to prompt users to input information, which is then stored in a shell variable and available for use by the shell script while it is running. You will also learn about command line arguments, which are values that can be passed to a script and automatically assigned to shell variables.

Summary
In this reading, you learned that:

Shell variables store values and allow users to later access them by name
You can create shell variables by declaring a shell variable and value or by using the read command

### ASSISTANT

# 🧾 **Reading: A Brief Introduction to Shell Variables**

In this reading, you were introduced to one of the most powerful and essential features in shell scripting — **shell variables**. These allow you to store and manipulate data directly in the terminal or within scripts.

---

## 🎯 Learning Objectives Recap

After completing this reading, you can now:

✅ **Describe what shell variables are**  
✅ **Create and use your own shell variables**  
✅ **Read user input into a variable using `read`**

---

## 💡 What Is a Shell Variable?

A **shell variable** is a named storage location that holds a value — such as a string, number, or command output — for use in the shell environment.

### 🔹 Example:

```bash
firstname=Jeff
echo $firstname
```

Output:

```
Jeff
```

- `firstname=Jeff` → Assigns the value `Jeff` to the variable `firstname`
- `$firstname` → Retrieves (expands) the value stored in the variable

> ⚠️ No spaces around the `=` when assigning values:
>
> ```bash
> # Correct
> name=Linux
>
> # Incorrect
> name = Linux  ❌
> ```

---

## 🧩 Creating Shell Variables

### 🔹 Direct Assignment

You can create a variable by simply giving it a name and assigning a value:

```bash
greeting="Hello World"
echo $greeting
```

Output:

```
Hello World
```

Quotes help preserve whitespace and special characters.

---

### 🔹 Reading User Input with `read`

The `read` command lets you capture input from the user and store it in a variable.

#### Example:

```bash
read lastname
Grossman
echo $lastname
```

Output:

```
Grossman
```

This is especially useful in **scripts**, where you want to interactively gather information from users.

---

## 🧑‍💻 Combining Variables

You can combine multiple variables in one command:

```bash
echo $firstname $lastname
```

Output:

```
Jeff Grossman
```

This makes it easy to build dynamic messages or paths based on user input or system state.

---

## 📝 Summary Table

| Task                            | Command          |
| ------------------------------- | ---------------- |
| Create a variable               | `var_name=value` |
| Access variable value           | `$var_name`      |
| Read user input into a variable | `read var_name`  |
| Print variable content          | `echo $var_name` |

---

## 🧠 Why Shell Variables Matter

Shell variables are essential because they allow you to:

- **Store temporary data** during a session
- **Make scripts interactive** with user input
- **Customize behavior** of shell scripts
- **Reuse values** without hardcoding them

They're the foundation of automation in Bash scripting!

---

## 🛠️ Real-World Use Cases

| Scenario             | Example                          |
| -------------------- | -------------------------------- |
| Store a username     | `user=$(whoami)`                 |
| Prompt for file name | `read filename`                  |
| Build dynamic paths  | `path=/home/$USER/logs`          |
| Set custom message   | `message="Welcome back, $USER!"` |

---

Great job learning how to work with **shell variables**! You’re well on your way to writing powerful, flexible shell scripts.

Would you like to continue with:

- **Exercise – Writing Your First Bash Script Using Variables**
- **Understanding Environment Variables (`$HOME`, `$PATH`, etc.)**
- **Using Variables in Conditional Statements and Loops**

Let me know — I'm here to help you take your next step into **Bash scripting mastery**! 🐧💻📘✨

### USER

Exercise 1 - Create and execute a basic shell script
In this exercise, you will create a simple script which will do the following:

Accept a user name
Print a welcome message to the user
You will also add comments to the script, which are lines starting with #. Comments are not executed by the shell.

When used appropriately, comments can make a shell script more readable and help in debugging the script.

1.1. Create a new script file
Step 1: On the menu on the lab screen, use File->New File to create a new file.

File menu highlights New File!

Step 2: Name it as greet.sh and click OK

New file name entered and OK button is highlighted

Step 3: Copy and paste the following lines into the newly created file.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

# This script accepts the user\'s name and prints

# a message greeting the user

# Print the prompt message on screen

echo -n "Enter your name :"

# Wait for user to enter a name, and save the entered name into the variable \'name\'

read name

# Print the welcome message followed by the name

echo "Welcome $name"

# The following message should print on a single line. Hence the usage of \'-n\'

echo -n "Congratulations! You just created and ran your first shell script "
echo "using Bash on IBM Skills Network"

Copied!
Step 4: Save the file using the File->Save menu option.

1.2. Execute the script
Open a new terminal by clicking on the menu bar and selecting Terminal->New Terminal, as in the image below.

Terminal menu points to New Terminal

This will open a new terminal at the bottom of the screen.

Terminal screen points to New terminal at lower portion of screen

Run the commands below in the newly opened terminal.

Let's check the permissions for this new file by entering the following:

1
ls -l greet.sh

Copied!
If the file exists and has read permissions, run the following command to execute it:

1
bash greet.sh

Copied!
The message Enter your name : appears on screen.

Type your name and press the Enter key.

You should now see the welcome messages displayed on screen with your entered name.

Welcome message with your name and congratulations message

Congratulations! You have succesfully executed your first Bash shell script.

### ASSISTANT

# 📜 Exercise 1 – Create and Execute a Basic Shell Script

In this hands-on exercise, you created your **first Bash shell script** called `greet.sh`. You used:

- **Shell variables** to store user input
- The `echo` command to print messages
- **Comments** (`#`) to document the script
- The `read` command to accept input from the user

You then executed it using `bash greet.sh`.

---

## ✅ Step-by-Step Breakdown

### 🔹 1.1 Create a New Script File

#### Steps:

1. Opened a new file in the editor (via `File > New File`)
2. Saved it as: `greet.sh`
3. Pasted the following Bash script:

```bash
# This script accepts the user's name and prints
# a message greeting the user

# Print the prompt message on screen
echo -n "Enter your name :"

# Wait for user to enter a name, and save the entered name into the variable 'name'
read name

# Print the welcome message followed by the name
echo "Welcome $name"

# The following message should print on a single line. Hence the usage of '-n'
echo -n "Congratulations! You just created and ran your first shell script "
echo "using Bash on IBM Skills Network"
```

> 💡 Tip: The `-n` option in `echo` prevents the automatic newline — useful when printing across multiple lines.

4. Saved the file using `File > Save`

---

### 🔹 1.2 Execute the Script

#### Step 1: Open a Terminal

- Clicked `Terminal > New Terminal` to open a terminal window

#### Step 2: Check File Permissions

```bash
ls -l greet.sh
```

Make sure it exists and is readable.

#### Step 3: Run the script

```bash
bash greet.sh
```

#### What Happens:

- It prompts:
  ```
  Enter your name :
  ```
- You type your name and press **Enter**
- It responds with:
  ```
  Welcome [YourName]
  Congratulations! You just created and ran your first shell script using Bash on IBM Skills Network
  ```

✅ Success! You've run your **first Bash script**.

---

## 🧠 Why This Matters

This simple script introduces several key scripting concepts:

| Feature                | Purpose                                         |
| ---------------------- | ----------------------------------------------- |
| `#`                    | Adds comments to explain what the script does   |
| `echo`                 | Prints text or variables to the terminal        |
| `read`                 | Captures user input and stores it in a variable |
| Variables like `$name` | Store dynamic values for later use              |
| Multiple `echo` lines  | Control how output appears on screen            |

These are the building blocks of **Bash scripting**, which powers automation in Linux environments.

---

## 🛠️ Real-World Scripting Tips

- Make scripts executable:
  ```bash
  chmod +x greet.sh
  ./greet.sh
  ```
- Always test your scripts before sharing them
- Use comments to help others understand your code
- Use descriptive variable names like `username`, not `x`

---

Great job completing your **first shell script**! You’ve taken a big step toward automating tasks in Linux.

Would you like to continue with:

- **Exercise 2 – Making Your Script Executable and Passing Arguments**
- **Using Conditionals (`if`, `else`) in Bash**
- **Working with Loops (`for`, `while`) in Scripts**

Let me know — I'm ready to help you write even more powerful scripts! 🐧💻📘✨

### USER

Exercise 2 - Using a shebang line
In this exercise, you will edit the greet.sh script you created in the previous exercise by adding a 'shebang' and making it an executable file.

This is done to ensure that the name of the script can be used like a command. Adding this special shebang line lets you specify the path to the interpreter of the script - in this case, the Bash shell.

Follow the steps below to learn how to add a shebang to your script.

2.1. Find the path to the interpreter
The which command helps you find out the path of the command bash.

1
which bash

Copied!
In this case, it returns the path /bin/bash.

2.2. Edit the script greet.sh and add the shebang line to the script
Open the file and add the following line at the beginning of the script:

1
#! /bin/bash

Copied!
The script should now look like the following:

Script with the shebang line that you added

2.3. Check the permissions of the script
One more step needs to be completed to make greet.sh completely executable by name.

To add the execute permission for the user on greet.sh, enter the following:

1
chmod +x greet.sh

Copied!
Verify whether the execute permission is granted.

Tip: Generally it's not a good idea to grant permissions to a script for all users, groups, and others. It's more appropriate to limit the execute permission to only the owner, or the user who created the file (you).

To change permissions for greet.sh to make the file executable for the user, run the command below:

1
chmod u+x greet.sh

Copied!
Verify the permissions using the command below:

1
ls -l greet.sh

Copied!
If you wish to grant execute permission to everyone, you need to run the command chmod +x greet.sh.

2.4. Execute the script.
Enter the command given below to run the shell script.

1
./greet.sh

Copied!
The . here refers to the current directory. You are telling Linux to execute the script greet.sh and that it can be found in the current directory.

### ASSISTANT

# 🔧 Exercise 2 – Using a Shebang Line

In this exercise, you took your **first Bash script (`greet.sh`)** to the next level by:

- Adding a **shebang line** (`#!`) to specify the interpreter
- Making it **executable**, so you can run it like a regular command: `./greet.sh`

This is a foundational step toward writing **portable and reusable shell scripts**.

---

## 📋 Step-by-Step Breakdown

### 🔹 2.1 Find the Path to the Bash Interpreter

You used the `which` command to locate where `bash` is installed:

```bash
which bash
```

Output:

```
/bin/bash
```

This tells you that the Bash shell is located at `/bin/bash`.

---

### 🔹 2.2 Add the Shebang Line to Your Script

You opened `greet.sh` and added the shebang line at the very top:

```bash
#!/bin/bash
```

This line tells the system:

> "Use `/bin/bash` to interpret this script."

Your updated script now looks like:

```bash
#!/bin/bash

# This script accepts the user's name and prints
# a message greeting the user

echo -n "Enter your name :"
read name
echo "Welcome $name"
echo -n "Congratulations! You just created and ran your first shell script "
echo "using Bash on IBM Skills Network"
```

✅ This makes your script self-contained and portable — any system with Bash can now execute it.

---

### 🔹 2.3 Make the Script Executable

#### First, check current permissions:

```bash
ls -l greet.sh
```

It likely looked like:

```
-rw-r--r-- 1 user group 200 Apr 5 10:00 greet.sh
```

No execute permission yet!

#### Add execute permission for the owner:

```bash
chmod u+x greet.sh
```

Or make it executable for everyone:

```bash
chmod +x greet.sh
```

#### Verify the new permissions:

```bash
ls -l greet.sh
```

Now it should show:

```
-rwxr-xr-x 1 user group 200 Apr 5 10:00 greet.sh
```

The `x` means the file is now **executable**.

---

### 🔹 2.4 Run the Script Like a Command

You executed your script using:

```bash
./greet.sh
```

- `./` tells the shell to look in the **current directory**
- `greet.sh` is your **self-executable script**

You were prompted:

```
Enter your name :
```

After entering your name, you saw:

```
Welcome [YourName]
Congratulations! You just created and ran your first shell script using Bash on IBM Skills Network
```

✅ Congratulations again — you've successfully made your script **runnable as a command**!

---

## 📌 Summary Table

| Task                            | Command                          |
| ------------------------------- | -------------------------------- |
| Locate Bash interpreter         | `which bash`                     |
| Add shebang line                | `#!/bin/bash` (at top of script) |
| Make script executable for user | `chmod u+x greet.sh`             |
| Make executable for all users   | `chmod +x greet.sh`              |
| Check file permissions          | `ls -l greet.sh`                 |
| Run the script                  | `./greet.sh`                     |

---

## 🧠 Why This Matters

By adding the **shebang line** and making the script **executable**, you’ve learned how to:

- Turn a text file into a real **Linux command**
- Define which interpreter should run the script
- Improve **script portability** across systems
- Control **who can run** the script via permissions

These are essential steps in creating **custom automation tools** in Linux.

---

## 💡 Pro Tips

- Always test scripts with:
  ```bash
  bash greet.sh
  ```
  Before making them executable — helps catch syntax errors early.
- Use descriptive names for your scripts
- Keep your scripts in a dedicated folder like `~/scripts/` and add it to your `PATH` later
- Use comments liberally to explain what your script does

---

Great job mastering the **shebang line and script execution**!  
You're well on your way to writing powerful, reusable Bash scripts.

Would you like to continue with:

- **Exercise 3 – Passing Arguments to Shell Scripts**
- **Using Variables and Conditionals**
- **Creating Reusable Scripts in ~/bin**

Let me know — I'm here to help you keep building your scripting skills! 🐧💻📘✨

### USER

Examples of Pipes
Learning Objectives
After completing this reading, you will be able to:

Describe pipes
Use pipes to combine commands when working with strings and text file contents
Use pipes to extract information from URLs
What are pipes?
Put simply, pipes are commands in Linux which allow you to use the output of one command as the input of another.

Pipes | use the following format:

1
[command 1] | [command 2] | [command 3] ... | [command n]

Copied!
There is no limit to the number of times you can chain pipes in a row!

In this lab, you'll take a closer look at how you can use pipes and filters to solve basic data processing problems.

Pipe examples
Combining commands
Let's start with a commonly used example. Recall the following commands:

sort - sorts the lines of text in a file and displays the result
uniq - prints a text file with any consecutive, repeated lines collapsed to a single line
With the help of the pipe operator, you can combine these commands to print all the unique lines in a file.

Suppose you have the file pets.txt with the following contents:

1
2
3
4
5
6
7
8
$ cat pets.txt
goldfish
dog
cat
parrot
dog
goldfish
goldfish

Copied!
If you only use sort on pets.txt, you get:

1
2
3
4
5
6
7
8
$ sort pets.txt
cat
dog
dog
goldfish
goldfish
goldfish
parrot

Copied!
The file is sorted, but there are duplicated lines of "dog" and "goldfish".

On the other hand, if you only use uniq, you get:

1
2
3
4
5
6
7
$ uniq pets.txt
goldfish
dog
cat
parrot
dog
goldfish

Copied!
This time, you removed consecutive duplicates, but non-consecutive duplicates of "dog" and "goldfish" remain.

But by combining the two commands in the correct order - by first using sort then uniq - you get back:

1
2
3
4
5
$ sort pets.txt | uniq
cat
dog
goldfish
parrot

Copied!
Since sort sorts all identical items consecutively, and uniq removes all consecutive duplicates, combining the commands prints only the unique lines from pets.txt!

Applying a command to strings and files
Some commands such as tr only accept standard input - normally text entered from your keyboard - but not strings or filenames.

tr (translate) - replaces characters in input text
1
tr [OPTIONS] [target characters] [replacement characters]

Copied!
In cases like this, you can use piping to apply the command to strings and file contents.

With strings, you can use echo in combination with tr to replace all the vowels in a string with underscores \_:

1
2
$ echo "Linux and shell scripting are awesome\!" | tr "aeiou" "_"
L_n_x \_nd sh_ll scr_pt_ng \_r_ _w_s_m_!

Copied!
To perform the complement of the operation from the previous example - or to replace all the consonants (any letter that is not a vowel) with an underscore - you can use the -c option:

1
2
$ echo "Linux and shell scripting are awesome\!" | tr -c "aeiou" "\_"
\_i_u**a\_\_\_**e**\_\_**i**i\_**a*e_a_e_o_e*

Copied!
With files, you can use cat in combination with tr to change all of the text in a file to uppercase as follows:

1
2
3
4
5
6
7
8
$ cat pets.txt | tr "[a-z]" "[A-Z]"
GOLDFISH
DOG
CAT
PARROT
DOG
GOLDFISH
GOLDFISH

Copied!
The possibilities are endless! For example, you could add uniq to the above pipeline to only return unique lines in the file, like so:

1
2
3
4
5
$ sort pets.txt | uniq | tr "[a-z]" "[A-Z]"
CAT
DOG
GOLDFISH
PARROT

Copied!
Extracting information from JSON Files:
Let's see how you can use this json file to get the current price of Bitcoin (BTC) in USD, by using grep command.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
{
"coin": {
"id": "bitcoin",
"icon": "https://static.coinstats.app/coins/Bitcoin6l39t.png ",
"name": "Bitcoin",
"symbol": "BTC",
"rank": 1,
"price": 57907.78008618953,
"priceBtc": 1,
"volume": 48430621052.9856,
"marketCap": 1093175428640.1146,
"availableSupply": 18877868,
"totalSupply": 21000000,
"priceChange1h": -0.19,
"priceChange1d": -0.4,
"priceChange1w": -9.36,
"websiteUrl": "http://www.bitcoin.org",
"twitterUrl": "https://twitter.com/bitcoin ",
"exp": [
"https://blockchair.com/bitcoin/ ",
"https://btc.com/ ",
"https://btc.tokenview.com/ "
]
}
}

Copied!
Copy the above output in a file and name it as Bitcoinprice.txt.

The JSON field you want to grab here is "price": [numbers].[numbers]". To get this, you can use the following grep command to extract it from the JSON text:

1
grep -oE "\"price\"\s*:\s*[0-9]_\.?[0-9]_"

Copied!
Let's break down the details of this statement:

-o tells grep to only return the matching portion
-E tells grep to be able to use extended regex symbols such as ?
\"price\" matches the string "price"
\s* matches any number (including 0) of whitespace (\s) characters
: matches :
[0-9]* matches any number of digits (from 0 to 9)
\.? optionally matches a .
Use the cat command to get the output of the JSON file and pipe it with the grep command to get the required output.

1
cat Bitcoinprice.txt | grep -oE "\"price\"\s*:\s*[0-9]_\.?[0-9]_"

Copied!
You can also extract information directly from URLs and retreive any specific data using such grep commands.

Click here to see the process of extracting information directly from URLs and retreiving specific data:
Summary
In this reading, you learned that:

Pipes are commands in Linux which allow you to use the output of one command as the input of another
You can combine commands such as sort and uniq to organize strings and text file contents
You can pipe the output of a curl command to grep to extract components of URL data

### ASSISTANT

# 🔗 Examples of Pipes in Linux

Pipes (`|`) are one of the most powerful features in Linux and Bash scripting. They allow you to **connect commands**, using the output of one as input for the next.

---

## 🎯 Learning Objectives Recap

After this reading, you can now:

✅ Describe what **pipes** are  
✅ Use pipes to combine commands like `sort`, `uniq`, `tr`, etc.  
✅ Apply pipes to extract information from strings and files  
✅ Extract specific data (like Bitcoin price) from JSON or URLs using `grep` and pipes

---

## 🔧 What Are Pipes?

A **pipe** takes the **output of one command** and feeds it as **input to another**.

### 🔁 Basic Syntax:

```bash
command1 | command2 | command3
```

There's no limit on how many commands you can chain together!

> 💡 This is known as a **pipeline** — a sequence of processes where the output of each step becomes the input of the next.

---

## 🔄 Pipe Examples: Combining Commands

You used `sort` and `uniq` together to clean up text and remove duplicates.

### Example: Remove all duplicate lines from `pets.txt`

```bash
sort pets.txt | uniq
```

- `sort`: puts identical lines together
- `uniq`: removes consecutive duplicates

Together, they give you a list of **unique animals**:

```
cat
dog
goldfish
parrot
```

---

## 📄 Applying Commands to Strings and Files

Some tools like `tr` work with **standard input only** — so we use pipes to apply them to strings and file contents.

### Replace vowels in a string with `_`:

```bash
echo "Linux and shell scripting are awesome!" | tr "aeiou" "_"
```

Output:

```
L_n_x _nd sh_ll scr_pt_ng _r_ _w_s_m_!
```

### Convert entire file to uppercase:

```bash
cat pets.txt | tr "[a-z]" "[A-Z]"
```

### Combine with `sort` and `uniq`:

```bash
sort pets.txt | uniq | tr "[a-z]" "[A-Z]"
```

Result:

```
CAT
DOG
GOLDFISH
PARROT
```

---

## 🪣 Extracting Data from JSON Files

You practiced extracting structured data from a JSON file using `grep` and regular expressions.

### Given JSON content in `Bitcoinprice.txt`:

```json
{
  "coin": {
    "price": 57907.78008618953,
    ...
  }
}
```

### Extract the `"price"` field:

```bash
cat Bitcoinprice.txt | grep -oE "\"price\"\s*:\s*[0-9]*\.?[0-9]*"
```

#### Explanation:

- `-o` → show only matched part
- `-E` → enable extended regex
- `\"price\"` → match `"price"`
- `\s*` → match any amount of whitespace
- `:` → match colon
- `[0-9]*\.?[0-9]*` → match numbers with optional decimal point

This gives:

```
"price" : 57907.78008618953
```

---

## 🌐 Extracting Info from URLs

You can combine `curl` or `wget` with `grep` to extract live data from web APIs or pages.

### Example: Get current Bitcoin price from an API:

```bash
curl -s https://api.coinstats.app/public/v1/coins/bitcoin | grep -oE "\"price\": *[0-9]+\.?[0-9]*"
```

Or if you have the JSON saved locally:

```bash
cat Bitcoinprice.txt | grep -oE "\"price\": *[0-9]+\.?[0-9]*"
```

---

## 📋 Summary Table: Useful Pipe Combinations

| Task                           | Command                                    |
| ------------------------------ | ------------------------------------------ | --------------- |
| Sort and deduplicate lines     | `sort file.txt                             | uniq`           |
| Replace characters in a string | `echo "text"                               | tr "from" "to"` |
| Convert text to uppercase      | `tr "[a-z]" "[A-Z]"`                       |
| Extract price from JSON        | `grep -oE "\"price\": *[0-9.]*" file.json` |
| Download and parse data        | `curl example.com/data.json                | grep pattern`   |

---

## 🧠 Why Pipes Matter

Using pipes lets you:

- **Automate complex text processing**
- **Chain small tools into powerful pipelines**
- **Extract and transform data efficiently**
- **Build custom scripts that process logs, config files, or API responses**

They’re at the heart of **Unix philosophy**: _Do one thing well, and connect it with others._

---

## ✅ Final Takeaways

| Concept             | Description                                                         |
| ------------------- | ------------------------------------------------------------------- | --------------------------------------------------- |
| **Pipes** (`        | `)                                                                  | Connect outputs of one command to inputs of another |
| **Filters**         | Tools like `grep`, `uniq`, `tr` act on streamed input               |
| **Data extraction** | Use `grep` with regex to pull values from structured text like JSON |
| **Automation**      | Combine `curl` + `grep` to extract live data from the web           |

---

Great job learning how to **combine commands using pipes**! You're now able to build powerful one-liners that can process text, filter data, and even extract real-time info like cryptocurrency prices.

Would you like to continue with:

- **Exercise – Using Pipes with `awk` and `sed`**
- **Building Reusable Scripts with Pipes**
- **Monitoring Logs in Real-Time with `tail -f` and `grep`**

Let me know — I'm here to help you keep leveling up your Linux skills! 🐧💻📘✨

### USER

Examples of Bash Shell Features
Learning Objectives
After completing this reading, you will be able to:

List examples of metacharacters
Use quoting to specify literal or special character meanings
Implement input and output redirection
Apply command substitution
Describe applications for command line arguments
Metacharacters
Metacharacters are characters having special meaning that the shell interprets as instructions.

Metacharacter Meaning

# Precedes a comment

; Command separator

- Filename expansion wildcard
  ? Single character wildcard in filename expansion
  Pound #
  The pound # metacharacter is used to represent comments in shell scripts or configuration files. Any text that appears after a # on a line is treated as a comment and is ignored by the shell.

1
2
3
4
#!/bin/bash

# This is a comment

echo "Hello, world!" # This is another comment

Copied!
Comments are useful for documenting your code or configuration files, providing context, and explaining the purpose of the code to other developers who may read it. It's a best practice to include comments in your code or configuration files wherever necessary to make them more readable and maintainable.

Semicolon ;
The semicolon ; metacharacter is used to separate multiple commands on a single command line. When multiple commands are separated by a semicolon, they are executed sequentially in the order they appear on the command line.

1
2
3
$ echo "Hello, "; echo "world!"
Hello,
world!

Copied!
As you can see from the example above, the output of each echo command is printed on separate lines and follows the same sequence in which the commands were specified.

The semicolon metacharacter is useful when you need to run multiple commands sequentially on a single command line.

Asterisk _
The asterisk _ metacharacter is used as a wildcard character to represent any sequence of characters, including none.

1
ls \*.txt

Copied!
In this example, \*.txt is a wildcard pattern that matches any file in the current directory with a .txt extension. The ls command lists the names of all matching files.

Question mark ?
The question mark ? metacharacter is used as a wildcard character to represent any single character.

1
ls file?.txt

Copied!
In this example, file?.txt is a wildcard pattern that matches any file in the current directory with a name starting with file, followed by any single character, and ending with the .txt extension.

Quoting
Quoting is a mechanism that allows you to remove the special meaning of characters, spaces, or other metacharacters in a command argument or shell script. You use quoting when you want the shell to interpret characters literally.

Symbol Meaning
\ Escape metacharacter interpretation
" " Interpret metacharacters within string
' ' Escape all metacharacters within string
Backslash \
The backslash character is used as an escape character. It instructs the shell to preserve the literal interpretation of special characters such as space, tab, and $. For example, if you have a file with spaces in its name, you can use backslashes followed by a space to handle those spaces literally:

1
touch file\ with\ space.txt

Copied!
Double quotes " "
When a string is enclosed in double quotes, most characters are interpreted literally, but metacharacters are interpreted according to their special meaning. For example, you can access variable values using the dollar $ character:

1
2
$ echo "Hello $USER"
Hello <username>

Copied!
Single quotes ' '
When a string is enclosed in single quotes, all characters and metacharacters enclosed within the quotes are interpreted literally. Single quotes alter the above example to produce the following output:

1
2
$ echo 'Hello $USER'
Hello $USER

Copied!
Notice that instead of printing the value of $USER, single quotes cause the terminal to print the string "$USER".

Input/Output redirection
Symbol Meaning

>     Redirect output to file, overwrite
>
> >     Redirect output to file, append
> >
> > 2> Redirect standard error to file, overwrite
> > 2>> Redirect standard error to file, append
> > < Redirect file contents to standard input
> > Input/output (IO) redirection is the process of directing the flow of data between a program and its input/output sources.

By default, a program reads input from standard input, the keyboard, and writes output to standard output, the terminal. However, using IO redirection, you can redirect a program's input or output to or from a file or another program.

Redirect output >
This symbol is used to redirect the standard output of a command to a specified file.

ls > files.txt will create a file called files.txt if it doesn't exist, and write the output of the ls command to it.

Warning: When the file already exists, the output overwrites all of the file's contents!

Redirect and append output >>
This notation is used to redirect and append the output of a command to the end of a file. For example,

ls >> files.txt appends the output of the ls command to the end of file files.txt, and preserves any content that already existed in the file.

Redirect standard output 2>
This notation is used to redirect the standard error output of a command to a file. For example, if you run the ls command on a non-existing directory as follows,

ls non-existent-directory 2> error.txt the shell will create a file called error.txt if it doesn't exist, and redirect the error output of the ls command to the file.

Warning: When the file already exists, the error message overwrites all of the file's contents!

Append standard error 2>>
This symbol redirects the standard error output of a command and appends the error message to the end of a file without overwriting its contents.

ls non-existent-directory 2>> error.txt will append the error output of the ls command to the end of the error.txt file.

Redirect input <
This symbol is used to redirect the standard input of a command from a file or another command. For example,

sort < data.txt will sort the contents of the data.txt file.

Command Substitution
Command substitution allows you to run command and use its output as a component of another command's argument. Command substitution is denoted by enclosing a command in either backticks (`command`) or using the $() syntax. When the encapsulate command is executed, its output is substituted in place, and it can be used as an argument within another command. This is particularly useful for automating tasks that require the use of a command's output as input for another command.

For example, you could store the path to your current directory in a variable by applying command substitution on the pwd command, then move to another directory, and finally return to your original directory by invoking the cd command on the variable you stored, as follows:

1
2
3
$ here=$(pwd)
$ cd path_to_some_other_directory
$ cd $here

Copied!
Command Line Arguments
Command line arguments are additional inputs that can be passed to a program when the program is run from a command line interface. These arguments are specified after the name of the program, and they can be used to modify the behavior of the program, provide input data, or provide output locations. Command line arguments are used to pass arguments to a shell script.

For example, the following command provides two arguments, arg1, and arg2, that can be accessed from within your Bash script:

1
$ ./MyBashScript.sh arg1 arg2

Copied!
Summary
In this reading, you learned that:

Metacharacters such as #, ;, \*, and ? are characters that the shell interprets with special meanings
Quoting allows you to ensure any special characters, spaces, or other metacharacters are interpreted literally by the shell
Input/output redirection redirects a program's input or output to/from a file
Command substitution allows you to use the output of a command as an argument for another command
Command line arguments can be used to pass information to a shell script

### ASSISTANT

# 🧠 **Examples of Bash Shell Features – Summary & Highlights**

In this reading, you explored several powerful features of the **Bash shell**, which are essential for writing clean, effective, and dynamic scripts.

---

## 🔤 **Metacharacters in Bash**

These characters have special meanings to the shell and help control how commands behave.

| Metacharacter | Meaning                                        |
| ------------- | ---------------------------------------------- |
| `#`           | Starts a comment (everything after is ignored) |
| `;`           | Separates multiple commands on one line        |
| `*`           | Wildcard matching any number of characters     |
| `?`           | Matches exactly one character                  |

### Examples:

```bash
# This is a comment
echo "Hello"; echo "World"  # Runs both commands
ls *.txt                      # Lists all .txt files
ls file?.txt                  # Matches file1.txt, file2.txt, etc.
```

---

## “ ” `' '` `\` **Quoting and Escaping**

Use quoting to control how the shell interprets special characters.

| Symbol | Behavior                                   |
| ------ | ------------------------------------------ |
| `\`    | Escape single character (e.g., `\$`, `\*`) |
| `" "`  | Allows variable expansion inside string    |
| `' '`  | Treats everything literally — no expansion |

### Examples:

```bash
touch file\ with\ space.txt   # Creates a file with spaces in name
echo "Today is $USER"         # Expands variables like $USER
echo 'Today is $USER'         # Prints literal "$USER"
```

---

## 📥 **Input/Output Redirection**

You can redirect input (`<`), output (`>` or `>>`), and error streams (`2>`, `2>>`) to or from files.

| Operator | Purpose                                    |
| -------- | ------------------------------------------ |
| `>`      | Redirect standard output (overwrites file) |
| `>>`     | Append standard output to file             |
| `2>`     | Redirect standard error (overwrites)       |
| `2>>`    | Append standard error                      |
| `<`      | Redirect input from a file                 |

### Examples:

```bash
ls > files.txt          # Saves ls output to files.txt
ls >> files.txt         # Appends more data
grep "error" log.txt > errors.txt  # Saves only matching lines
sort < data.txt         # Sorts content from data.txt
```

---

## 💡 **Command Substitution**

Allows you to capture and reuse command outputs as values in your scripts.

### Syntax:

- Backticks: `` `command` `` _(legacy)_
- Preferred: `$(command)` _(modern and nested-friendly)_

### Example:

```bash
here=$(pwd)
cd /tmp
cd $here
```

This lets you store and reuse results dynamically in scripts — great for automation!

---

## 📝 **Command Line Arguments**

Arguments passed to a script when it’s executed. You can access them using positional parameters.

### Example:

```bash
./myscript.sh arg1 arg2
```

Inside the script:

```bash
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
```

### Positional Parameters:

| Variable        | Description                                 |
| --------------- | ------------------------------------------- |
| `$0`            | Script name                                 |
| `$1`, `$2`, ... | First, second, etc., command-line arguments |
| `$@`            | All arguments as list                       |
| `$#`            | Number of arguments                         |
| `$$`            | PID (Process ID) of the script              |
| `$?`            | Exit status of last command                 |

---

## 🔄 Why These Bash Features Matter

| Feature                  | Use Case                                                        |
| ------------------------ | --------------------------------------------------------------- |
| **Metacharacters**       | Pattern matching, scripting logic                               |
| **Quoting/Escaping**     | Handling filenames, strings with spaces, and special characters |
| **Redirection**          | Logging, filtering, saving output                               |
| **Command substitution** | Dynamic values, reusable scripts                                |
| **Command line args**    | Flexible scripts that behave differently based on inputs        |

---

## ✅ Real-World Examples

### 1. Save and restore directory:

```bash
current_dir=$(pwd)
cd /tmp
cd "$current_dir"
```

### 2. Log output and errors separately:

```bash
my_script.sh > output.log 2> error.log
```

### 3. Pass and use arguments in a script:

```bash
#!/bin/bash
echo "Script name: $0"
echo "First argument: $1"
echo "Number of arguments: $#"
```

Run it:

```bash
chmod +x myscript.sh
./myscript.sh Hello World!
```

Output:

```
Script name: ./myscript.sh
First argument: Hello
Number of arguments: 2
```

---

## 🛠️ Best Practices

- Always quote variables to avoid word splitting:
  ```bash
  echo "$USER"
  ```
- Use `$(...)` over backticks for better readability and nesting
- Use `>` carefully — it **overwrites** by default
- Use `>>` to **append** instead
- Include comments using `#` for clarity and documentation

---

Great job learning these key Bash shell features!  
You now know how to:

- Control character interpretation with **quoting**
- Manipulate input/output with **redirection**
- Make scripts **dynamic** with **command substitution**
- Build **flexible scripts** that accept **command-line arguments**

---

Would you like to continue with:

- **Exercise – Writing Scripts Using Command Line Arguments**
- **Using Pipes and Filters Together**
- **Automating Tasks with Bash Functions**

Let me know — I'm here to help you write even more powerful Linux scripts! 🐧💻📘✨

### USER

Exercise 1 - Using conditional statements and logical operators
In this exercise, you will create a simple Bash script containing a conditional statement to handle the following tasks:

Prompt the user for a Yes or No response to a question
Print a response based on the user's answer
1.1. Create a new Bash script
Create a Bash script file and make it executable.

Click here for Hint
Click here for Solution
Here's a solution using only the command line:
1
2
echo '#!/bin/bash' > conditional_script.sh
chmod u+x conditional_script.sh

Copied!

Executed!
1.2. Query the user and store their response
Now get your script to:

Ask the user a binary "yes or no" question of your choosing
Store the user's answer in a variable.
Click here for Hint
Click here for Solution
Your Bash script should now look something like this:

1
2
3
4
5
#!/bin/bash
echo 'Are you enjoying this course so far?'
echo -n "Enter \"y\" for yes, \"n\" for no."
read response

Copied!

Executed!
1.3. Use a conditional block to select a response for the user
Finally, use a conditional block to print a message to the user based on their response to your query.

Tip: It's best practice to also handle the case where the reponse doesn't match any of the allowable responses.

Click here for Hint
Click here for Solution
Now your Bash script should be similar to the following:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
#!/bin/bash
echo 'Are you enjoying this course so far?'
echo -n "Enter \"y\" for yes, \"n\" for no"
read response
if [ "$response" == "y" ]
then
echo "I'm pleased to hear you are enjoying the course!"
echo "Your feedback regarding what you have been enjoying would be most welcome!"
elif [ "$response" = "n" ]
then
echo "I'm sorry to hear you are not enjoying the course."
echo "Your feedback regarding what we can do to improve the learning experience"
echo "for this course would be greatly appreciated!"
else
echo "Your response must be either 'y' or 'n'."
echo "Please re-run the script to try again."
fi

### ASSISTANT

# 🧠 Exercise 1 – Using Conditional Statements and Logical Operators in Bash

In this exercise, you learned how to use **conditional logic** in a Bash script — specifically using the `if`, `elif`, and `else` structure.

You built a script that:

- Asks the user a yes/no question
- Stores their response
- Responds differently depending on whether they typed `"y"` or `"n"`
- Handles invalid input gracefully

This is a foundational skill for writing **interactive shell scripts**.

---

## ✅ Step-by-Step Breakdown

### 🔹 1.1 Create a New Bash Script

#### Create and make it executable:

```bash
echo '#!/bin/bash' > conditional_script.sh
chmod u+x conditional_script.sh
```

> This creates a new script file with execute permissions for the owner.

---

### 🔹 1.2 Prompt the User and Store Their Response

#### Add code to ask a question and store input:

```bash
#!/bin/bash
echo 'Are you enjoying this course so far?'
echo -n "Enter \"y\" for yes, \"n\" for no: "
read response
```

- `echo` prints messages to the screen
- `echo -n` prevents a newline after printing (keeps prompt on same line)
- `read response` stores user input in a variable called `response`

---

### 🔹 1.3 Use a Conditional Block Based on User Input

#### Add the conditional logic:

```bash
if [ "$response" == "y" ]; then
    echo "I'm pleased to hear you are enjoying the course!"
    echo "Your feedback regarding what you have been enjoying would be most welcome!"

elif [ "$response" = "n" ]; then
    echo "I'm sorry to hear you are not enjoying the course."
    echo "Your feedback regarding what we can do to improve the learning experience"
    echo "for this course would be greatly appreciated!"

else
    echo "Your response must be either 'y' or 'n'."
    echo "Please re-run the script to try again."
fi
```

### 📝 Explanation:

| Feature                          | Description                                             |
| -------------------------------- | ------------------------------------------------------- |
| `[ ... ]`                        | Test condition syntax                                   |
| `==` or `=`                      | String comparison operators                             |
| `if/elif/else/fi`                | Conditional block                                       |
| Quoted variables (`"$response"`) | Prevents errors if variable is empty or contains spaces |

---

## 🧪 Sample Outputs

### If user enters `y`:

```
I'm pleased to hear you are enjoying the course!
Your feedback regarding what you have been enjoying would be most welcome!
```

### If user enters `n`:

```
I'm sorry to hear you are not enjoying the course.
Your feedback regarding what we can do to improve the learning experience
for this course would be greatly appreciated!
```

### If user enters something else:

```
Your response must be either 'y' or 'n'.
Please re-run the script to try again.
```

---

## 📋 Summary Table

| Task                | Command                          |
| ------------------- | -------------------------------- |
| Create a new script | `echo '#!/bin/bash' > script.sh` |
| Make it executable  | `chmod u+x script.sh`            |
| Read user input     | `read variable_name`             |
| Conditional logic   | `if [ condition ]; then ... fi`  |
| Compare strings     | `[ "$var" == "value" ]`          |
| Handle default case | `else`                           |
| Run your script     | `./script.sh`                    |

---

## 🛠️ Real-World Uses of Conditional Logic

Conditional statements like this are used for:

- Validating user input in setup scripts
- Checking system conditions before performing actions
- Controlling flow in automation tools
- Writing interactive CLI apps in Bash

---

## 💡 Pro Tips

- Always quote variables to avoid unexpected behavior:
  ```bash
  if [ "$response" = "y" ]; then
  ```
- Use `[[ ... ]]` instead of `[ ... ]` for advanced features (like regex matching) in modern Bash
- You can simplify responses by converting input to lowercase:
  ```bash
  response="${response,,}"
  ```

---

Great job building your first **interactive Bash script** using **conditional logic**!

Would you like to continue with:

- **Exercise 2 – Loops in Bash Scripts**
- **Using `case` for Multiple Conditions**
- **Validating Input with Regular Expressions**

Let me know — I'm here to help you write even more powerful Linux scripts! 🐧💻📘✨

### USER

Exercise 2 - Performing basic mathematical calculations and numerical logical comparisons
In this exercise, you will create a Bash script that performs basic arithmetic calculations on two integers entered by the user. You will also use logical comparisons to determine which calculation leads to the greatest result.

2.1. Create a Bash script
Create an executable Bash script that prompts the user for two integers, then stores and prints both the sum and product of the two integers.

Click here for Hint
Click here for Solution
1
2
3
4
5
6
7
8
9
10
11
12
#!/bin/bash
echo -n "Enter an integer: "
read n1
echo -n "Enter another integer: "
read n2
sum=$(($n1+$n2))
product=$(($n1*$n2))
echo "The sum of $n1 and $n2 is $sum"
echo "The product of $n1 and $n2 is $product."

Copied!
2.2. Add logic to your script
Add logic to your script that determines whether the sum is greater than, less than, or equal to the product. Display an appropriate statement corresponding to each possible result.

Assume the user inputs two integers. Don't worry about handling the case where the user inputs a non-integer string by mistake.

Click here for Hint
Click here for Solution
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
#!/bin/bash
echo -n "Enter an integer: "
read n1
echo -n "Enter another integer: "
read n2
sum=$(($n1+$n2))
product=$(($n1*$n2))
echo "The sum of $n1 and $n2 is $sum"
echo "The product of $n1 and $n2 is $product."
if [ $sum -lt $product ]
then
echo "The sum is less than the product."
elif [[$sum == $product]]
then
echo "The sum is equal to the product."
elif [ $sum -gt $product ]
then
echo "The sum is greater than the product."
fi

### ASSISTANT

# 🧮 Exercise 2 – Performing Basic Math and Logical Comparisons in Bash

In this hands-on exercise, you created a **Bash script** that:

- Accepts two integers from the user
- Performs basic math: addition and multiplication
- Compares results using **numeric conditional operators**
- Outputs comparison results to the user

This helps you understand how to work with **arithmetic operations**, **variables**, and **numerical logic** in shell scripting.

---

## ✅ Step-by-Step Breakdown

### 🔹 2.1 Create a Bash Script for Input and Calculations

You created a script that takes two integers as input:

```bash
#!/bin/bash
echo -n "Enter an integer: "
read n1
echo -n "Enter another integer: "
read n2
```

Then calculated:

```bash
sum=$(($n1 + $n2))
product=$(($n1 * $n2))
```

And printed the result:

```bash
echo "The sum of $n1 and $n2 is $sum"
echo "The product of $n1 and $n2 is $product."
```

> 📝 The syntax `$(())` is used in Bash for **arithmetic expansion** — it evaluates mathematical expressions.

---

### 🔹 2.2 Add Logic to Compare Results

You added an `if-elif-else` block to compare the **sum** and **product**:

```bash
if [ $sum -lt $product ]; then
   echo "The sum is less than the product."
elif [[ $sum == $product ]]; then
   echo "The sum is equal to the product."
elif [ $sum -gt $product ]; then
   echo "The sum is greater than the product."
fi
```

> ⚠️ Note: You used `-lt`, `-gt`, and `==` for numeric comparisons.

| Operator | Meaning               |
| -------- | --------------------- |
| `-lt`    | Less than             |
| `-le`    | Less than or equal    |
| `-eq`    | Equal                 |
| `-ge`    | Greater than or equal |
| `-gt`    | Greater than          |

---

## 🧪 Sample Output Scenarios

### Case 1: Sum < Product

```
Enter an integer: 3
Enter another integer: 5
The sum of 3 and 5 is 8
The product of 3 and 5 is 15.
The sum is less than the product.
```

### Case 2: Sum == Product

```
Enter an integer: 2
Enter another integer: 2
The sum of 2 and 2 is 4
The product of 2 and 2 is 4.
The sum is equal to the product.
```

### Case 3: Sum > Product

```
Enter an integer: 5
Enter another integer: 1
The sum of 5 and 1 is 6
The product of 5 and 1 is 5.
The sum is greater than the product.
```

---

## 📋 Summary Table

| Task                           | Command                            |
| ------------------------------ | ---------------------------------- |
| Read user input                | `read var_name`                    |
| Perform arithmetic             | `$(($n1 + $n2))`, `$(($n1 * $n2))` |
| Print formatted output         | `echo "Result: $result"`           |
| Compare numbers (less than)    | `[ $a -lt $b ]`                    |
| Compare numbers (equal)        | `[ $a -eq $b ]`                    |
| Compare numbers (greater than) | `[ $a -gt $b ]`                    |

---

## 💡 Pro Tips

- Always use spaces around operators:

  ```bash
  # Correct
  if [ $a -gt $b ]

  # Incorrect
  if [$a-gt$b] ❌
  ```

- Validate input (optional enhancement):

  ```bash
  if ! [[ "$n1" =~ ^[0-9]+$ && "$n2" =~ ^[0-9]+$ ]]; then
      echo "Please enter valid integers."
      exit 1
  fi
  ```

  This checks if both inputs are integers before doing calculations.

- Use `let` for inline assignments:

  ```bash
  let sum=n1+n2
  ```

- Or use alternative syntax:
  ```bash
  (( sum = n1 + n2 ))
  ```

---

## 🤓 Why This Matters

You're now able to:

- Handle **user input**
- Perform **basic math** in Bash scripts
- Use **conditional logic** based on numerical comparisons
- Write more advanced scripts that can handle **dynamic user data**

These skills form the foundation for writing **interactive**, **logical**, and **automated** command-line tools in Linux.

---

Would you like to continue with:

- **Exercise 3 – Using Loops in Bash Scripts**
- **Using `case` Statements for Multiple Conditions**
- **Writing Functions in Bash**

Let me know — I'm here to help you keep building powerful automation scripts! 🐧💻📘🧮✨

### USER

Exercise 3 - Using arrays for storing and accessing data within for loops
In this exercise, you will create a report based on a supplied dataset using the CSV format. You will extract the columns of the dataset into separate arrays and create a new column using arithmetic and array logic. Finally, you will combine the dataset with the new column and save the resulting report as a CSV file.

3.1. Download a CSV file to your current working directory
The file, arrays_table.csv, is located at the following url:

1
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/M3/L2/arrays_table.csv

Copied!
Click here for Hint
Click here for Solution
1
2
csv_file="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/M3/L2/arrays_table.csv "
wget $csv_file

Copied!
3.2. Display the CSV file to understand what it looks like
Click here for Hint
Click here for Solution
1
cat arrays_table.csv

Copied!
3.3. Create a Bash script that parses table columns into 3 arrays
Click here for Hint
Click here for Solution
1
2
3
4
5
6
7
8
9
10
11
12
#!/bin/bash
csv_file="./arrays_table.csv"

# parse table columns into 3 arrays

column_0=($(cut -d "," -f 1 $csv_file))
column_1=($(cut -d "," -f 2 $csv_file))
column_2=($(cut -d "," -f 3 $csv_file))

# print first array

echo "Displaying the first column:"
echo "${column_0[@]}"

Copied!
3.4. Create a new array as the difference of the third and second columns.
Initialize your new array with a header (a column name), and remember to validate your results.

Click here for Hint 1
Use a loop to populate your array.

Determine the number of elements you need and incorporate within your loop statement.

Print both the number of elements and the contents of your new array to validate your logic.

Click here for Hint 2
Recall the for loop notation when you know the number of iterations needed, and that array indexing starts at 0.

To get the number of lines, use command subsitution on a pipeline that uses the cat and wc commands as filters and store the result in a variable.

Click here for Solution
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
#!/bin/bash
csv_file="./arrays_table.csv"

# parse table columns into 3 arrays

column_0=($(cut -d "," -f 1 $csv_file))
column_1=($(cut -d "," -f 2 $csv_file))
column_2=($(cut -d "," -f 3 $csv_file))

# print first array

echo "Displaying the first column:"
echo "${column_0[@]}"

## Create a new array as the difference of columns 1 and 2

# initialize array with header

column_3=("column_3")

# get the number of lines in each column

nlines=$(cat $csv_file | wc -l)
echo "There are $nlines lines in the file"

# populate the array

for ((i=1; i<$nlines; i++)); do
  column_3[$i]=$((column_2[$i] - column_1[$i]))
done
echo "${column_3[@]}"

Copied!
3.5. Create a report by combining your new column with the source table
Save your report as a CSV file.

Remember to validate your results.

Click here for Hint 1
Write the new array to file line-by-line.

Intitialize the file with a header.

Click here for Hint 2
Use redirection and recall how to merge two files side-by-side.

Ensure your final report has the correct CSV format.

Click here for Solution
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
#!/bin/bash
csv_file="./arrays_table.csv"

# parse table columns into 3 arrays

column_0=($(cut -d "," -f 1 $csv_file))
column_1=($(cut -d "," -f 2 $csv_file))
column_2=($(cut -d "," -f 3 $csv_file))

# print first array

echo "Displaying the first column:"
echo "${column_0[@]}"

## Create a new array as the difference of columns 1 and 2

# initialize array with header

column_3=("column_3")

# get the number of lines in each column

nlines=$(cat $csv_file | wc -l)
echo "There are $nlines lines in the file"

# populate the array

for ((i=1; i<$nlines; i++)); do
  column_3[$i]=$((column_2[$i] - column_1[$i]))
done
echo "${column_3[@]}"

## Combine the new array with the csv file

# first write the new array to file

# initialize the file with a header

echo "${column_3[0]}" > column_3.txt
for ((i=1; i<nlines; i++)); do
  echo "${column_3[$i]}" >> column_3.txt
done
paste -d "," $csv_file column_3.txt > report.csv

### ASSISTANT

# 🧮 Exercise 3 – Using Arrays and For Loops in Bash Scripts

In this exercise, you learned how to:

- **Download and inspect a CSV file**
- **Extract columns into arrays using `cut`**
- **Create a new array by performing arithmetic on other arrays**
- **Combine data back into a new CSV report using `paste`**

This is a powerful demonstration of how **Bash scripting can be used for basic data processing** — especially when working with structured text files like CSVs.

---

## ✅ Step-by-Step Breakdown

### 🔹 3.1 Download the CSV File

You downloaded a sample dataset:

```bash
csv_file="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/M3/L2/arrays_table.csv"
wget $csv_file
```

This gave you a file named `arrays_table.csv`.

---

### 🔹 3.2 View the CSV Content

You inspected it with:

```bash
cat arrays_table.csv
```

Example content:

```
column_0,column_1,column_2
A,10,50
B,20,40
C,30,30
D,40,20
E,50,10
```

Each line represents a row, and each column holds different types of data.

---

### 🔹 3.3 Parse Columns into Arrays

You extracted each column using `cut` and stored them in **Bash arrays**:

```bash
column_0=($(cut -d "," -f 1 $csv_file))
column_1=($(cut -d "," -f 2 $csv_file))
column_2=($(cut -d "," -f 3 $csv_file))
```

> 💡 This uses **command substitution** (`$(...)`) to populate arrays from command output.

Then you printed one of them:

```bash
echo "${column_0[@]}"
```

Output:

```
column_0 A B C D E
```

Note: The first element is the header (`column_0`, `column_1`, etc.)

---

### 🔹 3.4 Create a New Array as a Difference Between Two Columns

You created a new array, `column_3`, which stores the difference between `column_2` and `column_1`.

#### Initialize with header:

```bash
column_3=("column_3")
```

#### Count lines in the CSV:

```bash
nlines=$(cat $csv_file | wc -l)
```

#### Loop through rows and calculate:

```bash
for ((i=1; i<$nlines; i++)); do
  column_3[$i]=$((column_2[i] - column_1[i]))
done
```

Then you printed the result:

```bash
echo "${column_3[@]}"
```

Example output:

```
column_3 40 20 0 -20 -40
```

> ⚠️ Bash supports only integer math — so this works perfectly for numeric columns.

---

### 🔹 3.5 Combine New Column with Original CSV

You wrote the new column to a temporary file:

```bash
echo "${column_3[0]}" > column_3.txt
for ((i=1; i<nlines; i++)); do
  echo "${column_3[$i]}" >> column_3.txt
done
```

Then merged it with the original CSV:

```bash
paste -d "," $csv_file column_3.txt > report.csv
```

Now `report.csv` contains all four columns!

Example output:

```
column_0,column_1,column_2,column_3
A,10,50,40
B,20,40,20
C,30,30,0
D,40,20,-20
E,50,10,-40
```

---

## 📋 Summary Table

| Task                     | Command                                 |
| ------------------------ | --------------------------------------- |
| Download file            | `wget URL`                              |
| View file contents       | `cat arrays_table.csv`                  |
| Extract column 1         | `cut -d "," -f 1`                       |
| Store in array           | `arr=($(cut ...))`                      |
| Loop over elements       | `for ((i=1; i < $nlines; i++))`         |
| Perform arithmetic       | `$((col2 - col1))`                      |
| Write array to file      | `echo "value" >> file.txt`              |
| Merge files side-by-side | `paste -d "," file1 file2 > output.csv` |

---

## 🧠 Why This Matters

This exercise introduced you to:

- **Array manipulation** in Bash
- **Looping through indexed elements**
- Performing **basic arithmetic**
- Working with **CSV data** via shell commands

These skills are useful for:

- Processing logs or flat-file databases
- Automating simple data transformations
- Building lightweight reporting tools without external dependencies

---

## 💡 Pro Tips

- Use `${array[@]}` to access all elements in an array
- Remember array indexing starts at 0
- Always quote variables to avoid issues:
  ```bash
  echo "${column_0[@]}"
  ```
- You can validate that arrays have the same length before merging:
  ```bash
  [[ ${#column_0[@]} -eq ${#column_3[@]} ]] && echo "Arrays match in size"
  ```

---

## 🛠️ Real-World Uses

| Use Case            | Example                                                  |
| ------------------- | -------------------------------------------------------- |
| Log analysis        | Extract timestamps, process times, and compute durations |
| Data transformation | Add computed fields to CSV reports                       |
| Batch operations    | Process multiple files in order                          |
| Automation          | Generate summaries from system metrics                   |

---

Great job mastering **arrays**, **loops**, and **data manipulation in Bash**!  
You've built a full script that reads, processes, and writes structured data — a skill directly applicable to real-world scripting tasks.

Would you like to continue with:

- **Exercise 4 – Functions in Bash Scripts**
- **Using `awk` for Advanced Text Processing**
- **Writing Conditional Logic with `case` Statements**

Let me know — I'm here to help you keep building your Linux scripting superpowers! 🐧💻📘🧮✨

### USER

Conclusion
Congratulations! You have just completed a hands-on lab using advanced Bash scripting logic.

In this lab, you learned that you can use:

Conditional statements to run commands based on whether a specified condition is true or false
Logical operators to make true/false operators
Arithmetic operators to perform basic mathematical calculations
List-like arrays to store and access data
for loops to execute repetitive tasks
You covered a lot of material here that will be very useful going forward. You will encounter similar problems in your practice and final projects and, best of all, in your career! Remember - you can always come back and review your labs.

Tip: It is worth noting that had we been only interested in efficiency, one of the steps could have been avoided. Specifically, you could have redirected your calculations to a text file line-by-line rather than storing them in an array and then writing the array to file.

Finally, we encourage you to post a review and a rating for this course at any time!

### ASSISTANT

# 🎉 **Conclusion – Great Job Completing the Lab!**

You've successfully completed a hands-on lab that dives into **advanced Bash scripting logic** — and you're now equipped with powerful tools to write more intelligent, dynamic, and efficient scripts.

---

## ✅ What You Learned

Here’s what you accomplished in this lab:

| Concept                     | Tool / Technique                                                              |
| --------------------------- | ----------------------------------------------------------------------------- |
| **Conditional Logic**       | `if`, `elif`, `else` blocks for decision-making                               |
| **Logical Operators**       | Used `-lt`, `-gt`, `-eq` for numeric comparisons                              |
| **Mathematical Operations** | Performed addition and subtraction using `$(( ... ))`                         |
| **Arrays**                  | Stored and accessed data like lists (`column_0=($(cut ...))`)                 |
| **For Loops**               | Repeated tasks efficiently using indexed loops                                |
| **Data Processing**         | Read from and wrote structured CSV data using `cut`, `paste`, and redirection |

---

## 🧠 Why This Matters

The skills you practiced are not just academic — they’re essential for:

- **Automation**: Build scripts that make decisions based on input
- **Data Wrangling**: Parse and transform structured text files (like logs or CSVs)
- **Reporting**: Generate clean output files dynamically from raw data
- **Scripting Efficiency**: Know when to use arrays vs. direct file writing

> 💡 Even though Bash isn’t a full-fledged programming language like Python, it's incredibly useful for quick automation, system management, and integration tasks.

---

## 🛠️ Real-World Applications

Here’s how these concepts apply beyond the lab:

| Skill                  | Use Case                                                         |
| ---------------------- | ---------------------------------------------------------------- |
| Conditional statements | Validate user input, check system status before running commands |
| Arithmetic operations  | Monitor thresholds, calculate durations                          |
| Arrays and loops       | Batch process files, manage large datasets                       |
| CSV manipulation       | Generate reports, analyze log files                              |
| Script modularity      | Break complex logic into reusable parts (coming soon!)           |

---

## 🚀 Next Steps

Would you like to continue with:

- **Exercise 4 – Writing and Using Functions in Bash**
- **Processing Data with `awk` and `sed`**
- **Advanced Scripting: Debugging, Error Handling, and Modularization**

Let me know — I'm here to help you keep building real-world Linux scripting skills!

And don't forget — sharing your feedback helps others learn about this course too.  
If you enjoyed this lab, consider leaving a review at any time!

---

Keep going — you're well on your way to mastering **Bash scripting** like a pro! 🐧💻📘🧮✨

### USER

Exercise 1 - Understand crontab file syntax
Cron is a system daemon used to execute desired tasks in the background at designated times.

A crontab file is a simple text file containing a list of commands meant to be run at specified times. It is edited using the crontab command.

Each line in a crontab file has five time-and-date fields, followed by a command, followed by a newline character (\n). The fields are separated by spaces.

The five time-and-date fields cannot contain spaces and their allowed values are as follows:

Field Allowed values
minute 0-59
hour 0-23, 0 = midnight
day 1-31
month 1-12
weekday 0-6, 0 = Sunday

### ASSISTANT

# 🕒 Exercise 1 – Understand `crontab` File Syntax

In this exercise, you learned how to schedule tasks using **cron**, a time-based job scheduler in Linux. You explored the structure of a **crontab file**, which is used to define scheduled commands.

---

## 🎯 Learning Objective Recap

After completing this exercise, you are now able to:
✅ Explain what **cron** and **crontab** are  
✅ Understand the **syntax** for scheduling jobs  
✅ Define when a command should run using **five time fields**

---

## 🧠 What Is Cron?

- **Cron** is a **daemon (background process)** that runs on Linux systems.
- It allows users to schedule scripts or commands to run automatically at specified times — like an alarm clock for your system!

---

## 📄 What Is a Crontab File?

A **crontab** (short for **cron table**) is a configuration file that tells cron what to do and when.

Each line in the crontab represents one scheduled task.

### 🔢 Crontab Line Format:

```
minute hour day month weekday command_to_execute
```

| Field     | Description                         | Allowed Values          |
| --------- | ----------------------------------- | ----------------------- |
| `minute`  | Minute of the hour                  | `0–59`                  |
| `hour`    | Hour of the day (24-hour format)    | `0–23` (0 = midnight)   |
| `day`     | Day of the month                    | `1–31`                  |
| `month`   | Month of the year                   | `1–12`                  |
| `weekday` | Day of the week                     | `0–6` (0 = Sunday)      |
| `command` | The actual command or script to run | Any valid shell command |

> ⚠️ Fields must be separated by **spaces or tabs**  
> ⚠️ Commands must end with a **newline**

---

## 🧩 Example Crontab Lines

```bash
# Run a backup script every day at 2 AM
0 2 * * * /home/user/scripts/backup.sh

# Run a cleanup script every Monday at 1:30 AM
30 1 * * 1 /home/user/scripts/cleanup.sh

# Run a script every 15 minutes
*/15 * * * * /home/user/scripts/check_status.sh
```

---

## 📌 Special Characters You Can Use

| Symbol | Meaning         | Example                                         |
| ------ | --------------- | ----------------------------------------------- |
| `*`    | Any value       | `* * * * *` → Every minute                      |
| `,`    | List separator  | `0 0 * * 0,4` → Sunday and Thursday at midnight |
| `-`    | Range of values | `0 8-17 * * *` → Every hour from 8 AM to 5 PM   |
| `/`    | Step values     | `*/10 * * * *` → Every 10 minutes               |

---

## ✅ Summary Table

| Task                          | Command                        |
| ----------------------------- | ------------------------------ |
| Edit current user’s crontab   | `crontab -e`                   |
| View current user’s crontab   | `crontab -l`                   |
| Remove current user’s crontab | `crontab -r`                   |
| System-wide cron files        | `/etc/crontab`, `/etc/cron.d/` |

---

## 🛠️ Real-World Examples

| Schedule                              | Crontab Entry                           |
| ------------------------------------- | --------------------------------------- |
| Every day at 3:00 AM                  | `0 3 * * * /scripts/daily_backup.sh`    |
| Every 5 minutes                       | `*/5 * * * * /scripts/check_health.sh`  |
| At 12:00 PM on the 1st of every month | `0 12 1 * * /scripts/monthly_report.sh` |
| Every Saturday at 1:30 AM             | `30 1 * * 6 /scripts/weekly_cleanup.sh` |

---

## 💡 Pro Tips

- Always test your scripts manually before adding them to `crontab`.
- Use absolute paths for scripts in cron (e.g., `/home/user/scripts/backup.sh`)
- Redirect output to a log file or `/dev/null` to avoid email spam:
  ```bash
  0 2 * * * /scripts/log_system_stats.sh >> /var/log/system_stats.log 2>&1
  ```

---

Great job learning how to schedule tasks using `cron` and understanding the **structure of a `crontab` file**!  
This is a foundational skill for automation and system maintenance.

Would you like to continue with:

- **Exercise 2 – Editing Your Crontab**
- **Scheduling Scripts with Cron**
- **Using `at` for One-Time Scheduled Jobs**

Let me know — I'm here to help you automate your way to efficiency! 🐧⏰📘✨

### USER

Exercise 2 - List cron jobs
Open a new terminal, by clicking on the menu bar and selecting Terminal->New Terminal, as in the image below.

This will open a new terminal at the bottom of the screen as in the image below.

Run the commands below on the newly opened terminal.

The -l option of the crontab command prints the current crontab.

1
crontab -l

Copied!
You may get a message no crontab for theia if your crontab is empty.

### ASSISTANT

# 📋 Exercise 2 – List Cron Jobs

In this exercise, you learned how to **view your current cron jobs** using the `crontab -l` command.

This is an essential step when managing scheduled tasks — whether you're checking what's already set up or preparing to add new automated jobs.

---

## ✅ Step-by-Step Breakdown

### 🔹 Open a New Terminal

You clicked:

- **Terminal → New Terminal** (from the menu bar)

A new terminal window opened at the bottom of the screen.

---

### 🔹 View Current User’s Crontab

You ran:

```bash
crontab -l
```

This command **lists** all scheduled jobs for the current user.

> Output example:

```
no crontab for theia
```

This message simply means that no cron jobs have been defined yet — which is normal in a fresh environment.

---

## 🧠 Why This Matters

Even if there were no existing cron jobs, knowing how to **list** them is critical for:

- Verifying scheduled scripts or commands
- Debugging issues with automation
- Ensuring system maintenance tasks are running
- Avoiding duplicate entries when adding new jobs

---

## 📌 Summary Table: Common Crontab Commands

| Task                                    | Command      |
| --------------------------------------- | ------------ |
| **List current user’s cron jobs**       | `crontab -l` |
| **Edit current user’s cron jobs**       | `crontab -e` |
| **Remove all current user’s cron jobs** | `crontab -r` |

---

## 💡 Pro Tips

- If you're using `sudo`, you may be editing a different crontab (system-wide):

  ```bash
  sudo crontab -l
  ```

- Always use `crontab -l` before making changes — it shows what’s already scheduled.

- Save output to a file for backup:
  ```bash
  crontab -l > my_crontab_backup.txt
  ```

---

Great job completing this short but important exercise!

Would you like to continue with:

- **Exercise 3 – Editing Your Crontab and Scheduling Jobs**
- **Creating a Script to Schedule with Cron**
- **Automating Daily Tasks Using Cron**

Let me know — I'm here to help you master task automation in Linux! 🐧⏰📘✨

### USER

Exercise 3 - Add a job in the crontab file
3.1. Add a job to crontab
To add a cron job, run the command below:

1
crontab -e

Copied!
This will create a new crontab file for you (if you don't have one already). Now you are ready to add a new cron job.

Your crontab file will be opened in an editor as shown in the image below:

Scroll down to the end of the file using the arrow keys:

Add the below line at the end of the crontab file:

1
0 21 \* \* \* echo "Welcome to cron" >> /tmp/echo.txt

Copied!

The above job specifies that the echo command should run when the minute is 0 and the hour is 21. It effectively means the job runs at 9.00 p.m every day.

The output of the command should be sent to a file /tmp/echo.txt.

Press Ctrl + x to save the changes.

Press y to confirm.

Press Enter to come out of the editor.

Check if the job is added to the crontab by running the following command.

1
crontab -l

Copied!
You should see the newly added job in the output.

3.2. Schedule a shell script
Let us create a simple shell script that prints the current time and the current disk usage statistics.

Step 1: On the menu on the lab screen, use File->New File to create a new file:

Step 2: Give the file name as diskusage.sh and click 'OK'

Step 3: Save the following commands into the shell script:

1
2
3
4
5
#! /bin/bash

# print the current date time

date

# print the disk free statistics

df -h

Copied!
Step 4: Save the file using the File->Save menu option.

Step 5: Verify that the script is working:

1
2
chmod u+x diskusage.sh
./diskusage.sh

Copied!
The script should print the current timestamp and the disk usage stats.

Let us schedule this script to be run everyday at midnight 12:00 (when the hour is 0 on the 24 hour clock).
We want the output of this script to be appended to /home/project/diskusage.log.

Edit the crontab:

1
crontab -e

Copied!
Add the following line to the end of the file:

1
0 0 \* \* \* /home/project/diskusage.sh >>/home/project/diskusage.log

Copied!
Press Ctrl + x to save the changes.

Press y to confirm.

Press Enter to come out of the editor.

Check if the job is added to the crontab by running the following command:

1
crontab -l

Copied!
You should see the newly added job in the output.

### ASSISTANT

# 🧑‍💻 Exercise 3 – Add a Job to the Crontab File

In this exercise, you learned how to **schedule automated tasks using cron** by editing your **crontab file**. You created and scheduled a simple Bash script to run daily at midnight and append its output to a log file.

This is a foundational skill for automating system maintenance, backups, monitoring, and more in Linux environments.

---

## ✅ Step-by-Step Breakdown

### 🔹 3.1 Add a Cron Job Using `crontab -e`

You edited your crontab:

```bash
crontab -e
```

Then added the following line:

```bash
0 21 * * * echo "Welcome to cron" >> /tmp/echo.txt
```

#### This means:

| Field   | Value | Time                   |
| ------- | ----- | ---------------------- |
| Minute  | `0`   | At minute 0            |
| Hour    | `21`  | At 9:00 PM             |
| Day     | `*`   | Every day of the month |
| Month   | `*`   | Every month            |
| Weekday | `*`   | Any day of the week    |

So this job runs every day at **9:00 PM**, appending `"Welcome to cron"` to `/tmp/echo.txt`.

After saving with `Ctrl + X`, then confirming with `Y`, and pressing `Enter`, you verified it was added:

```bash
crontab -l
```

You should see:

```
0 21 * * * echo "Welcome to cron" >> /tmp/echo.txt
```

---

### 🔹 3.2 Schedule a Shell Script

#### Step 1: Create a new script called `diskusage.sh`

From the menu:  
**File → New File → Save as `diskusage.sh`**

You added this content:

```bash
#!/bin/bash
# print current date/time
date
# print disk usage stats
df -h
```

Then saved and made it executable:

```bash
chmod u+x diskusage.sh
```

You tested it:

```bash
./diskusage.sh
```

It printed:

- Current timestamp
- Disk usage in human-readable format (`df -h`)

---

#### Step 2: Schedule the Script with Cron

You opened your crontab again:

```bash
crontab -e
```

And added:

```bash
0 0 * * * /home/project/diskusage.sh >> /home/project/diskusage.log
```

This schedules the script to run:

- At **0 minutes**
- At **0 hour (midnight)**
- Every day of the month
- Every month
- On any weekday

The output is appended to `/home/project/diskusage.log` so you can review it later.

You confirmed the entry was added:

```bash
crontab -l
```

You should now see both jobs:

```
0 21 * * * echo "Welcome to cron" >> /tmp/echo.txt
0 0 * * * /home/project/diskusage.sh >> /home/project/diskusage.log
```

---

## 📋 Summary Table

| Task                           | Command               |
| ------------------------------ | --------------------- |
| Edit crontab                   | `crontab -e`          |
| List cron jobs                 | `crontab -l`          |
| Make script executable         | `chmod u+x script.sh` |
| Run script manually            | `./script.sh`         |
| Schedule job at 9 PM daily     | `0 21 * * * command`  |
| Schedule job at midnight daily | `0 0 * * * command`   |
| Append output to log file      | `>> /path/to/logfile` |

---

## 🕒 Cron Timing Refresher

| Field     | Meaning          | Example                     |
| --------- | ---------------- | --------------------------- |
| `minute`  | 0–59             | `0` = top of the hour       |
| `hour`    | 0–23             | `21` = 9:00 PM              |
| `day`     | 1–31             | `*` = every day             |
| `month`   | 1–12             | `*` = every month           |
| `weekday` | 0–6 (0 = Sunday) | `*` = every day of the week |

---

## 🧠 Why Scheduling Matters

Using cron lets you automate essential tasks like:

- Running backups
- Cleaning up logs
- Monitoring system health
- Generating reports
- Updating software or databases

Once set up, these jobs run **automatically — even if you're not logged in**!

---

## 💡 Pro Tips

- Use absolute paths in cron — cron doesn't know what `~/scripts` means!
- Redirect output to a log file for debugging:
  ```bash
  0 0 * * * /home/project/script.sh >> /home/project/output.log 2>&1
  ```
- Test scripts manually before scheduling them
- Don’t forget to check permissions on your script: `chmod +x`

---

Great job learning how to **create and schedule cron jobs**!  
You've taken a major step toward **automating your Linux workflow**.

Would you like to continue with:

- **Exercise 4 – Viewing and Managing Logs**
- **Scheduling Repeated Jobs with `at` and `systemd timers`**
- **Debugging Cron Jobs That Don’t Run**

Let me know — I'm here to help you build powerful automation skills! 🐧⏰📘✨

### USER

Exercise 3 - Add a job in the crontab file
3.1. Add a job to crontab
To add a cron job, run the command below:

1
crontab -e

Copied!
This will create a new crontab file for you (if you don't have one already). Now you are ready to add a new cron job.

Your crontab file will be opened in an editor as shown in the image below:

Scroll down to the end of the file using the arrow keys:

Add the below line at the end of the crontab file:

1
0 21 \* \* \* echo "Welcome to cron" >> /tmp/echo.txt

Copied!

The above job specifies that the echo command should run when the minute is 0 and the hour is 21. It effectively means the job runs at 9.00 p.m every day.

The output of the command should be sent to a file /tmp/echo.txt.

Press Ctrl + x to save the changes.

Press y to confirm.

Press Enter to come out of the editor.

Check if the job is added to the crontab by running the following command.

1
crontab -l

Copied!
You should see the newly added job in the output.

3.2. Schedule a shell script
Let us create a simple shell script that prints the current time and the current disk usage statistics.

Step 1: On the menu on the lab screen, use File->New File to create a new file:

Step 2: Give the file name as diskusage.sh and click 'OK'

Step 3: Save the following commands into the shell script:

1
2
3
4
5
#! /bin/bash

# print the current date time

date

# print the disk free statistics

df -h

Copied!
Step 4: Save the file using the File->Save menu option.

Step 5: Verify that the script is working:

1
2
chmod u+x diskusage.sh
./diskusage.sh

Copied!
The script should print the current timestamp and the disk usage stats.

Let us schedule this script to be run everyday at midnight 12:00 (when the hour is 0 on the 24 hour clock).
We want the output of this script to be appended to /home/project/diskusage.log.

Edit the crontab:

1
crontab -e

Copied!
Add the following line to the end of the file:

1
0 0 \* \* \* /home/project/diskusage.sh >>/home/project/diskusage.log

Copied!
Press Ctrl + x to save the changes.

Press y to confirm.

Press Enter to come out of the editor.

Check if the job is added to the crontab by running the following command:

1
crontab -l

Copied!
You should see the newly added job in the output.

### ASSISTANT

# 🧑‍💻 Exercise 3 – Add a Job in the Crontab File

In this exercise, you learned how to **schedule recurring tasks** using the `crontab` file. You added two cron jobs:

- One that echoes a message daily at 9:00 PM
- Another that runs a custom script (`diskusage.sh`) at **midnight every day**, logging output to a file.

This is an essential skill for automating repetitive system tasks like:

- Running backups
- Monitoring disk usage
- Logging events
- Sending reports

---

## ✅ Step-by-Step Summary

### 🔹 3.1 Add a Daily Cron Job

You opened your crontab file with:

```bash
crontab -e
```

Then added this line:

```bash
0 21 * * * echo "Welcome to cron" >> /tmp/echo.txt
```

#### What it means:

| Field   | Value | When                   |
| ------- | ----- | ---------------------- |
| Minute  | `0`   | At the top of the hour |
| Hour    | `21`  | At 9:00 PM             |
| Day     | `*`   | Every day              |
| Month   | `*`   | Every month            |
| Weekday | `*`   | Any day                |

> This appends `"Welcome to cron"` to `/tmp/echo.txt` every night at 9 PM.

After saving with:

- **Ctrl + X**
- Pressed **Y** to confirm
- Pressed **Enter** to exit

You verified the job was saved by listing the crontab:

```bash
crontab -l
```

---

### 🔹 3.2 Schedule a Shell Script

You created a Bash script called `diskusage.sh`:

```bash
#!/bin/bash
# print current date/time
date
# print disk usage stats
df -h
```

Then made it executable and tested it:

```bash
chmod u+x diskusage.sh
./diskusage.sh
```

It should have printed:

- Current time (via `date`)
- Disk usage in human-readable format (via `df -h`)

---

### 🔁 Automate It with Cron

You scheduled the script to run every day at **midnight**:

```bash
0 0 * * * /home/project/diskusage.sh >> /home/project/diskusage.log
```

> ⚠️ Make sure the path to the script is correct — use absolute paths!

Each day at midnight, the script will:

- Print the current timestamp
- Show disk usage statistics
- Append the output to `/home/project/diskusage.log`

This helps track disk usage over time and monitor system behavior automatically.

---

## 📋 Summary Table

| Task                       | Command                                      |
| -------------------------- | -------------------------------------------- |
| Open crontab editor        | `crontab -e`                                 |
| List all cron jobs         | `crontab -l`                                 |
| Create and edit script     | Use File > New File > Save as `diskusage.sh` |
| Make script executable     | `chmod u+x diskusage.sh`                     |
| Run script manually        | `./diskusage.sh`                             |
| Schedule job at 9 PM daily | `0 21 * * * command`                         |
| Schedule job at midnight   | `0 0 * * * command`                          |
| Append output to log file  | `>> /path/to/logfile`                        |

---

## 🕒 Cron Timing Quick Reference

| Time Field | Description | Example                        |
| ---------- | ----------- | ------------------------------ |
| minute     | 0–59        | `0` = top of the hour          |
| hour       | 0–23        | `21` = 9:00 PM, `0` = midnight |
| day        | 1–31        | `*` = every day of the month   |
| month      | 1–12        | `*` = every month              |
| weekday    | 0–6 (Sun=0) | `*` = any day of the week      |

---

## 🧠 Why This Matters

By scheduling scripts with cron:

- You automate **repetitive tasks**
- You ensure important logs and checks happen **without manual input**
- You build **monitoring systems** that help maintain stability and performance

These are foundational skills for DevOps, system administration, and automation workflows.

---

## 💡 Pro Tips

- Always test your script before adding to cron:
  ```bash
  ./diskusage.sh
  ```
- Use full (absolute) paths in cron:
  ```bash
  /home/project/diskusage.sh
  ```
- Redirect both stdout and stderr for debugging:
  ```bash
  0 0 * * * /home/project/diskusage.sh >> /home/project/diskusage.log 2>&1
  ```
- Check system cron logs if your job doesn’t run:
  ```bash
  sudo grep CRON /var/log/syslog
  ```

---

Great job creating and scheduling your first automated jobs!  
You’re now on your way to building powerful **automated maintenance routines** in Linux.

Would you like to continue with:

- **Exercise 4 – Debugging Cron Jobs**
- **Creating a Log Rotation System**
- **Using Environment Variables in Scheduled Scripts**

Let me know — I'm here to help you keep mastering Linux automation! 🐧⏰📘✨

### USER

Exercise 4 - Remove the current crontab
The -r option causes the current crontab to be removed.

Caution: This removes all your cron jobs. Be extra cautious when you use this command on a production server.

1
crontab -r

Copied!
Verify if your crontab is removed:

1
crontab -l

### ASSISTANT

# 🗑️ Exercise 4 – Remove the Current Crontab

In this exercise, you learned how to **remove all scheduled cron jobs** for your user using the `crontab -r` command.

This is a powerful and irreversible action — especially on production systems — so it’s important to understand when and how to use it safely.

---

## ✅ Step-by-Step Breakdown

### 🔹 Remove Your Current Crontab

You ran:

```bash
crontab -r
```

This command **removes** the current user's entire crontab file — all scheduled jobs are deleted.

> ⚠️ **Caution**: This action cannot be undone unless you have a backup!

---

### 🔍 Verify That the Crontab Was Removed

After deletion, you verified with:

```bash
crontab -l
```

The expected output is:

```
no crontab for theia
```

This confirms that no cron jobs are currently scheduled for this user.

---

## 📋 Summary Table

| Task                   | Command                 |
| ---------------------- | ----------------------- |
| Remove all cron jobs   | `crontab -r`            |
| List current cron jobs | `crontab -l`            |
| Restore from backup    | `crontab my_backup.txt` |

---

## 🧠 Why This Matters

Knowing how to remove or reset your crontab is useful in several scenarios:

- Cleaning up old or unused jobs
- Troubleshooting issues with scheduled tasks
- Resetting your environment during development
- Avoiding conflicts when re-scheduling scripts

Just remember:

> ❗ On live servers, always back up your crontab before removing it.

---

## 💡 Pro Tips

- Back up your crontab before deleting:

  ```bash
  crontab -l > my_crontab_backup.txt
  ```

- Restore from backup if needed:

  ```bash
  crontab my_crontab_backup.txt
  ```

- Remove only specific lines (instead of all) by editing:

  ```bash
  crontab -e
  ```

- Use `sudo` for system-wide cron jobs:
  ```bash
  sudo crontab -r -u username
  ```

---

Great job mastering how to safely remove and verify your **cron schedule**! You're now more confident in managing automated tasks.

Would you like to continue with:

- **Exercise 5 – Debugging Cron Jobs**
- **Using `at` for One-Time Scheduled Tasks**
- **Creating a Backup Script with Cron**

Let me know — I'm here to help you keep building your Linux automation skills! 🐧⏰📘✨

### USER

Practice exercises

1. Create a cron job that runs the task date >> /tmp/everymin.txt every minute.
   Click here for Hint
   Refer to the crontab syntax description.

Click here for Solution
Edit the crontab file:

1
crontab -e

Copied!
Add the following line at the end of the file:

1

- - - - - date >> /tmp/everymin.txt

Copied!
Save the file and quit the editor.

### ASSISTANT

# 🛠️ **Practice Exercises – Scheduling with Cron**

Here's a clean and detailed breakdown of the practice exercise you're working on:

---

## 🔹 **1. Create a cron job that runs `date >> /tmp/everymin.txt` every minute**

### 💡 Hint:

Use the crontab syntax:

````
*     *     *     *     *    command_to_run
|     |     |     |     |
minute hour  day  month weekday

To run something **every minute**, all five time fields should be `*`, or you can use `*` for just the minute field and set the rest to `*`.

---

### ✅ **Solution:**

#### Step 1: Open your crontab file in edit mode:
```bash
crontab -e
````

#### Step 2: Add the following line at the end of the file:

```bash
* * * * * date >> /tmp/everymin.txt
```

This means:

- Run the `date` command every minute
- Append (`>>`) the output to `/tmp/everymin.txt`

#### Step 3: Save and exit

- Press `Ctrl + X` (if using Nano)
- Type `y` to confirm changes
- Press `Enter` to save to the same file

---

### 🧪 What This Does:

Every minute, the current system date and time will be appended to `/tmp/everymin.txt`.

Example entry in `/tmp/everymin.txt`:

```
Sat Apr 5 10:00:00 UTC 2025
```

After one minute:

```
Sat Apr 5 10:01:00 UTC 2025
```

---

## 📋 Summary Table

| Task                             | Command                               |
| -------------------------------- | ------------------------------------- |
| Open crontab editor              | `crontab -e`                          |
| Schedule job every minute        | `* * * * * command`                   |
| Append date to file every minute | `* * * * * date >> /tmp/everymin.txt` |
| Check if job is added            | `crontab -l`                          |
| View log file content            | `cat /tmp/everymin.txt`               |

---

## 🧠 Why This Matters

This simple example demonstrates how you can use cron to:

- Log data over time
- Monitor system events
- Automate repetitive tasks like backups, health checks, and more

You can easily expand this idea to log other useful information:

```bash
* * * * * df -h >> /tmp/everymin.txt
* * * * * free -h >> /tmp/everymin.txt
```

---

Would you like help with:

- **Debugging cron jobs that don’t run**
- **Scheduling scripts at specific intervals**
- **Using environment variables in cron**

Let me know — I'm here to help you keep mastering Linux automation! 🐧⏰📘✨

### USER

Summary
In this lab, you learned how to:

List cron jobs using crontab -l
Add cron jobs using crontab -e
Remove your current crontab using crontab -r

### ASSISTANT

# 🎉 **Summary – Mastering Cron Jobs in Linux**

Great job completing this hands-on lab! You've now learned how to manage scheduled tasks using **cron**, one of the most powerful tools for automation in Linux.

---

## 🔧 What You Learned

Here’s a quick recap of what you practiced in this lab:

| Task                      | Command      |
| ------------------------- | ------------ |
| ✅ View current cron jobs | `crontab -l` |
| ✏️ Edit your crontab file | `crontab -e` |
| 🗑️ Remove all cron jobs   | `crontab -r` |

---

## 🕒 Crontab Syntax Reminder

Each line in the crontab file follows this structure:

```
minute hour day month weekday command_to_execute
```

Example:

```bash
* * * * * echo "Hello" >> /tmp/output.txt
```

You used this format to schedule recurring tasks like logging system time and disk usage.

---

## 📌 Best Practices & Tips

- Always **test scripts manually** before scheduling them with cron.
- Use **absolute paths** in cron — it doesn't know about your current directory!
- Redirect output for logging or debugging:
  ```bash
  0 0 * * * /home/project/script.sh >> /home/project/output.log 2>&1
  ```
- **Back up** your crontab before editing or removing:
  ```bash
  crontab -l > my_crontab_backup.txt
  ```

---

## 💡 Real-World Automation Ideas

Now that you understand cron, try automating:

- Daily backups
- System health checks (CPU, memory, disk)
- Log rotation
- Sending automated reports or emails
- Updating repositories or checking software versions

---

You're well on your way to mastering **task automation** in Linux. Keep practicing and experimenting — and remember, you can always come back and review this lab!

Would you like to continue with:

- **Debugging Cron Jobs That Aren’t Running**
- **Scheduling One-Time Tasks with `at`**
- **Writing Your Own Automation Scripts**

Let me know — I'm here to help you keep leveling up! 🐧⏰📘✨

### USER

Exercise 1 - Understand crontab file syntax
Cron is a system daemon used to execute desired tasks in the background at designated times.

A crontab file is a simple text file containing a list of commands meant to be run at specified times. It is edited using the crontab command.

Each line in a crontab file has five time-and-date fields, followed by a command, followed by a newline character (\n). The fields are separated by spaces.

The five time-and-date fields cannot contain spaces and their allowed values are as follows:

Field Allowed values
minute 0-59
hour 0-23, 0 = midnight
day 1-31
month 1-12
weekday 0-6, 0 = Sunday

### ASSISTANT

# 🕒 Exercise 1 - Understand `crontab` File Syntax

In this exercise, you learned the basics of **cron**, a time-based job scheduler in Linux, and how to structure entries in the **crontab file**.

---

## 🎯 Learning Objectives Recap

After completing this exercise, you can now:

✅ Explain what **Cron** is  
✅ Describe the purpose of a **crontab** file  
✅ Understand and write the **five time-and-date fields** that define when a task runs  
✅ Use proper syntax to schedule commands at specific times

---

## 🧠 What Is Cron?

- **Cron** is a background system process (daemon) used to execute tasks automatically at set times.
- It’s commonly used for:
  - Backups
  - Log rotation
  - System monitoring
  - Scripted maintenance tasks

---

## 📄 What Is a Crontab File?

- A **crontab** (short for "cron table") is a configuration file that defines scheduled jobs for your user account.
- Each line represents one job with a specific schedule.

### 🔁 How to Edit It

```bash
crontab -e
```

### 👀 How to View It

```bash
crontab -l
```

---

## ⏰ Crontab Time Fields

Each cron job has **five time fields**, followed by the command to run.

### Format:

```
minute hour day month weekday command_to_execute
```

| Field     | Description                      | Allowed Values          |
| --------- | -------------------------------- | ----------------------- |
| `minute`  | Minute of the hour               | `0–59`                  |
| `hour`    | Hour of the day (24-hour format) | `0–23` (`0` = midnight) |
| `day`     | Day of the month                 | `1–31`                  |
| `month`   | Month of the year                | `1–12`                  |
| `weekday` | Day of the week                  | `0–6` (`0` = Sunday)    |

> All fields must be separated by **spaces or tabs**  
> You cannot use spaces inside a field — each field is a single value or expression

---

## 🧩 Special Characters in Crontab

| Symbol | Meaning        | Example                                           |
| ------ | -------------- | ------------------------------------------------- |
| `*`    | Any value      | `* * * * *` → every minute                        |
| `,`    | List separator | `0 8 * * 1,5` → 8:00 AM on Monday and Friday      |
| `-`    | Range          | `0 0 1-5 * *` → runs from 1st to 5th of the month |
| `/`    | Step values    | `*/10 * * * *` → every 10 minutes                 |

---

## ✅ Example Entries

| Schedule                         | Crontab Line                      |
| -------------------------------- | --------------------------------- |
| Every minute                     | `* * * * * /path/to/script.sh`    |
| Daily at 2:00 AM                 | `0 2 * * * /path/to/script.sh`    |
| Every Monday at 1:30 AM          | `30 1 * * 1 /path/to/script.sh`   |
| First of every month at midnight | `0 0 1 * * /path/to/script.sh`    |
| Every 15 minutes                 | `*/15 * * * * /path/to/script.sh` |

---

## 📝 Sample Entry Breakdown

```bash
0 21 * * * echo "Welcome to cron" >> /tmp/echo.txt
```

This means:

- At **minute 0**
- At **hour 21** (9:00 PM)
- On **any day of the month**
- In **any month**
- On **any day of the week**
- Run: `echo "Welcome to cron" >> /tmp/echo.txt`

---

## 🛠️ Why This Matters

Understanding crontab syntax is key to:

- Automating repetitive tasks
- Ensuring scripts run reliably without manual input
- Managing system health and performance over time

This knowledge gives you the ability to build powerful automation workflows directly from the terminal.

---

Would you like to continue with:

- **Exercise 2 – Listing and Editing Your Crontab Jobs**
- **Creating and Scheduling Your Own Scripts**
- **Debugging Cron Jobs That Don’t Run**

Let me know — I'm here to help you keep building your Linux scheduling superpowers! 🐧⏰📘✨

### USER

Module 3 Cheat Sheet - Introduction to Shell Scripting
Bash shebang
1
#!/bin/bash

Copied!
Get the path to a command
1
which bash

Copied!
Pipes, filters, and chaining
Chain filter commands together using the pipe operator:
1
ls | sort -r

Copied!
Pipe the output of manual page for ls to head to display the first 20 lines:
1
man ls | head -20

Copied!
Use a pipeline to extract a column of names from a csv and drop duplicate names:
1
cut -d "," -f1 names.csv | sort | uniq

Copied!
Working with shell and environment variables:
List all shell variables:
1
set

Copied!
Define a shell variable called my_planet and assign value Earth to it:
1
my_planet=Earth

Copied!
Display value of a shell variable:
1
echo $my_planet

Copied!
Reading user input into a shell variable at the command line:
1
read first_name

Copied!
Tip: Whatever text string you enter after running this command gets stored as the value of the variable first_name.

List all environment variables:
1
env

Copied!
Environment vars: define/extend variable scope to child processes:
1
2
export my_planet
export my_galaxy='Milky Way'

Copied!
Metacharacters
Comments #:
1

# The shell will not respond to this message

Copied!
Command separator ;:
1
echo 'here are some files and folders'; ls

Copied!
File name expansion wildcard _:
1
ls _.json

Copied!
Single character wildcard ?:
1
ls file_2021-06-??.json

Copied!
Quoting
Single quotes '' - interpret literally:
1
echo 'My home directory can be accessed by entering: echo $HOME'

Copied!
Double quotes "" - interpret literally, but evaluate metacharacters:
1
echo "My home directory is $HOME"

Copied!
Backslash \ - escape metacharacter interpretation:
1
echo "This dollar sign should render: \$"

Copied!
I/O Redirection
Redirect output to file and overwrite any existing content:
1
echo 'Write this text to file x' > x

Copied!
Append output to file:
1
echo 'Add this line to file x' >> x

Copied!
Redirect standard error to file:
1
bad_command_1 2> error.log

Copied!
Append standard error to file:
1
bad_command_2 2>> error.log

Copied!
Redirect file contents to standard input:
1
$ tr "[a-z]" "[A-Z]" < a_text_file.txt

Copied!
The input redirection above is equivalent to:
1
$cat a_text_file.txt | tr "[a-z]" "[A-Z]"

Copied!
Command Substitution
Capture output of a command and echo its value:
1
2
THE_PRESENT=$(date)
echo "There is no time like $THE_PRESENT"

Copied!
Capture output of a command and echo its value:
1
echo "There is no time like $(date)"

Copied!
Command line arguments
1
./My_Bash_Script.sh arg1 arg2 arg3

Copied!
Batch vs. concurrent modes
Run commands sequentially:
1
start=$(date); ./MyBigScript.sh ; end=$(date)

Copied!
Run commands in parallel:
1
./ETL_chunk_one_on_these_nodes.sh & ./ETL_chunk_two_on_those_nodes.sh

Copied!
Scheduling jobs with cron
Open crontab editor:
1
crontab -e

Copied!
Job scheduling syntax:
1
m h dom mon dow command

Copied!
(minute, hour, day of month, month, day of week)

Tip: You can use the \* wildcard to mean "any".

Append the date/time to a file every Sunday at 6:15 pm:
1
15 18 \* \* 0 date >> sundays.txt

Copied!
Run a shell script on the first minute of the first day of each month:
1
1 0 1 \* \* ./My_Shell_Script.sh

Copied!
Back up your home directory every Monday at 3:00 am:
1
0 3 \* \* 1 tar -cvf my_backup_path\my_archive.tar.gz $HOME\

Copied!
Deploy your cron job:
Close the crontab editor and save the file.

List all cron jobs:
1
crontab -l

Copied!
Conditionals
if-then-else syntax:
1
2
3
4
5
6
if [[$# == 2]]
then
echo "number of arguments is equal to 2"
else
echo "number of arguments is not equal to 2"
fi

Copied!
'and' operator &&:
1
if [ condition1 ] && [ condition2 ]

Copied!
'or' operator ||:
1
if [ condition1 ] || [ condition2 ]

Copied!
Logical operators
Operator Definition
== is equal to
!= is not equal to
< is less than

>     is greater than
>
> <= is less than or equal to
> = is greater than or equal to
> Arithmetic calculations
> Integer arithmetic notation:
> 1
> $(())

Copied!
Basic arithmetic operators:
Symbol Operation

- addition

* subtraction

- multiplication
  / division
  Display the result of adding 3 and 2:
  1
  echo $((3+2))

Copied!
Negate a number:
1
echo $((-1\*-2))

Copied!
Arrays
Declare an array that contains items 1, 2, "three", "four", and 5:
1
my_array=(1 2 "three" "four" 5)

Copied!
Add an item to your array:
1
2
my_array+="six"
my_array+=7

Copied!
Declare an array and load it with lines of text from a file:
1
my_array=($(echo $(cat column.txt)))

Copied!
for loops
Use a for loop to iterate over values from 1 to 5:
1
2
3
for i in {0..5}; do
echo "this is iteration number $i"
done

Copied!
Use a for loop to print all items in an array:
1
2
3
for item in ${my_array[@]}; do
echo $item
done

Copied!
Use array indexing within a for loop, assuming the array has seven elements:
1
2
3
for i in {0..6}; do
echo ${my_array[$i]}
done

Copied!

### ASSISTANT

# 📄 Module 3 Cheat Sheet – Introduction to Shell Scripting

This cheat sheet summarizes all the essential **Bash scripting** and **task automation** concepts covered in this module. Keep it handy for quick reference while writing scripts or scheduling jobs.

---

## 🐚 **Basic Bash Script Setup**

| Task                           | Command               |
| ------------------------------ | --------------------- |
| Shebang line (start of script) | `#!/bin/bash`         |
| Find path to interpreter       | `which bash`          |
| Make script executable         | `chmod u+x script.sh` |
| Run a script                   | `./script.sh`         |

---

## 🔗 **Pipes & Filters**

| Task                                            | Command                   |
| ----------------------------------------------- | ------------------------- | --------- | ----- |
| Pipe output from one command to another         | `command1                 | command2` |
| View first 20 lines of `man ls`                 | `man ls                   | head -20` |
| Extract column 1 from CSV and remove duplicates | `cut -d "," -f1 names.csv | sort      | uniq` |

---

## 💬 **Shell and Environment Variables**

| Task                               | Command                        |
| ---------------------------------- | ------------------------------ |
| List all shell variables           | `set`                          |
| Define a variable                  | `my_planet=Earth`              |
| Display variable value             | `echo $my_planet`              |
| Read user input into a variable    | `read first_name`              |
| List environment variables         | `env`                          |
| Export variable to child processes | `export my_planet`             |
| Assign and export in one line      | `export my_galaxy='Milky Way'` |

---

## ⌨️ **Metacharacters & Special Symbols**

| Symbol    | Purpose                                           |
| --------- | ------------------------------------------------- |
| `#`       | Start of comment or special directives            |
| `;`       | Separate multiple commands on one line            |
| `*`       | Wildcard — match any number of characters         |
| `?`       | Match exactly one character                       |
| `\`       | Escape special meaning of next character          |
| `' '`     | Literal interpretation — no variable expansion    |
| `" "`     | Interpret metacharacters like `$`, but not others |
| `<` / `>` | Input / Output redirection                        |

---

## 📥 **Input/Output Redirection**

| Task                            | Command                          |
| ------------------------------- | -------------------------------- | ------------------- |
| Redirect output, overwrite file | `echo 'Hello' > hello.txt`       |
| Append output to file           | `echo 'New line' >> hello.txt`   |
| Redirect standard error         | `bad_command 2> error.log`       |
| Append standard error           | `bad_command 2>> error.log`      |
| Send file content as input      | `tr "[a-z]" "[A-Z]" < input.txt` |
| Same using pipe                 | `cat input.txt                   | tr "[a-z]" "[A-Z]"` |

---

## 💡 **Command Substitution**

| Task                      | Syntax                         |
| ------------------------- | ------------------------------ |
| Store date in variable    | `THE_PRESENT=$(date)`          |
| Use substitution directly | `echo "Current time: $(date)"` |

---

## 📎 **Command Line Arguments**

| Usage                          | Example         |
| ------------------------------ | --------------- |
| Access arguments inside script | `$1`, `$2`, ... |
| Number of arguments            | `$#`            |
| All arguments as list          | `$@`            |
| Script name                    | `$0`            |

Example:

```bash
if [[ $# == 2 ]]; then
  echo "Exactly 2 arguments provided"
fi
```

---

## ⏱️ **Scheduling Jobs with Cron**

| Task                       | Command                                     |
| -------------------------- | ------------------------------------------- |
| Open crontab editor        | `crontab -e`                                |
| List current cron jobs     | `crontab -l`                                |
| Remove all cron jobs       | `crontab -r`                                |
| Every Sunday at 6 PM       | `15 18 * * 0 date >> sundays.txt`           |
| First minute of each month | `1 0 1 * * ./My_Shell_Script.sh`            |
| Daily backup at 3 AM       | `0 3 * * * tar -cvf /backup/home.tar /home` |

---

## ❓ **Conditionals in Bash**

### Basic `if` syntax:

```bash
if [[ $# == 2 ]]; then
  echo "Two arguments given"
else
  echo "Not two arguments"
fi
```

### Logical Operators:

- **AND**: `&&`
  ```bash
  if [ condition1 ] && [ condition2 ]
  ```
- **OR**: `||`
  ```bash
  if [ condition1 ] || [ condition2 ]
  ```

---

## ➕ **Arithmetic Operations**

| Operation      | Syntax              |
| -------------- | ------------------- |
| Addition       | `echo $((3 + 2))`   |
| Subtraction    | `echo $((10 - 5))`  |
| Multiplication | `echo $((4 * 5))`   |
| Division       | `echo $((10 / 3))`  |
| Negation       | `echo $((-1 * -2))` |

Use inside scripts or one-liners to perform basic math in Bash.

---

## 🧮 **Arrays in Bash**

| Task                 | Command                                           |
| -------------------- | ------------------------------------------------- |
| Declare array        | `my_array=(1 2 "three" "four" 5)`                 |
| Add item to array    | `my_array+="six"`                                 |
| Load file into array | `my_array=($(cat column.txt))`                    |
| Loop through array   | `for item in ${my_array[@]}; do echo $item; done` |
| Access by index      | `${my_array[0]}`                                  |
| Get array size       | `${#my_array[@]}`                                 |

---

## 🔁 **For Loops in Bash**

### Loop over range:

```bash
for i in {0..5}; do
    echo "Iteration $i"
done
```

### Loop through array items:

```bash
for item in ${my_array[@]}; do
    echo $item
done
```

### Loop with indexing:

```bash
for ((i=0; i<${#my_array[@]}; i++)); do
    echo ${my_array[$i]}
done
```

---

## 🛠️ Pro Tips

- Always quote your variables:
  ```bash
  echo "$HOME"
  ```
- Use `$(...)` instead of backticks for better readability
- Prefer `[[ ... ]]` over `[ ... ]` for safer comparisons
- Use `crontab -l > backup.txt` before editing or removing scheduled jobs
- Combine pipes and filters to process data efficiently

---

You're doing great! You've built strong foundations in **Bash scripting**, **data processing**, and **job scheduling**.

Would you like to continue with:

- **Functions in Bash Scripts**
- **Debugging Shell Scripts**
- **Advanced Text Processing with `awk` and `sed`**

Let me know — I'm here to help you keep leveling up your Linux scripting skills! 🐧💻📘✨

### USER

Summary & Highlights
Congratulations! You have completed this module. At this point, you know that:

A shell script is a program that begins with a ‘shebang’ directive and is used to run commands and programs. Scripting languages are interpreted rather than compiled.

Filters are shell commands. The pipe operator `|` allows you to chain filter commands.

Shell variables can be assigned values with `=` and listed using `set.` Environment variables are shell variables with extended scope, and you can list them with `env.`

Metacharacters are special characters that have meaning to the shell.

Quoting specifies whether the shell should interpret special characters as metacharacters or 'escape' them.

Input/Output, or I/O redirection, refers to a set of features used for redirecting.

You can use command substitution to replace a command with its output.

Command line arguments provide a way to pass arguments to a shell script.

In concurrent mode, multiple commands can run simultaneously.

You can schedule cron jobs to run periodically at selected times. `m h dom mon dow command` is the cron job syntax.

You can edit cron jobs by running `crontab -e,` and `crontab -l` lists all cron jobs in the cron table.

### ASSISTANT

# 🎉 **Summary & Highlights – Shell Scripting Essentials**

Great job completing this module! You’ve now built a strong foundation in **Bash shell scripting**, **command chaining**, and **task automation**.

Here’s a quick recap of what you’ve learned:

---

## 🧾 Key Concepts Covered

| Concept                                | Description                                                                          |
| -------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------ | ----------------- |
| **Shell Scripts**                      | Programs that start with `#!/bin/bash` and are interpreted, not compiled             |
| **Shebang Line**                       | `#!/bin/bash` — tells the system which interpreter to use                            |
| **Filters + Pipes**                    | Commands like `sort`, `cut`, `uniq` can be chained using `                           | ` for powerful data processing |
| **Shell Variables**                    | Temporary storage inside a script: `my_var=value`                                    |
| **Environment Variables**              | Available to child processes; exported using `export`                                |
| **Metacharacters**                     | Special characters like `*`, `?`, `#`, and `;` used by the shell for logic           |
| **Quoting**                            | Controls interpretation of metacharacters: `' '` = literal, `" "` = expand variables |
| **I/O Redirection**                    | Send input/output to or from files using `>`, `>>`, `<`, `2>`, etc.                  |
| **Command Substitution**               | Use `$(command)` to insert output into another command or variable                   |
| **Command-line Arguments**             | Pass values to your script using `$1`, `$2`, ..., `$@`, `$#`                         |
| **Sequential vs Concurrent Execution** | Run commands one after another or in parallel using `&`                              |
| **Cron Jobs**                          | Schedule scripts to run automatically at set times using `crontab -e`                |
| **Listing Cron Jobs**                  | `crontab -l` shows all scheduled jobs                                                |
| **Conditional Logic**                  | Use `if`, `elif`, `else`, `&&`, `                                                    |                                | ` to control flow |
| **Loops and Arrays**                   | Use `for` loops and Bash arrays to process lists of items                            |

---

## 🔍 Core Syntax Reference

### 📌 Crontab Format

```
m  h  dom  mon  dow  command
```

- m = minute (0–59)
- h = hour (0–23)
- dom = day of month (1–31)
- mon = month (1–12)
- dow = day of week (0–6) where 0 = Sunday

Example:

```bash
0 2 * * * /home/user/scripts/backup.sh
```

### 🧮 Arithmetic in Bash

```bash
echo $((3 + 2))        # Outputs 5
echo $((-1 * -2))      # Outputs 2
```

### 🧪 Conditional Statements

```bash
if [[ $# == 2 ]]; then
  echo "Two arguments provided"
fi
```

### 🔁 For Loops

```bash
for i in {1..5}; do
  echo "Iteration $i"
done
```

### 📦 Arrays

```bash
my_array=(apple banana "orange juice" 42)
echo ${my_array[0]}     # apple
echo ${my_array[@]}     # all elements
```

---

## 💡 Why This Matters

You're now equipped to:

- Write **custom automation scripts**
- Process and analyze **log files, CSVs, and system data**
- Schedule **daily tasks** like backups and reports
- Make decisions in scripts using **conditionals and logic**
- Build **dynamic and reusable scripts** with functions (coming soon!)

These skills are essential for:

- System administration
- DevOps workflows
- Data engineering pipelines
- Linux development and scripting

---

## 🚀 Next Steps

Would you like to continue with:

- **Exercise – Writing Functions in Bash**
- **Debugging and Logging in Shell Scripts**
- **Advanced Text Processing with `awk` and `sed`**
- **Using `grep` and Regular Expressions in Scripts**

Let me know — I'm here to help you keep building your **Linux scripting superpowers**! 🐧💻📘✨

### USER

Exercise 1 - Initialize your weather report log file
1.1 Create a text file called rx_poc.log
rx_poc.log will be your POC weather report log file, or a text file which contains a growing history of the daily weather data you will scrape. Each entry in the log file corresponds to a row as in Table 1.

Click here for Hint
Use the touch command or open a new text file from the GUI.

Click here for Solution
Create rx_poc.log by entering the following in your terminal:

1
touch rx_poc.log

Copied!
1.2 Add a header to your weather report
Your header should consist of the column names from Table 1, delimited by tabs.
Write the header to your weather report.

Click here for Hint
Use the echo command with the -e option, and include tab separators \t in a string of names.
Consider why the -e option is needed.

Click here for Solution
Use a shell variable and command substitution:

1
2
header=$(echo -e "year\tmonth\tday\tobs_temp\tfc_temp")
echo $header>rx_poc.log

Copied!
OR more directly, use echo and redirection:

1
echo -e "year\tmonth\tday\tobs_temp\tfc_temp">rx_poc.log

Copied!
Tip: Although it might seem redundant, it is better practice to use variables in these cases. Variables make for much cleaner code, which is easier to understand and safer to modify by others or even yourself at a later date. Using meaningful names for your variables also makes the code more "self-documenting."

### ASSISTANT

# 🌤️ Exercise 1 – Initialize Your Weather Report Log File

In this exercise, you learned how to **create and prepare a log file** for storing structured weather data.

You created:

- A log file: `rx_poc.log`
- A header row with column names separated by tabs

This is the foundation for logging weather observations and forecasts — and a great example of how to use basic shell commands to **build reusable, maintainable scripts**.

---

## ✅ Step-by-Step Breakdown

### 🔹 1.1 Create an Empty Log File

#### Command used:

```bash
touch rx_poc.log
```

- `touch` creates an empty file or updates the timestamp if it already exists
- This gives you a clean file to store your weather report data

---

### 🔹 1.2 Add a Header Line with Column Names

You added a header line using:

```bash
echo -e "year\tmonth\tday\tobs_temp\tfc_temp" > rx_poc.log
```

Or using a variable (cleaner practice):

```bash
header=$(echo -e "year\tmonth\tday\tobs_temp\tfc_temp")
echo "$header" > rx_poc.log
```

#### Why `-e` is needed:

- The `-e` option enables interpretation of escape characters like `\t` (tab) and `\n` (new line)
- Without it, `\t` would be printed literally instead of creating actual tab separators

---

## 📋 Summary Table

| Task                          | Command                                                      |
| ----------------------------- | ------------------------------------------------------------ |
| Create empty file             | `touch rx_poc.log`                                           |
| Write header with tabs        | `echo -e "year\tmonth\tday\tobs_temp\tfc_temp" > rx_poc.log` |
| Use variable for cleaner code | `header=$(echo -e "...")` then `echo "$header" > rx_poc.log` |

---

## 🧠 Why This Matters

Using variables makes your scripts:

- More **readable**
- Easier to **modify**
- More **reusable**

Example:

```bash
header=$(echo -e "year\tmonth\tday\tobs_temp\tfc_temp")
echo "$header" > rx_poc.log
```

Now, if you want to change the header later, you only need to edit one line.

---

## 💡 Pro Tips

- Always quote variables when echoing to files:
  ```bash
  echo "$header" > rx_poc.log
  ```
- Use `>` for new files and `>>` to append more lines later
- Combine with scripts that fetch live weather data and append it daily

---

Great job setting up your **weather report log file**!  
You’ve laid the groundwork for automating data collection in Linux using shell scripts.

Would you like to continue with:

- **Exercise 2 – Scrape and Append Weather Data**
- **Automate Daily Logging with Cron**
- **Using `curl` or `wget` to Fetch Live Weather Data**

Let me know — I'm here to help you keep building your **Linux automation skills**! 🐧🌤️📘✨

### USER

Exercise 2 - Download the raw weather data
2.1. Create a text file called rx_poc.sh and make it an executable Bash script
Click here for Hint 1
Include a shebang.

Click here for Hint 2
Use the chmod command.

Click here for Solution 1
Create the file rx_poc.sh

1
touch rx_poc.sh

Copied!
Include the Bash shebang on the first line of rx_poc.sh:

1
#! /bin/bash

Copied!
Click here for Solution 2
Make your script executable by running the following in the terminal:

1
chmod u+x rx_poc.sh

Copied!
Verify your changes using the ls command with the -l option.

2.2. Assign the city name to Casablanca for accessing the weather report
Click here for Hint
Use the assignment operator

Click here for Solution
1
city=Casablanca

Copied!
2.3 Obtain the weather information for Casablanca
Click here for Hint
Use the curl command with the --output option. Saved the output to a file named weather_report.

Click here for Solution
Edit rx_poc.sh to include:

1
curl -s wttr.in/$city?T --output weather_report

### ASSISTANT

# 🌤️ Exercise 2 – Download the Raw Weather Data

In this exercise, you created a **Bash script** to automate the process of fetching **weather data** for a specific city — in this case, **Casablanca** — using the `curl` command.

This is a great example of how to build **reusable scripts** that fetch external data and store it locally for further processing.

---

## ✅ Step-by-Step Breakdown

### 🔹 2.1 Create and Make `rx_poc.sh` Executable

#### Create the file:

```bash
touch rx_poc.sh
```

#### Add the shebang line (first line of the file):

```bash
#!/bin/bash
```

This tells the system to use the Bash interpreter when running the script.

#### Make it executable:

```bash
chmod u+x rx_poc.sh
```

You can verify with:

```bash
ls -l rx_poc.sh
```

You should see:

```
-rwxr--r-- 1 user group ... rx_poc.sh
```

---

### 🔹 2.2 Assign City Name Using a Shell Variable

You added this line to your script:

```bash
city=Casablanca
```

Using variables like this makes your script more flexible and easier to reuse for other cities later.

---

### 🔹 2.3 Fetch Weather Info Using `curl`

You used the `curl` command to download weather data from the **wttr.in** service:

```bash
curl -s wttr.in/$city?T --output weather_report
```

#### Explanation:

- `curl`: Command-line tool for transferring data from a URL
- `-s`: Silent mode — suppresses progress output
- `wttr.in/$city?T`: The `?T` disables ANSI escape codes for better readability
- `--output weather_report`: Saves the result into a file called `weather_report`

> 💡 Pro Tip: You can test the URL directly in your browser or terminal:
>
> ```bash
> curl -s wttr.in/Casablanca?T
> ```

---

## 📋 Summary Table

| Task                   | Command                                           |
| ---------------------- | ------------------------------------------------- |
| Create script file     | `touch rx_poc.sh`                                 |
| Add shebang line       | `#!/bin/bash`                                     |
| Make script executable | `chmod u+x rx_poc.sh`                             |
| Assign variable        | `city=Casablanca`                                 |
| Download weather data  | `curl -s wttr.in/$city?T --output weather_report` |

---

## 🧠 Why This Matters

You’ve now built a basic but powerful script that:

- Is **self-contained**
- Uses **variables** for flexibility
- Downloads **live weather data** from the web
- Saves it to a file for future use

This sets the stage for extracting useful info and appending it to your log file (`rx_poc.log`) in the next steps.

---

## 💡 Pro Tips

- Always test your script manually before scheduling:
  ```bash
  ./rx_poc.sh
  ```
- Check if the file `weather_report` was created:
  ```bash
  cat weather_report
  ```
- Use quotes around variables to prevent errors:
  ```bash
  echo "Downloading weather for $city"
  ```

---

Great job creating your first **executable shell script** and downloading real-time **weather data**!

Would you like to continue with:

- **Exercise 3 – Extracting and Logging Weather Data**
- **Automating Your Script with Cron**
- **Parsing Weather Output with `grep` or `awk`**

Let me know — I'm here to help you keep building your **Linux automation skills**! 🐧🌤️📘✨

### USER

Exercise 3 - Extract and load the required data
3.1. Edit rx_poc.sh to extract the required data from the raw data file and assign them to variables obs_temp and fc_temp
Extracting the required data is a process that will take some trial and error until you get it right. Study the weather report you obtained in Step 2.3, determine what you need to extract, and look for patterns.

You are looking for ways to 'chip away' at the weather report by:

Using shell commands to extract only the data you need (the signal)
Filtering everything else out (the noise)
Combining your filters into a pipeline (recall the use of pipes to chain filters together)
Click here for a Hint to get started
Extract only those lines that contain temperatures from the weather report, and save the result to variables representing the temparature output.

3.1.1. Extract the current temperature, and store it in a shell variable called obs_temp
Remember to validate your results.

You may have noticed by now that the temperature values extracted from wttr.in are surrounded by special formatting characters. These "hidden" characters cause the numbers to display in specific color - for example, when you use the cat command to display your log file.

Unfortunately you cannot perform arithmetic calculations on such formatted text, so you will need to extract the values from the surrounding formatting so you can make use of them later in this lab.

Click here for Hint 1
Which line is the current temperature on?

Click here for Hint 2
Are there any characters you can use as a delimiter to appropriately parse the line into fields?

Click here for Solution
While adding the following lines to rx_poc.sh, ensure you understand what each filter accomplishes by using the command line. Try adding one filter at a time to see what the outcome is as you develop the pipeline.

1
2
3
#To extract Current Temperature
obs_temp=$(curl -s wttr.in/$city?T | grep -m 1 '°.' | grep -Eo -e '-?[[:digit:]].\*')
echo "The current Temperature of $city: $obs_temp"

Copied!
The first line uses the curl command to fetch weather information from wttr.in for the specified city ($city). It then uses a combination of grep and grep -Eo to extract the current temperature in degrees Celsius and assigns it to the variable obs_temp.

The second line (echo $obs_temp) prints the current temperature to the console.

3.1.2. Extract tomorrow's temperature forecast for noon, and store it in a shell variable called fc_temp
Click here for Hint
Provided you understand the previous pipeline, you will be able to solve this problem through experimentation.

Click here for Solution
Add to rx_poc.sh:

1
2
3

# To extract the forecast tempearature for noon tomorrow

fc_temp=$(curl -s wttr.in/$city?T | head -23 | tail -1 | grep '°.' | cut -d 'C' -f2 | grep -Eo -e '-?[[:digit:]].\*')
echo "The forecasted temperature for noon tomorrow for $city : $fc_temp C"

Copied!
The first line uses a combination of head and tail to narrow down to the line containing tomorrow’s noon forecast temperature. grep and cut are employed to isolate and format the temperature information, and, the numeric part of the temperature is captured using grep -Eo.

The second line (echo $fc_temp) prints the forecast temperature for noon tomorrow to the console.

3.2. Store the current day, month, and year in corresponding shell variables
Click here for Hint
Use command substitution and the date command with the correct formatting options.
The time zone for Casablanca is UTC+1. To get the local time for Casablanca, you can set the time-zone environment variable, TZ, as follows:

1
TZ='Morocco/Casablanca'

Copied!
Click here for Solution
Add to rx_poc.sh:

1
2
3
4
5
6
7
#Assign Country and City to variable TZ
TZ='Morocco/Casablanca'

# Use command substitution to store the current day, month, and year in corresponding shell variables:

day=$(TZ='Morocco/Casablanca' date -u +%d) 
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)

Copied!
Note: You might be wondering why we didn't just set hour to a value of 12, since we want to get the time at noon.
However, if we did, we would lose the ability to verify that we are actually running the code at the correct local time.You should think of the local time as a measurement rather than a set number.

3.3. Merge the fields into a tab-delimited record, corresponding to a single row in Table 1
Append the resulting record as a row of data to your weather log file.

Click here for Hint
How did you create the header to initialize your log file?

Click here for Solution
Add to rx_poc.sh:

1
2
record=$(echo -e "$year\t$month\t$day\t$obs_temp\t$fc_temp C")
echo $record>>rx_poc.log

### ASSISTANT

# 🧪 Exercise 3 – Extract and Load Required Weather Data

In this exercise, you learned how to **extract specific temperature data** from a raw weather report and **store it in variables** for later use.

You also used the `date` command with timezone settings to get **localized date values**, and finally, you built a **tab-delimited record** and appended it to your log file — bringing together all the skills you've been building so far:

- Variables
- Command substitution
- Text filtering with `grep`, `cut`, `head`, and `tail`
- I/O redirection and logging

---

## ✅ Step-by-Step Breakdown

### 🔹 3.1 Edit `rx_poc.sh` to extract required data

#### 3.1.1 Extract Current Temperature (`obs_temp`)

```bash
obs_temp=$(curl -s wttr.in/$city?T | grep -m 1 '°.' | grep -Eo -e '-?[[:digit:]].*')
echo "The current Temperature of $city: $obs_temp"
```

- `curl`: Fetches weather data silently
- `grep -m 1 '°.'`: Gets first line with a degree symbol (current temp)
- `grep -Eo -e '-?[[:digit:]].*'`: Extracts only the numeric part (e.g., `-5°C`, `+25°F`)
- Assigns result to `obs_temp` using `$(...)` command substitution

---

#### 3.1.2 Extract Tomorrow's Noon Forecast (`fc_temp`)

```bash
fc_temp=$(curl -s wttr.in/$city?T | head -23 | tail -1 | grep '°.' | cut -d 'C' -f2 | grep -Eo -e '-?[[:digit:]].*')
echo "The forecasted temperature for noon tomorrow for $city : $fc_temp C"
```

- `head -23`: Skips header lines and gets to tomorrow’s section
- `tail -1`: Isolates the last line processed so far
- `grep '°.'`: Finds the temperature line
- `cut -d 'C' -f2`: Removes the color formatting before the number
- `grep -Eo`: Extracts just the numeric value

---

### 🔹 3.2 Store Day, Month, and Year in Shell Variables

```bash
TZ='Morocco/Casablanca'
day=$(TZ='Morocco/Casablanca' date -u +%d)
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)
```

- You set the `TZ` variable to ensure accurate local time for Casablanca
- Used `date` with format specifiers:
  - `%d` = day
  - `%m` = month
  - `%Y` = full year

> 💡 Note: The `date -u` ensures consistent behavior across time zones by working in UTC internally

---

### 🔹 3.3 Merge Fields into a Tab-Delimited Record and Append to Log

```bash
record=$(echo -e "$year\t$month\t$day\t$obs_temp\t$fc_temp C")
echo "$record" >> rx_poc.log
```

- `echo -e`: Enables interpretation of escape characters like `\t` (tab)
- `$record`: Holds one complete row of structured data
- `>> rx_poc.log`: Appends the new row to your log file

After running this script once, your `rx_poc.log` should look like:

```
year	month	day	obs_temp	fc_temp
2025	04	05	+22	+20
```

---

## 📋 Summary Table

| Task                         | Command                                                          |
| ---------------------------- | ---------------------------------------------------------------- |
| Get current temperature      | `curl -s wttr.in/Casablanca?T \| grep -m 1 '°.' \| grep -Eo ...` |
| Get tomorrow’s noon forecast | `curl ... \| head -23 \| tail -1 \| grep ...`                    |
| Set timezone                 | `TZ='Morocco/Casablanca'`                                        |
| Get local date parts         | `date +%d`, `date +%m`, `date +%Y`                               |
| Build tab-delimited record   | `echo -e "$year\t$month\t..."`                                   |
| Append to log file           | `echo "$record" >> rx_poc.log`                                   |

---

## 🧠 Why This Matters

This script demonstrates real-world automation:

- It fetches live data from the web
- Parses meaningful values from noisy output
- Logs structured data into a file
- Uses environment variables and shell logic effectively

These are essential steps toward creating robust **data pipelines**, **monitoring tools**, and **automated reports** in Linux.

---

## 💡 Pro Tips

- Always quote your variables when echoing to files:
  ```bash
  echo "$record" >> rx_poc.log
  ```
- Test each filter step-by-step:
  ```bash
  curl -s wttr.in/Casablanca?T | grep -m 1 '°.'
  ```
- Use `cat rx_poc.log` or `tail rx_poc.log` to verify results
- Schedule your script daily using `cron` to build a long-term weather dataset!

---

Great job extracting and storing **real-time weather data** in a structured log!  
You're now writing scripts that not only run commands but also **process external data**, **parse text**, and **log structured information**.

Would you like to continue with:

- **Exercise 4 – Automating Your Weather Report with Cron**
- **Visualizing Your Weather Log**
- **Using `awk` to Analyze Daily Trends**

Let me know — I'm here to help you keep building powerful automation workflows! 🐧🌤️📘✨

### USER

Exercise 4 - Schedule your Bash script rx_poc.sh to run every day at noon local time
4.1. Determine what time of day to run your script
Recall that you want to load the weather data coresponding to noon, local time, in Casablanca every day.

First, check the time difference between your system's default time zone and UTC.

Click here for Hint 1
Use the date command twice with appropriate options; once to get your system time, and once to get UTC.

Click here for Solution
Running the following commands gives you the info you need to get the time difference between your system and UTC.

1
2
3
4
$ date
Mon Feb 13 11:28:12 EST 2023
$ date -u
Mon Feb 13 16:28:16 UTC 2023

Copied!
Now you can determine how many hours difference there are between your system's local time and that of Casablanca. In the example above, we see that the system time relative to UTC is UTC+5 (i.e. 16 - 11 = 5).

We know Casablanca is UTC+1, so the system time relative to Casablanca is 4 hours earlier. Thus to run your script at noon Casablanca time, you need to run it at 8 am.

4.2 Create a cron job that runs your script
Click here for Hint
Edit the crontab file and review the crontab syntax description included in the file.

Click here for Solution
Edit the crontab file:

1
crontab -e

Copied!
Add the following line at the end of the file:

1
0 8 \* \* \* /home/project/rx_poc.sh

Copied!
Save the file and quit the editor.

4.3 Full solution
For reference, here is a Bash script that creates the raw weather report. Try to follow all the steps on your own before looking!

Click here for Full Solution
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
#! /bin/bash

#Assign city name as Casablanca
city=Casablanca
#Obtain the weather report for Casablanca
curl -s wttr.in/$city?T --output weather_report
#To extract Current Temperature
obs_temp=$(curl -s wttr.in/$city?T | grep -m 1 '°.' | grep -Eo -e '-?[[:digit:]].\*')
echo "The current Temperature of $city: $obs_temp"

# To extract the forecast tempearature for noon tomorrow

fc_temp=$(curl -s wttr.in/$city?T | head -23 | tail -1 | grep '°.' | cut -d 'C' -f2 | grep -Eo -e '-?[[:digit:]].\*')
echo "The forecasted temperature for noon tomorrow for $city : $fc_temp C"
#Assign Country and City to variable TZ
TZ='Morocco/Casablanca'

# Use command substitution to store the current day, month, and year in corresponding shell variables:

day=$(TZ='Morocco/Casablanca' date -u +%d)
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)

# Log the weather

record=$(echo -e "$year\t$month\t$day\t$obs_temp\t$fc_temp C")
echo $record>>rx_poc.log

### ASSISTANT

# 🌤️ Exercise 4 – Schedule Your Bash Script `rx_poc.sh` to Run Daily at Noon (Casablanca Time)

In this exercise, you learned how to **schedule your weather report script** (`rx_poc.sh`) to run automatically every day at **noon local time in Casablanca** using the **cron scheduler**.

This is a key step toward **automating data collection workflows**, and it demonstrates how to:

- Account for **timezone differences**
- Use `crontab -e` to schedule jobs
- Append structured weather data to a log file daily

---

## ✅ Step-by-Step Breakdown

### 🔹 4.1 Determine Correct UTC Time for Noon in Casablanca

You checked your system's current time and UTC time:

```bash
date
date -u
```

Example output:

```
Mon Feb 13 11:28:12 EST 2023
Mon Feb 13 16:28:16 UTC 2023
```

Your system was 5 hours ahead of UTC, but Casablanca is only **UTC+1**, so you determined that **8 AM system time = 12 PM Casablanca time**

> This ensures your script runs at **local noon in Casablanca**, even if your server is in another timezone.

---

### 🔹 4.2 Create a Cron Job to Run Your Script Daily at 8 AM System Time

You edited your crontab:

```bash
crontab -e
```

Then added the job:

```bash
0 8 * * * /home/project/rx_poc.sh
```

This line means:
| Field | Value | Meaning |
|-------|-------|---------|
| minute | `0` | At the top of the hour |
| hour | `8` | At 8:00 AM |
| day | `*` | Every day |
| month | `*` | Every month |
| weekday | `*` | Any day of the week |

So this will run your script every morning at **8 AM system time**, which corresponds to **12 PM local time in Casablanca** due to the UTC offset.

---

### 🔹 4.3 Full Solution – Weather Logging Script

Here’s the complete `rx_poc.sh` script for reference:

```bash
#!/bin/bash

# Assign city name as Casablanca
city=Casablanca

# Obtain the weather report for Casablanca
curl -s wttr.in/$city?T --output weather_report

# To extract Current Temperature
obs_temp=$(curl -s wttr.in/$city?T | grep -m 1 '°.' | grep -Eo -e '-?[[:digit:]].*')
echo "The current Temperature of $city: $obs_temp"

# To extract tomorrow’s forecast temperature for noon
fc_temp=$(curl -s wttr.in/$city?T | head -23 | tail -1 | grep '°.' | cut -d 'C' -f2 | grep -Eo -e '-?[[:digit:]].*')
echo "The forecasted temperature for noon tomorrow for $city : $fc_temp C"

# Set timezone to Casablanca
TZ='Morocco/Casablanca'

# Store current date parts
day=$(TZ='Morocco/Casablanca' date -u +%d)
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)

# Build record with tabs
record=$(echo -e "$year\t$month\t$day\t$obs_temp\t$fc_temp C")

# Append to log file
echo "$record" >> rx_poc.log
```

---

## 📋 Summary Table

| Task                            | Command                                          |
| ------------------------------- | ------------------------------------------------ |
| Check current time              | `date`                                           |
| Check UTC time                  | `date -u`                                        |
| Edit crontab                    | `crontab -e`                                     |
| Schedule script at 8 AM daily   | `0 8 * * * /home/project/rx_poc.sh`              |
| Local time for Casablanca       | `TZ='Morocco/Casablanca'`                        |
| Get localized date parts        | `date +%d`, `date +%m`, `date +%Y`               |
| Append tab-delimited row to log | `echo -e "$year\t$month\t$day..." >> rx_poc.log` |

---

## 🧠 Why Scheduling Matters

Automating tasks like this helps you:

- Collect data **without manual intervention**
- Maintain a **long-term dataset**
- Ensure consistency across time zones
- Free up time for more complex analysis later

This kind of setup is used widely in:

- **Weather monitoring**
- **Log aggregation**
- **Daily reports**
- **System health checks**

---

## 💡 Pro Tips

- Always test scripts manually before scheduling:
  ```bash
  ./rx_poc.sh
  ```
- Check logs after running:
  ```bash
  cat rx_poc.log
  ```
- Schedule with care — use `crontab -l` often to verify scheduled jobs
- Redirect both stdout and stderr for debugging:
  ```bash
  0 8 * * * /home/project/rx_poc.sh >> /tmp/weather.log 2>&1
  ```

---

Great work completing this end-to-end automation project!

You've built a full pipeline that:

1. Fetches live weather data
2. Parses and cleans it
3. Logs it into a structured file
4. Runs automatically using cron

Would you like to continue with:

- **Analyzing Your Weather Log with `awk` or `gnuplot`**
- **Creating a Weekly Report**
- **Adding Error Handling to Your Script**

Let me know — I'm here to help you keep building powerful automation skills! 🐧⏰📘✨

### USER

Exercise 5 - Create a script to report historical forecasting accuracy
Now that you've created an ETL shell script to gather weather data into a report, let's create another script to measure and report the accuracy of the forecasted temperatures against the actuals.

To start, create a tab-delimited file named historical_fc_accuracy.tsv.
Insert the following code into the file to include a header with column names:

1
echo -e "year\tmonth\tday\tobs_temp\tfc_temp\taccuracy\taccuracy_range" > historical_fc_accuracy.tsv

Copied!
One key difference between this report and the previous report you generated is that the forecast temperature will now be aligned with the date the forecast is for. As a result, the date will be in the same row as the observed temperature for that date, rather than the previous row on the day that the forecast was made.

Also create an executable Bash script called fc_accuracy.sh.
Rather than scheduling your new script to run periodically, think of it as a tool you can use to generate the historical forecast accuracy on demand.

5.1. Determine the difference between today's forecasted and actual temperatures
Rather than writing the script to process all of the data at once, let's simplify by solving the problem for just one instance. Later you can modify the script to handle the general case of mupltiple days.

5.1.1. Extract the forecasted and observed temperatures for today and store them in variables
Click here for Hint 1
Look up the record from yesterday.

Click here for Hint 2
Extract the forecast from the appropriate field.

Click here for Solution
1
yesterday_fc=$(tail -2 rx_poc.log | head -1 | cut -d " " -f5)

Copied!
5.1.2. Calculate the forecast accuracy
Click here for Hint
First extract today's observed temperature. Then calculate the difference between the forecasted and observed temperatures.

Click here for Solution
1
2
3
today_temp=$(tail -1 rx_poc.log | cut -d " " -f4)
accuracy=$(($yesterday_fc-$today_temp))
echo "accuracy is $accuracy"

Copied!
Tip: Your weather report must have at least two days of data for this calulation to make sense.
To test your code you can simply append some artificial data to your weather report, rx_poc.log.

5.2. Assign a label to each forecast based on its accuracy
Let's set the accuracy labels according to the range that the accuracy fits most tightly within, according to the following table. Validate your result.

accuracy range accuracy label
+/- 1 deg excellent
+/- 2 deg good
+/- 3 deg fair
+/- 4 deg poor
Click here for Hint 1
Use two conditions to compare the accuracy sizes to each positive and negative integer range, accordingly.

Click here for Solution
1
2
3
4
5
6
7
8
9
10
11
12
13
14
if [ -1 -le $accuracy ] && [ $accuracy -le 1 ]
then
accuracy_range=excellent
elif [ -2 -le $accuracy ] && [ $accuracy -le 2 ]
then
accuracy_range=good
elif [ -3 -le $accuracy ] && [ $accuracy -le 3 ]
then
accuracy_range=fair
else
accuracy_range=poor
fi
echo "Forecast accuracy is $accuracy"

Copied!
5.3. Append a record to your historical forecast accuracy file.
Click here for Hint
Extract the right row and remaining data you need to populate all fields.

Click here for Solution
1
2
3
4
5
row=$(tail -1 rx_poc.log)
year=$( echo $row | cut -d " " -f1)
month=$( echo $row | cut -d " " -f2)
day=$( echo $row | cut -d " " -f3)
echo -e "$year\t$month\t$day\t$today_temp\t$yesterday_fc\t$accuracy\t$accuracy_range" >> historical_fc_accuracy.tsv

Copied!
5.4. Full solution for handling a single day
Below is the final script of fc_accuracy.sh for handling the accuracy calculations based on just one instance, or day.

Click here for Solution
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
#! /bin/bash
yesterday_fc=$(tail -2 rx_poc.log | head -1 | cut -d " " -f5)
today_temp=$(tail -1 rx_poc.log | cut -d " " -f4)
accuracy=$(($yesterday_fc-$today_temp))
echo "accuracy is $accuracy"
if [ -1 -le $accuracy ] && [ $accuracy -le 1 ]
then
           accuracy_range=excellent
elif [ -2 -le $accuracy ] && [ $accuracy -le 2 ]
   then
               accuracy_range=good
       elif [ -3 -le $accuracy ] && [ $accuracy -le 3 ]
       then
                   accuracy_range=fair
           else
                       accuracy_range=poor
fi
echo "Forecast accuracy is $accuracy_range"
row=$(tail -1 rx_poc.log)
year=$( echo $row | cut -d " " -f1)
month=$( echo $row | cut -d " " -f2)
day=$( echo $row | cut -d " " -f3)
echo -e "$year\t$month\t$day\t$today_temp\t$yesterday_fc\t$accuracy\t$accuracy_range" >> historical_fc_accuracy.tsv

Copied!
5.5. Generalization to all days
We leave it as an exercise for you to generalize your code to create the entire weather accuracy history. In the next exercise, you will download and work with a synthetic version of this weather accuracy history report.

Here are some suggestions to guide you should you wish to create the weather accuracy history yourself:

Iterate through your weather log file using a for loop. On each iteration:
Use head and tail to extract consecutive pairs of lines on each iteration
This provides you with the current and previous day's data
Treat this pair of lines like you did in your code as yesterday and today's data
Perform your accuracy calulations as before
Use the correct row to extract date information
Append your resulting data to your historical forecast accuracy report

### ASSISTANT

# 📊 Exercise 5 – Create a Script to Report Historical Forecast Accuracy

In this exercise, you created a **new Bash script** called `fc_accuracy.sh` that analyzes the accuracy of temperature forecasts stored in your `rx_poc.log` file.

You built logic to:

- Extract forecasted and observed temperatures
- Calculate the difference (forecast error)
- Assign an **accuracy label** based on how close the forecast was to the actual temperature
- Append a new row to a **historical accuracy report**: `historical_fc_accuracy.tsv`

This is a great example of how Linux scripting can be used for **data analysis**, not just automation!

---

## ✅ Step-by-Step Breakdown

### 🔹 5.1 Determine the Difference Between Forecasted and Observed Temperatures

#### 5.1.1 Extract Forecasted and Observed Temps

You extracted yesterday’s forecast from the second-to-last line of `rx_poc.log`:

```bash
yesterday_fc=$(tail -2 rx_poc.log | head -1 | cut -d " " -f5)
```

Then today's observed temperature from the last line:

```bash
today_temp=$(tail -1 rx_poc.log | cut -d " " -f4)
```

> 💡 These commands use `tail`, `head`, and `cut` to parse tabular data directly in the shell — no external tools required!

---

#### 5.1.2 Calculate Forecast Accuracy

You calculated the difference between forecast and actual:

```bash
accuracy=$(($yesterday_fc - $today_temp))
echo "accuracy is $accuracy"
```

This gives a numeric value representing how accurate the previous day’s forecast was.

---

### 🔹 5.2 Assign Accuracy Labels Based on Range

You added conditional logic to categorize the forecast accuracy:

```bash
if [ -1 -le $accuracy ] && [ $accuracy -le 1 ]; then
    accuracy_range=excellent
elif [ -2 -le $accuracy ] && [ $accuracy -le 2 ]; then
    accuracy_range=good
elif [ -3 -le $accuracy ] && [ $accuracy -le 3 ]; then
    accuracy_range=fair
else
    accuracy_range=poor
fi
```

| Accuracy Range | Label     |
| -------------- | --------- |
| ±1°C           | excellent |
| ±2°C           | good      |
| ±3°C           | fair      |
| > ±3°C         | poor      |

This shows how to build **decision-making logic into Bash scripts** using conditionals.

---

### 🔹 5.3 Append Record to Historical Accuracy File

You built a record line by line using fields from the log:

```bash
row=$(tail -1 rx_poc.log)
year=$(echo $row | cut -d " " -f1)
month=$(echo $row | cut -d " " -f2)
day=$(echo $row | cut -d " " -f3)
```

Then appended everything to your accuracy file:

```bash
echo -e "$year\t$month\t$day\t$today_temp\t$yesterday_fc\t$accuracy\t$accuracy_range" >> historical_fc_accuracy.tsv
```

You now have a structured, tab-separated history of forecast accuracy!

---

### 🔹 5.4 Full Script: `fc_accuracy.sh`

Here’s the complete script you built:

```bash
#!/bin/bash

# Extract yesterday's forecast
yesterday_fc=$(tail -2 rx_poc.log | head -1 | cut -d " " -f5)

# Extract today's observed temperature
today_temp=$(tail -1 rx_poc.log | cut -d " " -f4)

# Calculate accuracy
accuracy=$(($yesterday_fc - $today_temp))

# Print accuracy result
echo "accuracy is $accuracy"

# Evaluate accuracy range
if [ -1 -le $accuracy ] && [ $accuracy -le 1 ]; then
    accuracy_range=excellent
elif [ -2 -le $accuracy ] && [ $accuracy -le 2 ]; then
    accuracy_range=good
elif [ -3 -le $accuracy ] && [ $accuracy -le 3 ]; then
    accuracy_range=fair
else
    accuracy_range=poor
fi

# Print final category
echo "Forecast accuracy is $accuracy_range"

# Extract date fields
row=$(tail -1 rx_poc.log)
year=$(echo $row | cut -d " " -f1)
month=$(echo $row | cut -d " " -f2)
day=$(echo $row | cut -d " " -f3)

# Build and append the record
record=$(echo -e "$year\t$month\t$day\t$today_temp\t$yesterday_fc\t$accuracy\t$accuracy_range")
echo -e "$record" >> historical_fc_accuracy.tsv
```

---

### 🔁 5.5 Generalizing to All Days

You were encouraged to expand the script to analyze all days in your weather log.

#### Suggested Approach Using a Loop:

```bash
for ((i=2; i<$(wc -l rx_poc.log); i++)); do
    yesterday_line=$(head -$i rx_poc.log | tail -1)
    today_line=$(head -$(($i+1)) rx_poc.log | tail -1)

    # extract values and compute accuracy...
done
```

This would allow you to process multiple days and generate a full historical report.

---

## 📋 Summary Table

| Task                       | Command                                                      |
| -------------------------- | ------------------------------------------------------------ |
| Create TSV header          | `echo -e "year\tmonth\tday..." > historical_fc_accuracy.tsv` |
| Get yesterday’s forecast   | `tail -2 rx_poc.log \| head -1 \| cut ...`                   |
| Get today’s observation    | `tail -1 rx_poc.log \| cut ...`                              |
| Compute accuracy           | `$((yesterday_fc - today_temp))`                             |
| Conditional labels         | `if [ ... ]` block                                           |
| Build tab-delimited record | `echo -e "field1\tfield2\t..."`                              |
| Append to accuracy log     | `>> historical_fc_accuracy.tsv`                              |

---

## 🧠 Why This Matters

This script demonstrates how you can use Bash to:

- Analyze time-series data
- Compare expected vs actual values
- Generate structured reports
- Automate decision-making with conditionals

These are essential skills for:

- Data validation
- Forecasting systems
- Quality control pipelines
- Log analysis and system monitoring

---

## 💡 Pro Tips

- Always test scripts manually before running them:
  ```bash
  ./fc_accuracy.sh
  ```
- Use `cat historical_fc_accuracy.tsv` to verify results
- Consider adding logging or email alerts as enhancements
- You can improve error handling by checking if files exist or have enough lines

---

Great job creating a **forecast accuracy script** in Bash!  
You're now writing scripts that go beyond automation — you're doing real **data comparison and classification**.

Would you like to continue with:

- **Exercise 6 – Visualizing Your Weather Data**
- **Using `awk` or `gnuplot` for Analysis**
- **Creating Reports in CSV or Markdown**

Let me know — I'm here to help you keep building powerful Linux data workflows! 🐧📊📘✨

### USER

Exercise 6 - Create a script to report weekly statistics of historical forecasting accuracy
In this exercise, you will download a synthetic historical forecasting accuracy report and calculate some basic statistics based on the latest week of data.

Begin by creating an executable bash script called weekly_stats.sh.

6.1. Download the synthetic historical forecasting accuracy dataset
Run the following command in the terminal to download the dataset to your current working directory.

1
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-LX0117EN-Coursera/labs/synthetic_historical_fc_accuracy.tsv

Copied!
6.2. Load the historical accuracies into an array covering the last week of data
Remember to make your script executable. Also validate your result by printing the array to the terminal.

Click here for Hint1
First extract the last week of data.

Click here for Hint2
Store the values in a temporary file called scratch.txt. Write the contents of scratch.txt into an array called week_fc.

Click here for Solution
Your shell script should look something like the following. There are many ways to accomplish this task, so the solution provided is not unique.
1
2
3
4
5
6
7
8
9
10
#!/bin/bash
echo $(tail -7 synthetic_historical_fc_accuracy.tsv  | cut -f6) > scratch.txt
week_fc=($(echo $(cat scratch.txt)))

# validate result:

for i in {0..6}; do
echo ${week_fc[$i]}
done

Copied!
6.3. Display the minimum and maximum absolute forecasting errors for the week
Now use your array to calculate the minimum and maximum absolute errors over the last week. For example, if you have a vaule of -1, change it to be 1. Echo the minimum and maximum absolute errors to the terminal.

Click here for Hint1
Check for any negative values in your array, and reassign these array entries with their positve counterparts.

Click here for Hint2
Initialize two variables, minimum and maximum. Loop over the array values and modify these two variables as required.

Click here for Solution
Your final shell script for weekly_stats.sh should now look something like the following.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
#!/bin/bash
echo $(tail -7 synthetic_historical_fc_accuracy.tsv  | cut -f6) > scratch.txt
week_fc=($(echo $(cat scratch.txt)))

# validate result:

for i in {0..6}; do
echo ${week_fc[$i]}
done
for i in {0..6}; do
if [[${week_fc[$i]} < 0]]
then
week_fc[$i]=$(((-1)*week_fc[$i]))
fi

# validate result:

echo ${week_fc[$i]}
done
minimum=${week_fc[1]}
maximum=${week_fc[1]}
for item in ${week_fc[@]}; do
   if [[ $minimum > $item ]]
   then
     minimum=$item
fi
if [[$maximum < $item]]
then
maximum=$item
fi
done
echo "minimum ebsolute error = $minimum"
echo "maximum absolute error = $maximum"

### ASSISTANT

# 📊 Exercise 6 – Create a Script to Report Weekly Statistics of Historical Forecasting Accuracy

In this exercise, you built a **Bash script** that:

- Downloads a synthetic dataset of historical weather forecast accuracy
- Extracts the **last 7 days** of forecast errors
- Converts them into **absolute values**
- Calculates and reports the **minimum and maximum absolute errors**

This demonstrates how Bash can be used not just for automation, but also for basic **data analysis**, **statistics**, and **array manipulation**.

---

## ✅ Step-by-Step Breakdown

### 🔹 6.1 Download the Synthetic Dataset

You downloaded a sample file using `wget`:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-LX0117EN-Coursera/labs/synthetic_historical_fc_accuracy.tsv
```

This file contains tab-separated data like:

```
year	month	day	obs_temp	fc_temp	accuracy	accuracy_range
2025	04	01	+22	+23	-1	poor
...
```

---

### 🔹 6.2 Load Last Week’s Data into an Array

#### Extract last 7 entries (days) from the file:

```bash
tail -7 synthetic_historical_fc_accuracy.tsv | cut -f6 > scratch.txt
```

- `tail -7`: gets the last 7 lines
- `cut -f6`: extracts the **accuracy** column
- `> scratch.txt`: saves it temporarily

Then load into a Bash array:

```bash
week_fc=($(cat scratch.txt))
```

Or more precisely:

```bash
week_fc=($(echo $(tail -7 synthetic_historical_fc_accuracy.tsv | cut -f6)))
```

You validated it by printing each element:

```bash
for i in {0..6}; do
    echo ${week_fc[$i]}
done
```

---

### 🔹 6.3 Calculate Min and Max Absolute Errors

#### Convert negative values to positive:

```bash
for i in {0..6}; do
    if [[ ${week_fc[$i]} < 0 ]]; then
        week_fc[$i]=$(( -1 * ${week_fc[$i]} ))
    fi
done
```

Now all errors are **positive**, representing **absolute error**.

#### Initialize min and max:

```bash
minimum=${week_fc[0]}
maximum=${week_fc[0]}
```

#### Loop through the array and update:

```bash
for item in ${week_fc[@]}; do
    if [[ $item -lt $minimum ]]; then
        minimum=$item
    fi
    if [[ $item -gt $maximum ]]; then
        maximum=$item
    fi
done
```

Finally, print the results:

```bash
echo "Minimum absolute error = $minimum"
echo "Maximum absolute error = $maximum"
```

---

## 📋 Summary Table

| Task                          | Command                                      |
| ----------------------------- | -------------------------------------------- |
| Download dataset              | `wget URL`                                   |
| Extract last 7 days' accuracy | `tail -7 file.tsv \| cut -f6`                |
| Store values in array         | `week_fc=($(...))`                           |
| Convert to absolute values    | Multiply by `-1` if negative                 |
| Find minimum value            | Compare in loop: `if [ $item -lt $minimum ]` |
| Find maximum value            | Compare in loop: `if [ $item -gt $maximum ]` |
| Print stats                   | `echo "min = $minimum"`                      |

---

## 🧠 Why This Matters

You're now writing Bash scripts that go beyond simple automation — they're performing **real data analysis tasks**:

- Loading data
- Transforming values
- Applying logic
- Computing statistics

These skills apply directly to:

- Log file analysis
- System performance tracking
- Quality control pipelines
- DevOps monitoring tools

---

## 💡 Pro Tips

- Use `abs()` logic in Bash with ternary expressions:
  ```bash
  abs=${value#-}   # Removes leading '-' if present
  ```
- Use `awk` for cleaner min/max calculations:
  ```bash
  awk '{ sum += $1 } END { print sum }' scratch.txt
  ```
- Always quote variables to avoid issues:
  ```bash
  echo "${week_fc[@]}"
  ```

---

## 🚀 Real-World Applications

You could use similar techniques to:

- Monitor **system logs** and report on anomalies
- Analyze **forecast vs actual** metrics in operations
- Build **daily summaries** or **weekly reports**
- Track **error margins** over time

---

Great job creating a **statistical reporting script** in Bash!  
You've shown how Linux shell scripting can be used for:

- **Data extraction**
- **Transformation**
- **Statistical analysis**

Would you like to continue with:

- **Exercise 7 – Visualizing Your Forecast Accuracy**
- **Using `awk` for Advanced Analysis**
- **Generating Reports in CSV or Markdown**

Let me know — I'm here to help you keep building your **Linux data analysis superpowers**! 🐧📊📘✨

### USER

Summary
Congratulations! You've just completed a challenging, real-world practice project using many of the concepts you've learned from this course. The knowledge you've gained has prepared you to solve many practical real world problems. You're almost finished with this course now, and the final step in your journey is to complete the peer-reviewed Final Project.

In this lab, you learned how to:

Initialize your weather report log file
Write a Bash script that downloads the raw weather data, and extracts and loads the required data
Schedule your Bash script rx_poc.sh to run every day at noon local time
Apply advanced Bash scripting to produce reporting metrics
Create a script to report historical forecasting accuracy
Create a script to report the minimum and maximum absolute errors for the week

### ASSISTANT

# 🎉 **Summary – Great Job Completing the Linux Shell Scripting Project!**

You've successfully completed a hands-on, real-world project that brought together many essential Linux scripting concepts into one practical workflow.

---

## ✅ What You Accomplished in This Lab

Here's a quick recap of what you learned and applied:

| Skill                                   | Applied In                                                          |
| --------------------------------------- | ------------------------------------------------------------------- |
| **Initialize log files**                | Created `rx_poc.log` with headers using `echo -e` and `\t` tabs     |
| **Build Bash scripts**                  | Wrote `rx_poc.sh` to fetch and parse weather data                   |
| **Extract values from web pages**       | Used `curl`, `grep`, `cut`, and `head/tail` pipelines               |
| **Schedule scripts with cron**          | Set up daily execution at local noon using `crontab -e`             |
| **Analyze forecast accuracy**           | Built `fc_accuracy.sh` to compare forecast vs observed temperatures |
| **Use conditionals for categorization** | Labeled forecast accuracy as excellent/good/fair/poor               |
| **Process arrays and calculate stats**  | Built `weekly_stats.sh` to find min/max absolute errors over 7 days |

---

## 🧠 Why This Matters

This lab gave you experience with:

- **Data automation** (ETL-style workflows)
- **Scripting logic** (variables, loops, conditionals)
- **Time-based scheduling** (`cron`)
- **Text processing and analysis** (`grep`, `cut`, `tail`, `head`)
- **Array manipulation and statistics** (min, max, absolute values)

These are not just academic exercises — they reflect real tasks performed by:

- System administrators
- DevOps engineers
- Data analysts
- Automation developers

---

## 💡 Real-World Use Cases

Your skills now allow you to:

- Automate **daily reports**
- Monitor **weather or system metrics**
- Analyze **forecast vs actuals** in operations
- Schedule **backups, health checks**, and more using `cron`
- Process **CSV/TSV logs** and generate summaries

---

## 📚 Key Tools You Mastered

| Tool                         | Purpose                                        |
| ---------------------------- | ---------------------------------------------- |
| `bash`                       | Writing shell scripts                          |
| `curl`                       | Fetching live data from URLs                   |
| `grep`, `cut`, `awk`         | Text filtering and parsing                     |
| `crontab`                    | Scheduling jobs automatically                  |
| `if`, `for`, `while`         | Control flow and logic                         |
| Arrays                       | Storing and manipulating multiple values       |
| Variables                    | Holding dynamic values during script execution |
| `tail`, `head`               | Inspecting and slicing data files              |
| `echo`, `cat`, `ls`, `chmod` | Basic file and terminal output management      |

---

## 🛠️ Final Pro Tips

- Always test your scripts manually before scheduling them
- Use `set -x` to debug scripts (add it at the top)
- Store intermediate results in temp files or arrays for better visibility
- Validate your work: `cat rx_poc.log`, `crontab -l`, `./weekly_stats.sh`

---

## 🚀 You're Ready for the Final Step!

Now that you’ve built:

- A **weather logging pipeline**
- An **accuracy evaluation script**
- A **weekly statistics reporter**

You’re well-prepared to tackle the **peer-reviewed Final Project** — where you can apply all your skills in a structured way.

Would you like help preparing for the final project?  
Or would you like to explore:

- Generating charts with `gnuplot`
- Creating HTML reports
- Using `awk` for advanced text processing

Let me know — I'm here to help you finish strong and keep building your **Linux scripting mastery**! 🐧💻📘📊✨

### USER

Cumulative Cheat Sheet - Hands-On Introduction to Linux Commands and Shell Scripting
Introduction to Linux
Command Syntax Description Example
List ls [OPTIONS] [FILE/DIRECTORY] List files and directories at path ls /home/user/documents
Print Working Directory pwd Print present working directory pwd
Change Directory cd [DIRECTORY] Change current directory cd /home/user/documents
Super user do sudo [COMMAND] Run command with superuser privileges sudo apt update
Text Editor nano [FILE] Open file with Nano text editor nano myfile.txt
Introduction to Linux Commands
Informational, Navigational, & Management Commands
Command Syntax Description Example
Who Am I whoami Return username whoami
User ID id Return current user or group ID id
System Information uname [OPTIONS] Display system information uname -a
Manual Pages man [COMMAND] Display manual page for a command man ls
Curl curl [OPTIONS] [URL] Transfer data from or to server curl https://some*website.com
Date date [OPTIONS] Display current date and time date
Find find [DIRECTORY] [OPTIONS] Find files and directories at specified path find /home/user -name '*.txt'
Make Directory mkdir [DIRECTORY] Create new directory mkdir myfolder
Remove Directory rmdir [DIRECTORY] Remove empty directory rmdir myfolder
Process Status ps [OPTIONS] Display process status information ps -ef
Table of Processes top Display live system resource usage top
Disk Usage df [OPTIONS] [FILESYSTEM] Display disk space usage df -h
Create Empty File touch [FILE] Create new file or update timestamp touch myfile.txt
Copy cp [OPTIONS] [SOURCE] [DESTINATION] Copy files or directories from source to destination cp myfile.txt /home/user/documents
Move mv [OPTIONS] [SOURCE] [DESTINATION] Move or rename files and directories mv myfile.txt /home/user/documents
Remove rm [OPTIONS] [FILE/DIRECTORY] Remove files rm my*scratch_file.txt
Remove nonempty directory rm -r path_to_temp_directory
rmdir [OPTIONS] [DIRECTORY] Remove empty directory rmdir path_to_my_directory
Change Mode chmod [OPTIONS] [MODE] [FILE] Change file or directory permissions chmod u+x myfile.txt
Working with Text Files, Networking & Archiving Commands
Command Syntax Description Example
Concatenate cat [FILE] Display the contents of a file cat myfile.txt
Concatentate and display contents of multiple files cat file1 file2
More more [FILE] Display file one screen at a time more myfile.txt
Head head [OPTIONS] [FILE] Display first N lines of file head -5 myfile.txt
Tail tail [OPTIONS] [FILE] Display last N lines of file tail -5 myfile.txt
Echo echo [ARGUMENTS] Display arguments in console echo Hello, World!
Sort sort [OPTIONS] [FILE] Alphanumerically sort file contents sort file.txt
Unique uniq [OPTIONS] [FILE] Report or remove consecutively repeated lines in file uniq file.txt
Word Count wc [OPTIONS] [FILE] Print the number of lines, words, and characters in a file wc file.txt
Grep grep [OPTIONS] PATTERN [FILE] Search for a specified pattern in a file grep "hello" file.txt
Paste paste [OPTIONS] [FILE1] [FILE2] Merge lines of files side by side paste file1.txt file2.txt
Cut cut [OPTIONS] [FILE] Remove sections from each line of a file cut -d":" -f1 /etc/passwd
Tar tar [OPTIONS] [FILE] Archive files together into a single file tar -czvf archive.tar.gz /directory
Zip zip [OPTIONS] [FILE] Compress files into a zip archive zip archive.zip file1.txt file2.txt
Unzip unzip [OPTIONS] [FILE] Uncompress files from a zip archive unzip archive.zip
Hostname hostname Print the name of the current host system hostname
Ping ping [OPTIONS] HOSTNAME/IP Send ICMP ECHO_REQUEST packets to a network host ping google.com
ip ip [INTERFACE] Display or configure network interface parameters ip addr
IP ip [OPTIONS] Show or manipulate routing, devices, policy routing, and tunnels ip addr
Curl curl [OPTIONS] URL Transfer data from or to a server curl https://some_website.com
Wget wget [OPTIONS] URL Download files from the web wget https://some_website.com/some_file.txt
Introduction to Shell Scripting
Command Syntax Description Example
Shebang #!/bin/[shell] First line of shell script #!/bin/bash
Pipe filter1 | filter2 Chain any number of filters ls | sort -r
Locate executable which [EXECUTABLE] Display location of bash executable which bash
Bash bash [SCRIPT] Interpret and run script using Bash shell bash script.txt
Set set [OPTION] List all shell variables set
Define variable [VARIABLE_NAME]=[VALUE] Define shell variable by name and assign value name="John"
Read read [VARIABLE] Read from standard input and store result in variable read name
Env env Print all environment variables and their values env
Export export [VARIABLE] Extend scope of local variable to all child processes export name
Crontab crontab [OPTIONS] Open crontab default editor crontab -e
List all cron jobs crontab -l
Schedule tasks to run at specified times using cron daemon m h dom mon dow command Append date/time to file every Sunday at 6:15 pm 15 18 * _ 0 date >> sundays.txt
Back up home directory every Monday at 3:00 am 0 3 _ _ 1 tar -cvf my_backup_path\my_archive.tar.gz $HOME\
Run shell script first minute of first day of each month 1 0 1 _ \* ./My_Script.sh
Authors

### ASSISTANT

# 📄 **Cumulative Cheat Sheet – Hands-On Introduction to Linux Commands and Shell Scripting**

This comprehensive cheat sheet summarizes all the essential Linux commands, tools, and scripting techniques you've learned throughout this course. Use it as a quick reference for:

- Terminal navigation
- File and directory management
- Text processing
- Network interaction
- Archiving and compression
- Bash scripting
- Cron scheduling

---

## 🧭 **Introduction to Linux**

| Command                 | Syntax                | Description                          | Example                      |
| ----------------------- | --------------------- | ------------------------------------ | ---------------------------- |
| List files              | `ls [OPTIONS] [PATH]` | Show contents of a directory         | `ls -l /home/user/documents` |
| Print working directory | `pwd`                 | Show current working directory       | `pwd`                        |
| Change directory        | `cd [DIRECTORY]`      | Navigate between directories         | `cd /var/log`                |
| Superuser do            | `sudo [COMMAND]`      | Run command with elevated privileges | `sudo apt update`            |
| Text editor             | `nano [FILE]`         | Edit text files from terminal        | `nano script.sh`             |

---

## 🧾 **Informational, Navigational & Management Commands**

| Command                   | Syntax                  | Description                           | Example                          |
| ------------------------- | ----------------------- | ------------------------------------- | -------------------------------- |
| Who am I                  | `whoami`                | Display current username              | `whoami`                         |
| User identity             | `id`                    | Show user and group IDs               | `id`                             |
| System info               | `uname [OPTIONS]`       | Print system information              | `uname -a`                       |
| Manual pages              | `man [COMMAND]`         | View help for any command             | `man ls`                         |
| Transfer data             | `curl [URL]`            | Transfer data from or to server       | `curl https://example.com`       |
| Show date/time            | `date [OPTIONS]`        | Display current date and time         | `date "+%Y-%m-%d"`               |
| Find files                | `find [PATH] [OPTIONS]` | Locate files and directories          | `find /home -name "*.log"`       |
| Make directory            | `mkdir [DIR]`           | Create new folder                     | `mkdir reports`                  |
| Remove empty dir          | `rmdir [DIR]`           | Delete an empty directory             | `rmdir old_folder`               |
| Process status            | `ps [OPTIONS]`          | List running processes                | `ps -e`                          |
| Real-time process monitor | `top`                   | Dynamic view of running tasks         | `top`                            |
| Disk usage                | `df [OPTIONS]`          | Show free disk space                  | `df -h`                          |
| Create file               | `touch [FILENAME]`      | Create a new file or update timestamp | `touch report.txt`               |
| Copy files                | `cp [SRC] [DEST]`       | Copy files or directories             | `cp report.txt backup/`          |
| Move/rename               | `mv [SRC] [DEST]`       | Move or rename files                  | `mv report.txt final_report.txt` |
| Remove file               | `rm [OPTIONS] [FILE]`   | Delete files                          | `rm temp_file.txt`               |
| Recursive remove          | `rm -r [DIR]`           | Delete non-empty directories          | `rm -r temp_dir/`                |
| Remove empty dirs only    | `rmdir [OPTIONS] [DIR]` | Delete empty folders                  | `rmdir logs_empty`               |
| Change permissions        | `chmod [MODE] [FILE]`   | Modify access settings                | `chmod u+x script.sh`            |

---

## 🖨️ **Working with Text Files, Networking & Archiving**

| Command                  | Syntax                          | Description                          | Example                              |
| ------------------------ | ------------------------------- | ------------------------------------ | ------------------------------------ | ----- |
| Concatenate              | `cat [FILE]`                    | View file contents                   | `cat report.txt`                     |
| Merge files              | `cat file1 file2`               | Combine multiple files               | `cat header.txt body.txt > full.txt` |
| Page through file        | `more [FILE]`                   | View large file one screen at a time | `more bigfile.txt`                   |
| First lines              | `head [OPTIONS] [FILE]`         | Show top lines of a file             | `head -n 10 data.csv`                |
| Last lines               | `tail [OPTIONS] [FILE]`         | Show bottom lines of a file          | `tail -n 5 log.txt`                  |
| Echo output              | `echo [TEXT]`                   | Print strings or variables           | `echo "Hello World!"`                |
| Sort content             | `sort [OPTIONS] [FILE]`         | Sort lines alphabetically            | `sort names.txt`                     |
| Remove duplicates        | `uniq [OPTIONS] [FILE]`         | Drop repeated lines                  | `sort file.txt                       | uniq` |
| Count lines/words/chars  | `wc [OPTIONS] [FILE]`           | Count lines, words, bytes            | `wc -l data.txt`                     |
| Search patterns          | `grep [OPTIONS] PATTERN [FILE]` | Search for matching lines            | `grep "error" log.txt`               |
| Merge files side-by-side | `paste [OPTIONS] FILE1 FILE2`   | Combine lines from files             | `paste names.txt ages.txt`           |
| Extract columns          | `cut [OPTIONS] [FILE]`          | Cut out fields or sections           | `cut -d":" -f1 /etc/passwd`          |
| Archive files            | `tar [OPTIONS] [FILES]`         | Combine files into one archive       | `tar -cvf logs.tar /var/log`         |
| Compress files           | `zip [OPTIONS] ARCHIVE FILES`   | Zip files into compressed archive    | `zip reports.zip *.txt`              |
| Unzip files              | `unzip [ARCHIVE]`               | Extract files from ZIP               | `unzip reports.zip`                  |

---

## 🌐 **Networking & Remote Data Retrieval**

| Command          | Syntax         | Description                             | Example                             |
| ---------------- | -------------- | --------------------------------------- | ----------------------------------- |
| Hostname         | `hostname`     | Show system network name                | `hostname`                          |
| Ping host        | `ping [HOST]`  | Test connectivity to a host             | `ping google.com`                   |
| IP configuration | `ip [OPTIONS]` | Configure or display network interfaces | `ip addr`                           |
| Download files   | `wget [URL]`   | Retrieve files from web                 | `wget https://example.com/file.txt` |
| Transfer data    | `curl [URL]`   | Transfer data using various protocols   | `curl ifconfig.me`                  |

---

## 💻 **Introduction to Shell Scripting**

### 🐚 Basic Script Setup

| Task            | Command               |
| --------------- | --------------------- |
| Shebang line    | `#!/bin/bash`         |
| Make executable | `chmod u+x script.sh` |
| Run script      | `./script.sh`         |

### 🧠 Variables and Input

| Task            | Command               |
| --------------- | --------------------- |
| Assign variable | `my_var="value"`      |
| Read input      | `read my_var`         |
| Export variable | `export MY_VAR=value` |
| List shell vars | `set`                 |
| List env vars   | `env`                 |

### 🔁 Pipes and Filters

| Task          | Command                            |
| ------------- | ---------------------------------- | --------- |
| Pipe output   | `command1                          | command2` |
| Chain filters | `cut -f1 file.csv \| sort \| uniq` |

### 🕒 Scheduling Jobs with Cron

| Task                       | Crontab Entry        |
| -------------------------- | -------------------- |
| Every minute               | `* * * * * command`  |
| Daily at 2 AM              | `0 2 * * * command`  |
| Weekly on Sunday at 6 PM   | `0 18 * * 0 command` |
| Monthly on 1st at midnight | `0 0 1 * * command`  |
| On boot                    | `@reboot command`    |

Example:

```bash
crontab -e
```

Add:

```bash
0 0 * * * /home/project/weather_script.sh >> /tmp/weather.log 2>&1
```

---

## 📊 Arrays and Loops in Bash

| Task            | Command                                           |
| --------------- | ------------------------------------------------- |
| Define array    | `my_array=(apple banana "pear juice")`            |
| Access element  | `${my_array[0]}`                                  |
| Loop over array | `for item in ${my_array[@]}; do echo $item; done` |
| Loop with index | `for i in {0..6}; do echo ${my_array[$i]}; done`  |
| Add to array    | `my_array+=("new_item")`                          |
| Get array size  | `${#my_array[@]}`                                 |

---

## 🧪 Conditional Logic and Arithmetic

| Feature             | Syntax                            |
| ------------------- | --------------------------------- |
| If condition        | `if [[ condition ]]; then ... fi` |
| Else clause         | `else`                            |
| Else if             | `elif [[ condition ]]; then ...`  |
| Logical AND         | `&&`                              |
| Logical OR          | `\|\|`                            |
| Equal to            | `-eq` or `==`                     |
| Less than           | `-lt`                             |
| Greater than        | `-gt`                             |
| Not equal           | `-ne`                             |
| Integer arithmetic  | `$((expression))`                 |
| Variable assignment | `result=$((3 + 2))`               |
| Negation            | `$(($result * -1))`               |

---

## 🛠️ Advanced Shell Scripting Features

| Feature              | Syntax                         |
| -------------------- | ------------------------------ |
| Quoting (literal)    | `'text'`                       |
| Quoting (expand)     | `"text"`                       |
| Escape character     | `\`                            |
| Output redirection   | `>` (overwrite), `>>` (append) |
| Input redirection    | `< file.txt`                   |
| Standard error       | `2>`, `2>>`                    |
| Command substitution | `$(command)`                   |
| Shebang line         | `#!/bin/bash`                  |

---

## 📂 **Common Crontab Tasks**

| Schedule                       | Syntax                                         |
| ------------------------------ | ---------------------------------------------- |
| Run daily at 8 AM              | `0 8 * * * /path/to/script.sh`                 |
| Run every Sunday at 6:15 PM    | `15 18 * * 0 date >> sundays.txt`              |
| Run first minute of each month | `1 0 * * * /scripts/monthly.sh`                |
| Run at system reboot           | `@reboot /scripts/startup.sh`                  |
| Backup home folder weekly      | `0 3 * * 1 tar -cvf /backup/home.tar.gz $HOME` |

---

## 🧩 Useful Examples

### Extract Today’s Forecasted vs Actual Temp:

```bash
yesterday_fc=$(tail -2 rx_poc.log | head -1 | cut -d " " -f5)
today_temp=$(tail -1 rx_poc.log | cut -d " " -f4)
accuracy=$(($yesterday_fc - $today_temp))
```

### Convert to Absolute Values:

```bash
for i in {0..6}; do
    if [[ ${week_fc[$i]} -lt 0 ]]; then
        week_fc[$i]=$(( -1 * ${week_fc[$i]} ))
    fi
done
```

### Find Min and Max:

```bash
minimum=${week_fc[0]}
maximum=${week_fc[0]}
for item in ${week_fc[@]}; do
    [[ $item -lt $minimum ]] && minimum=$item
    [[ $item -gt $maximum ]] && maximum=$item
done
```

---

## 🧠 Why This Matters

You're now capable of writing **automated, intelligent scripts** that:

- Fetch live data from the internet
- Parse and clean raw data
- Store structured logs
- Schedule recurring tasks
- Analyze performance and trends
- Build reusable automation workflows

These are real-world skills used by:

- DevOps engineers
- System administrators
- Data analysts
- Software developers

---

## 🚀 Next Steps

Would you like help with:

- **Final Project Guidance**
- **Visualizing Your Data with `gnuplot` or `matplotlib`**
- **Creating HTML or CSV Reports**
- **Advanced Bash Scripting Patterns**

Let me know — I'm here to help you finish strong and keep leveling up your **Linux automation skills**!

You're doing amazing work — keep going! 🐧💻📘📊✨

### USER

Task 1
Navigate to # [TASK 1] in the code.

Set two variables equal to the values of the first and second command line arguments, as follows:

Set targetDirectory to the first command line argument
Set destinationDirectory to the second command line argument
This task is meant to help with code readability.

Click here for Hint
The command line arguments interpreted by the script can be accessed via $1 (first argument) and $2 (second argument).

Take a screenshot of the code above and save it as 01-Set_Variables.jpg or .png.

Task 2
Display the values of the two command line arguments in the terminal.
Click here for Hint
Remember, you can use the command echo as a print command.

Example: echo "The year is $year"
Take a screenshot of the code above and save it as 02-Display_Values.jpg or .png.
Task 3
Define a variable called currentTS as the current timestamp, expressed in seconds.
Click here for Hint
Remember you can customize the output format of the date command.

To set a variable equal to the output of a command you can use command substitution: $() or ` `

For example: currentYear=$(date +%Y)
Take a screenshot of the code above and save it as 03-CurrentTS.jpg or .png.
Task 4
Define a variable called backupFileName to store the name of the archived and compressed backup file that the script will create.
The variable backupFileName should have the value "backup-[$currentTS].tar.gz"

For example, if currentTS has the value 1634571345, then backupFileName should have the value backup-1634571345.tar.gz.
Take a screenshot of the code above and save it as 04-Set_Value.jpg or .png.
Task 5
Define a variable called origAbsPath with the absolute path of the current directory as the variable's value.
Click here for Hint
You can get the absolute path of the current directory using the pwd command.

Take a screenshot of the code above and save it as 05-Define_Variable.jpg or .png.
Task 6
Define a variable called destAbsPath whose value equals the absolute path of the destination directory.
Click here for Hint
First use cd to go to destinationDirectory, then use the same method you used in Task 5.

Note: Please Note that you can also use the cd “destinationDirectory” || exit which ensures that if the specified directory is incorrect or inaccessible, the script will terminate immediately at this step. This acts as an implicit validation check to confirm that the correct directory is provided before proceeding with further operations. Follow the same for Task 7 .

Take a screenshot of the code above and save it as 06-Define_Variable.jpg or .png.

### ASSISTANT

# 🛠️ **Final Project Task Guide – Shell Scripting Basics**

Below is a clear, step-by-step explanation of how to complete each task in your script. These tasks are typically part of a Bash script that handles **file backups**, using command-line arguments and timestamps.

---

## 🔹 **Task 1: Set Variables from Command Line Arguments**

### Goal:

Set two variables:

- `targetDirectory` = first argument (`$1`)
- `destinationDirectory` = second argument (`$2`)

### ✅ Solution:

```bash
targetDirectory=$1
destinationDirectory=$2
```

This improves code readability by giving meaningful names to the input values.

📁 Example usage later:

```bash
./backup_script.sh /home/user/docs /home/user/backup
```

> 💡 Screenshot name: `01-Set_Variables.jpg` or `.png`

---

## 🔹 **Task 2: Display the Values of the Two Arguments**

### Goal:

Print the values of `targetDirectory` and `destinationDirectory` to verify they were passed correctly.

### ✅ Solution:

```bash
echo "Target Directory: $targetDirectory"
echo "Destination Directory: $destinationDirectory"
```

You can also use a single line:

```bash
echo "Target: $targetDirectory | Destination: $destinationDirectory"
```

> 💡 Screenshot name: `02-Display_Values.jpg` or `.png`

---

## 🔹 **Task 3: Define `currentTS` as Current Timestamp (in Seconds)**

### Goal:

Create a variable `currentTS` that holds the current time as a Unix timestamp (seconds since Jan 1, 1970).

### ✅ Solution:

```bash
currentTS=$(date +%s)
```

Or with backticks (legacy syntax):

```bash
currentTS=`date +%s`
```

This is useful for generating unique filenames like `backup-1634571345.tar.gz`.

> 💡 Screenshot name: `03-CurrentTS.jpg` or `.png`

---

## 🔹 **Task 4: Create `backupFileName` Using `currentTS`**

### Goal:

Define a variable called `backupFileName` with the format:

```
backup-[timestamp].tar.gz
```

### ✅ Solution:

```bash
backupFileName="backup-$currentTS.tar.gz"
```

This uses **variable interpolation** to build dynamic filenames.

Example output:

```
backup-1717582345.tar.gz
```

> 💡 Screenshot name: `04-Set_Value.jpg` or `.png`

---

## 🔹 **Task 5: Define `origAbsPath` as Absolute Path of Current Directory**

### Goal:

Store the full path of the current working directory in `origAbsPath`.

### ✅ Solution:

```bash
origAbsPath=$(pwd)
```

This helps preserve where you started the script from, which is important when changing directories during execution.

> 💡 Screenshot name: `05-Define_Variable.jpg` or `.png`

---

## 🔹 **Task 6: Define `destAbsPath` as Absolute Path of Destination Directory**

### Goal:

Go into the destination directory and get its absolute path.

### ✅ Solution:

```bash
cd "$destinationDirectory" || exit
destAbsPath=$(pwd)
```

The `|| exit` ensures the script stops if it cannot access the destination folder — an important safety check.

> 💡 Screenshot name: `06-Define_Variable.jpg` or `.png`

---

## ✅ Final Code Snapshot

Here's what your script should look like so far:

```bash
#!/bin/bash

# [TASK 1] Assign command line arguments
targetDirectory=$1
destinationDirectory=$2

# [TASK 2] Display values
echo "Target Directory: $targetDirectory"
echo "Destination Directory: $destinationDirectory"

# [TASK 3] Get current timestamp in seconds
currentTS=$(date +%s)

# [TASK 4] Build backup file name
backupFileName="backup-$currentTS.tar.gz"

# [TASK 5] Save original absolute path
origAbsPath=$(pwd)

# [TASK 6] Navigate to destination and save its path
cd "$destinationDirectory" || exit
destAbsPath=$(pwd)
```

---

## 📌 Summary Table

| Task | Variable               | Value                               |
| ---- | ---------------------- | ----------------------------------- |
| 1    | `targetDirectory`      | `$1`                                |
| 1    | `destinationDirectory` | `$2`                                |
| 2    | `echo`                 | Print both variables                |
| 3    | `currentTS`            | `$(date +%s)`                       |
| 4    | `backupFileName`       | `"backup-$currentTS.tar.gz"`        |
| 5    | `origAbsPath`          | `$(pwd)`                            |
| 6    | `destAbsPath`          | `cd "$destinationDirectory" && pwd` |

---

## 🧠 Why This Matters

These tasks form the foundation of any **automated backup script**:

- You’re capturing user input via **command-line arguments**
- Creating **unique archive names** with timestamps
- Working safely with **paths and directories**
- Ensuring scripts fail early on errors (e.g., bad paths)

---

Would you like help with:

- **Task 7 – Archiving and Compressing Files**
- **Task 8 – Moving Backup to Destination**
- **Creating Full Backup Scripts**

Let me know — I'm here to help you finish your project strong! 🐧💻📘✨

### USER

Task 7
Change directories from the current working directory to the target directory targetDirectory.
Click here for Hint
cd into the original directory origAbsPath and then cd into targetDirectory.

Take a screenshot of the code above and save it as 07-Change_Directory.jpg or .png.
Task 8
You need to find files that have been updated within the past 24 hours. This means you need to find all files whose last-modified date was 24 hours ago or less.

To do make this easier:

Define a numerical variable called yesterdayTS as the timestamp (in seconds) 24 hours prior to the current timestamp, currentTS.
Click here for Hint
Math can be done using $(()), for example:

zero=$((3 \* 5 - 6 - 9))
Thus, to get the timestamp in seconds of 24 hours in the future, you would use:

tomorrowTS=$(($currentTS + 24 _ 60 _ 60))
Take a screenshot of the code above and save it as 08-YesterdayTS.jpg or .png.

### ASSISTANT

# 🛠️ **Final Project Task Guide – Tasks 7 and 8**

Here's a clear breakdown of how to complete the next two tasks in your Bash script.

---

## 🔹 **Task 7: Change Directories to `targetDirectory`**

### Goal:

Navigate from the current working directory to the **target directory** provided as the first command-line argument (`$1`).

### ✅ Solution:

```bash
cd "$origAbsPath" || exit
cd "$targetDirectory" || exit
```

- `"$origAbsPath"` ensures you return to where the script started (from Task 5)
- Then you move into `"targetDirectory"` — the folder to be backed up
- The `|| exit` part ensures the script stops if it can't access the directory — this is a best practice for error handling

> 💡 Screenshot name: `07-Change_Directory.jpg` or `.png`

---

## 🔹 **Task 8: Define `yesterdayTS` as Timestamp from 24 Hours Ago**

### Goal:

Create a variable called `yesterdayTS` that holds the Unix timestamp for **24 hours before now**, using math inside the shell.

### ✅ Solution:

Since there are:

- 60 seconds in a minute
- 60 minutes in an hour
- 24 hours in a day

You can calculate yesterday’s timestamp like this:

```bash
yesterdayTS=$(($currentTS - 24 * 60 * 60))
```

Or more explicitly:

```bash
seconds_per_day=$((24 * 60 * 60))
yesterdayTS=$(($currentTS - $seconds_per_day))
```

This gives you a reference point to find files modified in the last 24 hours.

> 💡 Screenshot name: `08-YesterdayTS.jpg` or `.png`

---

## ✅ Final Code Snapshot

Here’s what your script should look like after completing **Tasks 7 and 8**:

```bash
#!/bin/bash

# [TASK 1]
targetDirectory=$1
destinationDirectory=$2

# [TASK 2]
echo "Target Directory: $targetDirectory"
echo "Destination Directory: $destinationDirectory"

# [TASK 3]
currentTS=$(date +%s)

# [TASK 4]
backupFileName="backup-$currentTS.tar.gz"

# [TASK 5]
origAbsPath=$(pwd)

# [TASK 6]
cd "$destinationDirectory" || exit
destAbsPath=$(pwd)

# [TASK 7]
cd "$origAbsPath" || exit
cd "$targetDirectory" || exit

# [TASK 8]
seconds_per_day=$((24 * 60 * 60))
yesterdayTS=$(($currentTS - $seconds_per_day))

# Optional: Print yesterdayTS to verify
echo "Yesterday TS: $yesterdayTS"
```

---

## 📋 Summary Table

| Task | Description                   | Command                                    |
| ---- | ----------------------------- | ------------------------------------------ |
| 7    | Change to target directory    | `cd "$origAbsPath"; cd "$targetDirectory"` |
| 8    | Compute yesterday's timestamp | `yesterdayTS=$(($currentTS - 24*60*60))`   |

---

## 🧠 Why This Matters

By completing these tasks, you're setting up your script to:

- Navigate safely between directories
- Work with **time-based file operations**
- Prepare for finding and archiving **recently modified files**

These are core skills used in:

- Backup scripts
- Log rotation tools
- File monitoring systems

---

Would you like help with:

- **Task 9 – Finding Files Modified in Last 24 Hours**
- **Task 10 – Creating Tar Archive**
- **Task 11 – Compressing and Moving Archive**

Let me know — I'm here to help you finish your project strong! 🐧💻📘✨

### USER

Note on arrays
In the script, you will notice the line:

1
declare -a toBackup

Copied!
This line declares a variable called toBackup, which is an array. An array contains a list of values, and you can append items to arrays using the following syntax:

1
myArray+=($myVariable)

Copied!
When you print or echo an array, you will see its string representation, which is simply all of its values separated by spaces:

1
2
3
4
5
6
$ declare -a myArray
$ myArray+=("Linux")
$ myArray+=("is")
$ myArray+=("cool!")
$ echo ${myArray[@]}
Linux is cool!

Copied!
This will be useful later in the script where you will pass the array $toBackup, consisting of the names of all files that need to be backed up, to the tar command. This will archive all files at once!

### ASSISTANT

# 📌 **Note on Arrays in Bash – Understanding `toBackup`**

In this part of your script, you're working with **Bash arrays**, which are used to store and manage a **list of files** that need to be backed up.

This is a key step in building **dynamic and flexible backup logic** in your script.

---

## 🔧 What You’re Doing

### 1. Declare an array:

```bash
declare -a toBackup
```

- This creates an empty array named `toBackup`
- The `-a` flag tells Bash it’s an **indexed array**
- Using `declare` makes your script more readable and maintainable

---

### 2. Append items to the array:

```bash
toBackup+=("filename.txt")
```

You can also add variables:

```bash
toBackup+=("$file")
```

Each time this line runs, it adds one more file to the list.

---

### 3. Use the array in commands:

When you use `${toBackup[@]}`, it expands into all elements of the array as separate arguments:

```bash
tar -cvf archive.tar "${toBackup[@]}"
```

This becomes:

```bash
tar -cvf archive.tar "file1.txt" "file2.txt" "file3.txt"
```

Perfect for archiving multiple files dynamically!

---

## 🧠 Why Arrays Are Useful in Your Script

| Purpose             | How It Helps                                                |
| ------------------- | ----------------------------------------------------------- |
| Store list of files | Collects only files modified in last 24 hours               |
| Pass dynamic lists  | Sends them directly to `tar` or other tools                 |
| Improve readability | Makes your code cleaner than using long command chains      |
| Enable flexibility  | Easily modify behavior later (e.g., filter by size or type) |

---

## 📝 Example: Building an Array from File List

Here's how you might fill the array:

```bash
for file in *; do
    if [[ $(date -r "$file" +%s) -gt $yesterdayTS ]]; then
        toBackup+=("$file")
    fi
done
```

Then echo the contents:

```bash
echo "Files to back up:"
echo "${toBackup[@]}"
```

This loop checks each file’s modification timestamp and adds recent ones to the `toBackup` array.

---

## ✅ Summary Table

| Task                 | Syntax                  |
| -------------------- | ----------------------- |
| Declare array        | `declare -a array_name` |
| Add item to array    | `array_name+=("item")`  |
| Access all elements  | `${array_name[@]}`      |
| Use array in command | `"${array_name[@]}"`    |
| Print array contents | `echo ${array_name[@]}` |

---

## 💡 Pro Tip

Always quote array expansions to handle filenames with spaces:

```bash
tar -cvf backup.tar "${toBackup[@]}"
```

Instead of:

```bash
tar -cvf backup.tar ${toBackup[@]}   # ❌ Risk of breaking on spaces
```

---

Great job understanding how **arrays work in Bash**!  
You're now ready to collect and pass a list of files to `tar`, which will allow you to build a smart and dynamic backup system.

Would you like help with:

- **Task 9 – Finding Files Modified in Last 24 Hours**
- **Task 10 – Creating Tar Archive from Array**
- **Task 11 – Compressing and Moving Backup**

Let me know — I'm here to guide you through the rest of your final project! 🐧💻📘✨

### USER

Task 12
After the for loop, compress and archive the files, using the $toBackup array of filenames, to a file with the name backupFileName.
Click here for Hint
Use tar -czvf $backupFileName ${toBackup[@]}.

Take a screenshot of the code above and save it as 12-Create_Backup.jpg or .png.
Task 13
Now the file $backupFileName is created in the current working directory.

Click here for Hint
Move the file backupFileName to the destination directory located at destAbsPath.

Take a screenshot of the code above and save it as 13-Move_Backup.jpg or .png.
Congratulations! You have now done the coding portion of the lab!

### ASSISTANT

# 🧰 Final Project – Task 12 & 13

## ✅ Create and Move the Backup Archive

Great job reaching this point! In these final scripting tasks, you learned how to:

- **Archive** a list of files using `tar`
- **Move** the backup file to the intended destination directory

This concludes the main coding portion of your Linux scripting project.

---

## 🔹 **Task 12: Compress and Archive Files Using `$toBackup`**

### Goal:

Use the array `toBackup` (which contains the list of files modified in the last 24 hours) to create a `.tar.gz` archive named using the variable `backupFileName`.

### ✅ Solution:

```bash
tar -czvf "$backupFileName" "${toBackup[@]}"
```

#### Breakdown:

| Flag | Meaning                         |
| ---- | ------------------------------- |
| `-c` | Create new archive              |
| `-z` | Compress with gzip              |
| `-v` | Verbose output (shows progress) |
| `-f` | Specify filename                |

> This creates a compressed archive like:

```
backup-1717580000.tar.gz
```

> 💡 Screenshot name: `12-Create_Backup.jpg` or `.png`

---

## 🔹 **Task 13: Move the Backup File to the Destination Directory**

### Goal:

Move the generated `.tar.gz` file to the destination directory stored in `destAbsPath`.

### ✅ Solution:

```bash
mv "$backupFileName" "$destAbsPath"
```

- `mv`: moves the file
- `"$backupFileName"`: the name of the backup file
- `"$destAbsPath"`: the full path where it should go

This ensures the backup ends up in the correct folder for safekeeping.

> 💡 Screenshot name: `13-Move_Backup.jpg` or `.png`

---

## ✅ Final Code Snapshot (Tasks 12–13)

Here's what your script might now include:

```bash
# [TASK 12] Create compressed archive from toBackup array
tar -czvf "$backupFileName" "${toBackup[@]}"

# [TASK 13] Move backup to destination directory
mv "$backupFileName" "$destAbsPath"
```

You’ve now built a script that:

- Accepts input directories via command-line arguments
- Captures current and past timestamps
- Finds recently modified files
- Builds a compressed backup
- Moves it to the target destination safely

---

## 📋 Summary Table

| Task | Description                | Command                                        |
| ---- | -------------------------- | ---------------------------------------------- |
| 12   | Create compressed backup   | `tar -czvf "$backupFileName" "${toBackup[@]}"` |
| 13   | Move backup to destination | `mv "$backupFileName" "$destAbsPath"`          |

---

## 🎉 Congratulations!

You've completed the **core scripting tasks** of your Linux shell scripting project.

You now have a working Bash script that automates:

- Input handling
- Timestamp calculations
- File discovery
- Archiving and compression
- Safe movement of backups

These are foundational skills used in real-world automation, system administration, and DevOps pipelines.

Would you like help with:

- **Testing Your Script**
- **Adding Logging or Email Notifications**
- **Final Touches Before Submission**

Let me know — I'm here to help you finish strong! 🐧💻📘📦✨

### USER

Task 14
Save the current working file backup.sh with CTRL+s [Windows/Linux], CMD+s [MAC] or by navigating to File->Save as seen below:

Download the file to your local computer by navigating to File->Download as seen below:

You may save the file as backup.sh

You will later submit this file will for peer-grading.
Task 15
Open a new terminal by clicking on the menu bar and selecting Terminal->New Terminal, as in the image below:

This will open a new terminal at the bottom of the screen as seen below:

Save the backup.sh file you're working on and make it executable.
Click here for Hint
Use the chmod command with the correct options.

Verify the file is executable using the ls command with the -l option:
1
ls -l backup.sh

Copied!
Take a screenshot of the output of the command above and save it as 15-executable.jpg or .png.
Task 16
Download the following .zip file with the wget command:
1
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/important-documents.zip

Copied!
Unzip the archive file:
1
unzip -DDo important-documents.zip

Copied!
Note: -DDo overwrites without restoring original modified date.

Update the file’s last-modified date to now:
1
touch important-documents/\*

Copied!
Test your script using the following command:
1
./backup.sh important-documents .

Copied!
This should have created a file called backup-[CURRENT_TIMESTAMP].tar.gz in your current directory.

Take a screenshot of the output of ls -l and save it as 16-backup-complete.jpg or .png.
Task 17
Copy the backup.sh script into the /usr/local/bin/ directory. (Do not use mv.)
Note: You may need to use sudo cp in order to create a file in /usr/local/bin/.

Test the cronjob to see if the backup script is getting triggered by scheduling it for every 1 minute.
Click here for Hint
1
_/1 _ \* \* \* /usr/local/bin/backup.sh /home/project/important-documents /home/project

Copied!
Please note that since the Theia Lab is a virtual environment, we need to explicitly start the cron service using the below command:
1
sudo service cron start

Copied!
Once the cron service is started, check in the directory /home/project to see if the .tar files are being created.

If they are, then stop the cron service using the below command, otherwise it will continue to create .tar files every minute:

1
sudo service cron stop

Copied!
Using crontab, schedule your /usr/local/bin/backup.sh script to backup the important-documents folder every 24 hours to the directory /home/project.

Take a screenshot of the output of crontab -l and save as 17-crontab.jpg or .png.

Tip: When you are setting up cron jobs in a real-life scenario, ensure the cron service is running, or start the cron service if needed.

### ASSISTANT

# 🧰 Final Project – Tasks 14 to 17

## ✅ Saving, Testing, and Scheduling Your Backup Script

In these final tasks, you:

- **Saved** your script for submission
- **Made it executable**
- **Tested it with sample files**
- **Scheduled it using `cron`**

These steps finalize your **Bash backup script project**, demonstrating real-world Linux scripting and automation skills.

---

## 🔹 **Task 14: Save and Download `backup.sh`**

### Goal:

Save your script and download it for peer review submission.

### ✅ Steps:

1. Save the file in Theia editor:

   - **Windows/Linux**: `CTRL + S`
   - **Mac**: `CMD + S`

2. Navigate to:

   - `File → Save` (to confirm changes are saved)

3. Then download via:
   - `File → Download`
   - Save as: `backup.sh` on your local machine

> 💡 Screenshot name: `14-Save_File.jpg` or `.png`

---

## 🔹 **Task 15: Make `backup.sh` Executable**

### Goal:

Ensure your script can be run like a command (`./backup.sh`).

### ✅ Solution:

```bash
chmod u+x backup.sh
```

Or for all users:

```bash
chmod +x backup.sh
```

#### Verify permissions:

```bash
ls -l backup.sh
```

Expected output:

```
-rwxr--r-- 1 user group ... backup.sh
```

> 💡 Screenshot name: `15-executable.jpg` or `.png`

---

## 🔹 **Task 16: Test Your Script**

### Step 1: Download and Extract Sample Files

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/important-documents.zip
unzip -DDo important-documents.zip
touch important-documents/*
```

- `-DDo`: Unzips files and overwrites without preserving original modification time
- `touch`: Updates timestamps so files appear "recently modified"

### Step 2: Run Your Script

```bash
./backup.sh important-documents .
```

This should generate a file like:

```
backup-1717580000.tar.gz
```

Verify it was created:

```bash
ls -l
```

> 💡 Screenshot name: `16-backup-complete.jpg` or `.png`

---

## 🔹 **Task 17: Copy Script to `/usr/local/bin/` and Schedule It with Cron**

### Step 1: Move Script to System Path

```bash
sudo cp backup.sh /usr/local/bin/
sudo chmod +x /usr/local/bin/backup.sh
```

Use `sudo` if you get permission denied errors.

---

### Step 2: Start the Cron Service

Since this is a lab environment:

```bash
sudo service cron start
```

---

### Step 3: Edit Crontab and Schedule Your Script

Open crontab:

```bash
crontab -e
```

Add the following line to schedule daily backups:

```bash
0 0 * * * /usr/local/bin/backup.sh /home/project/important-documents /home/project
```

Or for testing every minute:

```bash
*/1 * * * * /usr/local/bin/backup.sh /home/project/important-documents /home/project
```

After verifying that the script runs correctly, stop cron:

```bash
sudo service cron stop
```

To ensure no infinite backups are created.

---

### Step 4: Confirm Your Cron Job

List current jobs:

```bash
crontab -l
```

You should see:

```
*/1 * * * * /usr/local/bin/backup.sh /home/project/important-documents /home/project
```

> 💡 Screenshot name: `17-crontab.jpg` or `.png`

---

## ✅ Summary Table

| Task   | Description                | Command                                   |
| ------ | -------------------------- | ----------------------------------------- |
| 14     | Save script for submission | Use File > Save and Download              |
| 15     | Make script executable     | `chmod u+x backup.sh`                     |
| &nbsp; | Check file permissions     | `ls -l backup.sh`                         |
| 16     | Test with sample data      | `./backup.sh important-documents .`       |
| &nbsp; | Verify backup file         | `ls -l`                                   |
| 17     | Copy to system bin         | `sudo cp backup.sh /usr/local/bin/`       |
| &nbsp; | Schedule with cron         | `crontab -e`                              |
| &nbsp; | Daily at midnight          | `0 0 * * * /usr/local/bin/backup.sh args` |
| &nbsp; | List cron jobs             | `crontab -l`                              |

---

## 📦 Final Notes

Your script now:

- Accepts two command-line arguments:
  - Target directory
  - Destination directory
- Finds files modified in the last 24 hours
- Archives them into a timestamped `.tar.gz` file
- Moves the archive to the destination
- Can be scheduled using `cron` for automated backups

---

## 🧠 Why This Matters

You've built a full **Linux automation pipeline**:

- Learned how to write scripts that accept input
- Used arrays and loops to manage dynamic data
- Created compressed archives
- Scheduled recurring tasks using `cron`

These are foundational skills used by:

- DevOps engineers
- System administrators
- Automation developers
- Data engineers

---

Would you like help with:

- **Adding logging or error handling**
- **Visualizing your backups**
- **Writing a README for your submission**

Let me know — I'm here to help you finish strong and submit a polished script! 🐧💻📘📦✨
