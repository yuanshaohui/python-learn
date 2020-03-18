'''
@Author: your name
@Date: 2020-03-17 23:03:45
@LastEditTime: 2020-03-18 09:43:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\从零开始学python\python高级编程\随手练习\socket练习.py
'''
import socket
def main():
    # 创建upd套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    udp_socket.bind(("", 7890))


    while True:
        # 输入的数据
        send_data = input("请输入要发送的数据：")
        

        # 条件跳出
        if send_data == "exit":
            break


        # 可以使用套接字收发数据
        # socket_udp.sendto(b"这是发送的内容", ("ip", ))
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.43.71", 7788))
        

    # 关闭套接字
    udp_socket.close()

    # 显示执行过了
    print("-----已启动-----")


if __name__ == "__main__":
    main()
    pass
