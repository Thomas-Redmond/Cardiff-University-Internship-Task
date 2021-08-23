import sys
from pathlib import Path

class parser:
    def __init__(self):
        self.systemArguments = sys.argv
        self.address = ""

        self.findAddress() # address may be relative or other options


    def findAddress(self):
        for possibleAddress in self.systemArguments:
            if "/" in possibleAddress or "\" in possibleAddress:
                self.address = possibleAddress
                return
            else:
                pass

    def isAddressAbs(self):
        if Path.is_absolute(self.address):
            return True
        else:
            return False
