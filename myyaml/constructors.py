# -*- coding:utf-8 -*-
'''
@Description: yaml构造器
@Author: lamborghini1993
@Date: 2019-05-31 11:26:29
@UpdateDate: 2019-05-31 13:31:02
'''

import yaml

CACHE_YAML = "Cache/yaml.yaml"


class Person(yaml.YAMLObject):
    yaml_tag = "!person"    # 标记位

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "%s(name=%s,age=%d)" % (self.__class__.__name__, self.name, self.age)


james = Person("James", 20)
with open(CACHE_YAML, "w") as f:
    print(yaml.dump(james, f, default_flow_style=False)) # Python对象实例转为yaml

lily = yaml.load("!person {name: Lily, age: 19}")   # yaml转为Python对象实例,注意这里需要加空格
print(lily)
