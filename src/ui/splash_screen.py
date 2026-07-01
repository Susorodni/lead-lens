from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QSplashScreen


class SpashScreen(QSplashScreen):

    def __init__(self):
        pixmap = QPixmap(500, 300)
        pixmap.fill(Qt.GlobalColor.darkBlue)

        super().__init__(pixmap)

        self.showMessage(
            "LeadLens",
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignCenter,
            Qt.GlobalColor.white,
        )
