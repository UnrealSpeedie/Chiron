class TerrainTexturePack:
    def __init__(self, background_texture, r_texture, g_texture, b_texture):
        self._background_texture = background_texture
        self._r_texture = r_texture
        self._g_texture = g_texture
        self._b_texture = b_texture

    @property
    def background_texture(self):
        return self._background_texture

    @property
    def r_texture(self):
        return self._r_texture

    @property
    def g_texture(self):
        return self._g_texture

    @property
    def b_texture(self):
        return self._b_texture
