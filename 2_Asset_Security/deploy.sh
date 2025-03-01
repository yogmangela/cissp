#!/bin/bash

# Set up virtual environment
python3 -m venv autoclify_env
source autoclify_env/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Run the Flask app
python3 app.py