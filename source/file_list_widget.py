from .my_ui.file_list import Ui_file_list
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import sys

class FileListWidget(QWidget, Ui_file_list):

    show_file_err_signal = pyqtSignal(str)

    def __init__(self,parent=None, *args, **kwargs):
        super().__init__(parent=None, *args, **kwargs)
        self.setupUi(self)

    def show_file_err(self):
        # print("展示报告中的错误！")
        self.show_file_err_signal.emit(self.file_name_btn.text())

    def set_file_name_btn(self, file_name):
        self.file_name_btn.setText(file_name)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    file_list_widget = FileListWidget()
    file_list_widget.set_file_name_btn("2020-01-02")
    file_list_widget.show()
    sys.exit(app.exec_())
