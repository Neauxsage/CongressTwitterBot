import subprocess
import os

# Get the current script directory
current_script_dir = os.path.dirname(os.path.realpath(__file__))

# Define the scripts to run
scripts_to_run = [
    os.path.join(current_script_dir, 'bill.py'),
    os.path.join(current_script_dir, 'pdf.py'),
    os.path.join(current_script_dir, 'clearXL.py'),
    os.path.join(current_script_dir, 'del.py'),
    os.path.join(current_script_dir, 'test.py'),
]

# Run the scripts
for script in scripts_to_run:
    subprocess.check_call(['python3', script])
