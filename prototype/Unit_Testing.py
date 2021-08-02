import Squash
from P703 import P703 as P703_Test
from P704 import P704 as P704_Test
from P709 import P709 as P709_Test
from P710 import P710 as P710_Test
from P711 import P711 as P711_Test
from P712 import P712 as P712_Test
#from P719 import P719 as P719_Test
from P720 import P720 as P720_Test

class Controller:

    def __init__(self, errorReporter):
        # pass Error_Reporter instance by reference
        # allows this class to utilise its functions
        self._reportHere = errorReporter
        self._testsToRun = [
            P703_Test, P704_Test, P709_Test, P710_Test, P711_Test, P712_Test, P720_Test]

    def run(self):

        for test in self._testsToRun:
            instance = test(self._reportHere)
            instance.run()

        return
