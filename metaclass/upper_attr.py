# -*- coding:utf-8 -*-
# Author: xiaohao@corp.netease.com
# Date: 2022-04-22 14:48:55
"""
https://www.cnblogs.com/ajianbeyourself/p/4052084.html

将一个类的属性全部转为大写（以__开头的属性除外）
"""

import six


class UpperAttrMetaClass(type):
    def __new__(cls, clsname, bases, attrs):
        print("UpperAttrMetaClass", cls, clsname, bases, attrs)

        uppercase_attr = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                uppercase_attr[name] = val
            else:
                uppercase_attr[name.upper()] = val

        return super(UpperAttrMetaClass, cls).__new__(cls, clsname, bases, uppercase_attr)


pp = six.with_metaclass(UpperAttrMetaClass)
print(pp)

class Foo(pp):
    bar = "bip"

    def test(self):
        print("Foo test")


print(dir(Foo))
print(hasattr(Foo, "bar"))
print(hasattr(Foo, "BAR"))
print(hasattr(Foo, "test"))
print(hasattr(Foo, "TEST"))
foo = Foo()
foo.TEST()
print(dir(foo))
