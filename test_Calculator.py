###########################################################
#
#  pytest runner for the Calculator class
#
###########################################################

import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath)

from Calculator import Calculator
from Structure import Structure
from PluginBase import PluginBase
from CalcPlugin_ASE import CalcPlugin_ASE

test_file = "diamond.pdb"
dna_file = "dna.pdb"

# Generate Structure objects
diamond = Structure(file=test_file)
dna = Structure(file=dna_file)


def test_calculator_default():

    calc = Calculator()

    assert calc.parameters == {}

    assert calc.DEFAULT_ENGINE['XRD'] == 'ASE'
    assert calc.DEFAULT_ENGINE['SANS'] == 'ASE'
    assert calc.activePlugin == None
    calc.loadPlugin(engine="ASE")
    assert isinstance(calc.activePlugin, CalcPlugin_ASE) == True

def test_calculator_arg_structure():

    calc = Calculator(structure=diamond, wavelength=1.2)

    assert calc.parameters['structure'] == diamond
    assert calc.parameters['wavelength'] == 1.2

    assert calc.activePlugin == None
    calc.loadPlugin(engine="ASE")
    assert isinstance(calc.activePlugin, CalcPlugin_ASE) == True

def test_override_arguments():

    calc = Calculator(structure=diamond, wavelength=1.5)

    calc.structure = dna
    calc.wavelength = 1.1

    assert calc.parameters['structure'] == dna
    assert calc.parameters['wavelength'] == 1.1
    assert calc.structure == dna
    assert calc.wavelength == 1.1


def test_calculator_load_plugin():

    calc = Calculator(structure=diamond, wavelength=1.5)

    with pytest.raises(ModuleNotFoundError):
        calc.loadPlugin(engine="boop")
    
