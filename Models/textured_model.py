class TexturedModel:
    def __init__(self, model, texture):
        self._raw_model = model
        self._texture = texture

    @property
    def raw_model(self):
        return self._raw_model

    @property
    def texture(self):
        return self._texture
