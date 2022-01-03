#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/16 19:50
# @Author  : RooFTOooOP
# @FileName: gendata.py
# @Software: PyCharm

from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime
import re

tlds = ('com', 'edu', 'net', 'org', 'gov')


def get_str():
    mstr = ''
    for i in range(randrange(5, 11)):
        dtint = randrange(1e10)
        dtstr = ctime(dtint)
        llen = randrange(4, 8)
        login = ''.join(choice(lc) for _ in range(llen))
        dlen = randrange(llen, 13)
        dom = ''.join(choice(lc) for _ in range(dlen))
        mstr += '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen)
        mstr += '\n'
    return mstr


# ms = get_str()
# ms = ''
# with open('test.txt', 'r', encoding='utf-8') as f:
#     for line in f.readlines():
#         ms += line
# print(ms)
# patt1 = '^(.+?)::'
# patt2 = '::(.+?)::'
# patt3 = '\w{3} (\w+) '
# patt4 = ' (\d{4})::'
# patt5 = ' (\d{2}:\d{2}:\d{2}) '
# patt6 = '@(\w+)\.(\w{3})::'
# patt7 = '(?<=::)(\w+@\w+\.\w{3})(?=::)'
# patt8 = r'\w{3} (\w{3}) +(\d+) .{8} (\d{4})'
# m = re.sub(patt7, '1157290948@qq.com', ms)
# m0 = re.findall(patt8, ms, re.M)
# print(m0)
# m1 = re.finditer(patt8, ms)
# for n in m1:
#     print('%s,%s,%s' % (n.group(1), n.group(2), n.group(3)))

# patt9 = r'^(?:\(\d{3}\) |\d{3}-|)\d{3}-\d{4}'
# num1 = '800-555-1212'
# num2 = '555-1221'
# num3 = '(800) 555-1212'
# m = re.match(patt9, num1)
# n = re.match(patt9, num3)
# print(m.group())
# print(n.group())



