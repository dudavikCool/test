from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

from ShaderComponents import ShaderComponent
from DataTypes import *

from pathlib import Path

SHADER_SOURCES_PATH = Path("../ShaderSources")

class ShaderType:
    Basic = Path("Basic")
    DiffuseLight = Path("DiffuseLight")


class ShaderProgram:
    def __init__(self, shaderType : ShaderType):
        shaderPath = SHADER_SOURCES_PATH / shaderType 
        with open(shaderPath / Path("vertex.vert"), mode="r") as file_vert:
            vertex_src = file_vert.readlines()
        with open(shaderPath / Path("fragment.frag"), mode="r") as file_frag:
            fragment_src = file_frag.readlines()

        self.shaderProgram = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER),
                                    compileShader(fragment_src, GL_FRAGMENT_SHADER))
    
    def use(self):
        glUseProgram(self.shaderProgram)

    def passShaderComponents(self, shaderComponents):
        glUseProgram(self.shaderProgram)
        for _ in shaderComponents:
            self.__setUniform(_)

    def __setUniform(self, shaderComponent : ShaderComponent):
        dataType, name, value = shaderComponent.getUniform().getData()
        loc = glGetUniformLocation(self.shaderProgram, name)
        if dataType == Matrix:
            glUniformMatrix4fv(loc, 1, GL_FALSE, value)
        elif dataType == Vec3:
            glUniform3f(loc, value[0], value[1], value[2])


