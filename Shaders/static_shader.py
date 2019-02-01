from Shaders.shader_program import *
from Toolbox.maths import Maths


class StaticShader(ShaderProgram):
    vertex_file = "../shaders/vertex_shader.txt"
    fragment_file = "../shaders/fragment_shader.txt"

    def __init__(self):
        super().__init__(StaticShader.vertex_file, StaticShader.fragment_file)
        self.location_transformation_matrix = super().get_uniform_location("transformationMatrix")
        self.location_projection_matrix = super().get_uniform_location("projectionMatrix")
        self.location_view_matrix = super().get_uniform_location("viewMatrix")
        self.location_light_position = super().get_uniform_location("lightPosition")
        self.location_light_colour = super().get_uniform_location("lightColour")

    def bind_attributes(self):
        super().bind_attribute(0, "position")
        super().bind_attribute(1, "textureCoords")
        super().bind_attribute(2, "normal")


    # TODO PERHAPS MAKE IT WORK
    # This function need to bee modified to work and it is not called, but will be implemented for posterity
    def get_all_uniform_locations(self):
        self.location_transformation_matrix = super().get_uniform_location("transformationMatrix")
        self.location_projection_matrix = super().get_uniform_location("projectionMatrix")
        self.location_view_matrix = super().get_uniform_location("viewMatrix")
        self.location_light_position = super().get_uniform_location("lightPosition")
        self.location_light_colour = super().get_uniform_location("lightColour")

    def load_transformation_matrix(self, matrix):
        super().load_matrix(self.location_transformation_matrix, matrix)

    def load_light(self, light):
        super().load_vector(self.location_light_position, light.position)
        super().load_vector(self.location_light_colour, light.colour)

    def load_view_matrix(self, camera):
        view_matrix = Maths.create_view_matrix(camera)
        super().load_matrix(self.location_view_matrix, view_matrix)

    def load_projection_matrix(self, matrix):
        super().load_matrix(self.location_projection_matrix, matrix)
