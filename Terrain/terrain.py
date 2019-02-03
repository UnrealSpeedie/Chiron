class Terrain:
    _size = 50
    _vertex_count = 8

    def __init__(self, grid_x, grid_z, loader, texture):
        self.loader = loader
        self._texture = texture
        self._x = grid_x * Terrain._size
        self._z = grid_z * Terrain._size
        self._model = self.generate_terrain(loader)

    @property
    def vertex_count(self):
        return self._vertex_count

    @property
    def model(self):
        return self._model

    @property
    def texture(self):
        return self._texture

    @property
    def x(self):
        return self._x

    @property
    def z(self):
        return self._z

    def generate_terrain(self, loader):
        count = Terrain._vertex_count * Terrain._vertex_count
        vertices = [0.0]*count*3
        normals = [0.0]*count*3
        texture_coords = [0.0]*count*2
        indices = [0]*6*(Terrain._vertex_count-1)*(Terrain._vertex_count*1)
        vertex_pointer = 0

        for i in range(Terrain._vertex_count):
            for j in range(Terrain._vertex_count):
                vertices[vertex_pointer * 3] = -float(j)/float(Terrain._vertex_count - 1) * Terrain._size
                vertices[vertex_pointer * 3 + 1] = 0
                vertices[vertex_pointer * 3 + 2] = -float(i)/float(Terrain._vertex_count - 1) * Terrain._size
                normals[vertex_pointer * 3] = 0
                normals[vertex_pointer * 3 + 1] = 1
                normals[vertex_pointer * 3 + 2] = 0
                texture_coords[vertex_pointer*2] = float(j)/float(Terrain._vertex_count - 1)
                texture_coords[vertex_pointer*2+1] = float(i)/float(Terrain._vertex_count - 1)
                vertex_pointer += 1

                pointer = 0
                for gz in range(Terrain._vertex_count-1):
                    for gx in range(Terrain._vertex_count-1):
                        top_left = (gz*Terrain._vertex_count)+gx
                        top_right = top_left + 1
                        bottom_left = ((gz+1)*Terrain._vertex_count)+gx
                        bottom_right = bottom_left + 1
                        indices[pointer] = top_left
                        pointer += 1
                        indices[pointer] = bottom_left
                        pointer += 1
                        indices[pointer] = top_right
                        pointer += 1
                        indices[pointer] = top_right
                        pointer += 1
                        indices[pointer] = bottom_left
                        pointer += 1
                        indices[pointer] = bottom_right
                        pointer += 1

        return loader.load_to_vao(vertices, texture_coords, normals, indices)
