from OpenGL.GL import *

import numpy as np

from Render_Engine.raw_model import RawModel


class Loader:
    """
    TODO THIS CLASS MAY NOT BE STATIC!
    """

    # Used for clean up by keeping track of all VAOs/VBOs created
    _vaos = []
    _vbos = []

    @staticmethod
    def clean_up():
        map(glDeleteVertexArrays, Loader._vaos)
        map(glDeleteBuffers, Loader._vbos)

    @staticmethod
    def load_to_vao(positions, indices) -> RawModel:
        vao_id = Loader._create_vao()
        Loader._bind_indices_buffer(indices)
        Loader._store_data_in_attribute_list(0, positions)
        Loader._unbind_vao()
        return RawModel(vao_id, indices)

    @staticmethod
    def _create_vao() -> int:
        vao_id = glGenVertexArrays(1)
        Loader._vaos.append(vao_id)
        glBindVertexArray(vao_id)
        return vao_id

    @staticmethod
    def _store_data_in_attribute_list(attribute_number, data):
        vbo_id = glGenBuffers(1)
        Loader._vbos.append(vbo_id)
        glBindBuffer(GL_ARRAY_BUFFER, vbo_id)
        buffer = Loader._store_data_in_float32_numpy_array(data)
        glBufferData(GL_ARRAY_BUFFER, buffer, GL_STATIC_DRAW)
        glVertexAttribPointer(attribute_number, 3, GL_FLOAT, False, 0, None)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    @staticmethod
    def _unbind_vao():
        glBindVertexArray(0)

    @staticmethod
    def _bind_indices_buffer(indices):
        vbo_id = glGenBuffers(1)
        Loader._vbos.append(vbo_id)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbo_id)
        buffer = Loader._store_data_in_uint32_numpy_array(indices)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, buffer, GL_STATIC_DRAW)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    @staticmethod
    def _store_data_in_uint32_numpy_array(data) -> np.array([], dtype=np.uint32):
        return np.array(data, dtype=np.uint32)

    @staticmethod
    def _store_data_in_float32_numpy_array(data) -> np.array([], dtype=np.float32):
        return np.array(data, dtype=np.float32)
