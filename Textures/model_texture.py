class ModelTexture:
    def __init__(self, texture_id):
        self._texture_id = texture_id
        self._shine_damper = 1
        self._reflectivity = 0

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
