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


class ARM_EFLAGS(__pybind11_builtins.pybind11_object):
    """
    Members:
    
      SOFT_FLOAT
    
      VFP_FLOAT
    
      UNKNOWN
    
      EABI_VER1
    
      EABI_VER2
    
      EABI_VER3
    
      EABI_VER4
    
      EABI_VER5
    """
    def (self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ge__(*args, **kwargs)
        Overloaded function.
        
        1. __ge__(self: object, arg0: object) -> bool
        
        2. __ge__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> bool
        """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __and__(*args, **kwargs)
        Overloaded function.
        
        1. __and__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> int
        
        2. __and__(self: lief.ELF.ARM_EFLAGS, arg0: lief.ELF.ARM_EFLAGS) -> int
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: object, arg0: object) -> bool
        
        2. __eq__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> bool
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ge__(*args, **kwargs)
        Overloaded function.
        
        1. __ge__(self: object, arg0: object) -> bool
        
        2. __ge__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> bool
        """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __gt__(*args, **kwargs)
        Overloaded function.
        
        1. __gt__(self: object, arg0: object) -> bool
        
        2. __gt__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> bool
        """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __index__(self): # real signature unknown; restored from __doc__
        """ __index__(self: lief.ELF.ARM_EFLAGS) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: lief.ELF.ARM_EFLAGS) -> int """
        return 0

    def __invert__(self): # real signature unknown; restored from __doc__
        """ __invert__(self: lief.ELF.ARM_EFLAGS) -> int """
        return 0

    def __le__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __le__(*args, **kwargs)
        Overloaded function.
        
        1. __le__(self: object, arg0: object) -> bool
        
        2. __le__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> bool
        """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __lt__(*args, **kwargs)
        Overloaded function.
        
        1. __lt__(self: object, arg0: object) -> bool
        
        2. __lt__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> bool
        """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: object, arg0: object) -> bool
        
        2. __ne__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> bool
        """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __or__(*args, **kwargs)
        Overloaded function.
        
        1. __or__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> int
        
        2. __or__(self: lief.ELF.ARM_EFLAGS, arg0: lief.ELF.ARM_EFLAGS) -> int
        """
        pass

    def __rand__(self, arg0): # real signature unknown; restored from __doc__
        """ __rand__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> int """
        return 0

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __ror__(self, arg0): # real signature unknown; restored from __doc__
        """ __ror__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> int """
        return 0

    def __rxor__(self, arg0): # real signature unknown; restored from __doc__
        """ __rxor__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> int """
        return 0

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: lief.ELF.ARM_EFLAGS, arg0: int) -> None """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __xor__(*args, **kwargs)
        Overloaded function.
        
        1. __xor__(self: lief.ELF.ARM_EFLAGS, arg0: int) -> int
        
        2. __xor__(self: lief.ELF.ARM_EFLAGS, arg0: lief.ELF.ARM_EFLAGS) -> int
        """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    EABI_VER1 = ARM_EFLAGS.EABI_VER1
    EABI_VER2 = ARM_EFLAGS.EABI_VER2
    EABI_VER3 = ARM_EFLAGS.EABI_VER3
    EABI_VER4 = ARM_EFLAGS.EABI_VER4
    EABI_VER5 = ARM_EFLAGS.EABI_VER5
    SOFT_FLOAT = ARM_EFLAGS.SOFT_FLOAT
    UNKNOWN = ARM_EFLAGS.UNKNOWN
    VFP_FLOAT = ARM_EFLAGS.VFP_FLOAT
    __entries = {
        'EABI_VER1': (
            ARM_EFLAGS.EABI_VER1,
            None,
        ),
        'EABI_VER2': (
            ARM_EFLAGS.EABI_VER2,
            None,
        ),
        'EABI_VER3': (
            ARM_EFLAGS.EABI_VER3,
            None,
        ),
        'EABI_VER4': (
            ARM_EFLAGS.EABI_VER4,
            None,
        ),
        'EABI_VER5': (
            ARM_EFLAGS.EABI_VER5,
            None,
        ),
        'SOFT_FLOAT': (
            ARM_EFLAGS.SOFT_FLOAT,
            None,
        ),
        'UNKNOWN': (
            ARM_EFLAGS.UNKNOWN,
            None,
        ),
        'VFP_FLOAT': (
            ARM_EFLAGS.VFP_FLOAT,
            None,
        ),
    }
    __members__ = {
        'EABI_VER1': ARM_EFLAGS.EABI_VER1,
        'EABI_VER2': ARM_EFLAGS.EABI_VER2,
        'EABI_VER3': ARM_EFLAGS.EABI_VER3,
        'EABI_VER4': ARM_EFLAGS.EABI_VER4,
        'EABI_VER5': ARM_EFLAGS.EABI_VER5,
        'SOFT_FLOAT': ARM_EFLAGS.SOFT_FLOAT,
        'UNKNOWN': ARM_EFLAGS.UNKNOWN,
        'VFP_FLOAT': ARM_EFLAGS.VFP_FLOAT,
    }


