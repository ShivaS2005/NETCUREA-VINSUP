#!/bin/bash
echo "Starting NETCUREA application..."
echo "Current directory: $(pwd)"
echo "Files in current directory:"
ls -la
echo "Looking for app.py..."
find . -name "app.py" -type f
echo "Starting Python app..."
python app.py
