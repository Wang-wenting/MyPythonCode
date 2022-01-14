#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/18 17:12
# @Author  : RooFTOooOP
# @FileName: TCP时间戳服务器.py
# @Software: PyCharm


from socket import *
from time import ctime

HOST = ''  # 主机地址
PORT = 21567  # 端口号
BUFSIZ = 1024  # 缓存区大小，单位是字节，这里设定了1K的缓冲区
ADDR = (HOST, PORT)  # 链接地址

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建一个TCP套接字
tcpSerSock.bind(ADDR)  # 绑定地址
tcpSerSock.listen(5)  # 最大连接数为5

try:
    while True:
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()  # 等待接受连接
        print('...connect from:', addr)

        while True:
            data = tcpCliSock.recv(BUFSIZ)  # 接收数据,BUFSIZ是缓存区大小
            if not data:
                break
            msg = '%s %s' % (ctime(), data.decode())
            print(msg)
            tcpCliSock.send(msg.encode())

        tcpCliSock.close()  # 关闭连接
except Exception as e:
    print('服务器关机', e)
    tcpSerSock.close()  # 关闭服务器
