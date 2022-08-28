# pyvlive

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vlive?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/kvdomingo/pyvlive?style=for-the-badge)
![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/kvdomingo/pyvlive?include_prereleases&style=for-the-badge)

This is a WIP Python wrapper for the open (unofficial) VLIVE API.

## Installation
```shell
# pip
pip install vlive

# poetry
poetry add vlive 
```

## Usage

```python
import vlive

vlive.search.channels("twice")
```

Output:
```shell
> [Channel(name="TWICE", code="EBDF", icon="...", type="...")]
```