from OpenGL.GL import *
import numpy as np
import pygame
from Models.raw_model import RawModel


class Loader:
    """
    TODO THIS CLASS MAY NOT BE STATIC!
    """

    # Used for clean up by keeping track of all VAOs/VBOs created
    _vaos = []
    _vbos = []
    _textures = []

    @staticmethod
    def load_texture(file_name) -> int:
        texture_id = glGenTextures(1)
        Loader._textures.append(texture_id)

        texture = pygame.image.load(file_name)
        texture_data = pygame.image.tostring(texture, "RGBA", True)
        width = texture.get_width()
        height = texture.get_height()

        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        glBindTexture(GL_TEXTURE_2D, 0)

        return texture_id

    @staticmethod
    def clean_up():
        map(glDeleteVertexArrays, Loader._vaos)
        map(glDeleteBuffers, Loader._vbos)
        map(glDeleteTextures, Loader._textures)

    @staticmethod
    def load_to_vao(positions, texture_coords, indices) -> RawModel:
        vao_id = Loader._create_vao()
        Loader._bind_indices_buffer(indices)
        Loader._store_data_in_attribute_list(0, 3, positions, np.float32)
        Loader._store_data_in_attribute_list(1, 2, texture_coords, np.float32)
        Loader._unbind_vao()
        return RawModel(vao_id, indices)

    @staticmethod
    def _create_vao() -> int:
        vao_id = glGenVertexArrays(1)
        Loader._vaos.append(vao_id)
        glBindVertexArray(vao_id)
        return vao_id

    @staticmethod
    def _store_data_in_attribute_list(attribute_number, coordinate_size, data, dtype):
        vbo_id = glGenBuffers(1)
        Loader._vbos.append(vbo_id)
        glBindBuffer(GL_ARRAY_BUFFER, vbo_id)
        buffer = Loader._store_data_in_numpy_array(data, dtype)
        glBufferData(GL_ARRAY_BUFFER, buffer, GL_STATIC_DRAW)
        glVertexAttribPointer(attribute_number, coordinate_size, GL_FLOAT, GL_FALSE, 0, None)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    @staticmethod
    def _unbind_vao():
        glBindVertexArray(0)

    @staticmethod
    def _bind_indices_buffer(indices):
        vbo_id = glGenBuffers(1)
        Loader._vbos.append(vbo_id)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbo_id)
        buffer = Loader._store_data_in_numpy_array(indices, np.uint32)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, buffer, GL_STATIC_DRAW)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    @staticmethod
    def _store_data_in_numpy_array(data, dtype) -> np.array:
        return np.array(data, dtype=dtype)
