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
        if self.entities.get(entity.model) is not None:
            self.entities.get(entity.model).append(entity)
        else:
            self.entities.update({entity.model: [entity]})

    def clean_up(self):
        self.shader.clean_up()
