# encoding: utf-8
# module lief.PE
# from /home/herizo/anaconda3/lib/python3.8/site-packages/lief.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python API for PE """

# imports
import lief as __lief
import pybind11_builtins as __pybind11_builtins


class Relocation(__lief.Object):
    # no doc
    def add_entry(self, new_entry, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        add_entry(self: lief.PE.Relocation, new_entry: LIEF::PE::RelocationEntry) -> LIEF::PE::RelocationEntry
        
        Add a new :class:`~lief.PE.RelocationEntry`
        """
        pass

    def __eq__(self, arg0): # real signature unknown; restored from __doc__
        """ __eq__(self: lief.PE.Relocation, arg0: lief.PE.Relocation) -> bool """
        return False

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: lief.PE.Relocation) -> int """
        return 0

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: lief.PE.Relocation) -> None """
        pass

    def __ne__(self, arg0): # real signature unknown; restored from __doc__
        """ __ne__(self: lief.PE.Relocation, arg0: lief.PE.Relocation) -> bool """
        return False

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: lief.PE.Relocation) -> str """
        return ""

    entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    virtual_address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



