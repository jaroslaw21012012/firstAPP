from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout, QLabel, QLineEdit







class Calculator(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("    Calculator      ")
        self.setGeometry(0, 0, 300, 250)
        self.setMinimumSize(300, 250)
        self.setMaximumSize(300, 250)

        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)


        self.horizontal_layout = QHBoxLayout()
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.first_number = QLineEdit()
        self.second_number = QLineEdit()

        self.horizontal_layout.addWidget(self.first_number)
        self.horizontal_layout.addWidget(self.second_number)



        self.buttons_layout = QGridLayout()
        self.vertical_layout.addLayout(self.buttons_layout)

        self.plus = QPushButton("+")
        self.minus = QPushButton("-")
        self.umnozhit = QPushButton("*")
        self.razdelit = QPushButton("/")

        self.buttons_layout.addWidget(self.plus, 0, 0)
        self.buttons_layout.addWidget(self.minus, 0, 1)
        self.buttons_layout.addWidget(self.umnozhit, 1, 0)
        self.buttons_layout.addWidget(self.razdelit, 1, 1)


        self.result = QLabel("Result Here")
        self.vertical_layout.addWidget(self.result)
        self.plus.clicked.connect(self.math_plus)
        self.minus.clicked.connect(self.math_minus)
        self.umnozhit.clicked.connect(self.math_umnozhit)
        self.razdelit.clicked.connect(self.math_razdelit)

    def math_plus(self):
        first = self.first_number.text()
        second = self.second_number.text()
        result = float(first) + float(second)
        self.result.setText(str(result))

    def math_minus(self):
        first = self.first_number.text()
        second = self.second_number.text()
        result = float(first) - float(second)
        self.result.setText(str(result))

    def math_umnozhit(self):
        first = self.first_number.text()
        second = self.second_number.text()
        result = float(first) * float(second)
        self.result.setText(str(result))

    def math_razdelit(self):
        first = self.first_number.text()
        second = self.second_number.text()
        result = float(first) / float(second)
        self.result.setText(str(result))




if __name__ == '__main__':
    app = QApplication([])
    window = Calculator()
    window.show()
    app.exec()