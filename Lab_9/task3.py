from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
import sys


class ContactBookApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Телефонні книги")

        self.contacts1 = {}
        self.contacts2 = {}

        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)

        self.populateButton = QPushButton("Заповнити", self)
        self.populateButton.clicked.connect(self.populate_contacts)

        self.swapButton = QPushButton("Обміняти", self)
        self.swapButton.clicked.connect(self.swap_contacts)

        self.clearButton = QPushButton("Очистити", self)
        self.clearButton.clicked.connect(self.clear_contacts)

        self.updateButton = QPushButton("Оновити", self)
        self.updateButton.clicked.connect(self.update_contacts)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.populateButton)
        self.layout.addWidget(self.swapButton)
        self.layout.addWidget(self.clearButton)
        self.layout.addWidget(self.updateButton)

        self.setLayout(self.layout)

    def populate_contacts(self) -> None:
        self.contacts1 = {
            "Іванов": "123-456-789",
            "Петров": "987-654-321",
            "Сидоров": "555-555-555",
        }
        self.contacts2 = {
            "Кузнєцов": "111-222-333",
            "Смирнов": "444-555-666",
            "Попов": "777-888-999",
        }
        self.display_contacts()

    def swap_contacts(self) -> None:
        self.contacts1, self.contacts2 = self.contacts2, self.contacts1
        self.display_contacts()

    def clear_contacts(self) -> None:
        self.contacts1.clear()
        self.contacts2.clear()
        self.display_contacts()

    def update_contacts(self) -> None:
        self.contacts1.update({"Новий": "000-111-222", "Старий": "333-444-555"})
        self.contacts2.update({"Інший": "666-777-888"})

        if "Іванов" in self.contacts1:
            self.contacts1["Іванов"] = "999-999-999"
        self.display_contacts()

    def display_contacts(self) -> None:
        self.textEdit.clear()
        self.textEdit.append("Телефонна книга 1:")
        for name, number in self.contacts1.items():
            self.textEdit.append(f"{name}: {number}")
        self.textEdit.append("\nТелефонна книга 2:")
        for name, number in self.contacts2.items():
            self.textEdit.append(f"{name}: {number}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactBookApp()
    window.show()
    sys.exit(app.exec())
