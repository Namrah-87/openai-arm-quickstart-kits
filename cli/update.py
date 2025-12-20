# cli/update.py

import subprocess

def run_update():
    print("\n=== Updating ===")
    subprocess.run("git pull", shell=True)
    subprocess.run("pip install -r requirements.txt --upgrade", shell=True)
    print("Update complete.")
