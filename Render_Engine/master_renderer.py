from Shaders.static_shader import StaticShader
from Render_Engine.renderer import Renderer


class MasterRenderer:
    def __init__(self):
        self.shader = StaticShader()
        self.renderer = Renderer(self.shader)
        self.entities = {}

    def render(self, sun, camera):
        self.renderer.prepare()
        self.shader.start()
        self.shader.load_light(sun)
        self.shader.load_view_matrix(camera)
        self.renderer.render(self.entities)
        self.shader.stop()
        self.entities.clear()

    def process_entity(self, entity):
        entity_model = entity.model
        batch = self.entities.get(entity_model)
        if batch is not None:
            batch.append(entity)
        else:
            new_batch = [entity]
            self.entities.update({entity_model: new_batch})

    def clean_up(self):
        self.shader.clean_up()
