class ModelTexture:
    def __init__(self, texture_id):
        self._texture_id = texture_id
        self._shine_damper = 1
        self._reflectivity = 0
        self._has_transparency = False
        self._use_fake_lighting = False

    @property
    def has_transparency(self):
        return self._has_transparency

    @has_transparency.setter
    def has_transparency(self, value):
        self._has_transparency = value

    @property
    def use_fake_lighting(self):
        return self._use_fake_lighting

    @use_fake_lighting.setter
    def use_fake_lighting(self, value):
        self._use_fake_lighting = value

    @property
    def texture_id(self) -> int:
        return self._texture_id

    @property
    def shine_damper(self):
        return self._shine_damper

    @shine_damper.setter
    def shine_damper(self, value):
        self._shine_damper = value

    @property
    def reflectivity(self):
        return self._reflectivity

    @reflectivity.setter
    def reflectivity(self, value):
        self._reflectivity = value
