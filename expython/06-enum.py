# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-10 15:29:19
@UpdateDate: 2019-09-10 15:32:57
@Description: 枚举
'''

from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Mon, Weekday["Mon"], Weekday(1), Weekday.Mon.value)
for name, member in Weekday.__members__.items():
    print(f"{name} {member} {member.value}")
