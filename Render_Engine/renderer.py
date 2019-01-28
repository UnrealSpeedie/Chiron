from OpenGL.GL import *


class Renderer:
    """
    TODO MAY NOT BE STATIC!
    """

    @staticmethod
    def prepare():
        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)

    @staticmethod
    def render(model):
        glBindVertexArray(model.vao_id)
        glEnableVertexAttribArray(0)
        # This is slightly different from LWJGL's glDrawElements, as it needs the vertices also
        glDrawElements(GL_TRIANGLES, model.vertex_count, GL_UNSIGNED_INT, model.vertices)
        glDisableVertexAttribArray(0)
        glBindVertexArray(0)
