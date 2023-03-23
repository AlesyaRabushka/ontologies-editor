from interface import *
from dialog import *
from exit import *

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog



from model import Model


class App(QWidget):
    def __init__(self):
        app = QApplication([])
        super().__init__()

        Form, Window = uic.loadUiType("interface.ui")
        Form_Dialog, Dialog = uic.loadUiType("dialog.ui")
        Form_Exit, Exit = uic.loadUiType("exit.ui")
        Form_Edit, Edit = uic.loadUiType("edit.ui")



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
        self.form.open_file_button.clicked.connect(self.open_file)
        self.form.add_button.clicked.connect(self.add_dialog.open)
        self.form.edit_button.clicked.connect(self.edit.open)


        # Open File window



        # Add Dialog Window
        self.form_add_dialog.add_button.clicked.connect(self.show_dialog_info)
        self.form_add_dialog.back_button.clicked.connect(self.add_dialog.close)
        # self.form_add_dialog.back_button.clicked.connect(self.exit.show)
        self.form_add_dialog.class_box.addItems(self.model.get_classes()) # to select one of the classes



        # Edit Window
        # self.form_dialog.add_button.clicked.connect()
        self.form_edit.back_button.clicked.connect(self.edit.close)
        # self.form_edit.back_button.clicked.connect(self.exit.show)





        # Exit Window
        self.form_exit.yes_button.clicked.connect(
            lambda checked, button=self.form_exit.yes_button: self._on_click_back(self.form_exit.yes_button, 'add',
                                                                                  self.add_dialog))
        # if self.current_dialog_window == 'add':
        #     print('here')
        #     self.form_exit.yes_button.clicked.connect(self.add_dialog.close)
        # elif self.current_dialog_window == 'edit':
        #     self.form_exit.yes_button.clicked.connect(self.edit.close)
        #     print('edit')
        self.form_exit.no_button.clicked.connect(self.exit.close)

    def open_file(self):
        # filename, ok = QFileDialog.getOpenFileName(
        #     self,
        #     "Select a File",
        #     "D:\Kyrs3\PBZ_6sem\ontologies-editor\Documents",
        #     "Text File (*.owl)"
        # )
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.file, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "D:\Kyrs3\PBZ_6sem\ontologies-editor\Documents", "Text Files (*.owl)", options=options)



    def _on_click_back(self, button, window_name, window):
        print(self.current_dialog_window)
        if window_name == 'add':
            button.clicked.connect(self.add_dialog.close)
            button.clicked.connect(button.close)



    def set_current_add_dialog(self):
        self.current_dialog_window = 'add'
        print('add')
    def set_current_edit_dialog(self):
        self.current_dialog_window = 'edit'
        print('edit')

    def show_dialog_info(self):
        print(self.form_dialog.lineEdit.displayText())


if __name__ == '__main__':
    app = App()