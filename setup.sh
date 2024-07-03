#!/bin/bash

# Update System
sudo apt update
sudo apt upgrade

# Install Python 
sudo apt install python3

# Install AWS-CLI
pip3 install awscli --upgrade --user

# Install Venv
python3 -m venv env
source env/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Deactivate Python virtual environment
deactivate

# Set execute permission for run.sh
chmod +x run.sh

# Create log directory if it doesn't exist
mkdir -p log

# Optional: Provide feedback that setup is complete
echo "Setup completed successfully."
