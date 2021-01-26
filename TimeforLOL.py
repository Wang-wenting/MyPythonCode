from pynput.keyboard import Listener, Key, Controller
# import logging
import win32clipboard as w
# import win32con
import time


# import requests


# wenjianweizhi = "D:\\hi\\"

# logging.basicConfig(filename=(wenjianweizhi + "keylogger.txt"), format="%(asctime)s:%(message)s", level=logging.DEBUG)

# def download_page(url):
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
#     r = requests.get(url, headers=headers)  # 增加headers, 模拟浏览器
#     return r.text.replace('<br />', '') + "\r \n"


# def getClipboard():#读取剪切板
#     w.OpenClipboard()
#     d = w.GetClipboardData(win32con.CF_TEXT)
#     w.CloseClipboard()
#     return d
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
    time.sleep(0.001)
    keyboard.release(Key.ctrl)
    keyboard.release('v')


def timeinitial():
    time_1 = time.time()
    seconds = time_1 - time_0 + 300

    m, s = divmod(seconds, 60)
    m = int(m)
    s = int(s)
    # 在这里调接口，将数据写进剪贴板，然后模拟键盘的粘贴（Ctrl + V）
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
            # url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'
            # html = download_page(url)
            string = '上单闪现' + '->' + timeinitial()
            printtoboard(string)
        if key.char == '.':
            print('进来了  --  ')
            # url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'
            # html = download_page(url)
            string = '中路闪现' + '->' + timeinitial()
            printtoboard(string)
        if key.char == '/':
            print('进来了  --  ')
            # url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'
            # html = download_page(url)
            string = '打野闪现' + '->' + timeinitial()
            printtoboard(string)
        if key.char == ';':
            print('进来了  --  ')
            # url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'
            # html = download_page(url)
            string = 'ad闪现' + '->' + timeinitial()
            printtoboard(string)
        if key.char == "'":
            print('进来了  --  ')
            # url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'
            # html = download_page(url)
            string = '辅助闪现' + '->' + timeinitial()
            printtoboard(string)

    except Exception as e:
        print("已调到该程序，但是引用报错", e)


time_0 = time.time()

with Listener(on_press=press) as listener:
    listener.join()
