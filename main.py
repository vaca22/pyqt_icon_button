import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


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
        print("gaga")
        fname = QFileDialog.getOpenFileNames(self,"Open File","","Mp3 Files (*.mp3)")
        if fname:
            print(fname[0])


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
