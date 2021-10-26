import requests, time, os, datetime, random
from bs4 import BeautifulSoup
from multiprocessing import Process

# import asyncio
# import logging
# from datetime import datetime
# from aiowebsocket.converses import AioWebSocket

# async def startup(uri):
	# async with AioWebSocket(uri) as aws:
		# converse = aws.manipulator
		# # 客户端给服务端发送消息
		# await converse.send("createOrder"+"000000255372")#('{"action":"subscribe","args":["QuoteBin5m:14"]}')
		# while True:
			# mes = await converse.receive()
			# print('{time}-Client receive: {rec}'
				  # .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes.decode("utf8")))

# async def run(remote = 'ws://202.117.17.144:8887'):
	# try:
		# asyncio.get_event_loop().run_until_complete(startup(remote))
	# except KeyboardInterrupt as exc:
		# logging.info('Quit.')
	# loop = asyncio.get_event_loop()
	# await startup(remote)
				  
UA_header = {"User-Agent": "Mozilla/5.0 (Linux; Android 9; MI 8 SE Build/PKQ1.181121.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 toon/1909121424 toonType/1 toonVersion/6.1.0 toongine/1.0.8 toongineBuild/8 platform/android language/zh skin/white fontIndex/0",}

def login(s, UA_header=UA_header):
	header = {
	#     "User-Agent": "Mozilla/5.0 (Linux; Android 9; MI 8 SE Build/PKQ1.181121.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 toon/1909121424 toonType/1 toonVersion/6.1.0 toongine/1.0.8 toongineBuild/8 platform/android language/zh skin/white fontIndex/0",
		"User-Agent":"ok",
		"secretKey": "18a9d512c03745a791d92630bc0888f6",
	#     "deviceId":"cc5676d6-dfb3-4a19-94e3-897901978967",
	#     "Authorization":"7e3d55d0-deca-4ff9-8a1b-7a43fb250ec4",
	#     "platform": "android",
	#     "platformVersion": "28",
	#     "appVersion": "6.1.0",
	#     "toonType": "150",
		"X-Toon-User-Agent": "platform:android,appVersion:6.1.0,toonType:150,deviceId:cc5676d6-dfb3-4a19-94e3-897901978967",
	}
	print(s.cookies)
	response = s.get("http://org.xjtu.edu.cn/openplatform/toon/auth/generateTicket?personToken=7e3d55d0-deca-4ff9-8a1b-7a43fb250ec4&empNo=3118101076", headers=header)
	print(response.status_code, "\n", response.json())
	print(s.cookies)
	response = s.get("http://org.xjtu.edu.cn//workbench/member/appNew/getOauthCode?userId=718104&orgId=1000&appId=760&state=2222&redirectUri=http%3A%2F%2F202.117.17.144%3A8080%2Fweb%2Findex.html?userType=1&employeeNo=3118101076&personToken=7e3d55d0-deca-4ff9-8a1b-7a43fb250ec4",
					 headers=UA_header)
	print(response.status_code)
	print(s.cookies)
	return s

def book_area(post_data):
#     post_data = """param={"stockdetail":{%s}}&json=true"""%stockdetail#"""param={"stockdetail":{"39206":"949447","39205":"949440,949441"}}&json=true"""
	headers = {
		"Host": "202.117.17.144:8080",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Connection": "keep-alive",
		"X-Requested-With": "XMLHttpRequest",
		"Referer": "http://202.117.17.144:8080/web/product/show.html?id=103",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
		"User-Agent": "Mozilla/5.0 (Linux; Android 9; MI 8 SE Build/PKQ1.181121.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 toon/1909121424 toonType/1 toonVersion/6.1.0 toongine/1.0.8 toongineBuild/8 platform/android language/zh skin/white fontIndex/0",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	}

	book_url = "http://202.117.17.144:8080/web/order/tobook.html"
	response = s.post(book_url, headers=headers, data=post_data)
	print(response.status_code, "\n", response.json())
	
if __name__ == '__main__':
	remote = 'ws://202.117.17.144:8887'
	s = requests.Session()
	
	while True:
		date_today = datetime.datetime.now()
		if date_today.second % 30 == 0:
			print(date_today.strftime("%Y-%m-%d %H:%M:%S"))
		time.sleep(1)
		
		date_query = date_today + datetime.timedelta(4)
		date_query_str = '{}-{}-{} 06:59:59'.format(date_query.year, date_query.month, date_query.day)
		date_query_struct = datetime.datetime.strptime(date_query_str, "%Y-%m-%d %H:%M:%S")
		if date_query >= date_query_struct and date_query.hour <= 15:
			print("时间到", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "预定日期：", date_query_str)
			
			# 检查电脑能否联网
			while os.system("ping www.baidu.com -n 1"):
				print("无法访问百度，网络有问题！")
			
			# 多进程 Websocket
			print('Parent process %s.' % os.getpid())
			p = Process(target=os.system, args=("python async_websocket.py",))
			# p = Process(target=run, args=(remote,))
			print('Child process will start.')
			p.start()
			
			while True:
				
				# 捕捉服务器无法连接的异常
				try:
					response = s.get("http://202.117.17.144:8080/web/product/show.html?id=103", headers=UA_header, )
				except Exception as e:
					print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "发生错误：", e)
					continue
				soup = BeautifulSoup(response.text, "lxml")
				if soup.find(attrs={"id":"userno"})["value"]:
					print("暂未掉线！", soup.find(attrs={"id":"userno"})["value"])
				else:
					print("已掉线，尝试重新登录ing！")
					s = login(s)

				#  可用场地获取
				# date_query = '2019-12-14'
				data_url = "http://202.117.17.144:8080/web/product/findOkArea.html?s_date=%s&serviceid=103"%date_query_str[:10]
				response = requests.get(data_url, headers=UA_header)
				data_json = response.json()
				print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "可用场地共有%s个！"%len(data_json["object"]))
				
				
				areas = []
				for _item in data_json["object"]:
					if _item["sname"] not in ["场地3", "场地4"]:#, "场地4"
						continue
					time_no = _item["stock"]["time_no"]
					if "20" in time_no or "22" in time_no:
						post_data = """param={"stockdetail":{"%s":"%s"}}&json=true"""%(_item["stockid"], _item["id"])
						book_area(post_data)
						time.sleep(random.random()/5)
						areas.append([str(_item["stockid"]), str(_item["id"])])

				if len(areas) == 0:
					print("好场地已被约完！")
					break
					
			p.terminate()
			time.sleep(1)
			print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "进程状态为：%s"%(p.is_alive()))
			break