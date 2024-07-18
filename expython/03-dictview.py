def test1():
    d1 = dict(a=1, b=2)
    d2 = dict(b=2, c=3)
    v1 = d1.items()
    v2 = d2.items()
    # print(v1, type(v1))
    print("交集：", v1 & v2)
    print("并集：", v1 | v2)
    print("差集", v1 - v2)  #差集(仅v1有,v2没有的)
    print("对称差集", v1 ^ v2) # 对称差集 (不会同时出现在 v1 和 v2 中)


if __name__ == "__main__":
    test1()
