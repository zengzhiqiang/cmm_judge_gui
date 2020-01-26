# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sheet_err.ui'
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
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sheet_name_label = QtWidgets.QLabel(self.widget)
        self.sheet_name_label.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.sheet_name_label.setText("")
        self.sheet_name_label.setObjectName("sheet_name_label")
        self.horizontalLayout.addWidget(self.sheet_name_label)
        self.sheet_name_err_label = QtWidgets.QLabel(self.widget)
        self.sheet_name_err_label.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.sheet_name_err_label.setText("")
        self.sheet_name_err_label.setObjectName("sheet_name_err_label")
        self.horizontalLayout.addWidget(self.sheet_name_err_label)
        self.verticalLayout.addWidget(self.widget)
        self.row_err_widget = QtWidgets.QWidget(Form)
        self.row_err_widget.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.row_err_widget.setObjectName("row_err_widget")
        self.verticalLayout.addWidget(self.row_err_widget)

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
