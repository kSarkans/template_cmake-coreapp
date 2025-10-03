#!/usr/bin/env python

from pathlib import Path
import os

launch_json_base = """{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
    {
        "type": "lldb",
        "request": "launch",
        "name": "Launch",
        "program": "${workspaceFolder}/build/target/Debug-Linux/exapp",
        "args": [],
        "cwd": "${workspaceFolder}",
        "console": "externalTerminal",
        "env": {
            "TERM": "xterm-256color"
        },
        "preLaunchTask": "CMake: build"
    }
    ]
}
"""

if not os.path.isdir(".vscode"):
    os.mkdir(".vscode")
if not os.path.isfile(".vscode/launch.json"):
    launch_json_f = open(".vscode/launch.json", "x")
else:
    launch_json_f = open(".vscode/launch.json", "w")
launch_json_f.write(launch_json_base)
launch_json_f.close()