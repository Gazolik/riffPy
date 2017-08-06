import sys
from PyQt5.QtWidgets import (
    QWidget, QListWidget, QListWidgetItem,QTreeWidgetItem,
    QApplication, QTreeWidget, QGridLayout)


from riffPy.chunk import ListChunk, FinalChunk, RiffChunk

class FileItem(QListWidgetItem):
    def __init__(self, file_path):
        super().__init__(file_path)


class FileListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setGeometry(10, 10, 60, 200)

    def dragEnterEvent(self, e):
        e.accept()

    def dragMoveEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        mime_data = e.mimeData()
        if mime_data.hasUrls():
            url_list = mime_data.urls()
            for url in url_list:
                print(url.toString())
                item = FileItem(url.toLocalFile())
                self.addItem(item)
                print('Added')
        e.accept()

class ChunkTreeItem(QTreeWidgetItem):
    def __init__(self, parent, chunk):
        print('Creating')
        super().__init__(parent)
        self.chunk = chunk
        self.setText(0, chunk.name.decode('utf-8'))
        self.setText(1, str(chunk.size))
        if isinstance(chunk, ListChunk):
            for child in chunk.sub_chunks:
                child_tree_item = self.create_child(child)
                self.addChild(child_tree_item)

    def create_child(self, chunk):
        item = ChunkTreeItem(self, chunk)
        return item


class ChunkTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(2)
        self.setHeaderLabels(['name', 'size'])
        self.root = None
        self.setDragEnabled(True)
        self.setAcceptDrops(True)

    def set_riff(self, riff_chunk):
        self.clear()
        self.root = ChunkTreeItem(self, riff_chunk)


class RiffViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.general_layout = QGridLayout(self)
        self.top_viewer_layout = QGridLayout(self)
        self.bot_viewer_layout = QGridLayout(self)

        self.file_list = FileListWidget(self)
        self.file_list.addItem('0')

        self.riff_tree_top = ChunkTreeWidget(self)

        self.file_list2 = FileListWidget()
        self.file_list2.addItem('2')

        self.riff_tree_bot = ChunkTreeWidget(self)

        self.file_list4 = FileListWidget()
        self.file_list4.addItem('4')

        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 500, 500)
        self.general_layout.addWidget(self.file_list, 0, 0 , 2, 1)
        self.general_layout.addLayout(self.top_viewer_layout, 0, 1)
        self.general_layout.addLayout(self.bot_viewer_layout, 1, 1)

        self.top_viewer_layout.addWidget(self.riff_tree_top, 0, 0)
        self.top_viewer_layout.addWidget(self.file_list2, 0, 1)
        self.bot_viewer_layout.addWidget(self.riff_tree_bot, 0, 0)
        self.bot_viewer_layout.addWidget(self.file_list4, 0, 1)

    def set_riff_top(self, riff_chunk: RiffChunk):
        self.riff_tree_top.set_riff(riff_chunk)

    def set_riff_bot(self, riff_chunk: RiffChunk):
        self.riff_tree_bot.set_riff(riff_chunk)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = RiffViewer()
    main.show()
    app.exec_()