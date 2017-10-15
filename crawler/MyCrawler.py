import asyncio
import cgi
from collections import namedtuple
import logging
import re
import time
import urllib.parse
try:
    # Python 3.4.
    from asyncio import JoinableQueue as Queue
except ImportError:
    # Python 3.5.
    from asyncio import Queue

import aiohttp  # Install with "pip install aiohttp".

LOGGER = logging.getLogger(__name__)


class Crawler:
    def __init__(self, root_url, max_redirect, *, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self.max_tasks = 10
        self.url = root_url
        self.max_redirect = max_redirect
        self.q = Queue(loop=self.loop)
        self.seen_urls = set()
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.q.put_nowait((self.url, self.max_redirect))
        print('init:', self.q.qsize())

    async def fetch(self, url, sem=asyncio.Semaphore(100)):
        print('fetch:', self.url)
        async with self.session.get(url) as resp:
            print(resp.status)
            return 'Done'

    async def crawl(self):
        print('crawler:', self.url)
        tasks = [
            asyncio.Task(self.work(), loop=self.loop)
            for _ in range(self.max_tasks)
        ]
        # await asyncio.wait(tasks)
        await asyncio.sleep(1)
        for w in tasks:
            w.cancel()
        self.session.close()

    async def work(self):
        print('work')
        try:
            while True:
                if self.q.qsize() > 0:
                    print('work:', self.url)
                    url, max_redirect = await self.q.get()
                    await self.fetch(url, max_redirect)
                    self.q.task_done()
                else:
                    break
        except asyncio.CancelledError:
            pass

# asyncio.get_event_loop()默认本线程中的所有协程都会添加到loop中,
# 但是在主要的线程执行过程中需要使用至少一次await才会执行其他的协程
# The default policy defines context as the current thread, 
# and manages an event loop per thread that interacts with asyncio
# Get the event loop for the current context.
loop = asyncio.get_event_loop()
crawler = Crawler('https://www.baidu.com', max_redirect=10)
future = asyncio.ensure_future(crawler.crawl())
loop.run_until_complete(future)