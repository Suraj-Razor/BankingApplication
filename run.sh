#!/bin/bash

if command -v python &>/dev/null; then
    python -m venv .venv
    source .venv/bin/activate
    pip3 install pandas prettytable pytest
    ./setup.sh
    python3 main.py  
else
    echo "Python is not detected, please install Python and try again."
fi