import pygame


class Camera:
    def __init__(self):
        self._position = [0, 0, 0]
        self._pitch = 0
        self._yaw = 0
        self._roll = 0

        self._pitch_sensitivity = 0.2
        self._yaw_sensitivity = 0.2

        self._move_speed = 0.1

        self._speed = 0
        self._strafe = 0
        self._height = 0

    def move(self):
        self._position[2] += self._speed
        self._position[0] += self._strafe
        self._position[1] += self._height

        # Oddly, mouse input has to be collected in camera?
        mouse_rel = pygame.mouse.get_rel()
        self._pitch += -mouse_rel[1] * self._pitch_sensitivity
        self._yaw += -mouse_rel[0] * self._yaw_sensitivity

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

    @property
    def height(self):
        return self._height

    @position.setter
    def position(self, value):
        self._position = value

    @speed.setter
    def speed(self, value):
        self._speed = value

    @strafe.setter
    def strafe(self, value):
        self._strafe = value

    @height.setter
    def height(self, value):
        self._height = value

    @pitch.setter
    def pitch(self, value):
        self._pitch = value * self._pitch_sensitivity

    @yaw.setter
    def yaw(self, value):
        self._yaw = value * self._yaw_sensitivity
