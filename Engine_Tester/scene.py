# from Render_Engine.obj_loader import OBJLoader    # Old way
from Models.textured_model import TexturedModel
from Textures.model_texture import ModelTexture
from Render_Engine.loader import Loader
from Entities.entity import Entity
from Terrain.terrain import Terrain
from OBJ_Converter.obj_file_loader import OBJFileLoader
from Textures.terrain_texture import TerrainTexture
from Textures.terrain_texture_pack import  TerrainTexturePack


class Scene:
    def __init__(self):
        self.loader = Loader()
        self.entities = []
        self.terrains = []

    def scene1(self):
        model = OBJFileLoader.model_data("stall")
        model = self.loader.load_model_to_vao(model)
        static_model = TexturedModel(model, ModelTexture(self.loader.load_texture("stall_texture", "png")))
        texture = static_model.texture
        texture.shine_damper = 10
        texture.reflectivity = 1

        model1 = OBJFileLoader.model_data("cube")
        model1 = self.loader.load_model_to_vao(model1)
        static_model1 = TexturedModel(model1, ModelTexture(self.loader.load_texture("cube_texture", "jpg")))
        texture1 = static_model1.texture
        texture1.shine_damper = 10
        texture1.reflectivity = 1

        model2 = OBJFileLoader.model_data("tree")
        model2 = self.loader.load_model_to_vao(model2)
        static_model2 = TexturedModel(model2, ModelTexture(self.loader.load_texture("tree", "png")))
        texture2 = static_model2.texture
        texture2.shine_damper = 10
        texture2.reflectivity = 1

        model3 = OBJFileLoader.model_data("fern")
        model3 = self.loader.load_model_to_vao(model3)
        static_model3 = TexturedModel(model3, ModelTexture(self.loader.load_texture("fern", "png")))
        texture3 = static_model3.texture
        texture3.shine_damper = 10
        texture3.reflectivity = 0.25
        texture3.has_transparency = True
        texture3.use_fake_lighting = True

        model4 = OBJFileLoader.model_data("grassModel")
        model4 = self.loader.load_model_to_vao(model4)
        static_model4 = TexturedModel(model4, ModelTexture(self.loader.load_texture("flower", "png")))
        texture4 = static_model4.texture
        texture4.shine_damper = 10
        texture4.reflectivity = 0
        texture4.has_transparency = True
        texture4.use_fake_lighting = True

        model5 = OBJFileLoader.model_data("grassModel")
        model5 = self.loader.load_model_to_vao(model5)
        static_model5 = TexturedModel(model5, ModelTexture(self.loader.load_texture("grassTexture", "png")))
        texture5 = static_model5.texture
        texture5.shine_damper = 10
        texture5.reflectivity = 0
        texture5.has_transparency = True
        texture5.use_fake_lighting = True

        self.entities.append(Entity(static_model, [0, 0, -15], 0, 180, 0, 1))
        self.entities.append(Entity(static_model1, [10, 2, -15], 0, 20, 0, 2))
        self.entities.append(Entity(static_model1, [7, .5, -15], 0, 0, 0, .5))
        self.entities.append(Entity(static_model1, [12, 1, -11], 0, 0, 0, 1))
        self.entities.append(Entity(static_model2, [-8.5, 0, -14], 0, 0, 0, 6))
        self.entities.append(Entity(static_model3, [-8.5, -.5, -14], 0, 0, 0, .75))
        self.entities.append(Entity(static_model4, [0, 0, -10], 0, 90, 0, 1))
        self.entities.append(Entity(static_model5, [0, 0, -10], 0, 0, 0, 1))

        # Terrain texture stuff
        background_texture = TerrainTexture(self.loader.load_texture("grassy", "png"))
        r_texture = TerrainTexture(self.loader.load_texture("mud", "png"))
        g_texture = TerrainTexture(self.loader.load_texture("grassFlowers", "png"))
        b_texture = TerrainTexture(self.loader.load_texture("path", "png"))

        texture_pack = TerrainTexturePack(background_texture, r_texture, g_texture, b_texture)

        blend_map = TerrainTexture(self.loader.load_texture("blendmap", "png"))

        self.terrains.append(Terrain(0.5, 0, self.loader, texture_pack, blend_map))

    def load_scene_entities(self):
        return self.entities

    def load_scene_terrains(self):
        return self.terrains
