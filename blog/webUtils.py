#coding:utf-8
__author__ = 'hukangkang'

import asyncio, os, inspect, logging, functools
from urllib import parse
from aiohttp import web


#3层嵌套的效果是这样的：now = log('execute')(now)
def get(path):
    pass