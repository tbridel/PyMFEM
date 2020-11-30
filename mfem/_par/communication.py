# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _communication
else:
    import _communication

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _communication.SWIG_PyInstanceMethod_New
_swig_new_static_method = _communication.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


MFEM_VERSION = _communication.MFEM_VERSION

MFEM_VERSION_STRING = _communication.MFEM_VERSION_STRING

MFEM_VERSION_TYPE = _communication.MFEM_VERSION_TYPE

MFEM_VERSION_TYPE_RELEASE = _communication.MFEM_VERSION_TYPE_RELEASE

MFEM_VERSION_TYPE_DEVELOPMENT = _communication.MFEM_VERSION_TYPE_DEVELOPMENT

MFEM_VERSION_MAJOR = _communication.MFEM_VERSION_MAJOR

MFEM_VERSION_MINOR = _communication.MFEM_VERSION_MINOR

MFEM_VERSION_PATCH = _communication.MFEM_VERSION_PATCH

MFEM_HYPRE_VERSION = _communication.MFEM_HYPRE_VERSION

import mfem._par.array
import mfem._par.mem_manager
import mfem._par.table
import mfem._par.sets
class MPI_Session(object):
    r"""Proxy of C++ mfem::MPI_Session class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(MPI_Session self) -> MPI_Session
        __init__(MPI_Session self, int & argc, char **& argv) -> MPI_Session
        """
        _communication.MPI_Session_swiginit(self, _communication.new_MPI_Session(*args))
    __swig_destroy__ = _communication.delete_MPI_Session

    def WorldRank(self):
        r"""WorldRank(MPI_Session self) -> int"""
        return _communication.MPI_Session_WorldRank(self)
    WorldRank = _swig_new_instance_method(_communication.MPI_Session_WorldRank)

    def WorldSize(self):
        r"""WorldSize(MPI_Session self) -> int"""
        return _communication.MPI_Session_WorldSize(self)
    WorldSize = _swig_new_instance_method(_communication.MPI_Session_WorldSize)

    def Root(self):
        r"""Root(MPI_Session self) -> bool"""
        return _communication.MPI_Session_Root(self)
    Root = _swig_new_instance_method(_communication.MPI_Session_Root)

# Register MPI_Session in _communication:
_communication.MPI_Session_swigregister(MPI_Session)

class GroupTopology(object):
    r"""Proxy of C++ mfem::GroupTopology class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(GroupTopology self) -> GroupTopology
        __init__(GroupTopology self, MPI_Comm comm) -> GroupTopology
        __init__(GroupTopology self, GroupTopology gt) -> GroupTopology
        """
        _communication.GroupTopology_swiginit(self, _communication.new_GroupTopology(*args))

    def SetComm(self, comm):
        r"""SetComm(GroupTopology self, MPI_Comm comm)"""
        return _communication.GroupTopology_SetComm(self, comm)
    SetComm = _swig_new_instance_method(_communication.GroupTopology_SetComm)

    def GetComm(self):
        r"""GetComm(GroupTopology self) -> MPI_Comm"""
        return _communication.GroupTopology_GetComm(self)
    GetComm = _swig_new_instance_method(_communication.GroupTopology_GetComm)

    def MyRank(self):
        r"""MyRank(GroupTopology self) -> int"""
        return _communication.GroupTopology_MyRank(self)
    MyRank = _swig_new_instance_method(_communication.GroupTopology_MyRank)

    def NRanks(self):
        r"""NRanks(GroupTopology self) -> int"""
        return _communication.GroupTopology_NRanks(self)
    NRanks = _swig_new_instance_method(_communication.GroupTopology_NRanks)

    def Create(self, groups, mpitag):
        r"""Create(GroupTopology self, ListOfIntegerSets groups, int mpitag)"""
        return _communication.GroupTopology_Create(self, groups, mpitag)
    Create = _swig_new_instance_method(_communication.GroupTopology_Create)

    def NGroups(self):
        r"""NGroups(GroupTopology self) -> int"""
        return _communication.GroupTopology_NGroups(self)
    NGroups = _swig_new_instance_method(_communication.GroupTopology_NGroups)

    def GetNumNeighbors(self):
        r"""GetNumNeighbors(GroupTopology self) -> int"""
        return _communication.GroupTopology_GetNumNeighbors(self)
    GetNumNeighbors = _swig_new_instance_method(_communication.GroupTopology_GetNumNeighbors)

    def GetNeighborRank(self, i):
        r"""GetNeighborRank(GroupTopology self, int i) -> int"""
        return _communication.GroupTopology_GetNeighborRank(self, i)
    GetNeighborRank = _swig_new_instance_method(_communication.GroupTopology_GetNeighborRank)

    def IAmMaster(self, g):
        r"""IAmMaster(GroupTopology self, int g) -> bool"""
        return _communication.GroupTopology_IAmMaster(self, g)
    IAmMaster = _swig_new_instance_method(_communication.GroupTopology_IAmMaster)

    def GetGroupMaster(self, g):
        r"""GetGroupMaster(GroupTopology self, int g) -> int"""
        return _communication.GroupTopology_GetGroupMaster(self, g)
    GetGroupMaster = _swig_new_instance_method(_communication.GroupTopology_GetGroupMaster)

    def GetGroupMasterRank(self, g):
        r"""GetGroupMasterRank(GroupTopology self, int g) -> int"""
        return _communication.GroupTopology_GetGroupMasterRank(self, g)
    GetGroupMasterRank = _swig_new_instance_method(_communication.GroupTopology_GetGroupMasterRank)

    def GetGroupMasterGroup(self, g):
        r"""GetGroupMasterGroup(GroupTopology self, int g) -> int"""
        return _communication.GroupTopology_GetGroupMasterGroup(self, g)
    GetGroupMasterGroup = _swig_new_instance_method(_communication.GroupTopology_GetGroupMasterGroup)

    def GetGroupSize(self, g):
        r"""GetGroupSize(GroupTopology self, int g) -> int"""
        return _communication.GroupTopology_GetGroupSize(self, g)
    GetGroupSize = _swig_new_instance_method(_communication.GroupTopology_GetGroupSize)

    def GetGroup(self, g):
        r"""GetGroup(GroupTopology self, int g) -> int const *"""
        return _communication.GroupTopology_GetGroup(self, g)
    GetGroup = _swig_new_instance_method(_communication.GroupTopology_GetGroup)

    def Load(self, _in):
        r"""Load(GroupTopology self, std::istream & _in)"""
        return _communication.GroupTopology_Load(self, _in)
    Load = _swig_new_instance_method(_communication.GroupTopology_Load)

    def Copy(self, copy):
        r"""Copy(GroupTopology self, GroupTopology copy)"""
        return _communication.GroupTopology_Copy(self, copy)
    Copy = _swig_new_instance_method(_communication.GroupTopology_Copy)
    __swig_destroy__ = _communication.delete_GroupTopology

    def Save(self, *args):
        r"""
        Save(GroupTopology self, std::ostream & out)
        Save(GroupTopology self, char const * file, int precision=8)
        """
        return _communication.GroupTopology_Save(self, *args)
    Save = _swig_new_instance_method(_communication.GroupTopology_Save)

# Register GroupTopology in _communication:
_communication.GroupTopology_swigregister(GroupTopology)

class GroupCommunicator(object):
    r"""Proxy of C++ mfem::GroupCommunicator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    byGroup = _communication.GroupCommunicator_byGroup
    
    byNeighbor = _communication.GroupCommunicator_byNeighbor
    

    def __init__(self, *args, **kwargs):
        r"""__init__(GroupCommunicator self, GroupTopology gt, mfem::GroupCommunicator::Mode m=byNeighbor) -> GroupCommunicator"""
        _communication.GroupCommunicator_swiginit(self, _communication.new_GroupCommunicator(*args, **kwargs))

    def Create(self, ldof_group):
        r"""Create(GroupCommunicator self, intArray ldof_group)"""
        return _communication.GroupCommunicator_Create(self, ldof_group)
    Create = _swig_new_instance_method(_communication.GroupCommunicator_Create)

    def GroupLDofTable(self, *args):
        r"""
        GroupLDofTable(GroupCommunicator self) -> Table
        GroupLDofTable(GroupCommunicator self) -> Table
        """
        return _communication.GroupCommunicator_GroupLDofTable(self, *args)
    GroupLDofTable = _swig_new_instance_method(_communication.GroupCommunicator_GroupLDofTable)

    def Finalize(self):
        r"""Finalize(GroupCommunicator self)"""
        return _communication.GroupCommunicator_Finalize(self)
    Finalize = _swig_new_instance_method(_communication.GroupCommunicator_Finalize)

    def SetLTDofTable(self, ldof_ltdof):
        r"""SetLTDofTable(GroupCommunicator self, intArray ldof_ltdof)"""
        return _communication.GroupCommunicator_SetLTDofTable(self, ldof_ltdof)
    SetLTDofTable = _swig_new_instance_method(_communication.GroupCommunicator_SetLTDofTable)

    def GetGroupTopology(self, *args):
        r"""
        GetGroupTopology(GroupCommunicator self) -> GroupTopology
        GetGroupTopology(GroupCommunicator self) -> GroupTopology
        """
        return _communication.GroupCommunicator_GetGroupTopology(self, *args)
    GetGroupTopology = _swig_new_instance_method(_communication.GroupCommunicator_GetGroupTopology)

    def GetNeighborLTDofTable(self, nbr_ltdof):
        r"""GetNeighborLTDofTable(GroupCommunicator self, Table nbr_ltdof)"""
        return _communication.GroupCommunicator_GetNeighborLTDofTable(self, nbr_ltdof)
    GetNeighborLTDofTable = _swig_new_instance_method(_communication.GroupCommunicator_GetNeighborLTDofTable)

    def GetNeighborLDofTable(self, nbr_ldof):
        r"""GetNeighborLDofTable(GroupCommunicator self, Table nbr_ldof)"""
        return _communication.GroupCommunicator_GetNeighborLDofTable(self, nbr_ldof)
    GetNeighborLDofTable = _swig_new_instance_method(_communication.GroupCommunicator_GetNeighborLDofTable)
    __swig_destroy__ = _communication.delete_GroupCommunicator

    def PrintInfo(self, *args):
        r"""
        PrintInfo(GroupCommunicator self, std::ostream & out=mfem::out)
        PrintInfo(GroupCommunicator self, char const * file, int precision=8)
        """
        return _communication.GroupCommunicator_PrintInfo(self, *args)
    PrintInfo = _swig_new_instance_method(_communication.GroupCommunicator_PrintInfo)

# Register GroupCommunicator in _communication:
_communication.GroupCommunicator_swigregister(GroupCommunicator)


def ReorderRanksZCurve(comm):
    r"""ReorderRanksZCurve(MPI_Comm comm) -> MPI_Comm"""
    return _communication.ReorderRanksZCurve(comm)
ReorderRanksZCurve = _communication.ReorderRanksZCurve


