from pynput.keyboard import Listener, Key, Controller
# import logging
import win32clipboard as w
# import win32con
import time
import requests


# wenjianweizhi = "D:\\hi\\"

# logging.basicConfig(filename=(wenjianweizhi + "keylogger.txt"), format="%(asctime)s:%(message)s", level=logging.DEBUG)

def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)  # 增加headers, 模拟浏览器
    return r.text.replace('<br />', '') + "\r \n"


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


# def timeinitial(c):
#     time0 = time.time()


def press(key):
    try:
        print(key.char)
        if key.char == '-':
            print('进来了  --  ')
            url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'
            html = download_page(url)
            second = 0



            m, s = divmod(seconds, 60)
            # 在这里调接口，将数据写进剪贴板，然后模拟键盘的粘贴（Ctrl + V）
            setClipboard(str(html))
            keyboard = Controller()
            keyboard.press(Key.ctrl)
            keyboard.press('v')
            # 延时10毫秒
            time.sleep(0.01)
            keyboard.release(Key.ctrl)
            keyboard.release('v')


    except Exception as e:
        print("已调到该程序，但是引用报错", e)


with Listener(on_press=press) as listener:
    listener.join()