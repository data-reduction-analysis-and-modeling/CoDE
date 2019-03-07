"""
CoDE Atom structure
"""

class Chart(object):
    """
    Generic object for various charts
    """
    def __init__(self, parent=None, filename=""):
        """
        """
        self._chart = None
        #self._radiation = Radiation()
        self.dimension = 1
        self.filename = filename

        # state of this object
        self.state = {}
        if filename:
            self.load(filename=filename)
            self.state['filename'] = filename

    def load(self, filename=""):
        """
        Load the data and set the state
        """
        pass

    def setMplChart(self, chart=None):
        """
        Assign a matplotlib chart to the state
        """

    def getMplChart(self):
        """
        Return the matplotlib representation of the current chart
        """
        return self.state['mpl']

    def evaluateBackground(self):
        """
        Find background
        """
        pass

    def subtractBackground(self):
        """
        Subtract found background
        """
        pass

    def indexPeaks(self):
        """
        peak indexing algorithms...
        """
        pass

    def refinePeaks(self):
        """
        Pawley peak finding refinements
        """
        pass

class PowderDiffractionChart(Chart):
    """
    2-theta chart of powder diffraction
    """
    def smoothPattern(self):
        """
        Apply a data smoothing algorithm on an experimental diffraction pattern
        """
        pass

    def scalePattern(self):
        """
        Perform scaling on an experimental diffraction pattern
        """
        pass

    def calculateStructure(self):
        """
        Perform SA/PT calculations to determine crystal structure
        """
        pass 

class CrystalDiffractionChart(Chart):
    """
    2D diffraction chart for crystal diff
    """
    pass

