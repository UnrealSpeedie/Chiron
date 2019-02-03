from OpenGL.GL import *

from Toolbox.maths import Maths


class TerrainRenderer:
    def __init__(self, shader, projection_matrix):
        self._shader = shader
        shader.start()
        shader.load_projection_matrix(projection_matrix)
        shader.stop()

    def render(self, terrains):
        for terrain in terrains:
            self.prepare_terrain(terrain)
            self.load_model_matrix(terrain)
            glDrawElements(GL_TRIANGLES, terrain.model.vertex_count, GL_UNSIGNED_INT, terrain.model.vertices)
            self.unbind_textured_model()

    def prepare_terrain(self, terrain):
        glBindVertexArray(terrain.model.vao_id)
        glEnableVertexAttribArray(0)  # enables positions
        glEnableVertexAttribArray(1)  # enables texture coordinates
        glEnableVertexAttribArray(2)  # enables normals
        self._shader.load_shine_variables(terrain.texture.shine_damper, terrain.texture.reflectivity)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, terrain.texture.texture_id)

    @staticmethod
    def unbind_textured_model():
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glDisableVertexAttribArray(2)
        glBindVertexArray(0)

    def load_model_matrix(self, terrain):
        self._shader.load_transformation_matrix(
            Maths.create_transformation_matrix(
                [terrain.x, 0, terrain.z], 0, 0, 0, 1)
        )
