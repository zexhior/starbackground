# encoding: utf-8
# module PyQt5.QtCore
# from /home/herizo/anaconda3/lib/python3.8/site-packages/PyQt5/QtCore.so
# by generator 1.147
# no doc
# no imports

from .QObject import QObject

class QAbstractEventDispatcher(QObject):
    """ QAbstractEventDispatcher(parent: QObject = None) """
    def aboutToBlock(self): # real signature unknown; restored from __doc__
        """ aboutToBlock(self) [signal] """
        pass

    def awake(self): # real signature unknown; restored from __doc__
        """ awake(self) [signal] """
        pass

    def closingDown(self): # real signature unknown; restored from __doc__
        """ closingDown(self) """
        pass

    def filterNativeEvent(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ filterNativeEvent(self, Union[QByteArray, bytes, bytearray], sip.voidptr) -> Tuple[bool, int] """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) """
        pass

    def hasPendingEvents(self): # real signature unknown; restored from __doc__
        """ hasPendingEvents(self) -> bool """
        return False

    def installNativeEventFilter(self, QAbstractNativeEventFilter): # real signature unknown; restored from __doc__
        """ installNativeEventFilter(self, QAbstractNativeEventFilter) """
        pass

    def instance(self, thread=None): # real signature unknown; restored from __doc__
        """ instance(thread: QThread = None) -> QAbstractEventDispatcher """
        return QAbstractEventDispatcher

    def interrupt(self): # real signature unknown; restored from __doc__
        """ interrupt(self) """
        pass

    def processEvents(self, Union, QEventLoop_ProcessEventsFlags=None, QEventLoop_ProcessEventsFlag=None): # real signature unknown; restored from __doc__
        """ processEvents(self, Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag]) -> bool """
        return False

    def registeredTimers(self, QObject): # real signature unknown; restored from __doc__
        """ registeredTimers(self, QObject) -> List[QAbstractEventDispatcher.TimerInfo] """
        return []

    def registerSocketNotifier(self, QSocketNotifier): # real signature unknown; restored from __doc__
        """ registerSocketNotifier(self, QSocketNotifier) """
        pass

    def registerTimer(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        registerTimer(self, int, Qt.TimerType, QObject) -> int
        registerTimer(self, int, int, Qt.TimerType, QObject)
        """
        return 0

    def remainingTime(self, p_int): # real signature unknown; restored from __doc__
        """ remainingTime(self, int) -> int """
        return 0

    def removeNativeEventFilter(self, QAbstractNativeEventFilter): # real signature unknown; restored from __doc__
        """ removeNativeEventFilter(self, QAbstractNativeEventFilter) """
        pass

    def startingUp(self): # real signature unknown; restored from __doc__
        """ startingUp(self) """
        pass

    def unregisterSocketNotifier(self, QSocketNotifier): # real signature unknown; restored from __doc__
        """ unregisterSocketNotifier(self, QSocketNotifier) """
        pass

    def unregisterTimer(self, p_int): # real signature unknown; restored from __doc__
        """ unregisterTimer(self, int) -> bool """
        return False

    def unregisterTimers(self, QObject): # real signature unknown; restored from __doc__
        """ unregisterTimers(self, QObject) -> bool """
        return False

    def wakeUp(self): # real signature unknown; restored from __doc__
        """ wakeUp(self) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass



