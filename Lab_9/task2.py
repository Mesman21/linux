from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QLabel,
)
import sys


class ShopItemsApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Товари в Магазинах")

        self.shops = {
            "магазин_1": {"хліб", "молоко", "цукерки"},
            "магазин_2": {"молоко", "цукерки", "сир"},
            "магазин_3": {"хліб", "цукерки", "сир"},
        }

        self.full_item_set = {"хліб", "молоко", "цукерки", "сир", "масло"}

        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)

        self.resultLabel = QLabel(self)

        self.checkButton = QPushButton("Перевірити Товари", self)
        self.checkButton.clicked.connect(self.check_items)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.resultLabel)
        self.layout.addWidget(self.checkButton)

        self.display_shops()
        self.setLayout(self.layout)

    def display_shops(self) -> None:
        self.textEdit.clear()
        for shop, items in self.shops.items():
            self.textEdit.append(f"{shop}: {', '.join(items)}")

    def check_items(self) -> None:
        common_items = self.full_item_set.copy()
        for items in self.shops.values():
            common_items &= items

        all_items = set()
        for items in self.shops.values():
            all_items |= items

        missing_items = self.full_item_set - all_items

        result_text = (
            f"Товари в кожному магазині: {', '.join(common_items)}\n"
            f"Товари хоча б в одному магазині: {', '.join(all_items)}\n"
            f"Товари, яких немає в жодному магазині: {', '.join(missing_items)}"
        )
        self.resultLabel.setText(result_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShopItemsApp()
    window.show()
    sys.exit(app.exec())
