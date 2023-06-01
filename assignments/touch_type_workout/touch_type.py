"""

"""

import os
import time
from PySide2 import QtWidgets, QtCore, QtGui
from ui import ui_main


class TouchType(QtWidgets.QMainWindow, ui_main.Ui_TouchType):
    def __init__(self):
        super(TouchType, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":

    # root = os.path.dirname(os.path.abspath(__file__))
    app = QtWidgets.QApplication([])
    split_smart = TouchType()
    # split_smart.setWindowIcon(QtGui.QIcon('{0}/icons/split_smart.ico'.format(root)))
    split_smart.show()
    app.exec_()
    