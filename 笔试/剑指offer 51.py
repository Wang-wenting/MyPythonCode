#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 9:33
# @Author  : RooFTOooOP
# @FileName: 剑指offer 51.py
# @Software: PyCharm

def merge_sort(l, r):
    if l >= r: return 0
    m = (l + r) // 2
    res = merge_sort(l, m) + merge_sort(m + 1, r)
    i, j = l, m + 1
    tmp[l:r + 1] = nums[l:r + 1]
    for k in range(l, r + 1):
        if j == r + 1 or tmp[i] <= tmp[j]:
            nums[k] = tmp[i]
            i += 1
        elif i == m + 1:
            nums[k] = tmp[j]
            j += 1
        else:
            nums[k] = tmp[j]
            j += 1
            res += m - i + 1
    return res

nums = [4,5,6,7]
tmp = [0] * len(nums)
res = merge_sort(0, len(nums) - 1)
print(res)