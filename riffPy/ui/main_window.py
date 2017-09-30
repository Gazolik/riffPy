import sys

from PyQt5 import QtWidgets

from .main_window_ui import Ui_MainWindow
from .file_list import FileListWidget
from .visualizer import Visualizer


class RiffPy(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.fileListWidget = FileListWidget(self)
        self.fileListWidget.setMaximumWidth(300)
        self.fileListWidget.setObjectName("fileList")
        self.verticalLayout.addWidget(self.fileListWidget)


        self.topVisualizer = Visualizer(self)
        self.topVisualizer.setObjectName("topVisualizer")
        self.topVisualizer.fileName.setText('File name here')
        self.topVisualizer.chunkName.setText('Chunk name here')
        self.verticalLayout_2.addWidget(self.topVisualizer)

        self.botVisualizer = Visualizer(self)
        self.botVisualizer.setObjectName("botVisualizer")
        self.botVisualizer.fileName.setText('File name here')
        self.botVisualizer.chunkName.setText('Chunk name here')
        self.verticalLayout_2.addWidget(self.botVisualizer)

