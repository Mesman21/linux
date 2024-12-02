import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton)


class StudentAuthorizationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Авторизація студента')
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Логін
        login_layout = QHBoxLayout()
        login_layout.addWidget(QLabel('Логін:'))
        self.login_input = QLineEdit()
        login_layout.addWidget(self.login_input)
        layout.addLayout(login_layout)

        # Пароль
        password_layout = QHBoxLayout()
        password_layout.addWidget(QLabel('Пароль:'))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(self.password_input)
        layout.addLayout(password_layout)

        # Кнопка входу
        login_btn = QPushButton('Вхід')
        login_btn.clicked.connect(self.check_authorization)
        layout.addWidget(login_btn)

        # Результат
        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

    def check_authorization(self):
        # Жорстко закодовані дані для прикладу
        correct_login = 'student'
        correct_password = '12345'

        login = self.login_input.text()
        password = self.password_input.text()

        if login == correct_login and password == correct_password:
            self.result_label.setText('Вхід успішний!')
            self.result_label.setStyleSheet('color: green')
        else:
            self.result_label.setText('Невірний логін або пароль')
            self.result_label.setStyleSheet('color: red')


def main():
    app = QApplication(sys.argv)
    window = StudentAuthorizationApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()