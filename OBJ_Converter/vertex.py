class Vertex:
    _no_index = -1

    def __init__(self, index, position):
        self._position = []
        self._texture_index = Vertex._no_index
        self._normal_index = Vertex._no_index
        self._duplicate_vertex = None
        self._index = index
        self._position = position
        self._length = len(position)

    @property
    def index(self):
        return self._index

    @property
    def length(self):
        return self._length

    @property
    def texture_index(self):
        return self._texture_index

    @property
    def normal_index(self):
        return self._normal_index

    @property
    def position(self):
        return self._position

    def is_set(self):
        return self._texture_index != Vertex._no_index and self._normal_index != Vertex._no_index

    def has_same_texture_and_normal(self, texture_index_other, normal_index_other):
        return texture_index_other == self._texture_index and normal_index_other == self._normal_index

    @texture_index.setter
    def texture_index(self, value):
        self._texture_index = value

    @normal_index.setter
    def normal_index(self, value):
        self._normal_index = value

    @property
    def duplicate_vertex(self):
        return self._duplicate_vertex

    @duplicate_vertex.setter
    def duplicate_vertex(self, value):
        self._duplicate_vertex = value


