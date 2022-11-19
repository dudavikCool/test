import pyrr
import numpy as np

from Uniforms import *

class ShaderComponent:
    def getUniform(self) -> Uniform:
        pass

class ShaderProjection(ShaderComponent):
    def __init__(self, aspect):
        self.__uniform = MatrixUniform("projection")
        self.changePerspective(aspect)

    def getUniform(self):
        return self.__uniform

    def changePerspective(self, aspect, fovy=45, near=0.1, far=10):
        matrix = pyrr.matrix44.create_perspective_projection(
        fovy=fovy,
        aspect=aspect,
        near=near,
        far=far,
        dtype=np.float32
        )
        self.__uniform.set(matrix)


class ShaderModel(ShaderComponent):
    def __init__(self, eulears=[0, 0, 0], position=[0, 0, 0], scaling=[1, 1, 1]):
        self.__eulears = eulears
        self.__position = position
        self.__scaling = scaling
        
        self.__uniform = MatrixUniform("model")
        self.__transform()

    def getUniform(self):
        return self.__uniform

    def rotate(self, x, y, z):
        new_eulears = [sum(_) for _ in zip(self.__eulears, [x, y, z])]
        for _ in new_eulears:
            if _ >= 360:
                _ -= 360
        self.__eulears = new_eulears
        self.__transform()

    def translate(self, x, y, z):
        self.__position = [sum(_) for _ in zip(self.__position, [x, y, z])]
        self.__transform()
    
    def scale(self, x, y, z):
        self.__scaling = [_[0] * _[1] for _ in zip(self.__scaling, [x, y, z])]
        self.__transform()


    def __transform(self):
        modelMatrix = pyrr.matrix44.create_identity(dtype=np.float32)
        modelMatrix = pyrr.matrix44.multiply(
            m1=modelMatrix,
            m2=pyrr.matrix44.create_from_eulers(np.radians(self.__eulears), dtype=np.float32)
        )
        modelMatrix = pyrr.matrix44.multiply(
        m1=modelMatrix,
        m2=pyrr.matrix44.create_from_translation(self.__position, dtype=np.float32)
        )
        modelMatrix = pyrr.matrix44.multiply(
            m1=modelMatrix,
            m2=pyrr.matrix44.create_from_scale(self.__scaling, dtype=np.float32)
        )
        self.__uniform.set(modelMatrix)


class ShaderView(ShaderComponent):
    def __init__(self, eulears=[0, 0, 0], position=[0, 0, 0], scaling=[1, 1, 1]):
        self.__eulears = eulears
        self.__position = position
        self.__scaling = scaling
        self.__uniform = MatrixUniform("view")
        self.__transform()

    def getUniform(self) -> Uniform:
        return self.__uniform

    def rotate(self, x, y, z): 
        new_eulears = [_[0] - _[1] for _ in zip(self.__eulears, [x, y, z])]
        for _ in new_eulears:
            if _ <= 0:
                _ += 360
        self.__eulears = new_eulears
        self.__transform()

    def translate(self, x, y, z):
        self.__position = [_[0] - _[1] for _ in zip(self.__position, [x, y, z])]
        self.__transform()

    def __transform(self):
        modelMatrix = pyrr.matrix44.create_identity(dtype=np.float32)
        modelMatrix = pyrr.matrix44.multiply(
            m1=modelMatrix,
            m2=pyrr.matrix44.create_from_eulers(np.radians(self.__eulears), dtype=np.float32)
        )
        modelMatrix = pyrr.matrix44.multiply(
        m1=modelMatrix,
        m2=pyrr.matrix44.create_from_translation(self.__position, dtype=np.float32)
        )
        self.__uniform.set(modelMatrix)
    
class LightPoint(ShaderComponent):
    def __init__(self, position, name="lightPosition"):
        self.__position = position
        self.__uniform = Vec3Uniform(name)
        self.__transform()
    
    def getUniform(self):
        return self.__uniform

    def translate(self, x, y, z):
        self.__position = [sum(_) for _ in zip(self.__position, [x, y, z])]
        self.__transform()
    
    def __transform(self):
        self.__uniform.set(np.array(self.__position, dtype=np.float32))
