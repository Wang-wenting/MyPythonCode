#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/20 20:17
# @Author  : RooFTOooOP
# @FileName: TCP时间戳客户端.py
# @Software: PyCharm

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>  ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode())


tcpCliSock.close()