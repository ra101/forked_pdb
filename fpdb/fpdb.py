import sys
from pdb import *

class FPDb(Pdb):
    """
    PDB Subclass that can be used for multiprocessing child as well.
    Suggested in: https://stackoverflow.com/questions/4716533/
    """
    def interaction(self, *args, **kwargs):
        _stdin = sys.stdin
        try:
            sys.stdin = open('/dev/stdin')
            Pdb.interaction(self, *args, **kwargs)
        finally:
            sys.stdin = _stdin


def set_trace(*, header=None):
    fpdb_obj = FPDb()
    if header is not None:
        fpdb_obj.message(header)
    fpdb_obj.set_trace(sys._getframe().f_back)
