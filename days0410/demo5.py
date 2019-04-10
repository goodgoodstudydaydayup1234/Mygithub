"""
UDP服务端-客户端
"""
import threading
from multiprocessing import Process
import time
import socket


def server1():
    pass


def client1():
    pass


if __name__ == '__main__':
    p1 = Process(target=server1)
    p1.start()
    p2 = Process(target=client1)
    p2.start()
    p1.join()
    p2.join()

    client_info = []
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('192.168.12.167', 60000))
    t3 = threading.Thread(target=recv)
    t3.start()
    t4 = threading.Thread(target=send)
    t4.start()
    t3.join()
    t4.join()

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientsocket.sendto('hello'.encode('utf8'), ADDRES_TO)
    t5 = threading.Thread(target=tsend)
    t5.start()
    t6 = threading.Thread(target=trece)
    t6.start()
    t5.join()
    t6.join()
    print('finish')












