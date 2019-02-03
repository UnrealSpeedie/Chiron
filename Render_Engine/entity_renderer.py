from OpenGL.GL import *
from Toolbox.maths import Maths


class Renderer:
    """
    TODO MAY NOT BE STATIC!
    """
    def __init__(self, shader, projection_matrix):
        self._shader = shader
        shader.start()
        shader.load_projection_matrix(projection_matrix)
        shader.stop()

    def render(self, entities):
        for model in entities.keys():
            self.prepare_textured_model(model)
            for entity in entities.get(model):
                self.prepare_instance(entity)
                glDrawElements(GL_TRIANGLES, model.raw_model.vertex_count, GL_UNSIGNED_INT, model.raw_model.vertices)

        self.unbind_textured_model()

    def prepare_textured_model(self, model):
        glBindVertexArray(model.raw_model.vao_id)
        glEnableVertexAttribArray(0)  # enables positions
        glEnableVertexAttribArray(1)  # enables texture coordinates
        glEnableVertexAttribArray(2)  # enables normals
        self._shader.load_shine_variables(model.texture.shine_damper, model.texture.reflectivity)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, model.texture.texture_id)

    @staticmethod
    def unbind_textured_model():
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glDisableVertexAttribArray(2)
        glBindVertexArray(0)

    def prepare_instance(self, entity):
        self._shader.load_transformation_matrix(
            Maths.create_transformation_matrix(
                entity.position, entity.rotation[0], entity.rotation[1], entity.rotation[2], entity.scale)
        )
