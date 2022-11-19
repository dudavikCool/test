from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtOpenGL import QGLFormat, QGLWidget
from PyQt5.QtCore import QTimer

from GLContext import GLContext

import sys

class GLWindow(QGLWidget):
    def initializeGL(self):
        self.fmt = QGLFormat()
        self.fmt.setVersion(3, 3)
        self.fmt.setProfile(QGLFormat.OpenGLContextProfile.CoreProfile)
        self.GLContext = GLContext()
        self.setMouseTracking(True)
        
    def paintGL(self):
        self.GLContext.paintGL()

    def resizeGL(self, w, h):    
        self.GLContext.resizeGL(w, h)

    def mouseMoveEvent(self, event):
        self.GLContext.mouseMoveEvent(event)
        self.update()





if __name__ == "__main__":
    app = QApplication([])
    window = GLWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())