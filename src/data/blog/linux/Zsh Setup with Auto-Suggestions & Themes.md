---
title: Automate Your Zsh Setup- Scripted Installation of Oh My Zsh, Auto-Suggestions & Syntax Highlighting
pubDatetime: 2025-05-23
tags:
  - Hands On Lab
description: Ready for a smarter terminal? This guide provides a comprehensive shell script to completely automate the installation and configuration of Zsh as your default shell, set up Oh My Zsh, and integrate must-have plugins like zsh-autosuggestions and zsh-syntax-highlighting. Get a highly functional and beautiful command-line environment with minimal effort, simply by running a file.
---
Please save the following content into a file named `setup_zsh.sh` (or any .sh extension), then make it executable using chmod `+x setup_zsh.sh`, and run it with `./setup_zsh.sh`


# Only zsh (recommended)

```bash
#!/bin/bash

# Lightweight Zsh + Plugins + Git Prompt Setup Script

set -e

# === Functions ===
info() {
  echo -e "\n\033[1;32m==> $1\033[0m"
}

check_sudo() {
  if ! command -v sudo &>/dev/null; then
    echo "❌ sudo not found."
    exit 1
  fi
  if ! sudo -v &>/dev/null; then
    echo "❌ Sudo access required."
    exit 1
  fi
}

# === Begin ===
info "Checking sudo access..."
check_sudo

info "Installing zsh, git, curl..."
sudo apt update
sudo apt install -y zsh git curl

info "Setting zsh as default shell..."
if [[ "$SHELL" != *zsh ]]; then
  chsh -s "$(which zsh)"
  echo "✅ Zsh will be used next time you log in."
else
  echo "✅ Zsh is already the default shell."
fi

# === Plugin Setup ===
ZSH_PLUGIN_DIR="$HOME/.zsh/plugins"
mkdir -p "$ZSH_PLUGIN_DIR"

info "Installing zsh-autosuggestions..."
if [ ! -d "$ZSH_PLUGIN_DIR/zsh-autosuggestions" ]; then
  git clone https://github.com/zsh-users/zsh-autosuggestions "$ZSH_PLUGIN_DIR/zsh-autosuggestions"
else
  echo "zsh-autosuggestions already installed."
fi

info "Installing zsh-syntax-highlighting..."
if [ ! -d "$ZSH_PLUGIN_DIR/zsh-syntax-highlighting" ]; then
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$ZSH_PLUGIN_DIR/zsh-syntax-highlighting"
else
  echo "zsh-syntax-highlighting already installed."
fi

# === Generate .zshrc ===
ZSHRC="$HOME/.zshrc"
info "Writing ~/.zshrc..."

cat > "$ZSHRC" <<'EOF'
# === Git branch/status in prompt ===
autoload -Uz vcs_info
precmd() { vcs_info }
setopt prompt_subst

# Git status icons
zstyle ':vcs_info:*' enable git
zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:git:*' stagedstr '✔'
zstyle ':vcs_info:git:*' unstagedstr '✚'
zstyle ':vcs_info:git:*' untrackedstr '💥'
zstyle ':vcs_info:git:*' formats '(%b %u%c)'

# Show current dir and git info
PROMPT='%~ ${vcs_info_msg_0_}> '

# === Shell options ===
setopt autocd
setopt hist_expire_dups_first
setopt hist_ignore_space
setopt hist_verify

HISTFILE=~/.zsh_history
HISTSIZE=2000
SAVEHIST=4000

# === Autosuggestions ===
source $HOME/.zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#999999"
ZSH_AUTOSUGGEST_STRATEGY=(history completion)

# === Syntax Highlighting ===
source $HOME/.zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern)

# === Environment ===
export EDITOR="vim"
export PATH="$HOME/.local/bin:$PATH"
EOF

# === Done ===
info "✅ Zsh minimal setup complete."
echo -e "\n🎯 Run \033[1mzsh\033[0m or restart your terminal to start using Zsh."
```

# zsh + Oh My Zsh


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

-----


