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


class ELF_CLASS(__pybind11_builtins.pybind11_object):
    """
    Members:
    
      NONE
    
      CLASS32
    
      CLASS64
    """
    def (self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: object, arg0: object) -> bool
        
        2. __ne__(self: lief.ELF.ELF_CLASS, arg0: int) -> bool
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: object, arg0: object) -> bool
        
        2. __eq__(self: lief.ELF.ELF_CLASS, arg0: int) -> bool
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __index__(self): # real signature unknown; restored from __doc__
        """ __index__(self: lief.ELF.ELF_CLASS) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: lief.ELF.ELF_CLASS, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: lief.ELF.ELF_CLASS) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: object, arg0: object) -> bool
        
        2. __ne__(self: lief.ELF.ELF_CLASS, arg0: int) -> bool
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: lief.ELF.ELF_CLASS, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    CLASS32 = ELF_CLASS.CLASS32
    CLASS64 = ELF_CLASS.CLASS64
    NONE = ELF_CLASS.NONE
    __entries = {
        'CLASS32': (
            ELF_CLASS.CLASS32,
            None,
        ),
        'CLASS64': (
            ELF_CLASS.CLASS64,
            None,
        ),
        'NONE': (
            ELF_CLASS.NONE,
            None,
        ),
    }
    __members__ = {
        'CLASS32': ELF_CLASS.CLASS32,
        'CLASS64': ELF_CLASS.CLASS64,
        'NONE': ELF_CLASS.NONE,
    }


