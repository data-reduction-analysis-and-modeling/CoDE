"""
Base class for plugins exposing 3rd party computational backends.

Plugins are just wrappers for property calls to backends.

No state should be kept in the instance. Everything should be passed from the Calculator.
"""

class PluginBase(object):
    """
    """
    def __init__(self, parent=None):
        """
        """
        pass

    def name(self):
        """
        plugin name getter
        """
        assert("VIRTUAL METHOD NOT IMPLEMENTED")

    def canCalculate(self, prop=None):
        """
        Check if this plugin can calculate requested property
        """
        assert("VIRTUAL METHOD NOT IMPLEMENTED")

    def startBackend(self, **kwargs):
        """
        Start/connect to the 3rd party backend
        """
        assert("VIRTUAL METHOD NOT IMPLEMENTED")

    def getProperty(self, prop="", **kwargs):
        """
        Translate generic Calculator request for property into local method call
        """
        assert("VIRTUAL METHOD NOT IMPLEMENTED")
        
