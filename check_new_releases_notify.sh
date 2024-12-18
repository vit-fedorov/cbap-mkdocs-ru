#!/bin/bash

# Path to the Python script
PYTHON_SCRIPT_PATH="check_new_releases.py"

# Execute the Python script and capture the output
OUTPUT=$(python $PYTHON_SCRIPT_PATH)

# If the output contains any file names, send an email
if [[ ! -z "$OUTPUT" ]]; then
    echo -e "$OUTPUT" #| mail -s "New Files Found" email@example.com
fi