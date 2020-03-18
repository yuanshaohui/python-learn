"""
adsf
"""

import socket

def send_msg(udp_socket):
    """构建发送数据函数"""

    # 构建接收者的ip和端口
    ip = input("请输入对方的ip:")
    num = int(input("请输入对方的端口："))
    his_ip = (ip, num)

    # 构建发送数据
    send_data = input("请输入要发送的数据：")

    # 退出聊天
    # if send_data == "exit":
    #     print("-----欢迎下次使用-----")
    #     break

    # 发送数据
    udp_socket.sendto(send_data.encode("utf-8"), his_ip)

def recv_msg(udp_socket):
    """构建接收数据的函数"""

    # 接收回送过来的数据
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():

    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    local_addr = ("", 7788)
    udp_socket.bind(local_addr)


    while True:

        # 发送数据
        send_msg(udp_socket)

        # 接收数据
        recv_msg(udp_socket)


    #关闭套接字
    udp_socket.close()



if __name__ == "__main__":
    main()