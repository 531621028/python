#coding:utf-8
__author__ = 'hukangkang'

import asyncio
import os
import inspect
import logging
import functools
from urllib import parse
from aiohttp import web


# 3层嵌套的效果是这样的：now = log('execute')(now)
def get(path):
    '''Define decorator @get('/path')'''

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        wrapper.__method__ = 'GET'
        wrapper.__route__ = 'path'
        return wrapper

    return decorator


def post(path):
    '''Define decorator @get('/path')'''

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        wrapper.__method__ = 'POST'
        wrapper.__route__ = 'path'
        return wrapper

    return decorator


def get_required_kw_args(fn):
    '''
    获取fn中的命令关键字并且没有默认值的参数名称并以元组的形式返回
    '''
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if (param.kind == inspect.Parameter.KEYWORD_ONLY and
                param.default == inspect.Parameter.empty):  # 命令关键字参数并且没有默认值
            args.append(name)
    return tuple(args)


def get_named_kw_args(fn):
    '''
    获取fn中的命令关键字参数的名称并以元组的形式返回
    '''
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:  # 命令关键字
            args.append(name)
    return tuple(args)


def has_named_kw_args(fn):
    '''
    判断fn函数中是否有命名关键字参数
    有则返回True
    '''
    params = inspect.signature(fn).parameters
    for name, param in params.itmes():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:  # 命令关键字参数
            return True


def has_var_kw_arg(fn):
    '''
    判断fn函数中是否有关键字参数
    有则返回True
    '''
    params = inspect.signature(fn).parameters
    for name, param in params.itmes():
        if param.kind == inspect.Parameter.VAR_KEYWORD:  # 关键字参数
            return True


def has_request_arg(fn):
    '''
    判断fn函数中的位置参数或者默认参数中是否含有名为request的参数
    有则返回True
    '''
    # 提取函数签名inspect.signature(fn)
    sig = inspect.signature(fn)
    # 获取函数中的参数信息
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == 'request':
            found = True
            continue
        '''
        如果要限制关键字参数的名字，就可以用命名关键字参数
        关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，
        *后面的参数被视为命名关键字参数person(name, age, *, city, job)
        city，job为命名关键字参数
        如果函数定义中已经有了一个可变参数，
        后面跟着的命名关键字参数就不再需要一个特殊分隔符*了

        POSITIONAL_OR_KEYWORD 位置参数或者默认参数
        VAR_POSITIONAL 可变参数
        KEYWORD_ONLY 命令关键字
        VAR_KEYWORD 关键字参数
        '''
        if found and (param.kind != inspect.Parameter.VAR_POSITIONAL
                      and param.kind != inspect.Parameter.KEYWORD_ONLY
                      and param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError(
                'request parameter must be the last named parameter in function: {}{}'.
                format(fn.__name__, str(sig)))
    return found


class RequestHandler(object):
    '''
    A request handler can be any callable 
    that accepts a Request instance as its only 
    argument and returns a StreamResponse 
    derived (e.g. Response) instance:
    '''

    def __init__(self, app, fn):
        self._app = app
        self._func = fn
        self._has_request_arg = has_request_arg(fn)
        self._has_var_kw_arg = has_var_kw_arg(fn)
        self._has_named_kw_args = has_named_kw_args(fn)
        self._named_kw_args = get_named_kw_args(fn)
        self._required_kw_args = get_required_kw_args(fn)

    def __call__(self, request):
        kw = None
        if self._has_var_kw_arg or self._has_named_kw_args:
            pass


def add_routes(app, modules_name):
    n = modules_name.rfind('.')
    # 根据modules_name导入指定的模块并赋值给mod
    if n == (-1):
        mod = __import__(modules_name, globals(), locals())
    else:
        name = modules_name[n + 1:-1]
        # getattr(module,function_name)获取module中指定函数
        mod = getattr(__import__(modules_name, globals(), locals()), name)
    # 使用dir()函数可以查看对像内所有属于及方法
    for attr in dir(mod):
        if attr.startswith('_'):
            continue
        fn = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__route__', None)
            if method and path:
                add_route(app, fn)


def add_route(app, fn):
    method = getattr(fn, '__method__', None)
    path = getattr(fn, '__route__', None)
    if path is None or method is None:
        raise ValueError('@get or @post not defined in ().'.format(str(fn)))
    if not asyncio.iscoroutinefunction(fn) and inspect.isasyncgenfunction(fn):
        fn = asyncio.coroutine(fn)
    logging.info('add route {} {} => {}({})'.format(
        method, path, fn.__name__, ', '.join(
            inspect.signature(fn).parameters.keys())))
    app.router.add_route(method, path, RequestHandler(app, fn))