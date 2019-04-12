"""
UDP客户端
"""
# 1.引入socket模块
import socket
import time
import threading
from threading import Thread
# 2.构造socket对象
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ADDRES_TO = ('192.168.12.167', 60000)
BUFFER_SIZE = 1024
# 3.发送消息
# while True:
#     time.sleep(1)
#     clientsocket.sendto('hello'.encode('utf8'), ADDRES_TO)
# clientsocket.sendto('hello'.encode('utf8'), ADDRES_TO)
# 接收数据
# while True:
#     cont, info = clientsocket.recvfrom(BUFFER_SIZE)
#     print(cont)
#     print(info)


def tsend():
    while True:
        sendport = int(input('请输入要发送的对象：'))
        ADDRES_TO = ('192.168.12.167', sendport)
        time.sleep(2)
        send_content = input('请输入要发送的内容')
        clientsocket.sendto(send_content.encode('utf8'), ADDRES_TO)


def trece():
    BUFFER_SIZE = 1024
    while True:
        cont, info = clientsocket.recvfrom(BUFFER_SIZE)
        # print(cont.decode('utf8'))
        # print(info)
        print('收到%s发来的消息：%s' % (info[1], cont.decode('utf8')))


if __name__ == '__main__':
    # 2.构造socket对象
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientsocket.sendto('hello'.encode('utf8'), ADDRES_TO)
    t1 = Thread(target=tsend)
    t1.start()
    t2 = Thread(target=trece)
    t2.start()
    t1.join()
    t2.join()
    print('finish')








