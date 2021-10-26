#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/20 11:25
# @Author  : RooFTOooOP
# @FileName: 文件对比.py
# @Software: PyCharm

import os

while 1:
    try:
        a= []
        b=[]
        for i in range(13):
            a.append(input())

        for k in range(13):
            if input()!=a[k]:
                print(str(k+1)+'Error----'+a[k])
        print('right')


    except:
        break