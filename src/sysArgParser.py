import sys

from pathlib import Path


class parser:
    # Handles system arguments
    # Such as importing Squash from path given by user

    def __init__(self):
        self.filename = self.getFilenameFromSysArg() # Get address of Squash given by user in command line
        self.Squash = __import__(self.importModule(self.filename)) # Import Squash and store


    def getFilenameFromSysArg(self):
        try:
            for parameter in sys.argv[1:]: # skip flake8 command
                if Path(parameter).exists():
                    return Path(parameter)
                else:
                    pass

            raise UserWarning()

        except UserWarning as e:
            raise UserWarning(f"No valid files were given") # exception should always be raised
        except Exception as e:
            print(e)


    def importModule(self, filename):
        # Presuming filename is complete address,
        # Adds parent directory to path and returns filename stem.
        # Raises ModuleNotFoundError otherwise
        if Path.exists(filename):
            sys.path.insert(0, str(filename.parent))
            return filename.stem
        else:
            raise ModuleNotFoundError(f"Address {filename} was not found")
