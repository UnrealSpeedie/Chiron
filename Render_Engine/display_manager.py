import pygame
from pygame.locals import *


class DisplayManager:
    # Basic attributes of Pygame display
    _display = None
    _display_size = (960, 600)
    _aspect_ratio = _display_size[0] / _display_size[1]
    _display_title = "Interactive 3D Python Engine"

    _time = pygame.time.Clock()  # Used to initialise the Pygame clock to set FPS
    _fps = 100

    @staticmethod
    def create_display():
        # Create the Pygame display and set the display's title
        DisplayManager._display = pygame.display.set_mode(DisplayManager._display_size, pygame.HWSURFACE | DOUBLEBUF | OPENGL)
        pygame.display.set_caption(DisplayManager._display_title)

    @staticmethod
    def update_display():
        # Updates display
        pygame.display.flip()

        # Limits to FPS
        DisplayManager._time.tick(DisplayManager._fps)

        #print(DisplayManager._time.get_fps())

    @staticmethod
    def close_display():
        # Used to destroy the Pygame display
        pygame.display.quit()

    @property
    def aspect_ratio(self):
        return DisplayManager._aspect_ratio
