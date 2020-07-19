import socket
import time

# 创建对象
sk = socket.socket()

# 绑定IP端口
sk.bind(('127.0.0.1', 8000))

# 监听
sk.listen()

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 持续等待链接
while True:
    conn, addr = sk.accept()
    data = conn.recv(2048).decode("UTF-8")
    url = data.split()[1]
    print(url)
    # 头文件
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    if url == "/rihan":
        conn.send(b"<h1>rrrrrrr</h1>")
    elif url == "/oumei":
        conn.send(b"<h1>hhhhhhh</h1>")
    else:
        conn.send(b"<h1>404 not found</h1>")

    # 断开链接
    conn.close()
