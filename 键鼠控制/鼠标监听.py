# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pynput import mouse


# 鼠标移动事件
def on_move(x, y):
    print('[Move]', (x, y))


# 鼠标点击事件
def on_click(x, y, button, pressed):
    print('[Click]', (x, y, button.name, pressed))


# 鼠标滚动事件
def on_scroll(x, y, x_axis, y_axis):
    print('[Scroll]', (x, y, x_axis, y_axis))


# 监听事件绑定
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
