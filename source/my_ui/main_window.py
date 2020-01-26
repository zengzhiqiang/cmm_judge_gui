# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 my_ui code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.start_menu = QtWidgets.QMenu(self.menubar)
        self.start_menu.setObjectName("start_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.cmm_judge_action = QtWidgets.QAction(MainWindow)
        self.cmm_judge_action.setObjectName("cmm_judge_action")
        self.calculate_slog_action = QtWidgets.QAction(MainWindow)
        self.calculate_slog_action.setObjectName("calculate_slog_action")
        self.calculate_slog_k_action = QtWidgets.QAction(MainWindow)
        self.calculate_slog_k_action.setObjectName("calculate_slog_k_action")
        self.start_menu.addAction(self.cmm_judge_action)
        self.start_menu.addAction(self.calculate_slog_action)
        self.start_menu.addAction(self.calculate_slog_k_action)
        self.menubar.addAction(self.start_menu.menuAction())

        self.retranslateUi(MainWindow)
        self.cmm_judge_action.triggered.connect(MainWindow.open_cmm_judge_window)
        self.calculate_slog_action.triggered.connect(MainWindow.open_calculate_slog_window)
        self.calculate_slog_k_action.triggered.connect(MainWindow.open_calculate_slog_k_window)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_menu.setTitle(_translate("MainWindow", "开始"))
        self.cmm_judge_action.setText(_translate("MainWindow", "三坐标检查"))
        self.calculate_slog_action.setText(_translate("MainWindow", "计算Slog"))
        self.calculate_slog_k_action.setText(_translate("MainWindow", "calculate_slog_k"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
