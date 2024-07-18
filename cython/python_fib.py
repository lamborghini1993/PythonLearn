# -*- coding:utf-8 -*-
'''
@Description: 纯python代码
@Author: lamborghini1993
@Date: 2019-09-09 11:33:39
@UpdateDate: 2019-09-09 11:36:35
'''

import time


def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    t1 = time.time()
    print(fib(40))
    print("总共花费时间%s秒" % (time.time() - t1))
