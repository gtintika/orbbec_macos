# pyorbbecsdk-community 1.4.2 installation at macOS

## first install basic development tools 

[macOS development](../0 development.md)

## clone git repository

```sh
# assume parent folder is ~/projects
# choose any other
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/gtintika/orbbec_macos.git
```

## sync uv project

```sh
cd orbbec_macos/1start
uv sync
source .venv/bin/activate
```

## run examples

Always before examples, activate virtual environment

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





