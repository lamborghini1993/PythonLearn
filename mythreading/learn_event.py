"""
https://blog.csdn.net/brucewong0516/article/details/84588804
Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态。
isSet(): 当内置标志为True时返回True。
set(): 将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。
clear(): 将标志设为False。
wait([timeout]): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()。
"""

import threading
import time


event = threading.Event()

def func():
    print(f"{threading.current_thread().name} wait for event")
    event.wait()
    print(f"{threading.current_thread().name} recv event")

th1 = threading.Thread(target=func, name="th1")
th2 = threading.Thread(target=func, name="th2")

th1.start()
th2.start()

time.sleep(2)

print("MainThread set event")
event.set()

