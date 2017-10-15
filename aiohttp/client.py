import asyncio
from datetime import datetime

import aiohttp
import requests
from aiohttp import ClientSession

r = 100


# async def hello(url, i):
#     async with ClientSession() as session:
#         async with session.get(url.format(i)) as response:
#             response = await response.read()
#             print(response)

# loop = asyncio.get_event_loop()
# tasks = []  # I'm using test server localhost, but you can use any url
# url = "http://localhost:8080/{}"
# start = datetime.now()
# for i in range(r):
#     task = asyncio.ensure_future(hello(url, i))
#     tasks.append(task)
# loop.run_until_complete(asyncio.wait(tasks))
# print(datetime.now() - start)
async def fetch(session, url, sem=asyncio.Semaphore(100)):
# async def fetch(session, url):
    # async with ClientSession() as session:
    async with sem:
        async with session.get(url) as response:
            delay = response.headers.get("DELAY")
            d = response.headers.get("DATE")
            print("{}:{} delay {}".format(d, response.url, delay))
            return await response.read()


async def run(r):
    url = "http://httpbin.org/{}"
    # url = "http://localhost:8080/{}"
    tasks = []
    sem = asyncio.Semaphore(100)
    async with ClientSession() as session:
        for i in range(r):
            # pass Semaphore to every GET request
            task = asyncio.ensure_future(fetch(session, url.format(i), sem))
            # task = asyncio.ensure_future(bound_fetch(sem, session, url.format(i)))
            tasks.append(task)
            # you now have all response bodies in this variable
        # responses = await asyncio.gather(*tasks)
        responses = await asyncio.gather(*tasks)
        print(responses)


loop = asyncio.get_event_loop()
start = datetime.now()
future = asyncio.ensure_future(run(r))
loop.run_until_complete(future)
print(datetime.now() - start)

# url = "http://localhost:8080/{}"
# start = datetime.now()
# for i in range(r):
#     res = requests.get(url.format(i))
#     delay = res.headers.get("DELAY")
#     d = res.headers.get("DATE")
#     print("{}:{} delay {}".format(d, res.url, delay))
# print(datetime.now() - start)
