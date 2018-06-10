#ifndef ION_TRAPPING_LIB_H
#define ION_TRAPPING_LIB_H


void angular_damping(
	int num_ptcls,
	double omega,
	double kappa_dt,
	const double *x,
	double *v
	);

void axial_damping(
	int num_ptcls,
	double kappa_dt,
	double *v
	);

double coulomb_energy(
	int num_ptcls,
	const double *x,
	double charge);

double coulomb_energy_per_particle_charge(
	int num_ptcls,
	const double *x,
	const double *charge);

double trap_energy(
	int num_ptcls,
	const double *x,
	double kx,
	double ky,
	double kz,
	double theta,
	double charge,
	double mass,
	double omega,
	double B_z);

double kinetic_energy(
	int num_ptcls,
	const double *x,
	const double *v,
	double mass,
	double omega);

double kinetic_energy_in_plane(
	int num_ptcls,
	const double *x,
	const double *v,
	double mass,
	double omega);

double kinetic_energy_out_of_plane(
	int num_ptcls,
	const double *x,
	const double *v,
	double mass);


#endif
