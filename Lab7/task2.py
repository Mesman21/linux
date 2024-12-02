import os
import tempfile
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
        self.setWindowTitle("Обмін вмістом файлів f1 і f2")

        self.layout = QVBoxLayout()

        self.result_label = QLabel("Результат:")
        self.layout.addWidget(self.result_label)

        self.swap_btn = QPushButton("Виберіть два файли для обміну")
        self.swap_btn.clicked.connect(self.select_files)
        self.layout.addWidget(self.swap_btn)

        self.setLayout(self.layout)

    def select_files(self) -> None:
        file1_path, _ = QFileDialog.getOpenFileName(
            self, "Виберіть перший файл", "", "Text Files (*.txt);;All Files (*)"
        )
        if file1_path:
            file2_path, _ = QFileDialog.getOpenFileName(
                self, "Виберіть другий файл", "", "Text Files (*.txt);;All Files (*)"
            )
            if file2_path:
                self.swap_files(file1_path, file2_path)
            else:
                QMessageBox.warning(self, "Помилка", "Другий файл не вибрано!")
        else:
            QMessageBox.warning(self, "Помилка", "Перший файл не вибрано!")

    def swap_files(self, file1: str, file2: str) -> None:
        try:
            with open(file1, "r") as f1, tempfile.NamedTemporaryFile(delete=False) as temp:
                temp.write(f1.read().encode())
                temp_file_name = temp.name

            with open(file1, "w") as f1, open(file2, "r") as f2:
                f1.write(f2.read())

            with open(file2, "w") as f2, open(temp_file_name, "r") as temp:
                f2.write(temp.read())

            os.remove(temp_file_name)

            self.result_label.setText("Файли успішно поміняні місцями!")
        except Exception as e:
            QMessageBox.warning(self, "Помилка", f"Виникла помилка: {str(e)}")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
