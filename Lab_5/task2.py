import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Парні та непарні елементи масиву")

        self.layout = QVBoxLayout()

        self.input_label = QLabel("Введіть масив через кому:")
        self.layout.addWidget(self.input_label)

        self.input_array = QLineEdit()
        self.layout.addWidget(self.input_array)

        self.result_label = QLabel("Результат:")
        self.layout.addWidget(self.result_label)

        self.show_btn = QPushButton("Показати парні та непарні")
        self.show_btn.clicked.connect(self.show_even_odd)
        self.layout.addWidget(self.show_btn)

        self.setLayout(self.layout)

    def show_even_odd(self) -> None:
        array = list(map(int, self.input_array.text().split(',')))
        even = [x for x in array if x % 2 == 0]
        odd = [x for x in array if x % 2 != 0]
        self.result_label.setText(f"Парні: {even}, Непарні: {odd}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
