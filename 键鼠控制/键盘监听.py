#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 16:10
# @Author  : RooFTOooOP
# @FileName: 键盘监听.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xc_zhou/article/details/91484052

from pynput import keyboard


# 按键按下监听
def on_press(key):
    try:
        print('press key {0}, vk: {1}'.format(key.char, key.vk))
    except AttributeError:
        print('special press key {0}, vk: {1}'.format(key, key.value.vk))


# 按键释放监听
def on_release(key):

    if key == keyboard.Key.esc:
        # 停止监听
        return False

    try:
        print('release key {0}, vk: {1}'.format(key.char, key.vk))
    except AttributeError:
        print('special release key {0}, vk: {1}'.format(key, key.value.vk))


# 键盘监听
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
