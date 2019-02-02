import numpy as np
from pyrr import Matrix44


class Maths:

    @staticmethod
    def create_transformation_matrix(translation, rx, ry, rz, scale) -> Matrix44:
        matrix = Matrix44.identity()
        matrix = matrix.from_translation([translation])
        matrix = matrix * matrix.from_x_rotation(np.radians(rx)) * matrix.from_y_rotation(np.radians(ry)) * \
                 matrix.from_z_rotation(np.radians(rz)) * matrix.from_scale([scale, scale, scale])
        return matrix

    @staticmethod
    def create_view_matrix(camera):
        view_matrix = Matrix44.identity()
        view_matrix = view_matrix.from_x_rotation(np.radians(camera.pitch)) * \
                      view_matrix.from_y_rotation(np.radians(camera.yaw))
        negative_camera_position = [-camera.position[0], -camera.position[1], -camera.position[2]]
        view_matrix = view_matrix * view_matrix.from_translation(negative_camera_position)
        return view_matrix
