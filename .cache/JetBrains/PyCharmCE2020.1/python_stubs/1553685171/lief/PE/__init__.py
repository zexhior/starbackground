# encoding: utf-8
# module lief.PE
# from /home/herizo/anaconda3/lib/python3.8/site-packages/lief.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python API for PE """

# imports
import lief as __lief
import pybind11_builtins as __pybind11_builtins


# Variables with simple values

__loader__ = None

__spec__ = None

# functions

def get_imphash(binary): # real signature unknown; restored from __doc__
    """
    get_imphash(binary: lief.PE.Binary) -> str
    
    Compute the hash of imported functions
    
    Properties of the hash generated:
    	* Order agnostic
    	* Casse agnostic
    	* Ordinal (**in some extent**) agnostic
    
    .. warning::
    
    	The algorithm used to compute the *imphash* value has some variations compared to Yara, pefile, VT implementation
    .. seealso::
    
    	https://www.fireeye.com/blog/threat-research/2014/01/tracking-malware-import-hashing.html
    """
    return ""

def get_type(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    get_type(*args, **kwargs)
    Overloaded function.
    
    1. get_type(file: str) -> lief.PE.PE_TYPE
    
    If the input file is a ``PE`` one, return the :class:`~lief.PE.PE_TYPE`
    
    2. get_type(raw: List[int]) -> lief.PE.PE_TYPE
    
    If the input *raw* data represent a ``PE`` file, return the :class:`~lief.PE.PE_TYPE`
    """
    pass

def is_pe(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    is_pe(*args, **kwargs)
    Overloaded function.
    
    1. is_pe(file: str) -> bool
    
    Check if the given file is a ``PE``
    
    2. is_pe(raw: List[int]) -> bool
    
    Check if the given raw data is a ``PE``
    """
    pass

def oid_to_string(arg0): # real signature unknown; restored from __doc__
    """
    oid_to_string(arg0: str) -> str
    
    Convert an OID to a human-readable string
    """
    return ""

def parse(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    parse(*args, **kwargs)
    Overloaded function.
    
    1. parse(filename: str) -> LIEF::PE::Binary
    
    Parse the given binary and return a :class:`~lief.PE.Binary` object
    
    2. parse(raw: List[int], name: str = '') -> LIEF::PE::Binary
    
    Parse the given binary and return a :class:`~lief.PE.Binary` object
    
    3. parse(io: object, name: str = '') -> LIEF::PE::Binary
    """
    pass

def resolve_ordinals(import_, strict=False): # real signature unknown; restored from __doc__
    """
    resolve_ordinals(import: lief.PE.Import, strict: bool = False) -> lief.PE.Import
    
    Take an :class:`~lief.PE.Import` as entry and try to resolve its ordinal imports
    
    The ``strict`` boolean parameter enables to throw a :class:`~lief.not_found` exception if the ordinal can't be resolved. Otherwise it skips the entry.
    """
    pass

# classes

from .AuthenticatedAttributes import AuthenticatedAttributes
from .Binary import Binary
from .Builder import Builder
from .CodeIntegrity import CodeIntegrity
from .CodeView import CodeView
from .CodeViewPDB import CodeViewPDB
from .CODE_PAGES import CODE_PAGES
from .CODE_VIEW_SIGNATURES import CODE_VIEW_SIGNATURES
from .ContentInfo import ContentInfo
from .DataDirectory import DataDirectory
from .DATA_DIRECTORY import DATA_DIRECTORY
from .Debug import Debug
from .DEBUG_TYPES import DEBUG_TYPES
from .DIALOG_BOX_STYLES import DIALOG_BOX_STYLES
from .DLL_CHARACTERISTICS import DLL_CHARACTERISTICS
from .DosHeader import DosHeader
from .Export import Export
from .ExportEntry import ExportEntry
from .EXTENDED_WINDOW_STYLES import EXTENDED_WINDOW_STYLES
from .FIXED_VERSION_FILE_FLAGS import FIXED_VERSION_FILE_FLAGS
from .FIXED_VERSION_FILE_SUB_TYPES import FIXED_VERSION_FILE_SUB_TYPES
from .FIXED_VERSION_FILE_TYPES import FIXED_VERSION_FILE_TYPES
from .FIXED_VERSION_OS import FIXED_VERSION_OS
from .GUARD_CF_FLAGS import GUARD_CF_FLAGS
from .GUARD_RF_FLAGS import GUARD_RF_FLAGS
from .Header import Header
from .HEADER_CHARACTERISTICS import HEADER_CHARACTERISTICS
from .Import import Import
from .ImportEntry import ImportEntry
from .LangCodeItem import LangCodeItem
from .LoadConfiguration import LoadConfiguration
from .LoadConfigurationV0 import LoadConfigurationV0
from .LoadConfigurationV1 import LoadConfigurationV1
from .LoadConfigurationV2 import LoadConfigurationV2
from .LoadConfigurationV3 import LoadConfigurationV3
from .LoadConfigurationV4 import LoadConfigurationV4
from .LoadConfigurationV5 import LoadConfigurationV5
from .LoadConfigurationV6 import LoadConfigurationV6
from .LoadConfigurationV7 import LoadConfigurationV7
from .MACHINE_TYPES import MACHINE_TYPES
from .OptionalHeader import OptionalHeader
from .PE_TYPE import PE_TYPE
from .Pogo import Pogo
from .PogoEntry import PogoEntry
from .POGO_SIGNATURES import POGO_SIGNATURES
from .Relocation import Relocation
from .RelocationEntry import RelocationEntry
from .RELOCATIONS_BASE_TYPES import RELOCATIONS_BASE_TYPES
from .ResourceNode import ResourceNode
from .ResourceData import ResourceData
from .ResourceDialog import ResourceDialog
from .ResourceDialogItem import ResourceDialogItem
from .ResourceDirectory import ResourceDirectory
from .ResourceFixedFileInfo import ResourceFixedFileInfo
from .ResourceIcon import ResourceIcon
from .ResourcesManager import ResourcesManager
from .ResourceStringFileInfo import ResourceStringFileInfo
from .ResourceVarFileInfo import ResourceVarFileInfo
from .ResourceVersion import ResourceVersion
from .RESOURCE_LANGS import RESOURCE_LANGS
from .RESOURCE_SUBLANGS import RESOURCE_SUBLANGS
from .RESOURCE_TYPES import RESOURCE_TYPES
from .RichEntry import RichEntry
from .RichHeader import RichHeader
from .Section import Section
from .SECTION_CHARACTERISTICS import SECTION_CHARACTERISTICS
from .SECTION_TYPES import SECTION_TYPES
from .Signature import Signature
from .SignerInfo import SignerInfo
from .SUBSYSTEM import SUBSYSTEM
from .Symbol import Symbol
from .SYMBOL_BASE_TYPES import SYMBOL_BASE_TYPES
from .SYMBOL_COMPLEX_TYPES import SYMBOL_COMPLEX_TYPES
from .SYMBOL_SECTION_NUMBER import SYMBOL_SECTION_NUMBER
from .SYMBOL_STORAGE_CLASS import SYMBOL_STORAGE_CLASS
from .TLS import TLS
from .WINDOW_STYLES import WINDOW_STYLES
from .WIN_VERSION import WIN_VERSION
from .x509 import x509
