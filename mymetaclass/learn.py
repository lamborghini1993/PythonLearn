def test1():
    Foo = type("Foo", (), {})

    # class Foo:
    #     pass

    print(Foo())

    Bar = type("Bar", (Foo,), {
        "attr": 100,
        "attr_val": lambda x: x.attr
    })

    # class Bar(Foo):
    #     attr = 100
    #     def attr_val(self):
    #         return self.attr

    obj = Bar()
    print(obj, obj.attr, obj.attr_val())


def test2():
    def f(obj):
        print(f"attr={obj.attr}")

    Foo = type("Foo", (), {
        "attr": 100,
        "attr_val": f,
    })
    obj = Foo()
    print(obj, obj.attr, obj.attr_val())


def test3():
    def new(cls):
        x = object.__new__(cls)
        x.attr = 100
        return x

    class Foo:
        pass
    
    Foo.__new__ = new
    f = Foo()
    print(f.attr)


if __name__ == "__main__":
    # test1()
    # test2()
    test3()
