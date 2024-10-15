import socket
import time
import select
import logging
import os

curr_file_name = os.path.splitext(os.path.basename(__file__))[0]  # 获取当前文件名
LOG = logging.getLogger(curr_file_name)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
# Create formatter
formatter = logging.Formatter(
    fmt='[%(asctime)s %(levelname)s](%(name)s) %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# Add formatter to console handler
console_handler.setFormatter(formatter)

LOG.addHandler(console_handler)
LOG.setLevel(logging.INFO)


def server_side():
    """
    socket 服务端代码
    :return:
    """
    # 创建TCP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setblocking(False)  # 设置为非阻塞模式
    # 绑定IP地址和端口号
    server_socket.bind(('localhost', 9090))
    # 监听连接，最多允许5个连接排队
    server_socket.listen(5)
    while True:
        readable, _, _ = select.select([server_socket], [], [], 10)

        if readable:
            # 接受连接
            client_socket, client_address = server_socket.accept()

            while True:
                try:
                    # 接收客户端传送的数据
                    data = client_socket.recv(1024)
                    if not data.strip():
                        break
                    data = data.decode('utf-8')
                    LOG.info(f"Connection_from: {client_address[0]}:{client_address[1]} | recv_data：{data}")

                    # 返回客户端数据
                    send_data = "服务端发送的数据".encode('utf-8')
                    client_socket.sendall(send_data)
                except BlockingIOError:
                    continue
                except Exception as e:
                    logging.error(e)

            # 关闭客户端套接字
            client_socket.close()
        else:
            break


def client_side():
    """
    socket 客户端代码
    :return:
    """
    ti1 = time.time()
    for i in range(5):  # 创建多个客户端
        # 创建TCP套接字
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接服务器
        client_socket.connect(('localhost', 9090))

        for j in range(5):  # 单个客户端模拟多次数据交互
            # 发送数据
            send_data = f"客户端发送的数据_{i}-{j}。".encode('utf-8')
            client_socket.sendall(send_data)
            # 接收数据
            data = client_socket.recv(1024)
            data = data.decode('utf-8')
            print(f"客户端接受数据：{data}")
        # 关闭客户端套接字
        client_socket.close()

    print(f"消耗时间：{time.time() - ti1}")


if __name__ == '__main__':
    server_side()
