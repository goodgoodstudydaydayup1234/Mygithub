"""
TCP服务端，可被多个客户端连接
"""
# 1.导入模块
from socket import *
import threading


def srecv(BUFFERSIZE, client):
    while True:
        info = client.recv(BUFFERSIZE)
        if len(info) > 0:
            info1 = info.decode('gbk').split(':')
            to = info1[0]
            msg = info1[1].encode('utf8')
            if to in clientdict.keys():
                clientdict[to].send(msg)
            else:
                client.send('对方已离线'.encode('gbk'))
        else:
            clientdict.pop(str(client.getpeername()[1]))
            print('剩余客户端个数：', len(clientdict))
            break


# def ssend(client):
#     while True:
#         time.sleep(1)
#         cont = input('请输入发送内容：')
#         client.send(cont.encode('utf8'))


def taccept(server, clientdict):
    # 5.等待客户端连接，若没有客户端连接就一直等待，阻塞状态，返回值是客户端
    while True:
        # print(1111)
        client, clientaddr = server.accept()
        clientdict[str(clientaddr[1])] = client
        print(clientdict)
        print('客户端%s' % clientaddr[1], '连接上了服务端')
        print('共连接%s个客户端' % (len(clientdict)))
        # 6.接收消息
        BUFFERSIZE = 1024
        # 开的第二个线程：接收客户端发的消息
        tr = threading.Thread(target=srecv, args=(BUFFERSIZE, client))
        tr.start()


if __name__ == '__main__':
    try:
        clientdict = {}
        # 2.创建套接字对象
        server = socket(AF_INET, SOCK_STREAM)
        server_addr = ('192.168.12.167', 60000)
        # 3.绑定
        server.bind(server_addr)
        # 4.启动监听
        server.listen(4)
        print('启动监听')

        # 开的第一个线程：接收客户端的连接
        ta = threading.Thread(target=taccept, args=(server, clientdict))
        ta.start()

    except Exception as e:
        print(e)












