import pandas as pd
import numpy as np

data = pd.read_excel("./data/normalization_data.xls", sheet_name="Sheet1", header = None)

# 最大-最小、零-均值、小数定标规范化
data1 = data.copy()
data1 = (data1 - data1.min()) / (data1.max() - data1.min())
data2 = data.copy()
data2 = (data2 - data2.mean()) / data2.std()
data3 = data.copy()
data3 = data3 / 10**np.ceil(np.log10(data3.abs().max()))

print(data)
print(data1)
print(data2)
print(data3)