from typing import List
from typing import NewType
from ase import Atoms as ASE_Atoms
from ase.io import read

StringList = List[str]

class Atom(object):
    """
    CoDE Atom structure, based on ASE Atom
    """
    def __init__(self, parent=None)->None:
        self._atom = None
        pass

    def symbol(self)-> str:
        """
        Return atomic symbol
        """
        return self._symbol

class Cell(object):
    """
    CoDE Cell structure, based on ASE Atom.Cell
    """
    def __init__(self, parent=None)->None:
        pass

class Atoms(object):
    """
    CoDE Atoms structure, based on ASE Atoms
    """
    def __init__(self, parent=None, symbols:StringList=None, cell:Cell=None)->None:
        if symbols is not None:
            self._atoms = self.createFromSymbols(symbols)
            #self.aseAtoms = self.createASEAtomsFromSymbols(symbols)
        pass
    
    def createFromSymbols(self, symbols:StringList=None) -> list:
        """
        Create Atoms structure based on passed list of atoms
        """
        pass

    # def createASEAtomsFromSymbols(self, symbols:StringList=None) -> list:
    #     """
    #     Create ASE Atoms structure based on passed list of atoms
    #     """
    #     pass

class Structure(object):
    def __init__(self, file=None, atoms_represenatation=None):

        self._atoms = None # ASE Atoms object
        self._cell = None  # External representation of the cell
        self._bonds = None
        self._symmetry = None
        if file is not None:
            self.load(file)

    def create(self, formula=None):
        """
        Wrapper for ASE atoms generator
        """
        self._atoms = Atoms(symbols=formula)

    def create3D(self, formula=None, cell=None):
        """
        Wrapper for ASE atoms+cell generator
        """
        self._atoms = Atoms(symbols=formula, cell=cell)

    def load(self, file=None):
        """
        Load structure from file
        """
        # assume file can be read from within ASE
        self._atoms = read(file)
        
    def aseStructure(self):
        """
        Return the ASE representation of the Atoms in Structure
        """
        return self._atoms
