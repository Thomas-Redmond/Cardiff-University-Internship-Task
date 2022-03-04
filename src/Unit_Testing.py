#from src.Errors.P703 import P703
#from src.Errors.P704 import P704
#from src.Errors.P709 import P709
#from src.Errors.P710 import P710
#from src.Errors.P711 import P711
#from src.Errors.P712 import P712
#from src.Errors.P720 import P720
#from src.Errors.P721 import P721
#from src.Errors.P799 import P799

from src.sysArgParser import parser


class Controller:

    def __init__(self, errorReporter):
        # pass Error_Reporter instance by reference
        # allows this class to utilise its functions

        # Search Errors subfolder and grab files with 'u'.
        # Import each file, and append to self.testsToRun

        self.errorRecord = errorReporter
        self.testsToRun = [
            #P799,   # Special Case. Tests that required function names are used
                    # if failed, raises error and ends plugin run
            #P703,   # Return answer from WinProbability as a number
            #P704,   # Returned answer should not be rounded
            #P709,   # Question asked for a different function name ('game')
            #P710,   # Skip the header row in data.csv
            #P711,   # Convert data.csv data tuples to numbers
            #P712,   # Handle the extra column in data.csv
            #P720,   # Use the csv module
            #P721,   # Use the matplolib module

            #U000   # Special Case. Tests that require function names are used. If failed, will raise error and end plugin
            #U001   # Check Output is [9, 4, 7, 2] given input '9J4B72q'
            #U002   # Check Output is type list given GOOD input
            #U003   # Check Output is type int given bad input
            #U004   # Check Output is -1 given bad input

            # Tests for question part 2
            #U100   # Test 2 dimensional list GOOD input [["9J4B72q"]] expect [9, 4, 7, 2]
            #U101   # Test 2 dimensional list BAD input [[]] expect -1

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
