# -*- coding:utf-8 -*-
'''
@Description: 测试那种对称加密
@Author: lamborghini1993
@Date: 2019-06-23 22:09:17
@UpdateDate: 2019-06-25 21:21:30

加密方法：
1. pyminizip.compress(scr, "", zipname, "123", 5)
        https://github.com/smihica/pyminizip
2. zip命令 
        https://blog.51cto.com/no001/547862
3. 7zip命令
        7z a dstfile.7z -pxxxx -mhe srcfile
'''

import binascii
import glob
import os

from cryptography.fernet import Fernet

import pubfun


def MyPrint(*args):
    for txt in args:
        print(f"{txt},type:{type(txt)},len:{len(txt)}")


Sample = "如果特人个人或个人和.mp4"      # 14
Byte = Sample.encode("utf-8")         # 34


def Test1():
    s1 = binascii.b2a_hex(Byte)        # 68
    s2 = binascii.b2a_base64(Byte)     # 49
    s3 = s2.decode("utf-8")
    MyPrint(Sample, Byte, s1, s2, s3)


def Test2():
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(Byte)         # 140
    s1 = f.decrypt(token).decode("utf-8")
    MyPrint(Sample, key, token, s1)


def PrintAllMd5():
    sDir = r"F:\MyLove\old"
    for sFile in os.listdir(sDir):
        sFullFile = os.path.join(sDir, sFile)
        print(sFile, pubfun.GetFileMd5(sFullFile))


def test():
    dirname = r'C:\Users\XXXX\Desktop\New folder'
    allFile = glob.glob(dirname + os.sep + '*.mp4')
    for filename in allFile:
        pubfun.ChangeMd5(filename, filename + "_cp")
        print(filename + 'is Changed.')


def TestPyminizip():
    import pyminizip
    scrpath = "start.bat"
    zipname = "start.zip"
    scr = "/home/duoyi/mygit/MyCode/python3/resource_encryp/start.bat"
    pyminizip.compress(scr, "", zipname, "123", 5)


if __name__ == "__main__":
    TestPyminizip()
