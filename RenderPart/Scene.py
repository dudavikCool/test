from MeshObject import *
from OpenGL.GL import *


class SceneDisplayer:
    def __init__(self, scene):
        self.__scene = scene

    def display(self):
        for _ in self.__scene.objects:
            self.__drawMesh(_)

    def __drawMesh(self, mesh: BasicMeshObject):
        shader = mesh.getShader()
        requiredComponents = self.__scene.getShaderComponents() + mesh.getShaderComponents()
        shader.passShaderComponents(requiredComponents)
        shader.use()
        glBindVertexArray(mesh.getVAO())
        glDrawArrays(GL_QUADS, 0, mesh.getVerticesLength())



class Scene:
    def __init__(self, *objects):
        self.__globalComponents = []
        self.__displayer = SceneDisplayer(self)
        self.objects = []
        self.append(*objects)

    def __getitem__(self, index):
        return self.objects[index]

    def __len__(self):
        return len(self.objects)

    def append(self, *objects):
        self.objects += objects

    def getShaderComponents(self):
        return self.__globalComponents

    def addGlobalComponent(self, shaderComponent):
        self.__globalComponents.append(shaderComponent)


    def display(self):
        self.__displayer.display()



