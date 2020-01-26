from PyQt5.Qt import *
import sys
from source.data_err_widget import DataErrWidget

class TestWindow(QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setStyleSheet('background-color: red;')


class OtherWindow(QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = QLabel("XXX")
        self.label.setParent(self)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: green;")


def delete_widget(widget):
    widget.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ui = TestWindow()
    # other_window = OtherWindow()
    # # other_window.setParent(ui)
    # other_window.show()
    # ui.show()
    ui = QWidget()
    label1 = DataErrWidget()
    label2 = DataErrWidget()
    layout = QHBoxLayout()
    ui.setLayout(layout)
    layout.addWidget(label1)
    layout.addWidget(label2)
    # print(ui.children())
    for widget in ui.findChildren(DataErrWidget):
        widget.deleteLater()
    # delete_widget(label1)
    # delete_widget(label2)
    label3 = QPushButton("xxx")
    layout.addWidget(label3)
    label3.clicked.connect(lambda :print(ui.children()))
    # ui.show()
    print(ui.children())
    sys.exit(app.exec_())


