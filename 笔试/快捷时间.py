from pynput.keyboard import Listener, Key, Controller
# import logging
import win32clipboard as w
import time
import requests


def download_page(url):
   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
   r = requests.get(url, headers=headers)  # 增加headers, 模拟浏览器
   return r.text.replace('<br />','')+"\r \n"


def setClipboard(aString):  # 写入剪切板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(aString)
    w.CloseClipboard()


def printtoboard(string):
    setClipboard(str(string))
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    # 延时10毫秒
    time.sleep(0.005)
    keyboard.release(Key.ctrl)
    keyboard.release('v')


def timeinitial():
    time_1 = time.time()
    seconds = time_1 - time_0 + 300
    m, s = divmod(seconds, 60)
    m = int(m)
    s = int(s)
    if m < 10:
        minute = '0' + str(m)
    else:
        minute = str(m)
    if s < 10:
        sec = '0' + str(s)
    else:
        sec = str(s)
    string0 = minute + ':' + sec
    return string0


def press(key):
    try:
        print(key.char)
        if key.char == ',':
            print('进来了  --  ')
            string = '上单闪现' + '->' + timeinitial()
            printtoboard(string)
        if key.char == '.':
            print('进来了  --  ')
            string = '中路闪现' + '->' + timeinitial()
            printtoboard(string)
        if key.char == '/':
            print('进来了  --  ')
            string = '打野闪现' + '->' + timeinitial()
            printtoboard(string)
        if key.char == ';':
            print('进来了  --  ')
            string = 'ad闪现' + '->' + timeinitial()
            printtoboard(string)
        if key.char == "'":
            print('进来了  --  ')
            string = '辅助闪现' + '->' + timeinitial()
            printtoboard(string)
        if key.char == '-':
            print('进来了  --  ')
            url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'
            html = download_page(url)
            string = html
            printtoboard(string)
    except Exception as e:
        pass


def on_release(key):
    try:
        if key.char == '=':
            print(f'{key} 被释放了')
            return False
    except Exception as e:
        pass


number = 0


while number < 10:
    time_0 = time.time()
    with Listener(on_press=press, on_release=on_release) as listener:
        listener.join()
    number += 1
