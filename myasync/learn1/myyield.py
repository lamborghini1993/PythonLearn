def coroutine_example(name):
    print('start coroutine...name:', name)  # 1.1 start coroutine...name:Zarten
    x = yield name
    print('send值:', x) # 2.1   send值:Zarten
    return 'zhihuID: Zarten'


def grouper2():
    result2 = yield from coroutine_example('Zarten')
    print('result2的值：', result2) # 2.2 result2的值：zhihuID: Zarten
    return result2


def grouper():
    result = yield from grouper2()
    print('result的值：', result)   # 2.3 result的值：zhihuID: Zarten
    return result


def main():
    g = grouper()
    next(g)
    try:
        g.send(10)
    except StopIteration as e:
        print('返回值：', e.value)


if __name__ == '__main__':
    main()
