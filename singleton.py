from typing import Any


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        print("call __new__", cls, args, kwargs)
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, a, b=1) -> None:
        print("call __init__")
        self.a = a
        self.b = b

    def print(self):
        return self.a, self.b


obj1 = Singleton(2, 3)
obj2 = Singleton(12, 13)
# obj1 = Singleton()
# obj2 = Singleton()
print(id(obj1), id(obj2))
print(obj1.print(), obj2.print())

print("-" * 20)


class Singleton2(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        print("call __call__")
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton2, cls).__call__(*args, **kwds)
        return cls._instances[cls]


class cls1(metaclass=Singleton2):

    def __init__(self, a, b=1) -> None:
        print("call __init__")
        self.a = a
        self.b = b

    def print(self):
        return self.a, self.b


c1 = cls1(11, 2)
c2 = cls1(3, 4)
print(id(c1), id(c2))
print(c1.print(), c2.print())
print(cls1._instances)


class cls2(cls1):
    pass

class cls3(metaclass=Singleton2):
    pass

cc1 = cls2(1, 2)
cc2 = cls2(1, 2)

dd1 = cls3()
dd2 = cls3()

print(cls1._instances)
print(cls2._instances)
print(cls3._instances)
print(id(cls1._instances),id(cls2._instances),id(cls3._instances))
