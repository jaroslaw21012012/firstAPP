from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout
import sys



class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 600, 250)
        self.setMinimumSize(600, 250)
        self.setMaximumSize(600, 250)
        self.setWindowTitle("             task1_layout          ")
        self.horizontal_layout = QHBoxLayout()
        self.setLayout(self.horizontal_layout)

        self.button1 = QPushButton("Place")
        self.vertical_layout = QVBoxLayout()
        self.button2 = QPushButton("Place")

        self.button3 = QPushButton("Holder")
        self.button4 = QPushButton("Holder")
        self.button5 = QPushButton("Holder")

        self.horizontal_layout.addWidget(self.button1)
        self.horizontal_layout.addLayout(self.vertical_layout)
        self.horizontal_layout.addWidget(self.button2)
        self.vertical_layout.addWidget(self.button3)
        self.vertical_layout.addWidget(self.button4)
        self.vertical_layout.addWidget(self.button5)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()