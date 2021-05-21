# encoding: utf-8
# module lief.ELF
# from /home/herizo/anaconda3/lib/python3.8/site-packages/lief.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python API for ELF format """

# imports
import lief.ELF.ELF32 as ELF32 # <module 'lief.ELF.ELF32'>
import lief.ELF.ELF64 as ELF64 # <module 'lief.ELF.ELF64'>
import lief as __lief
import pybind11_builtins as __pybind11_builtins


class NOTE_TYPES_CORE(__pybind11_builtins.pybind11_object):
    """
    Members:
    
      UNKNOWN
    
      PRSTATUS
    
      PRFPREG
    
      PRPSINFO
    
      TASKSTRUCT
    
      AUXV
    
      SIGINFO
    
      FILE
    
      ARM_VFP
    
      ARM_TLS
    
      ARM_HW_BREAK
    
      ARM_HW_WATCH
    
      ARM_SYSTEM_CALL
    
      ARM_SVE
    
      I386_TLS
    
      I386_IOPERM
    
      I386_XSTATE
    """
    def (self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: object, arg0: object) -> bool
        
        2. __ne__(self: lief.ELF.NOTE_TYPES_CORE, arg0: int) -> bool
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: object, arg0: object) -> bool
        
        2. __eq__(self: lief.ELF.NOTE_TYPES_CORE, arg0: int) -> bool
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __index__(self): # real signature unknown; restored from __doc__
        """ __index__(self: lief.ELF.NOTE_TYPES_CORE) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: lief.ELF.NOTE_TYPES_CORE, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: lief.ELF.NOTE_TYPES_CORE) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: object, arg0: object) -> bool
        
        2. __ne__(self: lief.ELF.NOTE_TYPES_CORE, arg0: int) -> bool
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: lief.ELF.NOTE_TYPES_CORE, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    ARM_HW_BREAK = NOTE_TYPES_CORE.ARM_HW_BREAK
    ARM_HW_WATCH = NOTE_TYPES_CORE.ARM_HW_WATCH
    ARM_SVE = NOTE_TYPES_CORE.ARM_SVE
    ARM_SYSTEM_CALL = NOTE_TYPES_CORE.ARM_SYSTEM_CALL
    ARM_TLS = NOTE_TYPES_CORE.ARM_TLS
    ARM_VFP = NOTE_TYPES_CORE.ARM_VFP
    AUXV = NOTE_TYPES_CORE.AUXV
    FILE = NOTE_TYPES_CORE.FILE
    I386_IOPERM = NOTE_TYPES_CORE.I386_IOPERM
    I386_TLS = NOTE_TYPES_CORE.I386_TLS
    I386_XSTATE = NOTE_TYPES_CORE.I386_XSTATE
    PRFPREG = NOTE_TYPES_CORE.PRFPREG
    PRPSINFO = NOTE_TYPES_CORE.PRPSINFO
    PRSTATUS = NOTE_TYPES_CORE.PRSTATUS
    SIGINFO = NOTE_TYPES_CORE.SIGINFO
    TASKSTRUCT = NOTE_TYPES_CORE.TASKSTRUCT
    UNKNOWN = NOTE_TYPES_CORE.UNKNOWN
    __entries = {
        'ARM_HW_BREAK': (
            NOTE_TYPES_CORE.ARM_HW_BREAK,
            None,
        ),
        'ARM_HW_WATCH': (
            NOTE_TYPES_CORE.ARM_HW_WATCH,
            None,
        ),
        'ARM_SVE': (
            NOTE_TYPES_CORE.ARM_SVE,
            None,
        ),
        'ARM_SYSTEM_CALL': (
            NOTE_TYPES_CORE.ARM_SYSTEM_CALL,
            None,
        ),
        'ARM_TLS': (
            NOTE_TYPES_CORE.ARM_TLS,
            None,
        ),
        'ARM_VFP': (
            NOTE_TYPES_CORE.ARM_VFP,
            None,
        ),
        'AUXV': (
            NOTE_TYPES_CORE.AUXV,
            None,
        ),
        'FILE': (
            NOTE_TYPES_CORE.FILE,
            None,
        ),
        'I386_IOPERM': (
            NOTE_TYPES_CORE.I386_IOPERM,
            None,
        ),
        'I386_TLS': (
            NOTE_TYPES_CORE.I386_TLS,
            None,
        ),
        'I386_XSTATE': (
            NOTE_TYPES_CORE.I386_XSTATE,
            None,
        ),
        'PRFPREG': (
            NOTE_TYPES_CORE.PRFPREG,
            None,
        ),
        'PRPSINFO': (
            NOTE_TYPES_CORE.PRPSINFO,
            None,
        ),
        'PRSTATUS': (
            NOTE_TYPES_CORE.PRSTATUS,
            None,
        ),
        'SIGINFO': (
            NOTE_TYPES_CORE.SIGINFO,
            None,
        ),
        'TASKSTRUCT': (
            NOTE_TYPES_CORE.TASKSTRUCT,
            None,
        ),
        'UNKNOWN': (
            NOTE_TYPES_CORE.UNKNOWN,
            None,
        ),
    }
    __members__ = {
        'ARM_HW_BREAK': NOTE_TYPES_CORE.ARM_HW_BREAK,
        'ARM_HW_WATCH': NOTE_TYPES_CORE.ARM_HW_WATCH,
        'ARM_SVE': NOTE_TYPES_CORE.ARM_SVE,
        'ARM_SYSTEM_CALL': NOTE_TYPES_CORE.ARM_SYSTEM_CALL,
        'ARM_TLS': NOTE_TYPES_CORE.ARM_TLS,
        'ARM_VFP': NOTE_TYPES_CORE.ARM_VFP,
        'AUXV': NOTE_TYPES_CORE.AUXV,
        'FILE': NOTE_TYPES_CORE.FILE,
        'I386_IOPERM': NOTE_TYPES_CORE.I386_IOPERM,
        'I386_TLS': NOTE_TYPES_CORE.I386_TLS,
        'I386_XSTATE': NOTE_TYPES_CORE.I386_XSTATE,
        'PRFPREG': NOTE_TYPES_CORE.PRFPREG,
        'PRPSINFO': NOTE_TYPES_CORE.PRPSINFO,
        'PRSTATUS': NOTE_TYPES_CORE.PRSTATUS,
        'SIGINFO': NOTE_TYPES_CORE.SIGINFO,
        'TASKSTRUCT': NOTE_TYPES_CORE.TASKSTRUCT,
        'UNKNOWN': NOTE_TYPES_CORE.UNKNOWN,
    }


