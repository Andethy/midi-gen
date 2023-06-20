from constants import *


class KeySignature:
    def __init__(self, root: str, scale: str):
        self.root = root
        self.scale = scale
        self._root = TONICS_STR[root]
        self._scale = SCALES[scale]

    def get_relative_scale(self):
        return self._scale

    def get_key(self):
        return tuple(self._root + n for n in self._scale)
