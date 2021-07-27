import ast
from typing import Set

from Prototype import Plugin

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col + 1} {msg}' for line, col, msg, _ in plugin.run()'}

def test_trivial_case():
    return

def test_incorrect_case():
    return

def test_correct_case():
    return
