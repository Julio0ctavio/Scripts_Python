import sys
import os
import subprocess

# Check the current name of the parameters with the full path:
print(sys.argv)

# Differences between raw_input & input: https://es.stackoverflow.com/questions/38288/diferencia-entre-input-y-raw-input

# Call subprocess module to the following features:
# Linux: subprocess.run(["date"])
# Windows:
subprocess.run(["python", "--version"])

# See what we have in the current directory:
current_dir = os.listdir()
print(current_dir)

# More info about subprocess: https://docs.python.org/3/library/subprocess.html
