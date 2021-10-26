import asyncio
import logging
from datetime import datetime
from aiowebsocket.converses import AioWebSocket

async def startup(uri):
	async with AioWebSocket(uri) as aws:
		converse = aws.manipulator
		# 客户端给服务端发送消息
		await converse.send("createOrder"+"000000255372")#
		while True:
			mes = await converse.receive()
			print('{time}-Client receive: {rec}'
				  .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes.decode("utf8")))

def run():
	remote = 'ws://202.117.17.144:8887'
	try:
		asyncio.get_event_loop().run_until_complete(startup(remote))
		# loop = asyncio.get_event_loop()
		# await startup(remote)
	except RuntimeError as e:
		print("RuntimeError", e)
	except KeyboardInterrupt as exc:
		logging.info('Quit.')
		
if __name__ == '__main__':
	remote = 'ws://202.117.17.144:8887'
	try:
		asyncio.get_event_loop().run_until_complete(startup(remote))
	except KeyboardInterrupt as exc:
		logging.info('Quit.')
	