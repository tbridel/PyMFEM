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
            fp, pathname, description = imp.find_module('_hypre', [dirname(__file__)])
        except ImportError:
            import _hypre
            return _hypre
        if fp is not None:
            try:
                _mod = imp.load_module('_hypre', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _hypre = swig_import_helper()
    del swig_import_helper
else:
    import _hypre
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



_hypre.MFEM_TIMER_TYPE_swigconstant(_hypre)
MFEM_TIMER_TYPE = _hypre.MFEM_TIMER_TYPE
class intp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intp, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _hypre.new_intp()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _hypre.delete_intp
    __del__ = lambda self: None

    def assign(self, value):
        return _hypre.intp_assign(self, value)

    def value(self):
        return _hypre.intp_value(self)

    def cast(self):
        return _hypre.intp_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _hypre.intp_frompointer
    if _newclass:
        frompointer = staticmethod(_hypre.intp_frompointer)
intp_swigregister = _hypre.intp_swigregister
intp_swigregister(intp)

def intp_frompointer(t):
    return _hypre.intp_frompointer(t)
intp_frompointer = _hypre.intp_frompointer

import vector
import array
import ostream_typemap
import sparsemat
import operators
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

def sizeof_HYPRE_Int():
    return _hypre.sizeof_HYPRE_Int()
sizeof_HYPRE_Int = _hypre.sizeof_HYPRE_Int
class HypreParVector(vector.Vector):
    __swig_setmethods__ = {}
    for _s in [vector.Vector]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreParVector, name, value)
    __swig_getmethods__ = {}
    for _s in [vector.Vector]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HypreParVector, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _hypre.new_HypreParVector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

        if isinstance(args[-1], list):
        # in this case, ParVector does not own the object
        # in order to prevent python from freeing the input
        # array, object is kept in ParVector
        # args[-1][0]  _data
        # args[-1][0]  col
           self._linked_array = args[-1][0]




    def GetComm(self):
        return _hypre.HypreParVector_GetComm(self)

    def Partitioning(self):
        return _hypre.HypreParVector_Partitioning(self)

    def GlobalSize(self):
        return _hypre.HypreParVector_GlobalSize(self)

    def StealParVector(self):
        return _hypre.HypreParVector_StealParVector(self)

    def SetOwnership(self, own):
        return _hypre.HypreParVector_SetOwnership(self, own)

    def GetOwnership(self):
        return _hypre.HypreParVector_GetOwnership(self)

    def GlobalVector(self):
        return _hypre.HypreParVector_GlobalVector(self)

    def Assign(self, *args):
        return _hypre.HypreParVector_Assign(self, *args)

    def SetData(self, _data):
        return _hypre.HypreParVector_SetData(self, _data)

    def Randomize(self, seed):
        return _hypre.HypreParVector_Randomize(self, seed)

    def Print(self, fname):
        return _hypre.HypreParVector_Print(self, fname)
    __swig_destroy__ = _hypre.delete_HypreParVector
    __del__ = lambda self: None

    def GetPartitioningArray(self):
        return _hypre.HypreParVector_GetPartitioningArray(self)
HypreParVector_swigregister = _hypre.HypreParVector_swigregister
HypreParVector_swigregister(HypreParVector)


def InnerProduct(*args):
    return _hypre.InnerProduct(*args)
InnerProduct = _hypre.InnerProduct

def ParNormlp(vec, p, comm):
    return _hypre.ParNormlp(vec, p, comm)
ParNormlp = _hypre.ParNormlp
class HypreParMatrix(operators.Operator):
    __swig_setmethods__ = {}
    for _s in [operators.Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreParMatrix, name, value)
    __swig_getmethods__ = {}
    for _s in [operators.Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HypreParMatrix, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _hypre.new_HypreParMatrix(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def MakeRef(self, master):
        return _hypre.HypreParMatrix_MakeRef(self, master)

    def GetComm(self):
        return _hypre.HypreParMatrix_GetComm(self)

    def StealData(self):
        return _hypre.HypreParMatrix_StealData(self)

    def SetOwnerFlags(self, diag, offd, colmap):
        return _hypre.HypreParMatrix_SetOwnerFlags(self, diag, offd, colmap)

    def OwnsDiag(self):
        return _hypre.HypreParMatrix_OwnsDiag(self)

    def OwnsOffd(self):
        return _hypre.HypreParMatrix_OwnsOffd(self)

    def OwnsColMap(self):
        return _hypre.HypreParMatrix_OwnsColMap(self)

    def CopyRowStarts(self):
        return _hypre.HypreParMatrix_CopyRowStarts(self)

    def CopyColStarts(self):
        return _hypre.HypreParMatrix_CopyColStarts(self)

    def NNZ(self):
        return _hypre.HypreParMatrix_NNZ(self)

    def RowPart(self, *args):
        return _hypre.HypreParMatrix_RowPart(self, *args)

    def ColPart(self, *args):
        return _hypre.HypreParMatrix_ColPart(self, *args)

    def M(self):
        return _hypre.HypreParMatrix_M(self)

    def N(self):
        return _hypre.HypreParMatrix_N(self)

    def GetDiag(self, *args):
        return _hypre.HypreParMatrix_GetDiag(self, *args)

    def GetOffd(self, offd, cmap):
        return _hypre.HypreParMatrix_GetOffd(self, offd, cmap)

    def GetBlocks(self, blocks, interleaved_rows=False, interleaved_cols=False):
        return _hypre.HypreParMatrix_GetBlocks(self, blocks, interleaved_rows, interleaved_cols)

    def Transpose(self):
        return _hypre.HypreParMatrix_Transpose(self)

    def GetNumRows(self):
        return _hypre.HypreParMatrix_GetNumRows(self)

    def GetNumCols(self):
        return _hypre.HypreParMatrix_GetNumCols(self)

    def GetGlobalNumRows(self):
        return _hypre.HypreParMatrix_GetGlobalNumRows(self)

    def GetGlobalNumCols(self):
        return _hypre.HypreParMatrix_GetGlobalNumCols(self)

    def GetRowStarts(self):
        return _hypre.HypreParMatrix_GetRowStarts(self)

    def GetColStarts(self):
        return _hypre.HypreParMatrix_GetColStarts(self)

    def Mult(self, *args):
        return _hypre.HypreParMatrix_Mult(self, *args)

    def MultTranspose(self, *args):
        return _hypre.HypreParMatrix_MultTranspose(self, *args)

    def BooleanMult(self, alpha, x, beta, y):
        return _hypre.HypreParMatrix_BooleanMult(self, alpha, x, beta, y)

    def __iadd__(self, B):
        return _hypre.HypreParMatrix___iadd__(self, B)

    def Add(self, beta, B):
        return _hypre.HypreParMatrix_Add(self, beta, B)

    def LeftDiagMult(self, D, row_starts=None):
        return _hypre.HypreParMatrix_LeftDiagMult(self, D, row_starts)

    def ScaleRows(self, s):
        return _hypre.HypreParMatrix_ScaleRows(self, s)

    def InvScaleRows(self, s):
        return _hypre.HypreParMatrix_InvScaleRows(self, s)

    def __imul__(self, s):
        val = _hypre.HypreParMatrix___imul__(self, s)

        #    val.thisown = 0
        return self


        return val


    def Threshold(self, threshold=0.0):
        return _hypre.HypreParMatrix_Threshold(self, threshold)

    def EliminateZeroRows(self):
        return _hypre.HypreParMatrix_EliminateZeroRows(self)

    def EliminateRowsCols(self, *args):
        return _hypre.HypreParMatrix_EliminateRowsCols(self, *args)

    def Print(self, fname, offi=0, offj=0):
        return _hypre.HypreParMatrix_Print(self, fname, offi, offj)

    def Read(self, comm, fname):
        return _hypre.HypreParMatrix_Read(self, comm, fname)
    __swig_destroy__ = _hypre.delete_HypreParMatrix
    __del__ = lambda self: None

    def GetType(self):
        return _hypre.HypreParMatrix_GetType(self)

    def GetRowPartArray(self):
        return _hypre.HypreParMatrix_GetRowPartArray(self)

    def GetColPartArray(self):
        return _hypre.HypreParMatrix_GetColPartArray(self)

    def get_local_nnz(self):
        return _hypre.HypreParMatrix_get_local_nnz(self)

    def GetCooDataArray(self, base_i=0, base_j=0):
        return _hypre.HypreParMatrix_GetCooDataArray(self, base_i, base_j)
HypreParMatrix_swigregister = _hypre.HypreParMatrix_swigregister
HypreParMatrix_swigregister(HypreParMatrix)


def add_sparse(*args):
    return _hypre.add_sparse(*args)
add_sparse = _hypre.add_sparse

def ParMult(A, B):
    return _hypre.ParMult(A, B)
ParMult = _hypre.ParMult

def RAP(*args):
    return _hypre.RAP(*args)
RAP = _hypre.RAP

def EliminateBC(A, Ae, ess_dof_list, X, B):
    return _hypre.EliminateBC(A, Ae, ess_dof_list, X, B)
EliminateBC = _hypre.EliminateBC
class HypreSmoother(operators.Solver):
    __swig_setmethods__ = {}
    for _s in [operators.Solver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreSmoother, name, value)
    __swig_getmethods__ = {}
    for _s in [operators.Solver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HypreSmoother, name)
    __repr__ = _swig_repr
    Jacobi = _hypre.HypreSmoother_Jacobi
    l1Jacobi = _hypre.HypreSmoother_l1Jacobi
    l1GS = _hypre.HypreSmoother_l1GS
    l1GStr = _hypre.HypreSmoother_l1GStr
    lumpedJacobi = _hypre.HypreSmoother_lumpedJacobi
    GS = _hypre.HypreSmoother_GS
    Chebyshev = _hypre.HypreSmoother_Chebyshev
    Taubin = _hypre.HypreSmoother_Taubin
    FIR = _hypre.HypreSmoother_FIR

    def __init__(self, *args):
        this = _hypre.new_HypreSmoother(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def SetType(self, type, relax_times=1):
        return _hypre.HypreSmoother_SetType(self, type, relax_times)

    def SetSOROptions(self, relax_weight, omega):
        return _hypre.HypreSmoother_SetSOROptions(self, relax_weight, omega)

    def SetPolyOptions(self, poly_order, poly_fraction):
        return _hypre.HypreSmoother_SetPolyOptions(self, poly_order, poly_fraction)

    def SetTaubinOptions(self, arg2, mu, iter):
        return _hypre.HypreSmoother_SetTaubinOptions(self, arg2, mu, iter)

    def SetWindowByName(self, window_name):
        return _hypre.HypreSmoother_SetWindowByName(self, window_name)

    def SetWindowParameters(self, a, b, c):
        return _hypre.HypreSmoother_SetWindowParameters(self, a, b, c)

    def SetFIRCoefficients(self, max_eig):
        return _hypre.HypreSmoother_SetFIRCoefficients(self, max_eig)

    def SetPositiveDiagonal(self, pos=True):
        return _hypre.HypreSmoother_SetPositiveDiagonal(self, pos)

    def SetOperator(self, op):
        return _hypre.HypreSmoother_SetOperator(self, op)

    def Mult(self, *args):
        return _hypre.HypreSmoother_Mult(self, *args)
    __swig_destroy__ = _hypre.delete_HypreSmoother
    __del__ = lambda self: None
HypreSmoother_swigregister = _hypre.HypreSmoother_swigregister
HypreSmoother_swigregister(HypreSmoother)

class HypreSolver(operators.Solver):
    __swig_setmethods__ = {}
    for _s in [operators.Solver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [operators.Solver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HypreSolver, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetupFcn(self):
        return _hypre.HypreSolver_SetupFcn(self)

    def SolveFcn(self):
        return _hypre.HypreSolver_SolveFcn(self)

    def SetOperator(self, op):
        return _hypre.HypreSolver_SetOperator(self, op)

    def Mult(self, *args):
        return _hypre.HypreSolver_Mult(self, *args)
    __swig_destroy__ = _hypre.delete_HypreSolver
    __del__ = lambda self: None
HypreSolver_swigregister = _hypre.HypreSolver_swigregister
HypreSolver_swigregister(HypreSolver)

class HyprePCG(HypreSolver):
    __swig_setmethods__ = {}
    for _s in [HypreSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HyprePCG, name, value)
    __swig_getmethods__ = {}
    for _s in [HypreSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HyprePCG, name)
    __repr__ = _swig_repr

    def __init__(self, _A):
        this = _hypre.new_HyprePCG(_A)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def SetTol(self, tol):
        return _hypre.HyprePCG_SetTol(self, tol)

    def SetMaxIter(self, max_iter):
        return _hypre.HyprePCG_SetMaxIter(self, max_iter)

    def SetLogging(self, logging):
        return _hypre.HyprePCG_SetLogging(self, logging)

    def SetPrintLevel(self, print_lvl):
        return _hypre.HyprePCG_SetPrintLevel(self, print_lvl)

    def SetPreconditioner(self, precond):
        return _hypre.HyprePCG_SetPreconditioner(self, precond)

    def SetResidualConvergenceOptions(self, res_frequency=-1, rtol=0.0):
        return _hypre.HyprePCG_SetResidualConvergenceOptions(self, res_frequency, rtol)

    def SetZeroInintialIterate(self):
        return _hypre.HyprePCG_SetZeroInintialIterate(self)

    def GetNumIterations(self, num_iterations):
        return _hypre.HyprePCG_GetNumIterations(self, num_iterations)

    def SetupFcn(self):
        return _hypre.HyprePCG_SetupFcn(self)

    def SolveFcn(self):
        return _hypre.HyprePCG_SolveFcn(self)

    def Mult(self, *args):
        return _hypre.HyprePCG_Mult(self, *args)
    __swig_destroy__ = _hypre.delete_HyprePCG
    __del__ = lambda self: None
HyprePCG_swigregister = _hypre.HyprePCG_swigregister
HyprePCG_swigregister(HyprePCG)

class HypreGMRES(HypreSolver):
    __swig_setmethods__ = {}
    for _s in [HypreSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreGMRES, name, value)
    __swig_getmethods__ = {}
    for _s in [HypreSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HypreGMRES, name)
    __repr__ = _swig_repr

    def __init__(self, _A):
        this = _hypre.new_HypreGMRES(_A)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def SetTol(self, tol):
        return _hypre.HypreGMRES_SetTol(self, tol)

    def SetMaxIter(self, max_iter):
        return _hypre.HypreGMRES_SetMaxIter(self, max_iter)

    def SetKDim(self, dim):
        return _hypre.HypreGMRES_SetKDim(self, dim)

    def SetLogging(self, logging):
        return _hypre.HypreGMRES_SetLogging(self, logging)

    def SetPrintLevel(self, print_lvl):
        return _hypre.HypreGMRES_SetPrintLevel(self, print_lvl)

    def SetPreconditioner(self, precond):
        return _hypre.HypreGMRES_SetPreconditioner(self, precond)

    def SetZeroInintialIterate(self):
        return _hypre.HypreGMRES_SetZeroInintialIterate(self)

    def SetupFcn(self):
        return _hypre.HypreGMRES_SetupFcn(self)

    def SolveFcn(self):
        return _hypre.HypreGMRES_SolveFcn(self)

    def Mult(self, *args):
        return _hypre.HypreGMRES_Mult(self, *args)
    __swig_destroy__ = _hypre.delete_HypreGMRES
    __del__ = lambda self: None
HypreGMRES_swigregister = _hypre.HypreGMRES_swigregister
HypreGMRES_swigregister(HypreGMRES)

class HypreIdentity(HypreSolver):
    __swig_setmethods__ = {}
    for _s in [HypreSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreIdentity, name, value)
    __swig_getmethods__ = {}
    for _s in [HypreSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HypreIdentity, name)
    __repr__ = _swig_repr

    def SetupFcn(self):
        return _hypre.HypreIdentity_SetupFcn(self)

    def SolveFcn(self):
        return _hypre.HypreIdentity_SolveFcn(self)
    __swig_destroy__ = _hypre.delete_HypreIdentity
    __del__ = lambda self: None

    def __init__(self):
        this = _hypre.new_HypreIdentity()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
HypreIdentity_swigregister = _hypre.HypreIdentity_swigregister
HypreIdentity_swigregister(HypreIdentity)

class HypreDiagScale(HypreSolver):
    __swig_setmethods__ = {}
    for _s in [HypreSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreDiagScale, name, value)
    __swig_getmethods__ = {}
    for _s in [HypreSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HypreDiagScale, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _hypre.new_HypreDiagScale(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def SetupFcn(self):
        return _hypre.HypreDiagScale_SetupFcn(self)

    def SolveFcn(self):
        return _hypre.HypreDiagScale_SolveFcn(self)

    def GetData(self):
        return _hypre.HypreDiagScale_GetData(self)
    __swig_destroy__ = _hypre.delete_HypreDiagScale
    __del__ = lambda self: None
HypreDiagScale_swigregister = _hypre.HypreDiagScale_swigregister
HypreDiagScale_swigregister(HypreDiagScale)

class HypreParaSails(HypreSolver):
    __swig_setmethods__ = {}
    for _s in [HypreSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreParaSails, name, value)
    __swig_getmethods__ = {}
    for _s in [HypreSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HypreParaSails, name)
    __repr__ = _swig_repr

    def __init__(self, A):
        this = _hypre.new_HypreParaSails(A)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def SetSymmetry(self, sym):
        return _hypre.HypreParaSails_SetSymmetry(self, sym)

    def SetupFcn(self):
        return _hypre.HypreParaSails_SetupFcn(self)

    def SolveFcn(self):
        return _hypre.HypreParaSails_SolveFcn(self)
    __swig_destroy__ = _hypre.delete_HypreParaSails
    __del__ = lambda self: None
HypreParaSails_swigregister = _hypre.HypreParaSails_swigregister
HypreParaSails_swigregister(HypreParaSails)

class HypreBoomerAMG(HypreSolver):
    __swig_setmethods__ = {}
    for _s in [HypreSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreBoomerAMG, name, value)
    __swig_getmethods__ = {}
    for _s in [HypreSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HypreBoomerAMG, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _hypre.new_HypreBoomerAMG(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def SetOperator(self, op):
        return _hypre.HypreBoomerAMG_SetOperator(self, op)

    def SetSystemsOptions(self, dim):
        return _hypre.HypreBoomerAMG_SetSystemsOptions(self, dim)

    def SetElasticityOptions(self, fespace):
        return _hypre.HypreBoomerAMG_SetElasticityOptions(self, fespace)

    def SetPrintLevel(self, print_level):
        return _hypre.HypreBoomerAMG_SetPrintLevel(self, print_level)

    def SetupFcn(self):
        return _hypre.HypreBoomerAMG_SetupFcn(self)

    def SolveFcn(self):
        return _hypre.HypreBoomerAMG_SolveFcn(self)
    __swig_destroy__ = _hypre.delete_HypreBoomerAMG
    __del__ = lambda self: None
HypreBoomerAMG_swigregister = _hypre.HypreBoomerAMG_swigregister
HypreBoomerAMG_swigregister(HypreBoomerAMG)

class HypreAMS(HypreSolver):
    __swig_setmethods__ = {}
    for _s in [HypreSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreAMS, name, value)
    __swig_getmethods__ = {}
    for _s in [HypreSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HypreAMS, name)
    __repr__ = _swig_repr

    def __init__(self, A, edge_fespace):
        this = _hypre.new_HypreAMS(A, edge_fespace)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def SetPrintLevel(self, print_lvl):
        return _hypre.HypreAMS_SetPrintLevel(self, print_lvl)

    def SetSingularProblem(self):
        return _hypre.HypreAMS_SetSingularProblem(self)

    def SetupFcn(self):
        return _hypre.HypreAMS_SetupFcn(self)

    def SolveFcn(self):
        return _hypre.HypreAMS_SolveFcn(self)
    __swig_destroy__ = _hypre.delete_HypreAMS
    __del__ = lambda self: None
HypreAMS_swigregister = _hypre.HypreAMS_swigregister
HypreAMS_swigregister(HypreAMS)

class HypreADS(HypreSolver):
    __swig_setmethods__ = {}
    for _s in [HypreSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreADS, name, value)
    __swig_getmethods__ = {}
    for _s in [HypreSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HypreADS, name)
    __repr__ = _swig_repr

    def __init__(self, A, face_fespace):
        this = _hypre.new_HypreADS(A, face_fespace)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def SetPrintLevel(self, print_lvl):
        return _hypre.HypreADS_SetPrintLevel(self, print_lvl)

    def SetupFcn(self):
        return _hypre.HypreADS_SetupFcn(self)

    def SolveFcn(self):
        return _hypre.HypreADS_SolveFcn(self)
    __swig_destroy__ = _hypre.delete_HypreADS
    __del__ = lambda self: None
HypreADS_swigregister = _hypre.HypreADS_swigregister
HypreADS_swigregister(HypreADS)

class HypreLOBPCG(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreLOBPCG, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HypreLOBPCG, name)
    __repr__ = _swig_repr

    def __init__(self, comm):
        this = _hypre.new_HypreLOBPCG(comm)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _hypre.delete_HypreLOBPCG
    __del__ = lambda self: None

    def SetTol(self, tol):
        return _hypre.HypreLOBPCG_SetTol(self, tol)

    def SetMaxIter(self, max_iter):
        return _hypre.HypreLOBPCG_SetMaxIter(self, max_iter)

    def SetPrintLevel(self, logging):
        return _hypre.HypreLOBPCG_SetPrintLevel(self, logging)

    def SetNumModes(self, num_eigs):
        return _hypre.HypreLOBPCG_SetNumModes(self, num_eigs)

    def SetPrecondUsageMode(self, pcg_mode):
        return _hypre.HypreLOBPCG_SetPrecondUsageMode(self, pcg_mode)

    def SetRandomSeed(self, s):
        return _hypre.HypreLOBPCG_SetRandomSeed(self, s)

    def SetPreconditioner(self, precond):
        return _hypre.HypreLOBPCG_SetPreconditioner(self, precond)

    def SetOperator(self, A):
        return _hypre.HypreLOBPCG_SetOperator(self, A)

    def SetMassMatrix(self, M):
        return _hypre.HypreLOBPCG_SetMassMatrix(self, M)

    def Solve(self):
        return _hypre.HypreLOBPCG_Solve(self)

    def GetEigenvalues(self, eigenvalues):
        return _hypre.HypreLOBPCG_GetEigenvalues(self, eigenvalues)

    def GetEigenvector(self, i):
        return _hypre.HypreLOBPCG_GetEigenvector(self, i)

    def StealEigenvectors(self):
        return _hypre.HypreLOBPCG_StealEigenvectors(self)
HypreLOBPCG_swigregister = _hypre.HypreLOBPCG_swigregister
HypreLOBPCG_swigregister(HypreLOBPCG)

class HypreAME(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HypreAME, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HypreAME, name)
    __repr__ = _swig_repr

    def __init__(self, comm):
        this = _hypre.new_HypreAME(comm)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _hypre.delete_HypreAME
    __del__ = lambda self: None

    def SetTol(self, tol):
        return _hypre.HypreAME_SetTol(self, tol)

    def SetMaxIter(self, max_iter):
        return _hypre.HypreAME_SetMaxIter(self, max_iter)

    def SetPrintLevel(self, logging):
        return _hypre.HypreAME_SetPrintLevel(self, logging)

    def SetNumModes(self, num_eigs):
        return _hypre.HypreAME_SetNumModes(self, num_eigs)

    def SetPreconditioner(self, precond):
        return _hypre.HypreAME_SetPreconditioner(self, precond)

    def SetOperator(self, A):
        return _hypre.HypreAME_SetOperator(self, A)

    def SetMassMatrix(self, M):
        return _hypre.HypreAME_SetMassMatrix(self, M)

    def Solve(self):
        return _hypre.HypreAME_Solve(self)

    def GetEigenvalues(self, eigenvalues):
        return _hypre.HypreAME_GetEigenvalues(self, eigenvalues)

    def GetEigenvector(self, i):
        return _hypre.HypreAME_GetEigenvector(self, i)

    def StealEigenvectors(self):
        return _hypre.HypreAME_StealEigenvectors(self)
HypreAME_swigregister = _hypre.HypreAME_swigregister
HypreAME_swigregister(HypreAME)

# This file is compatible with both classic and new-style classes.


