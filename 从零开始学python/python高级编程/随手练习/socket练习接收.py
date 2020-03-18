'''
@Author: your name
@Date: 2020-03-17 23:36:45
@LastEditTime: 2020-03-18 09:53:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\从零开始学python\python高级编程\随手练习\socket练习接收.py
'''
import socket

def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定端口
    local_addr = ("", 7890)
    udp_socket.bind(local_addr)

    # 3. 接收数据
    recv_data = udp_socket.recvfrom(1024)  # 1024表示接受的最大数据
    recv_msg = recv_data[0]  # 因为接收到的是一个元组（"内容", （发送方的ip, 发送方的端口））
    recv_addr = recv_data[1]

    # 4. 打印内容
    print("%s:%s" % (str(recv_addr), recv_msg.decode("utf-8")))

    # 5. 关闭套接字
    udp_socket.close()

    # 6. 显示执行过了
    print("已经执行过了接收")

# 测试函数
if __name__ == "__main__":
    main()
    pass