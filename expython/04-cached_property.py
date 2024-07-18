import time

from cached_property import cached_property


class CTest1:
    def __init__(self):
        self.num = 10

    @cached_property
    def test(self):
        time.sleep(3)
        self.num += 10
        return self.num


def Test1():
    obj = CTest1()
    for _ in range(10):
        begin = time.time()
        print(obj.test, f"耗时{time.time()-begin}秒")


class my_cached_property:
    def __init__(self, func, name=None, doc=None):
        self.__name__ = name
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, None)
        if value is None:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value


class CTest2:
    def __init__(self):
        self.num = 10

    @my_cached_property
    def test(self):
        time.sleep(3)
        self.num += 10
        return self.num


def Test2():
    obj = CTest2()
    for _ in range(10):
        begin = time.time()
        print(obj.test, f"耗时{time.time()-begin}秒")


if __name__ == "__main__":
    # Test1()
    Test2()
