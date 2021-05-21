# encoding: utf-8
# module PyQt5.QtWidgets
# from /home/herizo/anaconda3/lib/python3.8/site-packages/PyQt5/QtWidgets.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QGraphicsTransform import QGraphicsTransform

class QGraphicsRotation(QGraphicsTransform):
    """ QGraphicsRotation(parent: QObject = None) """
    def angle(self): # real signature unknown; restored from __doc__
        """ angle(self) -> float """
        return 0.0

    def angleChanged(self): # real signature unknown; restored from __doc__
        """ angleChanged(self) [signal] """
        pass

    def applyTo(self, QMatrix4x4): # real signature unknown; restored from __doc__
        """ applyTo(self, QMatrix4x4) """
        pass

    def axis(self): # real signature unknown; restored from __doc__
        """ axis(self) -> QVector3D """
        pass

    def axisChanged(self): # real signature unknown; restored from __doc__
        """ axisChanged(self) [signal] """
        pass

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> QVector3D """
        pass

    def originChanged(self): # real signature unknown; restored from __doc__
        """ originChanged(self) [signal] """
        pass

    def setAngle(self, p_float): # real signature unknown; restored from __doc__
        """ setAngle(self, float) """
        pass

    def setAxis(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAxis(self, QVector3D)
        setAxis(self, Qt.Axis)
        """
        pass

    def setOrigin(self, QVector3D): # real signature unknown; restored from __doc__
        """ setOrigin(self, QVector3D) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


