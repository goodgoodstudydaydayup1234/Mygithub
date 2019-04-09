"""
进程的封装和继承
"""
from multiprocessing import Process


# class MyProcess(Process):
    # def run(self):
        # print('执行了')


def mainprocess(args, **kwargs):
    print('进程入口')
    print(args)
    print(kwargs)


def main():
    list1 = [1]
    # p1 = MyProcess()
    p1 = Process(target=mainprocess, args=(list1,), kwargs={'name': 'xcy'})
    p1.start()


if __name__ == '__main__':
    main()





