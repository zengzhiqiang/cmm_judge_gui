
from .my_ui.main_window import Ui_MainWindow
from .cmm_judge_pane import CmmJudgePane
from PyQt5 import QtWidgets
from PyQt5.Qt import *
from cmm_judge_main import CmmJudgeView
import sys


class MainWindowPane(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.cmm_judge_pane = CmmJudgePane()
        self.cmm_judge_view = CmmJudgeView(self.cmm_judge_pane)
        self.setupUi(self)

    def open_cmm_judge_window(self):
        print("打开三坐标检查程序！")
        # self.cmm_judge_pane.show()
        self.cmm_judge_view.run_cmm_judge_main()

    def open_calculate_slog_window(self):
        print("打开Slog计算程序！")

    def open_calculate_slog_k_window(self):
        print("打开Slog和K值计算程序！")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window_pane = MainWindowPane()
    main_window_pane.show()
    sys.exit(app.exec_())
