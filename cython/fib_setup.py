# -*- coding:utf-8 -*-
'''
@Description: 
    http://www.zhangdongshengtech.com/article-detials/212
    python fib_setup.py build_ext --inplace
@Author: lamborghini1993
@Date: 2019-09-09 11:37:11
@UpdateDate: 2019-09-09 11:51:44
'''

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("myfib", ["fib.pyx"])]
)
