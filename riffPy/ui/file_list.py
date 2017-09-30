from PyQt5.QtWidgets import (
    QListWidget, QListWidgetItem
)

class FileItem(QListWidgetItem):
    def __init__(self, file_path):
        super().__init__(file_path)


class FileListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        e.accept()

    def dragMoveEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        mime_data = e.mimeData()
        if mime_data.hasUrls():
            url_list = mime_data.urls()
            for url in url_list:
                item = FileItem(url.toLocalFile())
                self.addItem(item)
        e.accept()