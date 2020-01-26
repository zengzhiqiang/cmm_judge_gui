# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cmm_judge.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(892, 596)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_widget.sizePolicy().hasHeightForWidth())
        self.left_widget.setSizePolicy(sizePolicy)
        self.left_widget.setMinimumSize(QtCore.QSize(300, 0))
        self.left_widget.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.left_widget.setObjectName("left_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.left_top_widget = QtWidgets.QWidget(self.left_widget)
        self.left_top_widget.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.left_top_widget.setObjectName("left_top_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.left_top_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.open_folder_btn = QtWidgets.QPushButton(self.left_top_widget)
        self.open_folder_btn.setObjectName("open_folder_btn")
        self.gridLayout_2.addWidget(self.open_folder_btn, 1, 0, 1, 1)
        self.path_input_line_edit = QtWidgets.QLineEdit(self.left_top_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_input_line_edit.sizePolicy().hasHeightForWidth())
        self.path_input_line_edit.setSizePolicy(sizePolicy)
        self.path_input_line_edit.setObjectName("path_input_line_edit")
        self.gridLayout_2.addWidget(self.path_input_line_edit, 0, 0, 1, 2)
        self.start_check_btn = QtWidgets.QPushButton(self.left_top_widget)
        self.start_check_btn.setObjectName("start_check_btn")
        self.gridLayout_2.addWidget(self.start_check_btn, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.left_top_widget)
        self.left_mid_widget = QtWidgets.QWidget(self.left_widget)
        self.left_mid_widget.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.left_mid_widget.setObjectName("left_mid_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_mid_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.describe_label = QtWidgets.QLabel(self.left_mid_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.describe_label.sizePolicy().hasHeightForWidth())
        self.describe_label.setSizePolicy(sizePolicy)
        self.describe_label.setTextFormat(QtCore.Qt.PlainText)
        self.describe_label.setWordWrap(False)
        self.describe_label.setObjectName("describe_label")
        self.verticalLayout_2.addWidget(self.describe_label)
        self.path_label = QtWidgets.QLabel(self.left_mid_widget)
        self.path_label.setText("")
        self.path_label.setWordWrap(True)
        self.path_label.setObjectName("path_label")
        self.verticalLayout_2.addWidget(self.path_label)
        self.path_err_label = QtWidgets.QLabel(self.left_mid_widget)
        self.path_err_label.setText("")
        self.path_err_label.setWordWrap(True)
        self.path_err_label.setObjectName("path_err_label")
        self.verticalLayout_2.addWidget(self.path_err_label)
        self.verticalLayout.addWidget(self.left_mid_widget)
        self.left_bottom_widget = QtWidgets.QWidget(self.left_widget)
        self.left_bottom_widget.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.left_bottom_widget.setObjectName("left_bottom_widget")
        self.verticalLayout.addWidget(self.left_bottom_widget)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.left_widget)
        self.right_widget = QtWidgets.QWidget(Form)
        self.right_widget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.right_widget.setObjectName("right_widget")
        self.horizontalLayout.addWidget(self.right_widget)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)
        self.open_folder_btn.clicked.connect(Form.open_folder)
        self.start_check_btn.clicked.connect(Form.start_check)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "三坐标检查程序"))
        self.open_folder_btn.setText(_translate("Form", "选择文件夹"))
        self.start_check_btn.setText(_translate("Form", "开始"))
        self.describe_label.setText(_translate("Form", "文件夹路径为："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
