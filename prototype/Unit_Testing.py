import Squash
from PluginErrors import P703


class Controller:

    def __init__(self, errorReporter):
        # pass Error_Reporter instance by reference
        # allows this class to utilise its functions
        self._reportHere = errorReporter
        self._testsToRun = []

    def run(self):
        P703.run()
        return
