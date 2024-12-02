import sys
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
        self.setWindowTitle("Мін. і макс. у рядках матриці")

        self.layout = QVBoxLayout()

        self.input_label = QLabel(
            "Введіть матрицю (рядки через крапку з комою, елементи через кому):"
        )
        self.layout.addWidget(self.input_label)

        self.input_matrix = QTextEdit()
        self.layout.addWidget(self.input_matrix)

        self.result_label = QLabel("Результат:")
        self.layout.addWidget(self.result_label)

        self.swap_btn = QPushButton("Замінити мін. і макс.")
        self.swap_btn.clicked.connect(self.swap_min_max)
        self.layout.addWidget(self.swap_btn)

        self.setLayout(self.layout)

    def swap_min_max(self) -> None:
        matrix = [
            list(map(int, row.split(",")))
            for row in self.input_matrix.toPlainText().split(";")
        ]
        for i, row in enumerate(matrix):
            min_idx, max_idx = row.index(min(row)), row.index(max(row))
            row[min_idx], row[max_idx] = row[max_idx], row[min_idx]
        self.result_label.setText(f"Перетворена матриця: {matrix}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())