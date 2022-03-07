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

        # Search Errors subfolder and grab files with 'u'.
        # Import each file, and append to self.testsToRun

        self.errorRecord = errorReporter
        self.testsToRun = [

            RP01u06,    # Recommended Function names are not in use
            RP01u07,    # Check Output is [9, 4, 7, 2] given input '9J4B72q'
            RP01u08,    # Check Output is type list given GOOD input
            RP01u09,    # Check Output is type int given bad input
            RP01u10,    # Check Output is -1 given bad input
            RP01u11,    # Bad if -1 on input of 1
            RP01u12     # Bad if -1 on input of '1'
            ]

    def run(self):

        # For every test in self.sToRun create an instance and run that test.
        # Errors will be recorded in the instance of Reporter passed to this class upon instantiation.

        argumentParser = parser()           # checks whether TestThisFile address has been given correctly
        TestThisFile = argumentParser.TestThisFile      # raises exception if not

        for test in self.testsToRun:
            try:
                instance = test(self.errorRecord)
                instance.run(TestThisFile)
            except Exception as e:
                print(f"Unexpected Error {e}")
        return
