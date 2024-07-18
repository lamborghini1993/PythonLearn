# -*- coding:utf-8 -*-
'''
@Description: 对称加密
@Author: lamborghini1993
@Date: 2019-06-23 22:09:17
@UpdateDate: 2019-06-25 23:40:45
'''

import os
import platform
import pubfun

CODING = "utf-8"
if platform.system() == "Linux":
    DIR = "/home/duoyi/test"
else:
    DIR = "F:\\MyLove"
OLD_DIR = os.path.join(DIR, "old")
NEW_DIR = os.path.join(DIR, "new")
MD5FILE = "md5.yaml"
FILE_TREE = "tree.yaml"


class CEncry:
    def __init__(self):
        self.m_MD5Info = pubfun.Load4Yaml(MD5FILE)
        self.m_TreeInfo = pubfun.Load4Yaml(FILE_TREE)

    def Start(self):
        self.DFSOld2New(OLD_DIR, NEW_DIR, self.m_TreeInfo)
        pubfun.Save2Yaml(MD5FILE, self.m_MD5Info)
        pubfun.Save2Yaml(FILE_TREE, self.m_TreeInfo)

    def DFSOld2New(self, sOldDir: str, sNewDir: str, dTreeInfo: dict):
        for filename in os.listdir(sOldDir):
            sOldFile = os.path.join(sOldDir, filename)

            if os.path.isfile(sOldFile):
                print(f"<< {sOldFile}")
                oldmd5 = self.m_MD5Info.get(sOldFile, "")
                nowmd5 = pubfun.GetFileMd5(sOldFile)
                sNewFile = os.path.join(sNewDir, nowmd5 + ".7z")
                dTreeInfo[nowmd5] = filename
                if oldmd5 == nowmd5 and os.path.exists(sNewFile):
                    print("\t已存在")
                    continue
                sPassword = nowmd5[:4] + "1q!Q"
                self.Encryp(sOldFile, sNewFile, sPassword)
                self.m_MD5Info[sOldFile] = nowmd5
                continue

            sNewFile = os.path.join(sNewDir, filename)
            if not os.path.exists(sNewFile):
                os.makedirs(sNewFile)

            self.DFSOld2New(sOldFile, sNewFile, dTreeInfo.setdefault(filename, {}))

    def Encryp1(self, sOldFile, sNewFile):
        """第一种处理方法：
        1. 复制文件并重命名为对应16进制名
        2. 修改md5值
        3. 添加到压缩包+密码
        """
        pubfun.ChangeMd5(sOldFile, sNewFile)
        pubfun.Zip(sNewFile)

    def Encryp2(self):
        """第二种处理方法：
        添加到压缩包+密码
        """

    def Encryp3(self):
        """第三种处理方法：
        Hex重命名+修改md5值
        """

    def Encryp(self, oldfile: str, newfile: str, sPassword: str):
        """第三种处理方法：
        7zip对压缩包和文件名进行加密
        zip的文件名为Hex名
        """
        import subprocess
        # cmd = "\"D:\\7-Zip\\7z.exe\" a \"%s\" -p1234 -mhe \"%s\"" % (newfile, oldfile)

        pi = subprocess.Popen(["D:\\7-Zip\\7z.exe", "a", newfile, f"-p{sPassword}", "-mhe", oldfile], shell=True, stdout=subprocess.PIPE)
        result = pi.communicate()[0].decode("gbk")
        msg = "压缩成功" if "Everything is Ok" in result else "<<压缩失败>>.."
        print("\t" + msg)


if __name__ == "__main__":
    CEncry().Start()
