class ModelTexture:
    def __init__(self, texture_id):
        self._texture_id = texture_id

    @property
    def texture_id(self) -> int:
        return self._texture_id
