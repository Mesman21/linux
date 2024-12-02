import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
)


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Перетворення масиву")

        self.layout = QVBoxLayout()

        self.input_label = QLabel("Введіть масив через кому:")
        self.layout.addWidget(self.input_label)

        self.input_array = QLineEdit()
        self.layout.addWidget(self.input_array)

        self.result_label = QLabel("Результат:")
        self.layout.addWidget(self.result_label)

        self.transform_btn = QPushButton("Перетворити масив")
        self.transform_btn.clicked.connect(self.transform_array)
        self.layout.addWidget(self.transform_btn)

        self.setLayout(self.layout)

    def transform_array(self) -> None:
        array = list(map(int, self.input_array.text().split(",")))
        result = [
            (
                item
                if i == 0 or i == len(array) - 1
                else item + array[0] if item % 2 == 0 else item
            )
            for i, item in enumerate(array)
        ]
        self.result_label.setText(f"Перетворений масив: {result}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
