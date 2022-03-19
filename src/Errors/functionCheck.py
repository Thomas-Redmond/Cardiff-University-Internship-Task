from src.sysArgParser import parser

class funcCheck:

    # Checks if required function names for all the various tests are in use
    # To avoid a deluge of error messages all saying the same thing

    def __init__(self, errorReporter):
        self.errorRecord = errorReporter
        self.activated = False
        self.errorCode = "RP01f"

        argumentParser = parser()
        FileToTest = argumentParser.FileToTest

        try:
            listOfFuncs = [
            "program",
            "parseList",
            "parseStr",
            "parseInt"
            ]

            for funcName in listOfFuncs:
                if funcName not in dir(FileToTest):
                    errorText = f"Function {funcName} not found"
                    self.errorRecord.setRecord(-1, -1, self.errorCode + " : " + errorText)
                    self.activated = True

        except Exception as e:
            print(e)
