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


from .NoteDetails import NoteDetails

class CoreSigInfo(NoteDetails):
    # no doc
    def __eq__(self, arg0): # real signature unknown; restored from __doc__
        """ __eq__(self: lief.ELF.CoreSigInfo, arg0: lief.ELF.CoreSigInfo) -> bool """
        return False

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: lief.ELF.CoreSigInfo) -> int """
        return 0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, arg0): # real signature unknown; restored from __doc__
        """ __ne__(self: lief.ELF.CoreSigInfo, arg0: lief.ELF.CoreSigInfo) -> bool """
        return False

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: lief.ELF.CoreSigInfo) -> str """
        return ""

    sigcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Signal code"""

    sigerrno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If non-zero, an errno value associated with this signal"""

    signo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Signal number"""



