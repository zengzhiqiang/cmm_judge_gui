class RowData:

    def __init__(self, stand, up_tol, low_tol, test_data):
        self.stand = stand
        self.up_tol = up_tol
        self.low_tol = low_tol
        self.test_data = test_data
        # 设置运行
        # self.right_judge = None
        self.result = {
            "right judge": "/",
            "err data": {
            },
        }
        '''运行'''
        self.make_judge()

    def make_judge(self):

        if self.stand == None or (self.up_tol == None and self.low_tol == None):
            '''上下公差均为空'''
            pass
            # self.result["right judge"] = "/"
        elif self.up_tol == None:
            for i in range(0, len(self.test_data)):
                if self.test_data[i] < self.stand - self.low_tol:
                    self.result["err data"].update({i: self.test_data[i]})
        elif self.low_tol == None:
            for i in range(0, len(self.test_data)):
                if self.test_data[i] > self.stand + self.up_tol:
                    self.result["err data"].update({i: self.test_data[i]})
        else:
            for i in range(0, len(self.test_data)):
                if self.test_data[i] > self.stand + self.up_tol or self.test_data[i] < self.stand - self.low_tol:
                    self.result["err data"].update({i: self.test_data[i]})
            if not self.result["err data"]:
                self.result["right judge"] = "OK"

        if self.result["err data"]:
            self.result["right judge"] = "NO"




if __name__ == "__main__":
    '''测试类功能'''
    rowdata0 = RowData(100, 100, 100, [100, 200, 0])
    rowdata0.make_judge()

