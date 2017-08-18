import sys

from PyQt5 import QtWidgets

from riffPy.main_window import RiffPy
from riffPy.tree import RiffModel
from riffPy.riffStructure.reader import ChunkReader

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = RiffPy()
    main_window.show()
    sys.exit(app.exec())


def test():
    reader = ChunkReader()
    riff = reader.read_riff('./test.wav')
    print(riff)
    model = RiffModel(riff)
    print(model)

if __name__ == '__main__':
    main()