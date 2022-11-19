from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from GLWindow import GLWindow
from OpenGL import *

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 640, 480)
        self.gl = GLWindow()
        self.setCentralWidget(self.gl)
        self.glRatio = 0.8

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        width, height = int(a0.size().width() * self.glRatio), int(a0.size().height() * self.glRatio)
        self.gl.setGeometry(50, 50, width, height)
        pass
        
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
