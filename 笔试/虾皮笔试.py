#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 19:35
# @Author  : RooFTOooOP
# @FileName: 虾皮笔试.py
# @Software: PyCharm

def panduan(x):
    if x[0] == '1':
        if x[1] == '^':
            if x[2] == '0':
                return 1
            elif x[2] == '1':
                return 0
        elif x[1] == '|':
            return 1
        else:
            if x[2] == '0':
                return 0
            elif x[2] == '1':
                return 1
    else:
        if x[1] == '^':
            if x[2] == '0':
                return 0
            elif x[2] == '1':
                return 1
        elif x[1] == '&':
            return 0
        else:
            if x[2] == '0':
                return 0
            elif x[2] == '1':
                return 1


a = '1^0|0|1'
desired = False
dp = [[0] * 2 for _ in range(len(a))]
dp[0][0] = int(a[0])
dp[0][1] = panduan(a[0:2])
dp[-1][0] = int(a[-1])
dp[-1][1] = panduan(a[-2:])
for i in range(2, len(a), 2):
    dp[i][0]=