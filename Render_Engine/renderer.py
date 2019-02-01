from OpenGL.GL import *
from Toolbox.maths import Maths
from pyrr import Matrix44
import numpy as np

from Render_Engine.display_manager import DisplayManager


class Renderer:
    """
    TODO MAY NOT BE STATIC!
    """

    _fov = 70
    _near_plane = 0.1
    _far_plane = 1000

    def __init__(self, shader):
        self._projection_matrix = None
        self._shader = shader
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        self.create_projection_matrix()
        shader.start()
        shader.load_projection_matrix(self._projection_matrix)
        shader.stop()

    @staticmethod
    def prepare():
        glEnable(GL_DEPTH_TEST)
        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def render(self, entities):
        for model in entities.keys():
            self.prepare_textured_model(model)
            batch = entities.get(model)
            for entity in batch:
                self.prepare_instance(entity)
                glDrawElements(GL_TRIANGLES, model.raw_model.vertex_count, GL_UNSIGNED_INT, model.raw_model.vertices)

        self.unbind_textured_model()

    def prepare_textured_model(self, model):
        raw_model = model.raw_model
        glBindVertexArray(raw_model.vao_id)
        glEnableVertexAttribArray(0)  # enables positions
        glEnableVertexAttribArray(1)  # enables texture coordinates
        glEnableVertexAttribArray(2)  # enables normals
        texture = model.texture
        self._shader.load_shine_variables(texture.shine_damper, texture.reflectivity)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, model.texture.texture_id)

    @staticmethod
    def unbind_textured_model():
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glDisableVertexAttribArray(2)
        glBindVertexArray(0)

    def prepare_instance(self, entity):
        transformation_matrix = Maths.create_transformation_matrix(
            entity.position, entity.rotation[0], entity.rotation[1], entity.rotation[2], entity.scale
        )
        self._shader.load_transformation_matrix(transformation_matrix)

    def create_projection_matrix(self):
        dm = DisplayManager()
        self._projection_matrix = Matrix44
        self._projection_matrix = self._projection_matrix.perspective_projection(
            Renderer._fov, dm.aspect_ratio, Renderer._near_plane, Renderer._far_plane, dtype=np.float32
        )
