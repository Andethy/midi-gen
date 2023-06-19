from constants import *


class Key:
    def __init__(self, root: str, scale: str):
        self.root = root
        self.scale = scale
        self._root = TONICS_STR[root]
        self._scale = SCALES[scale]
