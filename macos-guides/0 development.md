# Install Basic Development Tools at macOS

## Install Visual Studio Code (vsc)

[Download Visual Studio Code](https://code.visualstudio.com/)

### Install vsc plugins

Click `Extensions` icon at Left Side Icon Bar

Install next extensions :  

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager)
- [Numbered Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.numbered-bookmarks)
- 
- [Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack)
- [Black FormatterPreview](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) 
- [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

- [Codex – OpenAI’s coding agent](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)
- [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)
- [Gemini Code Assist](https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist)

You need to sign at OpenAI ChatGPT.  
Click the Codex icon at Left Side Icon Bar.  
Then click the Settings icon at top for CODEX plugin.   
Click `Log out` or `Log in` menu.  


`Codex` will be available from the `ChatGPT` icon at Icon Left Bar. 

`Copilot Chat` will be available from the `Chat` icon at right of the top bar where the current folder is shown.

`Copilot Chat` needs to login to a github account using the `User` icon at left Icom Bar.   


### VSC Keyboard Shortcuts

[vsc keyboard for MacOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf).  
[vsc keyboard for Linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)

Must use keys:

- `shift` + `cmd` + P or `F1` : Show Command Palette
- `cmd` + `P` : Quick Open, Go to File…    
(type any part of the filename you want to edit)
- `cmd` + `B` : Show/Hide Sidebar
- `cmd` + `J`  or `ctrl` + ` : Show integrated terminal
- `cmd` + `K` `Z` : Zen Mode    
press `esc` `esc` to exit


### How to view `markdown` files (extension .md) properly at vsc

Open markdown (md) file at vsc

`shift` + `cmd` + `V` : Open Markdown preview

`cmd` + `K`  `V` : Open Markdown preview to the side


## Install Homebrew (brew) package manager 

[brew](https://brew.sh/)

Run MacOS `Terminal` application :

Run SpotLight with `cmd` `enter`

Type `Terminal`

copy/paste next line to `Terminal` and press `enter` to apply command

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

it will ask your password at MacOS to install the brew at specific protected directories

Type your password (will be hidden) and press `enter`

### Install Basic brew Packages

```shell
brew install python3

# verify python3 installation

python3 -V
```

```shell
brew install zoxide

echo 'eval "$(zoxide init zsh)"' >> ~/.zshrc
```

Start a new terminal session (close Terminal App & restart it)

now instead of use `cd` to go to an existing folder just give


```shell
# mkdir folder_name
# cd folder_name
#
# folder_name added at db
# 
# z folder_name 
# or
# z part_of_folder_name

# we have to cd at least once at folder folder_name and then we use z folder_name
```

```shell
brew install fd

# fdfind: finds a file at current folder by giving part of the filename
```

```shell
brew install uv

# uv: python package manager & virtual env
```


How to upgrade `brew` and brew packages

```shell

# update brew itshel
brew update

# upgrade a package or all packages
brew upgrade python3

brew upgrade

```

How to list `brew` installed packages

```shell
brew list

# get info for a package

brew info python3
```

### Select Python Interpreter at vsc

After you installed `python3` with brew.  

at vsc:

Type `F1` key.    
Type `Python Select Interpreter`


Choose python version which is marked as `Recommended` or `Workspace` by `vsc`
usually .venv/bin.python3 when current folder is a uv project

Now when you have open a python file at `vsc` editor you can run it at vsc's `Integrated Terminal` :

Click icon symbol like a `play` button which corresponds to `vsc` command `Run Python File`    
at right side of the File Bar at top of `vsc`


### install zsh / ohmyzsh

replace bash with zsh

[zsh](https://en.wikipedia.org/wiki/Z_shell)

#### install zsh & git

zsh is already the default shell at macOS after Catalina,
so no need to install with brew

```shell
brew install git
```
#### install ohmyz 

[ohmyz](https://ohmyz.sh/)

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
Start a new terminal session (close Terminal App & restart it)

Optional but very common) change theme

change next line at `~/.zshrc`

```
ZSH_THEME="robbyrussell"
```

with the theme you preffer from

[ohmyzsh themes](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)

### install next plugins for ohmyzsh

### zsh-autosuggestions
[zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)

Clone this repository into $ZSH_CUSTOM/plugins (by default ~/.oh-my-zsh/custom/plugins)

```
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

Add the plugin to the list of plugins for Oh My Zsh to load (inside ~/.zshrc):

```
plugins=( 
  # other plugins...
  zsh-autosuggestions
)
```
Start a new terminal session (close Terminal App & restart it)

### zsh-completions

[zsh-completions](https://github.com/zsh-users/zsh-completions)


Clone the repository into your custom plugins directory:

```shell
git clone https://github.com/zsh-users/zsh-completions.git \
  ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions
```

Update your ~/.zshrc configuration with 1 line before sourcing oh-my-zsh:

```
fpath+=${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions/src

# before existing lines (do not add them)
autoload -U compinit && compinit
source "$ZSH/oh-my-zsh.sh"
```


### choose any other ohmyzsh plugin from

[ohmyzsh plugins](https://github.com/ohmyzsh/ohmyzsh/wiki/plugins)


