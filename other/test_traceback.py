# -*- coding:utf-8 -*-
'''
@Description: traceback学习
@Author: lamborghini1993
@Date: 2019-03-14 10:50:35
@UpdateDate: 2019-03-14 11:11:54
'''

import sys
import traceback


def Func1():
    raise NameError("test fun1 NameError")


def Main1():
    try:
        Func1()
    except Exception as e:
        eType, eValue, eObj = sys.exc_info()
        print("type:", eType)
        print("value:", eValue)
        print("traceback obj:", eObj)


def Main2():
    """
    traceback.print_tb(tb[, limit[, file]])
    tb: 这个就是traceback object, 是我们通过sys.exc_info获取到的
    limit: 这个是限制stack trace层级的，如果不设或者为None，就会打印所有层级的stack trace
    file: 这个是设置打印的输出流的，可以为文件，也可以是stdout之类的file-like object。如果不设或为None，则输出到sys.stderr。
    """
    try:
        Func1()
    except Exception as e:
        eType, eValue, eObj = sys.exc_info()
        traceback.print_tb(eObj)


def Main3():
    """
    traceback.print_exception(etype, value, tb[, limit[, file]])
    跟print_tb相比多了两个参数etype和value，分别是exception type和exception value，加上tb(traceback object)，正好是sys.exc_info()返回的三个值
    另外，与print_tb相比，打印信息多了开头的"Traceback (most...)"信息以及最后一行的异常类型和value信息
    还有一个不同是当异常为SyntaxError时，会有"^"来指示语法错误的位置
    """
    try:
        Func1()
    except Exception as e:
        eType, eValue, eObj = sys.exc_info()
        traceback.print_exception(eType, eValue, eObj)


def Main4():
    """
    traceback.print_exc([limit[, file]])
    print_exc是简化版的print_exception, 
    由于exception type, value和traceback object都可以通过sys.exc_info()获取，
    因此print_exc()就自动执行exc_info()来帮助获取这三个参数了，
    也因此这个函数是我们的程序中最常用的，因为它足够简单
    """
    try:
        Func1()
    except Exception as e:
        traceback.print_exc(limit=1, file=sys.stdout)


def Main5():
    """
    traceback.format_exc([limit[, chain]])
    这个也是最常用的一个函数，它跟print_exc用法相同，
    只是不直接打印而是返回了字符串
    """
    try:
        Func1()
    except Exception as e:
        info = traceback.format_exc(limit=2)
        print("--%s--" % info)

def Main6():
    """打印堆栈"""
    traceback.print_stack(file=sys.stdout)


if __name__ == '__main__':
    print("------------------begin--------------------")
    Main6()
    print("------------------end--------------------")
