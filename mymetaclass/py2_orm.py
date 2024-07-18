# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-09 20:15:22
@UpdateDate: 2019-09-10 14:07:37
@Description: 使用元类定义一个ORM模型
    https://www.liaoxuefeng.com/wiki/897692888725344/923030550637312
'''


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping:%s==>%s" % (k, v))
                mappings[k] = v
        for k in mappings:
            attrs.pop(k)
        attrs["__table__"] = name
        attrs["__mappings__"] = mappings
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Model object has not attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = "insert into %s(%s) values (%s)" % (self.__table__, ",".join(fields), ",".join(params))
        print("SQL:", sql)


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('uid')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


if __name__ == "__main__":
    # 创建一个实例：
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    # 保存到数据库：
    u.save()
