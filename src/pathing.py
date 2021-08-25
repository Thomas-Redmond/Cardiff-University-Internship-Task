import sys
from pathlib import Path

def addToPathStart(address):
    try:
        sys.path.insert(0, address) # Add address to start of path
        print(f"Added file location {address} to Path")
    except Exception as e:
        raise Warning(f"Failure to add {address} to Path")

def addToPath(address):
    try:
        sys.path.append(address) # Add address to end of path
        print(f"Added file location {address} to Path")
    except Exception as e:
        raise Warning(f"Failure to add {address} to Path")
