#! /bin/sh

cd ~/transmission-helper # Directory must be in the home directory
source venv/bin/activate # Virtual environment must be called venv
python main.py >> log 2>&1 & # Logging for debugging the program
deactivate
