# -*- coding:utf-8 -*-
'''
@Description: 测试super和cls的区别
@Author: lamborghini1993
@Date: 2019-03-13 13:14:40
@UpdateDate: 2019-03-13 20:31:32
'''


class A1:
    def __init__(self):
        super(A1, self).__init__()
        print("A1.__init__")

    def Test(self):
        print("A1.Test")


class B1:
    def __init__(self):
        super(B1, self).__init__()
        print("B1.__init__")

    def Test(self):
        print("B1.Test")


class C1(A1, B1):
    """
    父类__init__中有super
    """

    def __init__(self):
        super(C1, self).__init__()
        print("C1.__init__")

    def Test(self):
        """
        macro顺序为: C1 A1 B1 object
        super方式无法调用B.Test
        """
        super(C1, self).Test()
        print("C1.Test")


###############################################################################


class A2(object):
    def __init__(self):
        print("A2.__init__")

    def Test(self):
        print("A2.Test")


class B2:
    def __init__(self):
        print("B2.__init__")

    def Test(self):
        print("B2.Test")


class C2(A2, B2):
    """
    父类__init__中无super
    """

    def __init__(self):
        super(C2, self).__init__()
        print("C2.__init__")

    def Test(self):
        """
        macro顺序为: C2 A2 B2 object
        super方式无法调用B.Test
        """
        super(C2, self).Test()
        print("C2.Test")


###############################################################################

class AA(object):
    def __init__(self):
        print("AA.__init__")

    def Test(self):
        print("AA.Test")


class BB:
    def __init__(self):
        print("BB.__init__")

    def Test(self):
        print("BB.Test")


class CC(AA, BB):
    def __init__(self):
        AA.__init__(self)
        BB.__init__(self)
        print("CC.__init__")

    def Test(self):
        AA.Test(self)
        BB.Test(self)
        print("CC.Test")


if __name__ == "__main__":
    C1().Test()
    print(C1.mro())
    print("-" * 50)
    C2().Test()
    print(C2.mro())
    print("-" * 50)
    CC().Test()
    print(CC.mro())
