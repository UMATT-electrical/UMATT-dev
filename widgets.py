from PyQt4 import QtGui, QtCore


def make_button(
        label,
        parent,
        font=QtGui.QFont('Times', 20, QtGui.QFont.Bold),
        size=(100, 100),
        location=(100, 100),
        style_sheet='background-color: rgb(43,21,0); color: rgb(255,184,0)'):
    button = QtGui.QPushButton(label, parent)
    button.setStyleSheet(style_sheet)
    # nfont.setStyleSheet('background-color: rgb(255,184,0); color: rgb(')
    button.setFont(font)
    button.resize(*size)
    button.move(*location)
    return button
