from Render_Engine.display_manager import *
from Render_Engine.loader import Loader
from Render_Engine.master_renderer import MasterRenderer
from Textures.model_texture import ModelTexture
from Models.textured_model import TexturedModel
from Entities.entity import Entity
from Entities.camera import Camera
from Render_Engine.obj_loader import OBJLoader
from Entities.light import Light
from Terrain.terrain import Terrain


# Initialize pygame
pygame.init()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

# Create the pygame display and OpenGl context
display = DisplayManager()
display.create_display()

# Creates a loader to load model data
loader = Loader()

# Takes model data and turns in into a model ready to be rendered
model = OBJLoader.load_obj_model("stall", loader)
static_model = TexturedModel(model, ModelTexture(loader.load_texture("stall_texture", "png")))
texture = static_model.texture
texture.shine_damper = 10
texture.reflectivity = 1

model1 = OBJLoader.load_obj_model("cube", loader)
static_model1 = TexturedModel(model1, ModelTexture(loader.load_texture("cube_texture", "jpg")))
texture1 = static_model1.texture
texture1.shine_damper = 10
texture1.reflectivity = 1

model2 = OBJLoader.load_obj_model("tree", loader)
static_model2 = TexturedModel(model2, ModelTexture(loader.load_texture("tree", "png")))
texture2 = static_model2.texture
texture2.shine_damper = 10
texture2.reflectivity = 1

# Makes multiple entities
entities = []
entities.append(Entity(static_model, [0, 0, -15], 0, 180, 0, 1))
entities.append(Entity(static_model1, [10, 2, -15], 0, 20, 0, 2))
entities.append(Entity(static_model1, [7, .5, -15], 0, 0, 0, .5))
entities.append(Entity(static_model1, [12, 1, -11], 0, 0, 0, 1))
entities.append(Entity(static_model2, [-8.5, 0, -14], 0, 0, 0, 6))



# Makes multiple terrain tiles
terrains = []
terrains.append(Terrain(0.5, 0, loader, ModelTexture(loader.load_texture("grass", "png"))))

# Scene light
light = Light([30, 30, 20], [1, 1, 1])

# The view camera
camera = Camera()
camera.position = [0, 3, 0]

# The renderer
renderer = MasterRenderer()

# Beginning!
if __name__ == "__main__":

    # Main game loop
    while True:

        # Event logic
        for event in pygame.event.get():

            # When window is closed
            if event.type == pygame.QUIT:
                renderer.clean_up()
                loader.clean_up()
                display.close_display()
                pygame.quit()
                quit()

            # Key press logic
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    renderer.clean_up()
                    loader.clean_up()
                    display.close_display()
                    pygame.quit()
                    quit()

                if event.key == pygame.K_w:
                    camera.speed = -camera.move_speed

                if event.key == pygame.K_s:
                    camera.speed = camera.move_speed

                if event.key == pygame.K_a:
                    camera.strafe = -camera.move_speed

                if event.key == pygame.K_d:
                    camera.strafe = camera.move_speed

                if event.key == pygame.K_SPACE:
                    camera.height = camera.move_speed

                if event.key == pygame.K_c:
                    camera.height = -camera.move_speed

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

                if event.key == pygame.K_SPACE:
                    camera.height = 0

                if event.key == pygame.K_c:
                    camera.height = 0

        # Camera movement
        camera.move()

        # Multiple entity terrain/render
        for terrain in terrains:
            renderer.process_terrain(terrain)

        for entity in entities:
            renderer.process_entity(entity)
            #entity.increase_rotation(0, 1, 0)

        # Render entities
        renderer.render(light, camera)

        # Update the pygame display
        display.update_display()

        # Pumps event messages from event queue
        pygame.event.pump()
