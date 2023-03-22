from interface import *
from dialog import *
from exit import *

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


from model import Model


class App:
    def __init__(self):
        Form, Window = uic.loadUiType("interface.ui")
        Form_Dialog, Dialog = uic.loadUiType("dialog.ui")
        Form_Exit, Exit = uic.loadUiType("exit.ui")
        Form_Edit, Edit = uic.loadUiType("edit.ui")

        app = QApplication([])

        self.model = Model()

        # Main Window
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)

        # Dialog Popup
        self.add_dialog = Dialog()
        self.form_add_dialog = Form_Dialog()
        self.form_add_dialog.setupUi(self.add_dialog)

        # Exit Popup
        self.exit = Exit()
        self.form_exit = Form_Exit()
        self.form_exit.setupUi(self.exit)

        # Edit Popup
        self.edit = Edit()
        self.form_edit = Form_Edit()
        self.form_edit.setupUi(self.edit)

        # for exit dialog to know which dialog to close
        self.current_dialog_window = ''

        self.window.show()

        # all button clickes configuration
        self.settings_configuration()

        app.exec_()



    def settings_configuration(self):
        # Main Window

        # передача параметров в функцию при нажатии на кнопку???
        self.form.add_button.clicked.connect(self.add_dialog.show)
        self.form.edit_button.clicked.connect(self.edit.show)



        # Dialog Window
        self.form_add_dialog.add_button.clicked.connect(self.show_dialog_info)
        self.form_add_dialog.back_button.clicked.connect(self.exit.show)
        self.form_add_dialog.class_box.addItems(self.model.get_classes()) # add items

        # Exit Window
        self.form_exit.yes_button.clicked.connect(self.exit.close)
        if self.current_dialog_window == 'add':
            self.form_exit.yes_button.clicked.connect(self.add_dialog.close)
        elif self.current_dialog_window == 'edit':
            self.form_exit.yes_button.clicked.connect(self.edit.close)
        self.form_exit.no_button.clicked.connect(self.exit.close)

        # Edit Window
        # self.form_dialog.add_button.clicked.connect()
        self.form_edit.back_button.clicked.connect(self.exit.show)


    def set_current_add_dialog(self):
        self.current_dialog_window = 'add'
    def set_current_edit_dialog(self):
        self.current_dialog_window = 'edit'

    def show_dialog_info(self):
        print(self.form_dialog.lineEdit.displayText())


if __name__ == '__main__':
    app = App()