# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pbilinearform', [dirname(__file__)])
        except ImportError:
            import _pbilinearform
            return _pbilinearform
        if fp is not None:
            try:
                _mod = imp.load_module('_pbilinearform', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pbilinearform = swig_import_helper()
    del swig_import_helper
else:
    import _pbilinearform
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except Exception:
    weakref_proxy = lambda x: x



_pbilinearform.MFEM_TIMER_TYPE_swigconstant(_pbilinearform)
MFEM_TIMER_TYPE = _pbilinearform.MFEM_TIMER_TYPE
import handle
import operators
import vector
import array
import ostream_typemap
import hypre
import sparsemat
import matrix
import densemat
import fespace
import coefficient
import intrules
import eltrans
import fe
import mesh
import ncmesh
import element
import geom
import table
import vertex
import fe_coll
import lininteg
import pfespace
import pmesh
import pncmesh
import communication
import sets
import bilinearform
import bilininteg
import gridfunc
import linearform
class ParBilinearForm(bilinearform.BilinearForm):
    __swig_setmethods__ = {}
    for _s in [bilinearform.BilinearForm]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParBilinearForm, name, value)
    __swig_getmethods__ = {}
    for _s in [bilinearform.BilinearForm]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParBilinearForm, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pbilinearform.new_ParBilinearForm(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def KeepNbrBlock(self, knb=True):
        return _pbilinearform.ParBilinearForm_KeepNbrBlock(self, knb)

    def SetOperatorType(self, tid):
        return _pbilinearform.ParBilinearForm_SetOperatorType(self, tid)

    def Assemble(self, skip_zeros=1):
        return _pbilinearform.ParBilinearForm_Assemble(self, skip_zeros)

    def ParallelAssembleElim(self, *args):
        return _pbilinearform.ParBilinearForm_ParallelAssembleElim(self, *args)

    def ParallelAssemble(self, *args):
        return _pbilinearform.ParBilinearForm_ParallelAssemble(self, *args)

    def ParallelEliminateEssentialBC(self, *args):
        return _pbilinearform.ParBilinearForm_ParallelEliminateEssentialBC(self, *args)

    def ParallelEliminateTDofs(self, tdofs_list, A):
        return _pbilinearform.ParBilinearForm_ParallelEliminateTDofs(self, tdofs_list, A)

    def TrueAddMult(self, x, y, a=1.0):
        return _pbilinearform.ParBilinearForm_TrueAddMult(self, x, y, a)

    def ParFESpace(self):
        return _pbilinearform.ParBilinearForm_ParFESpace(self)

    def SCParFESpace(self):
        return _pbilinearform.ParBilinearForm_SCParFESpace(self)

    def GetProlongation(self):
        return _pbilinearform.ParBilinearForm_GetProlongation(self)

    def GetRestriction(self):
        return _pbilinearform.ParBilinearForm_GetRestriction(self)

    def FormSystemMatrix(self, ess_tdof_list, A):
        return _pbilinearform.ParBilinearForm_FormSystemMatrix(self, ess_tdof_list, A)

    def RecoverFEMSolution(self, X, b, x):
        return _pbilinearform.ParBilinearForm_RecoverFEMSolution(self, X, b, x)

    def Update(self, nfes=None):
        return _pbilinearform.ParBilinearForm_Update(self, nfes)
    __swig_destroy__ = _pbilinearform.delete_ParBilinearForm
    __del__ = lambda self: None

    def FormLinearSystem(self, *args):
        return _pbilinearform.ParBilinearForm_FormLinearSystem(self, *args)
ParBilinearForm_swigregister = _pbilinearform.ParBilinearForm_swigregister
ParBilinearForm_swigregister(ParBilinearForm)

class ParMixedBilinearForm(bilinearform.MixedBilinearForm):
    __swig_setmethods__ = {}
    for _s in [bilinearform.MixedBilinearForm]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParMixedBilinearForm, name, value)
    __swig_getmethods__ = {}
    for _s in [bilinearform.MixedBilinearForm]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParMixedBilinearForm, name)
    __repr__ = _swig_repr

    def __init__(self, trial_fes, test_fes):
        this = _pbilinearform.new_ParMixedBilinearForm(trial_fes, test_fes)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def ParallelAssemble(self, *args):
        return _pbilinearform.ParMixedBilinearForm_ParallelAssemble(self, *args)

    def TrueAddMult(self, x, y, a=1.0):
        return _pbilinearform.ParMixedBilinearForm_TrueAddMult(self, x, y, a)
    __swig_destroy__ = _pbilinearform.delete_ParMixedBilinearForm
    __del__ = lambda self: None
ParMixedBilinearForm_swigregister = _pbilinearform.ParMixedBilinearForm_swigregister
ParMixedBilinearForm_swigregister(ParMixedBilinearForm)

class ParDiscreteLinearOperator(bilinearform.DiscreteLinearOperator):
    __swig_setmethods__ = {}
    for _s in [bilinearform.DiscreteLinearOperator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParDiscreteLinearOperator, name, value)
    __swig_getmethods__ = {}
    for _s in [bilinearform.DiscreteLinearOperator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParDiscreteLinearOperator, name)
    __repr__ = _swig_repr

    def __init__(self, dfes, rfes):
        this = _pbilinearform.new_ParDiscreteLinearOperator(dfes, rfes)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def ParallelAssemble(self):
        return _pbilinearform.ParDiscreteLinearOperator_ParallelAssemble(self)

    def GetParBlocks(self, blocks):
        return _pbilinearform.ParDiscreteLinearOperator_GetParBlocks(self, blocks)
    __swig_destroy__ = _pbilinearform.delete_ParDiscreteLinearOperator
    __del__ = lambda self: None
ParDiscreteLinearOperator_swigregister = _pbilinearform.ParDiscreteLinearOperator_swigregister
ParDiscreteLinearOperator_swigregister(ParDiscreteLinearOperator)

# This file is compatible with both classic and new-style classes.


