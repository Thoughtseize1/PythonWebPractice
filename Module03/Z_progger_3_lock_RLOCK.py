import threading
import time


value = 0
locker = threading.RLock()


def inc_value():
    global value
    while True:
        locker.acquire()
        value += 1
        time.sleep(3)
        print(value)
        locker.release()


def inc_value2():
    global value
    while True:
        with locker:
            value += 1
            time.sleep(1)
            print(value)


for _ in range(5):
    threading.Thread(target=inc_value, name="thr_Pidor_1").start()
