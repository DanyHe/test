import logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time  #asyncio��python����ı�׼�⣬�����˶��첽IO��֧�֣���asyncioģ����ֱ�ӻ�ȡһ��EventLoop�����ã�Ȼ�����Ҫִ�е�Э���ӵ�EventLoop��ִ�У���ʵ�����첽IO
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome')  #b�Ӵ�  h1��һ���⣬�ֵĸ�ʽ

@asyncio.coroutine  #��һ��generate���Ϊcoroutine���ͣ������coroutine�ӵ�EventLoop��ִ��
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000')
    return srv
loop = asyncio.get_event_loop()  #��ȡEventLoop
loop.run_until_complete(init(loop))  #ִ��coroutine
loop.run_forever()