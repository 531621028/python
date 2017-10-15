#coding:utf-8

import asyncio
import aiohttp
try:
    from asyncio import JoinableQueue as Queue
except ImportError:
    # In Python 3.5, asyncio.JoinableQueue is
    # merged into Queue.
    from asyncio import Queue

class Crawler:
    def __init__(self, root_url, max_redirect):
        self.max_tasks = 10
        self.max_redirect = max_redirect
        self.q = Queue()
        self.seen_urls = set()

        # aiohttp's ClientSession does connection pooling and
        # HTTP keep-alives for us.
        self.session = aiohttp.ClientSession(loop=loop)

        # Put (URL, max_redirect) in the queue.
        self.q.put((root_url, self.max_redirect))


        
    @asyncio.coroutine
    def crawl(self):
        """Run the crawler until all work is done."""
        workers = [asyncio.Task(self.work())
                   for _ in range(self.max_tasks)]

        # When all work is done, exit.
        yield from self.q.join()
        for w in workers:
            w.cancel()
    #Python sees that this code contains yield from statements, 
    #and compiles it into a generator function. 
    #So in crawl, when the main coroutine calls self.work ten times, 
    #it does not actually execute this method: it only creates ten generator objects with references to this code.

    @asyncio.coroutine
    def work(self):
        while True:
            url, max_redirect = yield from self.q.get()
            # Download page and add new links to self.q.
            yield from self.fetch(url, max_redirect)
            self.q.task_done()



loop = asyncio.get_event_loop()

crawler = Crawler('http://xkcd.com',max_redirect=10)
loop.run_until_complete(crawler.crawl())