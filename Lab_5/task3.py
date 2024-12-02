import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QTextEdit,
)


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Суми парних і непарних стовпців")

        self.layout = QVBoxLayout()

        self.input_label = QLabel(
            "Введіть матрицю (рядки через крапку з комою, елементи через кому):"
        )
        self.layout.addWidget(self.input_label)

        self.input_matrix = QTextEdit()
        self.layout.addWidget(self.input_matrix)

        self.combo_label = QLabel("Оберіть тип стовпців:")
        self.layout.addWidget(self.combo_label)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["Парні стовпці", "Непарні стовпці"])
        self.layout.addWidget(self.combo_box)

        self.result_label = QLabel("Результат:")
        self.layout.addWidget(self.result_label)

        self.sum_btn = QPushButton("Обчислити суми")
        self.sum_btn.clicked.connect(self.sum_columns)
        self.layout.addWidget(self.sum_btn)

        self.setLayout(self.layout)

    def sum_columns(self) -> None:
        matrix = [
            list(map(int, row.split(",")))
            for row in self.input_matrix.toPlainText().split(";")
        ]

        selected_option = self.combo_box.currentText()

        if selected_option == "Парні стовпці":
            sum_columns = sum(
                [
                    row[i]
                    for row in matrix
                    for i in range(1, len(row), 2)
                    if i < len(row)
                ]
            )
            self.result_label.setText(f"Сума елементів парних стовпців: {sum_columns}")
        else:
            sum_columns = sum(
                [
                    row[i]
                    for row in matrix
                    for i in range(0, len(row), 2)
                    if i < len(row)
                ]
            )
            self.result_label.setText(
                f"Сума елементів непарних стовпців: {sum_columns}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
