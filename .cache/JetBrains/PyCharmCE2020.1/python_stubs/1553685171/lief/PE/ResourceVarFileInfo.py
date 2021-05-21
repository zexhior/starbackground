# encoding: utf-8
# module lief.PE
# from /home/herizo/anaconda3/lib/python3.8/site-packages/lief.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python API for PE """

# imports
import lief as __lief
import pybind11_builtins as __pybind11_builtins


class ResourceVarFileInfo(__lief.Object):
    """ This object describes information about languages supported by the application """
    def __eq__(self, arg0): # real signature unknown; restored from __doc__
        """ __eq__(self: lief.PE.ResourceVarFileInfo, arg0: lief.PE.ResourceVarFileInfo) -> bool """
        return False

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: lief.PE.ResourceVarFileInfo) -> int """
        return 0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, arg0): # real signature unknown; restored from __doc__
        """ __ne__(self: lief.PE.ResourceVarFileInfo, arg0: lief.PE.ResourceVarFileInfo) -> bool """
        return False

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: lief.PE.ResourceVarFileInfo) -> str """
        return ""

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Signature of the structure. Must be ``VarFileInfo``"""

    translations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of languages that the application supports

The **least** significant 16-bits  must contain a Microsoft language identifier, and the **most** significant 16-bits must contain the :class:`~lief.PE.CODE_PAGES`
Either **most** or **least** 16-bits can be zero, indicating that the file is language or code page independent."""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of data in the version resource

* ``1`` if it contains text data
* ``0`` if it contains binary data
"""



