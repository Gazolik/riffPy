import sys

from PyQt5.QtWidgets import QApplication

from interface.interface import RiffViewer
from riffPy.reader import ChunkReader

if __name__ == '__main__':
    path = './test.wav'
    reader = ChunkReader()
    riff = reader.read_riff(path)
    print(riff.name)
    app = QApplication(sys.argv)
    main = RiffViewer()
    main.set_riff_top(riff)
    main.show()
    app.exec_()