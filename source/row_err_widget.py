from .my_ui.row_err import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import sys

class RowErrWidget(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent=None, *args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    row_err_widget = RowErrWidget("sheet1")
    row_err_widget.show()
    sys.exit(app.exec_())
