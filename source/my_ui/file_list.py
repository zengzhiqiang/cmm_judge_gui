# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_list.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_file_list(object):
    def setupUi(self, file_list):
        file_list.setObjectName("file_list")
        file_list.resize(255, 50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(file_list.sizePolicy().hasHeightForWidth())
        file_list.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(file_list)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_name_btn = QtWidgets.QPushButton(file_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_name_btn.sizePolicy().hasHeightForWidth())
        self.file_name_btn.setSizePolicy(sizePolicy)
        self.file_name_btn.setMinimumSize(QtCore.QSize(150, 28))
        self.file_name_btn.setObjectName("file_name_btn")
        self.horizontalLayout.addWidget(self.file_name_btn)
        self.file_name_label = QtWidgets.QLabel(file_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_name_label.sizePolicy().hasHeightForWidth())
        self.file_name_label.setSizePolicy(sizePolicy)
        self.file_name_label.setMinimumSize(QtCore.QSize(20, 20))
        self.file_name_label.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.file_name_label.setText("")
        self.file_name_label.setObjectName("file_name_label")
        self.horizontalLayout.addWidget(self.file_name_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(file_list)
        self.file_name_btn.clicked.connect(file_list.show_file_err)
        QtCore.QMetaObject.connectSlotsByName(file_list)

    def retranslateUi(self, file_list):
        _translate = QtCore.QCoreApplication.translate
        file_list.setWindowTitle(_translate("file_list", "Form"))
        self.file_name_btn.setText(_translate("file_list", "filename"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    file_list = QtWidgets.QWidget()
    ui = Ui_file_list()
    ui.setupUi(file_list)
    file_list.show()
    sys.exit(app.exec_())
