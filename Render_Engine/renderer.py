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
        glDrawArrays(GL_TRIANGLES, 0, model.vertex_count)
        glDisableVertexAttribArray(0)
        glBindVertexArray(0)
