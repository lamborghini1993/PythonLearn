# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2019-05-31 11:00:09
@UpdateDate: 2019-05-31 11:46:20

https://blog.csdn.net/lmj19851117/article/details/78843486

基本规则:
1. 大小写敏感 
2. 使用缩进表示层级关系 
3. 缩进时不允许使用Tab，只允许使用空格 
4. 缩进的空格数目不重要，只要相同层级的元素左对齐即可 
5. # 表示注释，从它开始到行尾都被忽略
'''

import yaml


CACHE_YAML = "Cache/yaml.yaml"


def myprint(x):
    print("-" * 30)
    print("type:", type(x))
    print("value:", x)


def Test1():
    path = "python3/pytest/myyaml/test1.yaml"
    with open(path, "r", encoding="utf-8") as f:
        y = yaml.load(f)
    myprint(y)


def Test2():
    # 这种报错
    path = "python3/pytest/myyaml/test2.yaml"
    with open(path, "r", encoding="utf-8") as f:
        y = yaml.load_all(f)    # generator object
    # myprint(y)
    for data in y:
        print(data)


def Test3():
    f = '''
---
name: James
age: 20
---
name: Lily
age: 19
'''
    y = yaml.load_all(f)
    myprint(y)
    for data in y:
        print(data)


def dump1():
    dInfo = {
        "name": "xiaohao",
        "age": 25,
        "traits": ["ONE_HAND", "ONE_EYE"]
    }
    with open("Cache/yaml.yaml", "w", encoding="utf-8") as f:
        result = yaml.dump(dInfo, stream=f)
        myprint(result)

    # yaml.dump(dInfo, CACHE_YAML)  


def dump2():
    data1 = {"name": "xiao"}
    data2 = {"name": "hao"}
    with open("Cache/yaml.yaml", "w", encoding="utf-8") as f:
        yaml.dump_all([data1, data2], f)


if __name__ == "__main__":
    # Test1()
    # Test2()
    # Test3()

    dump1()
    # dump2()
