# pyorbbecsdk-community 1.4.2 installation at macOS

## first install basic development tools 

to install python & uv package manager

[macos prepare development](https://github.com/gtintika/orbbec_macos/blob/main/macos-guides/0%20development.md)

## first time: clone git repository

Open Terminal app at macOS and copy paste:

```sh
# assume parent folder is ~/projects
# choose any other
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/gtintika/orbbec_macos.git
```

## each time to get changes: git pull

```sh
# assume parent folder is ~/projects
cd ~/projects/orbbec_macos
git pull
```

## sync uv project

```sh
cd orbbec_macos/1start
# pull from github changes
git pull
# install project dependencies
uv sync
# activate virtual environment
source .venv/bin/activate
```

## run examples

Always before examples, we should activate virtual environment
with command

**source .venv/bin/activate**

at terminal application

```sh
cd ~/projects/orbbec_macos/1start
source .venv/bin/activate
```

```sh
# basic hello program for pyorbbecsdk
python3 hello_orbbec.py

# print support profiles for device
python3 profiles.py

# Displays the color stream from the camera.
python3 color_viewer.py

# Displays the depth stream from the camera.
python3 depth_viewer.py

# Demonstrates how to synchronize the depth and color streams.
python3 depth_color_sync_align_viewer.py

```

## deactive project venv

```
deactivate
cd 
```





