import ast
from Errors.P700 import P700
from Errors.P701 import P701
from Errors.P702 import P702
from Errors.P705 import P705
from Errors.P713 import P713
from Errors.P714 import P714
from Errors.P717 import P717
from Errors.P716 import P716
from Errors.P718 import P718


class Router(ast.NodeVisitor):

    def __init__(self, errorReporter):
        # Takes instance of Error_Reporter passed by reference
        # To pass information by reference at later stages
        self._errorRecord = errorReporter

    def visit_FunctionDef(self, node):
        if node.name == 'game':
            P700_runTest = P700(self._errorRecord, node)

        elif node.name == 'q1a':
            P702_runTest = P702(self._errorRecord, node)

        elif node.name == 'readCSV':
            P705_runTest = P705(self._errorRecord, node)

        elif node.name == 'plotWinProbabilities':
            P713_runTest = P713(self._errorRecord, node)
            P714_runTest = P714(self._errorRecord, node)
            P716_runTest = P716(self._errorRecord, node)
            P718_runTest = P718(self._errorRecord, node)

        elif node.name == 'winProbability':
            P701_runTest = P701(self._errorRecord, node)
            P717_runTest = P717(self._errorRecord, node)

        else: pass
        self.generic_visit(node)
