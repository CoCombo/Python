import logging; logging.basicConfig(level = logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>Fuck</h1>')

@asyncio.coroutine
def init(loop):
	app = web.Application
