import threading
import time


def get_data(data, nope):
    while True:
        print(f"[{threading.current_thread().name}] - {data} - {nope}")
        time.sleep(1)


thr = threading.Thread(target=get_data, args=("1", 122), name="thr_Pidor_1")
thr.start()

for i in range(100):
    print(f"{threading.current_thread().name} - {i}")
    time.sleep(1)

    if i % 10 == 0:
        print("Active thread: ", threading.active_count())
        print("Enumerate: ", threading.enumerate())
        print("Thr-Pidor is alive: ", thr.is_alive())
