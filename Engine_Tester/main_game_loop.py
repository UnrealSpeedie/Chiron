from Render_Engine.display_manager import *
#from Render_Engine.raw_model import RawModel
from Render_Engine.loader import Loader
from Render_Engine.renderer import Renderer


# Initialize Pygame
pygame.init()

# Create the Pygame display and OpenGl context
dm = DisplayManager()
dm.create_display()

#rm = RawModel(1, 0)

loader = Loader()

renderer = Renderer()

# Test rectangle
vertices = [
    # Left bottom triangle
    -0.5, 0.5, 0,
    -0.5, -0.5, 0,
    0.5, -0.5, 0,
    # Right top triangle
    0.5, -0.5, 0,
    0.5, 0.5, 0,
    -0.5, 0.5, 0
]

model = loader.load_to_vao(vertices)

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
