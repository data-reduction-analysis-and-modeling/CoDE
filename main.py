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
    #ase_viewer(ase_fox)


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
    calc = Calculator(structure=dna, wavelength=1.2)

    # calculate XRD for the structure, using defined engine
    #data_out = calc.calculateXRD(structure=diamond, engine="ASE")

    # calculate XRD for the structure, using default engine
    data_out = calc.calculateXRD()

    # create a chart object
    chart = Chart()

    # add powder data to the chart. This needs to be made such that
    # setData doesn't need a type (setData1D/setDataCrystal) but rather 
    # gets set depending on the type of the argument passed
    chart.setData1D(data_out)

    # create MPL representation of the Chart object
    #mpl_chart = chart.getMplChart()
    #mpl_chart.show()

    # or just show it directly
    chart.show()


if __name__ == "__main__":

    #structure_test()

    # files for testing
    test_file = "diamond.pdb"
    dna_file = "dna.pdb"
    fox_file1 = "fox7.car"

    # Generate Structure objects for use in calculator_test
    diamond = Structure(file=test_file)
    dna = Structure(file=dna_file)
    fox7_1 = Structure(file=fox_file1)

    calculator_test()

