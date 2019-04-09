"""
进程池Pool
"""
from multiprocessing import Pool
import os
import time


def fun():
    while True:
        time.sleep(1)
        print('pid %d' % os.getpid())


if __name__ == '__main__':
    print(os.getpid())
    pool = Pool(4)
    # 异步取进程，不会阻塞主进程，
    pool.apply_async(fun)
    pool.apply_async(fun)
    pool.apply_async(fun)
    pool.apply_async(fun)
    pool.apply_async(fun)
    # 同步方式取进程，会阻塞主进程，
    # 必须等上一个进程执行完毕，才能执行下一个进程
    # pool.apply(fun)
    # pool.apply(fun)
    # pool.apply(fun)
    # 当进程池关闭之后就不能再从进程池中取进程，但是池中进程依然在运行
    pool.close()
    time.sleep(2)
    pool.terminate()
    # pool.apply_async(fun)
    # 阻塞主进程，当进程池中进程执行完毕后，打印finish，
    # 否则若主进程先结束，那么进程池中进程就不能执行了
    pool.join()
    print('finish')









