#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 10:47
# @Author  : RooFTOooOP
# @FileName: 中兴笔试.py
# @Software: PyCharm


# cake = [[-1,1,-1],[2,-2,1],[3,-2,-2]]
cake = [[-1,-2],[-3,-4]]
res = float('-inf')
n = len(cake)
dp = [[0]*n for _ in range(n)]

for j in range(n):
    dp[-1][j] = sum(cake[-1][0:j+1])
    res = max(res, dp[-1][j])

for i in range(n-2, -1, -1):
    for j in range(n):
        if i==0 and j==n-1:
            break
        dp[i][j] = sum(cake[i][0:j+1])
        dp[i][j] += max(dp[i+1][j:n])
        if dp[i][j]>res:
            res = dp[i][j]
print(res)