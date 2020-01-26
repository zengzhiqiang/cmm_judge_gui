# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_err.ui'
#
# Created by: PyQt5 my_ui code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.row_label = QtWidgets.QLabel(Form)
        self.row_label.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.row_label.setText("")
        self.row_label.setObjectName("row_label")
        self.horizontalLayout.addWidget(self.row_label)
        self.data_label = QtWidgets.QLabel(Form)
        self.data_label.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.data_label.setText("")
        self.data_label.setObjectName("data_label")
        self.horizontalLayout.addWidget(self.data_label)

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
