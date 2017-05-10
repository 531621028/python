#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Michael Liao'
import sys
def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello, Word!')
	elif len(args) == 2:
		print('Hello, %s' % args[1])
	else:
		print('Too many arguments!')
if __name__ == '__main__':
	test()

#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)