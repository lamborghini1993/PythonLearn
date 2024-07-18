# -*- coding:utf-8 -*-
'''
@Description: 装饰器学习
@Author: lamborghini1993
@Date: 2019-05-28 13:34:30
@UpdateDate: 2019-05-28 14:33:50

https://juejin.im/post/5cec00ae51882533826977bc
'''

import time
from functools import wraps, partial


def logger(func):
    """不带参数的函数装饰器-日志打印"""
    def _wrapper(*args, **kwargs):
        print("start {}".format(func.__name__))
        result = func(*args, **kwargs)
        print("end...")
        return result
    return _wrapper


def decorator1(name: str):
    """带参数的函数装饰器"""
    def _wrapper(func):
        def __wrapper(*args, **kwargs):
            print("start {} flag:{}".format(func.__name__, name))
            return func(*args, **kwargs)
        return __wrapper
    return _wrapper


@logger
@decorator1("test1")
def add(a: int, b: int):
    print("{} + {} = {}".format(a, b, a + b))


class CLogger:
    """不带参数的类装饰器-日志打印"""

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("start {}".format(self.func.__name__))
        result = self.func(*args, **kwargs)
        print("end...")
        return result


class CLogger2:
    """带参数的类装饰器-日志打印"""

    def __init__(self, flag):
        self.flag = flag

    def __call__(self, func):
        def _wrapper(*args, **kwargs):
            print("start {} flag:{}".format(func.__name__, self.flag))
            return func(*args, **kwargs)
        return _wrapper


@CLogger
def multiply(a: int, b: int):
    print("{} * {} = {}".format(a, b, a * b))


@CLogger2("test2")
def minu(a: int, b: int):
    print("{} - {} = {}".format(a, b, a - b))


def warpper1(func):
    def _inner(*args, **kwargs):
        pass
    return _inner


def warpper2(func):
    """
    functools .wraps 装饰器的作用就是:
        将被修饰的函数(wrapped) 的一些属性值赋值给 修饰器函数(wrapper)
        最终让属性的显示更符合我们的直觉。
    """
    @wraps(func)
    def _inner(*args, **kwargs):
        pass
    return _inner


@warpper1
def func_name1():
    pass


@warpper2
@warpper2
def func_name2():
    pass


class CDelay:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"wating for {self.duration} seconds...")
        time.sleep(self.duration)
        return self.func(*args, **kwargs)


def delay(duration):
    return partial(CDelay, duration)


@delay(3)
def division(a: int, b: int):
    print("{} / {} = {}".format(a, b, a / b))


if __name__ == "__main__":
    add(1, 2)   # logger(decorator1("test1")(add)(a,b))
    print("-" * 30)
    multiply(1, 2)
    print("-" * 30)
    minu(1, 2)
    print("-" * 30)
    print(func_name1.__name__)
    print(func_name2.__name__)
    print("-" * 30)
    division(1, 2)
    print(division.func)
