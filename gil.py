import threading
import dis

n = 0
N = 10000000


def add():
    global n
    for i in range(N):
        n = n + 1


def sub():
    global n
    for i in range(N - 10):
        n -= 1


print(dis.dis(add))
print(dis.dis(sub))

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=sub)

t1.start()
t2.start()

t1.join()
t2.join()
print("n:", n)

# python2 和 python3.6 n结果不定，python3.12 结果固定