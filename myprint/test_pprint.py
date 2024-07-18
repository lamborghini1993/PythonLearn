# -*- coding:utf-8 -*-
'''
@Description: Python3内置模块之pprint让打印比print更美观
@Author: lamborghini1993
@Date: 2019-05-30 21:16:00
@UpdateDate: 2019-05-30 21:22:03
https://juejin.im/post/5cee8ebb518825332550ce0a
'''

import pprint


def Test1():
    L = [str(i) * 20 for i in range(10)]
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(L)


def Test2():
    L = [str(i) * 20 for i in range(10)]
    pp = pprint.pformat(L, indent=2)    # 将目标对象的格式化表示形式返回为字符串
    print(pp)


if __name__ == "__main__":
    # Test1()
    Test2()
