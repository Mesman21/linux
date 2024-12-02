import sys
import random
from collections import deque
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
)


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Збільшення значень у черзі")

        self.layout = QVBoxLayout()

        self.result_label = QLabel("Сформована черга:")
        self.layout.addWidget(self.result_label)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout.addWidget(self.text_edit)

        self.process_btn = QPushButton("Сформувати чергу і збільшити значення")
        self.process_btn.clicked.connect(self.process_queue)
        self.layout.addWidget(self.process_btn)

        self.setLayout(self.layout)

    def process_queue(self) -> None:
        queue = deque(random.randint(1, 100) for _ in range(10))

        self.text_edit.append(f"Початкова черга: {list(queue)}")

        max_element = max(queue)
        self.text_edit.append(f"Максимальний елемент: {max_element}")

        for i in range(len(queue)):
            queue[i] += max_element

        self.text_edit.append(f"Змінена черга: {list(queue)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
