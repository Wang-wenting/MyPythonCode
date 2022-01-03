#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/20 21:50
# @Author  : RooFTOooOP
# @FileName: SocketServer时间戳TCP客户端.py
# @Software: PyCharm


from socket import *
'''
作用：时间戳TCP客户端。
'''
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

'''
函数解析：
    1；Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
'''
while True:
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    # data = data.encode()

    if not data:
        break
    tcpCliSock.sendall((data + '\n').encode())
    #tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode().strip())
    tcpCliSock.close()