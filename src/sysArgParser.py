import sys

from pathlib import Path


class parser:
    # Handles system arguments
    # Such as importing FileToTest from path given by user

    def __init__(self):
        self.filename = self.getFilenameFromSysArg() # Get address of FileToTest given by user in command line
        self.FileToTest = __import__(self.importModule(self.filename)) # Import File to Test and store


    def getFilenameFromSysArg(self):
        # Take 2nd parameter of Flake8 console command
        # Confirm para is ABSOLUTE file address
        # Otherwise trigger user warning

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
