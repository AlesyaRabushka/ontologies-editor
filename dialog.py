# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Kyrs3\PBZ_6sem\ontologies-editor\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.add_button = QtWidgets.QPushButton(Dialog)
        self.add_button.setGeometry(QtCore.QRect(20, 260, 93, 28))
        self.add_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add_button.setObjectName("add_button")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 30, 161, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.class_box = QtWidgets.QComboBox(Dialog)
        self.class_box.setGeometry(QtCore.QRect(190, 90, 161, 22))
        self.class_box.setMouseTracking(False)
        self.class_box.setTabletTracking(False)
        self.class_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.class_box.setEditable(False)
        self.class_box.setFrame(True)
        self.class_box.setObjectName("class_box")
        self.back_button = QtWidgets.QPushButton(Dialog)
        self.back_button.setGeometry(QtCore.QRect(170, 260, 93, 28))
        self.back_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.back_button.setObjectName("back_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add_button.setText(_translate("Dialog", "Добавить"))
        self.label.setText(_translate("Dialog", "Название объекта"))
        self.label_2.setText(_translate("Dialog", "Название класса"))
        self.back_button.setText(_translate("Dialog", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
