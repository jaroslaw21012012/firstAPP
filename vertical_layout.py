from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys






class App(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("    Vertical Layout    ")
        self.setGeometry(0, 0, 400, 400)
        self.setMinimumSize(400, 400)
        self.setMaximumSize(400, 400)

        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)

        self.button1 = QPushButton("PLACEHOLDER HERE")
        self.button2 = QPushButton("PLACEHOLDER HERE")
        self.button3 = QPushButton("PLACEHOLDER HERE")
        self.button4 = QPushButton("PLACEHOLDER HERE")
        self.button5 = QPushButton("PLACEHOLDER HERE")
        self.vertical_layout.addWidget(self.button1)
        self.vertical_layout.addWidget(self.button2)
        self.vertical_layout.addWidget(self.button3)
        self.vertical_layout.addWidget(self.button4)
        self.vertical_layout.addWidget(self.button5)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()