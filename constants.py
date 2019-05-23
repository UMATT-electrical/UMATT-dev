from enum import Enum
from PyQt4 import QtGui, QtCore


class ColourString(str):
    @property
    def background_string(self):
        return "background-color: %s" % self

    @property
    def colour_string(self):
        return "color: %s" % self


class RGBStrings(Enum):
    DARK_BROWN = ColourString('rgb(43,21,0)')
    GOLD = ColourString('rgb(255,184,0)')
    TRANSPARENT = ColourString('rgba(0,0,0,0%)')


def compass_text(incr, offset=0):
    all_vals = [idx*incr for idx in range(7)]
    return {cnt: (all_vals+all_vals)[idx+offset] for idx, cnt in enumerate(range(0, 359, 45))}

