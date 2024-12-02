import sys
import math
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QMessageBox,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from collections import deque


class Calculator(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setGeometry(500, 500, 300, 350)
        self.memory = 0
        self.stack = deque()

        self.lineEdit = QLineEdit(self)
        self.lineEdit_2 = QLineEdit(self)

        layout = QVBoxLayout()
        grid_layout = QGridLayout()

        self.lineEdit.setMaxLength(10)
        self.lineEdit.setAlignment(Qt.AlignRight)
        self.lineEdit.setFont(QFont("", 16))
        self.lineEdit_2.setAlignment(Qt.AlignRight)
        self.lineEdit_2.setFont(QFont("", 16))
        self.lineEdit_2.setEnabled(False)

        buttons = [
            ("7", 0, 0),
            ("8", 0, 1),
            ("9", 0, 2),
            ("/", 0, 3),
            ("4", 1, 0),
            ("5", 1, 1),
            ("6", 1, 2),
            ("*", 1, 3),
            ("1", 2, 0),
            ("2", 2, 1),
            ("3", 2, 2),
            ("-", 2, 3),
            ("0", 3, 0),
            (".", 3, 1),
            ("+", 3, 2),
            ("=", 3, 3),
            ("C", 4, 0),
            ("±", 4, 1),
            ("M+", 4, 2),
            ("M-", 4, 3),
            ("MC", 5, 0),
            ("MR", 5, 1),
            ("MS", 5, 2),
            ("⌫", 5, 3),
            ("cos", 6, 0),
            ("sin", 6, 1),
            ("tg", 6, 2),
            ("x²", 6, 3),
            ("√", 7, 0),
            ("1/x", 7, 1),
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
            grid_layout.addWidget(button, row, col)

        layout.addWidget(self.lineEdit)
        layout.addWidget(self.lineEdit_2)
        layout.addLayout(grid_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_button_click(self, char) -> None:
        try:
            if char.isdigit():
                self.lineEdit.insert(char)
            elif char in ["+", "-", "*", "/"]:
                self.calculate(char)
            elif char == "C":
                self.clear_all()
            elif char == "=":
                self.equals()
            elif char == ".":
                self.add_decimal()
            elif char == "±":
                self.change_sign()
            elif char == "M+":
                self.memory += float(self.lineEdit.text() or "0")
            elif char == "M-":
                self.memory -= float(self.lineEdit.text() or "0")
            elif char == "MR":
                self.lineEdit.setText(str(self.memory))
            elif char == "MC":
                self.memory = 0
            elif char == "MS":
                self.memory = float(
                    self.lineEdit.text() or "0"
                )
            elif char == "⌫":
                self.lineEdit.backspace()
            elif char == "cos":
                self.lineEdit.setText(
                    str(
                        round(
                            math.cos(math.radians(float(self.lineEdit.text() or "0"))),
                            6,
                        )
                    )
                )
            elif char == "sin":
                self.lineEdit.setText(
                    str(
                        round(
                            math.sin(math.radians(float(self.lineEdit.text() or "0"))),
                            6,
                        )
                    )
                )
            elif char == "tg":
                self.lineEdit.setText(
                    str(
                        round(
                            math.tan(math.radians(float(self.lineEdit.text() or "0"))),
                            6,
                        )
                    )
                )
            elif char == "x²":
                self.lineEdit.setText(str(float(self.lineEdit.text() or "0") ** 2))
            elif char == "√":
                self.lineEdit.setText(
                    str(math.sqrt(float(self.lineEdit.text() or "0")))
                )
            elif char == "1/x":
                self.lineEdit.setText(str(1 / float(self.lineEdit.text() or "0")))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def calculate(self, operator) -> None:
        if self.lineEdit.text():
            self.stack.append(self.lineEdit.text())
            self.stack.append(operator)
            self.lineEdit.clear()
            self.lineEdit_2.setText(" ".join(self.stack))

    def equals(self) -> None:
        try:
            if len(self.stack) == 2 and self.lineEdit.text():
                self.stack.append(self.lineEdit.text())
                val2 = float(self.stack.pop())
                operator = self.stack.pop()
                val1 = float(self.stack.pop())
                result = 0
                if operator == "+":
                    result = val1 + val2
                elif operator == "-":
                    result = val1 - val2
                elif operator == "*":
                    result = val1 * val2
                elif operator == "/":
                    result = val1 / val2 if val2 != 0 else val1
                expression = f"{val1} {operator} {val2} = {result}"
                self.lineEdit.setText(str(result))
                self.lineEdit_2.setText(expression)
                self.stack.clear()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def clear_all(self) -> None:
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.stack.clear()

    def add_decimal(self) -> None:
        if "." not in self.lineEdit.text():
            self.lineEdit.insert(".")

    def change_sign(self) -> None:
        text = self.lineEdit.text()
        if text.startswith("-"):
            self.lineEdit.setText(text[1:])
        else:
            self.lineEdit.setText("-" + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
