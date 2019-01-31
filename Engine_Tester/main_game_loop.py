from Render_Engine.display_manager import *
from Render_Engine.loader import Loader
from Render_Engine.renderer import Renderer
from Shaders.static_shader import StaticShader
from Textures.model_texture import ModelTexture
from Models.textured_model import TexturedModel
from Entities.entity import Entity
from Entities.camera import Camera


# Initialize Pygame
pygame.init()

# Create the Pygame display and OpenGl context
dm = DisplayManager()
dm.create_display()

# Creates a loader to load model data
loader = Loader()

# Loads shaders
shader = StaticShader()

# Initializes the renderer
renderer = Renderer(shader)

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

static_model = TexturedModel(model, ModelTexture(loader.load_texture("../res/image.png")))

entity = Entity(static_model, [0, 0, -1], 0, 0, 0, 1)

camera = Camera()

# Beginning!
if __name__ == "__main__":

    # Main game loop
    while True:

        # Event logic
        for event in pygame.event.get():

            # Camera movement
            camera.move(event)

            # When window is closed
            if event.type == pygame.QUIT:
                shader.clean_up()
                loader.clean_up()
                dm.close_display()
                pygame.quit()
                quit()

        # Prepares OpenGL context
        renderer.prepare()

        # Starts the shader program
        shader.start()

        # Camera view matrix update
        shader.load_view_matrix(camera)

        # Renders a model
        renderer.render(entity, shader)
        #entity.increase_position(0, 0, -0.1)

        # Stops te shader program
        shader.stop()

        # Update the Pygame display
        dm.update_display()

        # Pumps event messages from event queue
        pygame.event.pump()
