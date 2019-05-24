from PyQt4 import QtGui, QtCore
import compassWidget2 as CW
from constants import RGBStrings


def make_pixmap(parent, relative_file, size, position=None, scale_to_fit=True):
    pixmap = QtGui.QPixmap(relative_file)
    if scale_to_fit:
        pixmap.scaledToWidth(size[0])
        pixmap.scaledToHeight(size[1])
    image_logo = QtGui.QLabel(parent)
    image_logo.setPixmap(pixmap)
    image_logo.resize(*size)
    if position:
        image_logo.move(*position)
    return image_logo


def make_button(parent, label, font=None, size=None, position=None, style_sheet=None, pixmap=None):
    if pixmap:
        button = QtGui.QPushButton(QtGui.QIcon(pixmap), label, parent=parent)
    else:
        button = QtGui.QPushButton(label, parent)
    if style_sheet:
        button.setStyleSheet(style_sheet)
    # nfont.setStyleSheet('background-color: rgb(255,184,0); color: rgb(')
    if font:
        button.setFont(font)
    if size:
        button.resize(*size)
    if position:
        button.move(*position)
    return button


def make_compass_widget(
        back_text, point_text, size=None, angle=None, style_sheet=None):
    compass = CW.CompassWidget()
    if angle:
        compass.setAngle(angle)
    else:
        compass.setAngle(45)
    if size:
        compass.resize(*size)
    compass._backText = back_text
    compass._pointText = point_text
    if style_sheet:
        compass.setStyleSheet(style_sheet)
    return compass


def make_label(
        parent,
        text,
        size=None,
        position=None,
        font=None,
        alignment=QtCore.Qt.AlignCenter,
        style_sheet=None,
        margin_size=None,
        margin_colour=None
):
    if margin_colour and margin_size:
        background_label = QtGui.QLabel('', parent)
        background_label.size(size[0]+margin_size, size[1]+margin_size)
        background_label.setStyleSheet(margin_colour)
        background_label.move(*position)
    label = QtGui.QLabel(text, parent)
    if style_sheet:
        label.setStyleSheet(style_sheet)
    if font:
        label.setFont(font)
    if alignment:
        label.setAlignment(alignment)
    if size:
        label.resize(*size)
    if position:
        label.move(*position)
    return label


class LabelWithImage:
    def __init__(self, parent, size, position, image_name, text, background_colour, font, text_colour, margin_width=5):
        smaller_size = (size[0]-2*margin_width, size[1]-2*margin_width)
        smaller_position = (position[0]+margin_width, position[1]+margin_width)

        image_size = (size[1]*.75, size[1]*.75)
        image_position = (smaller_position[0]*1.1, position[1]+(.5*size[1])-(.5*image_size[1]))

        text_size = (size[0]*.7, size[1]*.8)
        text_position = (position[0]+size[0]*.25, position[1]+(size[1]*.5) - (text_size[1]*.5))

        background_label = make_label(
            parent, '', size=size, position=position, alignment=None, style_sheet=background_colour)

        text_background = make_label(parent, '', smaller_size, smaller_position, style_sheet=RGBStrings.WHITE.background_string)

        image = make_pixmap(parent, image_name, image_size, image_position)

        text_label = make_label(
            parent, text, size=text_size, position=text_position, font=font, style_sheet=text_colour, )

        self.background = background_label
        self.text_background = text_background
        self.image = image
        self.text = text_label
