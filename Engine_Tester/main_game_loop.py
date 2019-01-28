from Render_Engine.display_manager import *
from Render_Engine.loader import Loader
from Render_Engine.renderer import Renderer


# Initialize Pygame
pygame.init()

# Create the Pygame display and OpenGl context
dm = DisplayManager()
dm.create_display()

loader = Loader()

renderer = Renderer()

# Test rectangle
vertices = [
    -0.5, 0.5, 0,
    -0.5, -0.5, 0,
    0.5, -0.5, 0,
    0.5, 0.5, 0
]

indices = [
    0, 1, 3,
    3, 1, 2
]

model = loader.load_to_vao(vertices, indices)

# Beginning!
if __name__ == "__main__":

    # Main game loop
    while True:

        # Event logic
        for event in pygame.event.get():

            # When window is closed
            if event.type == pygame.QUIT:
                loader.clean_up()
                dm.close_display()
                pygame.quit()
                quit()

        # Prepares OpenGL context
        renderer.prepare()

        # Renders a model
        renderer.render(model)

        # Update the Pygame display
        dm.update_display()

        # Pumps event messages from event queue
        pygame.event.pump()
