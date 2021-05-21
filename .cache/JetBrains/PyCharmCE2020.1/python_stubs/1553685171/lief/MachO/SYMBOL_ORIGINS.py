# encoding: utf-8
# module lief.MachO
# from /home/herizo/anaconda3/lib/python3.8/site-packages/lief.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python API for MachO """

# imports
import lief as __lief
import pybind11_builtins as __pybind11_builtins


class SYMBOL_ORIGINS(__pybind11_builtins.pybind11_object):
    """
    Members:
    
      UNKNOWN
    
      DYLD_EXPORT
    
      LC_SYMTAB
    """
    def (self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: object, arg0: object) -> bool
        
        2. __ne__(self: lief.MachO.SYMBOL_ORIGINS, arg0: int) -> bool
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: object, arg0: object) -> bool
        
        2. __eq__(self: lief.MachO.SYMBOL_ORIGINS, arg0: int) -> bool
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __index__(self): # real signature unknown; restored from __doc__
        """ __index__(self: lief.MachO.SYMBOL_ORIGINS) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: lief.MachO.SYMBOL_ORIGINS, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: lief.MachO.SYMBOL_ORIGINS) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: object, arg0: object) -> bool
        
        2. __ne__(self: lief.MachO.SYMBOL_ORIGINS, arg0: int) -> bool
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: lief.MachO.SYMBOL_ORIGINS, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    DYLD_EXPORT = SYMBOL_ORIGINS.DYLD_EXPORT
    LC_SYMTAB = SYMBOL_ORIGINS.LC_SYMTAB
    UNKNOWN = SYMBOL_ORIGINS.UNKNOWN
    __entries = {
        'DYLD_EXPORT': (
            SYMBOL_ORIGINS.DYLD_EXPORT,
            None,
        ),
        'LC_SYMTAB': (
            SYMBOL_ORIGINS.LC_SYMTAB,
            None,
        ),
        'UNKNOWN': (
            SYMBOL_ORIGINS.UNKNOWN,
            None,
        ),
    }
    __members__ = {
        'DYLD_EXPORT': SYMBOL_ORIGINS.DYLD_EXPORT,
        'LC_SYMTAB': SYMBOL_ORIGINS.LC_SYMTAB,
        'UNKNOWN': SYMBOL_ORIGINS.UNKNOWN,
    }


