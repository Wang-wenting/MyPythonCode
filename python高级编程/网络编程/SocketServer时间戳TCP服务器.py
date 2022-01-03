#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/20 21:22
# @Author  : RooFTOooOP
# @FileName: SocketServer时间戳TCP服务器.py
# @Software: PyCharm
# @Blog: https://www.cnblogs.com/aaron456-rgv/p/12508769.html


from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime
'''
作用：通过使用SocketServer类，TCPServer 和 StreamRequestHandler ,该脚本创建了一个时间戳TCP服务器
'''

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

'''
函数解析：
    1；readline()方法每次读取一行；返回的是一个字符串对象，保持当前行的内存
    2；write() 方法用于向文件中写入指定字符串
    3；wfile不缓冲数据,对客户端发送的数据需一次性写入
    4；client_address:一个包含两个成员（主机名和端口）的数组，服务端输出的任何数据都将通过它们发送
'''


class MyRequestHandler(SRH):
    def handle(self):
        print("...connected from:", self.client_address)
        # self.request.send(('[%s] %s' % (ctime(), self.request.recv(1024).decode())).encode())
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline().decode())).encode())

# 利用给定的主机信息和请求处理类创建TCP服务器
tcpServ = TCP(ADDR, MyRequestHandler)
print("waiting for connection...")
tcpServ.serve_forever()