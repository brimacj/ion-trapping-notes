#ifndef ION_TRAPPING_LIB_H
#define ION_TRAPPING_LIB_H


int foo();
void angular_damping(
	int num_ptcls,
	double omega,
	double kappa_dt,
	const double *x,
	double *v
	);

#endif
