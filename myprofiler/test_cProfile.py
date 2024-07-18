# -*- coding:utf-8 -*-
'''
@Description: cProfile测试
@Author: lamborghini1993
@Date: 2019-04-22 15:41:35
@UpdateDate: 2019-04-22 15:42:13
'''


def sum_num(max_num):
    total = 0
    for i in range(max_num):
        total += i
    return total


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
    import cProfile
    # # 直接把分析结果打印到控制台
    # cProfile.run("test()")
    # # 把分析结果保存到文件中
    # cProfile.run("test()", filename="result.out")
    # 增加排序方式
    cProfile.run("test()", filename="result.out", sort="cumulative")
