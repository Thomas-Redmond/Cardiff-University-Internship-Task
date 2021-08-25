import sys
from pathlib import Path
try:
    # Tries to add system/address/to/src to path
    # Occurs after Linter imported by Flake8 Plugin Manager (prior to obj stuff)
    fileDirectory = Path(__file__).parent
    sys.path.insert(0, str(fileDirectory)) # add src folder to path
    print(f"{fileDirectory} added to Path")
except ModuleNotFoundError:
    print(f"Importing src files failed using path {fileDirectory}")
    print(f"Traceback {e}")
