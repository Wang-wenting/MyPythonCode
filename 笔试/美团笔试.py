#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/29 9:59
# @Author  : RooFTOooOP
# @FileName: 美团笔试.py
# @Software: PyCharm

while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        # a.sort()
        b.sort()
        ans = 1
        book = 0
        for drawer in range(n):
            while a[book] < b[drawer] and book < n - 1:
                book += 1
            ans *= (book - drawer + 1)
        # for i in range(1, n):
        #     j = i
        #     target = a[i]
        #     left = 0
        #     right = j
        #     while left<right:
        #         mid = (left+right)//2
        #         if b[mid] <target:
        #             left = mid+1
        #         elif b[mid]>target:
        #             right = mid
        #         else:
        #             left = mid
        #             break
        #     ans = ans*(i-left+1)
        print(ans%(10**9+7))

    except:
        break
