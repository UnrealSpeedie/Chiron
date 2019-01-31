import numpy as np
import pygame
from pyrr import Vector3


class Camera:
    def __init__(self):
        self._position = Vector3([0, 0, 0], dtype=np.float32)
        self._pitch = 0
        self._yaw = 0
        self._roll = 0

        self._move_speed = 0.02

        self._speed = 0
        self._strafe = 0

    def move(self):
        self.position.z += self._speed
        self.position.x += self._strafe

    @property
    def position(self):
        return self._position

    @property
    def pitch(self):
        return self._pitch

    @property
    def yaw(self):
        return self._yaw

    @property
    def roll(self):
        return self._roll

    @property
    def move_speed(self):
        return self._move_speed

    @property
    def speed(self):
        return self._speed

    @property
    def strafe(self):
        return self._strafe

    @speed.setter
    def speed(self, value):
        self._speed = value

    @strafe.setter
    def strafe(self, value):
        self._strafe = value
