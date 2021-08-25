import sys

from pathlib import Path


class parser:
    # Handles system arguments
    # Such as importing Squash from path given by user

    def __init__(self):
        self.filename = Path(sys.argv[1]) # Get address of Squash given by user in command line
        self.Squash = __import__(self.importModule(self.filename)) # Import Squash and store

    def importModule(self, filename):
        # Presuming filename is complete address,
        # Adds parent directory to path and returns filename stem.
        # Raises ModuleNotFoundError otherwise
        if Path.exists(filename):
            sys.path.insert(0, str(filename.parent))
            return filename.stem
        else:
            raise ModuleNotFoundError(f"Address {filename} was not found")
