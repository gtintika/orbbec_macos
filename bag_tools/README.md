# Orbbec Bag Player & Recorder

Tools for recording and playing back Orbbec camera streams using `.bag` files.

> **Note (macOS):** Femto Mega and other UVC-class Orbbec cameras require `sudo` on macOS due to the `UVCAssistant` daemon holding exclusive access to UVC devices. Prefix commands with `sudo` if you get a device access error.

## Setup & Refresh for changes

```bash
cd ~/projects/orbbec_macos
git pull

cd bag_player

uv sync
# activate the virtual environment
source .venv/bin/activate
```

## Tools

### record_bag.py — Live viewer with recording

Opens the Orbbec camera, displays Color + Depth streams side-by-side, and allows recording to a `.bag` file.

```bash
sudo uv run record_bag.py
```

**Controls:**
| Key       | Action                                              |
|-----------|-----------------------------------------------------|
| `R`       | Start recording (saves to `YYYYMMDD_HHMMSS.bag`)   |
| `S`       | Stop recording                                      |
| `Q` / ESC | Quit                                                |

### play_bag.py — Play back a .bag file

Plays a recorded `.bag` file displaying Depth (colorized) and Color streams side-by-side.

```bash
uv run play_bag.py /path/to/file.bag
```

### inspect_bag.py — Inspect a .bag file

Prints diagnostic info about a `.bag` file: device metadata, stream formats, resolutions, and timestamps.

```bash
uv run inspect_bag.py /path/to/file.bag

# Read more framesets (default is 30):
uv run inspect_bag.py -n 100 /path/to/file.bag
```
