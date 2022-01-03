#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/15 14:37
# @Author  : RooFTOooOP
# @FileName: 正则表达式.py
# @Software: PyCharm

import re

data = ('Mountain View,   CA   94040', 'Sunnyvale, CA', 'Los Altos, 94023')
for d in data:
    print(re.split(r', +| +(?=(?:\d{5}|[A-Z]{2}))', d))

