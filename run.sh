#! /bin/bash

python3 -m venv weather_CLI-venv
source weather_CLI-venv/bin/activate
pip3 install -r requirements.txt
python3 T1A3_Weather_CLI.py