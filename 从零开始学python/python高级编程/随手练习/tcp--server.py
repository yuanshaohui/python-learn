'''
@Author: your name
@Date: 2020-03-18 14:38:52
@LastEditTime: 2020-03-18 15:58:22
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\从零开始学python\python高级编程\随手练习\tcp--server.py
'''
import socket


def main():
    """创建服务器"""


    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定ip和端口
    tcp_socket.bind(("192.168.0.1", 7788))

    # 让默认的套接字主动变被动listen
    tcp_socket.listen(128)

    while True:  # 循环为多个客户端服务

        # 等待客户端的链接accept(返回的为一个元组，进行拆包处理)
        new_socket, client_addr = tcp_socket.accept()

        while True:  # 循环为一个客户端服务

            # 接收客户端发来的请求
            recv_data = new_socket.recv(1024)
            print("客户端发来的数据：%s", recv_data.decode("utf-8"))

            # 判断对方是否close关闭
            if not recv_data:
                break

            else:
                # 回复请求
                new_socket.send("已经接收到你的请求，正在处理".encode("utf-8"))

        # 关闭套接字
        new_socket.close()
    
    tcp_socket.close()


if __name__ == "__main__":
    main()