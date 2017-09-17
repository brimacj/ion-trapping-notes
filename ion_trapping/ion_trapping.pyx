import cython
import numpy as np
cimport numpy as np
cimport ion_trapping_lib


@cython.boundscheck(False)
@cython.wraparound(False)
def angular_damping(omega, kappa_theta,
                    np.ndarray[double, ndim=2, mode="c"] x not None,
                    np.ndarray[double, ndim=2, mode="c"] v not None):
    assert(x.shape[1] == 3)
    assert(v.shape[1] == 3)
    assert(x.shape[0] == v.shape[0])

    cdef num_ptcls
    num_ptcls = x.shape[0]

    ion_trapping_lib.angular_damping(
        num_ptcls,
        omega,
        kappa_theta,
        &x[0, 0],
        &v[0, 0]
    )


@cython.boundscheck(False)
@cython.wraparound(False)
def axial_damping(kappa_theta,
                  np.ndarray[double, ndim=2, mode="c"] v not None):
    assert(v.shape[1] == 3)

    cdef num_ptcls
    num_ptcls = v.shape[0]

    ion_trapping_lib.axial_damping(
        num_ptcls,
        kappa_theta,
        &v[0, 0]
    )
