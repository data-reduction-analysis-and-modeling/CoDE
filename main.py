"""
Functionality tests for the CoDE components

           ____________    ____________    _______
          |  Structure |--| Calculator |--| Chart |
           ------------    ------------    -------
                |              /\
                |              ||
                |              \/
                |         ________________
                |        | CrysFML, CCTBX |
                |         ----------------
          _______________
         |  ASE / Babel  |
          ---------------

"""

import numpy as np

from Structure import Structure
from Calculator import Calculator
from Chart import Chart
import xrayutilities as xu

def structure_test():
    """
    Test the Structure module
    Loading/conversion/save
    """
    from ase.visualize import view as ase_viewer

    # file of some type
    test_file = "diamond.pdb"
    dna_file = "dna.pdb"
    fox_file1 = "fox7.car"

    # Generate Structure objects
    diamond = Structure(file=test_file)
    dna = Structure(file=dna_file)
    fox = Structure(file=fox_file1)

    #ase_dna = dna.aseStructure()
    #ase_viewer(ase_dna)

    #ase_diamond = diamond.aseStructure()
    #ase_viewer(ase_diamond)

    ase_fox = fox.aseStructure()
    ase_viewer(ase_fox)


def chart_test():
    """
    Test the Chart module functionality
    """

    pass

def chart_test():

    chart_exp = Chart(filename=some_exp_chart)
    #chart_calc = calc.calculateXRD(structure)

    #is_converged = chart_exp - chart_calc


def calculator_test():
    """
    Test the calculator(s)
    """
    # instantiate default Calculator object
    # and define initial state
    calc = Calculator(structure=diamond, wavelength=1.2)

    # calculate XRD for the structure, using defined engine
    calc.calculateXRD(structure=diamond, engine="ASE")

    # calculate XRD for the structure, using default engine
    #chart = calc.calculateXRD()

    # calculate XRD for the new structure, using default state
    calc.calculateXRD(structure=dna)


    # calculate SANS for the structure, using default engine
    #calc.calculateSANS(structure=diamond)

    # calculate SANS for a new structure, using default engine
    #calc.calculateSANS(structure=dna)

    # xrayutilities
    #calc.calculateXRD(structure=fe)

if __name__ == "__main__":

    structure_test()

    # files for testing
    test_file = "diamond.pdb"
    dna_file = "dna.pdb"
    fox_file1 = "fox7.car"

    # Generate Structure objects for use in calculator_test
    diamond = Structure(file=test_file)
    dna = Structure(file=dna_file)
    fox7_1 = Structure(file=fox_file1)

    calculator_test()

    # Generate Chart objects for use in chart_test
    #test_file1d = "CF3Br.dat"
    #test_file2d = "test2d.dat"
    #chart_1d = Chart(filename=test_file1d)
    #chart_2d = Chart(filename=test_file2d)

    #chart_test()


