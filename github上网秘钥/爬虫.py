#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 15:17
# @Author  : RooFTOooOP
# @FileName: 爬虫.py
# @Software: PyCharm

import requests  # 用于向网站发送请求
import re  # lxml为第三方网页解析库，强大且速度快


class GetIp(object):
    def __init__(self):
        self.github_url = 'https://websites.ipaddress.com/github.com'
        self.ssl_url = 'https://websites.ipaddress.com/github.global.ssl.fastly.net'
        self.asset_url = 'https://websites.ipaddress.com/assets-cdn.github.com'
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko)\
                           Chrome/81.0.4044.129 Safari/537.36",
        }

    # github网址ip
    def getaddress(self):
        response = requests.get(self.github_url, headers=self.headers, timeout=10)
        html = response.text

        pattern = re.compile('<ul class="comma-separated"><li>.*?</li></ul>')
        result = re.search(pattern, html)

        res = re.search('<li>.*?</li>', result.group())
        return res.group()[4:-5]

    # github域名ip
    def getssl(self):
        response = requests.get(self.ssl_url, headers=self.headers, timeout=10)
        html = response.text

        pattern = re.compile('<ul class="comma-separated"><li>.*?</li></ul>')
        result = re.search(pattern, html)

        res = re.search('<li>.*?</li>', result.group())
        return res.group()[4:-5]

    # github静态ip
    def getasset(self):
        response = requests.get(self.asset_url, headers=self.headers, timeout=10)
        html = response.text

        pattern = re.compile('<ul class="comma-separated"><li>.*?</li></ul>')
        result = re.findall(pattern, html)
        result = ''.join(result[0:2])
        res = re.findall('<li>.*?</li>', result)
        asset = []
        for r in res:
            asset.append(r[4:-5])
        return asset


with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'r', encoding='utf-8') as f:
    text = f.readlines()

git_id = []
for i in range(len(text)):
    if 'github' in text[i] or 'Github' in text[i]:
        git_id.append(i)
git_id.sort(reverse=True)
for i in git_id:
    text.pop(i)

getip = GetIp()
address = getip.getaddress()
ssl = getip.getssl()
asset = getip.getasset()

git_ip = ['\n', '# Github start\n', address + '	github.com\n', ssl + '	github.global.ssl.fastly.net\n']
for a in asset:
    git_ip.append(a + '	assets-cdn.github.com\n')
git_ip.append('# Github end\n')

text.extend(git_ip)

with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'w', encoding='utf-8') as f1:
    f1.writelines(text)
