from CONSTANTS import *
from DataTypes import *


class Texcel(Vec2):
    pass

class Vertex(Vec3):
    pass

class Normal(Vec3):
    pass


class Layout_VertexType():
    def __init__(self, layout, vertexType):
        self.__layout = layout
        self.__vertexType = vertexType

    @property
    def layout(self):
        return self.__layout
    
    @property
    def vertexType(self):
        return self.__vertexType

class VertexData:
    def __init__(self, vertices, layouts=None):
        self.__vertices = vertices
        self.__layouts = layouts
        self.__dataTypesList = None
        self.__vertexCount = None
        self.__verticesList = None

    def getStride(self):
        return sum([_.vertexType.countValues for _ in self.getDataTypeList()]) * FLOAT_SIZE

    def getOffset(self, index):
        return sum([_.vertexType.countValues for _ in self.getDataTypeList()[:index]]) * FLOAT_SIZE

    def getVertexCount(self):
        if self.__vertexCount is None:
            self.__vertexCount = int(len(self.getVerticesList()) * FLOAT_SIZE / self.getStride())
        return self.__vertexCount

    def getDataTypeList(self):
        if self.__dataTypesList is None:
            types = []
            if self.__layouts is None:
                for _ in range(len(self.__vertices)):
                    vertexType = type(self.__vertices[_])
                    if vertexType in [_.vertexType for _ in types]:
                        break
                    types.append(Layout_VertexType(_, vertexType))
            else:
                types = [Layout_VertexType(data_vertex[0], type(data_vertex[1])) for data_vertex in zip(self.__layouts, self.__vertices)]
            self.__dataTypesList = types
        return self.__dataTypesList

    def getVerticesList(self):
        if self.__verticesList is None:
            l = []
            for _ in self.__vertices:
                l += _
            self.__verticesList = l
        return self.__verticesList
