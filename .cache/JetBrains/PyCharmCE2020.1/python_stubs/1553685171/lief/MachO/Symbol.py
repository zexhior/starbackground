# encoding: utf-8
# module lief.MachO
# from /home/herizo/anaconda3/lib/python3.8/site-packages/lief.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python API for MachO """

# imports
import lief as __lief
import pybind11_builtins as __pybind11_builtins


class Symbol(__lief.Symbol):
    # no doc
    def __eq__(self, arg0): # real signature unknown; restored from __doc__
        """ __eq__(self: lief.MachO.Symbol, arg0: lief.MachO.Symbol) -> bool """
        return False

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: lief.MachO.Symbol) -> int """
        return 0

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: lief.MachO.Symbol) -> None """
        pass

    def __ne__(self, arg0): # real signature unknown; restored from __doc__
        """ __ne__(self: lief.MachO.Symbol, arg0: lief.MachO.Symbol) -> bool """
        return False

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: lief.MachO.Symbol) -> str """
        return ""

    binding_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """:class:`~lief.MachO.BindingInfo` associated with the symbol (if any)"""

    demangled_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol's unmangled name"""

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    export_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """:class:`~lief.MachO.ExportInfo` associated with the symbol (if any)"""

    has_binding_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the symbol has an :class:`~lief.MachO.BindingInfo` associated with"""

    has_export_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the symbol has a :class:`~lief.MachO.ExportInfo` associated with"""

    numberof_sections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the :class:`~lief.MachO.SYMBOL_ORIGINS` of this symbol"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



