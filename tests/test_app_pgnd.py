import random
import sys

from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.hello: list[str] = ["Hello World", "Hola mundo", "Bruh"]

        self.button: QtWidgets.QPushButton = QtWidgets.QPushButton("Click me!")
        self.text: QtWidgets.QLabel = QtWidgets.QLabel(
            "Click button to start", alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.text)
        self.main_layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self) -> None:
        self.text.setText(random.choice(self.hello))


app: QtWidgets.QApplication = QtWidgets.QApplication([])

widget: MyWidget = MyWidget()
widget.resize(800, 600)
widget.show()

sys.exit(app.exec())
