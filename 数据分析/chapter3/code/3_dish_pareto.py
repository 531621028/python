# coding:utf-8

import os

import matplotlib.pyplot as plt
import pandas as pd

# os.path.dirname(__file__)获取当前文件的父目录
path = os.path.dirname(os.path.dirname(__file__))
dish_profit = path + '\data\catering_dish_profit.xls'  # 餐饮数据
data = pd.read_excel(dish_profit, index_col=u'菜品名')  # 读取数据，指定‘菜品’列为索引列
data = data[u'盈利'].copy()
data.sort_values(ascending=False)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure()
data.plot(kind='bar')
plt.ylabel(u'盈利（元）')
p = 1.0 * data.cumsum() / data.sum()
print(type(p))
print(type(p.plot(color='r', secondary_y=True, style='-o', linewidth=2)))
plt.annotate(
    format(p[6], '.4%'),
    xy=(6, p[6]),
    xytext=(6 * 0.9, p[6] * 0.9),
    arrowprops=dict(
        arrowstyle="->",
        connectionstyle="arc3,rad=.2"))  #添加注释，即85%处的标记。这里包括了指定箭头样式。
plt.ylabel(u'盈利（比例）')
# plt.show()
print(type(data))
