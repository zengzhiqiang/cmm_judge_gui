from .my_ui.sheet_err import Ui_Form
from PyQt5.Qt import *
import sys

class SheetErrWidget(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sheet_err_widget = SheetErrWidget()
    sheet_err_widget.show()
    sys.exit(app.exec_())
