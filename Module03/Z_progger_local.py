import time
import threading

data = threading.local()


def get():
    print(data.value)


def t1():
    data.value = 111
    print("t1: ", data.value)


def t2():
    data.test = 222
    print("t2: ", data.test)


threading.Thread(target=t1).start()
threading.Thread(target=t2).start()
