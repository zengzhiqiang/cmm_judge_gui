import sys
sys.path.append('../')
from .my_ui.cmm_judge import Ui_Form
from PyQt5.Qt import *


class CmmJudgePane(QWidget, Ui_Form):

    get_path_signal = pyqtSignal(str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def open_folder(self):
        print("打开文件夹！")
        open_folder_dialog = QFileDialog.getExistingDirectory()
        self.path_input_line_edit.setText(open_folder_dialog)

    def start_check(self):
        # print("开始检查三坐标报告！")
        folder_path = self.path_input_line_edit.text()
        if len(folder_path):
            self.path_label.setText(folder_path)
            self.get_path_signal.emit(folder_path)
            self.path_input_line_edit.clear()
        else:
            msgbox = QMessageBox(self)
            msgbox.setText("路径不能为空！")
            msgbox.show()

    def set_path_err_label(self):
        self.path_err_label.setText("该路径下没有报告，请检查！")

    def show_file_list(self, file_list):
        '''展示报告列表'''
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cmm_judge_pane = CmmJudgePane()
    cmm_judge_pane.show()
    sys.exit(app.exec_())
