# Native RPC Communication Library Tooling

Cross-platform and cross-language communication library CLI tooling. Part of larger [Native RPC](https://github.com/nativerpc) framework. See [README.md](https://github.com/nativerpc/nrpc-examples) in nrpc-examples project for more information.

# Prerequisites

Configuring developer tooling on Ubuntu.

```
pip install setuptools
pip install build packaging
pip install pytest colorama ipython
```

Configuring developer tooling on Windows.

- Install CMake 3.31 (or older)
- Install Visual Studio Community 2022 (or older)

# Configuration and dependency build

Configuring and building dependencies.

```
cmake -B build
```

# Build and installation

Building and installing 'nrpc-cli' module globally.

```
pip install -e .
```

# Command line tools

Command line tools included in this project and registester globally:

- "show" - Shows network topolgy and examines the schema.
- "term" - Configures interactive terminal execution. Great for demoing.
- "killall" - Cleans up python and powershell processes.

tutorial video?

# Manual testing

Technologies utilized by this projects can be tested with the following scripts:

```
python test\test_zmq.py
python test\test_process.py
python test\test_data.py
pytest
etc
```


set PATH=%PATH%;C:\Users\aarep\AppData\Local\fnm_multishells\6076_1741378646135;C:\Users\aarep\AppData\Local\Microsoft\WinGet\Packages\Schniz.fnm_Microsoft.Winget.Source_8wekyb3d8bbwe
