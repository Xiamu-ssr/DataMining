from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# sys.path.append('../utils/')
# import pretreatment as pret

# pret.sheet("./data/discretization_data.xls")
data = pd.read_excel("./data/discretization_data.xls", sheet_name="Sheet1")
col = data.columns.tolist()[0]

# 等宽法
data1 = data.copy()
bins = 5
labels = ["lower", "low", "mid", "high", "higher"]
data1[col] = pd.cut(data1[col], bins, labels=labels)

l = []
for la in labels:
    l.append(data1[col].value_counts()[la])
df = pd.DataFrame({col : l},index=labels)
plt.figure()
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
df.plot(kind = 'bar')
plt.savefig("./img/4-1.jpg")

# 等频法
data2 = data.copy()
labels = ["lower", "low", "mid", "high", "higher"]
data2[col] = pd.qcut(data2[col], bins, labels=labels)

l = []
for la in labels:
    l.append(data2[col].value_counts()[la])
df = pd.DataFrame({col : l},index=labels)
plt.figure()
df.plot(kind = 'bar')
plt.savefig("./img/4-2.jpg")
