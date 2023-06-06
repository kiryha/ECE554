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
        font = QtGui.QFont('Free Range Hive')
        font.setPointSize(48)
        self.labTasks.setFont(font)
        self.labTasks.setText('SELECT LESSON AND PRESS "START LESSON"')

        # Data
        self.keyboard_blank = f'{root}/data/images/blank.png'
        self.keyboard_all = f'{root}/data/images/all.png'
        self.lessons = f'{root}/data/lessons.json'
        self.tests = f'{root}/data/tests.json'
        self.lessons_data = None
        self.tests_data = None

        # Lesson flow control
        self.lesson_started = False
        self.sequence_ended = False
        self.lesson_name = None
        self.sequence_text = None
        self.number_of_sequences = 0
        self.current_sequence = 0
        self.current_string = 0
        self.string_length = None
        self.user_input = ''

        self.init_ui()

        # UI signals
        self.btnStartLesson.pressed.connect(self.start_lesson)

    def check_user_input(self, user_text):

        # print(f'user_text {user_text}')

        # Build a new string that will include correct and incorrect characters
        colored_string = ""

        for correct_char, user_char in zip(self.sequence_text, user_text):
            # Correct characters will be painted in black
            if correct_char == user_char:
                colored_string += "<font color='green'>{}</font>".format(user_char)
            # Incorrect characters will be painted in red
            else:
                colored_string += "<font color='red'>{}</font>".format(user_char)

        # Preserve the rest of the original string after the user's input
        # print(f'self.sequence_text[len(user_text):] {self.sequence_text[len(user_text):]}')
        colored_string += self.sequence_text[len(user_text):]
        # print(f'colored_string = {colored_string}')

        # Update the label text
        self.labTasks.setText(colored_string)

    def set_next_picture(self):

        # print(f' self.sequence_text = { self.sequence_text}')
        # print(f' self.current_string = { self.current_string}')

        # Get pressed key
        if self.sequence_text[self.current_string] == ' ':
            key = 'space'
        else:
            key = self.sequence_text[self.current_string].upper()

        # Show next letter in UI
        pixmap = f'{root}/data/images/{key}.png'
        self.labPictures.setPixmap(pixmap)

    def reset_ui(self):

        pixmap = QtGui.QPixmap(self.keyboard_blank)
        self.labPictures.setPixmap(pixmap)
        self.labTasks.clear()
        self.labTasks.setText('LESSON COMPLETE!')

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

    def start_sequence(self):

        self.sequence_text = self.lessons_data[self.lesson_name]['sequences'][self.current_sequence]
        self.labTasks.setText(self.sequence_text)

        pixmap = f'{root}/data/images/{self.sequence_text[self.current_string].upper()}.png'
        self.labPictures.setPixmap(pixmap)

        self.current_string = 1
        self.string_length = len(self.sequence_text)

    def start_lesson(self):

        self.lesson_name = self.comLessons.currentText()

        self.number_of_sequences = len(self.lessons_data[self.lesson_name]['sequences'])
        self.user_input = ''
        self.current_sequence = 0
        self.current_string = 0
        self.start_sequence()
        self.lesson_started = True
        self.labPictures.setFocus()  # Allow application to catch SPACE key

    def keyPressEvent(self, event):
        """
        Lesson Flow control
        """

        if self.lesson_started:

            # Check if it was a correct key
            task_letter = self.sequence_text[self.current_string - 1]
            pressed_letter = chr(event.key())
            self.user_input += pressed_letter
            self.check_user_input(self.user_input)

            if self.current_string == self.string_length:
                if self.number_of_sequences == self.current_sequence + 1:
                    # End of lesson
                    self.lesson_started = False
                    self.reset_ui()
                    return

                # End of Sequence
                pixmap = QtGui.QPixmap(self.keyboard_all)
                self.labPictures.setPixmap(pixmap)
                if self.sequence_ended:
                    # Last letter of sequence
                    self.sequence_ended = False
                    self.user_input = ''
                    self.current_string = 0
                    self.current_sequence += 1
                    self.start_sequence()
                    return
                self.sequence_ended = True
                return

            self.set_next_picture()

            # Update string counter
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
    touch_type = TouchType()
    # split_smart.setWindowIcon(QtGui.QIcon('{0}/icons/split_smart.ico'.format(root)))
    touch_type.show()
    app.exec_()
