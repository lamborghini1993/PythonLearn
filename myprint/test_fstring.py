# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2019-06-03 13:46:37
@UpdateDate: 2019-06-03 14:05:32
https://blog.csdn.net/sunxb10/article/details/81036693
'''

import math


def Test1():
    name = "Xiao Hao"
    print(f"Hello, my name is {name} - {name.lower()}")
    print(f"The result is {24 * 8 + 4}")
    print(f"PI = {math.pi}")


def Test2():
    """-string大括号内所用的引号不能和大括号外的引号定界符冲突"""
    print(f"I am {'Test2-1'}")
    print(f'I am {"Test2-2"}')
    print(f"""He said {"I'm Eric"}""")
    print(f'''He\'ll say {"I'm Eric"}''')

def Test3():
    print(f'|result is {(lambda x: x ** 2 + 1) (2):<+7.2f}|')

if __name__ == "__main__":
    # Test1()
    # Test2()
    Test3()
