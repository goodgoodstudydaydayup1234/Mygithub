"""
TCP客户端实现
"""
# 1.引入模块
from socket import *
import threading


def tsend2(client2):
    while True:
        msg = input('请输入要发送的消息：')
        if not client2._closed:
            client2.send(msg.encode('utf8'))
        else:
            # 客户端已关闭，断开连接
            print('连接已断开')
            break


def trecv2(BUFFERSIZE, client2):
    while True:
        msg1 = client2.recv(BUFFERSIZE)
        if len(msg1) > 0:
            print('收到来自%s的消息：%s' % (60000, msg1.decode('utf8')))
            with open('tcp_client.txt', 'ab', ) as f:
                f.write(msg1)
        else:
            # 当收到消息长度为0，则可能服务端已经断开，此时关闭客户端
            client2.close()
            break


if __name__ == '__main__':
    BUFFERSIZE = 1024
    # 2.创建客户端套接字
    client2 = socket(AF_INET, SOCK_STREAM)
    send_addr = ('192.168.12.167', 60000)
    # 3.创建连接
    client2.connect(send_addr)
    # 4.发送消息
    ts2 = threading.Thread(target=tsend2, args=(client2,))
    ts2.start()
    # 5.接收消息
    tr2 = threading.Thread(target=trecv2, args=(BUFFERSIZE, client2))
    tr2.start()
    ts2.join()
    tr2.join()
    # 6.关闭
    # client2.close()











