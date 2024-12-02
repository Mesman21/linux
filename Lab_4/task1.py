import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)


class NumberDescriptionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Опис числа')
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Введення числа
        input_layout = QHBoxLayout()
        self.number_input = QLineEdit()
        input_layout.addWidget(QLabel('Введіть число (-999 до 999):'))
        input_layout.addWidget(self.number_input)
        layout.addLayout(input_layout)

        # Кнопка аналізу
        analyze_btn = QPushButton('Аналізувати')
        analyze_btn.clicked.connect(self.analyze_number)
        layout.addWidget(analyze_btn)

        # Результат
        self.result_label = QLabel('Результат: ')
        layout.addWidget(self.result_label)

    def analyze_number(self):
        try:
            number = int(self.number_input.text())

            if number < -999 or number > 999:
                raise ValueError("Число поза допустимим діапазоном")

            if number == 0:
                description = "нульове число"
            elif number < 0:
                if -10 <= number < 0:
                    description = f"негативне однозначне число ({number})"
                elif -100 <= number < -10:
                    description = f"негативне двозначне число ({number})"
                else:
                    description = f"негативне тризначне число ({number})"
            else:
                if 0 < number < 10:
                    description = f"позитивне однозначне число ({number})"
                elif 10 <= number < 100:
                    description = f"позитивне двозначне число ({number})"
                else:
                    description = f"позитивне тризначне число ({number})"

            self.result_label.setText(f'Результат: {description}')

        except ValueError as e:
            QMessageBox.warning(self, 'Помилка', str(e))


def main():
    app = QApplication(sys.argv)
    window = NumberDescriptionApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()