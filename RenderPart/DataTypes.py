class Matrix:
    pass

class Vec:
    def __init__(self, *args):
        self.Vertex = [*args]
        
    def __getitem__(self, index):
        return self.Vertex[index]

    def __len__(self):
        return len(self.Vertex) 

class Vec2(Vec):
    countValues = 2
    def __init__(self, x, y):
        super().__init__(x, y)
        
class Vec3(Vec):
    countValues = 3 
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

class Vec4(Vec):
    countValues = 4
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z, w)


class Color(Vec3):
    def __init__(self, r, g, b):
        super().__init__(r, g, b)