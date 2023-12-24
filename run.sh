#!/bin/bash

if command -v python &>/dev/null; then
    python -m venv .venv
    source .venv/bin/activate
    pip3 install colored
    pip3 install pandas
    ./setup.sh
    python main.py
else
    echo "Python is not detected, please install python and try again."
fi
