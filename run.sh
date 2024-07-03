#!/bin/bash

# Define logfile path
LOGFILE="log/run.log"

# Activate Python3 virtual environment
source env/bin/activate

# Run main.py script
echo "Starting script at $(date)" | tee -a $LOGFILE
python3 main.py >> $LOGFILE 2>&1

# Check if the Python script executed successfully
if [ $? -eq 0 ]; then
    echo "Script execution completed successfully."
else
    echo "Error: Script execution failed. See $LOGFILE for details."
fi

# Deactivate Python virtual environment
deactivate
