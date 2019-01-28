import pygame
from pygame.locals import *


class DisplayManager:
    # Basic attributes of Pygame display
    _display = None
    _display_size = (800, 600)
    _aspect_ratio = _display_size[0] / _display_size[1]
    _display_title = "3D Python Game"

    _time = pygame.time.Clock()  # Used to initialise the Pygame clock to set FPS
    _fps = 100

    @staticmethod
    def create_display():
        # Create the Pygame display and set the display's title
        DisplayManager._display = pygame.display.set_mode(DisplayManager._display_size, DOUBLEBUF | OPENGL)
        pygame.display.set_caption(DisplayManager._display_title)

    @staticmethod
    def update_display():
        # Updates display
        pygame.display.flip()

        # Limits to FPS
        DisplayManager._time.tick(DisplayManager._fps)

    @staticmethod
    def close_display():
        # Used to destroy the Pygame display
        pygame.display.quit()
