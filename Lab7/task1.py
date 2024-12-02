import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QMessageBox,
)


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Пошук максимальних значень у групах по 5")

        self.layout = QVBoxLayout()

        self.file_label = QLabel("Виберіть файл з числами:")
        self.layout.addWidget(self.file_label)

        self.result_label = QLabel("Максимальні значення будуть записані у файл g.txt")
        self.layout.addWidget(self.result_label)

        self.process_btn = QPushButton("Вибрати файл і знайти максимуми")
        self.process_btn.clicked.connect(self.select_file)
        self.layout.addWidget(self.process_btn)

        self.setLayout(self.layout)

    def select_file(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Виберіть файл", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            self.find_max_in_groups(file_path)
        else:
            QMessageBox.warning(self, "Помилка", "Файл не вибрано!")

    def find_max_in_groups(self, file_path: str) -> None:
        try:
            with open(file_path, "r") as f:
                numbers = list(map(int, f.read().split()))

            output = []
            for i in range(0, len(numbers), 5):
                group = numbers[i : i + 5]
                output.append(max(group))

            with open("g.txt", "w") as g:
                g.write(" ".join(map(str, output)))

            self.result_label.setText(f"Результати записано у файл g.txt: {output}")
        except Exception as e:
            QMessageBox.warning(self, "Помилка", f"Виникла помилка: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())