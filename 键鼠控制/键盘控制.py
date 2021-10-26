#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 16:10
# @Author  : RooFTOooOP
# @FileName: 键盘控制.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xc_zhou/article/details/91484052

from pynput.keyboard import Key, Controller, KeyCode

# 键盘控制对象
keyboard = Controller()

# 按下 a 键
# keyboard.press('a')
# # 释放 a 键+！
# keyboard.release('a')
#
# # 按下 Shift 键
# keyboard.press(Key.shift)
# keyboard.press('b')
# keyboard.release('b')
# keyboard.press('c')
# keyboard.release('c')
# # 释放 Shift 键
# keyboard.release(Key.esc)

# 按下 Shift 键，然后依次按下其他按键，完成后Shift键自动释放
with keyboard.pressed(Key.shift):
    keyboard.press('=')
    keyboard.release('=')
keyboard.press('1')
keyboard.release('1')

# 依次按下 python （包括前面的空格）
keyboard.type(' python')

# # 按下 vk值为56的键 shift 键
# keyboard.touch(KeyCode.from_vk(56), True)
# keyboard.touch('a', True)
# keyboard.touch('a', False)
# # 释放 shift 键
# keyboard.touch(Key.shift, False)
