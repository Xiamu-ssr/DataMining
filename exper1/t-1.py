from numpy import NaN
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append('../utils/')
import pretreatment as pret

data = pd.read_excel(io="./data/catering_sale.xls",sheet_name="Sheet1")
data.rename(columns={'销量':'sales'}, inplace = True)

# 查看原始数据基本情况
print(data.describe())

# 原始数据作图
data.plot.box()
plt.savefig("./img/1-1.jpg")

# 挑选出箱线图离群点索引并丢弃
droplist =  pret.plot_box(data)
data.drop(data.index[droplist['sales']], inplace = True)
# print(droplist)
# print(data.describe())
# 以平均值填充缺失值
data.fillna(value = data.sales.mean(), inplace = True)
# print(data.describe())

# 处理后数据作图
data.plot.box()
plt.savefig("./img/1-2.jpg")