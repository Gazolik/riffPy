from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt, QMimeData, pyqtSignal
import pickle

from riffPy.riff.chunk import FinalChunk, ListChunk

class TreeNode(object):
    def __init__(self, parent, row):
        self.parent = parent
        self.row = row
        self.subnodes = self._getChildren()

    def _getChildren(self):
        raise NotImplementedError()

    def childCount(self):
        return len(self.subnodes)


class TreeModel(QAbstractItemModel):
    def __init__(self):
        super().__init__()
        self.rootNodes = self._getRootNodes()

    def _getRootNodes(self):
        raise NotImplementedError()

    def index(self, row, column, parent_index):
        if not self.hasIndex(row, column, parent_index):
            return QModelIndex()
        if not parent_index.isValid():
            child = self.rootNodes[0]
        else:
            parent = parent_index.internalPointer()
            child = parent.subnodes[row]
        return self.createIndex(row, column, child)


    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        child = index.internalPointer()
        parent = child.parent


        if parent is None:
            return QModelIndex()

        return self.createIndex(parent.row, 0, parent)

    def reset(self):
        self.rootNodes = self._getRootNodes()
        super().reset()

    def rowCount(self, parent_index):
        if not parent_index.isValid():
            return 1
        node = parent_index.internalPointer()
        return node.childCount()

    def columnCount(self, parent):
        return 2

    def itemFromIndex(self, index):
        return index.internalPointer() if index.isValid() else self.rootNodes[0]






class RiffNode(TreeNode):
    def __init__(self, ref, parent, row):
        self.ref = ref
        super().__init__(parent, row)

    def _getChildren(self):
        if isinstance(self.ref, FinalChunk):
            return []
        else:
            return [
                RiffNode(elem, self, index)
                for index, elem in enumerate(self.ref.sub_chunks)
            ]

    def reload(self):
        self.subnodes = self._getChildren()


class RiffModel(TreeModel):
    def __init__(self, riffChunk):
        self.rootElement = riffChunk
        super().__init__()

    def _getRootNodes(self):
        return [RiffNode(self.rootElement, None, 0)]



    def data(self, index, role):
        if not index.isValid():
            return None
        node = index.internalPointer()
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return node.ref.name.decode('utf8')
            elif index.column() == 1:
                return str(node.ref.size)
        return None

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == 0:
                return 'Name'
            elif section == 1:
                return 'Size'
        return None

    def supportedDragActions(self):
        return Qt.CopyAction | Qt.MoveAction

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled

    def mimeTypes(self):
        return ['application/x-riffnode-item-instance']

    def mimeData(self, indexes):
        data = b''
        item = indexes[0].internalPointer()
        data += pickle.dumps(item.ref)
        mime_data = QMimeData()
        mime_data.setData('application/x-riffnode-item-instance', data)
        return mime_data

    def dropMimeData(self, mime_data, action, row, column, parent_index):
        if not mime_data.hasFormat('application/x-riffnode-item-instance'):
            return False
        item = pickle.loads(mime_data.data('application/x-riffnode-item-instance'))
        drop_parent = self.itemFromIndex(parent_index)
        if not isinstance(drop_parent.ref, ListChunk):
            row = parent_index.row()
            parent = drop_parent.parent
        else:
            parent = drop_parent
            row = parent.childCount()

        # TODO Better solution without reloading whole model
        self.beginResetModel()
        parent.ref.sub_chunks.insert(row, item)
        parent.reload()
        self.endResetModel()

        return True

