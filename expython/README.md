# Python高级编程

- [知乎](https://zhuanlan.zhihu.com/p/33517855?utm_medium=social&utm_source=qq)
- [ppt](http://dongweiming.github.io/Expert-Python/)

# 包的构建

如果包里有一些模块不想被import * 这样引用，可以用 __all__ 把允许被引用的放进去；

```__all__ = ["add", "x"]```

# __slots__

限制给类实例绑定属性，大量属性时减少内存占用