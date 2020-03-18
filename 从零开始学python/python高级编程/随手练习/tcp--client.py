'''
@Author: your name
@Date: 2020-03-18 11:40:39
@LastEditTime: 2020-03-18 14:38:33
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\从零开始学python\python高级编程\随手练习\tcp--client.py
'''
import socket

def main():

    # 1. 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器
    server_ip = input("请输入要链接的服务器ip:")
    server_port = int(input("请输入要链接的端口port："))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)

    # 3. 发送数据/接收数据
    send_data = input("请输入要发送的数据：")
    tcp_socket.send(send_data.encode("utf-8"))

    # 4. 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()