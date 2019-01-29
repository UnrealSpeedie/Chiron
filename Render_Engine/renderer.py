from OpenGL.GL import *
import pygame


class Renderer:
    """
    TODO MAY NOT BE STATIC!
    """

    @staticmethod
    def prepare():
        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)

    @staticmethod
    def render(textured_model):
        model = textured_model.raw_model
        glBindVertexArray(model.vao_id)
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, textured_model.texture.texture_id)
        # This is slightly different from LWJGL's glDrawElements, as it needs the vertices also
        glDrawElements(GL_TRIANGLES, model.vertex_count, GL_UNSIGNED_INT, model.vertices)
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glBindVertexArray(0)
