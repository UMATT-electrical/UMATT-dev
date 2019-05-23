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
    WHITE = ColourString('white')


_screen = QtGui.QDesktopWidget().screenGeometry()


class SCREEN:
    HEIGHT = _screen.height()
    WIDTH = _screen.width()


HEIGHT = SCREEN.HEIGHT
WIDTH = SCREEN.WIDTH


class Gear(Enum):
    NEUTRAL = 'N'
    HIGH = "H"
    LOW = "L"
    FORWARD = 'F'
    REVERSE = "R"
