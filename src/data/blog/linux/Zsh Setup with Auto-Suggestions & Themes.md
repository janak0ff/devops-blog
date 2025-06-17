---
title: Automate Your Zsh Setup- Scripted Installation of Oh My Zsh, Auto-Suggestions & Syntax Highlighting
pubDatetime: 2025-05-23
tags:
  - Hands On Lab
description: Ready for a smarter terminal? This guide provides a comprehensive shell script to completely automate the installation and configuration of Zsh as your default shell, set up Oh My Zsh, and integrate must-have plugins like zsh-autosuggestions and zsh-syntax-highlighting. Get a highly functional and beautiful command-line environment with minimal effort, simply by running a file.
---

# Method 1: Fully automation with .sh file

Please save the following content into a file named `setup_zsh.sh` (or any .sh extension), then make it executable using chmod `+x setup_zsh.sh`, and run it with `./setup_zsh.sh`

```bash
#!/bin/bash
# This script automates the installation and configuration of Zsh,
# Oh My Zsh, and essential plugins like zsh-autosuggestions and
# zsh-syntax-highlighting on Ubuntu-based systems.
# This version keeps the default Oh My Zsh theme.

# Exit immediately if a command exits with a non-zero status.
set -e

# Function to check for sudo privileges
check_sudo() {
    if ! command -v sudo &> /dev/null; then
        echo "Error: sudo is not installed. Please install sudo or run as root."
        exit 1
    fi
    if ! sudo -v &> /dev/null; then
        echo "Error: This script requires sudo privileges. Please enter your password when prompted."
        exit 1
    fi
}

# Function to display messages
display_message() {
    echo -e "\n========================================"
    echo "$1"
    echo "========================================\n"
}

# Main script execution
display_message "Starting Zsh setup..."
check_sudo

# 1. Update package lists and install Zsh, Git, and Curl
display_message "Updating package lists and installing Zsh, Git, and Curl..."
sudo apt update
sudo apt install zsh git curl -y

# 2. Make Zsh your default shell
display_message "Setting Zsh as your default shell..."
if [ "$(basename "$SHELL")" = "zsh" ]; then
    echo "Zsh is already your default shell."
else
    chsh -s "$(which zsh)"
    echo "Zsh has been set as your default shell. Please log out and log back in (or restart your terminal) for this change to take effect."
fi

# 3. Install Oh My Zsh
display_message "Installing Oh My Zsh..."
if [ -d "$HOME/.oh-my-zsh" ]; then
    echo "Oh My Zsh is already installed. Skipping installation."
else
    # Install Oh My Zsh silently if it's not already installed
    # The 'RUNZSH=no' environment variable prevents it from immediately switching to zsh after installation.
    # The 'CHSH=no' environment variable prevents it from trying to change the default shell again.
    sh -c "$(RUNZSH=no CHSH=no curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
fi

# Set ZSH_CUSTOM variable (used by Oh My Zsh for custom plugins/themes)
ZSH_CUSTOM=${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}
mkdir -p "$ZSH_CUSTOM/plugins" # Ensure plugins directory exists

# 4. Install and Configure zsh-autosuggestions and zsh-syntax-highlighting
display_message "Installing zsh-autosuggestions and zsh-syntax-highlighting plugins..."

# Clone zsh-autosuggestions
if [ -d "${ZSH_CUSTOM}/plugins/zsh-autosuggestions" ]; then
    echo "zsh-autosuggestions plugin already cloned. Skipping."
else
    git clone https://github.com/zsh-users/zsh-autosuggestions "${ZSH_CUSTOM}/plugins/zsh-autosuggestions"
fi

# Clone zsh-syntax-highlighting
if [ -d "${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting" ]; then
    echo "zsh-syntax-highlighting plugin already cloned. Skipping."
else
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting"
fi

# Enable plugins in .zshrc
display_message "Enabling plugins in ~/.zshrc..."
# Check if plugins line exists
if grep -q "^plugins=(" "$HOME/.zshrc"; then
    # Add zsh-autosuggestions if not already in plugins
    if ! grep -q "zsh-autosuggestions" "$HOME/.zshrc"; then
        sed -i '/^plugins=(/ s/)$/ zsh-autosuggestions)/' "$HOME/.zshrc"
        echo "Added zsh-autosuggestions to plugins."
    else
        echo "zsh-autosuggestions already enabled."
    fi

    # Add zsh-syntax-highlighting if not already in plugins
    if ! grep -q "zsh-syntax-highlighting" "$HOME/.zshrc"; then
        sed -i '/^plugins=(/ s/)$/ zsh-syntax-highlighting)/' "$HOME/.zshrc"
        echo "Added zsh-syntax-highlighting to plugins."
    else
        echo "zsh-syntax-highlighting already enabled."
    fi
else
    echo "Warning: 'plugins=(...)' line not found in ~/.zshrc. Please add 'plugins=(git zsh-autosuggestions zsh-syntax-highlighting)' manually."
fi

# Ensure ZSH_THEME is set to robbyrussell if it's not already
display_message "Ensuring ZSH_THEME is set to 'robbyrussell'..."
if grep -q "^ZSH_THEME=" "$HOME/.zshrc"; then
    sed -i "s/^ZSH_THEME=\".*\"/ZSH_THEME=\"robbyrussell\"/" "$HOME/.zshrc"
else
    echo "ZSH_THEME=\"robbyrussell\"" >> "$HOME/.zshrc"
fi
echo "ZSH_THEME is set to: robbyrussell"


# 5. Reload your Zsh configuration
display_message "Reloading Zsh configuration..."
source "$HOME/.zshrc"
echo "Zsh configuration reloaded."

display_message "Zsh setup complete!"

# Post-setup instructions
echo "------------------------------------------------------------------"
echo "Next Steps:"
echo "1. If Zsh was not your default shell before, please LOG OUT and LOG BACK IN (or restart your terminal application) for the change to take full effect."
echo "2. If you ever want to change the theme later:"
echo "   - Open ~/.zshrc with 'nano ~/.zshrc'"
echo "     Find the line 'ZSH_THEME=\"robbyrussell\"' and change it to your desired theme name."
echo "   - Save the file and run 'source ~/.zshrc' or restart your terminal."
echo "   - You can browse themes at: https://github.com/ohmyzsh/ohmyzsh/wiki/Themes"
echo "------------------------------------------------------------------"
```

After the Script Runs: restart your terminal or run `source ~/.zshrc` to apply changes.


# Method 2: Manually Step by step

### Install Zsh

```bash
sudo apt update
sudo apt install zsh
```

-----

###  Make Zsh your default shell

```bash
chsh -s $(which zsh)
```

-----

###  Install Oh My Zsh 

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```


-----

### Install and Configure `zsh-autosuggestions, syntax-highlighting` 

Now let's install the `zsh-autosuggestions` plugin, which provides command auto-suggestion based on your history.

1.  **Clone the plugin repository:**

    ```bash
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    ```

     ```bash
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    ```


2.  **Enable the plugin in your `.zshrc` file:**
    Open your `~/.zshrc` file using a text editor (e.g., `nano`, `vim`, `code`):

    ```bash
    nano ~/.zshrc
    ```

    Find the line that starts with `plugins=(...)`. By default, it usually looks something like `plugins=(git)`.

    Add `zsh-autosuggestions and  syntax-highlighting` to the list of plugins. It should look like this:

    ```bash
    plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
    ```

    You can add other plugins later as you discover them.


3.  **Find Available Themes (Optional)**

Oh My Zsh has a dedicated wiki page listing all its built-in themes with screenshots. This is the best place to browse and see what they look like:

* **Oh My Zsh Themes Wiki:** [https://github.com/ohmyzsh/ohmyzsh/wiki/Themes](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)

You can also find them locally in your system:
```bash
ls ~/.oh-my-zsh/themes/*.zsh-theme
```
This command will list all the theme files, but it won't show you previews. The wiki page is much more useful for selection.

Some popular themes include:
* `agnoster` (requires a Powerline-compatible font)
* `pure` (not built-in to OMZ, but a popular standalone)
* `powerlevel10k` (not built-in to OMZ, but the most popular and customizable theme, also requires a Powerline-compatible font)
* `robbyrussell` (the default Oh My Zsh theme)
* `ys`
* `muse`


*  Look for the line that starts with `ZSH_THEME=`. By default, it's usually set to `robbyrussell`:
    ```bash
    ZSH_THEME="robbyrussell"
    ```

* Change the value inside the double quotes (`""`) to the name of the theme you want to try. For example, if you want to try the `agnoster` theme:
    ```bash
    ZSH_THEME="agnoster"
    ```
*    **Important Note for `agnoster` and `powerlevel10k`:** These themes use special characters (like arrows and icons) that require a "Powerline-compatible font" to display correctly. If you switch to them and see strange question marks or broken symbols, you'll need to install a font like `MesloLGS NF` (recommended for `powerlevel10k`) or any other Powerline font (e.g., from [Nerd Fonts](https://www.nerdfonts.com/)). After installing the font, you'll also need to configure your terminal emulator (e.g., iTerm2, Kitty, Alacritty, GNOME Terminal, etc.) to use that font.


  
###  Save and exit the `.zshrc` file.

-----

###   Reload your Zsh configuration

For the changes to take effect, you need to reload your `~/.zshrc` file.

```bash
source ~/.zshrc
```

-----


