from Shaders.shader_program import *


class StaticShader(ShaderProgram):
    vertex_file = "../shaders/vertex_shader.txt"
    fragment_file = "../shaders/fragment_shader.txt"

    def __init__(self):
        super().__init__(StaticShader.vertex_file, StaticShader.fragment_file)

    def bind_attributes(self):
        super().bind_attribute(0, "position")
