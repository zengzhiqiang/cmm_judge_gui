from source.cmm_judge_pane import CmmJudgePane
from core.judge_workbooks import judge_workbooks
from source.file_list_widget import FileListWidget
from source.file_err_widget import FileErrWidget
from source.sheet_err_widget import SheetErrWidget
from source.row_err_widget import RowErrWidget
from source.data_err_widget import DataErrWidget
from PyQt5.Qt import *
import sys

class CmmJudgeView(object):

    def __init__(self, cmm_judge_pane):
        self.result = None
        self.cmm_judge_pane = cmm_judge_pane
        # self.file_list_layout = QVBoxLayout(cmm_judge_pane.left_bottom_widget)
        self.file_list_layout = QVBoxLayout(cmm_judge_pane.left_bottom_widget)
        self.file_err_layout = QVBoxLayout(cmm_judge_pane.right_widget)

    def cmm_judge(self, path):
        self.clear_files()
        self.result = judge_workbooks(path)
        self.cmm_judge_pane.set_path_err_label()
        files_result = self.result["work books result"]
        self.show_file_list(files_result)

    def show_file_list(self, files_result):
        '''生成该目录下文件列表按钮，文件有错误显示红色，没有错误显示绿色'''
        self.file_list_layout.addStretch(1)
        for file_name in files_result.keys():
            file_list_widget = FileListWidget()
            file_list_widget.set_file_name_btn(file_name)
            file_result = files_result[file_name]
            search_file_err_result = self.search_file_err(file_result)
            # print(search_file_err_result)
            self.set_file_err_stylesheet(file_list_widget, search_file_err_result)
            file_list_widget.show_file_err_signal.connect(self.show_file_err)
            # print(file_name)
            self.file_list_layout.addWidget(file_list_widget)
        self.file_list_layout.addStretch(1)
        print(self.cmm_judge_pane.left_bottom_widget.children())

    def show_file_err(self, file_name):
        '''根据点击的报告名称显示错误信息'''
        self.clear_file()
        file_result = self.result["work books result"][file_name]
        file_err_widget = FileErrWidget()
        file_err_widget.file_name_label.setText(file_name)
        self.file_err_layout.addWidget(file_err_widget)
        sheet_names = file_result.keys()
        sheet_err_layout = QVBoxLayout(file_err_widget.sheet_err_widget)
        for sheet_name in sheet_names:
            sheet_err_widget = SheetErrWidget()
            sheet_err_widget.sheet_name_label.setText(sheet_name)
            sheet_err_layout.addWidget(sheet_err_widget)
            if file_result[sheet_name]["report name err"]:
                sheet_err_widget.sheet_name_err_label.setText("报告编号错了！")
            rows_results = file_result[sheet_name]["rows err"]
            rows_results_keys = rows_results.keys()
            rows_result_layout = QVBoxLayout(sheet_err_widget.row_err_widget)
            for rows_results_key in rows_results_keys:
                rows_err_widget = RowErrWidget()
                if rows_results[rows_results_key]["data format err"]:
                    rows_err_widget.row_err_label.setText(
                        "第{row}行数据格式有误，请检查！".format(row=str(rows_results_key))
                    )
                else:
                    rows_err_widget.row_err_label.setText(
                        "第{row}行错误，正确结果为{right_judge}".format(row=str(rows_results_key),
                        right_judge=rows_results[rows_results_key]["right judge"])
                    )
                rows_result_layout.addWidget(rows_err_widget)
                if "err data" in rows_results[rows_results_key].keys():
                    err_datas = rows_results[rows_results_key]["err data"]
                    if err_datas:
                        err_data_layout = QHBoxLayout(rows_err_widget.data_err_widget)
                        for k, err_data in err_datas.items():
                            data_err_widget = DataErrWidget()
                            data_err_widget.row_label.setText(str(k))
                            data_err_widget.data_label.setText(str(err_data))
                            err_data_layout.addWidget(data_err_widget)
        self.file_err_layout.addStretch(1)

    def clear_file(self):
        '''清空单个工作表'''
        self.delete_children_later(self.cmm_judge_pane.right_widget, FileErrWidget)

    def clear_files(self):
        '''清空所有'''
        self.delete_children_later(self.cmm_judge_pane.right_widget, FileErrWidget)
        self.delete_children_later(self.cmm_judge_pane.left_bottom_widget, FileListWidget)

    def delete_children_later(self, parent, children):
        '''
        parent: 实例化的widget
        children： 需要删除的父控件类
        删除父控件下指定的子控件窗口
        '''
        exist_widgets = parent.findChildren(children)
        for exist_widget in exist_widgets:
            exist_widget.deleteLater()

    def set_file_err_stylesheet(self, file_list_widget, result):
        '''将有错误的报告按钮后添加标识'''
        file_list_widget.file_name_label.setText(result)
        if result == "OK":
            file_list_widget.file_name_btn.setEnabled(False)

    def search_file_err(self, file_result):
        for sheet, sheet_result in file_result.items():
            if sheet_result["report name err"] or len(sheet_result["rows err"]):
                return "NO"
        return "OK"

    def run_cmm_judge_main(self):

        self.cmm_judge_pane.get_path_signal.connect(self.cmm_judge)
        print("打开三坐标检查程序！1")
        self.cmm_judge_pane.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    '''实例化窗口'''
    cmm_judge_pane = CmmJudgePane()
    '''将窗口传递给view类。实例化view类'''
    cmm_judge_view = CmmJudgeView(cmm_judge_pane)
    '''执行根据信号触发view中的槽函数'''
    # cmm_judge_pane.get_path_signal.connect(cmm_judge_view.cmm_judge)
    # cmm_judge_pane.path_input_line_edit.setText("C:\工作\桌面\临时\改善课题\改善课题\已提交\【改善小组】三坐标报告自动查错程序")
    # cmm_judge_pane.show()
    cmm_judge_view.run_cmm_judge_main()
    sys.exit(app.exec_())
