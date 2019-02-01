class OBJLoader:

    @staticmethod
    def load_obj_model(file_name, loader):
        vertices = []
        textures = []
        normals = []
        indices = []

        textures_array = []
        normals_array = []

        with open("../res/{}.obj".format(file_name), "r") as f:
            data = f.readlines()

            for line in data:
                line = line.split()

                if line[0] == "v":
                    vertex = [float(f) for f in line[1:]]
                    vertices.append(vertex)

                elif line[0] == "vt":
                    texture = [float(f) for f in line[1:]]
                    textures.append(texture)

                elif line[0] == "vn":
                    normal = [float(f) for f in line[1:]]
                    normals.append(normal)

                elif line[0] == "f":
                    textures_array = [0.0]*len(vertices)*2
                    normals_array = [0.0]*len(vertices)*3

                    break

            for line in data:
                line = line.split()
                if line[0] == "f":
                    vertex1 = list(map(int, line[1].split("/")))
                    vertex2 = list(map(int, line[2].split("/")))
                    vertex3 = list(map(int, line[3].split("/")))

                    OBJLoader.process_vertex(vertex1, indices, textures, normals, textures_array, normals_array)
                    OBJLoader.process_vertex(vertex2, indices, textures, normals, textures_array, normals_array)
                    OBJLoader.process_vertex(vertex3, indices, textures, normals, textures_array, normals_array)

        vertices_array = [0.0]*len(vertices)*3
        indices_array = [0]*len(indices)

        indices_pointer = 0

        for vertex in vertices:
            vertices_array[indices_pointer] = vertex[0]
            indices_pointer += 1
            vertices_array[indices_pointer] = vertex[1]
            indices_pointer += 1
            vertices_array[indices_pointer] = vertex[2]
            indices_pointer += 1

        for i in range(0, len(indices)):
            indices_array[i] = indices[i]

        return loader.load_to_vao(vertices_array, textures_array, normals_array, indices_array)

    @staticmethod
    def process_vertex(vertex_data, indices, textures, normals, texture_array, normals_array):
        current_vertex_pointer = vertex_data[0] - 1
        indices.append(current_vertex_pointer)

        current_tex = textures[vertex_data[1] - 1]
        texture_array[current_vertex_pointer * 2] = current_tex[0]
        texture_array[current_vertex_pointer * 2 + 1] = current_tex[1]

        current_norm = normals[vertex_data[2] - 1]
        normals_array[current_vertex_pointer * 3] = current_norm[0]
        normals_array[current_vertex_pointer * 3 + 1] = current_norm[1]
        normals_array[current_vertex_pointer * 3 + 2] = current_norm[2]
