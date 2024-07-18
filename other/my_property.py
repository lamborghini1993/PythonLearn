# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-06-04 15:40:53
@Description: 
'''

from typing import Optional, Callable, Any


# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         if age < 18:
#             print('年龄必须大于18岁')
#             return
#         self.__age = age
#         return self.__age


class Person(object):
    """等同于上面"""

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 18:
            print('年龄必须大于18岁')
            return
        self.__age = age
        return self.__age

    age = property(get_age, set_age)


# man = Person("xh", 18)
# man.age = 16
# print(man.age)


class MyProperty:
    def __init__(self, fget: Optional[Callable[[Any], Any]] = ...,
                 fset: Optional[Callable[[Any, Any], None]] = ...,
                 fdel: Optional[Callable[[Any], None]] = ...,
                 doc: Optional[str] = ...) -> None:
        self.__fget = fget
        self.__fset = fset
        self.__fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.__fget is None:
            raise AttributeError("unreadable attribute")
        return self.__fget(obj)

    def __set__(self, obj, value):
        if self.__fset is None:
            raise AttributeError("can't set attribute")
        self.__fset(obj, value)

    def __delete__(self, obj):
        if self.__fdel is None:
            raise AttributeError("can't delete attribute")
        self.__fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.__fset, self.__fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.__fget, fset, self.__fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.__fget, self.__fset, fdel, self.__doc__)


# class Test:
#     def __init__(self):
#         self.__value = 0

#     @MyProperty
#     def A(self):
#         return self.__value

#     @A.setter
#     def A(self, v):
#         self.__value = v


class Test:
    def __init__(self):
        self.__value = 0

    def getA(self):
        return self.__value

    def setA(self, v):
        self.__value = v

    A = MyProperty(getA, setA)


t = Test()
t.A = 1
print(t.A)
