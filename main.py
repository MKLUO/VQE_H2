# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:11:06 2018

@author: Aenna
"""
from qis_module import *
from utils import *

# Coefficients of the Bravyi-Kitaev transformed Hamiltonian of varius distances
from xlrd import open_workbook


def run():

    qis_module_init()

    # Precomputed B-K transformed Hamiltonian coefficients
    atom_configs = []
    wb = open_workbook('BKH_coef.xlsx')
    sheet = wb.sheets()[0]
    for row in range(1, sheet.nrows):

        r = sheet.cell(row, 0).value

        coefs = {}
        for col in range(1, sheet.ncols):
            coefs[str(sheet.cell(0, col).value)] = sheet.cell(row, col).value

        atom_config = Atom_config(r, coefs)
        atom_configs.append(atom_config)

    # Loop over varius atomic distances
    energy_min = 0.
    distance_min = 0.
    for atom_config in atom_configs:

        if atom_config.r < MIN_R or atom_config.r > MAX_R:
            continue

        print('Simulating distance: ' + str(atom_config.r))

        # Loop over varius input state parameter

        energy = 0.
        for theta in thetas:

            # print('.', end='', flush=True)

            # Loop over measurements
            energy_temp = 0.
            for measure in measure_tasks:

                # Simulation
                energy_temp += atom_config.coefs[measure] * \
                    Vqe_h2_task(theta, measure)

            # Update minimum energy

            print('energy_temp: ' + str(energy_temp) + ' at theta ' + str(theta))

            if energy_temp < energy:
                energy = energy_temp
                       
        """
        ######### MANUALLY SET THETA TO SOME VALUE

        energy = 0.

        for measure in measure_tasks:
            # Simulation
            energy += atom_config.coefs[measure] * \
                Vqe_h2_task(0.1 * pi, measure)

 

        ######### MANUALLY SET THETA TO SOME VALUE (END)
        """
        print('energy: ' + str(energy) + '\n')

        # Record minimum energy
        if energy < energy_min:
            energy_min = energy
            distance_min = atom_config.r

    print(energy_min, distance_min)

if __name__ == "__main__":
    run()
