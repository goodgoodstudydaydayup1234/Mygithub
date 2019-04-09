"""
多进程
"""
import os
import time
from multiprocessing import Process


def p1process():
    while True:
        time.sleep(1)
        print('p1执行了', os.getpid())


def p2process():
    while True:
        time.sleep(1)
        print('p2执行了', os.getpid())


def main():
    p1 = Process(target=p1process, name='p1')
    p1.start()
    print('p1进程的名字：', p1.name)
    # p1.join()
    p1.terminate()
    p2 = Process(target=p2process)
    p2.start()
    print(p1.is_alive())
    print(p2.is_alive())


if __name__ == '__main__':
    main()












