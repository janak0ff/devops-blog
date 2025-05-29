---
title: Zsh Setup with Auto-Suggestions, Syntax-highlighting & Themes
pubDatetime: 2025-05-23
tags:
  - Hands On Lab
description: setting up Zsh, making it your default shell, and enhancing it with Oh My Zsh. install zsh-autosuggestions for smart command completion, zsh-syntax-highlighting for better readability, and easily customize your terminal's look with various Zsh themes.
---

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


