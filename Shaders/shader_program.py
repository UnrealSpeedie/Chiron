from OpenGL.GL import *


class ShaderProgram:
    def __init__(self, vertex_file, fragment_file):
        self.vertex_shader_id = ShaderProgram._load_shader(vertex_file, GL_VERTEX_SHADER)
        self.fragment_shader_id = ShaderProgram._load_shader(fragment_file, GL_FRAGMENT_SHADER)
        self.program_id = glCreateProgram()
        glAttachShader(self.program_id, self.vertex_shader_id)
        glAttachShader(self.program_id, self.fragment_shader_id)
        glLinkProgram(self.program_id)
        glValidateProgram(self.program_id)

    def start(self):
        glUseProgram(self.program_id)

    @staticmethod
    def stop():
        glUseProgram(0)

    def clean_up(self):
        glDetachShader(self.program_id, self.vertex_shader_id)
        glDetachShader(self.program_id, self.fragment_shader_id)
        glDeleteShader(self.vertex_shader_id)
        glDeleteShader(self.fragment_shader_id)
        glDeleteProgram(self.program_id)

    # This should(tm) be implemented when instanced
    def bind_attributes(self):
        raise NotImplementedError()

    def bind_attribute(self, attribute, variable_name):
        glBindAttribLocation(self.program_id, attribute, variable_name)

    @staticmethod
    def _load_shader(file, shader_type):
        with open(file, "r") as f:
            shader_source = f.readlines()

        shader_id = glCreateShader(shader_type)
        glShaderSource(shader_id, shader_source)
        glCompileShader(shader_id)

        if glGetShaderiv(shader_id, GL_COMPILE_STATUS) == GL_FALSE:
            print(glGetShaderInfoLog(shader_id))
            print("Could not compile shader!")

        return shader_id
