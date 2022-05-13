from src.sysArgParser import parser
import csv
from pathlib import Path

class TestCases:

    def __init__(self, errorReporter):
        # pass Error_Reporter instance by reference
        # allows this class to utilise its functions

        self.errorRecord = errorReporter
        self.testData = []
        with open(Path("src/Errors/testData/unitTesting.csv"), newline='') as testFile:
            reader = csv.reader(testFile, delimiter=',')
            for row in reader:
                # testID, in, out

                testID = row[0]     # Get id of test
                testType = row[1]   # Get type of test allowed values: type, value
                func = row[2]       # Get function to test

                input = row[-2]
                if len(input) == 0:
                    input = None
                elif input[0] == "[":
                    # input designated as list
                    input = self.parseMultipleValues(input[1:-1])

                else:
                    input = self.parseSingleValue(input)

                # Get outputs from data
                # Maximum of one only, if no output expected value recieved should be None
                output = row[-1]
                if len(output) == 0:
                    output = None
                elif output[0] == "[":
                    # input designated as list
                    output = self.parseMultipleValues(output[1:-1])
                else:
                    output = self.parseSingleValue(output)

                self.testData.append([testID, testType, func, input, output])

        argumentParser = parser() # checks whether FileToTest address has been given correctly
        self.TestMe = argumentParser.FileToTest  # raises exception if not

    def parseSingleValue(self, inp):
        # If designated str remove ` char and return
        # Else cast to integer and return

        if inp[0] == "`":
            return inp[1:-1]
        else:
            return int(inp)

    def parseMultipleValues(self, inp):
        # Designated list type.
        # Lists can feature values either ints / strs / both


        v = []
        inp = inp.split(',')
        for value in inp:
            if len(value) == 0:
                v.append(None)
            else:
                v.append(self.parseSingleValue(value))

        return v

    def run(self):
        # For every test in self.sToRun create an instance and run that test.
        # Errors will be recorded in the instance of Reporter passed to this class upon instantiation.
        try:
            for test in self.testData:
                #try:
                # If input does not match expected output
                    errorCode = test[0]
                    type = test[1].lower()
                    func = test[2]
                    # can be easier to access from rear due to adding new variables in database
                    input = test[-2]
                    expected = test[-1]

                    func = getattr(self.TestMe, func) # use function name as passed in data

                    if type == 'value':
                        self.runValueTests(errorCode, func, input, expected)
                    elif type == 'type':
                        self.runTypeTests(errorCode, func, input, expected)
                    else:
                        print(f"{type} value not valid")

                #except Exception as e:
                #    print(f"There is a configuration fault with test {test[0]}")
                #    print(f"{e}")


                #if (self.TestMe.program(input) != expected):
                #    errorText = f"Input {type(input)} {input} Expected Output {type(expected)} {expected}"
                #    self.errorRecord.setRecord(-1, -1, errorCode + " : " + errorText)

        except Exception as e:
            print(f"{e}")

        return

    def runValueTests(self, errorCode, func, input, expected):
        # Run value type tests
        # If given multiple input values need to activate function to tests using *kwargs

        if func(input) != expected:
            errorText = f"Input {type(input)} {input} Expected Output {type(expected)} {expected}"
            self.errorRecord.setRecord(-1, -1, errorCode + " : " + errorText)

    def runTypeTests(self, errorCode, func, input, expected):
        # Run value type tests
        # If given multiple input values need to activate function to tests using *kwargs


        # Making sure expected type values have been written correctly
        if expected.lower() == 'list':
            expected = "<class 'list'>"

        elif expected.lower() == 'int':
            expected = "<class 'int'>"

        elif expected.lower() == 'None':
            expected = "<class 'NoneType'>"

        if str(type(func(input))) != expected:
            errorText = f"Input {input} Expected Output {expected}"
            self.errorRecord.setRecord(-1, -1, errorCode + " : " + errorText)
