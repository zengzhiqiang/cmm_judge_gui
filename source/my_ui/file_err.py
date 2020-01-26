# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_err.ui'
#
# Created by: PyQt5 my_ui code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.file_name_label = QtWidgets.QLabel(Form)
        self.file_name_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.file_name_label.setText("")
        self.file_name_label.setObjectName("file_name_label")
        self.verticalLayout.addWidget(self.file_name_label)
        self.sheet_err_widget = QtWidgets.QWidget(Form)
        self.sheet_err_widget.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.sheet_err_widget.setObjectName("sheet_err_widget")
        self.verticalLayout.addWidget(self.sheet_err_widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
