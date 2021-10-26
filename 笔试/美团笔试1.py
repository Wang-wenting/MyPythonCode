#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/29 10:58
# @Author  : RooFTOooOP
# @FileName: 美团笔试1.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41800366

while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        sum=0
        hashmap = {}
        hashmap[a[0]] = 0
        for i in range(1, n):
            b = list(hashmap.keys())
            res = a[0]
            for c in b:
                if a[i]>=c:
                    res = max(res,c)
            if a[i]==res:
                ans = hashmap[res]
                sum+=ans
            else:
                ans = hashmap[res]+1
                hashmap[a[i]] = ans
                sum+=ans
        print(sum)

    except:
        break
