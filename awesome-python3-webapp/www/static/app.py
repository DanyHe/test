import logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time  #asyncio是python引入的标准库，内置了对异步IO的支持；从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome')  #b加粗  h1第一标题，字的格式

@asyncio.coroutine  #把一个generate标记为coroutine类型，把这个coroutine扔到EventLoop中执行
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000')
    return srv
loop = asyncio.get_event_loop()  #获取EventLoop
loop.run_until_complete(init(loop))  #执行coroutine
loop.run_forever()