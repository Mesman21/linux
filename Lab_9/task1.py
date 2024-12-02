from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QRadioButton,
    QLineEdit,
    QPushButton,
    QMessageBox,
)
import sys


class MapStudentApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("mapStudent")

        self.students = {
            "Савчин": "ІПЗ-23",
            "Василик": "ІПЗ-21",
            "Данилів": "ІПЗ-21",
            "Гугляк": "ІПЗ-21",
            "Кальмюк": "ІПЗ-22",
            "Крутий": "ІПЗ-22",
            "Пристая": "ІПЗ-23",
            "Хорт": "ІПЗ-24",
            "Яблонський": "ІПЗ-24",
            "Федорко": "ІПЗ-24",
        }

        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)

        self.radioKey = QRadioButton("Пошук за прізвищем")
        self.radioValue = QRadioButton("Пошук за групою")
        self.radioKey.setChecked(True)

        self.searchField = QLineEdit(self)
        self.searchField.setPlaceholderText("Введіть значення для пошуку")

        self.resultField = QLineEdit(self)
        self.resultField.setReadOnly(True)

        self.searchButton = QPushButton("Шукати", self)
        self.searchButton.clicked.connect(self.search)

        self.addNameField = QLineEdit(self)
        self.addNameField.setPlaceholderText("Введіть прізвище для додавання")

        self.addGroupField = QLineEdit(self)
        self.addGroupField.setPlaceholderText("Введіть групу для додавання")

        self.addButton = QPushButton("Додати", self)
        self.addButton.clicked.connect(self.add_student)

        self.deleteNameField = QLineEdit(self)
        self.deleteNameField.setPlaceholderText("Введіть прізвище для видалення")

        self.deleteButton = QPushButton("Видалити", self)
        self.deleteButton.clicked.connect(self.delete_student)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.radioKey)
        self.layout.addWidget(self.radioValue)
        self.layout.addWidget(self.searchField)
        self.layout.addWidget(self.resultField)
        self.layout.addWidget(self.searchButton)
        self.layout.addWidget(self.addNameField)
        self.layout.addWidget(self.addGroupField)
        self.layout.addWidget(self.addButton)
        self.layout.addWidget(self.deleteNameField)
        self.layout.addWidget(self.deleteButton)

        self.display_students()
        self.setLayout(self.layout)

    def display_students(self) -> None:
        self.textEdit.clear()
        for student, group in self.students.items():
            self.textEdit.append(f"{student}: {group}")

    def search(self) -> None:
        query = self.searchField.text()
        if self.radioKey.isChecked():
            if query in self.students:
                self.resultField.setText(self.students[query])
            else:
                QMessageBox.warning(
                    self, "Увага", f"Студента з прізвищем '{query}' не знайдено."
                )
        else:
            result = [
                student for student, group in self.students.items() if group == query
            ]
            if result:
                self.resultField.setText(", ".join(result))
            else:
                QMessageBox.warning(
                    self, "Увага", f"Студентів з групи '{query}' не знайдено."
                )

    def add_student(self) -> None:
        name = self.addNameField.text()
        group = self.addGroupField.text()
        if name in self.students:
            QMessageBox.warning(
                self, "Увага", f"Студент з прізвищем '{name}' вже існує."
            )
        else:
            self.students[name] = group
            self.display_students()
            QMessageBox.information(
                self, "Успіх", f"Студента '{name}' додано до групи '{group}'."
            )

    def delete_student(self) -> None:
        name = self.deleteNameField.text()
        if name in self.students:
            group = self.students[name]
            del self.students[name]
            self.display_students()
            QMessageBox.information(
                self, "Успіх", f"Студента '{name}' з групи '{group}' видалено."
            )
        else:
            QMessageBox.warning(
                self, "Увага", f"Студента з прізвищем '{name}' не знайдено."
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapStudentApp()
    window.show()
    sys.exit(app.exec())
