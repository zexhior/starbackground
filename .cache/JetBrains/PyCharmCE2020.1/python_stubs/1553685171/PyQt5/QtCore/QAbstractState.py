# encoding: utf-8
# module PyQt5.QtCore
# from /home/herizo/anaconda3/lib/python3.8/site-packages/PyQt5/QtCore.so
# by generator 1.147
# no doc
# no imports

from .QObject import QObject

class QAbstractState(QObject):
    """ QAbstractState(parent: QState = None) """
    def active(self): # real signature unknown; restored from __doc__
        """ active(self) -> bool """
        return False

    def activeChanged(self, bool): # real signature unknown; restored from __doc__
        """ activeChanged(self, bool) [signal] """
        pass

    def entered(self): # real signature unknown; restored from __doc__
        """ entered(self) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exited(self): # real signature unknown; restored from __doc__
        """ exited(self) [signal] """
        pass

    def machine(self): # real signature unknown; restored from __doc__
        """ machine(self) -> QStateMachine """
        return QStateMachine

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ onEntry(self, QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ onExit(self, QEvent) """
        pass

    def parentState(self): # real signature unknown; restored from __doc__
        """ parentState(self) -> QState """
        return QState

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


