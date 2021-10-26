#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 16:02
# @Author  : RooFTOooOP
# @FileName: 鼠标控制.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41800366

from pynput.mouse import Button, Controller
import time

# 获取鼠标对象
mouse = Controller()

# 输出鼠标当前的坐标
print(mouse.position)

# 将新的坐标赋值给鼠标对象
mouse.position = (100, 500)

for index in range(0, 30):
    # 鼠标移动到指定坐标轴
    mouse.move(index, -index)
    print(mouse.position)
    time.sleep(0.01)

for index in range(0, 30):
    # 鼠标移动到指定坐标轴
    mouse.move(-index, index)
    print(mouse.position)
    time.sleep(0.01)

# 鼠标右键按下
mouse.press(Button.right)

time.sleep(0.01)

# 鼠标右键抬起
mouse.release(Button.right)

# 鼠标左键点击
mouse.click(Button.left, 1)

# 鼠标滚轮滚动距离500
mouse.scroll(0, 500)
