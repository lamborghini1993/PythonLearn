# -*- coding:utf-8 -*-
'''
@Description: 分析pyc文件
@Author: lamborghini1993
@Date: 2020-05-06 20:49:17
@UpdateDate: 2020-05-07 14:13:50
'''

# import py_compile
# py_compile.compile("sample.py", "sample.pyc")

import struct
import marshal
import sys
import types
import importlib.util
import importlib._bootstrap_external
import time

with open("sample.pyc", "rb") as f:
    code = f.read()

    # 前四个字节是表示python版本
    magic = code[:4]
    print(importlib.util.MAGIC_NUMBER, magic)

    # 5-8 空字节
    print(struct.unpack("i", code[4:8])[0])

    # 9-12 文件时间戳
    timestamp = code[8:12]
    timestamp = struct.unpack("I", timestamp)[0]
    localtime = time.localtime(timestamp)
    print(timestamp, localtime, time.strftime("%Y-%m-%d %H:%M:%S", localtime))

    # 13-16 文件大小
    size = struct.unpack("I", code[12:16])[0]
    print(size)

    # 从第16个字节开始是一个code对象
    codebyte = code[16:]
    co = marshal.loads(codebyte)    # 变为codeobject对象
    print(co)
    new_module = types.ModuleType("xh")  # 新建一个空模块
    exec(co, new_module.__dict__)   # 将codeobject导入到新模块中
    print(dir(new_module))  # 输出模块内容
    sys.modules["xh"] = new_module  # 添加到系统模块中，支持import
    import xh
    print(xh)
    xh.Sum(20, 30)
