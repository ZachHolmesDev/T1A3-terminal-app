#!/bin/bash

# Set the name of the virtual environment
VENV_NAME="weather_CLI-venv"

# Check if the virtual environment exists, and create it if it doesn't
if [ ! -d "$VENV_NAME" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_NAME"
fi

# Activate the virtual environment
source "$VENV_NAME/bin/activate"

# Check if the requirements have been installed, and install them if they haven't
if [ ! -f "$VENV_NAME/requirements_installed" ]; then
    echo "Installing requirements..."
    pip3 install -r requirements.txt
    touch "$VENV_NAME/requirements_installed"
fi

# Run the Python script
python3 main.py
