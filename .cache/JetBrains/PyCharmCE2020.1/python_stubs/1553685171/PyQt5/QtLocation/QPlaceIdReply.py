# encoding: utf-8
# module PyQt5.QtLocation
# from /home/herizo/anaconda3/lib/python3.8/site-packages/PyQt5/QtLocation.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QPlaceReply import QPlaceReply

class QPlaceIdReply(QPlaceReply):
    """ QPlaceIdReply(QPlaceIdReply.OperationType, parent: QObject = None) """
    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> str """
        return ""

    def operationType(self): # real signature unknown; restored from __doc__
        """ operationType(self) -> QPlaceIdReply.OperationType """
        pass

    def setId(self, p_str): # real signature unknown; restored from __doc__
        """ setId(self, str) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceReply.Type """
        pass

    def __init__(self, QPlaceIdReply_OperationType, parent=None): # real signature unknown; restored from __doc__
        pass

    RemoveCategory = 3
    RemovePlace = 2
    SaveCategory = 1
    SavePlace = 0


