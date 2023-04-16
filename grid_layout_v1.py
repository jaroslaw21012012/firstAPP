from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("                 grid_layout VERSION:1        ")
        self.setGeometry(0, 0, 400, 400)
        self.setMinimumSize(400, 400)
        self.setMaximumSize(400, 400)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.button1 = QPushButton("PLACE")
        self.button2 = QPushButton("PLACE")
        self.button3 = QPushButton("PLACE")
        self.button4 = QPushButton("PLACE")
        self.button5 = QPushButton("PLACE")
        self.button6 = QPushButton("PLACE")
        self.button7 = QPushButton("PLACE")
        self.button8 = QPushButton("PLACE")
        self.button9 = QPushButton("PLACE")

        self.grid_layout.addWidget(self.button1, 0, 0)
        self.grid_layout.addWidget(self.button2, 0, 1)
        self.grid_layout.addWidget(self.button3, 0, 2)
        self.grid_layout.addWidget(self.button4, 1, 0)
        self.grid_layout.addWidget(self.button5, 1, 1)
        self.grid_layout.addWidget(self.button6, 1, 2)
        self.grid_layout.addWidget(self.button7, 2, 0)
        self.grid_layout.addWidget(self.button8, 2, 1)
        self.grid_layout.addWidget(self.button9, 2, 2)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()