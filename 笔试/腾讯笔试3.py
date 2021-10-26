#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 20:09
# @Author  : RooFTOooOP
# @FileName: 腾讯笔试3.py
# @Software: PyCharm
import copy

while True:
    try:
        n, k = list(map(int, input().split()))
        cake = list(map(int, input().split()))
        res = 100000
        if n == k:
            print(0)
        else:
            for i in range(k-1, n):
                m = sum(cake[i-k+1: i+1])/k
                c1 = []
                c1.extend(cake[:i-k+1])
                c1.extend([m]*k)
                c1.extend(cake[i+1:])
                r = max(c1)-min(c1)
                if res > r:
                    res = r
            print(res)
    except:
        break



