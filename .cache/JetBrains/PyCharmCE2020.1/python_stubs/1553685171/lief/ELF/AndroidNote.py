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

class AndroidNote(NoteDetails):
    # no doc
    def __eq__(self, arg0): # real signature unknown; restored from __doc__
        """ __eq__(self: lief.ELF.AndroidNote, arg0: lief.ELF.AndroidNote) -> bool """
        return False

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: lief.ELF.AndroidNote) -> int """
        return 0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, arg0): # real signature unknown; restored from __doc__
        """ __ne__(self: lief.ELF.AndroidNote, arg0: lief.ELF.AndroidNote) -> bool """
        return False

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: lief.ELF.AndroidNote) -> str """
        return ""

    ndk_build_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Android NDK build number"""

    ndk_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Android NDK version used to build the current binary"""

    sdk_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Target SDK platform"""



