import sys
from PySide6.QtWidgets import QApplication
from app import CalendarApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec())