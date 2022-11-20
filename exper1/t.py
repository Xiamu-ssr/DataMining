import os
import sys
import pandas as pd

sys.path.append('../utils/')
import pretreatment as pret

# filePath = "./data/" 
# filesP = os.listdir(filePath)
# filesP2 = []
# for f in filesP:
#     filesP2.append(filePath + f)
# print(filesP2)

# for f in filesP2:
#     pret.sheet(f)

filePath = '../utils/t.txt'
savePath = '../utils/tabular.txt'
pret.tabular(filePath, savePath)

# data = pd.read_excel('./data/normalization_data.xls', header = None)

# print(data.describe().round(2))