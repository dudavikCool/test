import pyrr
import numpy as np

from DataTypes import *

from typing import Tuple
from pyrr import matrix44

class Uniform:
    def __init__(self, name, dataType):
        self.__dataType = dataType
        self.__name = name
        self.__value = None

    def getData(self):
        """Возвращает в формате (Тип значения, Название юниформы в шейдере, Значение)"""
        return self.__dataType, self.__name, self.__value

    def set(self, value):
        self.__value = value

class MatrixUniform(Uniform):
    def __init__(self, name):
        super().__init__(name, Matrix)

class Vec3Uniform(Uniform):
    def __init__(self, name):
        super().__init__(name, Vec3)


