#!/usr/bin/env python3
#antuor:Alan

import pandas as pd
sale = '/Users/Alan/desktop/项目5-项目数据分析/data.xlsx'
data = pd.read_excel(sale,index_col=u'日期')
data.describe()
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
p = data.boxplot()
x=p['fliers'][0].get_xdata()
y=p['fliers'][0].get_ydata()
y.sort()

for i in range(len(x)):
    if i >0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
plt.show()
