"""

"""

import os
import time
import json
from PySide2 import QtWidgets, QtCore, QtGui
from ui import ui_main


class TouchType(QtWidgets.QMainWindow, ui_main.Ui_TouchType):
    def __init__(self):
        super(TouchType, self).__init__()
        self.setupUi(self)

        # Data
        self.keyboard_blank = f'{root}/data/images/blank.jpg'
        self.lessons = f'{root}/data/lessons.json'
        self.tests = f'{root}/data/tests.json'
        self.lessons_data = None
        self.tests_data = None

        # Flow
        self.lesson_started = False
        self.lesson_name = None
        self.sequence_text = None
        self.number_of_sequences = 0
        self.current_sequence = 0
        self.current_string = 0
        self.string_length = None

        self.init_ui()

        # UI signals
        self.btnStartLesson.pressed.connect(self.start_lesson)

    def reset_ui(self):

        pixmap = QtGui.QPixmap(self.keyboard_blank)
        self.labPictures.setPixmap(pixmap)
        self.linTask.clear()

    def init_ui(self):

        # Load keyboard
        pixmap = QtGui.QPixmap(self.keyboard_blank)
        # self.labPictures.setPixmap(pixmap.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.labPictures.setPixmap(pixmap)

        # Load lessons and tests
        with open(self.lessons, 'r') as file_content:
            self.lessons_data = json.load(file_content)

        with open(self.lessons, 'r') as file_content:
            self.tests_data = json.load(file_content)

        self.comLessons.addItems(self.lessons_data.keys())
        self.comTests.addItems(self.tests_data.keys())

    def init_sequence(self):

        # lesson = self.comLessons.currentText()
        self.sequence_text = self.lessons_data[self.lesson_name]['sequences'][self.current_sequence]
        self.linTask.setText(self.sequence_text)
        pixmap = f'{root}/data/images/{self.sequence_text[self.current_string].upper()}_blue.jpg'
        self.labPictures.setPixmap(pixmap)

        self.current_string = 1
        self.string_length = len(self.sequence_text)
        print(f'len = {self.string_length}')

    def init_lesson(self):

        self.sequence_text = self.lessons_data[self.lesson_name]['sequences'][self.current_sequence]
        self.linTask.setText(self.sequence_text)
        pixmap = f'{root}/data/images/{self.sequence_text[self.current_string].upper()}_blue.jpg'
        self.labPictures.setPixmap(pixmap)

        self.current_string = 1
        self.string_length = len(self.sequence_text)
        print(f'len = {self.string_length}')

    def start_lesson(self):

        self.lesson_name = self.comLessons.currentText()

        self.number_of_sequences = len(self.lessons_data[self.lesson_name]['sequences'])
        self.current_sequence = 0
        self.current_string = 0
        self.init_sequence()
        self.lesson_started = True

    def keyPressEvent(self, event):

        # if event.key() == QtCore.Qt.Key_A:
        #     keyboard_a = "C:/Users/kko8/OneDrive/projects/master/ECE554/assignments/project/src/pressed_a.jpg"
        #     pixmap = QtGui.QPixmap(keyboard_a)
        #     self.labPictures.setPixmap(pixmap)
        #     print('A key was pressed')
        #     self.trigger = 1
        # else:
        #     print(f'Key pressed: {event.key()}')

        if self.lesson_started:
            print('Lesson started')

            print(f'current sequence = {self.current_sequence}')
            # if self.number_of_sequences == self.current_sequence:
            #     print('LAST')

            print(f'current string = {self.current_string}')
            if self.current_string == self.string_length:
                if self.number_of_sequences == self.current_sequence + 1:
                    print('LAST')
                    self.lesson_started = False
                    self.reset_ui()
                    return

                print('End Sequence')
                self.current_string = 0
                self.current_sequence += 1
                self.init_sequence()
                return

            if self.sequence_text[self.current_string] == ' ':
                key = 'space'
            else:
                key = self.sequence_text[self.current_string].upper()

            pixmap = f'{root}/data/images/{key}_blue.jpg'
            self.labPictures.setPixmap(pixmap)

            self.current_string += 1

    def keyReleaseEvent(self, event):
        # # This method will be called every time a key is released
        # if event.key() == QtGui.Qt.Key_A:
        #     print('A key was released')
        # else:
        #     print(f'Key released: {event.key()}')

        # pixmap = QtGui.QPixmap(self.keyboard_blank)
        # self.labPictures.setPixmap(pixmap)
        pass


if __name__ == "__main__":

    root = os.path.dirname(os.path.abspath(__file__))
    app = QtWidgets.QApplication([])
    split_smart = TouchType()
    # split_smart.setWindowIcon(QtGui.QIcon('{0}/icons/split_smart.ico'.format(root)))
    split_smart.show()
    app.exec_()
