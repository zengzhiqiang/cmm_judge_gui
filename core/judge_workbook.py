import xlrd
import re
from . import worksheet

def judge_workbook(file):
    workbook_state = {
    }
    report_number_file = re.search(r'20\d\d[-]\d\d[-]\d\d\d', file).group()
    workbook = xlrd.open_workbook(file)
    sheet_names = workbook.sheet_names()
    for sheet_name in sheet_names:
        table = workbook.sheet_by_name(sheet_name)
        sheet = worksheet.WorkSheet(table, report_number_file)
        workbook_state.update({sheet_name: sheet.table_state})
    return workbook_state


if __name__ == "__main__":

    file = r"C:\Myfile\github\CMM_judge_GUI\2019-08-267.xls"
    print(judge_workbook(file))
