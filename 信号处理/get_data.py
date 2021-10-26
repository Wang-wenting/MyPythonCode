#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 11:11
# @Author  : RooFTOooOP
# @FileName: get_data.py
# @Software: PyCharm


import pandas as pd
import numpy as np
from signal_analyse import SignalFeatures as SF
from a_v_s import ShiYvFa, PinYvFa
import matplotlib.pyplot as plt

fs = 12800
datafile = 'D:\寿命预测\XJTU-SY_Bearing_Datasets\\35Hz12kN\Bearing1_1\\1.csv'
data = pd.read_csv(datafile, encoding='utf-8', engine='python')
data = data.values
x_slice = data[:, 1]
n = x_slice.shape[0]
pyf = PinYvFa(x_slice, fs, n)
v,s = pyf.jifen()

sf = SF(v[5000:-5000], fs)
a = sf.junfanggenzhi()
print(a)

# sf1 = SF(v[5000:-5000], fs)
# b = sf1.junfanggenzhi()
# print(b)
#
# sf2 = SF(s[5000:-5000], fs)
# c = sf2.junfanggenzhi()
# print(c)

t, y = sf.shiyuboxing()
f, y1 = sf.pinpu()
f1, y2 = sf.baoluopu()
shiyv = np.array([t,y])
pinyv = np.array([f,y1])
baoluo = np.array([f1,y2])
pd_data1 = pd.DataFrame(shiyv, index=['time', 'amplitude'])
df1 = pd.DataFrame(pd_data1.values.T, columns=pd_data1.index)

pd_data2 = pd.DataFrame(pinyv, index=['frequency', 'amplitude'])
df2 = pd.DataFrame(pd_data2.values.T, columns=pd_data2.index)

pd_data3 = pd.DataFrame(baoluo, index=['frequency', 'amplitude'])
df3 = pd.DataFrame(pd_data3.values.T, columns=pd_data3.index)

df1.to_csv('Y方向速度信号.csv', index=False)
df2.to_csv('Y方向速度频谱.csv', index=False)
df3.to_csv('Y方向速度包络谱.csv', index=False)
# df3.to_csv('weiyibaoluo.csv')
