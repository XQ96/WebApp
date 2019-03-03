# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/3 12:10
# @File:coroweb.py

import asyncio,os,inspect,logging,functools
from urllib import parse
from aiohttp import web
from api import APIError

def get(path):
    '''
    Define decorator @get('/path')
    :param path:
    :return:
    '''

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            return func(*args,**kw)
        wrapper.__method__='GET'
        wrapper.__route__=path
        return wrapper
    return decorator

def post(path):
    '''
    Define decorator @post('/path')
    :param path:
    :return:
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            return func(*args,**kw)
        wrapper.__method__='POST'
        wrapper.__route__=path
        return wrapper
    return decorator
#获取各种参数
def get_required_kw_args(fn):
    args=[]
    params=inspect.signature(fn).parameters
    for name,param in params.items():
        if param.kind==inspect.Parameter.KEYWORD_ONLY and param.default==inspect.Parameter.empty:
            args.append(name)
    return tuple(args)

def get_named_kw_args(fn):
    args=[]
    params=inspect.signature(fn).parameters
    for name,param in params.items():
        if param.kind==inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)

def has_named_kw_args(fn):
    #args=[]
    params=inspect.signature(fn).parameters
    for name,param in params.items():
        if param.kind==inspect.Parameter.KEYWORD_ONLY:
            #args.append(name)
            return True

def has_var_kw_args(fn):
    #args=[]
    params=inspect.signature(fn).parameters
    for name,param in params.items():
        if param.kind==inspect.Parameter.VARWORD_ONLY:
            #args.append(name)
            return True






