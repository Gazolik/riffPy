from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QModelIndex

from .visualizer_ui import Ui_Form
from .file_list import FileListWidget
from .riffStructure.reader import ChunkReader
from .tree import RiffModel

class Visualizer(QtWidgets.QWidget, Ui_Form):
    NAME, SIZE = range(2)

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.riff_reader = ChunkReader()
        self.riff_model = None

    def setupUi(self, Form):
        super().setupUi(Form)
        self.connect_signals_slot()
        self.fileView.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)

    def connect_signals_slot(self):
        self.loadButton.clicked.connect(self.update_tree)


    @pyqtSlot()
    def update_tree(self):
        file_path = self.parent().findChild(FileListWidget, 'fileList').currentItem().text()
        self.fileName.setText(file_path)
        riff_chunk = self.riff_reader.read_riff(file_path)
        self.riff_model = RiffModel(riff_chunk)
        self.fileView.setModel(self.riff_model)
        self.riff_model.dataChanged.connect(self.modified_tree)

    @pyqtSlot(QModelIndex, QModelIndex, name='dataChanged')
    def modified_tree(self):
        print('modified !')
        self.fileView.setModel(self.riff_model)
        print('done')





