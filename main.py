from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()


    def UI(self):
        self.setWindowTitle("---------FirstApp------")
        self.setGeometry(100, 100, 400, 600)
        self.setMinimumSize(400, 600)
        self.setMaximumSize(400, 600)
        self.setStyleSheet("background:rgb(255, 255, 192) ;")

        button = QPushButton(":D Hello!", self)
        button.setGeometry(160, 260, 80, 30)
        button.setStyleSheet("border-radius: 10px;background: rgb(255, 255, 255);border: 2px solid rgb(0, 0, 0);")















if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())
