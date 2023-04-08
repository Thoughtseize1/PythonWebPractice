import multiprocessing
import time


def test():
    print("Процесс запущен")
    for _ in range(7):
        print(f"{multiprocessing.current_process()}", time.time())
        time.sleep(1)


if __name__ == "__main__":
    prc_list = []
    for i in range(3):
        pr = multiprocessing.Process(target=test, name=f"Pidor - {i}")
        prc_list.append(pr)
        pr.start()
    # МЫ не можем опуститься ниже данной строчки кода пока наш процесс этот не будет завершен!Для теста комментируй эту строку и смотри как меняется вывод.
    for i in prc_list:
        i.join()
    i = 1
    while i <= 3:
        print("La la la - MAIN PROCESS")
        time.sleep(1)
        i += 1
    print("END OF MAIN")
    print("All is end")
    print("All is end")
    print("All is end")
