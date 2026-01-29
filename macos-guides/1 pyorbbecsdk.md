# Install pyorbbecsdk-community at macOS

[pyorbbecsdk-community 1.4.2](https://pypi.org/project/pyorbbecsdk-community)

```sh
mkdir -p ~/projects/orbbec/1start
cd ~/projects/orbbec/1start
uv init
uv python install 3.12
uv venv --python 3.12

# always before we run python script
source .venv/bin/activate

uv pip install -U pip setuptools wheel

brew install libusb

uv add pyorbbecsdk-community==1.4.2
```
