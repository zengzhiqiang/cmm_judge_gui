import re
from . import rowdata

class WorkSheet():

    def __init__(self, table, report_number_file):
        self.table = table
        self.report_number_file = report_number_file
        '''运行变量'''
        self.table_state = {
            "report name err": True,            #记录该表格内报告编号是否错误, False表示没有错误
            "rows err": {

            },
        }
        '''执行函数'''
        self.run()

    def check_report_number(self):
        title_row = self.table.row_values(1)
        for title_row_data in title_row:
            report_number_table = re.search(r'20\d\d[-]\d\d[-]\d\d\d', title_row_data)
            if report_number_table and (report_number_table.group() == self.report_number_file):
                self.table_state["report name err"] = False

    def run(self):
        self.check_report_number()
        rows = self.table.nrows
        cols = self.table.ncols
        for row in range(0, rows):
            data = self.table.row_values(row)
            if type(data[0]) == float:
                stand = self.format_data(data[1])
                up_tol = self.format_data(data[2])
                low_tol = self.format_data(data[3])
                test_data = []
                for col in range(4, cols - 2):
                    if self.table.cell(row, col).value and self.table.cell(row, col).value != "/":
                        test_datums = str(self.table.cell(row, col).value).split("、")
                        for test_datum in test_datums:
                            try:
                                float(test_datum)
                                test_data.append(float(test_datum))
                            except:
                                self.table_state["rows err"].update({data[0]: {"data format err": True}})
                rdata = rowdata.RowData(stand, up_tol, low_tol, test_data)
                judge = str(data[len(data) - 2]).replace(" ", "")
                '''比较判定值与实际值是否一致'''
                if judge == rdata.result["right judge"]:
                    pass
                    # if data[0] in self.table_state.keys():
                    #     self.table_state[data[0]].update({"msg": True, "result": rdata.result})
                    # else:
                    #     self.table_state.update({data[0]: {"数字格式错误": False, "msg": True, "result": rdata.result}})
                else:
                    if data[0] in self.table_state["rows err"].keys():
                        self.table_state["rows err"][data[0]].update(rdata.result)
                    else:
                        self.table_state["rows err"].update({data[0]: {"data format err": False}})
                        self.table_state["rows err"][data[0]].update(rdata.result)

    def format_data(self, data):
        '''剔除data中非数字部分内容'''
        try:
            formatted_data = float(re.search(r"\d+(\.\d+)?", str(data)).group())
        except:
            formatted_data = None
        return formatted_data

if __name__ == "__main__":
    pass
