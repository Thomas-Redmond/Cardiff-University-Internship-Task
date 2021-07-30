import Squash
import P703
import P704
import P709
import P710
import P711
import P712
import P719
import P720


class Controller:

    def __init__(self, errorReporter):
        # pass Error_Reporter instance by reference
        # allows this class to utilise its functions
        self._reportHere = errorReporter
        self._testsToRun = []

    def run(self):
        test_703 = P703(self._reportHere)
        test_703.run()
        errorReporter.displayRecord()


        return
