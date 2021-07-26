def ReturnIsNumber(variable):
    # Test Case 4
    # variable = winProbability(1, 1 )
    if variable.type() == "float" or variable.type() == "int":
        print("Success")
    else:
        print("Error")



############
def globalVars():
    # Test case 28
    if len(is_global) == 0:
        print("Success")
    else:
        print("Failure")

############
import sys
def IsModuleUsed(moduleName):
    # Test Case 30
    if moduleName not in sys.modules:
        print("Error")
    else:
        print("Success")
