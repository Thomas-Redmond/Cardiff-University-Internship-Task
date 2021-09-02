from src.Errors.P703 import P703
from src.Errors.P704 import P704
from src.Errors.P709 import P709
from src.Errors.P710 import P710
from src.Errors.P711 import P711
from src.Errors.P712 import P712
from src.Errors.P720 import P720
from src.Errors.P799 import P799

from src.sysArgParser import parser

class Controller:

    def __init__(self, errorReporter):
        # pass Error_Reporter instance by reference
        # allows this class to utilise its functions
        self.errorRecord = errorReporter
        self.testsToRun = [
            P799,   # Special Case. Tests that required function names are used
                    # if failed, raises error and ends plugin run
            P703,   # Return answer from WinProbability as a number
            P704,   # Returned answer should not be rounded
            P709,   # Question asked for a different function name ('game')
            P710,   # Skip the header row in data.csv
            P711,   # Convert data.csv data tuples to numbers
            P712,   # Handle the extra column in data.csv
            P720    # Use the csv module
            ]

    def run(self):
        """
        For every test in self.sToRun create an instance and run that test.
        Errors will be recorded in the instance of Reporter passed to this class upon instantiation.
        """

        argumentParser = parser()           # checks whether Squash address has been given correctly
        Squash = argumentParser.Squash      # raises exception if not

        for test in self.testsToRun:
            try:
                instance = test(self.errorRecord)
                instance.run(Squash)
            except Exception as e:
                print(f"Unexpected Error {e}")
        return
