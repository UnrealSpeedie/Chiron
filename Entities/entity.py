import numpy as np


class Entity:
    def __init__(self, model, position, rot_x, rot_y, rot_z, scale):
        self._model = model
        self._position = np.array(position, dtype=np.float32)
        self._rotation = np.array([rot_x, rot_y, rot_z], dtype=np.float32)
        self._scale = scale

    def increase_position(self, dx, dy, dz):
        self._position += [dx, dy, dz]

    def increase_rotation(self, dx, dy, dz):
        self._rotation += [dx, dy, dz]

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = np.array(value, dtype=np.float32)

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = np.array(value, dtype=np.float32)

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = value
