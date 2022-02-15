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
    from . import _hexahedron
else:
    import _hexahedron

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _hexahedron.SWIG_PyInstanceMethod_New
_swig_new_static_method = _hexahedron.SWIG_PyStaticMethod_New

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


import weakref

import mfem._par.fe
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.geom
import mfem._par.intrules
import mfem._par.densemat
import mfem._par.operators
import mfem._par.matrix
import mfem._par.sparsemat
import mfem._par.globals
import mfem._par.fe_base
import mfem._par.fe_fixed_order
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.fe_h1
import mfem._par.fe_nd
import mfem._par.fe_rt
import mfem._par.fe_l2
import mfem._par.fe_nurbs
import mfem._par.fe_pos
import mfem._par.fe_ser
class Hexahedron(mfem._par.element.Element):
    r"""Proxy of C++ mfem::Hexahedron class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(Hexahedron self) -> Hexahedron
        __init__(Hexahedron self, int const * ind, int attr=1) -> Hexahedron
        __init__(Hexahedron self, int ind1, int ind2, int ind3, int ind4, int ind5, int ind6, int ind7, int ind8, int attr=1) -> Hexahedron
        """
        _hexahedron.Hexahedron_swiginit(self, _hexahedron.new_Hexahedron(*args))

    def GetType(self):
        r"""GetType(Hexahedron self) -> mfem::Element::Type"""
        return _hexahedron.Hexahedron_GetType(self)
    GetType = _swig_new_instance_method(_hexahedron.Hexahedron_GetType)

    def GetVertices(self, *args):
        r"""
        GetVertices(Hexahedron self, intArray v)
        GetVertices(Hexahedron self) -> int *
        """
        return _hexahedron.Hexahedron_GetVertices(self, *args)
    GetVertices = _swig_new_instance_method(_hexahedron.Hexahedron_GetVertices)

    def GetNVertices(self):
        r"""GetNVertices(Hexahedron self) -> int"""
        return _hexahedron.Hexahedron_GetNVertices(self)
    GetNVertices = _swig_new_instance_method(_hexahedron.Hexahedron_GetNVertices)

    def GetNEdges(self):
        r"""GetNEdges(Hexahedron self) -> int"""
        return _hexahedron.Hexahedron_GetNEdges(self)
    GetNEdges = _swig_new_instance_method(_hexahedron.Hexahedron_GetNEdges)

    def GetEdgeVertices(self, ei):
        r"""GetEdgeVertices(Hexahedron self, int ei) -> int const *"""
        return _hexahedron.Hexahedron_GetEdgeVertices(self, ei)
    GetEdgeVertices = _swig_new_instance_method(_hexahedron.Hexahedron_GetEdgeVertices)

    def GetNFaces(self, *args):
        r"""
        GetNFaces(Hexahedron self, int & nFaceVertices) -> int
        GetNFaces(Hexahedron self) -> int
        """

        if len(args) == 1:
             import warnings
             warnings.warn("Hexahedron::GetNFaces(int & nFaceVertices) is deprecated is deprecated",
         	              DeprecationWarning,)


        return _hexahedron.Hexahedron_GetNFaces(self, *args)


    def GetNFaceVertices(self, arg2):
        r"""GetNFaceVertices(Hexahedron self, int arg2) -> int"""
        return _hexahedron.Hexahedron_GetNFaceVertices(self, arg2)
    GetNFaceVertices = _swig_new_instance_method(_hexahedron.Hexahedron_GetNFaceVertices)

    def GetFaceVertices(self, fi):
        r"""GetFaceVertices(Hexahedron self, int fi) -> int const *"""
        return _hexahedron.Hexahedron_GetFaceVertices(self, fi)
    GetFaceVertices = _swig_new_instance_method(_hexahedron.Hexahedron_GetFaceVertices)

    def Duplicate(self, m):
        r"""Duplicate(Hexahedron self, mfem::Mesh * m) -> Element"""
        return _hexahedron.Hexahedron_Duplicate(self, m)
    Duplicate = _swig_new_instance_method(_hexahedron.Hexahedron_Duplicate)
    __swig_destroy__ = _hexahedron.delete_Hexahedron

# Register Hexahedron in _hexahedron:
_hexahedron.Hexahedron_swigregister(Hexahedron)


cvar = _hexahedron.cvar

