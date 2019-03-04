import numpy as np

from ase.utils.xrdebye import XrDebye, wavelengths
from PluginBase import PluginBase

class CalcPlugin_ASE(PluginBase):
    """
    """
    AVAILABLE_PROPERTIES = ["XRD",
                            "SANS"]

    def __init__(self, parent=None):
        """
        no state here
        """
        self._name = "ASE"
        pass

    # base method overrides
    def name(self):
        """
        plugin name getter
        """
        return self._name

    def canCalculate(self, prop=None):
        """
        Check if this plugin can calculate requested property
        """
        if prop is None:
            return True
        if prop.upper() in self.AVAILABLE_PROPERTIES:
            return True
        else:
            return False

    def startBackend(self, **kwargs):
        """
        Start/connect to the 3rd party backend
        """
        # Nothing to start for ASE
        pass
   
    def getProperty(self, prop="", **kwargs):
        """
        """
        if not prop:
            return None

        prop = prop.upper()
        if not self.canCalculate(prop):
            txt = "The ASE plugin does not support calculations of " + prop + "."
            raise NotImplementedError(txt)
        
        # get the property from ASE
        method_name = "get"+prop
        method = getattr(self, method_name)

        try:
            result = method(**kwargs)
        except Exception as ex:
            # re-raise with meaningful message
            msg = "ASE Calculation of " +prop+ " failed with: \n"
            msg += str(ex)
            raise RuntimeError()
        return result

    # Property calculate wrappers
    def getXRD(self, **kwargs):
        """
        calculate XRD
        """
        wavelength = None
        if 'wavelength' in kwargs:
            wavelength = kwargs['wavelength']
        if 'structure' not in kwargs:
            raise NameError("Structure not found!")
        structure = kwargs['structure']

        if wavelength is None or structure is None:
            raise RuntimeError("ASE Calculator cannot evaluate XRD - not enough parameters!")

        ase_atoms = structure.aseStructure()

        xrd_object = XrDebye(atoms=ase_atoms, wavelength=wavelength)
        xrd_object.calc_pattern(x=np.arange(15, 30, 0.1), mode='XRD')
        xrd_object.plot_pattern(filename=None)

    def getSANS(self, **kwargs):
        """
        calculate XRD
        """
        wavelength = None
        if 'wavelength' in kwargs:
            wavelength = kwargs['wavelength']
        if 'structure' not in kwargs:
            raise NameError("Structure not found!")
        structure = kwargs['structure']
        
        if wavelength is None or structure is None:
            raise RuntimeError("ASE Calculator cannot evaluate SANS - not enough parameters!")
            
        ase_atoms = structure.aseStructure()

        xrd_object = XrDebye(atoms=ase_atoms, wavelength=wavelength)
        xrd_object.calc_pattern(x=np.logspace(-2, -0.3, 50), mode='SAXS')
        xrd_object.plot_pattern(filename=None)

