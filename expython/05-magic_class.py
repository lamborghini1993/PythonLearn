# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-10 14:32:16
@UpdateDate: 2019-09-10 15:06:24
@Description: 魔改类(定制类)
    https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904
'''


class Student:
    """
    __str__()返回用户看到的字符串，print打印
    __repr__()返回程序开发者看到的字符串，调试服务
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        """重定义打印输出"""
        return f"Student object (name: {self.name})"

    __repr__ = __str__

    def __getattr__(self, attr: str):
        """在没有找到属性的情况下，会调用__getattr__"""
        if attr == "age":
            return 18
        return "Default"


# obj = Student("xiaohao")
# print(obj, obj.name, obj.age, obj.other, sep="\n")


class Fib:
    """
    如果一个类想被用于for ... in循环，类似list或tuple那样，
    就必须实现一个__iter__()方法，该方法返回一个迭代对象，
    然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
    直到遇到StopIteration错误时退出循环。
    """

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        """支持下标取数"""
        if isinstance(n, int):   # n是索引
            a, b = 1, 1
            for _ in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# f = Fib()

# for i in f:
#     print(i, end=" ")
# print()

# print(f[0], f[1], f[2], f[3], f[4], f[5])
# print(f[:9])


class Chain:
    """url链式调用"""

    def __init__(self, path="/root"):
        self._path = path

    def __getattr__(self, path: str)->str:
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, name):
        return Chain("%s/%s" % (self._path, name))


root = Chain()
print(root.status.user.list)
print(root.users('michael').repos)
