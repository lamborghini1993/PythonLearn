# -*- coding:utf-8 -*-
'''
@Description: python3类型注解
@Author: lamborghini1993
@Date: 2019-04-11 14:22:14
@UpdateDate: 2019-04-11 15:07:50
'''

from typing import Callable, Dict, List, NewType, Sequence, Tuple, Any


# 1. 函数注解
def Greeting(name: str)->str:
    return "Hello " + name


# 2. 类型别名
VectorF = List[float]
Address = Tuple[str, int]
ConnectionOptions = Dict[str, str]


def Scale(scalar: float, vector: VectorF)->VectorF:
    return [scalar*num for num in vector]


# 3.NewType
# UserID = NewType("UserID", int)
# print(UserID, type(UserID))
# for x in range(10):
#     idT = UserID(x+10)
#     print(idT, type(idT))


# 4.Callable
# 期望特定签名的回调函数的框架可以将类型标注为 Callable[[Arg1Type, Arg2Type], ReturnType]
# def GetNextItem(a: int, b: int)->int:
#     return a+b


# def Feeder(GetNextItemTmp: Callable[[int, int], int])->int:
#     return GetNextItemTmp(1, 2)


# print(Feeder(GetNextItem))


# 5. Any
def GetValue(sKey: str)->Any:
    return None
