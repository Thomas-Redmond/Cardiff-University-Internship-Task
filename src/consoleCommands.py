import sys
from pathlib import Path

class parser:
    def __init__(self):
        self.systemArguments = sys.argv
        self.address = ""

        self.findAddress() # address may be relative or other options


    def findAddress(self):
        for possibleAddress in self.systemArguments:
            if Path.exists(Path(possibleAddress)):
                self.address = Path(possibleAddress)
            else: pass

    def isAddressAbs(self):
        if Path.is_absolute(self.address):
            return True
        else:
            return False
