import pandas as pd
import numpy as np

# 返回一个字典,key是列名,values是列数据中以plot-box方法算出的离群点索引index
def plot_box(data:'pd.core.frame.DataFrame') -> 'dict':
    columns = data.columns.tolist()
    res = dict()
    for c in columns:
        d = data[c]
        q = d.quantile([0.25, 0.5, 0.75]).tolist()
        upper = q[2] + 1.5 * (q[2] - q[0])
        lower = q[0] - 1.5 * (q[2] - q[0])
        droplist = d[(d < lower)|(d > upper)].index.values.tolist()
        res[c] = droplist
    return res

# 输出xls中各个sheet的describe和shape
def sheet(url:'str'):
    print(url)
    data = pd.read_excel(url, sheet_name=None)
    sheets = list(data)
    for s in sheets:
        print("---", s, "---")
        print("shape",data[s].shape)
        if data[s].columns.any() != False:
            print("describe", data[s].describe())
            
# 给定文件，输出latex表格代码
def tabular(url:'str', url2:'str',T:'bool'=False):
    #read
    f = open(url)
    line = f.readlines()
    l = []
    for li in line:
        l.append(list(li.split()))
    f.close()
    # T?
    if T:
        ll = l
        l = []
        for j in range(0,len(ll[0])):
            lll = []
            for i in range(0,len(ll)):
                lll.append(ll[i][j])
            l.append(lll)
                
    #work
    stri = "\\begin{tabular}{|"
    for i in range(0,len(l[0])):
        stri += " c |"
    stri += "}\\hline\n"
    for i in l:
        for j in range(0,len(i)):
            if is_number(i[j]):
                stri += str(round(eval(i[j]),3))
            else:
                stri += i[j]
            if j != len(i)-1:
                stri += " & "
        stri += "\\\\\\hline\n"
    stri += "\\end{tabular}"
    #write
    with open(url2,'w') as f:
        f.write(stri)

# 给定文件，输出latex表格代码
def table(url:'str', url2:'str',T:'bool'=False):
    #read
    f = open(url)
    line = f.readlines()
    l = []
    for li in line:
        l.append(list(li.split()))
    f.close()
    # T?
    if T:
        ll = l
        l = []
        for j in range(0,len(ll[0])):
            lll = []
            for i in range(0,len(ll)):
                lll.append(ll[i][j])
            l.append(lll)
                
    #work
    stri = "\\begin{table}[H]\n\centering\n\\begin{tabular}{"
    for i in range(0,len(l[0])):
        stri += " c "
    stri += "}\\toprule\n"
    first = True
    for i in l:
        for j in range(0,len(i)):
            if is_number(i[j]):
                stri += str(round(eval(i[j]),3))
            else:
                stri += i[j]
            if j != len(i)-1:
                stri += " & "
        stri += "\\\\"
        if first:
            first = False
            stri += "\\hline"
        stri += "\n"
    stri += "\\bottomrule\n\\end{tabular}\n\end{table}\n"
    #write
    with open(url2,'w') as f:
        f.write(stri)

# 是否数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False