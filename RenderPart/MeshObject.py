from OpenGL.GL import *
from array import array
import numpy as np

from ShaderProgram import *
from VertexData import *
from CONSTANTS import *

from ShaderComponents import *


class BasicMeshObject:
    def __init__(self, vertexData : VertexData, shaderType: ShaderType):         
        
        self.__shader = ShaderProgram(shaderType)
        self.__vertexData = vertexData
        
        self.__shaderComponents = []
        self.__model = ShaderModel()
        self.__setShaderComponents()

        self.__vao = glGenVertexArrays(1)
        glBindVertexArray(self.__vao)
        self.__vbo = glGenBuffers(1)
        self.__setVBO()
        glBindVertexArray(0)

    def __setVBO(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.__vbo)
        VBOdata = np.array(self.__vertexData.getVerticesList(), dtype=np.float32)
        glBufferData(GL_ARRAY_BUFFER, VBOdata.nbytes, VBOdata, GL_STATIC_DRAW)

        dataTypeList = self.__vertexData.getDataTypeList() 

        for _ in range(len(dataTypeList)):
            glEnableVertexAttribArray(dataTypeList[_].layout)
            glVertexAttribPointer(dataTypeList[_].layout, dataTypeList[_].vertexType.countValues, GL_FLOAT,
            GL_FALSE, self.__vertexData.getStride(), ctypes.c_void_p(self.__vertexData.getOffset(_)))

    def __setShaderComponents(self):
        for _ in dir(self):
            field = self.__getattribute__(_)
            if isinstance(field, ShaderComponent):
                self.__shaderComponents.append(field)

    def getShaderComponents(self):
        return self.__shaderComponents


    def getVerticesLength(self):
        return self.__vertexData.getVertexCount()


    def rotate(self, x=0, y=0, z=0):
        self.__model.rotate(x, y, z)

    def translate(self, x=0, y=0, z=0):
        self.__model.translate(x, y, z)
    
    def scale(self, x=1, y=1, z=1):
        self.__model.scale(x, y, z)

    def viewportScale(self, x, y, z):
        self.__model.viewportScale(x, y, z)


    def getShader(self):
        return self.__shader

    def getVAO(self):
        return self.__vao
    
    def getVertexData(self):
        return self.__vertexData


    def destroy(self):
        glDeleteBuffers(1, (self.__vboVertices,))
        glDeleteBuffers(1, (self.__ebo,))
        glDeleteVertexArrays(1, (self.__vao,))


class CubeMesh(BasicMeshObject):
    def __init__(self, shaderType: ShaderType):
        vertexData = VertexData([
        Vertex(-1, -1, 1), Normal(0, 0, 1),
        Vertex(-1, 1, 1), Normal(0, 0, 1),
        Vertex(1, 1, 1), Normal(0, 0, 1),
        Vertex(1, -1, 1), Normal(0, 0, 1),

        Vertex(-1, -1, -1), Normal(0, 0, -1),
        Vertex(-1, 1, -1), Normal(0, 0, -1),
        Vertex(1, 1, -1), Normal(0, 0, -1),
        Vertex(1, -1, -1), Normal(0, 0, -1),

        Vertex(-1, -1, -1), Normal(-1, 0, 0),
        Vertex(-1, 1, -1), Normal(-1, 0, 0),
        Vertex(-1, 1, 1), Normal(-1, 0, 0),
        Vertex(-1, -1, 1), Normal(-1, 0, 0),

        Vertex(1, -1, -1), Normal(1, 0, 0),
        Vertex(1, 1, -1), Normal(1, 0, 0),
        Vertex(1, 1, 1), Normal(1, 0, 0),
        Vertex(1, -1, 1), Normal(1, 0, 0),

        Vertex(-1, 1, 1), Normal(0, 1, 0),
        Vertex(-1, 1, -1), Normal(0, 1, 0),
        Vertex(1, 1, -1), Normal(0, 1, 0),
        Vertex(1, 1, 1), Normal(0, 1, 0),

        Vertex(-1, -1, 1), Normal(0, -1, 0),
        Vertex(-1, -1, -1), Normal(0, -1, 0),
        Vertex(1, -1, -1), Normal(0, -1, 0), 
        Vertex(1, -1, 1), Normal(0, -1, 0)
        ])

     
        super().__init__(vertexData=vertexData, shaderType=shaderType)