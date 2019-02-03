from OpenGL.GL import *
from pyrr import Matrix44
import numpy as np

from Shaders.static_shader import StaticShader
from Shaders.terrain_shader import TerrainShader
from Render_Engine.entity_renderer import Renderer
from Render_Engine.display_manager import DisplayManager
from Render_Engine.terrain_renderer import TerrainRenderer


class MasterRenderer:
    _fov = 70
    _near_plane = 0.1
    _far_plane = 1000

    _projection_matrix = None

    def __init__(self):
        # Specific for pygame
        self.aspect_ratio = DisplayManager().aspect_ratio
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        self.terrain_shader = TerrainShader()
        self.create_projection_matrix()
        self.shader = StaticShader()
        self.renderer = Renderer(self.shader, MasterRenderer._projection_matrix)
        self.terrain_renderer = TerrainRenderer(self.terrain_shader, MasterRenderer._projection_matrix)

        self.entities = {}
        self.terrains = []

    def render(self, sun, camera):
        self.prepare()
        self.shader.start()
        self.shader.load_light(sun)
        self.shader.load_view_matrix(camera)
        self.renderer.render(self.entities)
        self.shader.stop()

        # Terrain rendering
        self.terrain_shader.start()
        self.terrain_shader.load_light(sun)
        self.terrain_shader.load_view_matrix(camera)
        self.terrain_renderer.render(self.terrains)
        self.terrain_shader.stop()

        self.terrains.clear()
        self.entities.clear()

    def process_terrain(self, terrain):
        self.terrains.append(terrain)

    def process_entity(self, entity):
        if self.entities.get(entity.model) is not None:
            self.entities.get(entity.model).append(entity)
        else:
            self.entities.update({entity.model: [entity]})

    def clean_up(self):
        self.shader.clean_up()
        self.terrain_shader.clean_up()

    @staticmethod
    def prepare():
        glEnable(GL_DEPTH_TEST)
        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def create_projection_matrix(self):
        MasterRenderer._projection_matrix = Matrix44.perspective_projection(
            MasterRenderer._fov, self.aspect_ratio, MasterRenderer._near_plane, MasterRenderer._far_plane, dtype=np.float32
        )
