import sys

from PyQt5 import QtWidgets

from riffPy.ui.main_window import RiffPy
from riffPy.ui.tree import RiffModel
from riffPy.riff.reader import ChunkReader
from riffPy.riff.writer import ChunkWriter

def main_ui():
    app = QtWidgets.QApplication(sys.argv)
    main_window = RiffPy()
    main_window.show()
    sys.exit(app.exec())


def read_write():
    reader = ChunkReader()
    writer = ChunkWriter()

    riff = reader.read_riff('./test.wav')
    riff.form_type = b'ABCD'
    writer.write_riff(riff, './test2.wav')



if __name__ == '__main__':
    main_ui()
    #read_write()