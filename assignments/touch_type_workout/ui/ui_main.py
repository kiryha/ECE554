# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TouchType(object):
    def setupUi(self, TouchType):
        if not TouchType.objectName():
            TouchType.setObjectName(u"TouchType")
        TouchType.resize(1135, 587)
        self.centralwidget = QWidget(TouchType)
        self.centralwidget.setObjectName(u"centralwidget")
        TouchType.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TouchType)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1135, 21))
        TouchType.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TouchType)
        self.statusbar.setObjectName(u"statusbar")
        TouchType.setStatusBar(self.statusbar)

        self.retranslateUi(TouchType)

        QMetaObject.connectSlotsByName(TouchType)
    # setupUi

    def retranslateUi(self, TouchType):
        TouchType.setWindowTitle(QCoreApplication.translate("TouchType", u"Touch Type Workout", None))
    # retranslateUi

