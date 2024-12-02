import sys
import random
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton


class Task2(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Завдання 2: Сортування списку за спаданням")
        self.setGeometry(300, 300, 300, 150)

        self.layout = QVBoxLayout()

        self.array_label = QLabel("Згенерований список: ")
        self.result_label = QLabel("Відсортований список: ")
        self.run_button = QPushButton("Відсортувати список")

        self.layout.addWidget(self.array_label)
        self.layout.addWidget(self.run_button)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)
        self.run_button.clicked.connect(self.sort_list)

        # Генерація випадкового списку
        self.numbers = [random.randint(1, 100) for _ in range(15)]
        self.array_label.setText(f"Згенерований список: {self.numbers}")

    def sort_list(self) -> None:
        self.numbers.sort(reverse=True)
        self.result_label.setText(f"Відсортований список: {self.numbers}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    task2_window = Task2()
    task2_window.show()
    sys.exit(app.exec())
