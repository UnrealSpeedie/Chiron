import numpy as np


class RawModel:
    def __init__(self, vao_id, vertices):
        self._vao_id = vao_id
        self._vertices = vertices
        self._vertex_count = len(vertices)

    @property
    def vao_id(self) -> int:
        return self._vao_id

    # This is needed for pyOpenGL implementation of OpenGL function
    @property
    def vertices(self) -> np.array([], dtype=np.uint32):
        return self._vertices

    @property
    def vertex_count(self) -> int:
        return self._vertex_count
