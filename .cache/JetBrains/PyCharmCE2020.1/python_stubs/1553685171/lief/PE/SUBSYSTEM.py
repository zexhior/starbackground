# encoding: utf-8
# module lief.PE
# from /home/herizo/anaconda3/lib/python3.8/site-packages/lief.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python API for PE """

# imports
import lief as __lief
import pybind11_builtins as __pybind11_builtins


class SUBSYSTEM(__pybind11_builtins.pybind11_object):
    """
    Members:
    
      UNKNOWN
    
      NATIVE
    
      WINDOWS_GUI
    
      WINDOWS_CUI
    
      OS2_CUI
    
      POSIX_CUI
    
      NATIVE_WINDOWS
    
      WINDOWS_CE_GUI
    
      EFI_APPLICATION
    
      EFI_BOOT_SERVICE_DRIVER
    
      EFI_RUNTIME_DRIVER
    
      EFI_ROM
    
      XBOX
    
      WINDOWS_BOOT_APPLICATION
    """
    def (self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: object, arg0: object) -> bool
        
        2. __ne__(self: lief.PE.SUBSYSTEM, arg0: int) -> bool
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: object, arg0: object) -> bool
        
        2. __eq__(self: lief.PE.SUBSYSTEM, arg0: int) -> bool
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __index__(self): # real signature unknown; restored from __doc__
        """ __index__(self: lief.PE.SUBSYSTEM) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: lief.PE.SUBSYSTEM, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: lief.PE.SUBSYSTEM) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: object, arg0: object) -> bool
        
        2. __ne__(self: lief.PE.SUBSYSTEM, arg0: int) -> bool
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: lief.PE.SUBSYSTEM, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    EFI_APPLICATION = SUBSYSTEM.EFI_APPLICATION
    EFI_BOOT_SERVICE_DRIVER = SUBSYSTEM.EFI_BOOT_SERVICE_DRIVER
    EFI_ROM = SUBSYSTEM.EFI_ROM
    EFI_RUNTIME_DRIVER = SUBSYSTEM.EFI_RUNTIME_DRIVER
    NATIVE = SUBSYSTEM.NATIVE
    NATIVE_WINDOWS = SUBSYSTEM.NATIVE_WINDOWS
    OS2_CUI = SUBSYSTEM.OS2_CUI
    POSIX_CUI = SUBSYSTEM.POSIX_CUI
    UNKNOWN = SUBSYSTEM.UNKNOWN
    WINDOWS_BOOT_APPLICATION = SUBSYSTEM.WINDOWS_BOOT_APPLICATION
    WINDOWS_CE_GUI = SUBSYSTEM.WINDOWS_CE_GUI
    WINDOWS_CUI = SUBSYSTEM.WINDOWS_CUI
    WINDOWS_GUI = SUBSYSTEM.WINDOWS_GUI
    XBOX = SUBSYSTEM.XBOX
    __entries = {
        'EFI_APPLICATION': (
            SUBSYSTEM.EFI_APPLICATION,
            None,
        ),
        'EFI_BOOT_SERVICE_DRIVER': (
            SUBSYSTEM.EFI_BOOT_SERVICE_DRIVER,
            None,
        ),
        'EFI_ROM': (
            SUBSYSTEM.EFI_ROM,
            None,
        ),
        'EFI_RUNTIME_DRIVER': (
            SUBSYSTEM.EFI_RUNTIME_DRIVER,
            None,
        ),
        'NATIVE': (
            SUBSYSTEM.NATIVE,
            None,
        ),
        'NATIVE_WINDOWS': (
            SUBSYSTEM.NATIVE_WINDOWS,
            None,
        ),
        'OS2_CUI': (
            SUBSYSTEM.OS2_CUI,
            None,
        ),
        'POSIX_CUI': (
            SUBSYSTEM.POSIX_CUI,
            None,
        ),
        'UNKNOWN': (
            SUBSYSTEM.UNKNOWN,
            None,
        ),
        'WINDOWS_BOOT_APPLICATION': (
            SUBSYSTEM.WINDOWS_BOOT_APPLICATION,
            None,
        ),
        'WINDOWS_CE_GUI': (
            SUBSYSTEM.WINDOWS_CE_GUI,
            None,
        ),
        'WINDOWS_CUI': (
            SUBSYSTEM.WINDOWS_CUI,
            None,
        ),
        'WINDOWS_GUI': (
            SUBSYSTEM.WINDOWS_GUI,
            None,
        ),
        'XBOX': (
            SUBSYSTEM.XBOX,
            None,
        ),
    }
    __members__ = {
        'EFI_APPLICATION': SUBSYSTEM.EFI_APPLICATION,
        'EFI_BOOT_SERVICE_DRIVER': SUBSYSTEM.EFI_BOOT_SERVICE_DRIVER,
        'EFI_ROM': SUBSYSTEM.EFI_ROM,
        'EFI_RUNTIME_DRIVER': SUBSYSTEM.EFI_RUNTIME_DRIVER,
        'NATIVE': SUBSYSTEM.NATIVE,
        'NATIVE_WINDOWS': SUBSYSTEM.NATIVE_WINDOWS,
        'OS2_CUI': SUBSYSTEM.OS2_CUI,
        'POSIX_CUI': SUBSYSTEM.POSIX_CUI,
        'UNKNOWN': SUBSYSTEM.UNKNOWN,
        'WINDOWS_BOOT_APPLICATION': SUBSYSTEM.WINDOWS_BOOT_APPLICATION,
        'WINDOWS_CE_GUI': SUBSYSTEM.WINDOWS_CE_GUI,
        'WINDOWS_CUI': SUBSYSTEM.WINDOWS_CUI,
        'WINDOWS_GUI': SUBSYSTEM.WINDOWS_GUI,
        'XBOX': SUBSYSTEM.XBOX,
    }


