from .judge_workbook import judge_workbook
import os
import re

def judge_workbooks(path):
    judge_workbooks_result = {
        "path err": False,  #记录路径是否错误
        "work books result": {

        },
    }
    files = []
    try:
        files = os.listdir(path)
    except:
        judge_workbooks_result["path err"] = True
    for file in files:
        if file[-4:] == '.xls' or file[-5:] == '.xlsx':
            if re.search(r'20\d\d[-]\d\d[-]\d\d\d', file):
                file_path = os.path.join(path, file)
                workbook_state = judge_workbook(file_path)
                judge_workbooks_result["work books result"].update({file: workbook_state})
                judge_workbooks_result["path err"] = True
    return judge_workbooks_result




if __name__ == "__main__":
    import json
    path = input("请输入文件夹：")
    with open("result.txt", "w") as result_file:
        result = judge_workbooks(path)
        result_file.write(json.dumps(result))

    print(judge_workbooks(path))


