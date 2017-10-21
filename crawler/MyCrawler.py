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

headers = {
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":
    "gzip, deflate",
    "Accept-Language":
    "zh-CN,zh;q=0.8",
    "Connection":
    "close",
    "Cookie":
    "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Host":
    "httpbin.org",
    "Upgrade-Insecure-Requests":
    "1",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}


class Crawler:
    def __init__(self,
                 root_url,
                 max_redirect=10,
                 max_tasks=10,
                 max_tries=3,
                 *,
                 loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self.max_tasks = max_tasks
        self.url = root_url
        self.max_redirect = max_redirect
        self.max_tries = max_tries
        self.q = Queue(loop=self.loop)
        self.seen_urls = set()
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.q.put_nowait((self.url, self.max_redirect))
        print('init:', self.q.qsize())

    async def fetch(self, url, sem=asyncio.Semaphore(100)):
        tries = 0
        # exception = None
        while tries < self.max_tries:
            try:
                resp = await self.session.get(url)
                if tries > 1:
                    LOGGER.info('try {} for {} success'.format(tries, url))
                break
            except aiohttp.ClientError as error:
                LOGGER.info(
                    'try {} for {} raised {}'.format(tries, url, error))
                # exception = error
            tries += 1
        else:
            LOGGER.error(
                '{} failed after {} tries'.format(url, self.max_tries))
            return
        links = await self.parse_links(resp)

    async def parse_links(self, resp):
        # links = set()
        content_type = None
        encoding = None
        body = await resp.read()

        if resp.status == 200:
            content_type = resp.headers.get('content-type')
            pdict = {}

            if content_type:
                content_type, pdict = cgi.parse_header(content_type)

            # encoding = pdict.get('charset', 'utf-8')
            if content_type in ('text/html', 'application/xml'):
                text = await resp.text()
                # with open('html.html','wt',encoding=encoding) as f:
                #     f.write(text)
                urls = set(re.findall(r'''(?i)href=["']([^\s"'<>]+)''', text))
                if urls:
                    LOGGER.info('got {} distinct urls from {}'.format(
                        len(urls), resp.url))
                    print('got {} distinct urls from {}'.format(
                        len(urls), resp.url))
                # for url in urls:
                #     if not url.startswith('http'):
                #         normalized = urllib.parse.urljoin(response.url, url)
                #     else:
                #         normalized = url
                #     defragmented, frag = urllib.parse.urldefrag(normalized)
                #     if self.url_allowed(defragmented):
                #         links.add(defragmented)
        return urls

    async def crawl(self):
        tasks = [
            asyncio.ensure_future(self.work(), loop=self.loop)
            for _ in range(self.max_tasks)
        ]
        # await asyncio.wait(tasks)
        await asyncio.sleep(1)
        for w in tasks:
            w.cancel()
        self.session.close()

    async def work(self):
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
crawler = Crawler('http://www.baidu.com', max_redirect=10)
future = asyncio.ensure_future(crawler.crawl())
loop.run_until_complete(future)