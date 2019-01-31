import numpy as np
from pyrr import Matrix44, Vector3


class Maths:

    @staticmethod
    def create_transformation_matrix(translation, rx, ry, rz, scale) -> Matrix44:
        matrix = Matrix44
        matrix = matrix.identity()
        matrix = matrix.from_translation([translation])
        matrix = matrix * matrix.from_x_rotation(np.radians(rx))
        matrix = matrix * matrix.from_y_rotation(np.radians(ry))
        matrix = matrix * matrix.from_z_rotation(np.radians(rz))
        matrix = matrix * matrix.from_scale([scale, scale, scale])
        return matrix

    @staticmethod
    def create_view_matrix(camera):
        view_matrix = Matrix44
        view_matrix = view_matrix.identity(dtype=np.float32)
        view_matrix = view_matrix.from_x_rotation(np.radians(camera.pitch), dtype=np.float32)
        view_matrix = view_matrix * view_matrix.from_y_rotation(np.radians(camera.yaw), dtype=np.float32)
        camera_pos = camera.position
        negative_camera_position = Vector3([-camera_pos.x, -camera_pos.y, -camera_pos.z], dtype=np.float32)
        view_matrix = view_matrix * view_matrix.from_translation(negative_camera_position, dtype=np.float32)
        return view_matrix
