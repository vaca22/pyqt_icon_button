import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fuck")

        self.setGeometry(100, 100, 600, 400)

        self.UiComponents()

        self.show()

    def UiComponents(self):
        button = QPushButton("Click", self)

        button.setGeometry(200, 150, 100, 30)

        button.clicked.connect(self.clickme)

        button.setIcon(QIcon('logo.png'))

    def clickme(self):
        print("press")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
