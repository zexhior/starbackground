# encoding: utf-8
# module PyQt5.QtSensors
# from /home/herizo/anaconda3/lib/python3.8/site-packages/PyQt5/QtSensors.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QSensorReading import QSensorReading

class QLidReading(QSensorReading):
    # no doc
    def backLidChanged(self, bool): # real signature unknown; restored from __doc__
        """ backLidChanged(self, bool) [signal] """
        pass

    def backLidClosed(self): # real signature unknown; restored from __doc__
        """ backLidClosed(self) -> bool """
        return False

    def frontLidChanged(self, bool): # real signature unknown; restored from __doc__
        """ frontLidChanged(self, bool) [signal] """
        pass

    def frontLidClosed(self): # real signature unknown; restored from __doc__
        """ frontLidClosed(self) -> bool """
        return False

    def setBackLidClosed(self, bool): # real signature unknown; restored from __doc__
        """ setBackLidClosed(self, bool) """
        pass

    def setFrontLidClosed(self, bool): # real signature unknown; restored from __doc__
        """ setFrontLidClosed(self, bool) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


