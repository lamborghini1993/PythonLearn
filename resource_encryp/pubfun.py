# -*- coding:utf-8 -*-
'''
@Description: 通用函数
@Author: lamborghini1993
@Date: 2019-06-23 21:42:33
@UpdateDate: 2019-06-25 23:16:18
'''

import binascii
import hashlib
import json
import os
import shutil
import time
import zipfile

import yaml


def MyPrint(*args):
    for txt in args:
        print(f"{txt},type:{type(txt)},len:{len(txt)}")


def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


def ChangeMd5(oldfile: str, newfile: str):
    shutil.copyfile(oldfile, newfile)
    with open(newfile, "a") as f:
        f.write("####%s####" % time.time())
    print(f"\tmd5 has changed.")


def Str2Hex(sTxt: str, coding="utf-8")->str:
    bTxt = sTxt.encode(coding)
    bHex = binascii.b2a_hex(bTxt)
    sHex = bHex.decode(coding)
    return sHex


def Hex2Str(sHex: str, coding="utf-8")->str:
    bTxt = binascii.a2b_hex(sHex)
    sTxt = bTxt.decode(coding)
    return sTxt


def Save2Json(filename: str, dInfo: dict):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(dInfo, f, indent=4)


def Load4Json(filename: str)->dict:
    if not os.path.exists(filename):
        return {}
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def Save2Yaml(filename: str, dInfo: dict):
    with open(filename, "w", encoding="utf-8") as f:
        yaml.dump(dInfo, stream=f, default_flow_style=False, allow_unicode=True)


def Load4Yaml(filename: str)->dict:
    if not os.path.exists(filename):
        return {}
    with open(filename, "r", encoding="utf-8") as f:
        return yaml.load(f)


def Zip(filename: str):
    import pyminizip
    myZip = filename + ".zip"
    textfile = os.path.split(filename)[1]
    password = textfile[:6] + "1!qQ"
    pyminizip.compress(filename, "", myZip, password, 5)
    # os.remove(filename)


def Zip1(filename: str):
    newfile = filename + ".zip"
    bPW = "123456".encode("utf-8")
    zfile = zipfile.ZipFile(newfile, "w", zipfile.ZIP_DEFLATED)
    zfile.extractall(pwd=bPW)
    textfile = os.path.split(filename)[1]
    zfile.write(filename, textfile)
    # password = textfile[:6] + "1!qQ,{"
    # bPass = password.encode("utf-8")
    # zfile.setpassword(bPW)    # ubuntu 密码无效
    zfile.close()
    os.remove(filename)


if __name__ == '__main__':
    pass
