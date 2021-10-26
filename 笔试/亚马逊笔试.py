#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/4 14:34
# @Author  : RooFTOooOP
# @FileName: 亚马逊笔试.py
# @Software: PyCharm

while True:
    try:
        m = int(input())
        n = int(input())
        buildings = []
        for _ in range(m):
            buildings.append(list(map(int, input().split())))
        res = [[m + n] * n for _ in range(m)]
        hashmap = []
        for i in range(m):
            for j in range(n):
                if buildings[i][j] == 1:
                    res[i][j] = 0
                    hashmap.append([i, j])
        for i in range(m):
            for j in range(n):
                for num in hashmap:
                    if res[i][j] == 0:
                        break
                    res[i][j] = min(res[i][j], abs(num[0] - i) + abs(num[1] - j))
                    if res[i][j] == 1:
                        break

        for i in range(m):
            for j in range(n):
                print(res[i][j], end=' ')
            print('')
    except:
        break
