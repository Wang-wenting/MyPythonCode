#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 16:04
# @Author  : RooFTOooOP
# @FileName: 鼠标录制回放.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xc_zhou/article/details/91484052

import json
import threading
import time
import tkinter

from pynput import mouse
from pynput.mouse import Button, Controller


# 鼠标动作模板
def mouse_action_template():
    return {
        "name": "mouse",
        "event": "default",
        "target": "default",
        "action": "default",
        "location": {
            "x": "0",
            "y": "0"
        }
    }


# 鼠标动作监听
class MouseActionListener(threading.Thread):

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def run(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            # 鼠标移动事件
            def on_move(x, y):
                template = mouse_action_template()
                template['event'] = 'move'
                template['location']['x'] = x
                template['location']['y'] = y
                file.writelines(json.dumps(template) + "\n")
                file.flush()

            # 鼠标点击事件
            def on_click(x, y, button, pressed):
                template = mouse_action_template()
                template['event'] = 'click'
                template['target'] = button.name
                template['action'] = pressed
                template['location']['x'] = x
                template['location']['y'] = y
                file.writelines(json.dumps(template) + "\n")
                file.flush()

            # 鼠标滚动事件
            def on_scroll(x, y, x_axis, y_axis):
                template = mouse_action_template()
                template['event'] = 'scroll'
                template['location']['x'] = x_axis
                template['location']['y'] = y_axis
                file.writelines(json.dumps(template) + "\n")
                file.flush()

            with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
                listener.join()


# 鼠标动作执行
class MouseActionExecute(threading.Thread):

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def run(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            mouse_exec = Controller()
            line = file.readline()
            time.sleep(0.01)
            while line:
                obj = json.loads(line)
                if obj['name'] == 'mouse':
                    if obj['event'] == 'move':
                        mouse_exec.position = (obj['location']['x'], obj['location']['y'])
                        time.sleep(0.01)
                    elif obj['event'] == 'click':
                        if obj['action']:
                            if obj['target'] == 'left':
                                mouse_exec.press(Button.left)
                            else:
                                mouse_exec.press(Button.right)
                        else:
                            if obj['target'] == 'left':
                                mouse_exec.release(Button.left)
                            else:
                                mouse_exec.release(Button.right)
                        time.sleep(0.01)
                    elif obj['event'] == 'scroll':
                        mouse_exec.scroll(obj['location']['x'], obj['location']['y'])
                        time.sleep(0.01)
                line = file.readline()


def button_onclick(action):

    m1 = MouseActionListener(file_name='mouse.action')
    m2 = MouseActionExecute(file_name='mouse.action')

    if action == 'listener':
        if startListenerBtn['text'] == '录制':
            m1.start()
            startListenerBtn['text'] = '录制中...关闭程序停止录制'
            startListenerBtn['state'] = 'disabled'

    elif action == 'execute':
        if startExecuteBtn['text'] == '回放':
            m2.start()
            startExecuteBtn['text'] = '回放中...关闭程序停止回放'
            startExecuteBtn['state'] = 'disabled'


if __name__ == '__main__':

    root = tkinter.Tk()
    root.title('鼠标精灵-蓝士钦')
    root.geometry('200x200+400+100')

    startListenerBtn = tkinter.Button(root, text="录制", command=lambda: button_onclick('listener'))
    startListenerBtn.place(x=10, y=10, width=180, height=80)

    startExecuteBtn = tkinter.Button(root, text="回放", command=lambda: button_onclick('execute'))
    startExecuteBtn.place(x=10, y=110, width=180, height=80)
    root.mainloop()
