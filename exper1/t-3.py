import pandas as pd
import numpy as np


data = pd.read_excel("./data/catering_sale_all.xls", sheet_name="Sheet1")

print(data.corr('pearson'))