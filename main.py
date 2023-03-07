from interface import *
from dialog import *

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


class App:
    def __init__(self):
        Form, Window = uic.loadUiType("interface.ui")
        Form_d, Dialog = uic.loadUiType("dialog.ui")
        app = QApplication([])

        window = Window()
        form = Form()
        form.setupUi(window)

        self.dialog = Dialog()
        form_d = Form_d()
        form_d.setupUi(self.dialog)

        window.show()



        form.pushButton.clicked.connect(self.add)
        app.exec_()

    def add(self):
        self.dialog.show()

if __name__ == '__main__':
    app = App()