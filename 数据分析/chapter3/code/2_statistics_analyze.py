# coding:utf-8

import os
import pandas as pd
# os.path.dirname(__file__)获取当前文件的父目录
path = os.path.dirname(os.path.dirname(__file__))
catering_sale = path + '\data\catering_sale.xls'  # 餐饮数据
data = pd.read_excel(catering_sale, index_col=u'日期')  # 读取数据，指定‘日期’列为索引列
data = data[(data[u'销量'] > 400) & (data[u'销量'] < 5000)]  #  过滤异常数据
statistics = data.describe()
statistics.loc['range'] = statistics.loc['mean'] - statistics.loc['min']  # 极差
statistics.loc['var'] = statistics.loc['std'] - statistics.loc['mean']  # 变异系数
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']  # 四分位数间距
print(type(statistics))
print(statistics)