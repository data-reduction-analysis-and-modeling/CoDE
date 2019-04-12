"""
CoDE Chart structure
"""
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

import fabio as fabio
# cctbx
# crysfml


class ChartDataPowder(object):
    """
    holder for 1d/2d powder profile data
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

class ChartDataCrystal(object):
    """
    holder for hkl single crystal data
    """
    def __init__(self, parent=None):
        """
        Initialize chart data fields
        """
        # list of h indices
        self.h = None
        # list of k indices
        self.k = None
        # list of l indices
        self.l = None
        # list of intensities
        self.intensity = None
        # list of errors
        self.sigma = None


    def numPoints(self):
        """
        Returns the number of points in the set
        """
        return len(self.intensity)


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

        self.data = None

        # state of this object
        self.state = {}
        self.state['data'] = self.data

        if filename:
            self.load(filename=filename)
            self.state['filename'] = filename

    def setData1D(self, data):
        """
        Grab the 1d data coming from the calculator and convert into ChartDataPowder
        [(x_1,y_1),(x_2, y_2),....] -> ChartDataPowder
        """
        x = []
        y = []
        for tup in data:
            # cheaper to first create full list than to append to immutable np.array
            x.append(tup[0])
            y.append(tup[1])

        # this is now a ChartDataPowder object
        if self.data is None:
            self.data = ChartDataPowder()
        self.data.x = np.array(x)
        self.data.y = np.array(y)

        # TODO: extend to dx, dy etc.

    def setDataHKL(self, data):
        """
        Grab the hkl data coming from the calculator and convert into ChartDataCrystal
        [(h,k,l,int), ....] -> ChartDataCrystal
        """
        h = []
        k = []
        l = []
        for tup in data:
            # cheaper to first create full list than to append to immutable np.array
            x.append(tup[0])
            y.append(tup[1])

        self.data.x = np.array(x)
        self.data.y = np.array(y)

        # TODO: extend to dx, dy etc.

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
        plt.clf()  # clear figure
        ax = plt.gca()

        ax.plot(self.data.x, self.data.y / np.max(self.data.y), '.-')
        ax.set_xlabel('2$\\theta$')
        ax.set_ylabel('Intensity')

        #self.mplChart = ax
        self.state['mpl'] = plt

    def getMplChart(self):
        """
        Return the matplotlib representation of the current chart
        """
        if 'mpl' not in self.state:
            self.setMplChart()

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

    def show(self):
        """
        Show the current document
        """
        if not 'mpl' in self.state:
            self.setMplChart()

        plt.show()

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

