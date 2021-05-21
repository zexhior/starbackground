# encoding: utf-8
# module lief.MachO
# from /home/herizo/anaconda3/lib/python3.8/site-packages/lief.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python API for MachO """

# imports
import lief as __lief
import pybind11_builtins as __pybind11_builtins


class BIND_OPCODES(__pybind11_builtins.pybind11_object):
    """
    Members:
    
      DONE
    
      SET_DYLIB_ORDINAL_IMM
    
      SET_DYLIB_ORDINAL_ULEB
    
      SET_DYLIB_SPECIAL_IMM
    
      SET_SYMBOL_TRAILING_FLAGS_IMM
    
      SET_TYPE_IMM
    
      SET_ADDEND_SLEB
    
      SET_SEGMENT_AND_OFFSET_ULEB
    
      ADD_ADDR_ULEB
    
      DO_BIND
    
      DO_BIND_ADD_ADDR_ULEB
    
      DO_BIND_ADD_ADDR_IMM_SCALED
    
      DO_BIND_ULEB_TIMES_SKIPPING_ULEB
    """
    def (self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: object, arg0: object) -> bool
        
        2. __ne__(self: lief.MachO.BIND_OPCODES, arg0: int) -> bool
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: object, arg0: object) -> bool
        
        2. __eq__(self: lief.MachO.BIND_OPCODES, arg0: int) -> bool
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __index__(self): # real signature unknown; restored from __doc__
        """ __index__(self: lief.MachO.BIND_OPCODES) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: lief.MachO.BIND_OPCODES, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: lief.MachO.BIND_OPCODES) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: object, arg0: object) -> bool
        
        2. __ne__(self: lief.MachO.BIND_OPCODES, arg0: int) -> bool
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: lief.MachO.BIND_OPCODES, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    ADD_ADDR_ULEB = BIND_OPCODES.ADD_ADDR_ULEB
    DONE = BIND_OPCODES.DONE
    DO_BIND = BIND_OPCODES.DO_BIND
    DO_BIND_ADD_ADDR_IMM_SCALED = BIND_OPCODES.DO_BIND_ADD_ADDR_IMM_SCALED
    DO_BIND_ADD_ADDR_ULEB = BIND_OPCODES.DO_BIND_ADD_ADDR_ULEB
    DO_BIND_ULEB_TIMES_SKIPPING_ULEB = BIND_OPCODES.DO_BIND_ULEB_TIMES_SKIPPING_ULEB
    SET_ADDEND_SLEB = BIND_OPCODES.SET_ADDEND_SLEB
    SET_DYLIB_ORDINAL_IMM = BIND_OPCODES.SET_DYLIB_ORDINAL_IMM
    SET_DYLIB_ORDINAL_ULEB = BIND_OPCODES.SET_DYLIB_ORDINAL_ULEB
    SET_DYLIB_SPECIAL_IMM = BIND_OPCODES.SET_DYLIB_SPECIAL_IMM
    SET_SEGMENT_AND_OFFSET_ULEB = BIND_OPCODES.SET_SEGMENT_AND_OFFSET_ULEB
    SET_SYMBOL_TRAILING_FLAGS_IMM = BIND_OPCODES.SET_SYMBOL_TRAILING_FLAGS_IMM
    SET_TYPE_IMM = BIND_OPCODES.SET_TYPE_IMM
    __entries = {
        'ADD_ADDR_ULEB': (
            BIND_OPCODES.ADD_ADDR_ULEB,
            None,
        ),
        'DONE': (
            BIND_OPCODES.DONE,
            None,
        ),
        'DO_BIND': (
            BIND_OPCODES.DO_BIND,
            None,
        ),
        'DO_BIND_ADD_ADDR_IMM_SCALED': (
            BIND_OPCODES.DO_BIND_ADD_ADDR_IMM_SCALED,
            None,
        ),
        'DO_BIND_ADD_ADDR_ULEB': (
            BIND_OPCODES.DO_BIND_ADD_ADDR_ULEB,
            None,
        ),
        'DO_BIND_ULEB_TIMES_SKIPPING_ULEB': (
            BIND_OPCODES.DO_BIND_ULEB_TIMES_SKIPPING_ULEB,
            None,
        ),
        'SET_ADDEND_SLEB': (
            BIND_OPCODES.SET_ADDEND_SLEB,
            None,
        ),
        'SET_DYLIB_ORDINAL_IMM': (
            BIND_OPCODES.SET_DYLIB_ORDINAL_IMM,
            None,
        ),
        'SET_DYLIB_ORDINAL_ULEB': (
            BIND_OPCODES.SET_DYLIB_ORDINAL_ULEB,
            None,
        ),
        'SET_DYLIB_SPECIAL_IMM': (
            BIND_OPCODES.SET_DYLIB_SPECIAL_IMM,
            None,
        ),
        'SET_SEGMENT_AND_OFFSET_ULEB': (
            BIND_OPCODES.SET_SEGMENT_AND_OFFSET_ULEB,
            None,
        ),
        'SET_SYMBOL_TRAILING_FLAGS_IMM': (
            BIND_OPCODES.SET_SYMBOL_TRAILING_FLAGS_IMM,
            None,
        ),
        'SET_TYPE_IMM': (
            BIND_OPCODES.SET_TYPE_IMM,
            None,
        ),
    }
    __members__ = {
        'ADD_ADDR_ULEB': BIND_OPCODES.ADD_ADDR_ULEB,
        'DONE': BIND_OPCODES.DONE,
        'DO_BIND': BIND_OPCODES.DO_BIND,
        'DO_BIND_ADD_ADDR_IMM_SCALED': BIND_OPCODES.DO_BIND_ADD_ADDR_IMM_SCALED,
        'DO_BIND_ADD_ADDR_ULEB': BIND_OPCODES.DO_BIND_ADD_ADDR_ULEB,
        'DO_BIND_ULEB_TIMES_SKIPPING_ULEB': BIND_OPCODES.DO_BIND_ULEB_TIMES_SKIPPING_ULEB,
        'SET_ADDEND_SLEB': BIND_OPCODES.SET_ADDEND_SLEB,
        'SET_DYLIB_ORDINAL_IMM': BIND_OPCODES.SET_DYLIB_ORDINAL_IMM,
        'SET_DYLIB_ORDINAL_ULEB': BIND_OPCODES.SET_DYLIB_ORDINAL_ULEB,
        'SET_DYLIB_SPECIAL_IMM': BIND_OPCODES.SET_DYLIB_SPECIAL_IMM,
        'SET_SEGMENT_AND_OFFSET_ULEB': BIND_OPCODES.SET_SEGMENT_AND_OFFSET_ULEB,
        'SET_SYMBOL_TRAILING_FLAGS_IMM': BIND_OPCODES.SET_SYMBOL_TRAILING_FLAGS_IMM,
        'SET_TYPE_IMM': BIND_OPCODES.SET_TYPE_IMM,
    }


