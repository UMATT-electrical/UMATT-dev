from PyQt4 import QtGui, QtCore
import compassWidget2 as CW


def make_pixmap(parent, relative_file, size, position=None):
    pixmap = QtGui.QPixmap(relative_file)
    pixmap = pixmap.scaled(*size)
    image_logo = QtGui.QLabel(parent)
    image_logo.setPixmap(pixmap)
    if position:
        image_logo.move(*position)
    return image_logo


def make_button(parent, label, font=None, size=None, position=None, style_sheet=None):
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
    label.setAlignment(alignment)
    if size:
        label.resize(*size)
    if position:
        label.move(*position)
    return label
