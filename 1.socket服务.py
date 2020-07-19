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
    data = conn.recv(2048)
    print(data)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n<h1>ok</h1>')
    conn.close()
