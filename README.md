# FPdb: A Forkable Python Debugger

A wrapper on python-pdb to debug forked child processes as well (multi-threaded and multi-processing code).

### Installation

```bash
pip install git+https://github.com/ra101/fpdb.py.git

# Install with other ratools.py utils.
pip install git+https://github.com/ra101/ratools.py.git
```

### Usage

```python
import fpdb
fpdb.set_trace()
```
