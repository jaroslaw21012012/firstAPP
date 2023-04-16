from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys



class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 400, 400)
        self.setMinimumSize(400, 400)
        self.setMaximumSize(400, 400)
        self.setWindowTitle("             horizontal_layout          ")
        self.horizontal_layout = QHBoxLayout()
        self.setLayout(self.horizontal_layout)
        self.button1 = QPushButton("PLACEHOLDER HERE")
        self.button2 = QPushButton("PLACEHOLDER HERE")
        self.button3 = QPushButton("PLACEHOLDER HERE")
        self.horizontal_layout.addWidget(self.button1)
        self.horizontal_layout.addWidget(self.button2)
        self.horizontal_layout.addWidget(self.button3)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()