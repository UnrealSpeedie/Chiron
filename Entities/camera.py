import numpy as np
import pygame
from pyrr import Vector3


class Camera:
    def __init__(self):
        self._position = Vector3([0, 0, 0], dtype=np.float32)
        self._pitch = 0
        self._yaw = 0
        self._roll = 0

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self._position.z -= 0.1

            if event.key == pygame.K_s:
                self._position.z += 0.1

            if event.key == pygame.K_a:
                self._position.x -= 0.1

            if event.key == pygame.K_d:
                self._position.x += 0.1

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
