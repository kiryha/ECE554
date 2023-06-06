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
        TouchType.resize(1060, 612)
        self.centralwidget = QWidget(TouchType)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_2 = QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.tab_1)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.comLessons = QComboBox(self.splitter)
        self.comLessons.setObjectName(u"comLessons")
        self.splitter.addWidget(self.comLessons)
        self.btnStartLesson = QPushButton(self.splitter)
        self.btnStartLesson.setObjectName(u"btnStartLesson")
        self.splitter.addWidget(self.btnStartLesson)
        self.line = QFrame(self.splitter)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.splitter.addWidget(self.line)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        self.splitter.addWidget(self.label_2)
        self.comTests = QComboBox(self.splitter)
        self.comTests.setObjectName(u"comTests")
        self.splitter.addWidget(self.comTests)
        self.btnStartTest = QPushButton(self.splitter)
        self.btnStartTest.setObjectName(u"btnStartTest")
        self.splitter.addWidget(self.btnStartTest)

        self.verticalLayout_2.addWidget(self.splitter)

        self.labTasks = QLabel(self.tab_1)
        self.labTasks.setObjectName(u"labTasks")

        self.verticalLayout_2.addWidget(self.labTasks)

        self.labPictures = QLabel(self.tab_1)
        self.labPictures.setObjectName(u"labPictures")

        self.verticalLayout_2.addWidget(self.labPictures)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        TouchType.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TouchType)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1060, 21))
        TouchType.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TouchType)
        self.statusbar.setObjectName(u"statusbar")
        TouchType.setStatusBar(self.statusbar)

        self.retranslateUi(TouchType)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TouchType)
    # setupUi

    def retranslateUi(self, TouchType):
        TouchType.setWindowTitle(QCoreApplication.translate("TouchType", u"Touch Type Workout", None))
        self.label.setText(QCoreApplication.translate("TouchType", u"Lessons: ", None))
        self.btnStartLesson.setText(QCoreApplication.translate("TouchType", u"Start Lesson", None))
        self.label_2.setText(QCoreApplication.translate("TouchType", u"Tests: ", None))
        self.btnStartTest.setText(QCoreApplication.translate("TouchType", u"Start Test", None))
        self.labTasks.setText(QCoreApplication.translate("TouchType", u"Select lesson adn press \"Satrt Lesson\"", None))
        self.labPictures.setText(QCoreApplication.translate("TouchType", u"PICTURES", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("TouchType", u"Lessons and Tests", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("TouchType", u"Statistics", None))
    # retranslateUi

