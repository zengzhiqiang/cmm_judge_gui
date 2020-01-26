from .my_ui.file_err import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import sys

class FileErrWidget(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    file_err_widget = FileErrWidget("2020-01-04")
    file_err_widget.show()
    sys.exit(app.exec_())
