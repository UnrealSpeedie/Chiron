from Render_Engine.display_manager import *
from Render_Engine.loader import Loader
from Render_Engine.renderer import Renderer
from Shaders.static_shader import StaticShader
from Textures.model_texture import ModelTexture
from Models.textured_model import TexturedModel

# Initialize Pygame
pygame.init()

# Create the Pygame display and OpenGl context
dm = DisplayManager()
dm.create_display()

# Creates a loader to load model data
loader = Loader()

# Initializes the renderer
renderer = Renderer()

# Loads shaders
static_shader = StaticShader()

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

texture_coords = [
    0, 0,
    0, 1,
    1, 1,
    1, 0
]

# Takes model data and turns in into a model ready to be rendered
model = loader.load_to_vao(vertices, texture_coords, indices)

texture = ModelTexture(loader.load_texture("../res/image.png"))
textured_model = TexturedModel(model, texture)

# Beginning!
if __name__ == "__main__":

    # Main game loop
    while True:

        # Event logic
        for event in pygame.event.get():

            # When window is closed
            if event.type == pygame.QUIT:
                static_shader.clean_up()
                loader.clean_up()
                dm.close_display()
                pygame.quit()
                quit()

        # Prepares OpenGL context
        renderer.prepare()

        # Starts the shader program
        static_shader.start()

        # Renders a model
        renderer.render(textured_model)

        # Stops te shader program
        static_shader.stop()

        # Update the Pygame display
        dm.update_display()

        # Pumps event messages from event queue
        pygame.event.pump()
