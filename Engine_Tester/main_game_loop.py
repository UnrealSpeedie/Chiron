from Render_Engine.display_manager import *
from Render_Engine.loader import Loader
from Render_Engine.master_renderer import MasterRenderer
from Entities.camera import Camera
from Entities.light import Light
from Engine_Tester.scene import Scene

# Initialize pygame
pygame.init()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

# Create the pygame display and OpenGl context
display = DisplayManager()
display.create_display()

# Creates a loader to load model data
loader = Loader()

# Creates a scene
scene = Scene()
scene.scene1()

# Takes entity and terrain data
entities = scene.load_scene_entities()
terrains = scene.load_scene_terrains()

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
