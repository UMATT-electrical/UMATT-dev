from enum import Enum
from PyQt4 import QtGui, QtCore


class RGBStrings(Enum):
    DARK_BROWN = 'rgb(43,21,0)'
    GOLD = 'rgb(255,184,0)'
    TRANSPARENT = 'rgba(0,0,0,0%)'
    WHITE = 'white'
    BLACK = 'black'

    @property
    def background_string(self):
        return "background-color: %s" % self.value

    @property
    def colour_string(self):
        return "color: %s" % self.value


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
