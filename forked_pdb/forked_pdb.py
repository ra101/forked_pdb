import sys
from pdb import *

class ForkedPdb(Pdb):
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

        ForkedPdb().set_trace()


def set_trace():
    ForkedPdb().set_trace()