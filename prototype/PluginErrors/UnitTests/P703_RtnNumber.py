"""

winProbability function must return number.
Positive result if Float / Integer returned.
Default = Fail

"""

from prototype import Squash # Relative import

try:
    variableReturned = Squash.winProbability()
    if variableReturned.type() == "float" or variableReturned.type() == "int":
        print("Success")
    else:
        print("Test Failed")

except:
    print("Unexpected Error")
