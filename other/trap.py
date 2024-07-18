# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-09 20:15:09
@UpdateDate: 2019-09-29 13:40:51
@Description: python中遇到的槽点（坑）
'''

def test1_append_to(element, to=[]):
    to.append(element)
    return to


def test1():
    print(test1_append_to(11))
    print(test1_append_to(22))


# def test2_create():
#     """
#     这是因为 i 是在闭包的作用域（demo 函数的外层作用域），而 Python 的闭包是迟绑定 ，
#     这意味着闭包中用到的变量的值，是在内部函数被调用时查询得到的；
#     """
#     a = []
#     for i in range(4):
#         def demo(x):
#             return x * i
#         a.append(demo)
#     return a


def test2_create():
    """主动早绑定"""
    a = []
    for i in range(4):
        def demo(x, i=i):
            return x * i
        a.append(demo)
    return a


def test2():
    for demo in test2_create():
        print(demo(2))


if __name__ == "__main__":
    # test1()
    test2()
