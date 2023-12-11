import sys
import pdb


class FPDb(pdb.Pdb):
    """
    PDB Subclass that can be used for multiprocessing child as well.
    Suggested in: https://stackoverflow.com/questions/4716533/
    """
    def interaction(self, *args, **kwargs):
        _stdin = sys.stdin
        try:
            if sys.platform == "win32":
                sys.stdin = self.WinStdHandle()
            else:
                sys.stdin = open('/dev/stdin')
            pdb.Pdb.interaction(self, *args, **kwargs)
        finally:
            sys.stdin = _stdin


    class WinStdHandle:
        """
        Provides Windows OS, a way to read the input from the console.
        """
        def __init__(self):
            import win32console

            self.screenBuffer = win32console.GetStdHandle(
                win32console.STD_INPUT_HANDLE
            )
        
        def readline(self):
            return self.screenBuffer.ReadConsole(1000)




def set_trace(*, header=None):
    debugger = FPDb()
    if header is not None:
        debugger.message(header)
    debugger.set_trace(sys._getframe().f_back)
