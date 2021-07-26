import sys
if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)
