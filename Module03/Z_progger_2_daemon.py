import threading
import time


def get_data(data):
    for i in range(5):
        print(f"[{threading.current_thread().name}] - {data} - {i}")
        time.sleep(1)


thr = threading.Thread(target=get_data, args=("PIDOR",), name="POTOK")
thr.daemon = True
thr.start()
for i in range(10):
    print("_____")
