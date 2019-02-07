from OBJ_Converter.vertex import Vertex
from OBJ_Converter.model_data import ModelData


class OBJFileLoader:

    @staticmethod
    def model_data(obj_file_name):
        with open("../res/{}.obj".format(obj_file_name, "r")) as f:
            data = f.readlines()

            vertices = []
            textures = []
            normals = []
            indices = []

            for line in data:
                line = line.split()

                if line[0] == "v":
                    vertex = [float(f) for f in line[1:]]
                    new_vertex = Vertex(len(vertices), vertex)
                    vertices.append(new_vertex)

                elif line[0] == "vt":
                    texture = [float(f) for f in line[1:]]
                    textures.append(texture)

                elif line[0] == "vn":
                    normal = [float(f) for f in line[1:]]
                    normals.append(normal)

                elif line[0] == "f":
                    break

            for line in data:
                line = line.split()
                if line[0] == "f":
                    vertex1 = list(map(int, line[1].split("/")))
                    vertex2 = list(map(int, line[2].split("/")))
                    vertex3 = list(map(int, line[3].split("/")))
                    OBJFileLoader.process_vertex(vertex1, vertices, indices)
                    OBJFileLoader.process_vertex(vertex2, vertices, indices)
                    OBJFileLoader.process_vertex(vertex3, vertices, indices)

        OBJFileLoader.remove_unused_vertices(vertices)
        vertices_array = [0.0]*len(vertices)*3
        textures_array = [0.0]*len(vertices)*2
        normals_array = [0.0]*len(vertices)*3

        furthest = OBJFileLoader.convert_data_to_arrays(vertices, textures, normals, vertices_array, textures_array, normals_array)

        indices_array = OBJFileLoader.convert_indices_list_to_array(indices)

        data = ModelData(vertices_array, textures_array, normals_array, indices_array, furthest)

        return data

    @staticmethod
    def process_vertex(vertex, vertices, indices):
        index = vertex[0] - 1
        current_vertex = vertices[index]
        texture_index = vertex[1] - 1
        normal_index = vertex[2] - 1
        if not current_vertex.is_set():
            current_vertex.texture_index = texture_index
            current_vertex.normal_index = normal_index
            indices.append(index)
        else:
            OBJFileLoader.deal_with_already_processed_vertex(current_vertex, texture_index, normal_index, indices, vertices)

    @staticmethod
    def convert_indices_list_to_array(indices):
        indices_array = [0]*len(indices)
        for i in range(0, len(indices)):
            indices_array[i] = indices[i]
        return indices_array

    @staticmethod
    def convert_data_to_arrays(vertices, textures, normals, vertices_array, textures_array, normals_array):
        furthest_point = 0
        for i in range(0, len(vertices)):
            current_vertex = vertices[i]
            if current_vertex.length > furthest_point:
                furthest_point = current_vertex.length

            position = current_vertex.position
            texture_coord = textures[current_vertex.texture_index]
            normal_vector = normals[current_vertex.normal_index]
            vertices_array[i * 3] = position[0]
            vertices_array[i * 3 + 1] = position[1]
            vertices_array[i * 3 + 2] = position[2]
            textures_array[i * 2] = texture_coord[0]
            textures_array[i * 2 + 1] = texture_coord[1]    # It seems this does no need the "1 -" before the texture
            normals_array[i * 3] = normal_vector[0]
            normals_array[i * 3 + 1] = normal_vector[1]
            normals_array[i * 3 + 2] = normal_vector[2]

        return furthest_point

    @staticmethod
    def deal_with_already_processed_vertex(previous_vertex, new_texture_index, new_normal_index, indices, vertices):
        if previous_vertex.has_same_texture_and_normal(new_texture_index, new_normal_index):
            indices.append(previous_vertex.index)
        else:
            another_vertex = previous_vertex.duplicate_vertex
            if another_vertex is not None:
                OBJFileLoader.deal_with_already_processed_vertex(another_vertex, new_texture_index, new_normal_index, indices, vertices)
            else:
                duplicate_vertex = Vertex(len(vertices), previous_vertex.position)
                duplicate_vertex.texture_index = new_texture_index
                duplicate_vertex.normal_index = new_normal_index
                previous_vertex.duplicate_vertex = duplicate_vertex
                vertices.append(duplicate_vertex)
                indices.append(duplicate_vertex.index)

    @staticmethod
    def remove_unused_vertices(vertices):
        for vertex in vertices:
            if not vertex.is_set():
                vertex.texture_index = 0
                vertex.normal_index = 0

# o = OBJFileLoader().model_data("stall")
