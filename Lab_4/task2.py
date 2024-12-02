import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QLabel, QLineEdit, QPushButton, QMessageBox)


class NumberProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Перевірка впорядкування чисел')
        self.setGeometry(100, 100, 300, 250)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Введення чисел
        self.x_input = QLineEdit()
        self.y_input = QLineEdit()
        self.z_input = QLineEdit()

        layout.addWidget(QLabel('Введіть X:'))
        layout.addWidget(self.x_input)
        layout.addWidget(QLabel('Введіть Y:'))
        layout.addWidget(self.y_input)
        layout.addWidget(QLabel('Введіть Z:'))
        layout.addWidget(self.z_input)

        # Кнопка обробки
        process_btn = QPushButton('Обробити')
        process_btn.clicked.connect(self.process_numbers)
        layout.addWidget(process_btn)

        # Результат
        self.result_label = QLabel('Результат: ')
        layout.addWidget(self.result_label)

    def process_numbers(self):
        try:
            x = float(self.x_input.text())
            y = float(self.y_input.text())
            z = float(self.z_input.text())

            original_values = [x, y, z]
            modified_values = original_values.copy()

            # Перевірка впорядкованості
            if x <= y <= z or x >= y >= z:
                # Подвоєння чисел
                modified_values = [val * 2 for val in modified_values]
                description = "Числа впорядковані. Виконане подвоєння."
            else:
                # Зміна на протилежні
                modified_values = [-val for val in modified_values]
                description = "Числа не впорядковані. Змінені на протилежні."

            result_text = (
                f"Результат:\n"
                f"Оригінальні числа: {original_values}\n"
                f"Змінені числа: {modified_values}\n"
                f"{description}"
            )

            self.result_label.setText(result_text)

        except ValueError:
            QMessageBox.warning(self, 'Помилка', 'Введіть коректні числові значення')


def main():
    app = QApplication(sys.argv)
    window = NumberProcessingApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()