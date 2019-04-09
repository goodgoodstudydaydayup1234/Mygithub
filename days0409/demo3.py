"""
线程方法
"""
import threading
import time


def fun(args):
    time.sleep(0.5)
    print(threading.enumerate())
    print('hello', threading.current_thread().name)
    print(args)


def main():
    print(threading.current_thread().name)

    list1 = []
    for i in range(5):
        t = threading.Thread(target=fun, args=(3,), name='MyThread-'+str(i))
        t.start()
        list1.append(t)
    for i in list1:
        i.join()


if __name__ == '__main__':
    main()


