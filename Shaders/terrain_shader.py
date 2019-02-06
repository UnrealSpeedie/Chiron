from Toolbox.maths import Maths

from Shaders.shader_program import ShaderProgram


class TerrainShader(ShaderProgram):
    vertex_file = "../shaders/terrain_vertex_shader.txt"
    fragment_file = "../shaders/terrain_fragment_shader.txt"

    def __init__(self):
        super().__init__(TerrainShader.vertex_file, TerrainShader.fragment_file)
        self.location_transformation_matrix = super().get_uniform_location("transformationMatrix")
        self.location_projection_matrix = super().get_uniform_location("projectionMatrix")
        self.location_view_matrix = super().get_uniform_location("viewMatrix")
        self.location_light_position = super().get_uniform_location("lightPosition")
        self.location_light_colour = super().get_uniform_location("lightColour")
        self.location_shine_damper = super().get_uniform_location("shineDamper")
        self.location_reflectivity = super().get_uniform_location("reflectivity")
        self.location_sky_colour = super().get_uniform_location("skyColour")

    def bind_attributes(self):
        super().bind_attribute(0, "position")
        super().bind_attribute(1, "textureCoords")
        super().bind_attribute(2, "normal")

    # TODO PERHAPS MAKE IT WORK?
    # This function need to bee modified to work and it is not called, but will be implemented for posterity
    # def get_all_uniform_locations(self):
    #     self.location_transformation_matrix = super().get_uniform_location("transformationMatrix")
    #     self.location_projection_matrix = super().get_uniform_location("projectionMatrix")
    #     self.location_view_matrix = super().get_uniform_location("viewMatrix")
    #     self.location_light_position = super().get_uniform_location("lightPosition")
    #     self.location_light_colour = super().get_uniform_location("lightColour")
    #     self.location_shine_damper = super().get_uniform_location("shineDamper")
    #     self.location_reflectivity = super().get_uniform_location("reflectivity")
    #     self.location_sky_colour = super().get_uniform_location("skyColour")

    def load_sky_colour(self, r, g, b):
        super().load_vector(self.location_sky_colour, [r, g, b])

    def load_shine_variables(self, damper, reflectivity):
        super().load_float(self.location_shine_damper, damper)
        super().load_float(self.location_reflectivity, reflectivity)

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
