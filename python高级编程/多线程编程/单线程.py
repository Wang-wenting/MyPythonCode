#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/2 10:08
# @Author  : RooFTOooOP
# @FileName: 单线程.py
# @Software: PyCharm

"""
一个循环必须在另一个开始前完成。总共消耗的时间是每个循环所用时间之和
"""

from time import sleep, ctime


def loop0():
    print("start loop0 at :", ctime())
    sleep(4)
    print("end loop0 at :", ctime())


def loop1():
    print("start loop1 at :", ctime())
    sleep(2)
    print("end loop1 at :", ctime())


if __name__ == '__main__':
    print("all start at: ", ctime())
    loop0()
    loop1()
    print("all end at: ", ctime())