#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 11:33
# @Author  : RooFTOooOP
# @FileName: 剑指offer 38.py
# @Software: PyCharm

s ='abbd'
used = [False]*len(s)
path =[]
res = []
def recur(s):
    if len(path)==len(s):
        res.append(''.join(path))
        return
    for i in range(len(s)):
        if i>0 and s[i]==s[i-1]: continue
        if used[i]:
            continue
        path.append(s[i])
        used[i]=True
        recur(s)
        used[i] = False
        path.pop()
s = list(s)
s.sort()
recur(s)
print(res)