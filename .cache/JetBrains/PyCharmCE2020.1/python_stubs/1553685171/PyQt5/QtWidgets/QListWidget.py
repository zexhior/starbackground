# encoding: utf-8
# module PyQt5.QtWidgets
# from /home/herizo/anaconda3/lib/python3.8/site-packages/PyQt5/QtWidgets.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QListView import QListView

class QListWidget(QListView):
    """ QListWidget(parent: QWidget = None) """
    def addItem(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addItem(self, QListWidgetItem)
        addItem(self, str)
        """
        pass

    def addItems(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ addItems(self, Iterable[str]) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closePersistentEditor(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ closePersistentEditor(self, QListWidgetItem) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> QListWidgetItem """
        return QListWidgetItem

    def currentItemChanged(self, QListWidgetItem, QListWidgetItem_1): # real signature unknown; restored from __doc__
        """ currentItemChanged(self, QListWidgetItem, QListWidgetItem) [signal] """
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ currentRow(self) -> int """
        return 0

    def currentRowChanged(self, p_int): # real signature unknown; restored from __doc__
        """ currentRowChanged(self, int) [signal] """
        pass

    def currentTextChanged(self, p_str): # real signature unknown; restored from __doc__
        """ currentTextChanged(self, str) [signal] """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def dropMimeData(self, p_int, QMimeData, Qt_DropAction): # real signature unknown; restored from __doc__
        """ dropMimeData(self, int, QMimeData, Qt.DropAction) -> bool """
        return False

    def editItem(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ editItem(self, QListWidgetItem) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def findItems(self, p_str, Union, Qt_MatchFlags=None, Qt_MatchFlag=None): # real signature unknown; restored from __doc__
        """ findItems(self, str, Union[Qt.MatchFlags, Qt.MatchFlag]) -> List[QListWidgetItem] """
        return []

    def indexFromItem(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ indexFromItem(self, QListWidgetItem) -> QModelIndex """
        pass

    def insertItem(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertItem(self, int, QListWidgetItem)
        insertItem(self, int, str)
        """
        pass

    def insertItems(self, p_int, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ insertItems(self, int, Iterable[str]) """
        pass

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ isSortingEnabled(self) -> bool """
        return False

    def item(self, p_int): # real signature unknown; restored from __doc__
        """ item(self, int) -> QListWidgetItem """
        return QListWidgetItem

    def itemActivated(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ itemActivated(self, QListWidgetItem) [signal] """
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, QPoint) -> QListWidgetItem
        itemAt(self, int, int) -> QListWidgetItem
        """
        return QListWidgetItem

    def itemChanged(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ itemChanged(self, QListWidgetItem) [signal] """
        pass

    def itemClicked(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ itemClicked(self, QListWidgetItem) [signal] """
        pass

    def itemDoubleClicked(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ itemDoubleClicked(self, QListWidgetItem) [signal] """
        pass

    def itemEntered(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ itemEntered(self, QListWidgetItem) [signal] """
        pass

    def itemFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ itemFromIndex(self, QModelIndex) -> QListWidgetItem """
        return QListWidgetItem

    def itemPressed(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ itemPressed(self, QListWidgetItem) [signal] """
        pass

    def items(self, QMimeData): # real signature unknown; restored from __doc__
        """ items(self, QMimeData) -> List[QListWidgetItem] """
        return []

    def itemSelectionChanged(self): # real signature unknown; restored from __doc__
        """ itemSelectionChanged(self) [signal] """
        pass

    def itemWidget(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ itemWidget(self, QListWidgetItem) -> QWidget """
        return QWidget

    def mimeData(self, Iterable, QListWidgetItem=None): # real signature unknown; restored from __doc__
        """ mimeData(self, Iterable[QListWidgetItem]) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def openPersistentEditor(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ openPersistentEditor(self, QListWidgetItem) """
        pass

    def removeItemWidget(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ removeItemWidget(self, QListWidgetItem) """
        pass

    def row(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ row(self, QListWidgetItem) -> int """
        return 0

    def scrollToItem(self, QListWidgetItem, hint=None): # real signature unknown; restored from __doc__
        """ scrollToItem(self, QListWidgetItem, hint: QAbstractItemView.ScrollHint = QAbstractItemView.EnsureVisible) """
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> List[QListWidgetItem] """
        return []

    def setCurrentItem(self, QListWidgetItem, Union=None, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCurrentItem(self, QListWidgetItem)
        setCurrentItem(self, QListWidgetItem, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        """
        pass

    def setCurrentRow(self, p_int, Union=None, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCurrentRow(self, int)
        setCurrentRow(self, int, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        """
        pass

    def setItemWidget(self, QListWidgetItem, QWidget): # real signature unknown; restored from __doc__
        """ setItemWidget(self, QListWidgetItem, QWidget) """
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        pass

    def setSelectionModel(self, QItemSelectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, QItemSelectionModel) """
        pass

    def setSortingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setSortingEnabled(self, bool) """
        pass

    def sortItems(self, order=None): # real signature unknown; restored from __doc__
        """ sortItems(self, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def takeItem(self, p_int): # real signature unknown; restored from __doc__
        """ takeItem(self, int) -> QListWidgetItem """
        return QListWidgetItem

    def visualItemRect(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ visualItemRect(self, QListWidgetItem) -> QRect """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


