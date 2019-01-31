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

    _projection_matrix = None

    def __init__(self, shader):
        Renderer.create_projection_matrix()
        shader.start()
        shader.load_projection_matrix(Renderer._projection_matrix)
        shader.stop()

    @staticmethod
    def prepare():
        glEnable(GL_DEPTH_TEST)
        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    @staticmethod
    def render(entity, shader):
        model = entity.model
        raw_model = model.raw_model
        glBindVertexArray(raw_model.vao_id)
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)

        transformation_matrix = Maths.create_transformation_matrix(
            entity.position, entity.rotation[0], entity.rotation[1], entity.rotation[2], entity.scale
        )
        shader.load_transformation_matrix(transformation_matrix)

        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, model.texture.texture_id)
        # This is slightly different from LWJGL's glDrawElements, as it needs the vertices also
        glDrawElements(GL_TRIANGLES, raw_model.vertex_count, GL_UNSIGNED_INT, raw_model.vertices)
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glBindVertexArray(0)

    @staticmethod
    def create_projection_matrix():
        dm = DisplayManager()
        Renderer._projection_matrix = Matrix44
        Renderer._projection_matrix = Renderer._projection_matrix.perspective_projection(
            Renderer._fov, dm.aspect_ratio, Renderer._near_plane, Renderer._far_plane, dtype=np.float32
        )
