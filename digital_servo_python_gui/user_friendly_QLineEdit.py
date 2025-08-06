# -*- coding: utf-8 -*-
"""
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets


class user_friendly_QLineEdit(QtWidgets.QLineEdit):

    def __init__(self, text):
        super(user_friendly_QLineEdit, self).__init__(text)

        self.textChanged.connect(self.change_my_color)
        self.returnPressed.connect(self.reset_my_color)

        self.reset_my_color()

    def change_my_color(self):
        palette = QtGui.QPalette()
        palette.setColor(self.backgroundRole(), QtGui.QColor('black'))
        palette.setColor(self.foregroundRole(), QtGui.QColor('white'))
        self.setPalette(palette)

    def reset_my_color(self):
        palette = QtGui.QPalette()
        palette.setColor(self.backgroundRole(), QtGui.QColor('white'))
        palette.setColor(self.foregroundRole(), QtGui.QColor('black'))
        self.setPalette(palette)
