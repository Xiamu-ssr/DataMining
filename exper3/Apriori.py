import pandas as pd

class Apriori():
    data = []
    C1 = None
    C2 = None
    Map = {}
    def __init__(self, read_path):
        self.df = pd.read_excel(read_path)
        self.columns = self.df.columns.values
        self.columns_len = len(self.columns)
        self.rows_len = len(self.df)
        self.C1 = [0] * self.columns_len
        self.C2 = [0] * self.columns_len * self.columns_len
        self.cal_Map()
        self.cal_data()
        self.cal_C1()
        self.cal_C2()
    def cal_data(self):
        for i in range(0, self.rows_len):
            df_row = self.df.iloc[i:i+1,:].values[0]
            tmp_list = []
            for j in range(1, self.columns_len):
                if df_row[j] == 1:
                    tmp_list.append(j)
            self.data.append(tmp_list)
    def cal_Map(self):
        k = 0
        for c in self.columns:
            self.Map[k] = c
            k += 1
    def cal_C1(self):
        for d in self.data:
            for i in d:
                self.C1[i-1] += 1
    def cal_C2(self):
        for d in self.data:
            for i in range(0, len(d)):
                for j in range(0, len(d)):
                    self.C2[d[i]*self.columns_len+d[j]] += 1
    def support(self, A, B):
        return self.C2[A*self.columns_len+B] / self.rows_len
    def confidence(self, A, B):
        return self.support(A, B) / (self.C1[A-1]/self.rows_len)
if __name__ == "__main__":
    confidence_start = [25, 26, 27, 28, 29, 30, 31]
    confidence_matrix = []
    ap = Apriori("./save.xlsx")
    confidence_rows_name = [ap.Map[i] for i in range(25, 32)]
    #计算置信度
    for c in confidence_start:
        confidence_list = []
        for i in range(1, 25):
            confidence_list.append(ap.confidence(c, i))
        for i in range(32, 76):
            confidence_list.append(ap.confidence(c, i))
        confidence_matrix.append(confidence_list)
    #计算列名
    form_header = ['退化程度']
    for i in range(1, 25):
        form_header.append(ap.Map[i])
    for i in range(32, 76):
        form_header.append(ap.Map[i])
    #写入表格
    confidence_excel = pd.DataFrame(columns=form_header)
    for i in range(0, len(confidence_matrix)):
        confidence_matrix[i].insert(0, confidence_rows_name[i])
        confidence_excel.loc[len(confidence_excel)+1] = confidence_matrix[i]
    confidence_excel.to_excel('./confidence_matrix.xlsx')
    
    
    