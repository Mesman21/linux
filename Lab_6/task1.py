import sys
import random
from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
)


class Task1(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Завдання 1: Видалення елементів з N по K")
        self.setGeometry(300, 300, 300, 150)

        self.layout = QVBoxLayout()

        self.array_label = QLabel("Згенерований список: ")
        self.range_label = QLabel("Введіть діапазон (N K) через пробіл:")
        self.input_line = QLineEdit()
        self.output_label = QLabel("Результат: ")
        self.run_button = QPushButton("Виконати")

        self.layout.addWidget(self.array_label)
        self.layout.addWidget(self.range_label)
        self.layout.addWidget(self.input_line)
        self.layout.addWidget(self.run_button)
        self.layout.addWidget(self.output_label)

        self.setLayout(self.layout)
        self.run_button.clicked.connect(self.process_list)

        # Генерація випадкового списку
        self.numbers = [random.randint(1, 100) for _ in range(20)]
        self.array_label.setText(f"Згенерований список: {self.numbers}")

    def process_list(self) -> None:
        try:
            n, k = map(int, self.input_line.text().split())
            if 0 <= n < len(self.numbers) and 0 <= k < len(self.numbers) and n <= k:
                del self.numbers[n : k + 1]
                self.output_label.setText(f"Список після видалення: {self.numbers}")
            else:
                self.output_label.setText("Невірний діапазон.")
        except Exception as e:
            self.output_label.setText(f"Помилка: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    task1_window = Task1()
    task1_window.show()
    sys.exit(app.exec())
