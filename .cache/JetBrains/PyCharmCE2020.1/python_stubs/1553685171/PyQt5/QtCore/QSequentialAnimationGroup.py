# encoding: utf-8
# module PyQt5.QtCore
# from /home/herizo/anaconda3/lib/python3.8/site-packages/PyQt5/QtCore.so
# by generator 1.147
# no doc
# no imports

from .QAnimationGroup import QAnimationGroup

class QSequentialAnimationGroup(QAnimationGroup):
    """ QSequentialAnimationGroup(parent: QObject = None) """
    def addPause(self, p_int): # real signature unknown; restored from __doc__
        """ addPause(self, int) -> QPauseAnimation """
        return QPauseAnimation

    def currentAnimation(self): # real signature unknown; restored from __doc__
        """ currentAnimation(self) -> QAbstractAnimation """
        return QAbstractAnimation

    def currentAnimationChanged(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ currentAnimationChanged(self, QAbstractAnimation) [signal] """
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def insertPause(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ insertPause(self, int, int) -> QPauseAnimation """
        return QPauseAnimation

    def updateCurrentTime(self, p_int): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, int) """
        pass

    def updateDirection(self, QAbstractAnimation_Direction): # real signature unknown; restored from __doc__
        """ updateDirection(self, QAbstractAnimation.Direction) """
        pass

    def updateState(self, QAbstractAnimation_State, QAbstractAnimation_State_1): # real signature unknown; restored from __doc__
        """ updateState(self, QAbstractAnimation.State, QAbstractAnimation.State) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


