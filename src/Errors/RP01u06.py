from src.Errors.errorType import basicError

class RP01u06(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "RP01u06"
        self.errorText = "Recommended Function names not in use"

    def run(self, TestThisFile):
        """
        Tests that function names used in other tests are available
        """
        try:
            listOfFuncs = [
            "program"
            ]
            for funcName in listOfFuncs:
                if funcName not in dir(TestThisFile):
                    self.fail()
                    return

        except Exception as e:
            print(e)
            self.fail()
