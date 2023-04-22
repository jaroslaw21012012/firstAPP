from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout, QLCDNumber, QProgressBar
import sys






class App(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("     TASK3       ")
        self.setGeometry(0, 0, 600, 300)
        self.setMinimumSize(600, 300)
        self.setMaximumSize(600, 300)

        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)


        self.horizontal_layout = QHBoxLayout()
        self.vertical_layout.addLayout(self.horizontal_layout)


        self.progressbar = QProgressBar()
        self.progressbar.setValue(99)
        self.vertical_layout.addWidget(self.progressbar)


        self.button1 = QPushButton("A")
        self.LCDNumber = QLCDNumber()
        self.button2 = QPushButton("B")

        self.grid_layout = QGridLayout()
        self.vertical_layout.addLayout(self.grid_layout)

        self.button3 = QPushButton("C")
        self.button4 = QPushButton("D")
        self.button5 = QPushButton("E")


        self.vertical_layout_two = QVBoxLayout()
        self.grid_layout.addLayout(self.vertical_layout_two, 1, 1)





        self.button6 = QPushButton("F")
        self.button7 = QPushButton("G")


        self.button8 = QPushButton("H")

        self.horizontal_layout.addWidget(self.button1)
        self.horizontal_layout.addWidget(self.LCDNumber)
        self.horizontal_layout.addWidget(self.button2)
        self.grid_layout.addWidget(self.button3, 0, 0)
        self.grid_layout.addWidget(self.button4, 0, 1)
        self.grid_layout.addWidget(self.button5, 1, 0)
        self.vertical_layout_two.addWidget(self.button6)
        self.vertical_layout_two.addWidget(self.button7)
        self.vertical_layout.addWidget(self.button8)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()