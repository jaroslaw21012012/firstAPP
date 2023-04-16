from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("                 task2_layout             ")
        self.setGeometry(0, 0, 600, 300)
        self.setMinimumSize(600, 300)
        self.setMaximumSize(600, 300)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.button1 = QPushButton("Place")
        self.button2 = QPushButton("Place")
        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()

        self.button3 = QPushButton("A")
        self.button4 = QPushButton("A")
        self.button5 = QPushButton("A")
        self.button6 = QPushButton("B")
        self.button7 = QPushButton("B")
        self.button8 = QPushButton("B")


        self.grid_layout.addWidget(self.button1, 0, 0)
        self.grid_layout.addWidget(self.button2, 0, 1)
        self.grid_layout.addLayout(self.vertical_layout, 1, 0)
        self.grid_layout.addLayout(self.horizontal_layout, 1, 1)

        self.vertical_layout.addWidget(self.button3)
        self.vertical_layout.addWidget(self.button4)
        self.vertical_layout.addWidget(self.button5)
        self.horizontal_layout.addWidget(self.button6)
        self.horizontal_layout.addWidget(self.button7)
        self.horizontal_layout.addWidget(self.button8)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()