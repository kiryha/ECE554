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

        # Test flow control
        self.test_started = False
        self.test_name = None

        self.init_ui()

        # UI calls
        self.btnStartLesson.pressed.connect(self.start_lesson)
        self.btnStartTest.pressed.connect(self.start_test)

    def check_user_input(self, user_text):
        """
        Paint green correct keys, red - incorrect
        """

        colored_string = ""

        for correct_character, user_character in zip(self.sequence_text, user_text):
            # Correct characters
            if correct_character == user_character:
                colored_string += f"<font color='green'>{user_character}</font>"
            # Incorrect characters
            else:
                colored_string += f"<font color='red'>{user_character}</font>"

        # Preserve the rest of the original string after the user's input
        colored_string += self.sequence_text[len(user_text):]

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

        if self.lesson_started:
            string = 'LESSON'
        else:
            string = 'TEST'

        self.labTasks.setText(f'{string} <font color="red">COMPLETE!</font>')

    def start_sequence(self):
        """
        Display sequence of strings for current lesson
        """
        if self.lesson_started:
            self.sequence_text = self.lessons_data[self.lesson_name]['sequences'][self.current_sequence]
        else:
            self.sequence_text = self.tests_data[self.test_name]['sequences'][self.current_sequence]

        self.labTasks.setText(self.sequence_text)

        pixmap = f'{root}/data/images/{self.sequence_text[self.current_string].upper()}.png'
        self.labPictures.setPixmap(pixmap)

        self.current_string = 1
        self.string_length = len(self.sequence_text)

    def init_ui(self):

        # Load keyboard
        pixmap = QtGui.QPixmap(self.keyboard_blank)
        self.labPictures.setPixmap(pixmap)

        # Load lessons and tests
        with open(self.lessons, 'r') as file_content:
            self.lessons_data = json.load(file_content)

        with open(self.tests, 'r') as file_content:
            self.tests_data = json.load(file_content)

        self.comLessons.addItems(self.lessons_data.keys())
        self.comTests.addItems(self.tests_data.keys())

    # Flow control
    def keyPressEvent(self, event):
        """
        Lesson Flow control
        """

        if self.lesson_started or self.test_started:

            # Check if it was a correct key
            task_letter = self.sequence_text[self.current_string - 1]
            pressed_letter = chr(event.key())
            self.user_input += pressed_letter
            self.check_user_input(self.user_input)

            if self.current_string == self.string_length:
                if self.number_of_sequences == self.current_sequence + 1:
                    # End of lesson
                    self.reset_ui()
                    self.lesson_started = False
                    self.test_started = False
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

    # UI calls
    def start_lesson(self):

        self.lesson_name = self.comLessons.currentText()

        self.number_of_sequences = len(self.lessons_data[self.lesson_name]['sequences'])
        self.user_input = ''
        self.current_sequence = 0
        self.current_string = 0
        self.lesson_started = True
        self.start_sequence()

        self.labPictures.setFocus()  # Allow application to catch SPACE key

    def start_test(self):

        self.test_name = self.comTests.currentText()
        self.number_of_sequences = len(self.tests_data[self.test_name]['sequences'])
        self.user_input = ''
        self.current_sequence = 0
        self.current_string = 0
        self.test_started = True
        self.start_sequence()

        self.labPictures.setFocus()  # Allow application to catch SPACE key


if __name__ == "__main__":

    root = os.path.dirname(os.path.abspath(__file__))
    app = QtWidgets.QApplication([])
    touch_type = TouchType()
    # split_smart.setWindowIcon(QtGui.QIcon('{0}/icons/split_smart.ico'.format(root)))
    touch_type.show()
    app.exec_()
