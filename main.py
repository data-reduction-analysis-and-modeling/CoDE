"""
Initial test for the CoDE ifrastructure layout

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

Used for testing/defining of the data flow between modules.
"""
import numpy as np

from Structure import Structure
from Calculator import Calculator

if __name__ == "__main__":

    # file of some type
    test_file = "diamond.pdb"
    dna_file = "dna.pdb"

    # Generate Structure objects
    diamond = Structure(file=test_file)
    dna = Structure(file=dna_file)

    # instantiate default Calculator object
    # and define initial state
    calc = Calculator(structure=diamond, wavelength=1.2)

    # calculate XRD for the structure, using defined engine
    # calc.calculateXRD(structure=diamond, engine="ASE")

    # calculate XRD for the structure, using default engine
    # calc.calculateXRD()

    # calculate XRD for the new structure, using default state
    calc.calculateXRD(structure=dna)


    # calculate SANS for the structure, using default engine
    #calc.calculateSANS(structure=diamond)

    # calculate SANS for a new structure, using default engine
    calc.calculateSANS(structure=dna)

