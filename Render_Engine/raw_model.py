class RawModel:
    def __init__(self, vao_id, vertex_count):
        self._vao_id = vao_id
        self._vertex_count = vertex_count

    @property
    def vao_id(self) -> int:
        return self._vao_id

    @property
    def vertex_count(self) -> int:
        return self._vertex_count
