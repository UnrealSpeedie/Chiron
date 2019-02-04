from Render_Engine.obj_loader import OBJLoader
from Models.textured_model import TexturedModel
from Textures.model_texture import ModelTexture
from Render_Engine.loader import Loader
from Entities.entity import Entity
from Terrain.terrain import Terrain


class Scene:
    def __init__(self):
        self.loader = Loader()
        self.entities = []
        self.terrains = []

    def scene1(self):
        model = OBJLoader.load_obj_model("stall", self.loader)
        static_model = TexturedModel(model, ModelTexture(self.loader.load_texture("stall_texture", "png")))
        texture = static_model.texture
        texture.shine_damper = 10
        texture.reflectivity = 1

        model1 = OBJLoader.load_obj_model("cube", self.loader)
        static_model1 = TexturedModel(model1, ModelTexture(self.loader.load_texture("cube_texture", "jpg")))
        texture1 = static_model1.texture
        texture1.shine_damper = 10
        texture1.reflectivity = 1

        model2 = OBJLoader.load_obj_model("tree", self.loader)
        static_model2 = TexturedModel(model2, ModelTexture(self.loader.load_texture("tree", "png")))
        texture2 = static_model2.texture
        texture2.shine_damper = 10
        texture2.reflectivity = 1

        model3 = OBJLoader.load_obj_model("fern", self.loader)
        static_model3 = TexturedModel(model3, ModelTexture(self.loader.load_texture("fern", "png")))
        texture3 = static_model3.texture
        texture3.shine_damper = 10
        texture3.reflectivity = 0.25
        texture3.has_transparency = True
        texture3.use_fake_lighting = True

        model4 = OBJLoader.load_obj_model("grassModel", self.loader)
        static_model4 = TexturedModel(model4, ModelTexture(self.loader.load_texture("flower", "png")))
        texture4 = static_model4.texture
        texture4.shine_damper = 10
        texture4.reflectivity = 0
        texture4.has_transparency = True
        texture4.use_fake_lighting = True

        model5 = OBJLoader.load_obj_model("grassModel", self.loader)
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

        self.terrains.append(Terrain(0.5, 0, self.loader, ModelTexture(self.loader.load_texture("grass", "png"))))

    def load_scene_entities(self):
        return self.entities

    def load_scene_terrains(self):
        return self.terrains
