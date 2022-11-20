from sqlite3 import DatabaseError
import pandas as pd
import numpy as np


class Dual():
    # 新表路径
    save_path = './save.xlsx'
    # 0.按标签划分 1.按数据范围划分 2.不划分 3.忽略此列
    column_type = [2, 3, 3, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    #按数据划分,分几层
    column_data_num = 4
    #这些层的分界线
    column_data_line = []
    # #按数据划分填划分多少块,标签划分填标签种类数量,忽略填0,原样填充填1
    # column_piece =[1, 0, 0, 4, 4, 4, ]
    def __init__(self, read_path, sheet):
        self.df = pd.read_excel(read_path, sheet)
        self.init_col()
    def init_data_line(self):
        describe = self.df.describe().values
        column_num = len(self.df.columns.values)
        k = 0
        for i in range(0, column_num):
            if self.column_type[i] == 1:
                l = [describe[4][k], describe[5][k], describe[6][k]]
                k += 1
                self.column_data_line.append(l)
            else:
                self.column_data_line.append([])
    def init_col(self):
        self.init_data_line()
        #列的属性都存入此
        self.column = []
        column_name = self.df.columns.values
        column_num = len(column_name)
        for i in range(0, column_num):
            d = {}
            d['name'] = column_name[i]
            d['type'] = self.column_type[i]
            d['piece'] = []
            if d['type'] == 3:
                d['len'] = 0
            elif d['type'] == 2:
                d['len'] = 1
            elif d['type'] == 1:
                d['len'] = self.column_data_num
                d['piece'] = self.column_data_line[i]
            elif d['type'] == 0:
                d['piece'] = list(set(list(v[0] for v in  self.df.iloc[:,i:i+1].values)))
                d['len'] = len(d['piece'])
            self.column.append(d)
            
    def work_row(self):
        #创建表头
        form_header = []
        for c in self.column:
            if c['type'] == 0:
                for i in range(0,c['len']):
                    form_header.append(c['piece'][i])
            elif c['type'] == 1:
                for i in range(0,c['len']):
                    tmp_name = c['name'] + '-' + str(i+1) + '/' + str(self.column_data_num)
                    form_header.append(tmp_name)
            elif c['type'] == 2:
                form_header.append(c['name'])
        self.save = pd.DataFrame(columns=form_header)
        #work
        for i in range(0, len(self.df)):
            df_row = self.df.iloc[i:i+1,:].values[0]
            tmp_row = []
            for j in range(0, len(self.df.columns.values)):
                if self.column[j]['type'] == 2:
                    tmp_row.append(df_row[j])
                elif self.column[j]['type'] == 3:
                    None
                elif self.column[j]['type'] == 1:
                    flag = self.work_cal_data_flag(df_row[j], self.column[j]['piece'])
                    for k in range(0, self.column_data_num):
                        if k == flag:
                            tmp_row.append(1)
                        else:
                            tmp_row.append(0)
                elif self.column[j]['type'] == 0:
                    for k in range(0, self.column[j]['len']):
                        if self.column[j]['piece'][k] == df_row[j]:
                            tmp_row.append(1)
                        else:
                            tmp_row.append(0)
            self.save.loc[len(self.save)+1] = tmp_row
        self.save.to_excel(self.save_path)
    def work_cal_data_flag(self, data, line):
        f = 0
        for l in line:
            if data < l:
                return f
            f += 1
        return f
        

if __name__ == '__main__':
    dual = Dual("./data.xlsx", '样地信息')
    dual.work_row()
    