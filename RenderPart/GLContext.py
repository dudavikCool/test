from OpenGL.GL import *
from ShaderProgram import *
from MeshObject import *

from Scene import *

class GLContext():
    def __init__(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 1.0)

        self.mousePosition = (160, 120)
        self.screenSize = None

        self.projection = ShaderProjection(640/480)
        self.scene = Scene()
        self.scene.addGlobalComponent(self.projection)
        self.scene.addGlobalComponent(LightPoint([0, -2, 0 ]))
        self.camera = ShaderView()
        self.scene.addGlobalComponent(self.camera)
        self.init_scene()

    def init_scene(self):
        obj2 = CubeMesh(ShaderType.DiffuseLight)
        obj2.translate(0, 0, -5)
        obj2.scale(1, 1, 1)
        obj2.rotate(z=30)
        self.scene.append(obj2)
        self.camera.translate(0, 0, 0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # self.camera.rotate(-0.5, 0, 0)
        self.scene.display()

    def mouseMoveEvent(self, event):
        pass
    
    def resizeGL(self, w, h):    
        glViewport(0, 0, int(w), int(h))
        self.screenSize = w, h
        # self.scene.scaleToViewport(int(w) / int(h))
        self.projection.changePerspective(int(w) / int(h))


