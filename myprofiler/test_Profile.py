# -*- coding:utf-8 -*-
'''
@Description: 性能分析
    需要库: pip install line_profiler   性能分析
        python3 -m line_profiler test_lineProfile.py
    需要库: pip install memory_profiler 内存分析
        python3 -m memory_profiler test_lineProfile.py
@Author: lamborghini1993
@Date: 2019-04-22 16:06:41
@UpdateDate: 2019-04-22 21:19:10
'''


def sum_num(max_num):
    total = 0
    for i in range(max_num):
        total += i
    return total


@profile
def test():
    total = 0
    for i in range(40000):
        total += i
    t1 = sum_num(100000)
    t2 = sum_num(200000)
    t3 = sum_num(300000)
    t4 = sum_num(400000)
    t5 = sum_num(500000)
    test2()
    return total


def test2():
    total = 0
    for i in range(40000):
        total += i

    t6 = sum_num(600000)
    t7 = sum_num(700000)

    return total


if __name__ == "__main__":
    test()
