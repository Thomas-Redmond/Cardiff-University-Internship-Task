import sys
from pathlib import Path

class parser:
    def __init__(self):
        self.systemArguments = sys.argv
        self.address = ""

    def addressAcceptance(self):
        for possibleAddress in self.systemArguments:
            if Path.is_absolute(possibleAddress):
                self.address = possibleAddress
                return True
            else:
                return False
