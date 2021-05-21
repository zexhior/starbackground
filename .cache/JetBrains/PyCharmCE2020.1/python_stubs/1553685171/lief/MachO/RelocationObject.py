# encoding: utf-8
# module lief.MachO
# from /home/herizo/anaconda3/lib/python3.8/site-packages/lief.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python API for MachO """

# imports
import lief as __lief
import pybind11_builtins as __pybind11_builtins


from .Relocation import Relocation

class RelocationObject(Relocation):
    # no doc
    def __eq__(self, arg0): # real signature unknown; restored from __doc__
        """ __eq__(self: lief.MachO.RelocationObject, arg0: lief.MachO.RelocationObject) -> bool """
        return False

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: lief.MachO.RelocationObject) -> int """
        return 0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, arg0): # real signature unknown; restored from __doc__
        """ __ne__(self: lief.MachO.RelocationObject, arg0: lief.MachO.RelocationObject) -> bool """
        return False

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: lief.MachO.RelocationObject) -> str """
        return ""

    is_scattered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the relocation is a scattered one"""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For **scattered** relocations, the address of the relocatable expression for the item in the file that needs to be updated if the address is changed.

For relocatable expressions with the difference of two section addresses, the address from which to subtract (in mathematical terms, the minuend) is contained in the first relocation entry and the address to subtract (the subtrahend) is contained in the second relocation entry."""



