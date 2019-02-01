from OpenGL.GL import *
import numpy as np


class ShaderProgram:

    matrix_buffer = None

    def __init__(self, vertex_file, fragment_file):
        self.vertex_shader_id = ShaderProgram._load_shader(vertex_file, GL_VERTEX_SHADER)
        self.fragment_shader_id = ShaderProgram._load_shader(fragment_file, GL_FRAGMENT_SHADER)
        self.program_id = glCreateProgram()
        glAttachShader(self.program_id, self.vertex_shader_id)
        glAttachShader(self.program_id, self.fragment_shader_id)
        self.bind_attributes()
        glLinkProgram(self.program_id)
        glValidateProgram(self.program_id)
        self.get_all_uniform_locations()

    # This should(tm) be implemented when instanced
    def get_all_uniform_locations(self):
        raise NotImplementedError()

    def get_uniform_location(self, uniform_name):
        return glGetUniformLocation(self.program_id, uniform_name)

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
    def load_float(location, value):
        glUniform1f(location, value)

    @staticmethod
    def load_vector(location, vector):
        glUniform3f(location, vector[0], vector[1], vector[2])

    @staticmethod
    def load_boolean(location, value):
        if value:
            value = 1
        else:
            value = 0
        glUniform1f(location, value)

    @staticmethod
    def load_matrix(location, matrix):
        ShaderProgram.matrix_buffer = np.array(matrix, dtype=np.float32).reshape(4, 4)
        glUniformMatrix4fv(location, 1, GL_FALSE, ShaderProgram.matrix_buffer)

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
