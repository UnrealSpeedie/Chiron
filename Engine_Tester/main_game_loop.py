from Render_Engine.display_manager import *
from Render_Engine.loader import Loader
from Render_Engine.renderer import Renderer
from Shaders.static_shader import StaticShader
from Textures.model_texture import ModelTexture
from Models.textured_model import TexturedModel
from Entities.entity import Entity
from Entities.camera import Camera
from Render_Engine.obj_loader import OBJLoader
from Entities.light import Light


# Initialize Pygame
pygame.init()

# Create the Pygame display and OpenGl context
display = DisplayManager()
display.create_display()

# Creates a loader to load model data
loader = Loader()

# Loads shaders
shader = StaticShader()

# Initializes the renderer
renderer = Renderer(shader)

# Test rectangle
"""
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
"""

# Test cube
"""
vertices = [
    -0.5, 0.5, -0.5,
    -0.5, -0.5, -0.5,
    0.5, -0.5, -0.5,
    0.5, 0.5, -0.5,

    -0.5, 0.5, 0.5,
    -0.5, -0.5, 0.5,
    0.5, -0.5, 0.5,
    0.5, 0.5, 0.5,

    0.5, 0.5, -0.5,
    0.5, -0.5, -0.5,
    0.5, -0.5, 0.5,
    0.5, 0.5, 0.5,

    -0.5, 0.5, -0.5,
    -0.5, -0.5, -0.5,
    -0.5, -0.5, 0.5,
    -0.5, 0.5, 0.5,

    -0.5, 0.5, 0.5,
    -0.5, 0.5, -0.5,
    0.5, 0.5, -0.5,
    0.5, 0.5, 0.5,

    -0.5, -0.5, 0.5,
    -0.5, -0.5, -0.5,
    0.5, -0.5, -0.5,
    0.5, -0.5, 0.5
]

texture_coords = [
    0, 0,
    0, 1,
    1, 1,
    1, 0,
    0, 0,
    0, 1,
    1, 1,
    1, 0,
    0, 0,
    0, 1,
    1, 1,
    1, 0,
    0, 0,
    0, 1,
    1, 1,
    1, 0,
    0, 0,
    0, 1,
    1, 1,
    1, 0,
    0, 0,
    0, 1,
    1, 1,
    1, 0
]

indices = [
    0, 1, 3,
    3, 1, 2,
    4, 5, 7,
    7, 5, 6,
    8, 9, 11,
    11, 9, 10,
    12, 13, 15,
    15, 13, 14,
    16, 17, 19,
    19, 17, 18,
    20, 21, 23,
    23, 21, 22
]
"""

# Takes model data and turns in into a model ready to be rendered
model = OBJLoader.load_obj_model("dragon", loader)

static_model = TexturedModel(model, ModelTexture(loader.load_texture("white_texture")))

entity = Entity(static_model, [0, 0, -25], 0, 0, 0, 1)
light = Light([0, 0, -20], [1, 1, 1])

camera = Camera()

# Beginning!
if __name__ == "__main__":

    # Main game loop
    while True:

        # Event logic
        for event in pygame.event.get():

            # When window is closed
            if event.type == pygame.QUIT:
                shader.clean_up()
                loader.clean_up()
                display.close_display()
                pygame.quit()
                quit()

            # Key press logic
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    camera.speed = -camera.move_speed

                if event.key == pygame.K_s:
                    camera.speed = camera.move_speed

                if event.key == pygame.K_a:
                    camera.strafe = -camera.move_speed

                if event.key == pygame.K_d:
                    camera.strafe = camera.move_speed

            # Key release logic
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    camera.speed = 0

                if event.key == pygame.K_s:
                    camera.speed = 0

                if event.key == pygame.K_a:
                    camera.strafe = 0

                if event.key == pygame.K_d:
                    camera.strafe = 0

        # Camera movement
        camera.move()

        # Prepares OpenGL context
        renderer.prepare()

        # Starts the shader program
        shader.start()

        # Loads a light to the frame
        shader.load_light(light)

        # Camera view matrix update
        shader.load_view_matrix(camera)

        # Renders a model
        renderer.render(entity, shader)

        entity.increase_rotation(0, 1, 0)

        # Stops te shader program
        shader.stop()

        # Update the Pygame display
        display.update_display()

        # Pumps event messages from event queue
        pygame.event.pump()
