import ast
from src.Errors.P700 import P700
from src.Errors.P701 import P701
from src.Errors.P702 import P702
from src.Errors.P705 import P705
from src.Errors.P713 import P713
from src.Errors.P714 import P714
from src.Errors.P717 import P717
from src.Errors.P716 import P716
from src.Errors.P718 import P718
from src.Errors.P719 import P719


class Router(ast.NodeVisitor):

    def __init__(self, errorReporter):
        # Takes instance of Error_Reporter passed by reference
        # To pass information by reference at later stages
        self.errorRecord = errorReporter

    def visit_Global(self, node):
        P719_runTest = P719(self.errorRecord, node)


    def visit_FunctionDef(self, node):
        if node.name == 'game':
            P700_runTest = P700(self.errorRecord, node)

        elif node.name == 'q1a':
            P702_runTest = P702(self.errorRecord, node)

        elif node.name == 'readCSV':
            P705_runTest = P705(self.errorRecord, node)

        elif node.name == 'plotWinProbabilities':
            P713_runTest = P713(self.errorRecord, node)
            P714_runTest = P714(self.errorRecord, node)
            P716_runTest = P716(self.errorRecord, node)
            P718_runTest = P718(self.errorRecord, node)

        elif node.name == 'winProbability':
            P701_runTest = P701(self.errorRecord, node)
            P717_runTest = P717(self.errorRecord, node)

        else: pass
        self.generic_visit(node)
