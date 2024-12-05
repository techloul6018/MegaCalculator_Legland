import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QGridLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


class Dogs:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_info(self):
        return f"Name: {self.__name}, Age: {self.__age}"


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)
        self.initUI()
        self.dogs_list = []  

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        self.input_field = QLineEdit()
        self.input_field.setReadOnly(True)
        self.input_field.setStyleSheet("font-size: 20px;")
        layout.addWidget(self.input_field)

        grid_layout = QGridLayout()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row, col = 0, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.setStyleSheet("font-size: 20px;")
            btn.clicked.connect(self.on_button_click)
            grid_layout.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        special_buttons = [
            'Hello World',
            'Drop Text',
            'Create Dog',
            'My button'
        ]

        row = 4
        col = 0
        for button in special_buttons:
            btn = QPushButton(button)
            if button == "Hello World":
                btn.setStyleSheet("font-size: 20px;")
                btn.clicked.connect(self.on_button_click)
            elif button == "Drop Text":
                btn.setStyleSheet("font-size: 20px; color: white; background-color: red;")
                btn.clicked.connect(self.on_button_click)
            elif button == "Create Dog":
                btn.setStyleSheet("font-size: 20px; color: white; background-color: blue;")
                btn.clicked.connect(self.on_button_click)
            elif button == "My button":
                btn.setStyleSheet("font-size: 20px; background-color: orange;")
                btn.clicked.connect(self.open_youtube_link)
            grid_layout.addWidget(btn, row, col, 1, 4)
            row += 1

        layout.addLayout(grid_layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == "C" or text == "Drop Text":
            self.input_field.clear()

        elif text == "=":
            try:
                result = eval(self.input_field.text())
                self.input_field.setText(str(result))
            except Exception:
                self.input_field.setText("Error")

        elif text == "Create Dog":
            dog_names = ["Melki", "Buddy", "Bella", "Charlie", "Max", "Luna", "Rocky", "Milo", "Lucy", "Coco"]
            name = random.choice(dog_names)
            age = random.randint(1, 13)
            new_dog = Dogs(name, age)
            self.dogs_list.append(new_dog)
            self.input_field.setText(new_dog.get_info())

        else:
            self.input_field.setText(self.input_field.text() + text)

    def open_youtube_link(self):
        QDesktopServices.openUrl(QUrl("https://www.youtube.com/watch?v=q-Y0bnx6Ndw"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
