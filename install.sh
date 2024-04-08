#!/bin/sh

python3 -m venv venv --system-site-packages
source venv/bin/activate
python3 install.py