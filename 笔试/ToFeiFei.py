# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=ZjRPEXoe5X01yvcMgVYu1U5s&client_secret=Trhdsb8BuSqq80St5SRoTmObTtX43RFe'
response = requests.get(host)
if response:
    print(response.json())
