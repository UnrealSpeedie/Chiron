from OpenGL.GL import *

from Toolbox.maths import Maths


class TerrainRenderer:
    def __init__(self, shader, projection_matrix):
        self._shader = shader
        shader.start()
        shader.load_projection_matrix(projection_matrix)
        shader.connect_texture_units()
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
        self.bind_textures(terrain)
        self._shader.load_shine_variables(1, 0)

    def bind_textures(self, terrain):
        texture_pack = terrain.texture_pack
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, texture_pack.background_texture.texture_id)
        glActiveTexture(GL_TEXTURE1)
        glBindTexture(GL_TEXTURE_2D, texture_pack.r_texture.texture_id)
        glActiveTexture(GL_TEXTURE2)
        glBindTexture(GL_TEXTURE_2D, texture_pack.g_texture.texture_id)
        glActiveTexture(GL_TEXTURE3)
        glBindTexture(GL_TEXTURE_2D, texture_pack.b_texture.texture_id)
        glActiveTexture(GL_TEXTURE4)
        glBindTexture(GL_TEXTURE_2D, terrain.blend_map.texture_id)


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
