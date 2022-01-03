#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/3 9:52
# @Author  : RooFTOooOP
# @FileName: 使用Threading模块.py
# @Software: PyCharm

"""
创建Thread实例，并传递给它一个函数
"""

import threading
from time import ctime, sleep

loops = [4, 2]


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at', ctime())


def main():
    print('starting at ', ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()  # 等待所有线程完成，功能等价于线程锁
    print('ending at ', ctime())

main()