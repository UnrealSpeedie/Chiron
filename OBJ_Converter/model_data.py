class ModelData:
    def __init__(self, vertices, texture_coords, normals, indices, furthest_point):
        self._vertices = vertices
        self._texture_coords = texture_coords
        self._normals = normals
        self._indices = indices
        self._furthest_point = furthest_point

    @property
    def vertices(self):
        return self._vertices

    @property
    def texture_coords(self):
        return self._texture_coords

    @property
    def normals(self):
        return self._normals

    @property
    def indices(self):
        return self._indices

    @property
    def furthest_point(self):
        return self._furthest_point
