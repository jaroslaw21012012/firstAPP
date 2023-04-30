import random, string
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpinBox, QCheckBox, QMessageBox

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("       PASSWORD GENERATOR v0.1       ")
        self.setGeometry(0, 0, 300, 250)
        self.setMaximumSize(300, 250)
        self.setMinimumSize(300, 250)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.title_label = QLabel("PASSWORD GENERATOR")
        self.main_layout.addWidget(self.title_label)


        self.top_horizontal = QHBoxLayout()
        self.main_layout.addLayout(self.top_horizontal)

        self.length_label = QLabel("Password Lenght:")
        self.spinbox = QSpinBox()
        self.spinbox.setValue(8)
        self.spinbox.setRange(4, 35)
        self.top_horizontal.addWidget(self.length_label)
        self.top_horizontal.addWidget(self.spinbox)


        self.lower_letters = QCheckBox("Строчные буквы")
        self.lower_letters.setChecked(True)
        self.upper_letters = QCheckBox("Заглавные буквы")
        self.digital_symbols = QCheckBox("Числа")
        self.some_symbols = QCheckBox("Спец. Символы")

        self.main_layout.addWidget(self.lower_letters)
        self.main_layout.addWidget(self.upper_letters)
        self.main_layout.addWidget(self.digital_symbols)
        self.main_layout.addWidget(self.some_symbols)


        self.output_password_label = QLabel("")


        self.main_layout.addWidget(self.output_password_label)


        self.button_layout = QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)

        self.generate_btn = QPushButton("GENERATE")
        self.copy_btn = QPushButton("COPY")
        self.copy_btn.setEnabled(False)

        self.button_layout.addWidget(self.generate_btn)
        self.button_layout.addWidget(self.copy_btn)


        self.generate_btn.clicked.connect(self.generate_pass)
        self.copy_btn.clicked.connect(self.copy_pass)

    def generate_pass(self):
        chars = ''
        if self.lower_letters.isChecked():
            chars += string.ascii_lowercase
        if self.upper_letters.isChecked():
            chars += string.ascii_uppercase
        if self.digital_symbols.isChecked():
            chars += string.digits
        if self.some_symbols.isChecked():
            chars += string.punctuation
        length = self.spinbox.value()
        result = ''
        for i in range(length):
            result += random.choice(chars)
        self.output_password_label.setText(result)
        self.copy_btn.setEnabled(True)


    def copy_pass(self):
        password = self.output_password_label.text()
        QApplication.clipboard().setText(password)
        QMessageBox.information(self, "copy", "copied УСПЕШНО")





if __name__ == '__main__':
    app = QApplication([])
    window = PasswordGenerator()
    window.show()
    app.exec()