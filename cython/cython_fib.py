# -*- coding:utf-8 -*-
'''
@Description: 使用cython来加速
@Author: lamborghini1993
@Date: 2019-09-09 11:42:30
@UpdateDate: 2019-09-09 11:51:13
'''

import myfib
import time


if __name__ == "__main__":
    t1 = time.time()
    print(myfib.fib(40))
    print("cython总共花费时间%s秒" % (time.time() - t1))
