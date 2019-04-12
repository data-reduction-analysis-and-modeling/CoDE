"""
CoDE Atom structure
"""
# image loaders
import fabio as fabio
# cctbx
# crysfml


class ChartData(object):
    """
    holder for 1d/2d profile data
    """
    def __init__(self, parent=None):
        """
        Initialize chart data fields
        """
        # list of x coordinates
        self.x = None
        # list of y coordinates
        self.y = None
        # list of x coordinate errors
        self.dx = None
        # list of y coordinate errors
        self.dy = None
        # list of intensities up
        self.iup = None
        # list of intensities down
        self.idown = None


    def numPoints(self):
        """
        Returns the number of points in the set
        """
        return len(self.x) * len(self.y)


class Chart(object):
    """
    Generic object for various charts
    """
    def __init__(self, parent=None, filename=""):
        """
        """
        #self._radiation = Radiation()
        self.dimension = 1
        self.filename = filename

        self.data = ChartData(self)

        # state of this object
        self.state = {}
        if filename:
            self.load(filename=filename)
            self.state['filename'] = filename

    def load(self, filename=""):
        """
        Load the data and set the state
        """
        # use fabio
        try:
            image = fabio.open(filename)
        except Exception as ex:
            print("Something bad happened: " + str(ex))
            return
        # convert fabio object into ChartData
        self.data = self.fabioToChart(image=image)

    def fabioToChart(self, image=None):
        """
        Convert fabio object to our ChartData
        """
        chart_data = ChartData()

        for row in image.rows():
            chart_data

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

