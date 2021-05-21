# encoding: utf-8
# module PyQt5.QtWidgets
# from /home/herizo/anaconda3/lib/python3.8/site-packages/PyQt5/QtWidgets.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QAbstractItemView import QAbstractItemView

class QListView(QAbstractItemView):
    """ QListView(parent: QWidget = None) """
    def batchSize(self): # real signature unknown; restored from __doc__
        """ batchSize(self) -> int """
        return 0

    def clearPropertyFlags(self): # real signature unknown; restored from __doc__
        """ clearPropertyFlags(self) """
        pass

    def currentChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ currentChanged(self, QModelIndex, QModelIndex) """
        pass

    def dataChanged(self, QModelIndex, QModelIndex_1, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, QModelIndex, QModelIndex, roles: Iterable[int] = []) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, QDragMoveEvent) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def flow(self): # real signature unknown; restored from __doc__
        """ flow(self) -> QListView.Flow """
        pass

    def gridSize(self): # real signature unknown; restored from __doc__
        """ gridSize(self) -> QSize """
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ indexAt(self, QPoint) -> QModelIndex """
        pass

    def indexesMoved(self, Iterable, QModelIndex=None): # real signature unknown; restored from __doc__
        """ indexesMoved(self, Iterable[QModelIndex]) [signal] """
        pass

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, QModelIndex) -> bool """
        return False

    def isRowHidden(self, p_int): # real signature unknown; restored from __doc__
        """ isRowHidden(self, int) -> bool """
        return False

    def isSelectionRectVisible(self): # real signature unknown; restored from __doc__
        """ isSelectionRectVisible(self) -> bool """
        return False

    def isWrapping(self): # real signature unknown; restored from __doc__
        """ isWrapping(self) -> bool """
        return False

    def layoutMode(self): # real signature unknown; restored from __doc__
        """ layoutMode(self) -> QListView.LayoutMode """
        pass

    def modelColumn(self): # real signature unknown; restored from __doc__
        """ modelColumn(self) -> int """
        return 0

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
        pass

    def moveCursor(self, QAbstractItemView_CursorAction, Union, Qt_KeyboardModifiers=None, Qt_KeyboardModifier=None): # real signature unknown; restored from __doc__
        """ moveCursor(self, QAbstractItemView.CursorAction, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier]) -> QModelIndex """
        pass

    def movement(self): # real signature unknown; restored from __doc__
        """ movement(self) -> QListView.Movement """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def rectForIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ rectForIndex(self, QModelIndex) -> QRect """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def resizeMode(self): # real signature unknown; restored from __doc__
        """ resizeMode(self) -> QListView.ResizeMode """
        pass

    def rowsAboutToBeRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsAboutToBeRemoved(self, QModelIndex, int, int) """
        pass

    def rowsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsInserted(self, QModelIndex, int, int) """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, int, int) """
        pass

    def scrollTo(self, QModelIndex, hint=None): # real signature unknown; restored from __doc__
        """ scrollTo(self, QModelIndex, hint: QAbstractItemView.ScrollHint = QAbstractItemView.EnsureVisible) """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> List[QModelIndex] """
        return []

    def selectionChanged(self, QItemSelection, QItemSelection_1): # real signature unknown; restored from __doc__
        """ selectionChanged(self, QItemSelection, QItemSelection) """
        pass

    def setBatchSize(self, p_int): # real signature unknown; restored from __doc__
        """ setBatchSize(self, int) """
        pass

    def setFlow(self, QListView_Flow): # real signature unknown; restored from __doc__
        """ setFlow(self, QListView.Flow) """
        pass

    def setGridSize(self, QSize): # real signature unknown; restored from __doc__
        """ setGridSize(self, QSize) """
        pass

    def setLayoutMode(self, QListView_LayoutMode): # real signature unknown; restored from __doc__
        """ setLayoutMode(self, QListView.LayoutMode) """
        pass

    def setModelColumn(self, p_int): # real signature unknown; restored from __doc__
        """ setModelColumn(self, int) """
        pass

    def setMovement(self, QListView_Movement): # real signature unknown; restored from __doc__
        """ setMovement(self, QListView.Movement) """
        pass

    def setPositionForIndex(self, QPoint, QModelIndex): # real signature unknown; restored from __doc__
        """ setPositionForIndex(self, QPoint, QModelIndex) """
        pass

    def setResizeMode(self, QListView_ResizeMode): # real signature unknown; restored from __doc__
        """ setResizeMode(self, QListView.ResizeMode) """
        pass

    def setRootIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ setRootIndex(self, QModelIndex) """
        pass

    def setRowHidden(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setRowHidden(self, int, bool) """
        pass

    def setSelection(self, QRect, Union, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setSelection(self, QRect, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setSelectionRectVisible(self, bool): # real signature unknown; restored from __doc__
        """ setSelectionRectVisible(self, bool) """
        pass

    def setSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setSpacing(self, int) """
        pass

    def setUniformItemSizes(self, bool): # real signature unknown; restored from __doc__
        """ setUniformItemSizes(self, bool) """
        pass

    def setViewMode(self, QListView_ViewMode): # real signature unknown; restored from __doc__
        """ setViewMode(self, QListView.ViewMode) """
        pass

    def setWordWrap(self, bool): # real signature unknown; restored from __doc__
        """ setWordWrap(self, bool) """
        pass

    def setWrapping(self, bool): # real signature unknown; restored from __doc__
        """ setWrapping(self, bool) """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def startDrag(self, Union, Qt_DropActions=None, Qt_DropAction=None): # real signature unknown; restored from __doc__
        """ startDrag(self, Union[Qt.DropActions, Qt.DropAction]) """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def uniformItemSizes(self): # real signature unknown; restored from __doc__
        """ uniformItemSizes(self) -> bool """
        return False

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def viewMode(self): # real signature unknown; restored from __doc__
        """ viewMode(self) -> QListView.ViewMode """
        pass

    def viewOptions(self): # real signature unknown; restored from __doc__
        """ viewOptions(self) -> QStyleOptionViewItem """
        return QStyleOptionViewItem

    def viewportSizeHint(self): # real signature unknown; restored from __doc__
        """ viewportSizeHint(self) -> QSize """
        pass

    def visualRect(self, QModelIndex): # real signature unknown; restored from __doc__
        """ visualRect(self, QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, QItemSelection): # real signature unknown; restored from __doc__
        """ visualRegionForSelection(self, QItemSelection) -> QRegion """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ wordWrap(self) -> bool """
        return False

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Adjust = 1
    Batched = 1
    Fixed = 0
    Free = 1
    IconMode = 1
    LeftToRight = 0
    ListMode = 0
    SinglePass = 0
    Snap = 2
    Static = 0
    TopToBottom = 1


