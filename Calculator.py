"""
CoDE Calculator class
"""

from Structure import Structure
import importlib

class Calculator(object):
    """
    Base class for calculators
    """

    # Default calculators for properties.
    # This will contain all types of structure and chart calculations
    DEFAULT_ENGINE = {'XRD': 'ASE',
                      'SANS': 'ASE'}

    def __init__(self, parent=None,
                 structure=None,
                 wavelength=None,
                ):
        """
        The constructor takes structure and other properties.
        This will define the state of the calculator.
        Quick calculations with overriden properties can be performed
        by calling calculate methods with extra arguments.
        """
        self.parent = parent

        # simple dictionary defining calculator state.
        # Currently it only holds 'wavelength' for testing
        self.parameters = {}

        # Active calculator plugin. Can change depending on what needs to be evaluated
        self.activePlugin = None

        if structure is not None:
            self.parameters['structure'] = structure
        if wavelength is not None:
            self.parameters['wavelength'] = wavelength

    @property
    def structure(self):
        return self.parameters['structure']

    @structure.setter
    def structure(self, value):
        self.parameters['structure'] = value

    @property
    def wavelength(self):
        return self.parameters['wavelength']

    @wavelength.setter
    def wavelength(self, value):
        self.parameters['wavelength'] = value

    def loadPlugin(self, engine=""):
        """
        Instantiate a 3rd party computational plugin
        """
        # see if we have the right engine
        if self.activePlugin is None or self.activePlugin.name() != engine:
            self.activePlugin = self.createPlugin(engine)

    def createPlugin(self, engine=""):
        """
        Create an instance of a computational plugin, based on engine name.
        """
        module_name = "CalcPlugin_"+engine
        method_module = importlib.import_module(module_name)
        method_to_call = getattr(method_module, module_name)

        return method_to_call()

    def calculateXRD(self, structure=None, engine="", wavelength=None):
        """
        calculate simple diffraction pattern on atoms
        """
        if not engine:
            engine = self.DEFAULT_ENGINE['XRD']
        self.loadPlugin(engine)

        # Make sure the plugin can calculate this property
        if not self.activePlugin.canCalculate('XRD'):
            raise RuntimeError("Requested calculation engine can't be used to calculate XRD.")

        # check the argument list
        if structure is None:
            if 'structure' not in self.parameters:
                # no structure -> bail out
                raise RuntimeError ("No active structure!")
            else:
                structure = self.parameters['structure']

        if wavelength is None:
            # check the Calculator dictionary
            if 'wavelength' in self.parameters:
                wavelength = self.parameters['wavelength']

        # Fall back to default
        if wavelength is None:
            wavelength = 1.5405981

        # call the XRD method on the ASE calculator plugin
        self.activePlugin.getProperty('XRD', structure=structure, wavelength=wavelength)


    def calculateSANS(self, structure=None, engine="", wavelength=None):
        """
        calculate simple diffraction pattern on atoms
        """
        if not engine:
            engine = self.DEFAULT_ENGINE['SANS']
        self.loadPlugin(engine)

        # Make sure the plugin can calculate this property
        if not self.activePlugin.canCalculate('SANS'):
            raise RuntimeError("Requested calculation engine can't be used to calculate SANS.")

        # check the argument list
        if structure is None:
            if 'structure' not in self.parameters:
                # no structure -> bail out
                raise RuntimeError ("No active structure!")
            else:
                structure = self.parameters['structure']

        if wavelength is None:
            # check the Calculator dictionary
            if 'wavelength' in self.parameters:
                wavelength = self.parameters['wavelength']

        # Fall back to default
        if wavelength is None:
            wavelength = 1.5405981

        self.activePlugin.getProperty('SANS', structure=structure, wavelength=wavelength)

    def calculateQPA(self, structure=None):
        """
        Perform Quantitative Phase Analysis
        """
        pass

    def calculateCrystallinity(self, structure=None):
        """
        Perform degree of crystallinity calculations
        """
        pass

    def __eq__(self, other):
        """
        Default behaviour for =
        """
        #if isinstance(other, Calculator):
        #    return self.number == other.number
        return False
