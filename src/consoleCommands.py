import sys
from pathlib import Path

import pathing

class parser:
    def __init__(self):
        self.systemArguments = sys.argv
        self.address = ""
        self.file = ""

        self.findAddress() # address may be relative or other options


    def findAddress(self):
        for possibleAddress in self.systemArguments:
            print(f"{possibleAddress}")
            if Path.exists(Path(possibleAddress)):
                newPath = Path(possibleAddress)

                self.address = newPath.parent
                print(f"{newPath} detected")
                self.file = Path(newPath.name)
            else: pass

    def isAddressAbs(self):
        if Path.is_absolute(self.address):
            return True
        else:
            return False

    def importFromFile(self):
        pathing.addToPathStart(self.address)
        return self.file.stem
