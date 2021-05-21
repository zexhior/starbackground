# encoding: utf-8
# module lief.PE
# from /home/herizo/anaconda3/lib/python3.8/site-packages/lief.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python API for PE """

# imports
import lief as __lief
import pybind11_builtins as __pybind11_builtins


from .ResourceNode import ResourceNode

class ResourceData(ResourceNode):
    # no doc
    def __eq__(self, arg0): # real signature unknown; restored from __doc__
        """ __eq__(self: lief.PE.ResourceData, arg0: lief.PE.ResourceData) -> bool """
        return False

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: lief.PE.ResourceData) -> int """
        return 0

    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.
        
        1. __init__(self: lief.PE.ResourceData) -> None
        
        Default constructor
        
        2. __init__(self: lief.PE.ResourceData, content: List[int], code_page: int) -> None
        """
        pass

    def __ne__(self, arg0): # real signature unknown; restored from __doc__
        """ __ne__(self: lief.PE.ResourceData, arg0: lief.PE.ResourceData) -> bool """
        return False

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: lief.PE.ResourceData) -> str """
        return ""

    code_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The code page that is used to decode code point values within the resource data. Typically, the code page would be the Unicode code page"""

    content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Resource content"""

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Offset of the content within the resource"""

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reserved value. Should be ``0``"""



