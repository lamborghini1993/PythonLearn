# -*- coding:utf-8 -*-
'''
@Description: profiler性能测试
@Author: lamborghini1993
@Date: 2019-04-23 16:36:27
@UpdateDate: 2019-05-17 13:35:46
'''

import cProfile
import os
import pstats
import time

from pyprof2calltree import convert, visualize

g_Profile = None
g_State = False

PROFILER_DIR = "Cache"


def StartProState():
    global g_State, g_Profile
    if g_State:
        return
    g_State = True
    g_Profile = cProfile.Profile()
    g_Profile.enable()


def EndProState():
    global g_State, g_Profile
    if not g_Profile:
        return
    g_State = False
    g_Profile.disable()
    if not os.path.isdir(PROFILER_DIR):
        os.mkdir(PROFILER_DIR)
    sTime = "%04d-%02d-%02d_%02d-%02d-%02d" % (time.localtime()[:6])
    sPath = os.path.join(PROFILER_DIR, sTime)
    TxtProfile(sPath, 1000, "time")
    ViewProfile(sPath)
    g_Profile = None


def TxtProfile(path: str, entryCnt: int, *orderNames):
    """打印profile信息到文件中
    Arguments:
        path {str} -- 文件路径
        entryCnt {int} -- 打印的行数
    """
    global g_Profile
    path += ".txt"
    with open(path, "wt") as f:
        st = pstats.Stats(g_Profile, stream=f)
        st.strip_dirs().sort_stats(*orderNames).print_stats(entryCnt)


def ViewProfile(path: str):
    """生成QCacheGrind可视化的文件
    Arguments:
        path {str} -- 保存路径
    """
    global g_Profile
    path += ".view"
    # visualize(g_Profile.getstats())
    convert(g_Profile.getstats(), path)


def Dump(path: str):
    global g_Profile
    if g_Profile:
        g_Profile.dump_stats(path)


def TestProfile():
    iCnt = 0
    for x in range(10000):
        iCnt += x
    print(iCnt)


if __name__ == "__main__":
    StartProState()
    TestProfile()
    EndProState()
