from PyQt4 import QtGui, QtCore
import compassWidget2 as CW


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
        back_text, point_text, size=(100, 100), angle=0, style_sheet='background-color: rgba(0,0,0,0%)'):
    compass = CW.CompassWidget()
    compass.setAngle(angle)
    compass.resize(*size)
    compass._backText = back_text
    compass._pointText = point_text
    compass.setStyleSheet(style_sheet)
    return compass


def make_label(
        parent,
        text,
        size=(100, 100),
        position=(100, 100),
        font=QtGui.QFont('Times', 90, QtGui.QFont.Bold),
        alignment=QtCore.Qt.AlignCenter,
        style_sheet='background-color: rgb(43,21,0); color: rgb(255,184,0)'
):
    label = QtGui.QLabel(text, parent)
    label.setStyleSheet(style_sheet)
    label.setFont(font)
    label.setAlignment(alignment)
    label.resize(*size)
    label.move(*position)
    return label
