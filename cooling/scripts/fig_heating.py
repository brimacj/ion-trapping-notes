from common import *
import ion_trapping


def potential_energy(ensemble, B_z, omega, theta, kx, ky, kz):
    energy = 0
    energy += ion_trapping.trap_energy(
            ensemble.x,
            kx, ky, kz, theta,
            ensemble.ensemble_properties['charge'],
            ensemble.ensemble_properties['mass'],
            omega, B_z)
    energy += ion_trapping.coulomb_energy(
            ensemble.x,
            ensemble.ensemble_properties['charge'])
    return energy


def kinetic_energy(ensemble, omega):
    energy = ion_trapping.kinetic_energy(
            ensemble.x, ensemble.v,
            ensemble.ensemble_properties['mass'], omega)
    return energy


def total_energy(ensemble, B_z, omega, theta, kx, ky, kz):
    energy = 0
    energy += potential_energy(ensemble, B_z, omega, theta, kx, ky, kz)
    energy += kinetic_energy(ensemble, omega)
    return energy


dt = 1.0e-9
t_max = 1.0e-8
num_steps = 10
my_ensemble = initial_state.copy()
trap_potential.reset_phase()


kin = [kinetic_energy(my_ensemble, mode_analysis.wrot)]
pot = [potential_energy(my_ensemble,
        mode_analysis.B, mode_analysis.wrot,
        trap_potential.phi,
        trap_potential.kx,
        trap_potential.ky,
        trap_potential.kz)]
t = 0.0
for i in range(num_steps):
    print(i, ' ', t, kin[-1], pot[-1], kin[-1] + pot[-1])
    evolve_ensemble(dt, t_max, my_ensemble, mode_analysis.B,
                    forces + [in_plane_cooling] + axial_cooling)
    t += t_max
    kin.append(kinetic_energy(my_ensemble, mode_analysis.wrot))
    pot.append(potential_energy(my_ensemble,
            mode_analysis.B, mode_analysis.wrot,
            trap_potential.phi,
            trap_potential.kx,
            trap_potential.ky,
            trap_potential.kz))
print(num_steps, ' ', t, kin[-1], pot[-1], kin[-1] + pot[-1])
print(kin)

            
           
