import ast
from typing import Set

from COMSC_Plugin import Plugin

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col + 1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    # Checking empty string
    # Should result in empty error set using results
    # Assertation error otherwise
    assert _results('') == set()

def test_incorrect_case():
    # Tests failing input
    # Asserts
    ret = _results('f(**{"foo": "bar"})')
    assert ret == {'1:1 FNA100 named argument should not use **'}

def test_allowed_splat_arguments():
    assert _results('f(**{"foo-bar": "baz"})') == set()
