from src.Errors.RP01u06 import RP01u06
from src.Errors.RP01u07 import RP01u07
from src.Errors.RP01u08 import RP01u08
from src.Errors.RP01u09 import RP01u09
from src.Errors.RP01u10 import RP01u10
from src.Errors.RP01u11 import RP01u11
from src.Errors.RP01u12 import RP01u12

from src.sysArgParser import parser

class Controller:

    def __init__(self, errorReporter):
        # pass Error_Reporter instance by reference
        # allows this class to utilise its functions

        self.errorRecord = errorReporter
        self.testsToRun = [
            RP01u06,
            RP01u07,
            RP01u08,
            RP01u09,
            RP01u10,
            RP01u11,
            RP01u12,
            ]

    def run(self):

        # For every test in self.sToRun create an instance and run that test.
        # Errors will be recorded in the instance of Reporter passed to this class upon instantiation.

        argumentParser = parser()           # checks whether Squash address has been given correctly
        Squash = argumentParser.Squash      # raises exception if not

        for test in self.testsToRun:
            try:
                instance = test(self.errorRecord)
                instance.run(Squash)
            except Exception as e:
                print(f"Unexpected Error {e}")
        return
