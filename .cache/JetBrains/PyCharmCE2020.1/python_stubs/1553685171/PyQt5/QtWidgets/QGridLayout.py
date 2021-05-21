# encoding: utf-8
# module PyQt5.QtWidgets
# from /home/herizo/anaconda3/lib/python3.8/site-packages/PyQt5/QtWidgets.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QLayout import QLayout

class QGridLayout(QLayout):
    """
    QGridLayout(QWidget)
    QGridLayout()
    """
    def addItem(self, QLayoutItem, p_int=None, p_int_1=None, rowSpan=1, columnSpan=1, alignment=None, Qt_Alignment=None, Qt_AlignmentFlag=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addItem(self, QLayoutItem, int, int, rowSpan: int = 1, columnSpan: int = 1, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        addItem(self, QLayoutItem)
        """
        pass

    def addLayout(self, QLayout, p_int, p_int_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addLayout(self, QLayout, int, int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        addLayout(self, QLayout, int, int, int, int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        """
        pass

    def addWidget(self, QWidget, p_int=None, p_int_1=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addWidget(self, QWidget)
        addWidget(self, QWidget, int, int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = 0)
        addWidget(self, QWidget, int, int, int, int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = 0)
        """
        pass

    def cellRect(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellRect(self, int, int) -> QRect """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def columnMinimumWidth(self, p_int): # real signature unknown; restored from __doc__
        """ columnMinimumWidth(self, int) -> int """
        return 0

    def columnStretch(self, p_int): # real signature unknown; restored from __doc__
        """ columnStretch(self, int) -> int """
        return 0

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> Qt.Orientations """
        pass

    def getItemPosition(self, p_int): # real signature unknown; restored from __doc__
        """ getItemPosition(self, int) -> Tuple[int, int, int, int] """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ heightForWidth(self, int) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> int """
        return 0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ itemAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def itemAtPosition(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ itemAtPosition(self, int, int) -> QLayoutItem """
        return QLayoutItem

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> QSize """
        pass

    def minimumHeightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ minimumHeightForWidth(self, int) -> int """
        return 0

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def originCorner(self): # real signature unknown; restored from __doc__
        """ originCorner(self) -> Qt.Corner """
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowMinimumHeight(self, p_int): # real signature unknown; restored from __doc__
        """ rowMinimumHeight(self, int) -> int """
        return 0

    def rowStretch(self, p_int): # real signature unknown; restored from __doc__
        """ rowStretch(self, int) -> int """
        return 0

    def setColumnMinimumWidth(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setColumnMinimumWidth(self, int, int) """
        pass

    def setColumnStretch(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setColumnStretch(self, int, int) """
        pass

    def setDefaultPositioning(self, p_int, Qt_Orientation): # real signature unknown; restored from __doc__
        """ setDefaultPositioning(self, int, Qt.Orientation) """
        pass

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ setGeometry(self, QRect) """
        pass

    def setHorizontalSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, int) """
        pass

    def setOriginCorner(self, Qt_Corner): # real signature unknown; restored from __doc__
        """ setOriginCorner(self, Qt.Corner) """
        pass

    def setRowMinimumHeight(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRowMinimumHeight(self, int, int) """
        pass

    def setRowStretch(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRowStretch(self, int, int) """
        pass

    def setSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setSpacing(self, int) """
        pass

    def setVerticalSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ takeAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> int """
        return 0

    def __init__(self, QWidget=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


