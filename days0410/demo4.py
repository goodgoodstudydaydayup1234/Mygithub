"""
UDP服务端
"""
import socket
import threading
import time


def recv():
    while True:
        time.sleep(1)
        cont, info =server_socket.recvfrom(1024)
        print(cont.decode('utf8'), info)
        client_info.append(info)
        # client_info[0] = info
        # print(client_info)


def send():
    while True:
        send_content = input('请输入发送内容：')
        server_socket.sendto(send_content.encode('utf8'), (client_info[-1]))


if __name__ == '__main__':
    client_info = []
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('192.168.12.167', 60000))
    t1 = threading.Thread(target=recv)
    t1.start()
    t2 = threading.Thread(target=send)
    t2.start()
    t1.join()
    t2.join()
    print('finish')








