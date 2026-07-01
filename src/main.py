"""main.py"""
import sys
import time

from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.splash_screen import SpashScreen


def main():
    app: QApplication = QApplication(sys.argv)
    splash: SpashScreen = SpashScreen()
    splash.show()
    
    app.processEvents()
    
    # placeholder wait
    time.sleep(2)
    
    window: MainWindow = MainWindow()
    window.show()
    
    splash.finish(window)
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()