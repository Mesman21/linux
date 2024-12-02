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
        self.setWindowTitle("Заміна значень у стеку")

        self.layout = QVBoxLayout()

        self.result_label = QLabel("Сформований стек:")
        self.layout.addWidget(self.result_label)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout.addWidget(self.text_edit)

        self.process_btn = QPushButton("Сформувати стек і замінити значення")
        self.process_btn.clicked.connect(self.process_stack)
        self.layout.addWidget(self.process_btn)

        self.setLayout(self.layout)

    def process_stack(self) -> None:
        stack = deque(random.randint(-20, 20) for _ in range(10))

        self.text_edit.append(f"Початковий стек: {list(stack)}")

        for i in range(len(stack)):
            if stack[i] > 0:
                stack[i] = 1
            elif stack[i] < 0:
                stack[i] = -1

        self.text_edit.append(f"Змінений стек: {list(stack)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
