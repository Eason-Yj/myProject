# socket相关

## 1 socket基本概念

Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在Socket接口后面，对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。

Socket通信是一种常用的进程间通信机制，可以用于跨网络与不同主机上的进程之间通信，也可以在同一台主机上的进程之间进行通信。

在使用Socket通信时，一个进程可以作为服务器端创建一个Socket，并指定一个IP地址和端口号来监听连接请求；另一个进程则可以作为客户端创建一个Socket，指定服务器的IP地址和端口号来发起连接。一旦连接建立，服务器和客户端就可以通过Socket进行数据的发送和接收。

在同一台主机上，进程可以使用特殊的IP地址（如本地回环地址127.0.0.1）和不同的端口号来建立Socket连接，实现进程间的通信。这种方式被称为本地回环通信，可以用于进程之间的协作和数据交换。



## 2 代码示例

- 服务端

``````python
import socket

# 创建TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP地址和端口号
server_socket.bind(('localhost', 9090))
# 监听连接，最多允许5个连接排队
server_socket.listen(5)
while True:
    # 接受连接
    client_socket, client_address = server_socket.accept()

    while True:
        # 接收客户端传送的数据
        data = client_socket.recv(1024)
        data = data.decode('utf-8')
        print(f"'Connection from', {client_address}; 服务端接受数据：{data}")
        if not data.strip():
            break

        # 返回客户端数据
        send_data = "服务端发送的数据".encode('utf-8')
        client_socket.sendall(send_data)

    # 关闭客户端套接字
    client_socket.close()
``````

- 客户端

``````python
import socket

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
``````

