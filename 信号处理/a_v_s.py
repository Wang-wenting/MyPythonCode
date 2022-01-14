#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 11:38
# @Author  : RooFTOooOP
# @FileName: a_v_s.py
# @Software: PyCharm


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 13:04
# @Author  : RooFTOooOP
# @FileName: 加速度积分.py
# @Software: PyCharm

import numpy as np
from matplotlib import pyplot as plt
import math
import numpy as np
from scipy import linalg
from sklearn.linear_model import LinearRegression
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class PinYvFa(object):
    """
        Parameters
        ----------
        data : 输入加速度信号，一维列表
        fs : 采样频率，整型变量
        n : 采样点数，整型变量
        ----------
        Note：本方法为加速度信号的频域积分法
    """
    def __init__(self, data, fs, n):
        self.data = data
        self.fs = fs
        self.n = n

    # 定义均方误差MSE
    def jifen(self):
        # d = np.array(self.data)
        # d = d - d.mean()
        transformed = np.fft.fft(self.data)  # 使用fft函数对信号进行傅里叶变换
        v = []
        v.append(0)
        s = []
        s.append(0)
        for i in range(1, len(transformed)):
            w_j = 0.0 + i * 2 * math.pi * 1j * self.fs / self.n
            w_2 = -((i * 2 * math.pi * self.fs / self.n) ** 2)
            if i * 2 * math.pi * self.fs / self.n <= 10:
                vi = 0
                si = 0
            else:
                vi = 2 * transformed[i] / w_j
                si = 2 * transformed[i] / w_2
            v.append(vi)
            s.append(si)
        # wave_0 = np.fft.ifft(transformed)
        v_0 = (np.fft.ifft(v)).real
        v_0 = v_0*1000
        s_0 = (np.fft.ifft(s)).real
        s_0 = np.reshape(s_0, [-1, 1])
        # s = s[:len(self.data) // 2]  # 使用fft函数对余弦波信号进行傅里叶变换。
        # s = np.abs(s) / len(self.data) * 2.
        t = np.linspace(0, self.n / self.fs, self.n + 1)
        t = t[0:self.n]
        t = np.reshape(t, [-1, 1])
        lr = LinearRegression().fit(t, s_0)
        slope = lr.coef_[0][0]
        y_int = lr.intercept_[0]
        s_1 = []
        for j in range(len(t)):
            expected_val = slope * t[j] + y_int
            s_1.append(s_0[j] - expected_val)
        s_1 = np.squeeze(np.array(s_1))
        s_1 = s_1*1000
        return v_0, s_1

    def plot_a(self):
        t = np.linspace(0, self.n / self.fs, self.n + 1)
        t = t[0:self.n]
        plt.figure()
        p1, = plt.plot(t, self.data, color='b')
        plt.ylabel(u'幅值', size=14)
        plt.xlabel(u'时间', size=14)
        plt.title(u'加速度信号', size=18)
        plt.show()

    def plot_v(self):
        t = np.linspace(0, self.n / self.fs, self.n + 1)
        t = t[0:self.n]
        v, s= self.jifen()
        v = np.array(v)*1000

        plt.figure()
        p1, = plt.plot( v, color='b')
        plt.ylabel(u'幅值', size=14)
        plt.xlabel(u'Hz', size=14)
        plt.title(u'频域积分速度信号', size=18)
        plt.show()

    def plot_s(self):
        t = np.linspace(0, self.n / self.fs, self.n + 1)
        t = t[0:self.n]
        v, s = self.jifen()
        # s = np.array(s) * 1000000
        plt.figure()
        p1, = plt.plot(s, color='b')
        plt.ylabel(u'幅值', size=14)
        plt.xlabel(u'时间', size=14)
        plt.title(u'频域积分位移信号', size=18)
        plt.show()


class ShiYvFa(object):
    """
        Parameters
        ----------
        data : 输入加速度信号，一维列表
        fs : 采样频率，整型变量
        n : 采样点数，整型变量
        ----------
        Note：本方法为去除趋势项的加速度信号时域积分法
    """

    def __init__(self, data, fs, n):
        self.data = data
        self.fs = fs
        self.n = n

    # 时域积分
    def jifen(self):
        v = []
        v.append(0)
        # 时域积分得到含趋势项速度信号
        for i in range(1, self.n):
            vi = v[i - 1] + (self.data[i - 1] + self.data[i]) / (2 * self.fs)
            v.append(vi)
        # 去除趋势项
        v_correct = [0 for _ in range(self.n)]
        A_0 = self.n
        A_1 = 0
        for i in range(self.n):
            A_1 = A_1 + i / self.fs
        A_2 = A_1
        A_3 = 0
        for i in range(self.n):
            A_3 = A_3 + (i / self.fs) ** 2
        B_0 = 0
        for i in range(self.n):
            B_0 = B_0 + v[i]
        B_1 = 0
        for i in range(self.n):
            B_1 = B_1 + v[i] * (i / self.fs)
        A = np.array([[A_0, A_1], [A_2, A_3]])  # A代表系数矩阵
        b = np.array([B_0, B_1])  # b代表常数列
        p = linalg.solve(A, b)
        for i in range(1, self.n):
            v_correct[i] = v[i] - p[1] * (i / self.fs) - p[0]

        # 时域积分得到含趋势项位移信号
        s = []
        s.append(0)
        for i in range(1, self.n - 1):
            si = s[i - 1] + (v[i] + v[i + 1]) / (2 * self.fs)
            s.append(si)
        s_correct = [0 for _ in range(self.n - 1)]
        # 去除趋势项
        C_0 = self.n - 1
        C_1 = 0
        for i in range(self.n - 1):
            C_1 = C_1 + i / self.fs
        C_2 = 0
        for i in range(self.n - 1):
            C_2 = C_2 + (i / self.fs) ** 2
        C_3 = C_1
        C_4 = C_2
        C_5 = 0
        for i in range(self.n - 1):
            C_5 = C_5 + (i / self.fs) ** 3
        C_6 = C_2
        C_7 = C_5
        C_8 = 0
        for i in range(self.n - 1):
            C_8 = C_8 + (i / self.fs) ** 4
        D_0 = 0
        for i in range(self.n - 1):
            D_0 = D_0 + s[i]
        D_1 = 0
        for i in range(self.n - 1):
            D_1 = D_1 + s[i] * (i / self.fs)
        D_2 = 0
        for i in range(self.n - 1):
            D_2 = D_2 + s[i] * ((i / self.fs) ** 2)
        C = np.array([[C_0, C_1, C_2], [C_3, C_4, C_5], [C_6, C_7, C_8]])  # C代表系数矩阵
        d = np.array([D_0, D_1, D_2])  # d代表常数列
        q = linalg.solve(C, d)
        for i in range(1, self.n - 1):
            s_correct[i] = s[i] - q[2] * ((i / self.fs) ** 2) - q[1] * (i / self.fs) - q[0]
        return v_correct, s_correct

    def plot_a(self):
        t = np.linspace(0, self.n / self.fs, self.n + 1)
        t = t[0:self.n]
        plt.figure()
        p1, = plt.plot(t, self.data, color='b')
        plt.ylabel(u'幅值', size=14)
        plt.xlabel(u'时间', size=14)
        plt.title(u'加速度信号', size=18)
        plt.show()

    def plot_v(self):
        t = np.linspace(0, self.n / self.fs, self.n + 1)
        t = t[0:self.n]
        t_0 = t[0:self.n]
        v, s = self.jifen()
        v = np.array(v) * 1000
        plt.figure()
        p1, = plt.plot(t_0, v, color='b')
        plt.ylabel(u'幅值', size=14)
        plt.xlabel(u'时间', size=14)
        plt.title(u'时域积分速度信号', size=18)
        plt.show()

    def plot_s(self):
        t = np.linspace(0, self.n / self.fs, self.n + 1)
        t = t[0:self.n]
        t_1 = t[0:self.n - 1]
        v, s = self.jifen()
        s = np.array(s) * 1000000
        plt.figure()
        p1, = plt.plot(t_1, s, color='b')
        plt.ylabel(u'幅值', size=14)
        plt.xlabel(u'时间', size=14)
        plt.title(u'时域积分位移信号', size=18)
        plt.show()


# file_name = 'E:\横向课题\昇阳项目资料\加速度信号转速度信号及位移信号\\2A浆液循环泵电机非驱动端4-2.txt'
# list1 = []  # X方向振动加速度信号
# list2 = []  # Y方向振动加速度信号
# list3 = []  # Z方向振动加速度信号
# with open(file_name, "r", encoding='utf-8') as f:  # 打开文件
#     data = f.readlines()
#     for line in data:
#         line = line.strip('\n')
#     for i in range(14, len(data)):
#         list1.append(float(data[i].split()[1]))
#         list2.append(float(data[i].split()[2]))
#         list3.append(float(data[i].split()[3]))
# fs = 3200
# n = 1024
# pinyvfa = PinYvFa(list1, fs, n)
# # pinyvfa.plot_a()
# pinyvfa.plot_v()
# pinyvfa.plot_s()


# shiyvfa = ShiYvFa(list1, fs, n)
# shiyvfa.plot_a()
# shiyvfa.plot_v()
# shiyvfa.plot_s()