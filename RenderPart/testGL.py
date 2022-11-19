from ShaderComponents import *
# from MeshObject import *
# import pygame as pg

# pg.init()
# pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
# pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
# pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
#                             pg.GL_CONTEXT_PROFILE_CORE)
# pg.display.set_mode((640,480), pg.OPENGL|pg.DOUBLEBUF)

# v = CubeMesh(ShaderType.Basic)

sv = ShaderView()
sm = ShaderModel()
print(sv.getUniform().getData())
print(sm.getUniform().getData())

sv.translate(2, 2, 2)
sm.translate(2, 2, 2)

print(sv.getUniform().getData())
print(sm.getUniform().getData())
